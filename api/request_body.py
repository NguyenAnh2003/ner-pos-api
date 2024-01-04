from pydantic import BaseModel

class RequestBody(BaseModel):
    """
    :param sentence: str
    request body for all request to server
    including ner, pos task
    """
    sentence: str
