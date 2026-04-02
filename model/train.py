import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def train_and_save():
    model_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(model_dir)
    data_path = os.path.join(project_root, "data", "sample_dataset.csv")

    print(f"Loading data from {data_path}...")
    if not os.path.exists(data_path):
        print("Data file not found. Please create it first.")
        return

    df = pd.read_csv(data_path)
    X = df['text']
    y = df['label']

    print("Training TF-IDF Vectorizer and MultinomialNB model...")
    # Create a pipeline
    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(analyzer='char_wb', ngram_range=(1, 3))),
        ('classifier', MultinomialNB())
    ])

    pipeline.fit(X, y)

    os.makedirs(model_dir, exist_ok=True)
    pipeline_path = os.path.join(model_dir, "spam_classifier_pipeline.joblib")

    joblib.dump(pipeline, pipeline_path)
    
    print(f"Pipeline saved to {pipeline_path}")
    print("Training complete!")

if __name__ == "__main__":
    train_and_save()
