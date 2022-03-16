from sqlalchemy.orm import Session

from src.modules.users.entities.user import User
from src.modules.users.models import UserModelPayload

from src.shared.exceptions.bad_exception import BadRequestException

class DetailUserService:
    
    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, uuid: str) -> UserModelPayload:
        user = self._db.query(User).filter(User.uuid == uuid).first()

        if not user:
            raise BadRequestException(message='Usuário não encontrado')
        
        return UserModelPayload.from_orm(user)