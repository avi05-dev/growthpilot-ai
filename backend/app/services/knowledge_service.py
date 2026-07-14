from fastapi import HTTPException

from app.repositories.knowledge_repository import KnowledgeRepository
from app.schemas.knowledge import KnowledgeItemRead, KnowledgeResponse


class KnowledgeService:
    def __init__(self, repository: KnowledgeRepository) -> None:
        self.repository = repository

    def list_knowledge(self, domain: str | None = None) -> KnowledgeResponse:
        return KnowledgeResponse(knowledge=[KnowledgeItemRead.model_validate(item) for item in self.repository.list(domain)])

    def get_knowledge_item(self, item_id: str) -> KnowledgeItemRead:
        item = self.repository.get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Knowledge item not found")
        return KnowledgeItemRead.model_validate(item)
