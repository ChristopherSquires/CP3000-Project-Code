"""
preprocess.py
-------------
Image preprocessing utilities shared between training and inference.
"""

from __future__ import annotations

from typing import Tuple

import numpy as np
from PIL import Image


# Dimensions that match the EfficientNetB0 input
DEFAULT_IMAGE_SIZE: Tuple[int, int] = (224, 224)


def load_and_preprocess_image(
    image_source,
    image_size: Tuple[int, int] = DEFAULT_IMAGE_SIZE,
) -> np.ndarray:
    """
    Load an image from a file path or a PIL ``Image`` object, resize it, and
    return a pre-processed NumPy array ready for EfficientNet inference.

    Parameters
    ----------
    image_source:
        Either a file-path string/``pathlib.Path``, or a PIL ``Image`` object.
    image_size:
        ``(height, width)`` target size.

    Returns
    -------
    np.ndarray
        Shape ``(1, height, width, 3)``, dtype ``float32``, pixel values in
        ``[0, 255]`` (EfficientNet's ``preprocess_input`` will rescale them).
    """
    if isinstance(image_source, Image.Image):
        img = image_source.convert("RGB")
    else:
        img = Image.open(image_source).convert("RGB")

    img = img.resize((image_size[1], image_size[0]), Image.LANCZOS)
    img_array = np.array(img, dtype=np.float32)

    # Add batch dimension → (1, H, W, 3)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def apply_efficientnet_preprocessing(img_array: np.ndarray) -> np.ndarray:
    """
    Apply EfficientNet-specific pre-processing (scales pixel values to
    ``[-1, 1]``).

    Parameters
    ----------
    img_array:
        Raw pixel array with values in ``[0, 255]``, shape ``(1, H, W, 3)``.

    Returns
    -------
    np.ndarray
        Preprocessed array suitable for direct model input.
    """
    # Import here to keep this module usable without TF installed for tests
    from tensorflow.keras.applications.efficientnet import preprocess_input
    return preprocess_input(img_array)
