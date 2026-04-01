"""
train.py
--------
Training script for the dog-breed classification model.

Usage
-----
    python -m model.train --images_dir path/to/images/Images

The script performs two-phase transfer learning:
  1. Warm-up  – only the new classification head is trained (base frozen).
  2. Fine-tune – the top layers of EfficientNetB0 are unfrozen and trained
                 at a much lower learning rate.

Trained model weights and class names are saved under ``saved_model/``.
"""

from __future__ import annotations

import argparse
import os
import pathlib

import tensorflow as tf
from tensorflow import keras

from data.dataset_loader import build_dataset, save_class_names
from model.model_config import (
    BATCH_SIZE,
    DEFAULT_CLASS_NAMES_PATH,
    DEFAULT_MODEL_PATH,
    DROPOUT_RATE,
    FINE_TUNE_AT_LAYER,
    FINE_TUNE_EPOCHS,
    FINE_TUNE_LEARNING_RATE,
    IMAGE_SIZE,
    INITIAL_LEARNING_RATE,
    NUM_CLASSES,
    VALIDATION_SPLIT,
    WARMUP_EPOCHS,
)


def build_model(num_classes: int = NUM_CLASSES) -> keras.Model:
    """
    Build the transfer-learning model using EfficientNetB0 as the base.

    Architecture
    ------------
    EfficientNetB0 (ImageNet weights, top removed)
        → GlobalAveragePooling2D
        → BatchNormalization
        → Dropout
        → Dense(num_classes, softmax)

    The base model is frozen during initial training (warm-up phase).
    """
    # Load pre-trained base model
    base_model = keras.applications.EfficientNetB0(
        include_top=False,
        weights="imagenet",
        input_shape=(*IMAGE_SIZE, 3),
    )
    base_model.trainable = False  # Freeze during warm-up

    # Build classifier head
    inputs = keras.Input(shape=(*IMAGE_SIZE, 3))
    # Note: EfficientNet preprocessing (pixel scaling) is applied externally
    # in utils/preprocess.py before images are passed to this model.
    x = base_model(inputs, training=False)
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Dropout(DROPOUT_RATE)(x)
    outputs = keras.layers.Dense(num_classes, activation="softmax")(x)

    model = keras.Model(inputs, outputs)
    return model


def compile_model(
    model: keras.Model,
    learning_rate: float = INITIAL_LEARNING_RATE,
) -> None:
    """Compile *model* in place with Adam and sparse categorical cross-entropy."""
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )


def unfreeze_top_layers(model: keras.Model, fine_tune_at: int = FINE_TUNE_AT_LAYER) -> None:
    """
    Unfreeze layers of the base EfficientNetB0 starting from *fine_tune_at*.

    Called between the warm-up and fine-tuning phases.
    """
    base_model = model.layers[1]  # second layer is the base model
    base_model.trainable = True

    for layer in base_model.layers[:fine_tune_at]:
        layer.trainable = False

    print(
        f"Fine-tuning: {sum(1 for l in base_model.layers if l.trainable)} / "
        f"{len(base_model.layers)} base-model layers are now trainable."
    )


def train(images_dir: str) -> None:
    """
    Full two-phase training pipeline.

    Parameters
    ----------
    images_dir:
        Path to the ``images/Images`` directory of the Stanford Dogs Dataset.
    """
    print(f"Loading dataset from: {images_dir}")
    train_ds, val_ds, class_names = build_dataset(
        images_dir,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        validation_split=VALIDATION_SPLIT,
    )
    num_classes = len(class_names)
    print(f"Found {num_classes} breed classes.")

    # ── Phase 1: Warm-up ──────────────────────────────────────────────────
    print("\n=== Phase 1: Warm-up (head only) ===")
    model = build_model(num_classes=num_classes)
    compile_model(model, learning_rate=INITIAL_LEARNING_RATE)
    model.summary()

    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor="val_accuracy", patience=5, restore_best_weights=True
        ),
        keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.5, patience=3, min_lr=1e-7
        ),
    ]

    model.fit(
        train_ds,
        epochs=WARMUP_EPOCHS,
        validation_data=val_ds,
        callbacks=callbacks,
    )

    # ── Phase 2: Fine-tuning ──────────────────────────────────────────────
    print("\n=== Phase 2: Fine-tuning (top base-model layers) ===")
    unfreeze_top_layers(model, fine_tune_at=FINE_TUNE_AT_LAYER)
    compile_model(model, learning_rate=FINE_TUNE_LEARNING_RATE)

    model.fit(
        train_ds,
        epochs=FINE_TUNE_EPOCHS,
        validation_data=val_ds,
        callbacks=callbacks,
    )

    # ── Save artefacts ────────────────────────────────────────────────────
    model_path = pathlib.Path(DEFAULT_MODEL_PATH)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    model.save(str(model_path))
    print(f"\nModel saved to {model_path}")

    save_class_names(class_names, DEFAULT_CLASS_NAMES_PATH)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Train the dog-breed identification model."
    )
    parser.add_argument(
        "--images_dir",
        required=True,
        help=(
            "Path to the 'images/Images' directory of the Stanford Dogs Dataset. "
            "Download from https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset"
        ),
    )
    args = parser.parse_args()
    train(args.images_dir)


if __name__ == "__main__":
    main()
