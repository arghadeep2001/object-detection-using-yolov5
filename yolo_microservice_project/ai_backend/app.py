import os
import shutil

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO

app = FastAPI()
model = YOLO("model/best.pt")
OUTPUT_DIR = "../output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join(OUTPUT_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    results = model.predict(source=file_path, save=True, project=OUTPUT_DIR, name="predictions")
    detections = []
    for r in results:
        for box in r.boxes:
            detections.append(
                {
                    "bbox": box.xyxy[0].tolist(),
                    "class_id": int(box.cls[0]),
                    "class_name": model.names[int(box.cls[0])],
                    "confidence": float(box.conf[0]),
                }
            )
    return JSONResponse({"image": file.filename, "detections": detections})
