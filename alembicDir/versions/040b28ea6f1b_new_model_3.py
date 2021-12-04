"""new model 3

Revision ID: 040b28ea6f1b
Revises: 81cb55dca959
Create Date: 2021-12-03 22:55:10.920425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040b28ea6f1b'
down_revision = '81cb55dca959'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_table', sa.Column('remove_id', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_table', 'remove_id')
    # ### end Alembic commands ###
