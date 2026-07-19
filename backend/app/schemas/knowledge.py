from datetime import datetime

from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)


class KnowledgeResponse(BaseModel):
    knowledge: list[KnowledgeItemRead]
