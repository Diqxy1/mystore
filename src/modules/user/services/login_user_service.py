from fastapi_jwt_auth.auth_jwt import AuthJWT
from sqlalchemy.orm import Session
from datetime import timedelta

from src.modules.user.entities.user import User
from src.modules.user.models import (
    LoginUserModel, 
    UserModelPayload,
    AuthResponseModel
)

from src.shared.middlewares.bcrypt import BcryptService
from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.bad_exception import BadRequestException

class LoginUserService:

    def __init__(self, db: Session):
        self._db = db
        self._bcrypt_service = BcryptService()
        self._cryptography_service = AuthJWT()
    
    def execute(self, model: LoginUserModel) -> AuthResponseModel:
        user = self.make_validations(model.username, model.password)
        
        # JWT
        expires = timedelta(hours=2)
        expires_refresh = timedelta(hours=4)
        acess_token = self._cryptography_service.create_access_token(subject=user.id, expires_time=expires)
        refresh_token = self._cryptography_service.create_refresh_token(subject=user.id, expires_time=expires_refresh)
        auth_response = AuthResponseModel(
            id=user.id,
            username=user.username,
            acess_token=acess_token,
            refresh_acess_token=refresh_token
        )

        return auth_response

    def make_validations(self, username: str, password: str) -> UserModelPayload:
        user = self._db.query(User).filter(User.username == username).first()

        if not user:
            raise NotFoundException(message='Usuário não encontrado')
        
        if not self._bcrypt_service.verify(password, user.password):
            raise BadRequestException(message='Senha incorreta')

        return user