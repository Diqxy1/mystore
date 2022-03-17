from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_jwt_auth.auth_jwt import AuthJWT

from src.config.database import get_database

from src.modules.categories.models import CreateCategoryModel, CategoryPayloadModel
from src.modules.categories.services.create_category_service import CreateCategoryService
from src.modules.categories.services.list_category_service import ListCategoryService
from src.modules.categories.services.delete_category_service import DeleteCategoryService, DeleteBaseModel

from src.modules.users.services.get_current_user_service import GetCurrentUserService

from src.shared.middlewares.jwt_swagger import JWTBearer


router = APIRouter(
    prefix='/categories',
    tags=['Categories']
)

@router.post('/', response_model=CategoryPayloadModel)
def create_category(
    model: CreateCategoryModel,
    db: Session = Depends(get_database)
):
    service = CreateCategoryService(db)
    return service.execute(model)

@router.get('/', response_model=List[CategoryPayloadModel])
def list_categories(
    db: Session = Depends(get_database)
):
    service = ListCategoryService(db)
    return service.execute()

@router.delete('/{category_id}', response_model=DeleteBaseModel)
def list_categories(
    category_id: int,
    db: Session = Depends(get_database),
):
    service = DeleteCategoryService(db)
    return service.execute(category_id)