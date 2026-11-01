import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
MODEL_PATH = "artifacts/model.pkl"

if not os.path.exists(MODEL_PATH):
    import train
    train.main()

model = joblib.load(MODEL_PATH)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Payload must include 'features' key"}), 400

    features = data["features"]
    if len(features) != 8:
        return jsonify({"error": "Expected 8 features"}), 400

    input_data = np.array(features).reshape(1, -1)
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data).tolist()[0]

    return jsonify({
        "price_range_prediction": int(prediction[0]),
        "probabilities": probabilities
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
