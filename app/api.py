from app.schemas.tasks import TranslationRequest, TranslationResponse
from app.inference_services.translate import (translate_text,
                                              long_text_translation,
                                              predicted_language)
from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from datetime import datetime as dt
from app.file_translate.utils import parse_filename, validate_uploaded_file, \
    extract_txt_frm_upload, create_txt_file, generate_translated_file

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/translate", response_model=TranslationResponse)
def translate(translation_request: TranslationRequest):
    # This is the pont where it checks if the source language is not Null
    source_language = None
    if translation_request.source_language == "":
        source_language = predicted_language(translation_request.text)

    if len(translation_request.text) < 200:
        response = translate_text(translation_request.text,
                                  translation_request.source_language,
                                  translation_request.target_language)
    else:
        response = long_text_translation(translation_request.text,
                                         translation_request.source_language,
                                         translation_request.target_language)

    return TranslationResponse(text=response, source_language=source_language)


# file translate endpoint
@app.post("/api/file-translate")
async def upload_file(
    file: Annotated[UploadFile, File()],
    src_lang: Annotated[str, Form()],
    trans_lang: Annotated[str, Form()]
):

    filename, file_type = parse_filename(file.filename)
    filename = f'{filename}_{dt.now()}'
    validate_uploaded_file(file_type=file_type, file_size=file.size)

    content = await file.read()
    text = extract_txt_frm_upload(
        content=content, filename=filename, file_type=file_type)

    create_txt_file(text=text, filename=filename)

    translated_file_url = generate_translated_file(
        src_text=text,
        src_lang=src_lang,
        trans_lang=trans_lang,
        filename=filename
    )

    return {
        'translated-file': translated_file_url
    }
