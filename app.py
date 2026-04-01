"""
app.py
------
Streamlit web application for the AI-powered dog-breed identification tool.

Run with:
    streamlit run app.py

The app allows users to upload a dog image (JPG, JPEG, or PNG) and:
  • Identifies the breed using a trained EfficientNetB0 model.
  • Displays the top-3 breed predictions with confidence scores.
  • Shows detailed information about the top predicted breed, including
    name, group, origin, lifespan, size, temperament, and description.

Note: A trained model must be present at saved_model/dog_breed_classifier.keras
(or the path configured in model/model_config.py).  Run model/train.py first.
"""

from __future__ import annotations

import io
import pathlib
from typing import Optional

import streamlit as st
from PIL import Image

# ──────────────────────────────────────────────────────────────────────────────
# Page configuration (must be the first Streamlit call)
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🐶 Dog Breed Identifier",
    page_icon="🐶",
    layout="centered",
)

# ──────────────────────────────────────────────────────────────────────────────
# Helper functions
# ──────────────────────────────────────────────────────────────────────────────

MODEL_READY = pathlib.Path("saved_model/dog_breed_classifier.keras").exists()


@st.cache_resource(show_spinner="Loading AI model…")
def load_predictor():
    """Import the predictor and warm-up model loading (cached across re-runs)."""
    from model.predict import predict_breed, _load_model
    _load_model()
    return predict_breed


def render_breed_card(breed_info: dict, confidence: float) -> None:
    """Render a styled information card for one breed prediction."""
    name = breed_info.get("name", "Unknown")
    group = breed_info.get("group", "—")
    origin = breed_info.get("origin", "—")
    lifespan = breed_info.get("lifespan", "—")
    height = breed_info.get("height", "—")
    weight = breed_info.get("weight", "—")
    temperament = breed_info.get("temperament", [])
    description = breed_info.get("description", "")

    st.markdown(f"### 🐾 {name}")
    st.progress(min(confidence, 1.0), text=f"Confidence: {confidence * 100:.1f}%")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Group:** {group}")
        st.markdown(f"**Origin:** {origin}")
        st.markdown(f"**Lifespan:** {lifespan}")
    with col2:
        st.markdown(f"**Height:** {height}")
        st.markdown(f"**Weight:** {weight}")

    if temperament:
        tags = "  ".join(f"`{t}`" for t in temperament)
        st.markdown(f"**Temperament:** {tags}")

    if description:
        st.info(description)

    st.divider()


# ──────────────────────────────────────────────────────────────────────────────
# Main UI
# ──────────────────────────────────────────────────────────────────────────────

st.title("🐶 Dog Breed Identifier")
st.markdown(
    """
Upload a photo of a dog and the AI will identify its breed and provide
detailed information including lifespan, origin, size, and temperament.

*Powered by EfficientNetB0 trained on the*
[Stanford Dogs Dataset](https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset)
*(120 breeds).*
"""
)

# Model availability notice
if not MODEL_READY:
    st.warning(
        "⚠️ **No trained model found.**\n\n"
        "To enable breed identification, first train the model:\n"
        "```\n"
        "python -m model.train --images_dir path/to/images/Images\n"
        "```\n"
        "Download the Stanford Dogs Dataset from: "
        "https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset"
    )

st.markdown("---")

# File upload widget
uploaded_file = st.file_uploader(
    "Choose a dog image…",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG, PNG",
)

if uploaded_file is not None:
    # Display the uploaded image
    image_bytes = uploaded_file.read()
    pil_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    col_img, col_info = st.columns([1, 1])
    with col_img:
        st.image(pil_image, caption="Uploaded Image", use_column_width="always")

    with col_info:
        if not MODEL_READY:
            st.error(
                "Model not available. Please train the model first "
                "(see the warning above)."
            )
        else:
            with st.spinner("🔍 Analysing breed…"):
                try:
                    predict_breed = load_predictor()
                    predictions = predict_breed(pil_image, top_k=3)
                except FileNotFoundError as exc:
                    st.error(str(exc))
                    predictions = []

            if predictions:
                top = predictions[0]
                breed_name = top["breed_info"].get("name", top["class_name"])
                st.success(f"**Top prediction: {breed_name}**")

    # Show detailed breed cards
    if MODEL_READY:
        if uploaded_file is not None:
            st.markdown("## 📋 Breed Details")

            try:
                predict_breed = load_predictor()
                # Re-use cached predictions
                predictions = predict_breed(pil_image, top_k=3)

                tabs = st.tabs(
                    [
                        f"#{p['rank']} {p['breed_info'].get('name', p['class_name'])}"
                        for p in predictions
                    ]
                )
                for tab, pred in zip(tabs, predictions):
                    with tab:
                        render_breed_card(pred["breed_info"], pred["confidence"])

            except FileNotFoundError as exc:
                st.error(str(exc))

# ──────────────────────────────────────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown(
        """
**Dog Breed Identifier** uses a deep learning model (EfficientNetB0)
trained on the Stanford Dogs Dataset to classify 120 different dog breeds
from a single photograph.

**How it works:**
1. Upload any photo containing a dog.
2. The AI analyses the image and predicts the most likely breed(s).
3. Detailed breed information is shown, including origin, lifespan,
   size, temperament traits, and a breed description.

**Model:**  EfficientNetB0 + transfer learning  
**Dataset:** Stanford Dogs Dataset (20,580 images, 120 breeds)  
**Source:** Kaggle – jessicali9530/stanford-dogs-dataset
"""
    )

    st.header("🔧 Setup")
    st.code(
        "# 1. Install dependencies\n"
        "pip install -r requirements.txt\n\n"
        "# 2. Download dataset from Kaggle\n"
        "#    https://www.kaggle.com/datasets/\n"
        "#    jessicali9530/stanford-dogs-dataset\n\n"
        "# 3. Train the model\n"
        "python -m model.train \\\n"
        "  --images_dir path/to/images/Images\n\n"
        "# 4. Run the app\n"
        "streamlit run app.py",
        language="bash",
    )
