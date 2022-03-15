import secrets
from pydantic import BaseModel


token = secrets.token_hex()

class Settings(BaseModel):
    authjwt_secret_key: str = token