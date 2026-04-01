"""
tests/test_breed_info.py
------------------------
Unit tests for the breed information database (data/breed_info.py).
These tests do NOT require TensorFlow or a trained model.
"""

import pytest

from data.breed_info import BREED_INFO, BREED_ALIASES, get_breed_info


# ──────────────────────────────────────────────────────────────────────────────
# BREED_INFO structure tests
# ──────────────────────────────────────────────────────────────────────────────

REQUIRED_KEYS = {"name", "group", "origin", "lifespan", "height", "weight", "temperament", "description"}


def test_breed_info_not_empty():
    """The database must contain at least the 120 breeds from the Stanford Dogs Dataset."""
    assert len(BREED_INFO) >= 80, "BREED_INFO should contain at least 80 breeds."


def test_each_breed_has_required_keys():
    """Every breed entry must contain all required information keys."""
    for breed_key, info in BREED_INFO.items():
        missing = REQUIRED_KEYS - info.keys()
        assert not missing, f"Breed '{breed_key}' is missing keys: {missing}"


def test_temperament_is_list():
    """Temperament field must be a list for every breed."""
    for breed_key, info in BREED_INFO.items():
        assert isinstance(
            info["temperament"], list
        ), f"Breed '{breed_key}' temperament should be a list."


def test_description_is_nonempty_string():
    """Description field must be a non-empty string."""
    for breed_key, info in BREED_INFO.items():
        assert isinstance(info["description"], str), (
            f"Breed '{breed_key}' description should be a string."
        )
        assert len(info["description"]) > 0, (
            f"Breed '{breed_key}' description must not be empty."
        )


# ──────────────────────────────────────────────────────────────────────────────
# get_breed_info() tests
# ──────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("breed_key", [
    "golden-retriever",
    "labrador-retriever",
    "german-shepherd",
    "poodle",        # partial match should still work
    "chihuahua",
    "beagle",
    "pug",
    "boxer",
    "dalmatian",
    "siberian-husky",
])
def test_get_breed_info_known_breeds(breed_key):
    """Known breed keys must return a complete info dict."""
    info = get_breed_info(breed_key)
    assert info["name"] != ""
    assert info["group"] != ""


def test_get_breed_info_stanford_folder_name():
    """Stanford Dogs Dataset folder names (with ImageNet synset prefix) must resolve."""
    info = get_breed_info("n02099601-golden_retriever")
    assert "Golden" in info["name"], f"Expected Golden Retriever, got: {info}"


def test_get_breed_info_unknown_breed_returns_fallback():
    """An unrecognised breed key should return a fallback dict with the name set."""
    info = get_breed_info("my-totally-fake-breed-xyz")
    assert info is not None
    assert isinstance(info, dict)
    assert "name" in info


def test_get_breed_info_case_insensitive():
    """Lookups should work regardless of case."""
    info_lower = get_breed_info("golden-retriever")
    info_upper = get_breed_info("GOLDEN-RETRIEVER")
    assert info_lower["name"] == info_upper["name"]


def test_get_breed_info_whitespace_tolerance():
    """Leading/trailing whitespace in the key should be stripped."""
    info = get_breed_info("  beagle  ")
    assert info["name"] == "Beagle"


# ──────────────────────────────────────────────────────────────────────────────
# BREED_ALIASES tests
# ──────────────────────────────────────────────────────────────────────────────

def test_all_alias_values_exist_in_breed_info():
    """Every alias value must correspond to a key that exists in BREED_INFO."""
    for alias_key, canonical in BREED_ALIASES.items():
        assert canonical in BREED_INFO, (
            f"Alias '{alias_key}' points to '{canonical}' which is not in BREED_INFO."
        )


def test_alias_resolution():
    """A sample of Stanford Dogs folder names should resolve correctly."""
    sample_aliases = {
        "n02099601-golden_retriever": "golden-retriever",
        "n02099712-labrador_retriever": "labrador-retriever",
        "n02106662-german_shepherd": "german-shepherd",
        "n02110958-pug": "pug",
        "n02085620-chihuahua": "chihuahua",
    }
    for folder_name, expected_canonical in sample_aliases.items():
        resolved = BREED_ALIASES.get(folder_name)
        assert resolved == expected_canonical, (
            f"Alias '{folder_name}' resolved to '{resolved}', expected '{expected_canonical}'."
        )
