import sqlalchemy as sa
from sqlalchemy.orm import relationship

from src.config.database import Base


class Category(Base):
    
    __tablename__ = 'categories'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    products = relationship('Product', back_populates='categories', uselist=False)
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text(), nullable=True)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())