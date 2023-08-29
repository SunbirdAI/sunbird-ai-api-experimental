from fastapi.testclient import TestClient
from utils.api import app

client = TestClient(app)
def test_root_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}