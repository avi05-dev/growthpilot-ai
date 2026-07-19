from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Recommendation(BaseModel):
    id: str
    knowledge_item_id: str
    priority: str
    recommended_action: str
    reason: str
    estimated_effort: str
    content_opportunity: str
    created_at: datetime
    topic: str
    channel: str = "Content"
    action_label: str = Field("Generate Draft", serialization_alias="actionLabel")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class RecommendationsResponse(BaseModel):
    recommendations: list[Recommendation]
