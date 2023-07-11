from fastapi import FastAPI
from predictor.ner_predictor import ner_predictor
from predictor.pos_predictor import pos_predictor
app = FastAPI()

# uvicorn main:app --reload
# install requirement : pip install -r requirements.txt

@app.get('/')
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post('/nlp/ner')
async def ner_prediction(sentence: str):
    # tokens = await ner_predictor(sentence)
    return sentence

# predict pos
@app.post('/nlp/pos')
async def pos_prediction(sentence: str):
    tokens = await pos_predictor(sentence)
    return tokens
