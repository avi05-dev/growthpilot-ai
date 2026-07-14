from datetime import UTC, datetime

from app.domain.registry import DomainScoringConfig
from app.intelligence.constants import SCORE_MAX, SCORE_MIN
from app.models.database import KnowledgeItem


def clamp_score(value: float) -> float:
    return round(max(SCORE_MIN, min(SCORE_MAX, value)), 2)


def freshness_score(item: KnowledgeItem, now: datetime | None = None) -> float:
    if item.published_at is None:
        return 40.0
    reference = now or datetime.now(UTC)
    published = item.published_at if item.published_at.tzinfo else item.published_at.replace(tzinfo=UTC)
    age_days = max((reference - published).days, 0)
    if age_days <= 1:
        return 100.0
    if age_days <= 7:
        return clamp_score(95.0 - (age_days * 5.0))
    if age_days <= 30:
        return clamp_score(70.0 - ((age_days - 7) * 1.5))
    if age_days <= 90:
        return clamp_score(35.0 - ((age_days - 30) * 0.35))
    return 10.0


def authority_score(item: KnowledgeItem, config: DomainScoringConfig) -> float:
    source = item.source.lower()
    for trusted_source, score in config.authority_sources.items():
        if trusted_source in source:
            return clamp_score(score)
    if item.url:
        return 60.0
    return 45.0


def relevance_score(item: KnowledgeItem, config: DomainScoringConfig) -> float:
    text = f"{item.title} {item.summary} {item.category}".lower()
    matches = sum(1 for keyword in config.relevance_keywords if keyword.lower() in text)
    base = 45.0
    return clamp_score(base + (matches * 9.0))


def momentum_score(item: KnowledgeItem, config: DomainScoringConfig) -> float:
    if item.category in config.momentum_categories:
        return clamp_score(config.momentum_categories[item.category])
    return 55.0


def confidence_score(item: KnowledgeItem) -> float:
    score = 35.0
    if item.title.strip():
        score += 15.0
    if len(item.summary.strip()) >= 40:
        score += 20.0
    elif item.summary.strip():
        score += 10.0
    if item.source.strip():
        score += 10.0
    if item.url:
        score += 10.0
    if item.published_at:
        score += 10.0
    return clamp_score(score)
