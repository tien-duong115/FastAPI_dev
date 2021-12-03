"""add owner_id and post_user_fk columns into posts_table

Revision ID: f73d25313e18
Revises: 1fd533ff43a3
Create Date: 2021-12-02 22:25:54.127719

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = 'f73d25313e18'
down_revision = '1fd533ff43a3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users_table',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=True),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users_table')
    pass
