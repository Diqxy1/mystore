from uuid import uuid4
from sqlalchemy.orm import Session

from src.modules.user.entities.user import User
from src.modules.user.models import UserModelPayload, CreateUserModel

from src.shared.exceptions.bad_exception import BadRequestException

class CreateUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, model: CreateUserModel) -> UserModelPayload:
        user = self._db.query(User).filter(User.username == model.username).first()

        if user:
            raise BadRequestException(message='Nome de usuário já utilizado')

        #@TODO crypothografa senha
        db_user = User(**model.dict())
        db_user.uuid = uuid4()

        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)

        return UserModelPayload.from_orm(db_user)