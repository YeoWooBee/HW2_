import os
import joblib

class SpamClassifier:
    def __init__(self, pipeline_path="model/spam_classifier_pipeline.joblib"):
        if not os.path.exists(pipeline_path):
            raise FileNotFoundError(f"Model pipeline not found at {pipeline_path}. Please run python model/train.py first.")
        
        self.pipeline = joblib.load(pipeline_path)

    def predict(self, text: str):
        # Predict the class (0 for ham, 1 for spam)
        prediction_label = self.pipeline.predict([text])[0]
        
        # Predict the probabilities
        probabilities = self.pipeline.predict_proba([text])[0]
        confidence = float(probabilities[prediction_label])
        
        return {
            "label": int(prediction_label),
            "confidence": confidence
        }
