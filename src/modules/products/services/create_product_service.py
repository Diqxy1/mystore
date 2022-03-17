from sqlalchemy.orm import Session

from src.modules.users.entities.user import User
from src.modules.users.models import SignedUserModel

from src.modules.products.entities.product import Product
from src.modules.products.models import CreateProductModel, ProductPayloadModel

class CreateProductService:

    def __init__(self, db: Session):
        self._db = db

    def execute(self, model: CreateProductModel, current_user: SignedUserModel) -> ProductPayloadModel:
        print(current_user)
        db_product = Product(**model.dict())
        db_product.user_id = current_user.id
        
        self._db.add(db_product)
        self._db.commit()
        self._db.refresh(db_product)

        return ProductPayloadModel.from_orm(db_product)