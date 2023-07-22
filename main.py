from fastapi import FastAPI
from predictor.ner_predictor import ner_predictor
from predictor.pos_predictor import pos_predictor
from fastapi.responses import JSONResponse
from classes.pos_req import PosReq
from classes.ner_req import NerReq
from classes.Req import Req
import json


app = FastAPI()
# uvicorn main:app --reload
# uvicorn main:app --port 8001 --reload
# install requirement : pip install -r requirements.txt

@app.get('/')
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post('/nlp/ner')
def ner_prediction(req: Req):
    tokens = ner_predictor(req)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        color = sublist[2]
        result.append({"word": word, "tag": tag, "color": color})
    return result

# predict pos
@app.post('/nlp/pos')
def pos_prediction(req: Req):
    tokens = pos_predictor(req)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        result.append({"word": word, "tag": tag})
    return result
