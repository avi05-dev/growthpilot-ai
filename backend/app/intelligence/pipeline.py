import logging
from time import perf_counter

from app.domain.registry import DomainRegistry
from app.intelligence.engine import IntelligenceEngine
from app.intelligence.schemas import ProcessResponse
from app.services.intelligence_service import KnowledgeIntelligenceService

logger = logging.getLogger(__name__)


class KnowledgeIntelligencePipeline:
    def __init__(self, service: KnowledgeIntelligenceService, registry: DomainRegistry | None = None, engine: IntelligenceEngine | None = None) -> None:
        self.service = service
        self.registry = registry or DomainRegistry()
        self.engine = engine or IntelligenceEngine()

    def process_pending(self) -> ProcessResponse:
        started = perf_counter()
        processed = 0
        failed = 0
        logger.info("Processing started")
        for item in self.service.list_pending_items():
            try:
                self.service.process_item(item, self.registry, self.engine)
                processed += 1
            except Exception:
                failed += 1
                logger.exception("Processing failed", extra={"knowledge_item_id": item.id})
        duration_ms = int((perf_counter() - started) * 1000)
        logger.info("Processing completed", extra={"processed": processed, "failed": failed, "duration_ms": duration_ms})
        return ProcessResponse(processed=processed, failed=failed, duration_ms=duration_ms)
