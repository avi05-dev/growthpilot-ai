from dataclasses import dataclass, field

from app.intelligence.constants import DEFAULT_PRIORITY_THRESHOLDS
from app.intelligence.exceptions import UnsupportedDomainError


@dataclass(frozen=True)
class DomainScoringConfig:
    name: str
    authority_sources: dict[str, float] = field(default_factory=dict)
    relevance_keywords: tuple[str, ...] = ()
    momentum_categories: dict[str, float] = field(default_factory=dict)
    priority_thresholds: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_PRIORITY_THRESHOLDS))


class DomainRegistry:
    def __init__(self) -> None:
        self._domains: dict[str, DomainScoringConfig] = {
            "technology": DomainScoringConfig(
                name="technology",
                authority_sources={"github": 92.0, "arxiv": 88.0, "openai": 90.0, "google": 86.0, "microsoft": 84.0, "hacker news": 72.0},
                relevance_keywords=("ai", "agent", "automation", "developer", "growth", "product", "security", "data", "cloud", "api"),
                momentum_categories={"AI": 92.0, "Development": 82.0, "Career": 64.0},
            )
        }

    def supported_domains(self) -> list[str]:
        return sorted(self._domains)

    def validate(self, domain: str) -> None:
        if domain.lower() not in self._domains:
            raise UnsupportedDomainError(f"Unsupported domain: {domain}")

    def get_config(self, domain: str) -> DomainScoringConfig:
        normalized = domain.lower()
        self.validate(normalized)
        return self._domains[normalized]
