from twilio.rest import Client
from pydantic import BaseModel
from decouple import config


class SendSmsModel(BaseModel):
    phone_number: str
    message: str


class TwilioSmsService:

    def __init__(self):
        account_id = config("TWILIO_ACCOUNT_ID")
        auth_token = config("TWILIO_AUTH_TOKEN")
        self._client = Client(account_id, auth_token)
    
    def send(self, model: SendSmsModel):
        self._send(model)
    
    def _send(self, model: SendSmsModel):
        a = self._client.messages.create(
            body=model.message,
            from_='+16202675562',
            to=model.phone_number
        )
        print(a.status)
        print(a.error_code)
        print(a.sid)