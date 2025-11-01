from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model
model_data = joblib.load('model/segmentation_model.pkl')
kmeans = model_data['kmeans']
scaler = model_data['scaler']
features = model_data['features']
labels = model_data['labels']


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    X = df[features].fillna(0)
    X_scaled = scaler.transform(X)
    pred = kmeans.predict(X_scaled)[0]
    return jsonify({
        'segment_id': int(pred),
        'segment': labels[pred],
        # Optional confidence
        'confidence': float(np.max(kmeans.predict_proba(X_scaled)))
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
