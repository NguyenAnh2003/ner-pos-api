from fastapi import APIRouter
from request_body import RequestBody
from service import *
""" defining api router """

router = APIRouter() # fast router

@router.post('/danangnlp/ner')
def entity_extraction(request: RequestBody):
    ner_result = ner_service(request.sentence)
    return ner_result

@router.post('/danangnlp/pos')
def pos_tag(request: RequestBody):
    pos_result = pos_service(request.sentence)
    return pos_result