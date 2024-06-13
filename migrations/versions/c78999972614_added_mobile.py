"""added mobile

Revision ID: c78999972614
Revises: 63b6bdfd3eec
Create Date: 2024-06-13 09:19:46.739778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c78999972614'
down_revision = 'd760155f6fe3'
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
