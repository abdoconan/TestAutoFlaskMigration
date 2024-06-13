"""added new_script_column

Revision ID: 4f644ab9721b
Revises: 4ec23e9ce420
Create Date: 2024-06-13 10:42:31.386604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f644ab9721b'
down_revision = '4ec23e9ce420'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('new_script_column', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_column('new_script_column')

    # ### end Alembic commands ###
