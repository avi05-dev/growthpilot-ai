from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.domain_repository import DomainRepository
from app.repositories.knowledge_repository import KnowledgeRepository
from app.memory.repository import AgentMemoryRepository
from app.memory.service import AgentMemoryService
from app.repositories.recommendation_repository import RecommendationRepository
from app.services.dashboard_service import DashboardService
from app.services.domain_service import DomainService
from app.services.knowledge_service import KnowledgeService
from app.services.recommendation_service import RecommendationService
from app.services.trend_service import TrendService
from app.services.workspace_service import WorkspaceService
from app.agents.knowledge.agent import KnowledgeAgent
from app.agents.planner.agent import PlannerAgent
from app.core.config import get_settings
from app.graph.runtime import LangGraphRuntime
from app.providers.llm.factory import build_llm_provider
from app.providers.search.factory import build_search_provider


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


def get_workspace_service(db: Session = Depends(get_db)) -> WorkspaceService:
    settings = get_settings()
    memory_service = AgentMemoryService(AgentMemoryRepository(db))
    knowledge_agent = KnowledgeAgent(
        memory_service=memory_service,
        search_provider=build_search_provider(settings.default_search_provider),
        llm_provider=build_llm_provider(settings.default_llm_provider),
    )
    runtime = LangGraphRuntime(workflow_name="generate_intelligence", agents={"planner": PlannerAgent(), "knowledge": knowledge_agent})
    return WorkspaceService(runtime)
