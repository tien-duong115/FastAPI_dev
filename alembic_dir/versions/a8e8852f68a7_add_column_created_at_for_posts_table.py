"""add column created_at for posts_table

Revision ID: a8e8852f68a7
Revises: e0c59e9db47b
Create Date: 2021-12-02 22:10:56.710274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8e8852f68a7'
down_revision = 'e0c59e9db47b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts_table',
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                            nullable=True)
                  )
    pass


def downgrade():
    op.drop_column('Posts_table','created_at')
    pass
