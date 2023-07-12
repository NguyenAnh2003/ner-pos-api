from fastapi import FastAPI
from predictor.ner_predictor import ner_predictor
from predictor.pos_predictor import pos_predictor
from fastapi.responses import JSONResponse
import json


app = FastAPI()
# uvicorn main:app --reload
# install requirement : pip install -r requirements.txt

@app.get('/')
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post('/nlp/ner')
def ner_prediction(sentence: str):
    tokens = ner_predictor(sentence)
    x = [' thủ_đô ', ('Việt_Nam', 'Địa điểm', '#84a59d'), ' là ', ('Hà_Nội', 'Địa điểm', '#84a59d')]

    return tokens

# predict pos
@app.post('/nlp/pos')
def pos_prediction(sentence: str):
    tokens = pos_predictor(sentence)
    return tokens
