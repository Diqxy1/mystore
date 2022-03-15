"""twofactor

Revision ID: 6c8274ee4ec8
Revises: f49f2c54fc00
Create Date: 2022-03-15 15:16:40.121883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c8274ee4ec8'
down_revision = 'f49f2c54fc00'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'two_factor',
        sa.Column('id', sa.Integer, nullable=False, unique=True),
        sa.Column('uuid', sa.String(36), nullable=False),
        sa.Column('code', sa.String(10), nullable=False),
        sa.Column('token', sa.String(50), nullable=False),
        sa.Column('two_factor_type', sa.String(10), nullable=False),
        sa.Column('expires_hours', sa.DateTime, nullable=False),
        sa.Column('validated_at', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_table('two_factor')
