"""Danswer Custom Tool Flow

Revision ID: dba7f71618f5
Revises: d5645c915d0e
Create Date: 2023-09-18 15:18:37.370972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dba7f71618f5"
down_revision = "d5645c915d0e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "persona", sa.Column("retrieval_enabled", sa.Boolean(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column("persona", "retrieval_enabled")
