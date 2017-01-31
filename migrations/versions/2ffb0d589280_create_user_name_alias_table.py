"""create user_name_alias table

Revision ID: 2ffb0d589280
Revises: 11673cfcc25a
Create Date: 2017-01-31 09:24:41.077072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ffb0d589280'
down_revision = '11673cfcc25a'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_alias_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_id', sa.Unicode(length=100), nullable=False),
    sa.Column('alias_name', sa.Unicode(length=100), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias_name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_alias_name')
    ### end Alembic commands ###
