import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base


class Product(Base):
    
    __tablename__ = 'products'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    users = relationship("User", back_populates='products')
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text(), nullable=True)
    price = sa.Column(sa.Integer, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())