from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model_data = joblib.load("model/segmentation_model.pkl")
kmeans = model_data['kmeans']
scaler = model_data['scaler']
features = model_data['features']
labels = model_data['labels']


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to LG Customer Segmentation API – model is live!"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = [data.get(f, 0) for f in features]
    features_array = np.array([input_data])
    scaled = scaler.transform(features_array)
    prediction = kmeans.predict(scaled)[0]
    segment_label = labels[prediction]
    confidence = np.max(kmeans.predict_proba(scaled)) if hasattr(
        kmeans, 'predict_proba') else 1.0
    return jsonify({
        "segment_id": int(prediction),
        "segment": segment_label,
        "confidence": float(confidence)
    })


if __name__ == "__main__":
    app.run(debug=True)
