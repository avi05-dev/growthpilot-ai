from app.repositories.trend_repository import TrendRepository
from app.schemas.trends import TrendsResponse


class TrendService:
    def __init__(self, repository: TrendRepository | None = None) -> None:
        self.repository = repository or TrendRepository()

    def list_trends(self) -> TrendsResponse:
        return self.repository.list_trends()
