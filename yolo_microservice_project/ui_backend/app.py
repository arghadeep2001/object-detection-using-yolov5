from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
AI_BACKEND_URL = "http://ai_backend:8000/predict/"

@app.route("/", methods=["GET"])
def index():
    return "<h1>Upload Image for YOLO Detection</h1><form action='/upload' method='post' enctype='multipart/form-data'><input type='file' name='file'><input type='submit'></form>"

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    response = requests.post(AI_BACKEND_URL, files={"file": file})
    return jsonify(response.json())
