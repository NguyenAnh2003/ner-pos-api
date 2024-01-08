from fastapi import status
from api.routes import router # setup defined router
from config.app_config import setup_app

# include defined app
app = setup_app()
app.include_router(router) # include route defined