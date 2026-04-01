"""
predict.py
----------
Inference module for the dog-breed classification model.

A pre-trained model is loaded once and cached; subsequent calls to
:func:`predict_breed` reuse the same model instance for efficiency.
"""

from __future__ import annotations

import pathlib
from typing import Optional

import numpy as np

from data.breed_info import get_breed_info
from model.model_config import (
    DEFAULT_CLASS_NAMES_PATH,
    DEFAULT_MODEL_PATH,
    IMAGE_SIZE,
)
from utils.preprocess import apply_efficientnet_preprocessing, load_and_preprocess_image

# Module-level cache so the model is loaded only once
_model = None
_class_names: Optional[list[str]] = None


def _load_model(
    model_path: str = DEFAULT_MODEL_PATH,
    class_names_path: str = DEFAULT_CLASS_NAMES_PATH,
):
    """Load the Keras model and class-name list into module-level cache."""
    global _model, _class_names

    import tensorflow as tf

    model_path_obj = pathlib.Path(model_path)
    class_names_path_obj = pathlib.Path(class_names_path)

    if not model_path_obj.exists():
        raise FileNotFoundError(
            f"Trained model not found at '{model_path_obj}'. "
            "Please run 'python -m model.train --images_dir <path>' first."
        )
    if not class_names_path_obj.exists():
        raise FileNotFoundError(
            f"Class names file not found at '{class_names_path_obj}'. "
            "Please run 'python -m model.train --images_dir <path>' first."
        )

    _model = tf.keras.models.load_model(str(model_path_obj))
    _class_names = class_names_path_obj.read_text().splitlines()
    print(f"Model loaded from {model_path_obj} ({len(_class_names)} classes).")


def predict_breed(
    image_source,
    top_k: int = 3,
    model_path: str = DEFAULT_MODEL_PATH,
    class_names_path: str = DEFAULT_CLASS_NAMES_PATH,
) -> list[dict]:
    """
    Identify the dog breed(s) in an image.

    Parameters
    ----------
    image_source:
        File path (str / ``pathlib.Path``) or PIL ``Image`` object.
    top_k:
        Number of top predictions to return (default: 3).
    model_path:
        Path to the saved Keras model file.
    class_names_path:
        Path to the saved class-names text file.

    Returns
    -------
    list[dict]
        A list of up to *top_k* prediction dictionaries, sorted by confidence
        (highest first). Each dict contains::

            {
                "rank":        int,      # 1-based rank
                "class_name":  str,      # raw folder-name label
                "confidence":  float,    # probability in [0, 1]
                "breed_info":  dict,     # from data.breed_info.get_breed_info()
            }
    """
    global _model, _class_names

    if _model is None:
        _load_model(model_path=model_path, class_names_path=class_names_path)

    # Preprocess the image
    img_array = load_and_preprocess_image(image_source, image_size=IMAGE_SIZE)
    img_array = apply_efficientnet_preprocessing(img_array)

    # Run inference
    predictions = _model.predict(img_array, verbose=0)  # shape: (1, num_classes)
    probs = predictions[0]  # shape: (num_classes,)

    # Get top-k indices sorted by probability descending
    top_indices = np.argsort(probs)[::-1][:top_k]

    results = []
    for rank, idx in enumerate(top_indices, start=1):
        class_name = _class_names[idx]
        confidence = float(probs[idx])
        results.append(
            {
                "rank": rank,
                "class_name": class_name,
                "confidence": confidence,
                "breed_info": get_breed_info(class_name),
            }
        )

    return results
