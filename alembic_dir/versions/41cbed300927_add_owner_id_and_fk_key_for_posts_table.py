"""add owner_id and fk key for posts table

Revision ID: 41cbed300927
Revises: f73d25313e18
Create Date: 2021-12-02 22:34:02.742925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41cbed300927'
down_revision = 'f73d25313e18'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts_table',
                  sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='Posts_table', referent_table="users_table", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="Posts_table")
    op.drop_column('Posts_table','owner_id')
    pass
