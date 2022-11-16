"""create phone number for user col

Revision ID: 10b4e60cf1bb
Revises: 
Create Date: 2022-11-15 14:20:32.333107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10b4e60cf1bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "phone_number")
