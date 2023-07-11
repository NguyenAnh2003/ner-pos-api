from fastapi import FastAPI
from predictor.ner_predictor import ner_predictor
from predictor.pos_predictor import pos_predictor
app = FastAPI()

# uvicorn main:app --reload

@app.get("/")
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post("/nlp/ner")
async def ner_prediction(sentence: str):
    return ner_predictor(sentence)

# predict pos
@app.post("/nlp/pos")
async def pos_prediction(sentence: str):
    return pos_predictor(sentence)
