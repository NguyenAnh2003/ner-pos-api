import fastapi
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

def setup_app():
    try:
        """ try cactch exception to catch error avoid crash app """
        app = FastAPI() # define app
        # allow app to access resource
        origin = "http://localhost:3000"
        # CORS config
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origin,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    except:
        # throw exception
        pass
    return app
