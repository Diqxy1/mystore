from datetime import date
from pydantic import BaseModel

class UserModelPayload(BaseModel):
    id: int
    uuid: str
    username: str
    password: str
    first_name: str
    second_name: str
    birth_date: date
    email: str
    phone: str
    is_active: bool

    class Config:
        orm_mode = True

class CreateUserModel(BaseModel):
    username: str
    password: str
    first_name: str
    second_name: str
    birth_date: date
    email: str
    phone: str
