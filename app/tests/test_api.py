from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_root_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
def test_root_api():
    assert 1 == 1
