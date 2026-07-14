from datetime import UTC, datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.domain.registry import DomainRegistry
from app.intelligence.engine import IntelligenceEngine
from app.intelligence.pipeline import KnowledgeIntelligencePipeline
from app.intelligence.ranking import calculate_intelligence_score, classify_priority
from app.intelligence.schemas import ComponentScores, Priority
from app.intelligence.scoring import authority_score, confidence_score, freshness_score, relevance_score
from app.models.database import Base, KnowledgeItem
from app.repositories.knowledge_repository import KnowledgeRepository
from app.services.intelligence_service import KnowledgeIntelligenceService


def make_item() -> KnowledgeItem:
    return KnowledgeItem(
        id="item-1",
        domain="technology",
        title="AI agent API automation",
        summary="A detailed technology signal about developer automation and product growth.",
        source="GitHub",
        category="AI",
        url="https://example.com",
        published_at=datetime.now(UTC) - timedelta(days=1),
        status="published",
    )


def test_scoring_functions_return_bounded_scores() -> None:
    item = make_item()
    config = DomainRegistry().get_config("technology")
    scores = [freshness_score(item), authority_score(item, config), relevance_score(item, config), confidence_score(item)]
    assert all(0.0 <= score <= 100.0 for score in scores)


def test_ranking_calculates_score_and_priority() -> None:
    score = calculate_intelligence_score(ComponentScores(freshness=100, authority=80, relevance=90, momentum=70, confidence=60))
    assert score == 83.5
    assert classify_priority(score, {"Critical": 85, "High": 70, "Medium": 45, "Low": 0}) is Priority.HIGH


def test_pipeline_processes_pending_items() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    db.add(make_item())
    db.commit()

    repository = KnowledgeRepository(db)
    service = KnowledgeIntelligenceService(repository)
    response = KnowledgeIntelligencePipeline(service).process_pending()
    processed = repository.get("item-1")

    assert response.processed == 1
    assert response.failed == 0
    assert processed is not None
    assert processed.processing_status == "Completed"
    assert processed.intelligence_score is not None
    assert processed.priority in {"Critical", "High", "Medium", "Low"}
