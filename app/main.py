import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from app.schemas import PredictRequest, PredictResponse
from app.model import SpamClassifier

app = FastAPI(
    title="Spam Message Classifier API",
    description="A lightweight API for classifying spam messages using TF-IDF and MultinomialNB.",
    version="1.0.0"
)

# Initialize the classifier instance
try:
    classifier = SpamClassifier()
except Exception as e:
    classifier = None
    print(f"Warning: Could not initialize classifier: {e}")

@app.get("/health")
def health_check():
    status = "healthy" if classifier is not None else "degraded"
    return {"status": status, "model_loaded": classifier is not None}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    if classifier is None:
        raise HTTPException(status_code=503, detail="Model is not loaded. Cannot predict.")
    
    result = classifier.predict(request.text)
    return PredictResponse(
        label=result["label"],
        confidence=result["confidence"]
    )

@app.get("/", response_class=FileResponse)
def get_ui():
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path)
    raise HTTPException(status_code=404, detail="index.html not found.")
