from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from api.request_body import RequestBody
from api.services import *
from api.response_model import *
from setup.setup_model import setup_model
from setup.setup_encoded import setup_encoded_data
from setup.sys_utils import setup_device
""" defining api router """

router = APIRouter()  # fast router

# setup model
device = setup_device() # setup device
enc_pos, enc_tag = setup_encoded_data() # encoded data
model = setup_model(enc_tag, enc_pos, device)

@router.post('/danangnlp/ner', response_model=ResponseNER, status_code=status.HTTP_200_OK)
def ner_route(request: RequestBody):
    """
    :param request: raw sentence
    :return: NER response model
    """
    try:
        ner_result = ner_service(request.sentence, model)
        response_data = ResponseNER(
            data=[WordNER(**item) for item in ner_result])
        return response_data
    except Exception as e:
        # Handle other general exceptions
        error_detail = "Internal Server Error: {}".format(str(e))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error_detail}
        )


@router.post('/danangnlp/pos', response_model=ResponsePOS, status_code=status.HTTP_200_OK)
def pos_route(request: RequestBody):
    """
    :param request: raw sentence
    :return: POS response model
    """
    try:
        pos_result = pos_service(request.sentence, model)
        response_data = ResponsePOS(
            data=[WordPOS(**item) for item in pos_result])
        return response_data
    except Exception as e:
        # Handle other general exceptions
        error_detail = "Internal Server Error: {}".format(str(e))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": error_detail}
        )


@router.post('/danangnlp/wordsegment', status_code=status.HTTP_200_OK)
def segment_route(request: RequestBody):
    """ This function use external api then must be async function
    :param request: raw sentence
    :return: normalized sentence
    """
    # code for word segment
    return
