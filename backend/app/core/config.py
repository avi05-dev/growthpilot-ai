from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GrowthPilot AI API"
    version: str = "0.4.0"
    environment: str = "development"
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    database_url: str = Field("postgresql+psycopg://postgres:postgres@localhost:5432/growthpilot", validation_alias="DATABASE_URL")

    model_config = SettingsConfigDict(env_file=".env", env_prefix="GROWTHPILOT_", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
