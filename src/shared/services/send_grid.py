import json
import requests
from pydantic import BaseModel
from typing import List, Optional
from decouple import config


class SendMailModel(BaseModel):
    to: List[str]
    subject: str
    text: Optional[str]
    html: Optional[str]


class SendGridService:

    def __init__(self):
        super().__init__()
        self._url = config('SENDGRID_URL')
        self._email_from = config('EMAIL_FROM')

    def send(self, model: SendMailModel):

        data = {
            "personalizations":[
                {
                    "to":[
                        {
                            "email": model.to[0],
                        }
                    ],
                    "subject": model.subject
                }
            ],
            "content":[
                {
                    "type": "text/html",
                    "value": model.html
                }
            ],
            "from":{
                "email": self._email_from,
            }
        }

        data = json.dumps(data)

        headers_payload = {
            "Authorization": f"Bearer {config('SENDGRID_API_KEY')}",
            "Content-Type": "application/json"
        }

        r= requests.post(
            url=self._url,
            headers=headers_payload,
            data=data
        )

        print(r.status_code)
        print(r.text)