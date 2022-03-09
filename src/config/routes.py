from fastapi import FastAPI

from src.modules.user import routes as user_router

def init_app(app: FastAPI) -> None:
    app.include_router(user_router.router)