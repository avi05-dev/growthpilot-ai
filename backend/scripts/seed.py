from datetime import datetime, timezone

from app.db.session import SessionLocal
from app.models.database import Domain, KnowledgeItem, Recommendation

CATEGORIES = ["AI", "Development", "Career"]


def run() -> None:
    db = SessionLocal()
    try:
        if db.query(Domain).filter_by(name="technology").first() is None:
            db.add(Domain(id="technology", name="technology", display_name="Technology", description="Software engineering, AI product, and developer growth signals.", is_enabled=True))
        existing = db.query(KnowledgeItem).filter_by(domain="technology").count()
        if existing == 0:
            items = []
            for index in range(10):
                item = KnowledgeItem(
                    id=f"technology-knowledge-{index + 1}",
                    domain="technology",
                    title=f"Technology Signal {index + 1}",
                    summary=f"Database-backed technology insight {index + 1} for planning useful content.",
                    source=["GitHub", "Hacker News", "Dev.to"][index % 3],
                    category=CATEGORIES[index % 3],
                    url=f"https://example.com/technology/{index + 1}",
                    published_at=datetime(2026, 7, index + 1, tzinfo=timezone.utc),
                    status="published",
                )
                items.append(item)
                db.add(item)
            db.flush()
            for index, item in enumerate(items):
                db.add(Recommendation(id=f"technology-recommendation-{index + 1}", knowledge_item_id=item.id, priority=["High", "Medium", "Low"][index % 3], recommended_action=f"Create a practical post about {item.title}", reason=f"{item.title} has enough signal to support a concise audience insight.", estimated_effort="30 minutes", content_opportunity=f"Turn {item.title} into a short educational content draft."))
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    run()
