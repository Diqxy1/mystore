from typing import Optional
from pydantic import BaseModel


class CreateProductModel(BaseModel):
    name: str
    description: Optional[str]
    price: int


class ProductPayloadModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: int

    class Config:
        orm_mode = True