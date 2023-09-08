import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f'{BASE_DIR}/pipeline_MultinomialNB.pkl', "rb") as f:
    model = joblib.load(f)


def predicted_language(sentence):
    samples = [sentence]
    prediction = str(model.predict(samples))
    prediction = prediction[2:-2]
    return prediction
