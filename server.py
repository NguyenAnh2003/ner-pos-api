from fastapi import FastAPI
from api.routes import router # setup defined router
# define app
app = FastAPI() # get app config

app.include_router(router) # include route defined