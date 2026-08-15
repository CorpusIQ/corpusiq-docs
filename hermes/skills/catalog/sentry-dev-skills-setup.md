---
title: Sentry Dev Skill — Official Sentry CLI Setup Guide for Hermes Agents
description: "sentry/dev — the official Sentry skill: sentry-cli (127.3K installs). Error monitoring, release management, sourcemap uploads, event querying, and project administration from the agent via the Sentry CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sentry-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "sentry", "error monitoring", "observability"]
---

# Sentry Dev Skill — Setup Guide

**Source:** [sentry/dev](https://skills.sh/sentry/dev)
**GitHub:** [sentry/dev](https://github.com/sentry/dev)
**Skills:** 1 skill (`sentry-cli`) · 127.3K total installs
**Category:** Error Monitoring & Release Management
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟢 Production (official Sentry)

The official Sentry skill teaches an agent to operate the Sentry CLI: configure auth tokens, manage releases and deploys, upload sourcemaps and debug symbols, query issues and events, and administer projects and teams. At 127.3K installs it is one of the highest-installed single skills on the marketplace, and it was rising on the hot leaderboard (+94 installs in the sweep hour). For any team already running Sentry for error monitoring, this skill turns the agent into a release engineer that can wire deploys into Sentry without manual CLI work.

---

## Installation

```bash
npx skills add sentry/dev
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Sentry account + org** | A Sentry organization and project to manage |
| **Sentry auth token** | `sentry auth login` or an org auth token with the needed scopes |
| **Node.js + npx** | For the `skills add` installer |

## What It Provides

| Capability | Notes |
|---|---|
| Auth & config | Token setup, org/project context selection |
| Releases & deploys | `sentry-cli releases new/finalize/set-commits`, deploys tracking |
| Sourcemaps | Upload sourcemaps for JS/Flutter/native builds, debug symbols |
| Issue triage | List/query issues, assign, resolve, event details |
| Project admin | Create/configure projects, teams, keys (DSN) |

## Quick Start

1. `npx skills add sentry/dev`
2. `sentry-cli login` and select the org/project
3. Ask: "create a release for commit abc123 and upload sourcemaps from dist/"
4. "Show me unresolved errors from the last 24 hours, grouped by type"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **mcp2.corpusiq.io monitoring** | Wire server deploys to Sentry releases; triage error spikes after pushes |
| **Frontend releases** | Sourcemap uploads for www.corpusiq.io deploys so stack traces resolve |
| **Incident triage** | Query recent issues during incidents instead of clicking through the Sentry UI |
| **Release hygiene** | Associate commits with releases for regression blame |

## Limitations / Verification

- Requires Sentry account access; the CLI needs an auth token with project scopes
- Read-mostly triage and release operations — admin actions still need org permissions

```bash
sentry-cli info    # verify auth + org context
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Chrome DevTools MCP Skills Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup/) — console/error inspection during debugging

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
