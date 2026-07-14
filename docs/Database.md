# Database

GrowthPilot AI uses PostgreSQL for the persistence foundation introduced in GPS-0004A.

## Configuration

Set `DATABASE_URL` before running migrations, seed scripts, or the API:

```bash
export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/growthpilot
```

## Migrations

Alembic migrations live in `backend/alembic/versions`.

```bash
cd backend
alembic upgrade head
```

## Seed data

The seed script creates the Technology domain, 10 knowledge items, and 10 recommendations.

```bash
cd backend
python -m scripts.seed
```

## Tables

- `domains`: enabled business/content domains.
- `knowledge_items`: curated source material for the dashboard and trend radar.
- `recommendations`: persisted action recommendations linked to knowledge items.

## Knowledge Intelligence Columns

GPS-0004B extends `knowledge_items` with persisted intelligence fields:

- `freshness_score`
- `authority_score`
- `relevance_score`
- `momentum_score`
- `confidence_score`
- `intelligence_score`
- `priority`
- `processing_status`
- `processed_at`

Migration `0002_add_intelligence_fields` adds these columns. Existing rows default to the `Pending` processing status until the processing endpoint calculates and persists intelligence values.
