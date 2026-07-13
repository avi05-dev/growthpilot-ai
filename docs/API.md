# API

Base URL is configured by the frontend with `VITE_API_BASE_URL`.

## Endpoints

- `GET /health` returns `{ "status": "healthy" }`.
- `GET /version` returns `{ "version": "0.3.0" }`.
- `GET /api/dashboard` returns the daily briefing, action center, and growth snapshot.
- `GET /api/trends` returns trend summaries.
- `GET /api/recommendations` returns content recommendations.

OpenAPI is available at `/openapi.json` and Swagger UI at `/docs` when the backend is running.
