import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base

class Address(Base):

    __tablename__ = 'address'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    users = relationship("User", back_populates='address')
    address = sa.Column(sa.String, nullable=False)
    number = sa.Column(sa.String, nullable=False)
    neighborhood = sa.Column(sa.String, nullable=False)
    city = sa.Column(sa.String, nullable=False)
    state = sa.Column(sa.String, nullable=False)
    postal_code = sa.Column(sa.String, nullable=False)
    country = sa.Column(sa.String, nullable=False)
    telephone = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())