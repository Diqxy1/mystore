"""product category

Revision ID: 8999fbd61126
Revises: 11ce7f8bd6aa
Create Date: 2022-03-17 10:18:30.402939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8999fbd61126'
down_revision = '11ce7f8bd6aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('categories')
