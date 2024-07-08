"""rename department

Revision ID: 92690e4f1952
Revises: d65d5acf6f69
Create Date: 2024-07-07 22:06:16.806265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92690e4f1952'
down_revision = 'd65d5acf6f69'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')


def downgrade():
    op.rename_table('departments', 'department')
