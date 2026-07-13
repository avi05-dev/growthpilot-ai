from fastapi import APIRouter, Depends

from app.dependencies.services import get_recommendation_service
from app.schemas.recommendations import RecommendationsResponse
from app.services.recommendation_service import RecommendationService

router = APIRouter(prefix="/api", tags=["recommendations"])


@router.get("/recommendations", response_model=RecommendationsResponse)
def list_recommendations(service: RecommendationService = Depends(get_recommendation_service)) -> RecommendationsResponse:
    return service.list_recommendations()
