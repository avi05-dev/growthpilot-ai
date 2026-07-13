from pydantic import BaseModel


class TrendSummary(BaseModel):
    id: str
    category: str
    title: str
    description: str
    score: int
    sources: list[str]


class TrendsResponse(BaseModel):
    trends: list[TrendSummary]
