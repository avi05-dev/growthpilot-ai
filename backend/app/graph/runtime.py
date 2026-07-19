from typing import Protocol

from langgraph.graph import END, StateGraph

from app.agents.common.config import load_workflow
from app.agents.common.types import AgentRequest, AgentState, WorkspaceIntelligence


class RunnableAgent(Protocol):
    name: str

    async def execute(self, state: AgentState) -> AgentState:
        raise NotImplementedError


class LangGraphRuntime:
    def __init__(self, *, workflow_name: str, agents: dict[str, RunnableAgent]) -> None:
        workflow_definition = load_workflow(workflow_name)
        workflow = StateGraph(AgentState)
        for step in workflow_definition.steps:
            if step not in agents:
                raise ValueError(f"Workflow step has no registered agent: {step}")
            workflow.add_node(step, agents[step].execute)
        workflow.set_entry_point(workflow_definition.steps[0])
        for current_step, next_step in zip(workflow_definition.steps, workflow_definition.steps[1:]):
            workflow.add_edge(current_step, next_step)
        workflow.add_edge(workflow_definition.steps[-1], END)
        self.graph = workflow.compile()

    async def generate(self, request: AgentRequest) -> WorkspaceIntelligence:
        final_state = await self.graph.ainvoke({"request": request})
        return final_state["intelligence"]
