from datetime import datetime

from app.domain.registry import DomainScoringConfig
from app.intelligence import scoring
from app.intelligence.ranking import calculate_intelligence_score, classify_priority
from app.intelligence.schemas import ComponentScores, IntelligenceResult, ProcessingStatus
from app.models.database import KnowledgeItem


class IntelligenceEngine:
    def score_item(self, item: KnowledgeItem, config: DomainScoringConfig) -> IntelligenceResult:
        component_scores = ComponentScores(
            freshness=scoring.freshness_score(item),
            authority=scoring.authority_score(item, config),
            relevance=scoring.relevance_score(item, config),
            momentum=scoring.momentum_score(item, config),
            confidence=scoring.confidence_score(item),
        )
        overall_score = calculate_intelligence_score(component_scores)
        return IntelligenceResult(
            component_scores=component_scores,
            overall_score=overall_score,
            priority=classify_priority(overall_score, config.priority_thresholds),
            processing_status=ProcessingStatus.COMPLETED,
            processed_at=datetime.utcnow(),
        )
