from fastapi.testclient import TestClient
from app.api import app
from app.inference_services.translate import translate_text, predicted_language
client = TestClient(app)


def test_root_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_mul_mul(mocker):
    fake_response_eng = 'Where are we heading?'
    mocker.patch('requests.post').return_value.json['text'].return_value = fake_response_eng

    fake_response_mul = 'Nituza nkahi?'
    mocker.patch('requests.post').return_value.json['text'].return_value = fake_response_mul

    assert translate_text('Tuli wa', 'Luganda', 'Runyankole') == 'Nituza nkahi?'


def test_mul_eng(mocker):
    fake_response_eng = 'Where are we heading?'
    mocker.patch('requests.post').return_value.json['text'].return_value = fake_response_eng
    assert translate_text('Tuli wa', 'Luganda',
                          'English') == "Where are we heading?"


def test_eng_mul(mocker):
    fake_response_mul = 'Nituza nkahi?'
    mocker.patch('requests.post').return_value.json['text'].return_value = fake_response_mul
    p = str(translate_text('Where are we heading?',
                   'English', 'Runyankole'))
    print(p)
    assert p == "Nituza nkahi?"


def test_language_detect():
    assert predicted_language('Ninyisha omuka') == "nyn"
