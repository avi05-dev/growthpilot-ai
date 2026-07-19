# Backend

The backend uses Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, and pytest.

## Run locally

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
cd backend
pytest
```

## Configuration

Settings are loaded through Pydantic Settings with the `GROWTHPILOT_` prefix. See `backend/.env.example`.

## Database-backed APIs

GPS-0004A adds PostgreSQL-backed endpoints for domains, knowledge, and recommendations:

- `GET /api/domains`
- `GET /api/knowledge`
- `GET /api/knowledge/{id}`
- `GET /api/recommendations`

Set `DATABASE_URL` to a PostgreSQL SQLAlchemy URL, run Alembic migrations, then run the seed script before starting the API. Repository classes own persistence logic and service classes own business logic.
