from collections import defaultdict

from app.repositories.knowledge_repository import KnowledgeRepository
from app.schemas.trends import TrendSummary, TrendsResponse


class TrendService:
    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def list_trends(self) -> TrendsResponse:
        grouped: dict[str, list] = defaultdict(list)
        for item in self.repository.list():
            grouped[item.category].append(item)
        trends = []
        for category, items in grouped.items():
            for index, item in enumerate(items[:3]):
                trends.append(TrendSummary(id=item.id, category=category, title=item.title, description=item.summary, score=max(70, 95 - index * 4), sources=[item.source]))
        return TrendsResponse(trends=trends)
