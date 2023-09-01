from base import inference_request_en_mul, inference_request_mul_en
from language_ID_Impl.model import predicted_language


def create_payload_en_mul(text, target_language):
    payload = {
        "inputs": ">>" + str(target_language) + "<<" + str(text)
    }
    return payload


def create_payload_mul_en(text):
    payload = {
        "inputs": str(text)
    }
    return payload


def translate(text, target_language=None, source_language=None):
    def translate_text():
        if source_language != 'eng' and target_language != 'eng':
            payload = create_payload_mul_en(text)
            response_eng = inference_request_mul_en(payload)
            response_eng = response_eng[20:-3]
            payload = create_payload_en_mul(response_eng,
                                            target_language)
            response = inference_request_en_mul(payload)
            print("mult-mult")

        elif source_language == 'eng':
            payload = create_payload_en_mul(text,
                                            target_language)
            response = inference_request_en_mul(payload)
            print("eng-mult")

        elif target_language == 'eng':
            payload = create_payload_mul_en(text)
            response = inference_request_mul_en(payload)
            print("mult-eng")
        response = response[20:-3]
        return response

    if source_language is None:
        source_language = predicted_language(text)
        response_text = translate_text()
    else:
        response_text = translate_text()
    return response_text


print(translate("Tudda eka leero", "nyn", None))
