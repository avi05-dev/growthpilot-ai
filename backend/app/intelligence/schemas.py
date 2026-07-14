from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class ProcessingStatus(StrEnum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Priority(StrEnum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class ComponentScores(BaseModel):
    freshness: float = Field(ge=0.0, le=100.0)
    authority: float = Field(ge=0.0, le=100.0)
    relevance: float = Field(ge=0.0, le=100.0)
    momentum: float = Field(ge=0.0, le=100.0)
    confidence: float = Field(ge=0.0, le=100.0)


class IntelligenceResult(BaseModel):
    component_scores: ComponentScores
    overall_score: float = Field(ge=0.0, le=100.0)
    priority: Priority
    processing_status: ProcessingStatus
    processed_at: datetime


class ProcessResponse(BaseModel):
    processed: int
    failed: int
    duration_ms: int


class IntelligenceHealth(BaseModel):
    status: str
    engine: str
    supported_domains: list[str]
