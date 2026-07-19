from app.repositories.knowledge_repository import KnowledgeRepository
from app.repositories.recommendation_repository import RecommendationRepository
from app.schemas.dashboard import ActionTask, DailyBriefing, DashboardResponse, KpiMetric


class DashboardService:
    def __init__(self, knowledge_repository: KnowledgeRepository, recommendation_repository: RecommendationRepository) -> None:
        self.knowledge_repository = knowledge_repository
        self.recommendation_repository = recommendation_repository

    def get_dashboard(self) -> DashboardResponse:
        items = self.knowledge_repository.list()[:3]
        recommendations = self.recommendation_repository.list_recommendations()[:4]
        focus = recommendations[0].recommended_action if recommendations else "Review the latest knowledge items."
        return DashboardResponse(
            briefing=DailyBriefing(
                title="Today's Briefing",
                items=[{"id": item.id, "text": item.summary} for item in items],
                best_posting_window="10:30 AM – 12:00 PM",
                recommended_focus=focus,
            ),
            action_tasks=[ActionTask(id=item.id, title=item.recommended_action, description=item.reason, priority=item.priority) for item in recommendations],
            kpis=[
                KpiMetric(id="knowledge-items", label="Knowledge Items", value=str(len(self.knowledge_repository.list())), helper="database-backed signals"),
                KpiMetric(id="recommendations", label="Recommendations", value=str(len(self.recommendation_repository.list_recommendations())), helper="ready actions"),
                KpiMetric(id="enabled-domain", label="Enabled Domain", value="Technology", helper="seeded workspace"),
                KpiMetric(id="persistence", label="Persistence", value="PostgreSQL", helper="mock repositories removed"),
            ],
        )
