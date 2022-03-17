from typing import List
from sqlalchemy.orm import Session

from src.modules.products.entities.product import Product
from src.modules.products.models import ProductPayloadModel

from src.modules.users.models import SignedUserModel


class ListProductsByUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, current_user: SignedUserModel) -> List[ProductPayloadModel]:
        products_by_user = self._db.query(Product).filter(Product.user_id == current_user.id).all()

        for product in products_by_user:

            return [ProductPayloadModel.from_orm(product) if product else None]