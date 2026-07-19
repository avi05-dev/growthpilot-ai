from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.database import Recommendation


_PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


class RecommendationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_recommendations(self) -> list[Recommendation]:
        items = list(self.db.scalars(select(Recommendation).options(joinedload(Recommendation.knowledge_item))))
        return sorted(items, key=lambda item: (_PRIORITY_ORDER.get(item.priority, 99), item.created_at))
