"""rename address

Revision ID: ef9bc8dd0477
Revises: 92690e4f1952
Create Date: 2024-07-07 22:09:29.705009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef9bc8dd0477'
down_revision = '92690e4f1952'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('departments', 'address', new_column_name='location')


def downgrade():
    op.alter_column('departments', 'location', new_column_name='address')
