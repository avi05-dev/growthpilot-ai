from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.database import Base, Domain, KnowledgeItem, Recommendation
from app.repositories.domain_repository import DomainRepository
from app.repositories.knowledge_repository import KnowledgeRepository
from app.repositories.recommendation_repository import RecommendationRepository
from app.services.domain_service import DomainService
from app.services.knowledge_service import KnowledgeService
from app.services.recommendation_service import RecommendationService


def test_repositories_and_services() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    db.add(Domain(id="technology", name="technology", display_name="Technology", description="Tech", is_enabled=True))
    item = KnowledgeItem(id="item-1", domain="technology", title="Signal", summary="Summary", source="GitHub", category="AI", status="published")
    db.add(item)
    db.flush()
    db.add(Recommendation(id="rec-1", knowledge_item_id="item-1", priority="High", recommended_action="Act", reason="Because", estimated_effort="30 minutes", content_opportunity="Post"))
    db.commit()

    assert DomainService(DomainRepository(db)).list_domains().domains[0].name == "technology"
    assert KnowledgeService(KnowledgeRepository(db)).get_knowledge_item("item-1").title == "Signal"
    assert RecommendationService(RecommendationRepository(db)).list_recommendations().recommendations[0].topic == "Signal"
