from sqlalchemy.orm import Session

from src.modules.users.entities.user import User
from src.modules.users.models import SignedUserModel

from src.shared.exceptions.not_found_exception import NotFoundException

class GetCurrentUserService:

    def __init__(self, db: Session):
        self._db = db

    def execute(self, id: int) -> SignedUserModel:
        user_exist = self._db.query(User).filter(User.id == id).first()
        
        return SignedUserModel.from_orm(user_exist)