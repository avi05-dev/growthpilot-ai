from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version_endpoint() -> None:
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.3.0"}


def test_dashboard_endpoint() -> None:
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    payload = response.json()
    assert payload["briefing"]["title"] == "Today's Briefing"
    assert len(payload["actionTasks"]) == 4
    assert len(payload["kpis"]) == 4


def test_trends_endpoint() -> None:
    response = client.get("/api/trends")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["trends"]) == 9
    assert payload["trends"][0]["category"] == "AI"


def test_recommendations_endpoint() -> None:
    response = client.get("/api/recommendations")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["recommendations"]) == 3
    assert payload["recommendations"][0]["channel"] == "LinkedIn"
