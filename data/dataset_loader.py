"""
dataset_loader.py
-----------------
Utilities for loading and preparing the Stanford Dogs Dataset for training.

Dataset source:
  https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset

Expected on-disk layout after unzipping the Kaggle download::

    <dataset_root>/
        images/
            Images/
                n02085620-Chihuahua/
                    n02085620_10074.jpg
                    ...
                n02085782-Japanese_spaniel/
                    ...
                ...
        annotations/
            Annotation/
                n02085620-Chihuahua/
                    n02085620_10074       ← XML bounding-box annotation
                    ...

Pass the path to the top-level `images/Images` directory as `images_dir`.
"""

from __future__ import annotations

import os
import pathlib
from typing import Tuple

import numpy as np
import tensorflow as tf

# Default image dimensions expected by EfficientNet models
IMAGE_SIZE: Tuple[int, int] = (224, 224)
AUTOTUNE = tf.data.AUTOTUNE


def _get_class_names(images_dir: str) -> list[str]:
    """Return sorted list of class folder names found under *images_dir*."""
    images_path = pathlib.Path(images_dir)
    class_names = sorted(
        [d.name for d in images_path.iterdir() if d.is_dir()]
    )
    return class_names


def build_dataset(
    images_dir: str,
    image_size: Tuple[int, int] = IMAGE_SIZE,
    batch_size: int = 32,
    validation_split: float = 0.2,
    seed: int = 42,
) -> Tuple[tf.data.Dataset, tf.data.Dataset, list[str]]:
    """
    Build train and validation ``tf.data.Dataset`` objects from the Stanford
    Dogs Dataset image directory.

    Parameters
    ----------
    images_dir:
        Path to the ``images/Images`` directory extracted from the Kaggle download.
    image_size:
        ``(height, width)`` to resize every image to.
    batch_size:
        Number of samples per batch.
    validation_split:
        Fraction of images to use for validation.
    seed:
        Random seed for reproducible splits.

    Returns
    -------
    train_ds, val_ds, class_names
        Two ``tf.data.Dataset`` objects and the sorted list of class-folder names
        (used to map model output indices back to breed labels).
    """
    train_ds = tf.keras.utils.image_dataset_from_directory(
        images_dir,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size,
        label_mode="int",
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        images_dir,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size,
        label_mode="int",
    )

    class_names: list[str] = train_ds.class_names  # type: ignore[attr-defined]

    # Performance optimisations
    train_ds = train_ds.cache().shuffle(1000, seed=seed).prefetch(AUTOTUNE)
    val_ds = val_ds.cache().prefetch(AUTOTUNE)

    return train_ds, val_ds, class_names


def save_class_names(class_names: list[str], output_path: str) -> None:
    """Persist *class_names* to a plain text file, one name per line."""
    output_path_obj = pathlib.Path(output_path)
    output_path_obj.parent.mkdir(parents=True, exist_ok=True)
    output_path_obj.write_text("\n".join(class_names))
    print(f"Class names saved to {output_path_obj}")


def load_class_names(path: str) -> list[str]:
    """Load class names from a text file previously saved by :func:`save_class_names`."""
    return pathlib.Path(path).read_text().splitlines()
