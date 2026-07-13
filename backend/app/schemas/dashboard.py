from pydantic import BaseModel, Field


class BriefingItem(BaseModel):
    id: str
    text: str


class DailyBriefing(BaseModel):
    title: str
    items: list[BriefingItem]
    best_posting_window: str = Field(serialization_alias="bestPostingWindow")
    recommended_focus: str = Field(serialization_alias="recommendedFocus")


class ActionTask(BaseModel):
    id: str
    title: str
    description: str
    priority: str


class KpiMetric(BaseModel):
    id: str
    label: str
    value: str
    helper: str


class DashboardResponse(BaseModel):
    briefing: DailyBriefing
    action_tasks: list[ActionTask] = Field(serialization_alias="actionTasks")
    kpis: list[KpiMetric]
