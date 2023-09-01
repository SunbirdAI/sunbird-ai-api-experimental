import requests
import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()


@retry(
    stop=stop_after_attempt(4),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def inference_request_en_mul(payload):
    API_URL = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/sunbird-en-mul'
    headers_en_mul = {"Authorization": os.getenv("HEADERS_EN_MUL")}
    response = requests.post(API_URL, headers=headers_en_mul, json=payload)
    return response.text


@retry(
    stop=stop_after_attempt(4),  # Maximum number of retries
    wait=wait_exponential(multiplier=1, min=1, max=60)  # Exponential backoff
)
def inference_request_mul_en(payload):
    API_URL = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/mbart-mul-en'
    headers_mul_en = {"Authorization": os.getenv("HEADER_MUL_EN")}
    response = requests.post(API_URL, headers=headers_mul_en, json=payload)
    return response.text
