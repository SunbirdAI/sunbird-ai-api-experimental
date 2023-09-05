from fastapi.testclient import TestClient
from app.api import app
import json

client = TestClient(app)


def test_root_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


# def test_mul_mul():
#     content = {
#                 "source_language": "nyn",
#                 "target_language": "lug",
#                 "text": "Turi ahu."
#                 }
#
#     response = client.post(
#         url='/translate',
#         content=json.dumps(content)
#     )
#
#     assert response.status_code == 200
#     assert response.json()['text'] == "N'olwekyo, tuli mu mbeera ng'eyo."
#     assert response.json()['source_language'] is None
#
#
# def test_mul_eng():
#     content = {
#                 "source_language": "nyn",
#                 "target_language": "eng",
#                 "text": "Turi ahu."
#                 }
#
#     response = client.post(
#         url='/translate',
#         content=json.dumps(content)
#     )
#
#     assert response.status_code == 200
#     assert response.json()['text'] == "We are at a crossroads."
#     assert response.json()['source_language'] is None
#
#
# def test_eng_mul():
#     content = {
#                 "source_language": "eng",
#                 "target_language": "nyn",
#                 "text": "Where are we."
#                 }
#
#     response = client.post(
#         url='/translate',
#         content=json.dumps(content)
#     )
#
#     assert response.status_code == 200
#     assert response.json()['text'] == "Turi ahu."
#     assert response.json()['source_language'] is None
#
#
# def test_language_detect():
#     content = {
#                 "source_language": "",
#                 "target_language": "lug",
#                 "text": "Turi ahu."
#                 }
#
#     response = client.post(
#         url='/translate',
#         content=json.dumps(content)
#     )
#
#     assert response.status_code == 200
#     assert response.json()['text'] == "N'olwekyo, tuli mu mbeera ng'eyo."
#     assert response.json()['source_language'] == "nyn"
