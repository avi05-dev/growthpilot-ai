# Changelog

All notable changes to GrowthPilot AI will be documented in this file.

## [0.4.0] - 2026-07-13

### Added

#### GPS-0004B - Knowledge Intelligence Engine

- Added the reusable, domain-independent Knowledge Intelligence Engine module for component scoring, weighted Intelligence Score calculation, priority classification, and processing schemas.
- Added the initial Technology domain registry configuration for authority sources, relevance keywords, momentum categories, and configurable priority thresholds.
- Added intelligence persistence fields to knowledge items, including component scores, overall score, priority, processing status, and processed timestamp.
- Added Alembic migration `0002_add_intelligence_fields` for the new intelligence columns.
- Added repository-backed intelligence service and orchestration pipeline for processing pending knowledge items.
- Added `POST /api/intelligence/process` and `GET /api/intelligence/health` endpoints.
- Added intelligence metadata to knowledge API responses.
- Added dashboard display for overall Intelligence Score, priority, processing status, and expandable component scores.
- Added Knowledge Intelligence Engine documentation and GPS-0004B review notes.
- Added backend tests for scoring, ranking, pipeline, service, repository, and API coverage.

#### GPS-0004A - PostgreSQL Persistence

- Added PostgreSQL persistence configuration through `DATABASE_URL`.
- Added SQLAlchemy models for domains, knowledge items, and recommendations.
- Added Alembic migration support for the persistence tables and indexes.
- Added repository and service layers for database-backed domains, knowledge, recommendations, dashboard, and trends.
- Added database-backed API endpoints for domains, knowledge, and recommendations.
- Added a seed script for the Technology domain, 10 knowledge items, and 10 recommendations.
- Added backend tests for repositories, services, and API endpoints with an in-memory database override.
- Added database documentation and GPS-0004A implementation review notes.

### Changed

- Replaced remaining backend mock repository usage with database-backed services.
- Updated frontend API typing to support database-backed dashboard recommendation and trend data.

## [0.3.0] - 2026-07-13

### Added

- Converted the project into a frontend/backend monorepo.
- Added a FastAPI backend with API, service, repository, schema, middleware, dependency, and test layers.
- Added REST endpoints for health, version, dashboard, trends, and recommendations.
- Added Axios and TanStack Query frontend API integration.
- Added Docker support for frontend and backend.
- Added GitHub Actions CI for frontend build and backend tests.
- Added backend, API, architecture, and development setup documentation.

### Changed

- Moved mock dashboard data out of the frontend and into backend repositories.
- Updated the frontend to consume backend APIs exclusively.

## [0.2.0] - 2026-07-13

### Added

- Replaced the generic dashboard with a premium AI Workspace experience centered on daily professional growth decisions.
- Added a reusable dashboard component system including TrendCard, KpiCard, DashboardCard, SectionHeader, PriorityChip, and ActionItem.
- Added a mock dashboard service layer that returns Promise-based data shaped like a future API contract.
- Added loading, empty, and error states for future API readiness.
- Expanded the design foundation with reusable tokens for colors, radii, shadows, spacing, and priority status colors.

### Changed

- Updated the dashboard shell navigation and visual language to align with the AI Growth Operating System direction.

## [0.1.0] - 2026-07-12

### Added

- Initialized GrowthPilot AI as a React, TypeScript, Vite, and Material UI application.
- Added a production-oriented project structure for app composition, routes, layouts, features, and theme configuration.
- Implemented a responsive dashboard shell with sidebar navigation, mobile drawer behavior, top navigation, and routed placeholder pages.
- Added placeholder analytics cards, revenue momentum progress indicators, and AI growth-play recommendations.
- Added README documentation and release notes.
