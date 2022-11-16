"""Create new address table

Revision ID: 31b382aea388
Revises: 10b4e60cf1bb
Create Date: 2022-11-15 14:31:06.091997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31b382aea388'
down_revision = '10b4e60cf1bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("address1", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("state", sa.String(), nullable=False),
                    sa.Column("country", sa.String(), nullable=False),
                    sa.Column("postalcode", sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("address")
