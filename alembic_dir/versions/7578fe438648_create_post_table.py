"""create post table

Revision ID: 7578fe438648
Revises: 
Create Date: 2021-12-01 21:11:27.528811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7578fe438648'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
