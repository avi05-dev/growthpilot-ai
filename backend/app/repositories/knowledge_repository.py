from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.database import KnowledgeItem


class KnowledgeRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self, domain: str | None = None) -> list[KnowledgeItem]:
        stmt = select(KnowledgeItem).order_by(KnowledgeItem.published_at.desc().nullslast(), KnowledgeItem.created_at.desc())
        if domain:
            stmt = stmt.where(KnowledgeItem.domain == domain)
        return list(self.db.scalars(stmt))

    def get(self, item_id: str) -> KnowledgeItem | None:
        return self.db.get(KnowledgeItem, item_id)


    def list_by_processing_status(self, status: str) -> list[KnowledgeItem]:
        stmt = select(KnowledgeItem).where(KnowledgeItem.processing_status == status).order_by(KnowledgeItem.created_at.asc())
        return list(self.db.scalars(stmt))

    def save(self, item: KnowledgeItem) -> KnowledgeItem:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
