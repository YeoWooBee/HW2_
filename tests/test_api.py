from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True

def test_predict_endpoint_spam():
    # Example likely spam message
    payload = {"text": "Win a FREE iPhone now! Click here to claim your prize."}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "confidence" in data
    assert data["label"] == 1 # Expected to be classified as SPAM

def test_predict_endpoint_ham():
    # Example likely ham message
    payload = {"text": "Hey, let's have lunch together tomorrow at 12."}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "confidence" in data
    assert data["label"] == 0 # Expected to be classified as HAM
