# CP3000 Project – AI Dog Breed Identifier

An AI-powered application that identifies a dog's breed from a provided image
and generates detailed information about that breed.

**Dataset:**
[Stanford Dogs Dataset](https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset)
(20,580 images · 120 breeds)

---

## Features

- **Upload any dog photo** (JPG / JPEG / PNG).
- **AI breed identification** – returns the top-3 most likely breeds with
  confidence percentages.
- **Detailed breed cards** – for each prediction the app shows:
  - Breed name, group & country of origin
  - Typical lifespan
  - Height and weight ranges
  - Temperament traits
  - A descriptive summary
- Interactive **Streamlit** web interface.
- Two-phase **transfer learning** using EfficientNetB0 (ImageNet pre-trained).

---

## Project Structure

```
CP3000-Project-Code/
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
│
├── model/
│   ├── model_config.py           # Hyper-parameters and path constants
│   ├── train.py                  # Two-phase training script
│   └── predict.py                # Inference / breed identification
│
├── data/
│   ├── breed_info.py             # Breed information database (120 breeds)
│   └── dataset_loader.py         # Stanford Dogs Dataset tf.data pipeline
│
├── utils/
│   └── preprocess.py             # Image loading and preprocessing utilities
│
├── tests/
│   ├── test_breed_info.py        # Unit tests – breed database
│   ├── test_preprocess.py        # Unit tests – image preprocessing
│   └── test_model_config.py      # Unit tests – model configuration
│
└── saved_model/                  # Created after training
    ├── dog_breed_classifier.keras
    └── class_names.txt
```

---

## Quick Start

### Windows users – enable Long Path support first

TensorFlow ships header files nested in very deep sub-directories.
On Windows the default `MAX_PATH` limit (260 characters) is too short for
those paths when the project lives somewhere like
`C:\Users\<name>\Desktop\CP3000-Project-Code\…`.
You will see an error like:

```
OSError: [Errno 2] No such file or directory: '…\client_side_weighted_round_robin.upb_minitable.h'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled.
```

**Option A – automated setup script (recommended)**

Run the provided helper from an *elevated* (Administrator) command prompt.
It enables Long Path support, creates the virtual environment at a short path
(`C:\cp3000\.venv`), and installs all dependencies:

```bat
setup_windows.bat
```

Then activate the environment and run the app:

```bat
C:\cp3000\.venv\Scripts\activate
streamlit run app.py
```

**Option B – manual steps**

1. Enable Long Paths via an elevated PowerShell:
   ```powershell
   New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
       -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force
   ```
   Then **reboot** to activate the change.

2. Clone the repo to a short base path, e.g.:
   ```bat
   git clone <repo-url> C:\cp3000\src
   cd C:\cp3000\src
   ```

3. Create the virtual environment at a short path:
   ```bat
   python -m venv C:\cp3000\.venv
   C:\cp3000\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

### 1 · Clone & install dependencies

```bash
git clone <repo-url>
cd CP3000-Project-Code
pip install -r requirements.txt
```

### 2 · Download the dataset

1. Create a free [Kaggle](https://www.kaggle.com) account and install the
   Kaggle CLI:
   ```bash
   pip install kaggle
   ```
2. Place your `kaggle.json` API token in `~/.kaggle/`.
3. Download and unzip the dataset:
   ```bash
   kaggle datasets download jessicali9530/stanford-dogs-dataset
   unzip stanford-dogs-dataset.zip -d stanford-dogs-dataset
   ```

The expected directory layout after extraction:
```
stanford-dogs-dataset/
└── images/
    └── Images/
        ├── n02085620-Chihuahua/
        ├── n02085782-Japanese_spaniel/
        └── ...  (120 breed folders)
```

### 3 · Train the model

```bash
python -m model.train --images_dir stanford-dogs-dataset/images/Images
```

Training runs in two phases:

| Phase | Layers trained | Epochs | LR |
|---|---|---|---|
| Warm-up | Classification head only | 10 | 1e-3 |
| Fine-tuning | Top EfficientNetB0 layers + head | 20 | 1e-5 |

The trained model and class-name list are saved under `saved_model/`.

### 4 · Run the web app

```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`) and upload a dog photo.

---

## How It Works

```
Dog Image
    │
    ▼
┌─────────────────────────────┐
│  utils/preprocess.py        │  Resize to 224×224, add batch dim
│  load_and_preprocess_image  │  apply EfficientNet preprocess_input
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  EfficientNetB0 Base        │  Pre-trained on ImageNet
│  + Classification Head      │  Fine-tuned on Stanford Dogs Dataset
└─────────────────────────────┘
    │  120-class softmax output
    ▼
┌─────────────────────────────┐
│  model/predict.py           │  Top-k predictions with confidence
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  data/breed_info.py         │  Breed name, lifespan, origin, etc.
└─────────────────────────────┘
    │
    ▼
  Streamlit UI  (app.py)
```

---

## Running Tests

```bash
pytest tests/ -v
```

All tests run **without** requiring a trained model or TensorFlow GPU support.

---

## Model Details

| Attribute | Value |
|---|---|
| Base model | EfficientNetB0 (ImageNet weights) |
| Input size | 224 × 224 × 3 |
| Output classes | 120 |
| Head | GAP → BatchNorm → Dropout(0.3) → Dense(120, softmax) |
| Optimiser | Adam |
| Warm-up LR | 1e-3 |
| Fine-tune LR | 1e-5 |

---

## Dataset Reference

> J. Liu, A. Kanazawa, D. Jacobs, P. Perona. *Dog Breed Classification Using
> Part Localization.* ECCV 2012.
>
> Dataset available at:
> https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset
