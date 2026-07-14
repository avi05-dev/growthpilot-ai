from fastapi import APIRouter, Depends

from app.dependencies.services import get_domain_service
from app.schemas.domain import DomainsResponse
from app.services.domain_service import DomainService

router = APIRouter(prefix="/api", tags=["domains"])


@router.get("/domains", response_model=DomainsResponse)
def list_domains(service: DomainService = Depends(get_domain_service)) -> DomainsResponse:
    return service.list_domains()
