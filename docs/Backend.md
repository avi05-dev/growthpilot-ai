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
