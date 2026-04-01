"""
model_config.py
---------------
Central configuration for the dog-breed classification model.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Architecture
# ---------------------------------------------------------------------------

#: Base feature extractor from Keras Applications
BASE_MODEL_NAME: str = "EfficientNetB0"

#: Number of dog breed classes in the Stanford Dogs Dataset
NUM_CLASSES: int = 120

#: Input image size (height, width) expected by EfficientNetB0
IMAGE_SIZE: tuple[int, int] = (224, 224)

# ---------------------------------------------------------------------------
# Training hyper-parameters
# ---------------------------------------------------------------------------

#: Initial learning rate for the classification head training phase
INITIAL_LEARNING_RATE: float = 1e-3

#: Learning rate used during fine-tuning of the top layers of the base model
FINE_TUNE_LEARNING_RATE: float = 1e-5

#: Batch size for training and validation
BATCH_SIZE: int = 32

#: Total epochs for the head-only warm-up phase
WARMUP_EPOCHS: int = 10

#: Total epochs for the fine-tuning phase
FINE_TUNE_EPOCHS: int = 20

#: Fraction of data to use for validation
VALIDATION_SPLIT: float = 0.2

#: Dropout rate applied before the final classification layer
DROPOUT_RATE: float = 0.3

#: Number of top layers of the base model to unfreeze during fine-tuning.
#: EfficientNetB0 has ~237 layers; unfreezing the top 30 is a good starting point.
FINE_TUNE_AT_LAYER: int = 200

# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

#: Default path to save / load the trained Keras model
DEFAULT_MODEL_PATH: str = "saved_model/dog_breed_classifier.keras"

#: Default path to save / load the list of class names
DEFAULT_CLASS_NAMES_PATH: str = "saved_model/class_names.txt"
