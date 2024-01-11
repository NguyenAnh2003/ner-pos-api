from pydantic import BaseModel
from typing import List

class WordNER(BaseModel):
    word: str
    tag: str
    color: str


class ResponseNER(BaseModel):
    data: List[WordNER]


class WordPOS(BaseModel):
    word: str
    tag: str

class ResponsePOS(BaseModel):
    data: List[WordPOS]
