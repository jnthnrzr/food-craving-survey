"""trials table

Revision ID: 031ae057f86f
Revises: 
Create Date: 2018-03-04 21:09:45.634988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '031ae057f86f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trial',
    sa.Column('participant', sa.Integer(), nullable=False),
    sa.Column('session', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('participant', 'session')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trial')
    # ### end Alembic commands ###
