from app.repositories.recommendation_repository import RecommendationRepository
from app.schemas.recommendations import Recommendation, RecommendationsResponse


class RecommendationService:
    def __init__(self, repository: RecommendationRepository) -> None:
        self.repository = repository

    def list_recommendations(self) -> RecommendationsResponse:
        recommendations = []
        for item in self.repository.list_recommendations():
            recommendations.append(
                Recommendation(
                    id=item.id,
                    knowledge_item_id=item.knowledge_item_id,
                    priority=item.priority,
                    recommended_action=item.recommended_action,
                    reason=item.reason,
                    estimated_effort=item.estimated_effort,
                    content_opportunity=item.content_opportunity,
                    created_at=item.created_at,
                    topic=item.knowledge_item.title,
                    channel=item.knowledge_item.category,
                )
            )
        return RecommendationsResponse(recommendations=recommendations)
