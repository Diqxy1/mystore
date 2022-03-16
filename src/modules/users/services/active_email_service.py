""" from sqlalchemy.orm import Session

from src.shared.exceptions.not_found_exception import NotFoundException
from src.shared.exceptions.forbidden_exception import ForbiddenException

from src.shared.services.send_grid import SendGridService, SendMailModel
from src.shared.services.template import TemplateService

from src.modules.two_factor.models import CreateTwoFactorModel, TwoFactorType
from src.modules.two_factor.services.create_two_factor_service import CreateTwoFactorService
from src.modules.users.models import CreateEmailModel, EmailModelResponse
from src.modules.users.entities.user import User


class CreateEmailService:

    def __init__(self, db: Session):
        self._db = db
        self._create_two_factor_service = CreateTwoFactorService(db)
        self._mail_service = SendGridService()
        self._template_service = TemplateService()

    def execute(self, model: CreateEmailModel) -> EmailModelResponse:
        user_exists = self._db.query(User).filter(User.uuid == model.uuid).first()

        if not user_exists:
            raise NotFoundException(message='Usuário não encontrado')

        user_email_exists = self._db.query(User).filter(User.email == model.email).first()

        if user_email_exists and user_email_exists.uuid != user_exists.uuid:
            raise ForbiddenException(message='E-mail já está em uso')

        two_factor_model = CreateTwoFactorModel(
            user_uuid=user_exists.uuid,
            two_factor_type=TwoFactorType.EMAIL.value
        )

        two_factor_token = self._create_two_factor_service.execute(two_factor_model)

        self._notify_user(name=user_exists.username, code=two_factor_token.code, email=user_exists.email)

        payload = EmailModelResponse(activate_email_token=two_factor_token.token)

        return payload

    def _notify_user(self, name: str, code: str, email: str):
        mail_html = self._template_service.render(
            TemplateService.SEND_CODE,
            {'name': name, 'code': code}
        )
        send_mail_model = SendMailModel(
            to=[email],
            subject='Validação de conta',
            html=mail_html
        )
        self._mail_service.send(send_mail_model) """