from typing import List
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from fastapi_jwt_auth.auth_jwt import AuthJWT

from src.config.database import get_database

from src.modules.user.models import (
    UserModelPayload, 
    CreateUserModel,
    AuthResponseModel,
    LoginUserModel
)
from src.modules.user.services.create_user_service import CreateUserService
from src.modules.user.services.list_user_service import ListUserService
from src.modules.user.services.detail_user_service import DetailUserService
from src.modules.user.services.delete_user_service import DeleteUserService
from src.modules.user.services.login_user_service import LoginUserService

from src.shared.exceptions.precondition_failed_exception import PreconditionFailedException
from src.shared.middlewares.jwt_swagger import JWTBearer

router = APIRouter(
    prefix='/users',
    tags=['User']
)

# POST /users
@router.post('/', response_model=UserModelPayload)
def create_user(
    model: CreateUserModel,
    db: Session = Depends(get_database)
):
    service = CreateUserService(db)
    return service.execute(model)


# GET /users
@router.get('/', response_model=List[UserModelPayload], dependencies=[Depends(JWTBearer())])
def list_user(
    key: str = Header(None),
    db: Session = Depends(get_database),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    #@TODO fazer chave aleatoria para travar a rota
    if key != '123':
        raise PreconditionFailedException(message='Authorização invalida')
    
    service = ListUserService(db)
    return service.execute()

# GET /users/uuid
@router.get('/{uuid}', response_model=UserModelPayload, dependencies=[Depends(JWTBearer())])
def detail_user(
    uuid: str,
    db: Session = Depends(get_database),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    service = DetailUserService(db)
    return service.execute(uuid)

# DELETE /users/uuid
@router.delete('/{uuid}', dependencies=[Depends(JWTBearer())])
def delete_user(
    uuid: str,
    db: Session = Depends(get_database),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    service = DeleteUserService(db)
    return service.execute(uuid)

# POST /users/login
@router.post('/login', response_model=AuthResponseModel)
def login_user(
    model: LoginUserModel,
    db: Session = Depends(get_database)
):
    service = LoginUserService(db)
    return service.execute(model)
