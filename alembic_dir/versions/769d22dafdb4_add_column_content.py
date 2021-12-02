"""add column content

Revision ID: 769d22dafdb4
Revises: 7578fe438648
Create Date: 2021-12-01 21:17:11.949447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '769d22dafdb4'
down_revision = '7578fe438648'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('users', 'content')
    pass
