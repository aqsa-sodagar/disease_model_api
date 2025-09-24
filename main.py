import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Load your trained model
MODEL_PATH = "model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels (update if different)
CLASS_NAMES = ["control", "diseased"]

app = FastAPI(title="Disease Detection API")

# Image preprocessing
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))  # resize to model input size
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        input_data = preprocess_image(image_bytes)
        preds = model.predict(input_data)
        class_idx = np.argmax(preds[0])
        confidence = float(np.max(preds[0]))
        return JSONResponse({
            "class": CLASS_NAMES[class_idx],
            "confidence": confidence
        })
    except Exception as e:
        return JSONResponse({"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
