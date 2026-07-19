# Development Setup

## Frontend

```bash
cd frontend
npm install
cp .env.example .env
# VITE_API_BASE_URL is optional at runtime; when omitted the client uses same-origin requests.
# VITE_BACKEND_PROXY_TARGET enables the Vite dev proxy for local backend calls.
npm run dev
```

## Backend

```bash
docker compose up -d db
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Docker

```bash
docker compose up --build
```

Frontend: http://localhost:5173
Backend: http://localhost:8000
