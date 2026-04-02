# MLOps Spam Classifier API

A simple, lightweight API for classifying text messages as `spam` or `notspam`. Built with FastAPI and scikit-learn (TF-IDF + MultinomialNB).

## Features
- `GET /health`: Healthcheck endpoint
- `POST /predict`: Inference endpoint receiving `{ "text": "..." }` and outputting prediction and probability.

## Local Setup

### 1. Create a virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate # Mac/Linux

pip install -r requirements.txt
```

### 2. Train the initial model
To start the server, you need the trained model artifacts (`.pkl` files). Run the simple training script:
```bash
python model/train.py
```
This will train a basic model mapped to dummy data and output `model/spam_model.pkl` and `model/vectorizer.pkl`.

### 3. Run the API server
```bash
uvicorn app.main:app --reload
```
You can view the Swagger UI documentation at `http://127.0.0.1:8000/docs`.

### 4. Test the API
You can test the prediction endpoint via curl:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Win a free iPhone now!"
}'
```

## Docker Deployment
Easily deploy using Docker.

```bash
# 1. Provide the model artifacts first
python model/train.py

# 2. Build the Docker image
docker build -t spam-classifier .

# 3. Run the container
docker run -p 8000:8000 spam-classifier
```
