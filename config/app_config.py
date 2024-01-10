import fastapi
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
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
        app.include_router(router)
        return app
    except:
        # throw exception
        raise HTTPException(status_code=500, detail="Cannot host app")