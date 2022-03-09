import sqlalchemy as sa

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
    phone = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())