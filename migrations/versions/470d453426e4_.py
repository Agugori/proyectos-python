"""empty message

Revision ID: 470d453426e4
Revises: 34e4e67b619d
Create Date: 2023-03-20 11:20:35.771431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '470d453426e4'
down_revision = '34e4e67b619d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
