"""create agent memory

Revision ID: 0003_create_agent_memory
Revises: 0002_add_intelligence_fields
Create Date: 2026-07-17
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0003_create_agent_memory"
down_revision: str | None = "0002_add_intelligence_fields"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "agent_memory",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("query", sa.String(length=500), nullable=False),
        sa.Column("domain", sa.String(length=80), nullable=False),
        sa.Column("goal", sa.String(length=120), nullable=False),
        sa.Column("time_window", sa.String(length=40), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("findings", sa.JSON(), nullable=False),
        sa.Column("recommended_actions", sa.JSON(), nullable=False),
        sa.Column("sources", sa.JSON(), nullable=False),
        sa.Column("provider", sa.String(length=80), nullable=False),
        sa.Column("llm_model", sa.String(length=120), nullable=False),
        sa.Column("memory_metadata", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_agent_memory_query", "agent_memory", ["query"])
    op.create_index("ix_agent_memory_domain", "agent_memory", ["domain"])
    op.create_index("ix_agent_memory_goal", "agent_memory", ["goal"])
    op.create_index("ix_agent_memory_expires_at", "agent_memory", ["expires_at"])


def downgrade() -> None:
    op.drop_table("agent_memory")
