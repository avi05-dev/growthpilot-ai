# GrowthPilot AI

GrowthPilot AI is an AI-powered growth command center for monitoring acquisition, activation, and revenue signals. Version `0.1.0` establishes the frontend foundation with React, TypeScript, Vite, React Router, and Material UI.

## Features

- Responsive dashboard shell with desktop sidebar and mobile drawer navigation.
- Material UI theme with GrowthPilot brand colors, typography, and component defaults.
- Top navigation with search, notifications, and user profile affordances.
- Routed placeholder pages for Dashboard, Campaigns, Audiences, and Insights.
- Placeholder analytics cards, trend modules, and recommended growth plays ready for data integration.

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
  layouts/      Shared app shells and layout components
  routes/       Route declarations
  theme/        Material UI theme configuration
```

## Release Notes

See [CHANGELOG.md](./CHANGELOG.md) for release history.
