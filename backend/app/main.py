from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dashboard import router as dashboard_router
from app.api.recommendations import router as recommendations_router
from app.api.system import router as system_router
from app.api.trends import router as trends_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.middleware.logging import RequestLoggingMiddleware

configure_logging()
settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.version)

app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system_router)
app.include_router(dashboard_router)
app.include_router(trends_router)
app.include_router(recommendations_router)
