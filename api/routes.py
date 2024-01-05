from fastapi import APIRouter, status
from request_body import RequestBody
from services import *
""" defining api router """

router = APIRouter() # fast router

@router.post('/danangnlp/ner', status_code=status.HTTP_200_OK)
def ner_route(request: RequestBody):
    ner_result = ner_service(request.sentence)
    return ner_result

@router.post('/danangnlp/pos', status_code=status.HTTP_200_OK)
def pos_route(request: RequestBody):
    """
    :param request: raw sentence
    :return: Pos response model
    """
    pos_result = pos_service(request.sentence)
    return pos_result

@router.post('/danangnlp/wordsegment', status_code=status.HTTP_200_OK)
def segment_route(request: RequestBody):
    """ This function use external api then must be async function
    :param request: raw sentence
    :return: normalized sentence
    """
    # code for word segment
    return