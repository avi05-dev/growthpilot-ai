# GrowthPilot AI Backend

FastAPI backend for GrowthPilot AI v0.3.0.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest
```

## API docs

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json
