from fastapi import APIRouter, Depends

from app.dependencies.services import get_workspace_service
from app.schemas.workspace import WorkspaceGenerateRequest, WorkspaceGenerateResponse
from app.services.workspace_service import WorkspaceService

router = APIRouter(prefix="/api/workspace", tags=["workspace"])


@router.post("/generate", response_model=WorkspaceGenerateResponse)
async def generate_workspace_intelligence(request: WorkspaceGenerateRequest, service: WorkspaceService = Depends(get_workspace_service)) -> WorkspaceGenerateResponse:
    return await service.generate(request)
