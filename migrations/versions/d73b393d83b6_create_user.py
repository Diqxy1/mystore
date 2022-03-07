"""create user

Revision ID: d73b393d83b6
Revises: 
Create Date: 2022-03-07 14:09:17.816420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd73b393d83b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', sa.String(36), nullable=False, unique=True),
        sa.Column('username', sa.String(120), nullable=False, unique=True),
        sa.Column('password', sa.Text(), nullable=False),
        sa.Column('first_name', sa.String(120)),
        sa.Column('second_name', sa.String(120)),
        sa.Column('birth_date', sa.DateTime, nullable=False),
        sa.Column('email', sa.String(60), nullable=True, unique=True),
        sa.Column('phone', sa.String(20), nullable=True, unique=True),
        sa.Column('is_active', sa.Boolean, default=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_column('users')
