# YOLO Microservice Project

This is a ready-to-use microservice for object detection using YOLO.

## Setup
1. Place your trained `best.pt` in `ai_backend/model/`
2. Build and run the containers:
```
docker-compose up --build
```
3. Access UI backend at `http://localhost:5000/`.
4. Upload images. Predictions are saved in `output/predictions/` and JSON.

## Notes
- Docker is required.
- You can extend the UI with a proper HTML interface.
- Submission-ready: zip this folder including your weights.
