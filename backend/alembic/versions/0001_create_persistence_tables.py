"""create persistence tables

Revision ID: 0001_create_persistence_tables
Revises: 
Create Date: 2026-07-13
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001_create_persistence_tables"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "domains",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("display_name", sa.String(length=160), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("is_enabled", sa.Boolean(), nullable=False),
    )
    op.create_index("ix_domains_name", "domains", ["name"], unique=True)
    op.create_table(
        "knowledge_items",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("domain", sa.String(length=80), nullable=False),
        sa.Column("title", sa.String(length=240), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("source", sa.String(length=120), nullable=False),
        sa.Column("category", sa.String(length=80), nullable=False),
        sa.Column("url", sa.String(length=500), nullable=True),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("status", sa.String(length=40), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_knowledge_items_domain", "knowledge_items", ["domain"])
    op.create_index("ix_knowledge_items_category", "knowledge_items", ["category"])
    op.create_table(
        "recommendations",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("knowledge_item_id", sa.String(length=36), sa.ForeignKey("knowledge_items.id", ondelete="CASCADE"), nullable=False),
        sa.Column("priority", sa.String(length=40), nullable=False),
        sa.Column("recommended_action", sa.Text(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("estimated_effort", sa.String(length=80), nullable=False),
        sa.Column("content_opportunity", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_recommendations_knowledge_item_id", "recommendations", ["knowledge_item_id"])


def downgrade() -> None:
    op.drop_table("recommendations")
    op.drop_table("knowledge_items")
    op.drop_table("domains")
