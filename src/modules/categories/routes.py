from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_jwt_auth.auth_jwt import AuthJWT

from src.config.database import get_database

from src.modules.categories.models import CreateCategoryModel, CategoryPayloadModel
from src.modules.categories.services.create_category_service import CreateCategoryService

from src.modules.users.services.get_current_user_service import GetCurrentUserService

from src.shared.middlewares.jwt_swagger import JWTBearer


router = APIRouter(
    prefix='/categories',
    tags=['Categories']
)

@router.post('/', response_model=CategoryPayloadModel)
def create_product(
    model: CreateCategoryModel,
    db: Session = Depends(get_database)
):
    service = CreateCategoryService(db)
    return service.execute(model)