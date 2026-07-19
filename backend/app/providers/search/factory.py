from app.providers.search.base import SearchProvider
from app.providers.search.configured import ConfiguredSearchProvider


def build_search_provider(name: str) -> SearchProvider:
    providers: dict[str, SearchProvider] = {"configured": ConfiguredSearchProvider()}
    if name not in providers:
        raise ValueError(f"Unsupported search provider: {name}")
    return providers[name]
