from app.agents.common.types import DomainProfile, LLMResult, SearchResult
from app.core.config import get_settings
from app.providers.llm.base import LLMProvider


class DeterministicLLMProvider(LLMProvider):
    name = "deterministic"

    async def complete(self, *, domain_profile: DomainProfile, goal: str, time_window: str, search_results: list[SearchResult]) -> LLMResult:
        settings = get_settings()
        findings = [f"{result.source}: {result.snippet}" for result in search_results]
        actions = [f"Create {content_type} content for {goal} using {domain_profile.display_name or domain_profile.name} signals." for content_type in domain_profile.content_types]
        return LLMResult(
            summary=f"Generated {domain_profile.display_name or domain_profile.name} intelligence for {goal} over {time_window} from {len(search_results)} configured search signals.",
            top_findings=findings,
            recommended_actions=actions,
            token_usage={"prompt_tokens": len(findings) * 12, "completion_tokens": len(actions) * 10},
            model=settings.default_llm_model,
        )
