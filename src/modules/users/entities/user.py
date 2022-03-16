import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base

class User(Base):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    uuid = sa.Column(sa.String, unique=True)
    username = sa.Column(sa.String, nullable=False, unique=True)
    password = sa.Column(sa.String, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    second_name = sa.Column(sa.String, nullable=False)
    birth_date = sa.Column(sa.Date, nullable=False)
    email = sa.Column(sa.String, nullable=False)
    verified_email = sa.Column(sa.Boolean, nullable=True)
    phone = sa.Column(sa.String, nullable=False)
    verified_phone = sa.Column(sa.Boolean, nullable=True)
    is_active = sa.Column(sa.Boolean, default=False)
    address = relationship('Address', back_populates='users', uselist=False)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())