---
title: Hermes Marketing Dashboard — Setup Guide for Hermes Agents
description: Open-source marketing operations control center for AI agent teams. CRM, outreach sequencing, content ops, analytics powered by OpenClaw + SQLite. 970+ installs.
---

# Hermes Marketing Dashboard — Setup Guide

**Source:** [aradotso/marketing-skills](https://github.com/builderz-labs/marketing-dashboard) (Community)
**Skill:** `hermes-marketing-dashboard` · **Installs:** 970+ · **Category:** Marketing / Operations
**Platform:** Linux, macOS, Windows

Hermes Marketing Dashboard is an open-source marketing operations control center designed for AI agent teams. It provides CRM, outreach sequencing, content operations, analytics, and automation workflows in a single Next.js application powered by OpenClaw integration and local SQLite storage.

## Installation

```bash
npx skills add aradotso/marketing-skills@hermes-marketing-dashboard
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Node.js 18+ | Runtime for Next.js application |
| pnpm | Package manager — `npm install -g pnpm` or `corepack enable` |
| OpenClaw CLI | Optional but recommended for agent integration |

## Quick Start

```bash
git clone https://github.com/builderz-labs/marketing-dashboard.git
cd marketing-dashboard
pnpm install
pnpm env:bootstrap
pnpm dev
```

The application starts at `http://localhost:3000`.

## Configuration

### Required Environment Variables

Create `.env.local`:

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

```bash
# OpenClaw home directory
HERMES_OPENCLAW_HOME=/path/to/openclaw

# Default instance name
HERMES_DEFAULT_INSTANCE=main

# Multi-instance support (optional JSON array)
HERMES_OPENCLAW_INSTANCES='[{"name":"prod","path":"/openclaw/prod"},{"name":"dev","path":"/openclaw/dev"}]'
```

## Features

| Module | Description |
|--------|-------------|
| CRM | Contact management, deal pipeline, activity tracking |
| Outreach | Email sequences, campaign management, response tracking |
| Content Ops | Content calendar, asset management, publishing workflow |
| Analytics | Dashboard metrics, campaign performance, ROI tracking |
| Automation | Workflow builder, triggers, agent task delegation |

## Database

Uses SQLite via `./state/hermes.db`. Auto-created on first run. Back up with:

```bash
cp ./state/hermes.db ./state/hermes-backup-$(date +%Y%m%d).db
```

## Verification

After setup:
- `http://localhost:3000` loads the dashboard
- Login with configured `AUTH_USER` / `AUTH_PASS`
- Database file exists at `./state/hermes.db`
- OpenClaw integration shows agent status (if configured)

## Related Skills

- [Hermes Agent Framework](/hermes/skills/catalog/hermes-agent-framework-setup/)
- [OpenClaw Ecosystem (June 26)](/hermes/skills/catalog/openclaw-ecosystem-june26-setup/)
- [Marketing Skills Collection](/hermes/skills/catalog/coreyhaines31-marketing-skills-setup/)
