"""'new'

Revision ID: 4c24273e3d14
Revises: 184df04c2a5d
Create Date: 2021-04-03 03:05:21.046126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c24273e3d14'
down_revision = '184df04c2a5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bid', sa.Column('count_bid', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bid', 'count_bid')
    # ### end Alembic commands ###
