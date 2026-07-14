from fastapi import APIRouter, Depends

from app.dependencies.services import get_intelligence_pipeline
from app.domain.registry import DomainRegistry
from app.intelligence.pipeline import KnowledgeIntelligencePipeline
from app.intelligence.schemas import IntelligenceHealth, ProcessResponse

router = APIRouter(prefix="/api/intelligence", tags=["intelligence"])


@router.post("/process", response_model=ProcessResponse)
def process_pending(pipeline: KnowledgeIntelligencePipeline = Depends(get_intelligence_pipeline)) -> ProcessResponse:
    return pipeline.process_pending()


@router.get("/health", response_model=IntelligenceHealth)
def intelligence_health() -> IntelligenceHealth:
    registry = DomainRegistry()
    return IntelligenceHealth(status="healthy", engine="running", supported_domains=registry.supported_domains())
