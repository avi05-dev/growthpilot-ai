# Architecture

GrowthPilot AI v0.3.0 is a monorepo with a React frontend and FastAPI backend.

```text
React Frontend -> REST API -> FastAPI -> Service Layer -> Repository Layer -> Mock Data
```

The frontend never imports mock data. All application data is retrieved through REST endpoints. Backend repositories currently return mock data only, which keeps v0.3.0 focused on architecture rather than AI, integrations, or persistence.

## Backend layering

- API routers: HTTP contracts and dependency injection only.
- Services: business orchestration and future policy decisions.
- Repositories: data access. In v0.3.0 this is mock data; in v0.4.0 it can become PostgreSQL-backed.
- Schemas: Pydantic response models defining the REST contract.

## v0.4.0 readiness

SQLAlchemy and Alembic are installed and scaffolded so PostgreSQL models and migrations can be introduced without changing the API or frontend contracts.
