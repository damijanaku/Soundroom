"""force LLM approval for recommendation imports

Revision ID: 0006_radio_llm
Revises: 0005_playlists
Create Date: 2026-11-08

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0006_radio_llm"
down_revision: str | None = "0005_playlists"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "rip_jobs",
        sa.Column(
            "force_llm_approval",
            sa.Boolean(),
            server_default=sa.false(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("rip_jobs", "force_llm_approval")
