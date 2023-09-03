from pydantic import BaseModel
from enum import Enum


class Language(str, Enum):
    acholi = "ach"
    ateso = "teo"
    english = "eng"
    luganda = "lug"
    lugbara = "lgg"
    runyankole = "nyn"


class translation_response(BaseModel):
    text: str
    source_language: Language | None = None


class translation_request(BaseModel):
    source_language: Language | None = None
    target_language: Language
    text: str
