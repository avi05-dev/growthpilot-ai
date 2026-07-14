from app.intelligence.constants import INTELLIGENCE_SCORE_WEIGHTS
from app.intelligence.schemas import ComponentScores, Priority


def calculate_intelligence_score(scores: ComponentScores) -> float:
    weighted = (
        scores.freshness * INTELLIGENCE_SCORE_WEIGHTS["freshness"]
        + scores.relevance * INTELLIGENCE_SCORE_WEIGHTS["relevance"]
        + scores.authority * INTELLIGENCE_SCORE_WEIGHTS["authority"]
        + scores.momentum * INTELLIGENCE_SCORE_WEIGHTS["momentum"]
        + scores.confidence * INTELLIGENCE_SCORE_WEIGHTS["confidence"]
    )
    return round(weighted, 2)


def classify_priority(score: float, thresholds: dict[str, float]) -> Priority:
    ordered = sorted(thresholds.items(), key=lambda item: item[1], reverse=True)
    for priority, threshold in ordered:
        if score >= threshold:
            return Priority(priority)
    return Priority.LOW
