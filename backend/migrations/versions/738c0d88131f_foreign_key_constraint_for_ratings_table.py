"""foreign key constraint for ratings table

Revision ID: 738c0d88131f
Revises: 889d4238323f
Create Date: 2018-04-16 23:28:09.931260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '738c0d88131f'
down_revision = '889d4238323f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'rating', 'trial', ['participant_id', 'session_id'], ['participant', 'session'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rating', type_='foreignkey')
    # ### end Alembic commands ###