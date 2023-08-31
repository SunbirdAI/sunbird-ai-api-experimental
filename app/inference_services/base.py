import requests
from tenacity import retry, stop_after_attempt, wait_exponential


API_URL = "https://api-inference.huggingface.co/models/Sunbird/sunbird-en-mul"
headers = {"Authorization": "Bearer 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"}

# Define the retry decorator


@retry(
    stop=stop_after_attempt(5),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.text
