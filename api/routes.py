from fastapi import APIRouter, status, HTTPException, Depends
from api.request_body import RequestBody
from api.services import *
from api.response_model import *
""" defining api router """

router = APIRouter()  # fast router

@router.post('/danangnlp/ner', response_model=ResponseNER, status_code=status.HTTP_200_OK)
def ner_route(request: RequestBody):
    """
    :param request: raw sentence
    :return: NER response model
    """
    try:
        ner_result = ner_service(request.sentence)
        response_data = ResponseNER(
            data=[WordNER(**item) for item in ner_result])
        return response_data
    except Exception as e:
        # Handle other general exceptions
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post('/danangnlp/pos', response_model=ResponsePOS, status_code=status.HTTP_200_OK)
def pos_route(request: RequestBody):
    """
    :param request: raw sentence
    :return: POS response model
    """
    try:
        pos_result = pos_service(request.sentence)
        response_data = ResponsePOS(
            data=[WordPOS(**item) for item in pos_result])
        return response_data
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
