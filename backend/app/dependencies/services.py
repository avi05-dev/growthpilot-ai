from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.intelligence.pipeline import KnowledgeIntelligencePipeline
from app.repositories.domain_repository import DomainRepository
from app.repositories.knowledge_repository import KnowledgeRepository
from app.repositories.recommendation_repository import RecommendationRepository
from app.services.dashboard_service import DashboardService
from app.services.domain_service import DomainService
from app.services.intelligence_service import KnowledgeIntelligenceService
from app.services.knowledge_service import KnowledgeService
from app.services.recommendation_service import RecommendationService
from app.services.trend_service import TrendService


def get_domain_service(db: Session = Depends(get_db)) -> DomainService:
    return DomainService(DomainRepository(db))


def get_knowledge_service(db: Session = Depends(get_db)) -> KnowledgeService:
    return KnowledgeService(KnowledgeRepository(db))


def get_recommendation_service(db: Session = Depends(get_db)) -> RecommendationService:
    return RecommendationService(RecommendationRepository(db))


def get_dashboard_service(db: Session = Depends(get_db)) -> DashboardService:
    return DashboardService(KnowledgeRepository(db), RecommendationRepository(db))


def get_trend_service(db: Session = Depends(get_db)) -> TrendService:
    return TrendService(KnowledgeRepository(db))


def get_intelligence_service(db: Session = Depends(get_db)) -> KnowledgeIntelligenceService:
    return KnowledgeIntelligenceService(KnowledgeRepository(db))


def get_intelligence_pipeline(service: KnowledgeIntelligenceService = Depends(get_intelligence_service)) -> KnowledgeIntelligencePipeline:
    return KnowledgeIntelligencePipeline(service)
