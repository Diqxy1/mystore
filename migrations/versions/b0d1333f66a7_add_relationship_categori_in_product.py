"""add relationship categori in product

Revision ID: b0d1333f66a7
Revises: 8999fbd61126
Create Date: 2022-03-17 10:32:23.980483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0d1333f66a7'
down_revision = '8999fbd61126'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'products',
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id'), nullable=False),
    )


def downgrade():
    op.drop_column(
        'products',
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.id'), nullable=False),
    )
