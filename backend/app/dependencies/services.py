from app.services.dashboard_service import DashboardService
from app.services.recommendation_service import RecommendationService
from app.services.trend_service import TrendService


def get_dashboard_service() -> DashboardService:
    return DashboardService()


def get_trend_service() -> TrendService:
    return TrendService()


def get_recommendation_service() -> RecommendationService:
    return RecommendationService()
