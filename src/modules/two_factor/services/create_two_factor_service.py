
from sqlalchemy.orm import Session
from sqlalchemy import and_
from random import randrange
from uuid import uuid4
from datetime import datetime, timedelta

from src.modules.two_factor.models import TwoFactorModel, CreateTwoFactorModel
from src.modules.two_factor.entities.two_factor import TwoFactor

class CreateTwoFactorService:

    def __init__(self, db: Session):
        self._db = db
    
    def execute(self, model: CreateTwoFactorModel) -> TwoFactorModel:
        two_factor_exists = self._db.query(TwoFactor).filter(and_(
            TwoFactor.user_uuid == model.user_uuid,
            TwoFactor.two_factor_type == model.two_factor_type
        )).first()

        model.code = str(randrange(100_000, 999_999))
        model.token = str(uuid4())

        if not model.expires_hours:
            model.expires_hours = 2
        
        if two_factor_exists:
            two_factor_exists.code = model.code
            two_factor_exists.token = model.token
            two_factor_exists.expires_hours = model.expires_hours
            two_factor_exists.expires_at = datetime.now() + timedelta(hours=model.expires_hours)
            two_factor_exists.validated_at = None

            self._db.add(two_factor_exists)
            self._db.commit()
            self._db.refresh(two_factor_exists)

            return TwoFactorModel.from_orm(two_factor_exists)
        
        else:
            model.expires_at = datetime.now() + timedelta(hours=model.expires_hours)
            two_factor = TwoFactor(**model.dict())

            self._db.add(two_factor)
            self._db.commit()
            self._db.refresh(two_factor)

            return TwoFactorModel.from_orm(two_factor)
