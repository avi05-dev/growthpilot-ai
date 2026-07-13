from fastapi import APIRouter, Depends, Query

from app.dependencies.services import get_knowledge_service
from app.schemas.knowledge import KnowledgeItemRead, KnowledgeResponse
from app.services.knowledge_service import KnowledgeService

router = APIRouter(prefix="/api", tags=["knowledge"])


@router.get("/knowledge", response_model=KnowledgeResponse)
def list_knowledge(domain: str | None = Query(default=None), service: KnowledgeService = Depends(get_knowledge_service)) -> KnowledgeResponse:
    return service.list_knowledge(domain)


@router.get("/knowledge/{item_id}", response_model=KnowledgeItemRead)
def get_knowledge_item(item_id: str, service: KnowledgeService = Depends(get_knowledge_service)) -> KnowledgeItemRead:
    return service.get_knowledge_item(item_id)
