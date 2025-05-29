import tensorflow as tf
from PIL import Image
import numpy as np
import io
import json

# Load model and classes
model = tf.keras.models.load_model("models/plant_disease_model.h5")

with open("models/class_indices.json") as f:
    class_indices = json.load(f)
    class_labels = {v: k for k, v in class_indices.items()}

def preprocess(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_disease(image_bytes):
    image = preprocess(image_bytes)
    preds = model.predict(image)[0]
    idx = np.argmax(preds)
    return {
        "class": class_labels[idx],
        "confidence": float(round(preds[idx], 4))
    }
