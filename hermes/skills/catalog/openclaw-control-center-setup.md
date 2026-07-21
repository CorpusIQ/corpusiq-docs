---
title: OpenClaw Control Center — Agent Monitoring Dashboard for OpenClaw
description: Local-first, security-first control center for OpenClaw agents. Visibility dashboard with readonly defaults, token attribution, and collaboration tracing. 4.3K+ installs.
---

# OpenClaw Control Center — Setup Guide

**Source:** [aradotso/trending-skills](https://skills.sh/aradotso/trending-skills/openclaw-control-center) (4,300+ installs)
**Category:** Agent Infrastructure / Monitoring
**Quality Tier:** 🟢 Production

Transforms OpenClaw from a black box into a local, auditable control center. Provides visibility into agent activity, token spend, task execution chains, cross-session collaboration, memory state, and document sources — with security-first defaults that keep all mutations off by default.

---

## Installation

```bash
git clone https://github.com/TianyiDataScience/openclaw-control-center.git
cd openclaw-control-center
npm install
cp .env.example .env
npm run build
npm test
npm run smoke:ui
npm run dev:ui
```

Open:
- English: `http://127.0.0.1:4310/?section=overview&lang=en`
- Chinese: `http://127.0.0.1:4310/?section=overview&lang=zh`

> Use `npm run dev:ui` over `UI_MODE=true npm run dev` — more stable, especially on Windows.

---

## Project Structure

```
openclaw-control-center/
├── control-center/          # All modifications must stay here
│   ├── src/
│   │   ├── runtime/         # Core runtime, connectors, monitors
│   │   └── ui/              # Frontend UI components
│   ├── .env.example
│   └── package.json
├── docs/
│   └── assets/              # Screenshots and docs
├── README.md
└── README.en.md
```

> **Critical constraint**: Only modify files inside `control-center/`. Never modify `~/.openclaw/openclaw.json`.

---

## Environment Configuration

Copy `.env.example` to `.env` and configure:

```env
# Security defaults — do NOT change without understanding implications
READONLY_MODE=true
LOCAL_TOKEN_AUTH_REQUIRED=true
IMPORT_MUTATION_ENABLED=false
IMPORT_MUTATION_DRY_RUN=false
APPROVAL_ACTIONS_ENABLED=false
APPROVAL_ACTIONS_DRY_RUN=true

# Connection
OPENCLAW_GATEWAY_URL=http://127.0.0.1:PORT
OPENCLAW_HOME=~/.openclaw

# UI
PORT=4310
DEFAULT_LANG=en
```

### Security Flag Reference

| Flag | Default | Effect |
|------|---------|--------|
| `READONLY_MODE` | `true` | All state-changing endpoints disabled |
| `LOCAL_TOKEN_AUTH_REQUIRED` | `true` | Import/export and write APIs require local token |
| `IMPORT_MUTATION_ENABLED` | `false` | Import mutations blocked entirely |
| `IMPORT_MUTATION_DRY_RUN` | `false` | Dry-run mode for imports when enabled |
| `APPROVAL_ACTIONS_ENABLED` | `false` | Approval actions hard-disabled |
| `APPROVAL_ACTIONS_DRY_RUN` | `true` | Approval actions run as dry-run when enabled |

---

## Dashboard Sections

| Section | What It Shows |
|---|---|
| **Overview** | System health, pending items, risk signals, operational summary |
| **Usage** | Daily/7d/30d token spend, quota, context pressure |
| **Staff** | Who is actively executing vs. queued |
| **Collaboration** | Parent-child session handoffs, verified cross-session messages |
| **Tasks** | Task board, approvals, execution chains, run evidence |
| **Memory** | Per-agent memory health, searchability, source file editing |
| **Documents** | Shared and agent-core documents from actual source files |
| **Settings** | Connector wiring status, security risk summary, update status |

---

## Key Commands

```bash
# Development
npm run dev:ui          # Start UI server (recommended)
npm run dev             # One-shot monitor run, no HTTP UI

# Build & Test
npm run build           # TypeScript compile
npm test                # Run test suite
npm run smoke:ui        # Smoke test the UI endpoints

# Lint
npm run lint            # ESLint check
```

---

## Verification

```bash
# Start the control center
npm run dev:ui

# Verify health
curl http://127.0.0.1:4310/api/health

# Open in browser
# http://127.0.0.1:4310/?section=overview&lang=en
```

---

## Notes

- **Security-first**: All mutations are disabled by default (`READONLY_MODE=true`)
- **Local-only**: Runs entirely on localhost, no cloud dependency
- **Dual-language**: Full English and Chinese (中文) UI support
- Pairs well with `hermes-labyrinth-observability` for deeper journey-level observability
- From the [ara.so](https://ara.so) Daily 2026 Skills collection
- Repository: [TianyiDataScience/openclaw-control-center](https://github.com/TianyiDataScience/openclaw-control-center)
