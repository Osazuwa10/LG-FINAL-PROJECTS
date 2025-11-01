# serve.py
import joblib
import pandas as pd
import json
from io import StringIO

model_data = joblib.load('model/segmentation_model.pkl')
kmeans = model_data['kmeans']
scaler = model_data['scaler']
features = model_data['features']
labels = model_data['labels']


def model_fn(model_dir):
    return model_data


def input_fn(input_data, content_type):
    if content_type == 'application/json':
        return pd.DataFrame([json.loads(input_data)])
    elif content_type == 'text/csv':
        return pd.read_csv(StringIO(input_data))
    raise ValueError("Unsupported")


def predict_fn(input_data, model):
    X = input_data[features].fillna(0)
    X_scaled = scaler.transform(X)
    preds = kmeans.predict(X_scaled)
    return [{'segment': labels[p], 'segment_id': int(p)} for p in preds]


def output_fn(prediction, accept):
    return json.dumps({'predictions': prediction}), accept
