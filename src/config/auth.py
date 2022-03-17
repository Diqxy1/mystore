from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = config('JWT_KEY')