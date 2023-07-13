from pydantic import BaseModel
class NerReq(BaseModel):
    sentence: str