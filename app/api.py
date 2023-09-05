from fastapi import FastAPI
from app.schemas.tasks import TranslationRequest, TranslationResponse
from app.inference_services.translate import (translate_text,
                                              long_text_translation,
                                              predicted_language)


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
