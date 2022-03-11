from pydantic import BaseModel


class AddressPayloadModel(BaseModel):
    id: int
    address: str
    number: str
    neighborhood: str
    city: str
    state: str
    postal_code: str
    country: str
    telephone: str


    class Config:
        orm_mode = True


class CreateAddressModel(BaseModel):
    address: str
    number: str
    neighborhood: str
    city: str
    state: str
    postal_code: str
    country: str
    telephone: str