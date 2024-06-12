"""another_column_3

Revision ID: c5f534a3f818
Revises: 6e029a13c3e3
Create Date: 2024-06-12 16:02:34.492250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f534a3f818'
down_revision = '6e029a13c3e3'
branch_labels = None
depends_on = None


def upgrade():
    
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('another_column_3', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_column('another_column_3')

    # ### end Alembic commands ###
