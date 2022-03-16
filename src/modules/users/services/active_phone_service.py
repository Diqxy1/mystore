""" from sqlalchemy.orm import Session


from src.shared.exceptions.not_found_exception import NotFoundException

from src.modules.users.models import UserModelPayload
from src.modules.users.entities.user import User

from src.modules.two_factor.services.active_two_factor_service import ActivateTwoFactorService
from src.modules.two_factor.models import ActivateTwoFactorModel
from src.modules.two_factor.entities.two_factor import TwoFactor


class ActivatePhoneService:

    def __init__(self, db: Session):
        self._db = db
        self._activate_two_factor_service = ActivateTwoFactorService(db)
    
    def execute(self, model: ActivateTwoFactorModel) -> UserModelPayload:
        two_factor_activated = self._db.query(TwoFactor).filter(TwoFactor.token == model.token).first()

        if not two_factor_activated:
            raise NotFoundException(message='Falha ao ativar')
        
        two_factor_model = self._activate_two_factor_service.execute(model)

        user = self._db.query(User).filter(User.uuid == two_factor_model.user_uuid).first()

        if not user:
            raise NotFoundException(message='Usuário não encontrado')

        #@TODO adicionar verified_phone
        user.verified_phone = True

        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)

        return UserModelPayload.from_orm(user) """