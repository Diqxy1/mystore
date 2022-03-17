from fastapi import FastAPI

from src.modules.users import routes as user_router
from src.modules.two_factor import routes as two_factor_router
from src.modules.products import routes as product_router
from src.modules.categories import routes as category_router

def init_app(app: FastAPI) -> None:
    app.include_router(user_router.router)
    app.include_router(two_factor_router.router)
    app.include_router(product_router.router)
    app.include_router(category_router.router)