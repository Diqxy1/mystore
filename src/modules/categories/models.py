from typing import Optional
from pydantic import BaseModel


class CreateCategoryModel(BaseModel):
    name: str
    description: Optional[str]


class CategoryPayloadModel(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True