from fastapi import FastAPI
from setup_predictor.setup_predictor import *
from setup_predictor.main_predictor import create_word_list
from api.request_body import RequestBody

app = FastAPI()
# uvicorn main:app --reload
# uvicorn main:app --port 8001 --reload
# install requirement : pip install -r requirements.txt

@app.get('/')
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post('/nlp/ner')
def ner_prediction(req: RequestBody):
    tokens = ner_predictor(req.string)
def ner_prediction(req: Req):
    tokens = ner_predictor(req.string)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        color = sublist[2]
        result.append({"word": word, "tag": tag, "color": color})
    return result

# predict pos
@app.post('/nlp/pos')
def pos_prediction(req: RequestBody):
    tokens = pos_predictor(req.string)
def pos_prediction(req: Req):
    tokens = pos_predictor(req.string)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        result.append({"word": word, "tag": tag})
    return result

@app.post('/nlp/segment')
def segment(req: RequestBody):
    tokens = [create_word_list(req.sentence)]
    return tokens