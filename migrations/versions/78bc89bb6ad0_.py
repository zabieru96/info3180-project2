"""empty message

Revision ID: 78bc89bb6ad0
Revises: a0d20fd52309
Create Date: 2017-04-25 19:50:56.757550

"""

# revision identifiers, used by Alembic.
revision = '78bc89bb6ad0'
down_revision = 'a0d20fd52309'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('image', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_foreign_key(None, 'wishlist_item', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wishlist_item', type_='foreignkey')
    op.drop_table('user')
    # ### end Alembic commands ###
