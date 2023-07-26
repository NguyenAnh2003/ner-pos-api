from fastapi import FastAPI
from predictor.ner_predictor import ner_predictor
from predictor.pos_predictor import pos_predictor
from classes.Req import Req
from predictor.main_predictor import create_word_list

app = FastAPI()
# uvicorn main:app --reload
# install requirement : pip install -r requirements.txt

@app.get('/')
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post('/nlp/ner')
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
def pos_prediction(req: Req):
    tokens = pos_predictor(req.string)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        result.append({"word": word, "tag": tag})
    return result

@app.post('/nlp/segment')
def word_segment(req: Req):
    tokens = [create_word_list(req.string)]
    return tokens