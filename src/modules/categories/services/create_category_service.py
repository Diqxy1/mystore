from sqlalchemy.orm import Session

from src.modules.categories.entities.category import Category
from src.modules.categories.models import CategoryPayloadModel, CreateCategoryModel


class CreateCategoryService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, model: CreateCategoryModel) -> CategoryPayloadModel:
        
        db_category = Category(**model.dict())

        self._db.add(db_category)
        self._db.commit()
        self._db.refresh(db_category)

        return CategoryPayloadModel.from_orm(db_category)