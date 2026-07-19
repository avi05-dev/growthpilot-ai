from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "GrowthPilot AI API"
    version: str = "0.5.0"
    environment: str = "development"
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    database_url: str = Field("postgresql+psycopg://postgres:postgres@localhost:5432/growthpilot", validation_alias="DATABASE_URL")
    agent_memory_ttl_minutes: int = Field(1440, validation_alias="AGENT_MEMORY_TTL_MINUTES")
    default_search_provider: str = Field("configured", validation_alias="SEARCH_PROVIDER")
    default_llm_provider: str = Field("deterministic", validation_alias="LLM_PROVIDER")
    default_llm_model: str = Field("growthpilot-deterministic-v1", validation_alias="LLM_MODEL")

    model_config = SettingsConfigDict(env_file=".env", env_prefix="GROWTHPILOT_", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
