from app.inference_services.base import (inference_request_en_mul,
                                         inference_request_mul_en)
from app.inference_services.language_ID_Impl import predicted_language


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


def translate_text(text, source_language=None,  target_language=None):
    def translate_text():
        if source_language != 'eng' and target_language != 'eng':
            payload = create_payload_mul_en(text)
            response_eng = inference_request_mul_en(payload)
            response_eng = response_eng[20:-3]
            print(response_eng)
            payload = create_payload_en_mul(response_eng,
                                            target_language)
            response = inference_request_en_mul(payload)

        elif source_language == 'eng':
            payload = create_payload_en_mul(text,
                                            target_language)
            response = inference_request_en_mul(payload)

        elif target_language == 'eng':
            payload = create_payload_mul_en(text)
            response = inference_request_mul_en(payload)
        response = response[20:-3]
        return response

    while True:
        try:
            if (len(text) > 3 and len(text) < 5000):
                if source_language is None:
                    source_language = predicted_language(text)
                    response_text = translate_text()
                else:
                    response_text = translate_text()
                print('Please')
            return response_text
        except ValueError:
            response_text = ("Please enter a valid text longer than "
                             "3 characters and less than 5000 characters")
            return response_text


def create_chunks(text: str, chunk_size: int):
    # TODO: currently chunk size has to be larger than first word in text
    chunks = []
    last_char_index = len(text)
    chunk_start = 0
    chunk_stop = 0

    while chunk_stop != last_char_index:

        chunk_stop += chunk_size

        if chunk_stop > last_char_index:
            chunk_stop = last_char_index

        if chunk_stop != last_char_index:
            while text[chunk_stop] != " ":
                chunk_stop -= 1

        chunks.append(text[chunk_start:chunk_stop])

        chunk_start = chunk_stop+1

    return chunks


def long_text_translation(src_text: str, src_lang: str, trans_lang: str):
    src_text_chunks = create_chunks(src_text, chunk_size=200)
    trans_text_chunks = []
    for chunk in src_text_chunks:
        trans_text_chunks.append(
                         translate_text(text=chunk,
                                        target_language=trans_lang,
                                        source_language=src_lang))
    return " ".join(trans_text_chunks)
