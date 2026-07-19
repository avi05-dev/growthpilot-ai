from datetime import datetime, timedelta, timezone

from app.agents.common.types import Source, WorkspaceIntelligence
from app.core.config import get_settings
from app.memory.repository import AgentMemoryRepository
from app.models.database import AgentMemory


class AgentMemoryService:
    def __init__(self, repository: AgentMemoryRepository) -> None:
        self.repository = repository

    def get(self, *, query: str, domain: str, goal: str, time_window: str) -> WorkspaceIntelligence | None:
        memory = self.repository.get_valid(query=query, domain=domain, goal=goal, time_window=time_window)
        if memory is None:
            return None
        return WorkspaceIntelligence(
            summary=memory.summary,
            top_findings=memory.findings,
            recommended_actions=memory.recommended_actions,
            sources=[Source.model_validate(source) for source in memory.sources],
            generated_at=memory.created_at,
            expires_at=memory.expires_at,
            cache_hit=True,
        )

    def save(
        self,
        *,
        query: str,
        domain: str,
        goal: str,
        time_window: str,
        summary: str,
        findings: list[str],
        recommended_actions: list[str],
        sources: list[Source],
        provider: str,
        llm_model: str,
        metadata: dict[str, object],
    ) -> WorkspaceIntelligence:
        settings = get_settings()
        now = datetime.now(timezone.utc)
        expires_at = now + timedelta(minutes=settings.agent_memory_ttl_minutes)
        memory = AgentMemory(
            query=query,
            domain=domain,
            goal=goal,
            time_window=time_window,
            summary=summary,
            findings=findings,
            recommended_actions=recommended_actions,
            sources=[source.model_dump() for source in sources],
            provider=provider,
            llm_model=llm_model,
            memory_metadata=metadata,
            created_at=now,
            expires_at=expires_at,
        )
        saved = self.repository.save(memory)
        return WorkspaceIntelligence(
            summary=saved.summary,
            top_findings=saved.findings,
            recommended_actions=saved.recommended_actions,
            sources=[Source.model_validate(source) for source in saved.sources],
            generated_at=saved.created_at,
            expires_at=saved.expires_at,
            cache_hit=False,
        )
