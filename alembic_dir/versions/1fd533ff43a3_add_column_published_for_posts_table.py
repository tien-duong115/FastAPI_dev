"""add column published for posts_table

Revision ID: 1fd533ff43a3
Revises: a8e8852f68a7
Create Date: 2021-12-02 22:14:23.565000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd533ff43a3'
down_revision = 'a8e8852f68a7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts_table',
                sa.Column("published", sa.Boolean(), nullable=False, server_default=sa.text('TRUE')),
                )
    pass


def downgrade():
    op.drop_column('Posts_table' ,'published')
    pass
