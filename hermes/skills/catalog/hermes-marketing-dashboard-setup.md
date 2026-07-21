---
title: Hermes Marketing Dashboard — Marketing Ops Control Center for AI Agent Teams
description: Open-source marketing operations dashboard with CRM, outreach, content ops, and analytics. Next.js + OpenClaw + SQLite. 966+ installs.
---

# Hermes Marketing Dashboard — Setup Guide

**Source:** [aradotso/marketing-skills](https://skills.sh/aradotso/marketing-skills/hermes-marketing-dashboard) (966+ installs)
**Category:** Growth Operations / Marketing
**Quality Tier:** 🟡 Beta

Open-source marketing operations control center designed for AI agent teams. Provides CRM, outreach sequencing, content operations, analytics, and automation workflows in a single Next.js application powered by OpenClaw integration and local SQLite storage.

---

## Installation

### Prerequisites

- Node.js 18+
- pnpm (required) — install with `npm install -g pnpm` or `corepack enable`
- OpenClaw CLI (optional but recommended for agent integration)

### Quick Start

```bash
git clone https://github.com/builderz-labs/marketing-dashboard.git
cd marketing-dashboard
pnpm install
pnpm env:bootstrap
pnpm dev
```

The application starts at `http://localhost:3000`.

---

## Configuration

### Required Environment Variables

Create a `.env.local` file:

```bash
# Authentication (required)
AUTH_USER=admin
AUTH_PASS=your-secure-password-min-10-chars
API_KEY=your-api-key-for-programmatic-access

# Cookie security (false for HTTP local, true for HTTPS production)
AUTH_COOKIE_SECURE=false

# Database (auto-created in ./state)
DATABASE_URL=./state/hermes.db
```

### OpenClaw Integration

For AI agent integration with OpenClaw:

```bash
# OpenClaw home directory
HERMES_OPENCLAW_HOME=/path/to/openclaw

# Default instance name
HERMES_DEFAULT_INSTANCE=main

# Multi-instance support (optional JSON array)
HERMES_OPENCLAW_INSTANCES='[{"name":"prod","path":"/openclaw/prod"},{"name":"dev","path":"/openclaw/dev"}]'
```

### Security Configuration

```bash
# Host access lock (default: local-only)
HERMES_HOST_LOCK=local  # or 'off' or 'host1,host2'

# Writeback protection (keep false unless explicitly needed)
HERMES_ALLOW_POLICY_WRITE=false
HERMES_ALLOW_CRON_WRITE=false
HERMES_ALLOW_WORKSPACE_WRITE=false
```

### Optional Analytics Integration

```bash
# Plausible Analytics
NEXT_PUBLIC_PLAUSIBLE_DOMAIN=yourdomain.com
PLAUSIBLE_API_KEY=your-plausible-api-key

# Google Analytics 4
NEXT_PUBLIC_GA4_ID=G-XXXXXXXXXX
```

---

## Key Commands

```bash
# Development
pnpm dev              # Start development server
pnpm build            # Build for production
pnpm start            # Start production server

# Quality
pnpm typecheck        # Type checking
pnpm lint             # Linting
pnpm test             # Run tests
pnpm test:e2e         # Run end-to-end tests

# Database
pnpm env:bootstrap    # Bootstrap environment and database
pnpm db:reset         # Reset database (destructive)
```

---

## Verification

```bash
# Clone and start
git clone https://github.com/builderz-labs/marketing-dashboard.git
cd marketing-dashboard
pnpm install
pnpm env:bootstrap
pnpm dev

# Verify at http://localhost:3000
curl -s http://localhost:3000 | head -5
```

---

## Notes

- **Self-hosted** with local SQLite — no cloud dependency
- **OpenClaw-native** — designed to integrate with OpenClaw agent infrastructure
- **Read-only by default** — writeback protection prevents accidental mutations
- From the [ara.so](https://ara.so) Marketing Skills collection
