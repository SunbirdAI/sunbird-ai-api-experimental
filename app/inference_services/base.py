import requests
import os
# import time
from dotenv import load_dotenv
from tenacity import retry, wait_exponential

load_dotenv()


@retry(
    wait=wait_exponential(multiplier=3, min=98, max=120)  # Exponential backoff
)
def inference_request_en_mul(payload):
    url = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/sunbird-en-mul'
    headers_en_mul = {"Authorization": os.getenv("HEADER_HUGGING_FACE_TOKEN")}
    response = requests.post(url, headers=headers_en_mul, json=payload)
    # TODOCreate a function that just calls it
    # This is where i applied the exponential backoff
    # if response.status_code == 503:
    #     estimated_time = response.json()['estimated_time']
    #     time.sleep(estimated_time)
    #     # logging.info(f"Model Loading ...{estimated_time}")
    #     print(estimated_time)
    #     response = requests.post(url, headers=headers_en_mul, json=payload)
    #     return response.text
    # else:

    return response.json()[0]['generated_text']


@retry(
    wait=wait_exponential(multiplier=3, min=98, max=120)  # Exponential backoff
)
def inference_request_mul_en(payload):
    url = 'https://api-inference.huggingface.co/m'\
              'odels/Sunbird/mbart-mul-en'
    headers_mul_en = {"Authorization": os.getenv("HEADER_HUGGING_FACE_TOKEN")}
    response = requests.post(url, headers=headers_mul_en, json=payload)
    # # This is where i applied the exponential backoff
    # if response.status_code == 503:
    #     estimated_time = response.json()['estimated_time']
    #     time.sleep(estimated_time)
    #     # logging.info(f"Model Loading ...{estimated_time}")
    #     print(estimated_time)
    #     response = requests.post(url, headers=headers_mul_en, json=payload)
    #     return response.text
    # else:
    return response.json()[0]['generated_text']
