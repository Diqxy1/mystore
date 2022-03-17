from typing import List
from sqlalchemy.orm import Session

from src.modules.categories.models import CategoryPayloadModel
from src.modules.categories.entities.category import Category

class ListCategoryService:

    def __init__(self, db: Session):
        self._db = db

    def execute(self) -> List[CategoryPayloadModel]:
        categories = self._db.query(Category).all()

        for category in categories:
            return [CategoryPayloadModel.from_orm(category) if category else None]