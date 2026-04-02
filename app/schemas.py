from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    text: str = Field(..., description="The input text message to classify.", example="Win a free iPhone now!")

class PredictResponse(BaseModel):
    label: int = Field(..., description="Classification result label: 1 for 'spam', 0 for 'not spam'")
    confidence: float = Field(..., description="Confidence probability of the prediction (0.0 to 1.0)")
