from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload

@app.get("/")
async def index():
    return {"hello world": "hello from nguyenanh"}

# predict ner
@app.post("/nlp/ner")
async def ner_prediction(sentence: str):
    pass

# predict pos
@app.post("/nlp/pos")
async def pos_prediction(sentence: str):
    pass
