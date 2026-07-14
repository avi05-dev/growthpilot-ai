from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.database import Domain


class DomainRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_enabled(self) -> list[Domain]:
        return list(self.db.scalars(select(Domain).where(Domain.is_enabled.is_(True)).order_by(Domain.display_name)))
