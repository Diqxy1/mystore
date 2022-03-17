from datetime import date
from typing import Optional
from pydantic import BaseModel


from src.modules.address.models import CreateAddressModel, AddressPayloadModel

class UserModelPayload(BaseModel):
    id: int
    uuid: str
    username: str
    #password: str
    first_name: str
    second_name: str
    birth_date: date
    email: str
    verified_email: Optional[bool]
    phone: str
    verified_phone: Optional[bool]
    is_active: bool
    address: AddressPayloadModel

    class Config:
        orm_mode = True


class SignedUserModel(BaseModel):
    id: int
    uuid: str
    username: str
    first_name: str
    second_name: str
    birth_date: date
    email: str
    verified_email: Optional[bool]
    phone: str
    verified_phone: Optional[bool]
    is_active: bool
    address: AddressPayloadModel

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
    address: CreateAddressModel


class LoginUserModel(BaseModel):
    username: str
    password: str


class AuthResponseModel(BaseModel):
    id: int
    username: str
    acess_token: str
    refresh_acess_token: str


class CreatePhoneModel(BaseModel):
    uuid: str
    phone: str


class PhoneModelResponse(BaseModel):
    activate_phone_token: str


class CreateEmailModel(BaseModel):
    uuid: str
    email: str


class EmailModelResponse(BaseModel):
    activate_email_token: str