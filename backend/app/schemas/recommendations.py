from pydantic import BaseModel


class Recommendation(BaseModel):
    id: str
    channel: str
    topic: str
    actionLabel: str


class RecommendationsResponse(BaseModel):
    recommendations: list[Recommendation]
