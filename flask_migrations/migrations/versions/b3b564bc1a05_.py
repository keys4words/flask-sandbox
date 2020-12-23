"""empty message

Revision ID: b3b564bc1a05
Revises: 6da2ec3fc033
Create Date: 2020-12-23 10:02:21.662305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3b564bc1a05'
down_revision = '6da2ec3fc033'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('subscribed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member', 'subscribed')
    # ### end Alembic commands ###
