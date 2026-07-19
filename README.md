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

## API Documentation

When the backend is running:

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json

## Debug a UI request in VS Code

The repository includes a VS Code debug configuration at `.vscode/launch.json`.
It starts the FastAPI backend with the working directory set to `backend/`.

### One-time setup

1. Install the VS Code **Python** extension.
2. In VS Code, run **Python: Select Interpreter** and select
   `backend/.venv/bin/python`.
3. Start PostgreSQL, then set up and seed the backend database:

   ```bash
   docker compose up -d db
   cd backend
   source .venv/bin/activate
   cp .env.example .env
   alembic upgrade head
   python -m scripts.seed
   ```

4. In a second VS Code terminal, start the frontend:

   ```bash
   cd frontend
   npm install
   cp .env.example .env
   npm run dev
   ```

### Run and step through a real browser request

1. Set a breakpoint in `backend/app/api/workspace.py` on the
   `return await service.generate(request)` line. Optionally set another in
   `backend/app/services/workspace_service.py` inside `generate`.
2. Open **Run and Debug** (`Cmd+Shift+D` on macOS), select **Debug FastAPI
   backend**, and press `F5`.
3. Open http://localhost:5173/dashboard in a browser.
4. In the **Generate Intelligence** card, click **Generate Intelligence**.
   The frontend sends `POST /api/workspace/generate`, and VS Code pauses at
   the breakpoint.
5. Use the debug controls to inspect `request` and step through the backend:

   - `F10` — step over
   - `F11` — step into a function
   - `Shift+F11` — step out
   - `F5` — continue
   - `Shift+F5` — stop

If the frontend reports a network error, confirm both terminals are running:
the frontend must be on port 5173 and the VS Code backend debugger must be on
port 8000. The browser's Network tab will show the corresponding API request.

### Debug with Docker Compose

To run the backend in Docker and attach VS Code to it, start the debug Compose
overlay from the repository root:

```bash
docker compose -f docker-compose.yml -f docker-compose.debug.yml up --build
```

Compose starts PostgreSQL, applies the Alembic migrations, and runs the
idempotent seed script before it starts the debugger. This prevents requests
paused in VS Code from failing because a table or the initial records are
missing.

The backend waits for the debugger on port `5678`. In VS Code, open **Run and
Debug**, select **Attach to FastAPI backend (Docker)**, and press `F5`. The API
then starts on port `8000`, and the frontend is available at
http://localhost:5173.

Set a breakpoint in `backend/app/api/workspace.py`, open the dashboard, and
click **Generate Intelligence** to step through the actual browser request.
The source mapping between `backend/` on your machine and `/app` in the
container is already configured. Stop the containers with `Ctrl+C` or run:

```bash
docker compose -f docker-compose.yml -f docker-compose.debug.yml down
```

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

## GPS-0005 Agent Workspace

The workspace can generate agent-driven intelligence through LangGraph:

```bash
cd backend
export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/growthpilot
alembic upgrade head
uvicorn app.main:app --reload
```

Then run the frontend and use the Generate Intelligence button. The current workflow is configured in `backend/config/workflows/generate_intelligence.yaml` and domain profiles live under `backend/config/domains`.
