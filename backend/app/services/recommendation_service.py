from app.repositories.recommendation_repository import RecommendationRepository
from app.schemas.recommendations import RecommendationsResponse


class RecommendationService:
    def __init__(self, repository: RecommendationRepository | None = None) -> None:
        self.repository = repository or RecommendationRepository()

    def list_recommendations(self) -> RecommendationsResponse:
        return self.repository.list_recommendations()
