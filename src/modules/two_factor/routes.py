from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_database

from src.modules.two_factor.services.create_two_factor_service import CreateTwoFactorService
from src.modules.two_factor.services.active_two_factor_service import ActivateTwoFactorService
from src.modules.two_factor.models import TwoFactorModel, CreateTwoFactorModel, ActivateTwoFactorModel

router = APIRouter(
    prefix='/two-factor',
    tags=['Two-factor']
)

@router.post('/', response_model=TwoFactorModel)
def create_two_factor_email(
    model: CreateTwoFactorModel,
    db: Session = Depends(get_database)
):
    service = CreateTwoFactorService(db)
    return service.execute(model)

@router.post('/activate')
def activate_two_factor_email(
    model: ActivateTwoFactorModel,
    db: Session = Depends(get_database)
):
    service = ActivateTwoFactorService(db)
    return service.execute(model)