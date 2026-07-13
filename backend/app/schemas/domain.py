from pydantic import BaseModel, ConfigDict


class DomainRead(BaseModel):
    id: str
    name: str
    display_name: str
    description: str
    is_enabled: bool

    model_config = ConfigDict(from_attributes=True)


class DomainsResponse(BaseModel):
    domains: list[DomainRead]
