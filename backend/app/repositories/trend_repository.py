from app.schemas.trends import TrendSummary, TrendsResponse


class TrendRepository:
    def list_trends(self) -> TrendsResponse:
        return TrendsResponse(
            trends=[
                TrendSummary(id="gpt-models", category="AI", title="GPT Models", description="Developers are comparing model quality, cost, and latency for production AI workflows.", score=94, sources=["GitHub", "Hacker News"]),
                TrendSummary(id="ai-agents", category="AI", title="AI Agents", description="Agentic workflows are moving from demos into internal productivity systems.", score=91, sources=["GitHub", "Reddit"]),
                TrendSummary(id="open-source-llms", category="AI", title="Open Source LLMs", description="Open models are gaining traction for private, cost-aware experimentation.", score=86, sources=["Hacker News", "Dev.to"]),
                TrendSummary(id="react", category="Development", title="React", description="React remains a durable signal for frontend roles and AI application interfaces.", score=88, sources=["GitHub", "Dev.to"]),
                TrendSummary(id="typescript", category="Development", title="TypeScript", description="Strict TypeScript is increasingly expected in professional-grade AI products.", score=85, sources=["GitHub", "Reddit"]),
                TrendSummary(id="kubernetes", category="Development", title="Kubernetes", description="Platform teams continue to value Kubernetes fluency for scalable services.", score=76, sources=["Hacker News", "Dev.to"]),
                TrendSummary(id="engineering-leadership", category="Career", title="Engineering Leadership", description="Technical leadership content is resonating as teams adapt to AI-assisted delivery.", score=82, sources=["Reddit", "Dev.to"]),
                TrendSummary(id="remote-hiring", category="Career", title="Remote Hiring", description="Remote-first roles remain competitive, with AI fluency becoming a differentiator.", score=79, sources=["Reddit", "Hacker News"]),
                TrendSummary(id="interview-preparation", category="Career", title="Interview Preparation", description="Candidates are practicing system design through AI product case studies.", score=74, sources=["Dev.to", "Reddit"]),
            ]
        )
