from fastapi import FastAPI
from app.schemas.tasks import translation_request, translation_response
from app.inference_services.translate import (translate_text,
                                              long_text_translation)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/translate", response_model=translation_response)
async def translate(translation_request=translation_request):
    source_language = translation_request.source_language
    if translation_request.text > 200:
        response = translate_text(translation_request.text,
                                  translation_request.source_language,
                                  translation_request.target_language)
    else:
        response = long_text_translation(translation_request.text,
                                         translation_request.source_language,
                                         translation_request.target_language)
    return translation_response(text=response,
                                source_language=source_language)
