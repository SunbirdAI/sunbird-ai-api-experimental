import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
auth_type = 'token'  #@param ["token", "login-credentials"]
token = os.getenv('SUNBIRD_TOKEN')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def inference_request(payload):
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)
    translated_text = response.json()["text"]
    return translated_text
