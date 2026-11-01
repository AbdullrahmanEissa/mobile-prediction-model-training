import os
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    data_path = "data/mobile_phones.csv"
    df = pd.read_csv(data_path)

    features = [
        "battery_power", "ram", "int_memory", "mobile_wt",
        "px_height", "px_width", "four_g", "touch_screen"
    ]
    X = df[features]
    y = df["price_range"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/model.pkl")

    with open("artifacts/metrics.json", "w") as f:
        json.dump({"accuracy": float(accuracy)}, f)

if __name__ == "__main__":
    main()
