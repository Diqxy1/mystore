from fastapi import FastAPI

from src.modules.user import routes as user_router
from src.modules.two_factor import routes as two_factor_router

def init_app(app: FastAPI) -> None:
    app.include_router(user_router.router)
    app.include_router(two_factor_router.router)