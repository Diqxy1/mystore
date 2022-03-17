from sqlalchemy import and_
from sqlalchemy.orm import Session
from pydantic import BaseModel

from src.modules.categories.entities.category import Category


class DeleteBaseModel(BaseModel):
    message: str = 'Deletado com sucesso'


class DeleteCategoryService:

    def __init__(self, db: Session):
        self._db = db

    def execute(self, category_id: int) -> DeleteBaseModel:
        self._db.query(Category).filter(Category.id == category_id).delete()

        return DeleteBaseModel