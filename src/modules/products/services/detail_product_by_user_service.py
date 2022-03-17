from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.modules.products.models import ProductPayloadModel
from src.modules.products.entities.product import Product

from src.modules.users.models import SignedUserModel

from src.shared.exceptions.not_found_exception import NotFoundException

class DetailProductByUserService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, product_id: int, current_user: SignedUserModel) -> ProductPayloadModel:
        product = self._db.query(Product).filter(and_(
            Product.id == product_id,
            Product.user_id == current_user.id
        )).first()

        if not product:
            raise NotFoundException(message='Produto não encontrado')
        
        return ProductPayloadModel.from_orm(product)