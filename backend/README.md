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

## Debug an actual UI request in VS Code

1. Open the repository root in VS Code and install the **Python** extension.
2. Run **Python: Select Interpreter** and choose `backend/.venv/bin/python`.
3. Set up the database before starting the API:

   ```bash
   cp .env.example .env
   alembic upgrade head
   python -m scripts.seed
   ```

4. Put a breakpoint in `app/api/workspace.py` on:

   ```python
   return await service.generate(request)
   ```

5. Open **Run and Debug**, choose **Debug FastAPI backend**, and press `F5`.
   This uses the repository's `.vscode/launch.json` configuration.
6. In a separate VS Code terminal, start the frontend:

   ```bash
   cd ../frontend
   npm install
   cp .env.example .env
   npm run dev
   ```

7. Open http://localhost:5173/dashboard and click **Generate Intelligence**.
   The UI sends `POST /api/workspace/generate`, which pauses on the
   breakpoint.

Use `F10` to step over lines, `F11` to enter a function, and `F5` to continue.
Set a second breakpoint in `app/services/workspace_service.py` to follow the
request into the service and agent workflow.

## Debug with Docker Compose

From the repository root, start the backend and frontend with the debug
overlay:

```bash
docker compose -f docker-compose.yml -f docker-compose.debug.yml up --build
```

PostgreSQL must be running on the host and have the migrations and seed data
applied. The overlay uses `host.docker.internal` to reach the host database;
set `DATABASE_URL` before the command to use another database.

The backend waits for VS Code on port `5678`. In VS Code, select **Attach to
FastAPI backend (Docker)** in **Run and Debug** and press `F5`. The attached
debugger maps the local `backend/` directory to `/app` in the container.

Once attached, open http://localhost:5173/dashboard and click **Generate
Intelligence** to hit a breakpoint in `app/api/workspace.py`.
