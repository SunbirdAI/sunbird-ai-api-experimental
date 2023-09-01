import requests
from tenacity import retry, stop_after_attempt, wait_exponential


@retry(
    stop=stop_after_attempt(5),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def inference_request_en_mul(payload):
    API_URL = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/sunbird-en-mul'
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.text


@retry(
    stop=stop_after_attempt(5),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def inference_request_mul_en(payload):
    API_URL = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/mbart-mul-en'
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.text
