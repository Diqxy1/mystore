""" from sqlalchemy.orm import Session

from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.forbidden_exception import ForbiddenException

from src.shared.services.twilio import TwilioSmsService, SendSmsModel

from src.modules.two_factor.models import CreateTwoFactorModel, TwoFactorType
from src.modules.two_factor.services.create_two_factor_service import CreateTwoFactorService
from src.modules.users.models import CreatePhoneModel, PhoneModelResponse
from src.modules.users.entities.user import User


class CreatePhoneService:

    def __init__(self, db: Session):
        self._db = db
        self._create_two_factor_servie = CreateTwoFactorService(db)
        self._sms_service = TwilioSmsService()
    
    def execute(self, model: CreatePhoneModel) -> PhoneModelResponse:
        user_exist = self._db.query(User).filter(User.uuid == model.uuid).first()

        if not user_exist:
            raise NotFoundException(message='Usuário não encontrado')
        
        user_phone_exist = self._db.query(User).filter(User.phone == model.phone).first()

        if user_phone_exist and user_phone_exist.uuid != user_exist.uuid:
            raise ForbiddenException(message='E-mail já está em uso')
        
        user_exist.phone = model.phone

        self._db.add(user_exist)
        self._db.commit()
        self._db.refresh(user_exist)

        two_factor_model = CreateTwoFactorModel(
            user_uuid=user_exist.uuid,
            two_factor_type=TwoFactorType.SMS.value
        )

        two_factor_token = self._create_two_factor_servie.execute(two_factor_model)

        self._notify_user(name=user_exist.username, code=two_factor_token.code, phone=user_exist.phone)

        payload = PhoneModelResponse(
            activate_phone_token=two_factor_token.token
        )

        return payload
    
    def _notify_user(self, name: str, code: str, phone: str):
        sms_model = SendSmsModel(
            phone_number=phone,
            message=f'Olá {name}, seu código de ativação é: {code}'
        )
        self._sms_service.send(sms_model) """