from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_jwt_auth.auth_jwt import AuthJWT

from src.config.database import get_database

from src.modules.products.models import CreateProductModel, ProductPayloadModel

from src.modules.products.services.create_product_service import CreateProductService
from src.modules.products.services.list_product_service import ListProductsService
from src.modules.products.services.list_product_by_user_service import ListProductsByUserService
from src.modules.products.services.detail_product_by_user_service import DetailProductByUserService
from src.modules.products.services.delete_product_by_user_service import DeleteProductByUserService, DeleteBaseModel

from src.modules.users.services.get_current_user_service import GetCurrentUserService

from src.shared.middlewares.jwt_swagger import JWTBearer


router = APIRouter(
    prefix='/products',
    tags=['Products']
)

@router.post('/', response_model=ProductPayloadModel, dependencies=[Depends(JWTBearer())])
def create_product(
    model: CreateProductModel,
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_database)
):
    Authorize.jwt_required()

    current_user = GetCurrentUserService(db).execute(Authorize.get_jwt_subject())

    service = CreateProductService(db)
    return service.execute(model, current_user)

@router.get('/', response_model=List[ProductPayloadModel])
def list_products(
    db: Session = Depends(get_database)
):
    service = ListProductsService(db)
    return service.execute()

@router.get('/my-products/', response_model=List[ProductPayloadModel], dependencies=[Depends(JWTBearer())])
def list_products_by_user(
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_database)
):
    Authorize.jwt_required()

    current_user = GetCurrentUserService(db).execute(Authorize.get_jwt_subject())

    service = ListProductsByUserService(db)
    return service.execute(current_user)

@router.get('/detail-product/{product_id}', response_model=ProductPayloadModel, dependencies=[Depends(JWTBearer())])
def detail_product_by_user(
    product_id: int,
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_database)
):
    Authorize.jwt_required()

    current_user = GetCurrentUserService(db).execute(Authorize.get_jwt_subject())

    service = DetailProductByUserService(db)
    return service.execute(product_id, current_user)

@router.delete('/delete-by-user/{id}', response_model=DeleteBaseModel, dependencies=[Depends(JWTBearer())])
def delete_product_by_user(
    product_id: int,
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_database)
):
    Authorize.jwt_required()

    current_user = GetCurrentUserService(db).execute(Authorize.get_jwt_subject())

    service = DeleteProductByUserService(db)
    return service.execute(product_id, current_user)