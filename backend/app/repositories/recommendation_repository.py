from app.schemas.recommendations import Recommendation, RecommendationsResponse


class RecommendationRepository:
    def list_recommendations(self) -> RecommendationsResponse:
        return RecommendationsResponse(
            recommendations=[
                Recommendation(id="linkedin-react", channel="LinkedIn", topic="React Released", actionLabel="Generate Draft"),
                Recommendation(id="x-openai", channel="X Thread", topic="OpenAI Update", actionLabel="Generate Draft"),
                Recommendation(id="blog-ai-engineering", channel="Blog", topic="State of AI Engineering", actionLabel="Generate Draft"),
            ]
        )
