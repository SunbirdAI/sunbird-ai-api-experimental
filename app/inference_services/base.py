import requests

API_URL = "https://api-inference.huggingface.co/models/Sunbird/sunbird-en-mul"
headers = {"Authorization": "Bearer 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"}


def inference_request(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = inference_request(
    {
        "inputs": ">>lug<<The answer is Yes!"
    }
)

print(output)
