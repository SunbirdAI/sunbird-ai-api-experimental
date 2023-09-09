from app.inference_services.base import inference_request
from app.inference_services.model import predicted_language


def create_payload(source_language_id, target_language_id, text):
    payload = {
            "source_language": source_language_id,
            "target_language": target_language_id,
            "text": text
    }
    return payload


def translate_text(text, source_language=None,  target_language=None):
    response_translate: str | None = None
    while source_language is None:
        source_language = predicted_language(text)

    if source_language != 'English' and target_language != 'English':
        payload = create_payload(source_language,'English', text)
        response_eng = inference_request(payload)
        payload = create_payload('English', target_language, response_eng)
        response_translate = inference_request(payload)

    elif source_language == 'eng':
        payload = create_payload(source_language,'English', text)
        response_translate = inference_request(payload)

    elif target_language == 'eng':
        payload = create_payload('English', target_language, text)
        response_translate = inference_request(payload)
    return response_translate


def create_chunks(text: str, chunk_size: int):
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
