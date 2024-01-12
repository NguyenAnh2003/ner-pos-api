from pydantic import BaseModel
from typing import List

class WordNER(BaseModel):
    """ structure for one word with NER 
    attributes:
        word (str): The actual word in the text input.
        tag (str): The NER tag associated with the word.
        color (str): A color code or name associated with the NER tag for visualization purposes.
    """
    word: str
    tag: str
    color: str


class ResponseNER(BaseModel):
    """ response structure for ner result
    attributes:
        data (List[WordNER]): A list of WordNER instances representing the NER tagging results for each word.
    """
    data: List[WordNER]


class WordPOS(BaseModel):
    """ structure for one word with POS
    attributes:
        word (str): The actual word in the text input.
        tag (str): The POS tag associated with the word
    """
    word: str
    tag: str


class ResponsePOS(BaseModel):
    """ reponse structure for pos result
    attributes:
        data (List[WordPOS]): A list of WordPOS instances representing the POS tagging results for each word.
    """
    data: List[WordPOS]
