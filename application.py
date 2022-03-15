from fastapi import FastAPI
from fastapi_jwt_auth.auth_jwt import AuthJWT

from src.config import routes, exceptions, auth

from src.config.env import env

description = """ 
    My Store - HEX CORE
"""

def create_app() -> FastAPI:
    docs_url = "/docs" if env.get_item("DEBUG", None) == "True" else None

    app = FastAPI(
        docs_url=docs_url,
        redoc_url='/',
        title='My Store',
        description=description,
        version="1.0"
    )

    routes.init_app(app)
    exceptions.init_app(app)

    return app

app = create_app()

@AuthJWT.load_config
def get_config():
    return auth.Settings()