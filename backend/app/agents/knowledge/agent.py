import logging
from time import perf_counter

from app.agents.common.types import AgentState, Source
from app.memory.service import AgentMemoryService
from app.providers.llm.base import LLMProvider
from app.providers.search.base import SearchProvider

logger = logging.getLogger(__name__)


class KnowledgeAgent:
    name = "knowledge"

    def __init__(self, *, memory_service: AgentMemoryService, search_provider: SearchProvider, llm_provider: LLMProvider) -> None:
        self.memory_service = memory_service
        self.search_provider = search_provider
        self.llm_provider = llm_provider

    async def execute(self, state: AgentState) -> AgentState:
        started = perf_counter()
        request = state["request"]
        profile = state["domain_profile"]
        query = f"{request.domain}:{request.goal}:{request.time_window}"
        cache_hit = False
        token_usage: dict[str, int] = {}
        try:
            cached = self.memory_service.get(query=query, domain=request.domain, goal=request.goal, time_window=request.time_window)
            if cached is not None:
                cache_hit = True
                return {**state, "intelligence": cached, "cache_hit": True, "search_provider": self.search_provider.name, "llm_provider": self.llm_provider.name, "token_usage": token_usage}

            search_results = await self.search_provider.search(domain_profile=profile, goal=request.goal, time_window=request.time_window)
            llm_result = await self.llm_provider.complete(domain_profile=profile, goal=request.goal, time_window=request.time_window, search_results=search_results)
            token_usage = llm_result.token_usage
            sources = [Source(title=result.title, url=result.url, provider=result.source) for result in search_results]
            intelligence = self.memory_service.save(
                query=query,
                domain=request.domain,
                goal=request.goal,
                time_window=request.time_window,
                summary=llm_result.summary,
                findings=llm_result.top_findings,
                recommended_actions=llm_result.recommended_actions,
                sources=sources,
                provider=self.search_provider.name,
                llm_model=llm_result.model,
                metadata={"token_usage": token_usage, "llm_provider": self.llm_provider.name},
            )
            return {**state, "intelligence": intelligence, "cache_hit": False, "search_provider": self.search_provider.name, "llm_provider": self.llm_provider.name, "token_usage": token_usage}
        except Exception:
            logger.exception("agent_execution_error", extra={"agent_name": self.name})
            raise
        finally:
            elapsed_ms = (perf_counter() - started) * 1000
            logger.info(
                "agent_execution",
                extra={
                    "agent_name": self.name,
                    "execution_time_ms": elapsed_ms,
                    "cache_hit": cache_hit,
                    "search_provider": self.search_provider.name,
                    "llm_provider": self.llm_provider.name,
                    "token_usage": token_usage,
                    "latency_ms": elapsed_ms,
                },
            )
