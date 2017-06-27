"""empty message

Revision ID: adf802d9cd2e
Revises: 
Create Date: 2017-06-27 20:03:58.057718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adf802d9cd2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subs',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('channel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['channel_id'], ['channel.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subs')
    op.drop_table('user')
    op.drop_table('channel')
    # ### end Alembic commands ###