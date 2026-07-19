from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, JSON, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def new_id() -> str:
    return str(uuid4())


class Base(DeclarativeBase):
    pass


class Domain(Base):
    __tablename__ = "domains"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    name: Mapped[str] = mapped_column(String(80), unique=True, index=True, nullable=False)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class KnowledgeItem(Base):
    __tablename__ = "knowledge_items"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    domain: Mapped[str] = mapped_column(String(80), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(240), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    source: Mapped[str] = mapped_column(String(120), nullable=False)
    category: Mapped[str] = mapped_column(String(80), index=True, nullable=False)
    url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(40), nullable=False, default="published")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    recommendations: Mapped[list["Recommendation"]] = relationship(back_populates="knowledge_item")


class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    knowledge_item_id: Mapped[str] = mapped_column(ForeignKey("knowledge_items.id", ondelete="CASCADE"), index=True, nullable=False)
    priority: Mapped[str] = mapped_column(String(40), nullable=False)
    recommended_action: Mapped[str] = mapped_column(Text, nullable=False)
    reason: Mapped[str] = mapped_column(Text, nullable=False)
    estimated_effort: Mapped[str] = mapped_column(String(80), nullable=False)
    content_opportunity: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    knowledge_item: Mapped[KnowledgeItem] = relationship(back_populates="recommendations")


class AgentMemory(Base):
    __tablename__ = "agent_memory"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    query: Mapped[str] = mapped_column(String(500), index=True, nullable=False)
    domain: Mapped[str] = mapped_column(String(80), index=True, nullable=False)
    goal: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    time_window: Mapped[str] = mapped_column(String(40), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    findings: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    recommended_actions: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    sources: Mapped[list[dict[str, str]]] = mapped_column(JSON, nullable=False, default=list)
    provider: Mapped[str] = mapped_column(String(80), nullable=False)
    llm_model: Mapped[str] = mapped_column(String(120), nullable=False)
    memory_metadata: Mapped[dict[str, object]] = mapped_column(JSON, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
