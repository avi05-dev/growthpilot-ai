# Knowledge Intelligence Engine

## Architecture

The Knowledge Intelligence Engine transforms stored Knowledge Items into explainable intelligence. It is intentionally domain-independent and receives domain-specific configuration from the Domain Registry.

```text
Knowledge Item
  ↓
Validation
  ↓
Normalization
  ↓
Component Scores
  ↓
Overall Intelligence Score
  ↓
Priority
  ↓
Persist
  ↓
Completed
```

## Pipeline

`KnowledgeIntelligencePipeline` processes every item with `Pending` status. For each item it:

1. Marks the item as `Processing`.
2. Validates the domain through `DomainRegistry`.
3. Invokes `IntelligenceEngine` for pure score calculation.
4. Persists component scores, overall score, priority, status, and timestamp through the repository-backed service.
5. Marks failures as `Failed` and continues processing remaining items.

## Scoring

Each component score returns `0.0` through `100.0` and never mutates database state.

- **Freshness** evaluates how recently the item was published.
- **Authority** evaluates source trust from domain configuration.
- **Relevance** evaluates keyword alignment from domain configuration.
- **Momentum** evaluates category momentum from domain configuration.
- **Confidence** evaluates completeness of title, summary, source, URL, and publish date.

The overall Intelligence Score uses configurable weights:

- Freshness: 25%
- Relevance: 25%
- Authority: 20%
- Momentum: 20%
- Confidence: 10%

## Priority

Priority thresholds are configurable per domain. The initial defaults are:

- `Critical`: 85+
- `High`: 70+
- `Medium`: 45+
- `Low`: 0+

## APIs

- `POST /api/intelligence/process` processes all pending knowledge items.
- `GET /api/intelligence/health` reports engine status and supported domains.
- `GET /api/knowledge` includes `component_scores`, `overall_score`, `priority`, `processing_status`, and `processed_at`.

## Future Extension

Future milestones can move domain configuration to YAML or JSON, add new domains, introduce recommendation generation, and connect scheduled background workers. GPS-0004B intentionally does not implement LLM generation, recommendations, publishing, RSS, GitHub, Reddit, authentication, or scheduling.
