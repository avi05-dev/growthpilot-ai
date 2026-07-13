from fastapi import APIRouter, Depends

from app.dependencies.services import get_trend_service
from app.schemas.trends import TrendsResponse
from app.services.trend_service import TrendService

router = APIRouter(prefix="/api", tags=["trends"])


@router.get("/trends", response_model=TrendsResponse)
def list_trends(service: TrendService = Depends(get_trend_service)) -> TrendsResponse:
    return service.list_trends()
