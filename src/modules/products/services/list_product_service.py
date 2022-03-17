from itertools import product
from typing import List
from sqlalchemy.orm import Session

from src.modules.products.models import ProductPayloadModel
from src.modules.products.entities.product import Product

class ListProductsService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self) -> List[ProductPayloadModel]:
        products = self._db.query(Product).all()

        for product in products:
            return [ProductPayloadModel.from_orm(product) if product else None]