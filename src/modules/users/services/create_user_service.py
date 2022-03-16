from uuid import uuid4
from sqlalchemy.orm import Session

from src.modules.users.entities.user import User
from src.modules.users.models import UserModelPayload, CreateUserModel

from src.modules.address.entities.address import Address

from src.shared.middlewares.bcrypt import BcryptService
from src.shared.exceptions.bad_exception import BadRequestException

class CreateUserService:

    def __init__(self, db: Session):
        self._db = db
        self._bcrypt_service = BcryptService()
    
    def execute(self, model: CreateUserModel) -> UserModelPayload:
        user = self._db.query(User).filter(User.username == model.username).first()

        if user:
            raise BadRequestException(message='Nome de usuário já utilizado')

        #@TODO crypothografa senha
        db_user = User(**model.dict(exclude={"address"}))
        db_user.uuid = uuid4()

        hash_password = self._bcrypt_service.hash(model.password)
        db_user.password = hash_password

        db_address = Address(**model.address.dict())

        db_user.address = db_address

        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)

        return UserModelPayload.from_orm(db_user)