"""added mobile column

Revision ID: 1c48dbf5268e
Revises: 39d32f74760f
Create Date: 2024-06-12 14:42:35.194570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c48dbf5268e'
down_revision = '39d32f74760f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mobile', sa.String(length=256), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_column('mobile')

    # ### end Alembic commands ###