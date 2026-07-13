from app.repositories.domain_repository import DomainRepository
from app.schemas.domain import DomainRead, DomainsResponse


class DomainService:
    def __init__(self, repository: DomainRepository) -> None:
        self.repository = repository

    def list_domains(self) -> DomainsResponse:
        return DomainsResponse(domains=[DomainRead.model_validate(domain) for domain in self.repository.list_enabled()])
