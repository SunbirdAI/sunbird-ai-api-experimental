from pydantic import BaseModel, Field


class TranslationResponse(BaseModel):
    text: str
    source_language: str = None


class TranslationRequest(BaseModel):
    source_language: str = None
    target_language: str
    text: str = Field(max_length=5000, min_length=3)
