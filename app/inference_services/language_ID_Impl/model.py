import joblib

with open('app/inference_services/language_ID_Impl'
          '/pipeline_MultinomialNB.pkl', "rb") as f:
    model = joblib.load(f)


def predicted_language(sentence):
    samples = [sentence]
    prediction = str(model.predict(samples))
    prediction = prediction[2:-2]
    return prediction
