from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WorkspaceGenerateRequest(BaseModel):
    domain: str
    goal: str
    time_window: str


class WorkspaceSource(BaseModel):
    title: str
    url: str
    provider: str

    model_config = ConfigDict(from_attributes=True)


class WorkspaceGenerateResponse(BaseModel):
    summary: str
    top_findings: list[str]
    recommended_actions: list[str]
    sources: list[WorkspaceSource]
    generated_at: datetime
    expires_at: datetime
    cache_hit: bool
