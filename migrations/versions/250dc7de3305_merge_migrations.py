"""Merge migrations

Revision ID: 250dc7de3305
Revises: 1cc947571f17, c296d8e89033
Create Date: 2024-06-09 07:35:12.933886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '250dc7de3305'
down_revision = ('1cc947571f17', 'c296d8e89033')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
