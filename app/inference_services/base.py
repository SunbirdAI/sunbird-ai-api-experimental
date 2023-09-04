import requests
import os
from dotenv import load_dotenv
from tenacity import retry, wait_exponential

load_dotenv()


@retry(
    wait=wait_exponential(min=98,)  # Exponential backoff
)
def inference_request_en_mul(payload):
    API_URL = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/sunbird-en-mul'
    headers_en_mul = {"Authorization": os.getenv("HEADER_HUGGING_FACE_TOKEN")}
    response = requests.post(API_URL, headers=headers_en_mul, json=payload)
    return response.text


@retry(
    wait=wait_exponential(min=98)  # Exponential backoff
)
def inference_request_mul_en(payload):
    API_URL = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/mbart-mul-en'
    headers_mul_en = {"Authorization": os.getenv("HEADER_HUGGING_FACE_TOKEN")}
    response = requests.post(API_URL, headers=headers_mul_en, json=payload)
    return response.text
