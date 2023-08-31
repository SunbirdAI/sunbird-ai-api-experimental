from app.inference_services.base import inference_request


def create_payload(text, source_language=None, target_language=None):
    payload = {
        "instances": [
            {
                "sentence": text,
                "target_language": target_language,
                "source_language": source_language
            }
        ]
    }
    return payload


def translate(text, source_language=None, target_language=None):
    payload = create_payload(text,
                             source_language,
                             target_language)
    response = inference_request(payload).json()
    return response


print(translate("Where are we", "English", "Luganda"))
