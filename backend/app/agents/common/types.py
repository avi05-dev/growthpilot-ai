from datetime import datetime
from typing import Any, TypedDict

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    domain: str
    goal: str
    time_window: str


class DomainProfile(BaseModel):
    name: str
    display_name: str | None = None
    search_queries: list[str] = Field(default_factory=list)
    trusted_sources: list[str] = Field(default_factory=list)
    content_types: list[str] = Field(default_factory=list)


class WorkflowDefinition(BaseModel):
    name: str
    steps: list[str]


class Source(BaseModel):
    title: str
    url: str
    provider: str


class SearchResult(BaseModel):
    title: str
    snippet: str
    url: str
    source: str


class LLMResult(BaseModel):
    summary: str
    top_findings: list[str]
    recommended_actions: list[str]
    token_usage: dict[str, int] = Field(default_factory=dict)
    model: str


class WorkspaceIntelligence(BaseModel):
    summary: str
    top_findings: list[str]
    recommended_actions: list[str]
    sources: list[Source]
    generated_at: datetime
    expires_at: datetime
    cache_hit: bool


class AgentState(TypedDict, total=False):
    request: AgentRequest
    workflow_name: str
    workflow_steps: list[str]
    domain_profile: DomainProfile
    intelligence: WorkspaceIntelligence
    cache_hit: bool
    search_provider: str
    llm_provider: str
    token_usage: dict[str, int]
    metadata: dict[str, Any]
