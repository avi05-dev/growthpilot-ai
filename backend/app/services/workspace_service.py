from app.agents.common.types import AgentRequest
from app.graph.runtime import LangGraphRuntime
from app.schemas.workspace import WorkspaceGenerateRequest, WorkspaceGenerateResponse, WorkspaceSource


class WorkspaceService:
    def __init__(self, runtime: LangGraphRuntime) -> None:
        self.runtime = runtime

    async def generate(self, request: WorkspaceGenerateRequest) -> WorkspaceGenerateResponse:
        intelligence = await self.runtime.generate(AgentRequest(domain=request.domain, goal=request.goal, time_window=request.time_window))
        return WorkspaceGenerateResponse(
            summary=intelligence.summary,
            top_findings=intelligence.top_findings,
            recommended_actions=intelligence.recommended_actions,
            sources=[WorkspaceSource.model_validate(source) for source in intelligence.sources],
            generated_at=intelligence.generated_at,
            expires_at=intelligence.expires_at,
            cache_hit=intelligence.cache_hit,
        )
