from fastapi.testclient import TestClient
from app.api import app
import json

client = TestClient(app)


def test_root_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_detect():
    content = {
                "source_language": "",
                "target_language": "nyn",
                "text": "Where are we going"
                }

    response = client.post(
        url='/detect',
        content=json.dumps(content)
    )

    assert response.status_code == 200
    assert response.json()['lang'] == 'eng'