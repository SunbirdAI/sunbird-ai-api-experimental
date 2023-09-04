from fastapi import FastAPI
from app.schemas.tasks import TranslationRequest, TranslationResponse
from app.inference_services.translate import translate_text


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/translate")
def translate(translation_request: TranslationRequest):
    response = translate_text(translation_request.text,
                              translation_request.source_language,
                              translation_request.target_language)
    print(response)
    return TranslationResponse(text=response)
