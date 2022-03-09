from typing import List
from sqlalchemy.orm import Session

from src.modules.user.entities.user import User
from src.modules.user.models import UserModelPayload


class ListUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self) -> List[UserModelPayload]:
        users = self._db.query(User).all()

        for user in users:
            return [UserModelPayload.from_orm(user) if user else None]