from abc import ABC, abstractmethod

from app.agents.common.types import DomainProfile, LLMResult, SearchResult


class LLMProvider(ABC):
    name: str

    @abstractmethod
    async def complete(self, *, domain_profile: DomainProfile, goal: str, time_window: str, search_results: list[SearchResult]) -> LLMResult:
        raise NotImplementedError
