# Changelog

All notable changes to GrowthPilot AI will be documented in this file.

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
