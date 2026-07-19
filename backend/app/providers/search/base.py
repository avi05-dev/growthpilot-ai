from abc import ABC, abstractmethod

from app.agents.common.types import DomainProfile, SearchResult


class SearchProvider(ABC):
    name: str

    @abstractmethod
    async def search(self, *, domain_profile: DomainProfile, goal: str, time_window: str) -> list[SearchResult]:
        raise NotImplementedError
