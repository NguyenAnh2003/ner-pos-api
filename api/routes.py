from fastapi import APIRouter, status, HTTPException
from api.request_body import RequestBody
from api.services import *
""" defining api router """

router = APIRouter()  # fast router


@router.post('/danangnlp/ner', status_code=status.HTTP_200_OK)
def ner_route(request: RequestBody):
    try:
        ner_result = ner_service(request.sentence)
        return ner_result
    except Exception as e:
        # Handle other general exceptions
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post('/danangnlp/pos', status_code=status.HTTP_200_OK)
def pos_route(request: RequestBody):
    """
    :param request: raw sentence
    :return: Pos response model
    """
    try:
        pos_result = pos_service(request.sentence)
        return pos_result
    except Exception as e:
        # Handle other general exceptions
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post('/danangnlp/wordsegment', status_code=status.HTTP_200_OK)
def segment_route(request: RequestBody):
    """ This function use external api then must be async function
    :param request: raw sentence
    :return: normalized sentence
    """
    # code for word segment
    return
