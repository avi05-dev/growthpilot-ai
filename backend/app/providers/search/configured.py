from app.agents.common.types import DomainProfile, SearchResult
from app.providers.search.base import SearchProvider


class ConfiguredSearchProvider(SearchProvider):
    name = "configured"

    async def search(self, *, domain_profile: DomainProfile, goal: str, time_window: str) -> list[SearchResult]:
        results: list[SearchResult] = []
        sources = domain_profile.trusted_sources or [domain_profile.display_name or domain_profile.name]
        for index, query in enumerate(domain_profile.search_queries):
            source = sources[index % len(sources)]
            results.append(
                SearchResult(
                    title=f"{query.title()} signal",
                    snippet=f"{source} signal for {goal} in the {time_window} window.",
                    url=f"https://example.com/{domain_profile.name}/{index + 1}",
                    source=source,
                )
            )
        return results
