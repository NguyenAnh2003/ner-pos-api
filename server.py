from fastapi import FastAPI
from api.routes import router # setup defined router
# define app
app = FastAPI()

app.include_router(router)