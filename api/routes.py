from fastapi import APIRouter, status
from request_body import RequestBody
from services import *
""" defining api router """

router = APIRouter() # fast router

@router.post('/danangnlp/ner', status_code=status.HTTP_201_CREATED)
async def entity_extraction(request: RequestBody):
    ner_result = await ner_service(request.sentence)
    return ner_result

@router.post('/danangnlp/pos', status_code=status.HTTP_201_CREATED)
async def pos_tag(request: RequestBody):
    """
    :param request: raw sentence
    :return: Pos response model
    """
    pos_result = await pos_service(request.sentence)
    return pos_result