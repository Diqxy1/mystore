from typing import Optional
from pydantic import BaseModel

from src.modules.categories.models import CategoryPayloadModel


class CreateProductModel(BaseModel):
    name: str
    description: Optional[str]
    price: int
    category_id: int


class ProductPayloadModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: int
    categories: CategoryPayloadModel

    class Config:
        orm_mode = True