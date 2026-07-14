# GrowthPilot AI

GrowthPilot AI is an AI-powered growth command center for monitoring acquisition, activation, and revenue signals. Version `0.3.0` transitions the project from a frontend prototype into a production-ready full-stack foundation.

## v0.3.0 Architecture

```text
React Frontend
  ↓
REST API
  ↓
FastAPI
  ↓
Service Layer
  ↓
Repository Layer
  ↓
Mock Data
```

The frontend no longer reads local mock data. Dashboard, trend, and recommendation data is served by the FastAPI backend through REST APIs.

## Repository Structure

```text
frontend/        React + TypeScript + Vite application
backend/         FastAPI application, services, repositories, schemas, tests
docs/            Architecture, API, backend, and setup documentation
infrastructure/  Future deployment and database infrastructure assets
.github/         CI workflows
```

## Frontend

- React + TypeScript
- Vite
- Material UI + Emotion
- React Router
- Axios
- TanStack Query

```bash
cd frontend
npm install
npm run dev
npm run build
```

## Backend

- Python 3.12
- FastAPI
- Pydantic v2
- SQLAlchemy 2
- Alembic
- pytest

```bash
cd backend
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

## Docker

```bash
docker compose up --build
```

Frontend: http://localhost:5173
Backend: http://localhost:8000
PostgreSQL: localhost:5432

## API Documentation

When the backend is running:

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json

## Documentation

- [Architecture](./docs/Architecture.md)
- [Backend](./docs/Backend.md)
- [API](./docs/API.md)
- [Development Setup](./docs/DevelopmentSetup.md)

## Release Notes

See [CHANGELOG.md](./CHANGELOG.md) for release history.

## GPS-0004A PostgreSQL persistence

The app now reads dashboard, trend, domain, knowledge, and recommendation data through database-backed FastAPI services.

```bash
cd backend
export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/growthpilot
alembic upgrade head
python -m scripts.seed
uvicorn app.main:app --reload
```

Frontend data fetching continues to use React Query against the FastAPI endpoints.
When using Docker Compose, Postgres, migrations, and seed data all start with the stack.

## GPS-0004B Knowledge Intelligence Engine

Version `0.4.0` introduces the first Knowledge Intelligence Engine. Stored knowledge items can now be processed into explainable component scores, an overall Intelligence Score, a priority classification, and a processing status.

```text
Knowledge Item
  ↓ Validation and domain configuration
  ↓ Freshness, Authority, Relevance, Momentum, Confidence scores
  ↓ Weighted Intelligence Score
  ↓ Priority classification
  ↓ Persisted results
  ↓ Dashboard display
```

New endpoints:

- `GET /api/intelligence/health` reports engine health and supported domains.
- `POST /api/intelligence/process` processes all pending knowledge items.
- `GET /api/knowledge` includes component scores, overall score, priority, status, and processed timestamp.

The engine is domain-independent. Domain-specific scoring inputs currently live in the Technology domain registry and can later move to YAML or JSON configuration.
