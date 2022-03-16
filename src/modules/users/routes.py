from typing import List
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from fastapi_jwt_auth.auth_jwt import AuthJWT

from src.config.database import get_database

from src.modules.users.models import (
    UserModelPayload, 
    CreateUserModel,
    AuthResponseModel,
    LoginUserModel
)
from src.modules.users.services.create_user_service import CreateUserService
from src.modules.users.services.list_user_service import ListUserService
from src.modules.users.services.detail_user_service import DetailUserService
from src.modules.users.services.delete_user_service import DeleteUserService
from src.modules.users.services.login_user_service import LoginUserService

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
@router.get('/{uuid}/', response_model=UserModelPayload, dependencies=[Depends(JWTBearer())])
def detail_user(
    uuid: str,
    db: Session = Depends(get_database),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    service = DetailUserService(db)
    return service.execute(uuid)

# DELETE /users/uuid
@router.delete('/{uuid}/', dependencies=[Depends(JWTBearer())])
def delete_user(
    uuid: str,
    db: Session = Depends(get_database),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    service = DeleteUserService(db)
    return service.execute(uuid)

# POST /users/login
@router.post('/login/', response_model=AuthResponseModel)
def login_user(
    model: LoginUserModel,
    db: Session = Depends(get_database)
):
    service = LoginUserService(db)
    return service.execute(model)


""" @router.post('/phone/', response_model=PhoneModelResponse)
def create_phone(
    model: CreatePhoneModel,
    db: Session = Depends(get_database)
):
    service = CreatePhoneService(db)
    return service.execute(model) """

""" @router.post('/phone/activate/', response_model=UserModelPayload)
def phone_activate(
    model: ActivateTwoFactorModel,
    db: Session = Depends(get_database)
):
    service = ActivatePhoneService(db)
    return service.execute(model)

@router.post('/email')
def phone_activate(
    model: CreateEmailModel,
    db: Session = Depends(get_database)
):
    service = CreateEmailService(db)
    return service.execute(model) """