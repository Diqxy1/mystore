from fastapi import FastAPI

from src.config import routes, exceptions

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