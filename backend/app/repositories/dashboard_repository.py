from app.schemas.dashboard import ActionTask, DailyBriefing, DashboardResponse, KpiMetric


class DashboardRepository:
    def get_dashboard(self) -> DashboardResponse:
        return DashboardResponse(
            briefing=DailyBriefing(
                title="Today's Briefing",
                items=[
                    {"id": "react-adoption", "text": "React adoption is accelerating across AI-native product teams."},
                    {"id": "openai-capabilities", "text": "OpenAI released new developer capabilities worth tracking for builders."},
                    {"id": "ai-hiring", "text": "AI Engineering hiring continues to grow for full-stack professionals."},
                ],
                best_posting_window="10:30 AM – 12:00 PM",
                recommended_focus="Create one LinkedIn post about AI Engineering.",
            ),
            action_tasks=[
                ActionTask(id="publish-linkedin", title="Publish LinkedIn Post", description="Turn the AI Engineering focus into a concise professional insight.", priority="High"),
                ActionTask(id="review-trend", title="Review AI Trend", description="Validate the strongest AI trend before generating content.", priority="Medium"),
                ActionTask(id="generate-blog", title="Generate Blog Draft", description="Outline a long-form article for the weekly growth library.", priority="Medium"),
                ActionTask(id="schedule-post", title="Schedule Tomorrow's Post", description="Reserve a publishing slot based on the next best window.", priority="Low"),
            ],
            kpis=[
                KpiMetric(id="posts-this-week", label="Posts This Week", value="3 / 5", helper="Two posts remaining"),
                KpiMetric(id="engagement", label="Engagement", value="+18%", helper="vs. last week"),
                KpiMetric(id="followers", label="Followers", value="+42", helper="net audience growth"),
                KpiMetric(id="consistency", label="Consistency", value="84%", helper="publishing rhythm"),
            ],
        )
