"""create user address

Revision ID: f49f2c54fc00
Revises: d73b393d83b6
Create Date: 2022-03-10 10:51:58.992406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f49f2c54fc00'
down_revision = 'd73b393d83b6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('address', sa.Text(), nullable=False),
        sa.Column('number', sa.String(5), nullable=False),
        sa.Column('neighborhood', sa.String(50), nullable=False),
        sa.Column('city', sa.String(25), nullable=False),
        sa.Column('state', sa.String(2), nullable=False),
        sa.Column('postal_code', sa.String(25), nullable=False),
        sa.Column('country', sa.String(25), nullable=False),
        sa.Column('telephone', sa.String(15), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('address')
