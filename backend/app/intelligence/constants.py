from typing import Final

SCORE_MIN: Final[float] = 0.0
SCORE_MAX: Final[float] = 100.0

INTELLIGENCE_SCORE_WEIGHTS: Final[dict[str, float]] = {
    "freshness": 0.25,
    "relevance": 0.25,
    "authority": 0.20,
    "momentum": 0.20,
    "confidence": 0.10,
}

DEFAULT_PRIORITY_THRESHOLDS: Final[dict[str, float]] = {
    "Critical": 85.0,
    "High": 70.0,
    "Medium": 45.0,
    "Low": 0.0,
}
