from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.session import get_db
from app.main import app
from app.models.database import Base, Domain, KnowledgeItem, Recommendation


@pytest.fixture()
def db_session() -> Generator[Session, None, None]:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        db.add(Domain(id="technology", name="technology", display_name="Technology", description="Technology domain", is_enabled=True))
        items = []
        for index in range(10):
            item = KnowledgeItem(id=f"knowledge-{index}", domain="technology", title=f"Signal {index}", summary=f"Summary {index}", source="GitHub", category=["AI", "Development", "Career"][index % 3], status="published")
            items.append(item)
            db.add(item)
        db.flush()
        for index, item in enumerate(items):
            db.add(Recommendation(id=f"recommendation-{index}", knowledge_item_id=item.id, priority=["High", "Medium", "Low"][index % 3], recommended_action=f"Action {index}", reason=f"Reason {index}", estimated_effort="30 minutes", content_opportunity=f"Opportunity {index}"))
        db.commit()
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(db_session: Session) -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version_endpoint(client: TestClient) -> None:
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.4.0"}


def test_dashboard_endpoint(client: TestClient) -> None:
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    payload = response.json()
    assert payload["briefing"]["title"] == "Today's Briefing"
    assert len(payload["actionTasks"]) == 4
    assert len(payload["kpis"]) == 4


def test_domains_endpoint(client: TestClient) -> None:
    response = client.get("/api/domains")
    assert response.status_code == 200
    assert response.json()["domains"][0]["name"] == "technology"


def test_knowledge_endpoints(client: TestClient) -> None:
    response = client.get("/api/knowledge")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["knowledge"]) == 10
    detail = client.get(f"/api/knowledge/{payload['knowledge'][0]['id']}")
    assert detail.status_code == 200


def test_trends_endpoint(client: TestClient) -> None:
    response = client.get("/api/trends")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["trends"]) == 9


def test_recommendations_endpoint(client: TestClient) -> None:
    response = client.get("/api/recommendations")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["recommendations"]) == 10
    assert payload["recommendations"][0]["channel"] in {"AI", "Development", "Career"}
