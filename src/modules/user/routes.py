from typing import List, Optional
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from src.config.database import get_database

from src.modules.user.models import UserModelPayload, CreateUserModel
from src.modules.user.services.create_user_service import CreateUserService
from src.modules.user.services.list_user_service import ListUserService
from src.modules.user.services.detail_user_service import DetailUserService
from src.modules.user.services.delete_user_service import DeleteUserService

from src.shared.exceptions.precondition_failed_exception import PreconditionFailedException

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
@router.get('/', response_model=List[UserModelPayload])
def list_user(
    key: str = Header(None),
    db: Session = Depends(get_database)
):
    #@TODO fazer chave aleatoria para travar a rota
    if key != '123':
        raise PreconditionFailedException(message='Authorização invalida')
    
    service = ListUserService(db)
    return service.execute()

# GET /users/uuid
@router.get('/{uuid}', response_model=UserModelPayload)
def detail_user(
    uuid: str,
    db: Session = Depends(get_database)
):
    service = DetailUserService(db)
    return service.execute(uuid)

# DELETE /users/uuid
@router.delete('/{uuid}')
def delete_user(
    uuid: str,
    db: Session = Depends(get_database)
):
    service = DeleteUserService(db)
    return service.execute(uuid)