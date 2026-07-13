# GrowthPilot AI

GrowthPilot AI is an AI-powered growth command center for monitoring acquisition, activation, and revenue signals. Version `0.2.0` establishes the AI Workspace foundation with React, TypeScript, Vite, React Router, and Material UI.

## Features

- Premium AI Workspace that answers: "What should I do today to grow?"
- Service-backed mock dashboard data shaped like a future API contract.
- Reusable TrendCard, KpiCard, DashboardCard, SectionHeader, PriorityChip, and ActionItem components.
- Responsive dashboard shell with desktop sidebar and mobile drawer navigation.
- Loading, empty, and error states prepared for future backend APIs.

## Tech Stack

- React + TypeScript
- Vite
- Material UI + Emotion
- React Router
- ESLint

## Getting Started

### Prerequisites

- Node.js 20 or newer
- npm 10 or newer

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

### Production Build

```bash
npm run build
```

### Linting

```bash
npm run lint
```

## Project Structure

```text
src/
  app/          Application composition
  features/     Feature-level pages and modules
    dashboard/
      components/  Reusable dashboard UI primitives
      data/        Mock dashboard data
      services/    Future API-shaped mock services
      types/       Feature TypeScript contracts
  layouts/      Shared app shells and layout components
  routes/       Route declarations
  theme/        Material UI theme configuration
```

## Release Notes

See [CHANGELOG.md](./CHANGELOG.md) for release history.
