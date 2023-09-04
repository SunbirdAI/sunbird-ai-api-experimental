from pydantic import BaseModel


class TranslationResponse(BaseModel):
    text: str


class TranslationRequest(BaseModel):
    source_language: str
    target_language: str
    text: str
