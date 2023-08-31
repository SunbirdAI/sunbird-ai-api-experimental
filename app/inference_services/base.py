import requests

API_URL = "https://api-inference.huggingface.co/models/Sunbird/sunbird-en-mul"
headers = {"Authorization": "Bearer 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"}


def inference_requests(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = inference_requests({
    "inputs": ">>lug<<The answer to the universe is",
})

print(output)
