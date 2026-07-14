from app.domain.registry import DomainRegistry
from app.intelligence.engine import IntelligenceEngine
from app.intelligence.schemas import ProcessingStatus
from app.models.database import KnowledgeItem
from app.repositories.knowledge_repository import KnowledgeRepository


class KnowledgeIntelligenceService:
    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def list_pending_items(self) -> list[KnowledgeItem]:
        return self.repository.list_by_processing_status(ProcessingStatus.PENDING.value)

    def process_item(self, item: KnowledgeItem, registry: DomainRegistry, engine: IntelligenceEngine) -> KnowledgeItem:
        item.processing_status = ProcessingStatus.PROCESSING.value
        self.repository.save(item)
        try:
            config = registry.get_config(item.domain)
            result = engine.score_item(item, config)
            item.freshness_score = result.component_scores.freshness
            item.authority_score = result.component_scores.authority
            item.relevance_score = result.component_scores.relevance
            item.momentum_score = result.component_scores.momentum
            item.confidence_score = result.component_scores.confidence
            item.intelligence_score = result.overall_score
            item.priority = result.priority.value
            item.processing_status = result.processing_status.value
            item.processed_at = result.processed_at
        except Exception:
            item.processing_status = ProcessingStatus.FAILED.value
            self.repository.save(item)
            raise
        return self.repository.save(item)
