"""add column breed

Revision ID: 9c5a4df4cf9d
Revises: 466925fa3a27
Create Date: 2020-08-08 15:48:41.505085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c5a4df4cf9d'
down_revision = '466925fa3a27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###
