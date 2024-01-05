from pydantic import BaseModel

class RequestBody(BaseModel):
    """ This is common body for 3 task: pos, ner, word segment
    :param sentence: str
    request body for all request to server
    including ner, pos task
    """
    sentence: str
