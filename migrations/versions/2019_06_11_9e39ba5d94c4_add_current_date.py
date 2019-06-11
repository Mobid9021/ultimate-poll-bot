"""Add current date

Revision ID: 9e39ba5d94c4
Revises: 1f4e87f7575c
Create Date: 2019-06-11 11:24:11.491769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e39ba5d94c4'
down_revision = '1f4e87f7575c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poll', sa.Column('current_date', sa.Date(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poll', 'current_date')
    # ### end Alembic commands ###
