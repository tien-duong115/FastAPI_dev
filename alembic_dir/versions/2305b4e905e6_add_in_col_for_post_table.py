"""add in col for post_table

Revision ID: 2305b4e905e6
Revises: 
Create Date: 2021-12-02 20:52:31.824822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2305b4e905e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Posts_table',
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content',sa.String(), nullable=False)
                    )
    pass


def downgrade():
    op.drop_table('Posts_table')
    pass
