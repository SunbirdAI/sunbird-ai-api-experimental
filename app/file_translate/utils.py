import io
import os
import re
import pypdf
from fastapi import HTTPException

from app.file_translate.file_process import FileUploader
from app.inference_services.model import predicted_language as predict_language
from app.inference_services.translate import translate_text \
    as translate_text_low_level


DATA_FOLDER = "data"  # folder to store txt files
CHUNK_SIZE = 200  # maximum characters per chunk
FILE_SPECS = {
    "FILE_TYPES": ("pdf", "txt"),
    "FILE_SIZE": 2 * 1024 * 1024  # 2 mb
}


def validate_uploaded_file(file_type: str, file_size: int):

    if file_type not in FILE_SPECS["FILE_TYPES"]:
        raise HTTPException(
            status_code=400,
            detail="Txt, pdf files expected"
        )

    if file_size > FILE_SPECS["FILE_SIZE"]:
        raise HTTPException(
            status_code=400,
            detail="File size sh'd be less than 2MB"
        )

    return


def parse_filename(filename: str):

    name = ".".join(filename.split(".")[:-1])  # files with many "."
    ext = filename.split(".")[-1]
    return name, ext


def extract_txt_frm_upload(content: bytes, filename: str, file_type: str):

    if file_type == "txt":
        return content.decode("utf-8")

    reader = pypdf.PdfReader(io.BytesIO(content))
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return re.sub(r'[^a-zA-Z0-9\s]+', ' ', text)  # replace non alpha with ' '


def create_txt_file(text: str, filename: str):

    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    with open(f"{DATA_FOLDER}/{filename}.txt", "w") as txt_file:
        txt_file.write(text)

    return


def get_chunks(text: str, chunk_size: int):
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


def translate_text(text: str, src_lang: str, trans_lang: str):
    return translate_text_low_level(
        text=text,
        source_language=src_lang,
        target_language=trans_lang
    )


def generate_translated_text(src_text: str, src_lang: str, trans_lang: str):

    src_text_chunks = get_chunks(src_text, chunk_size=CHUNK_SIZE)
    trans_text_chunks = []
    for chunk in src_text_chunks:
        trans_text_chunks.append(
            translate_text(
                text=chunk,
                src_lang=src_lang,
                trans_lang=trans_lang
            )
        )

    return " ".join(trans_text_chunks)


def generate_translated_file(
    src_text: str, src_lang: str, trans_lang: str, filename: str
):

    if src_lang is None:
        src_lang = predict_language(src_text)

    translated_text = generate_translated_text(
        src_text=src_text,
        src_lang=src_lang,
        trans_lang=trans_lang
    )

    translated_filename = f"{filename}_td"
    create_txt_file(text=translated_text, filename=translated_filename)

    file_uploader = FileUploader(translated_filename)
    file_uploader.upload_file()
    translated_file_url = file_uploader.retrieve_file_url()

    return translated_file_url


__all__ = [
    'parse_filename',
    'validate_uploaded_file',
    'extract_txt_frm_upload',
    'create_txt_file',
    'generate_translated_file'
]
