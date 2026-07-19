from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.database import AgentMemory


class AgentMemoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_valid(self, *, query: str, domain: str, goal: str, time_window: str) -> AgentMemory | None:
        now = datetime.now(timezone.utc)
        stmt = (
            select(AgentMemory)
            .where(AgentMemory.query == query)
            .where(AgentMemory.domain == domain)
            .where(AgentMemory.goal == goal)
            .where(AgentMemory.time_window == time_window)
            .where(AgentMemory.expires_at > now)
            .order_by(AgentMemory.created_at.desc())
        )
        return self.db.scalars(stmt).first()

    def save(self, memory: AgentMemory) -> AgentMemory:
        self.db.add(memory)
        self.db.commit()
        self.db.refresh(memory)
        return memory
