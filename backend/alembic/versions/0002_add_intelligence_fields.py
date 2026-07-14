"""add intelligence fields

Revision ID: 0002_add_intelligence_fields
Revises: 0001_create_persistence_tables
Create Date: 2026-07-14
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002_add_intelligence_fields"
down_revision: str | None = "0001_create_persistence_tables"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("knowledge_items", sa.Column("freshness_score", sa.Float(), nullable=True))
    op.add_column("knowledge_items", sa.Column("authority_score", sa.Float(), nullable=True))
    op.add_column("knowledge_items", sa.Column("relevance_score", sa.Float(), nullable=True))
    op.add_column("knowledge_items", sa.Column("momentum_score", sa.Float(), nullable=True))
    op.add_column("knowledge_items", sa.Column("confidence_score", sa.Float(), nullable=True))
    op.add_column("knowledge_items", sa.Column("intelligence_score", sa.Float(), nullable=True))
    op.add_column("knowledge_items", sa.Column("priority", sa.String(length=40), nullable=True))
    op.add_column("knowledge_items", sa.Column("processing_status", sa.String(length=40), nullable=False, server_default="Pending"))
    op.add_column("knowledge_items", sa.Column("processed_at", sa.DateTime(timezone=True), nullable=True))
    op.alter_column("knowledge_items", "processing_status", server_default=None)


def downgrade() -> None:
    op.drop_column("knowledge_items", "processed_at")
    op.drop_column("knowledge_items", "processing_status")
    op.drop_column("knowledge_items", "priority")
    op.drop_column("knowledge_items", "intelligence_score")
    op.drop_column("knowledge_items", "confidence_score")
    op.drop_column("knowledge_items", "momentum_score")
    op.drop_column("knowledge_items", "relevance_score")
    op.drop_column("knowledge_items", "authority_score")
    op.drop_column("knowledge_items", "freshness_score")
