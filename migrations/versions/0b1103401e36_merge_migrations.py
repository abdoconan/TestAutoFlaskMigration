"""Merge migrations

Revision ID: 0b1103401e36
Revises: 1e5695910a2c, 90bee2a637c8
Create Date: 2024-06-10 09:07:50.132748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b1103401e36'
down_revision = ('1e5695910a2c', '90bee2a637c8')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
