import requests


API_URL = "https://api-inference.huggingface.co/models/Sunbird/sunbird-en-mul"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.text
