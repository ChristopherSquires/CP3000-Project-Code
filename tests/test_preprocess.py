"""
tests/test_preprocess.py
------------------------
Unit tests for utils/preprocess.py.
These tests do NOT require a trained model or the full dataset.
"""

import numpy as np
import pytest
from PIL import Image

from utils.preprocess import load_and_preprocess_image, DEFAULT_IMAGE_SIZE


def _make_random_pil_image(width: int = 300, height: int = 400) -> Image.Image:
    """Create a random RGB PIL image for testing."""
    arr = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    return Image.fromarray(arr, mode="RGB")


def test_output_shape_from_pil_image():
    """load_and_preprocess_image with a PIL image should return (1, H, W, 3)."""
    img = _make_random_pil_image()
    result = load_and_preprocess_image(img)
    h, w = DEFAULT_IMAGE_SIZE
    assert result.shape == (1, h, w, 3), f"Unexpected shape: {result.shape}"


def test_output_shape_custom_size():
    """Custom image_size parameter should be respected."""
    img = _make_random_pil_image()
    custom_size = (128, 128)
    result = load_and_preprocess_image(img, image_size=custom_size)
    assert result.shape == (1, 128, 128, 3)


def test_output_dtype():
    """Output array should be float32."""
    img = _make_random_pil_image()
    result = load_and_preprocess_image(img)
    assert result.dtype == np.float32


def test_pixel_value_range_before_preprocessing():
    """Raw pixel values before EfficientNet preprocessing should be in [0, 255]."""
    img = _make_random_pil_image()
    result = load_and_preprocess_image(img)
    assert result.min() >= 0.0
    assert result.max() <= 255.0


def test_rgba_image_converted_to_rgb():
    """An RGBA image should be converted to RGB without error."""
    arr = np.random.randint(0, 256, (50, 50, 4), dtype=np.uint8)
    rgba_img = Image.fromarray(arr, mode="RGBA")
    result = load_and_preprocess_image(rgba_img)
    assert result.shape[-1] == 3  # 3 colour channels


def test_load_from_file_path(tmp_path):
    """load_and_preprocess_image should accept a file path string."""
    img = _make_random_pil_image(width=100, height=100)
    img_path = tmp_path / "test_dog.jpg"
    img.save(str(img_path))

    result = load_and_preprocess_image(str(img_path))
    h, w = DEFAULT_IMAGE_SIZE
    assert result.shape == (1, h, w, 3)
