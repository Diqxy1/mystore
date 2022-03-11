import secrets
from datetime import date
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT


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
    phone: str
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


# JWT
class Settings(BaseModel):
    authjwt_secret_key: str = secrets.token_hex()

@AuthJWT.load_config
def get_config():
    return Settings()