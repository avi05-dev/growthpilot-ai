from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from app.agents.common.types import DomainProfile, WorkflowDefinition

CONFIG_ROOT = Path(__file__).resolve().parents[3] / "config"


@lru_cache
def load_domain_profile(domain: str) -> DomainProfile:
    path = CONFIG_ROOT / "domains" / f"{domain}.yaml"
    if not path.exists():
        raise ValueError(f"Domain profile not found: {domain}")
    data: dict[str, Any] = yaml.safe_load(path.read_text())
    return DomainProfile.model_validate(data)


@lru_cache
def load_workflow(name: str) -> WorkflowDefinition:
    path = CONFIG_ROOT / "workflows" / f"{name}.yaml"
    if not path.exists():
        raise ValueError(f"Workflow not found: {name}")
    data: dict[str, Any] = yaml.safe_load(path.read_text())
    return WorkflowDefinition.model_validate(data)
