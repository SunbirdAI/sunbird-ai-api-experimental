from base import inference_request_en_mul, inference_request_mul_en


def create_payload_en_mul(text, target_language):
    payload = {
        "inputs": ">>" + str(target_language) + "<<" + str(text)
    }
    return payload


def create_payload_mul_en(text, target_language):
    payload = {
        "inputs": ">>" + str(target_language) + "<<" + str(text)
    }
    return payload


def translate(text, source_language=None, target_language=None):
    if source_language != 'eng' and target_language != 'eng':
        payload = create_payload_mul_en(text,
                                        source_language)
        response = inference_request_mul_en(payload)
        response = response[20:-3]
        payload = create_payload_en_mul(response,
                                        target_language)
        response = inference_request_en_mul(payload)
    elif source_language == 'eng':
        payload = create_payload_en_mul(text,
                                        target_language)
        response = inference_request_en_mul(payload)
    else:
        payload = create_payload_mul_en(text,
                                        source_language)
        response = inference_request_mul_en(payload)
    response = response[20:-3]
    return response


print(translate("Nituza ahari nyikiro", "nyn", "lug"))
