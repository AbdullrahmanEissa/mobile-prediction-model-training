# Mobile Price Prediction & Training Pipeline
<img width="1841" height="961" alt="Screenshot from 2026-11-01 11-59-53" src="https://github.com/user-attachments/assets/0ce51a5d-a54d-4b54-8476-4d5456634d17" />
<img width="1841" height="961" alt="Screenshot from 2026-11-01 12-13-33" src="https://github.com/user-attachments/assets/7d53ee50-0e57-40b9-87c6-205e0463d66c" />
<img width="1841" height="961" alt="Screenshot from 2026-11-01 12-13-24" src="https://github.com/user-attachments/assets/82c1433d-9453-4d92-b3f7-c188c1d0e855" />
An end-to-end Machine Learning Operations (MLOps) project for training, versioning, containerizing, and serving a mobile phone price classification model.

---

## Architecture Overview

1. **Data Generation & Tracking:** Dataset generation and version tracking using **DVC (Data Version Control)** with local remote storage.
2. **Model Training:** Scikit-learn Random Forest classifier producing serialized model artifacts (`model.pkl`) and performance metrics (`metrics.json`).
3. **Inference API:** Lightweight **Flask** REST API providing health check and real-time prediction endpoints.
4. **Containerization:** **Docker** container bundling the runtime environment, dependencies, training stage, and API server.

---

## Tech Stack

* **Language:** Python 3.12
* **Machine Learning:** Scikit-learn, Pandas, NumPy, Joblib
* **Data Versioning:** DVC (Data Version Control)
* **API Framework:** Flask
* **Containerization:** Docker
* **CLI & Version Control:** Git, GitHub CLI (`gh`)

---

## Project Structure

```text
mobile-prediction-model-training/
├── artifacts/
│   ├── metrics.json          # Evaluation accuracy metrics
│   └── model.pkl             # Trained model binary
├── data/
│   └── mobile_phones.csv     # Mobile specifications dataset
├── .gitignore                # Environment and cache ignore rules
├── Dockerfile                # Container build and runtime configuration
├── app.py                    # Flask REST API server
├── generate_data.py          # Dataset generation script
├── requirements.txt          # Python dependencies
└── train.py                  # Model training and artifact generation pipeline

```

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/AbdullrahmanEissa/mobile-prediction-model-training.git](https://github.com/AbdullrahmanEissa/mobile-prediction-model-training.git)
cd mobile-prediction-model-training

```

### 2. Local Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

```

---

## Data Versioning with DVC

The dataset can be managed and versioned using DVC backed by local or cloud object storage:

```bash
# Initialize DVC
dvc init

# Configure local remote storage
dvc remote add -d localremote /tmp/dvcstore

# Track dataset changes
dvc add data/mobile_phones.csv

# Push data to storage
dvc push

# Restore data from storage
dvc pull

```

---

## Model Training

Run the training pipeline locally to generate the serialized model and metrics:

```bash
python train.py

```

* Output artifacts will be saved to `artifacts/model.pkl` and `artifacts/metrics.json`.

---

## Docker Deployment & Inference

### 1. Build the Docker Image

```bash
docker build -t mobile-prediction-model:latest .

```

### 2. Run the Container

```bash
docker run -d -p 5000:5000 --name mobile-predictor mobile-prediction-model:latest

```

### 3. Verify Health

```bash
curl -s http://localhost:5000/health

```

**Response:**

```json
{"status": "healthy"}

```

### 4. Real-Time Prediction Endpoint

Send inference requests with the 8 input features:
`[battery_power, ram, int_memory, mobile_wt, px_height, px_width, four_g, touch_screen]`

```bash
curl -s -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [4500, 8192, 128, 175, 1440, 3120, 1, 1]}'

```

**Response:**

```json
{
  "price_range_prediction": 3,
  "probabilities": [0.0, 0.0, 0.11, 0.89]
}

```

*(Classes: `0: Low Cost`, `1: Medium Cost`, `2: High Cost`, `3: Very High Cost`)*

```

---

### Push README Directly to GitHub

Save the file and push it directly from your terminal:

```bash
cat << 'EOF' > README.md
# Mobile Price Prediction & Training Pipeline

An end-to-end Machine Learning Operations (MLOps) project for training, versioning, containerizing, and serving a mobile phone price classification model.

---

## Architecture Overview

1. **Data Generation & Tracking:** Dataset generation and version tracking using **DVC (Data Version Control)** with local remote storage.
2. **Model Training:** Scikit-learn Random Forest classifier producing serialized model artifacts (`model.pkl`) and performance metrics (`metrics.json`).
3. **Inference API:** Lightweight **Flask** REST API providing health check and real-time prediction endpoints.
4. **Containerization:** **Docker** container bundling the runtime environment, dependencies, training stage, and API server.

---

## Tech Stack

* **Language:** Python 3.12
* **Machine Learning:** Scikit-learn, Pandas, NumPy, Joblib
* **Data Versioning:** DVC (Data Version Control)
* **API Framework:** Flask
* **Containerization:** Docker
* **CLI & Version Control:** Git, GitHub CLI (`gh`)

---

## Project Structure

```text
mobile-prediction-model-training/
├── artifacts/
│   ├── metrics.json          # Evaluation accuracy metrics
│   └── model.pkl             # Trained model binary
├── data/
│   └── mobile_phones.csv     # Mobile specifications dataset
├── .gitignore                # Environment and cache ignore rules
├── Dockerfile                # Container build and runtime configuration
├── app.py                    # Flask REST API server
├── generate_data.py          # Dataset generation script
├── requirements.txt          # Python dependencies
└── train.py                  # Model training and artifact generation pipeline

```

---

## Setup and Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/AbdullrahmanEissa/mobile-prediction-model-training.git](https://github.com/AbdullrahmanEissa/mobile-prediction-model-training.git)
cd mobile-prediction-model-training

```

### 2. Local Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

```

---

## Data Versioning with DVC

The dataset can be managed and versioned using DVC backed by local or cloud object storage:

```bash
# Initialize DVC
dvc init

# Configure local remote storage
dvc remote add -d localremote /tmp/dvcstore

# Track dataset changes
dvc add data/mobile_phones.csv

# Push data to storage
dvc push

# Restore data from storage
dvc pull

```

---

## Model Training

Run the training pipeline locally to generate the serialized model and metrics:

```bash
python train.py

```

* Output artifacts will be saved to `artifacts/model.pkl` and `artifacts/metrics.json`.

---

## Docker Deployment & Inference

### 1. Build the Docker Image

```bash
docker build -t mobile-prediction-model:latest .

```

### 2. Run the Container

```bash
docker run -d -p 5000:5000 --name mobile-predictor mobile-prediction-model:latest

```

### 3. Verify Health

```bash
curl -s http://localhost:5000/health

```

**Response:**

```json
{"status": "healthy"}

```

### 4. Real-Time Prediction Endpoint

Send inference requests with the 8 input features:
`[battery_power, ram, int_memory, mobile_wt, px_height, px_width, four_g, touch_screen]`

```bash
curl -s -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [4500, 8192, 128, 175, 1440, 3120, 1, 1]}'

```

**Response:**

```json
{
  "price_range_prediction": 3,
  "probabilities": [0.0, 0.0, 0.11, 0.89]
}

```

*(Classes: `0: Low Cost`, `1: Medium Cost`, `2: High Cost`, `3: Very High Cost`)*
