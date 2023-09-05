from pydantic import BaseModel, Field
# from enum import Enum

# TODO: Include Enum
# class Language(str, Enum):
#     Acholi = "ach"
#     Ateso = "teo"
#     English = "eng"
#     Luganda = "lug"
#     Lugbara = "Lgg"
#     Runyankole = "nyn"


class TranslationResponse(BaseModel):
    text: str
    source_language: str | None = None


class TranslationRequest(BaseModel):
    source_language: str | None = None
    target_language: str
    text: str = Field(max_length=5000, min_length=3)
