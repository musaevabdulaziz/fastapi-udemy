"""Create address_id column to users

Revision ID: 91d16c1a6b3e
Revises: 31b382aea388
Create Date: 2022-11-15 14:41:49.777484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91d16c1a6b3e'
down_revision = '31b382aea388'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key("address_users_fk", source_table="users", referent_table="address",
                          local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_user_fk", table_name="users")
    op.drop_column("users", "address_id")
