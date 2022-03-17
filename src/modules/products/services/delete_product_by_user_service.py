from pydantic import BaseModel
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.modules.users.models import SignedUserModel

from src.modules.products.entities.product import Product


class DeleteBaseModel(BaseModel):
    message: str = 'Produto deletado com sucesso'


class DeleteProductByUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, product_id: int, current_user: SignedUserModel) -> DeleteBaseModel:
        self._db.query(Product).filter(and_(
            Product.user_id == current_user.id,
            Product.id == product_id
        )).delete()

        return DeleteBaseModel
