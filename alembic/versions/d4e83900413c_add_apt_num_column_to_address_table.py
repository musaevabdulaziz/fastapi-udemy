"""Add apt_num column to address table

Revision ID: d4e83900413c
Revises: 91d16c1a6b3e
Create Date: 2022-11-16 11:47:54.654026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e83900413c'
down_revision = '91d16c1a6b3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
