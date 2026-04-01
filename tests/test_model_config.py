"""
tests/test_model_config.py
--------------------------
Smoke tests for model/model_config.py – verifies that all expected
configuration constants are present and have sensible values.
"""

import pytest

import model.model_config as cfg


def test_num_classes():
    assert cfg.NUM_CLASSES == 120


def test_image_size_tuple():
    assert isinstance(cfg.IMAGE_SIZE, tuple)
    assert len(cfg.IMAGE_SIZE) == 2
    assert all(isinstance(d, int) and d > 0 for d in cfg.IMAGE_SIZE)


def test_learning_rates_positive():
    assert cfg.INITIAL_LEARNING_RATE > 0
    assert cfg.FINE_TUNE_LEARNING_RATE > 0
    assert cfg.FINE_TUNE_LEARNING_RATE < cfg.INITIAL_LEARNING_RATE, (
        "Fine-tune LR should be smaller than warm-up LR."
    )


def test_batch_size_positive():
    assert cfg.BATCH_SIZE > 0


def test_epoch_counts_positive():
    assert cfg.WARMUP_EPOCHS > 0
    assert cfg.FINE_TUNE_EPOCHS > 0


def test_validation_split_range():
    assert 0.0 < cfg.VALIDATION_SPLIT < 1.0


def test_dropout_rate_range():
    assert 0.0 <= cfg.DROPOUT_RATE < 1.0


def test_default_paths_are_strings():
    assert isinstance(cfg.DEFAULT_MODEL_PATH, str)
    assert isinstance(cfg.DEFAULT_CLASS_NAMES_PATH, str)
    assert cfg.DEFAULT_MODEL_PATH.endswith(".keras")
    assert cfg.DEFAULT_CLASS_NAMES_PATH.endswith(".txt")
