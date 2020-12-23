"""empty message

Revision ID: fb6afde7437f
Revises: 5fb848a66748
Create Date: 2020-12-23 10:46:06.504523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb6afde7437f'
down_revision = '5fb848a66748'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_column('member', 'location')
    with op.batch_alter_table('member') as batch_op:
        batch_op.drop_column('location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('location', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
