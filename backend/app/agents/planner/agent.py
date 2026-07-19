import logging
from time import perf_counter

from app.agents.common.config import load_domain_profile, load_workflow
from app.agents.common.types import AgentState

logger = logging.getLogger(__name__)


class PlannerAgent:
    name = "planner"

    def __init__(self, workflow_name: str = "generate_intelligence") -> None:
        self.workflow_name = workflow_name

    async def execute(self, state: AgentState) -> AgentState:
        started = perf_counter()
        request = state["request"]
        workflow = load_workflow(self.workflow_name)
        profile = load_domain_profile(request.domain)
        elapsed_ms = (perf_counter() - started) * 1000
        logger.info(
            "agent_execution",
            extra={
                "agent_name": self.name,
                "execution_time_ms": elapsed_ms,
                "cache_hit": False,
                "search_provider": None,
                "llm_provider": None,
                "token_usage": {},
                "latency_ms": elapsed_ms,
            },
        )
        return {**state, "workflow_name": workflow.name, "workflow_steps": workflow.steps, "domain_profile": profile}
