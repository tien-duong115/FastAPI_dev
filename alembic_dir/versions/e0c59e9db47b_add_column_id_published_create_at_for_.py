"""add column id, published, create_at for posts_table"

Revision ID: e0c59e9db47b
Revises: 2305b4e905e6
Create Date: 2021-12-02 21:01:45.110471

"""
from datetime import timezone
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = 'e0c59e9db47b'
down_revision = '2305b4e905e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts_table',
                  sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                  )
    pass


def downgrade():
    op.drop_column('Posts_table','id')
    pass
