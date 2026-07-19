from app.providers.llm.base import LLMProvider
from app.providers.llm.deterministic import DeterministicLLMProvider


def build_llm_provider(name: str) -> LLMProvider:
    providers: dict[str, LLMProvider] = {"deterministic": DeterministicLLMProvider()}
    if name not in providers:
        raise ValueError(f"Unsupported LLM provider: {name}")
    return providers[name]
