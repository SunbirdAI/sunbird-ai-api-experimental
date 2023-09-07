from fastapi.testclient import TestClient
from app.api import app
from unittest.mock import MagicMock
from app.inference_services.translate import translate_text, predicted_language
client = TestClient(app)


def test_root_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_mul_mul(mocker):
    fake_response_eng = MagicMock()
    fake_response_eng = [{"generated_text": "Where are we heading?"}]
    mocker.patch('app.inference_services.base.inference_request_mul_en.reque'
                 'sts.post').return_value.text.return_value = fake_response_eng

    fake_response_mul = MagicMock()
    fake_response_mul = [{"generated_text": "Nituza nkahi?"}]
    mocker.patch('app.inference_services.base.inference_request_en_mul.reque'
                 'sts.post').return_value.text.return_value = fake_response_mul

    assert translate_text('Tuli wa', 'lug', 'nyn') == 'Nituza nkahi?'


def test_mul_eng(mocker):
    fake_response_eng = [{"generated_text": "Where are we heading?"}]
    mocker.patch('app.inference_services.base.inference_request_mul_en.reque'
                 'sts.post').return_value.text.return_value = fake_response_eng

    assert translate_text('Tuli wa', 'lug',
                          'eng') == "Where are we heading?"


def test_eng_mul(mocker):
    fake_response_mul = [{"generated_text": "Nituza nkahi?"}]
    mocker.patch('app.inference_services.base.inference_request_mul_en.reque'
                 'sts.post').return_value.text.return_value = fake_response_mul

    assert translate_text('Where are we heading?',
                          'eng', 'nyn') == "Nituza nkahi?"


def test_language_detect():
    assert predicted_language('Ninyisha omuka') == "nyn"
