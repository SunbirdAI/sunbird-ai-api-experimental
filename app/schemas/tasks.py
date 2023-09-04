from pydantic import BaseModel


class TranslationResponse(BaseModel):
    text: str
    source_language: str | None = None


class TranslationRequest(BaseModel):
    source_language: str
    target_language: str
    text: str
