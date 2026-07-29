---
title: "July 28, 2026 — Hermes Skills Sweep: Dogfood QA, History Ingest, Imports, Marketing Dashboard, Skill Vetter, OpenClaw Backup (6 new skills, 34.4K+ installs)"
description: "6 new Hermes-relevant skills discovered: Dogfood (4.9K), Skill Vetter (20.6K), OpenClaw Backup (3.1K), Hermes History Ingest (2.1K), Hermes Imports (2.7K), Hermes Marketing Dashboard (970). Combined 34.4K+ installs across 6 sources."
---

# July 28, 2026 — Hermes Skills Sweep

**6 new skills discovered — 34.4K+ combined installs.** This sweep focuses on Hermes-specific and OpenClaw ecosystem skills from the skills.sh marketplace. Discovery via `npx skills find` across 18 search terms.

## New Skills at a Glance

| # | Skill | Source | Installs | Category | Setup Guide |
|---|-------|--------|:--------:|----------|:-----------:|
| 1 | `dogfood` | nousresearch/hermes-agent | 4.9K | QA / Testing | ✅ |
| 2 | `skill-vetter` | useai-pro/openclaw-skills-security | 20.6K | Security | ✅ |
| 3 | `openclaw-backup` | theagentservice/skills | 3.1K | Backup / DevOps | ✅ |
| 4 | `hermes-imports` | affaan-m/everything-claude-code | 2.7K | Workflow / DevOps | ✅ |
| 5 | `hermes-history-ingest` | ar9av/obsidian-wiki | 2.1K | Memory / Knowledge | ✅ |
| 6 | `hermes-marketing-dashboard` | aradotso/marketing-skills | 970 | Marketing / Ops | ✅ |

## Category Breakdown

### Hermes Official (nousresearch/hermes-agent)

| Skill | Installs | Description |
|-------|:--------:|-------------|
| `dogfood` | 4.9K | Systematic exploratory QA testing of web apps using browser tools. 5-phase workflow: Plan → Explore → Interact → Edge Cases → Report. Produces structured bug reports with screenshots. |

### OpenClaw Ecosystem

| Skill | Source | Installs | Description |
|-------|--------|:--------:|-------------|
| `skill-vetter` | useai-pro/openclaw-skills-security | 20.6K | Security-first pre-install vetting for OpenClaw skills. Structured red-flag checklist for permissions, patterns, and suspicious instructions. 97% trust score. |
| `openclaw-backup` | theagentservice/skills | 3.1K | Encrypted backup/restore for OpenClaw workspace files (SOUL.md, MEMORY.md, IDENTITY.md, AGENTS.md). AES-256-CBC via openssl + soul-upload.com API. |

### Community Hermes Skills

| Skill | Source | Installs | Description |
|-------|--------|:--------:|-------------|
| `hermes-imports` | affaan-m/everything-claude-code | 2.7K | Convert local Hermes workflows into sanitized ECC skills. Strips private paths, credentials, and account names. Release-pack artifact generation. |
| `hermes-history-ingest` | ar9av/obsidian-wiki | 2.1K | Ingest Hermes agent history into Obsidian wiki. Mines past sessions for knowledge, extracts insights from conversations, imports ~/.hermes memories. |
| `hermes-marketing-dashboard` | aradotso/marketing-skills | 970 | Open-source marketing ops control center for AI agent teams. CRM, outreach, content ops, analytics powered by OpenClaw + SQLite. Next.js application. |

## Setup Guides Created

1. **[Dogfood Setup Guide](/hermes/skills/catalog/dogfood-setup/)** — Systematic QA testing with browser tools. 5-phase workflow for finding bugs and producing structured reports.
2. **[Skill Vetter Setup Guide](/hermes/skills/catalog/skill-vetter-setup/)** — Pre-install security vetting for OpenClaw skills. Red-flag checklist for safe skill adoption.
3. **[OpenClaw Backup Setup Guide](/hermes/skills/catalog/openclaw-backup-setup/)** — Encrypted workspace backup with AES-256-CBC. Auto-generated passwords, soul-upload.com API.
4. **[Hermes Imports Setup Guide](/hermes/skills/catalog/hermes-imports-setup/)** — Sanitize and export Hermes workflows as reusable ECC skills.
5. **[Hermes History Ingest Setup Guide](/hermes/skills/catalog/hermes-history-ingest-setup/)** — Mine Hermes session history into Obsidian knowledge base.
6. **[Hermes Marketing Dashboard Setup Guide](/hermes/skills/catalog/hermes-marketing-dashboard-setup/)** — Full-stack marketing control center with CRM, outreach, and analytics.

## Quick Install

```bash
# Official Hermes — QA testing
npx skills add nousresearch/hermes-agent@dogfood

# Security vetting for any skill install
npx skills add useai-pro/openclaw-skills-security@skill-vetter

# Encrypted workspace backup
npx skills add theagentservice/skills@openclaw-backup

# Sanitize and export Hermes workflows
npx skills add affaan-m/everything-claude-code@hermes-imports

# Mine Hermes history into Obsidian
npx skills add ar9av/obsidian-wiki@hermes-history-ingest

# Marketing dashboard for agent teams
npx skills add aradotso/marketing-skills@hermes-marketing-dashboard
```

## Why This Matters for Hermes

These six skills fill critical gaps in the Hermes ecosystem. `dogfood` brings systematic QA testing — essential as Hermes agents increasingly drive production workflows. `skill-vetter` addresses the growing security surface area of the skills marketplace at 20.6K installs. `openclaw-backup` solves agent state persistence with encryption. The three community Hermes skills (`hermes-imports`, `hermes-history-ingest`, `hermes-marketing-dashboard`) demonstrate the maturing operator toolchain around Hermes — workflow export, knowledge mining, and marketing ops.
