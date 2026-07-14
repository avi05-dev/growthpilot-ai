from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class ComponentScoresRead(BaseModel):
    freshness: float | None
    authority: float | None
    relevance: float | None
    momentum: float | None
    confidence: float | None


class KnowledgeItemRead(BaseModel):
    id: str
    domain: str
    title: str
    summary: str
    source: str
    category: str
    url: str | None
    published_at: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime
    component_scores: ComponentScoresRead
    overall_score: float | None
    priority: str | None
    processing_status: str
    processed_at: datetime | None

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def model_validate(cls, obj: Any, *args: Any, **kwargs: Any) -> "KnowledgeItemRead":
        if hasattr(obj, "freshness_score"):
            data = {
                "id": obj.id,
                "domain": obj.domain,
                "title": obj.title,
                "summary": obj.summary,
                "source": obj.source,
                "category": obj.category,
                "url": obj.url,
                "published_at": obj.published_at,
                "status": obj.status,
                "created_at": obj.created_at,
                "updated_at": obj.updated_at,
                "component_scores": {
                    "freshness": obj.freshness_score,
                    "authority": obj.authority_score,
                    "relevance": obj.relevance_score,
                    "momentum": obj.momentum_score,
                    "confidence": obj.confidence_score,
                },
                "overall_score": obj.intelligence_score,
                "priority": obj.priority,
                "processing_status": obj.processing_status,
                "processed_at": obj.processed_at,
            }
            return super().model_validate(data, *args, **kwargs)
        return super().model_validate(obj, *args, **kwargs)


class KnowledgeResponse(BaseModel):
    knowledge: list[KnowledgeItemRead]
