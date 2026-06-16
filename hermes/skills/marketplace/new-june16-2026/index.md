---
title: New Skills — June 16, 2026
description: Latest skill discoveries this week — ClawPilot ecosystem (5 skills) for mobile-to-agent bridging, trending skills, and what's coming next. Updated June 16, 2026.
---

# New Skills — June 16, 2026

**Discovery sweep:** June 16, 2026 at 04:00 MST
**Source:** skills.sh REST API
**Total new this week:** 5 skills across 2 repos
**Cumulative marketplace total:** 290+ skills

## What's New This Week

The June 16 sweep surfaced the **ClawPilot ecosystem** — a mobile-to-agent bridge that pairs PocketClaw (the iOS mobile app) with Hermes Agent, OpenClaw, and cc-connect host runtimes. This is the first major mobile-accessible interface for Hermes agents, enabling operators to manage their agents from a phone without SSH access.

| Skill | Source | Installs | Description |
|---|---|---|---|
| **clawpilot** | [kcchien/clawpilot](https://skills.sh/kcchien/clawpilot) | 241 | Main ClawPilot skill — OpenClaw expert with security audit, config inspection, and session scanning capabilities |
| **clawpilot-pair** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 29 | Generate pairing codes to connect PocketClaw mobile app to Hermes/OpenClaw/cc-connect hosts |
| **clawpilot-send** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 22 | Send local or agent-generated files from host machine back to PocketClaw mobile |
| **clawpilot-config** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 21 | Validate and fix host configuration for pairing, authentication, and host-side operations |
| **clawpilot-doctor** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 20 | Diagnose and repair ClawPilot host issues — status checks, log inspection, restart, update, self-repair |

### ClawPilot Ecosystem Architecture

```
PocketClaw (iOS) ──▶ ClawPilot Gateway ──▶ Hermes Agent (your agent)
                     │                      OpenClaw host
                     │                      cc-connect host
                     │
                     ├─ clawpilot-pair: establish secure connection
                     ├─ clawpilot-send: file and report delivery
                     ├─ clawpilot-config: validate setup and fix issues
                     └─ clawpilot-doctor: diagnose and repair problems
```

### Why ClawPilot Matters

Hermes agents typically run on headless infrastructure — cloud VMs, local servers, DGX Spark machines. Access requires SSH or a web dashboard. ClawPilot changes this by providing a mobile-native interface:

- **Check agent status from your phone** — No SSH, no terminal. Open PocketClaw and see what your agents are doing.
- **Send files for processing** — Drop a CSV or document into PocketClaw, it lands on the agent host for processing.
- **Receive generated reports on mobile** — Agents generate reports, analyses, and outputs that appear in your PocketClaw inbox.
- **Diagnose issues remotely** — Agent frozen? Cron not firing? Run `clawpilot-doctor` from your phone to diagnose.
- **Pair new devices without SSH key exchange** — Generate a pairing code, scan it with PocketClaw, connected.

For teams operating multiple Hermes agents across different machines, ClawPilot provides a unified mobile operations center.

## Trending Skills This Week

Beyond the new ClawPilot discoveries, here's what's gaining traction across the marketplace:

| Skill | Trend | Why It's Hot |
|-------|-------|-------------|
| `skill-auditor` (590) | ↑ Rising | Security audit automation for agent skills — teams are taking agent security seriously |
| `neon-postgres` (40.3K) | → Steady | Serverless Postgres remains the go-to state backend for agent systems |
| `hermes-webui-agent` (193) | ↑ Rising | Growing demand for web-based agent dashboards over terminal-only interfaces |
| `rag-implementation` (9.5K) | ↑ Rising | Production RAG patterns are in demand as teams move beyond proof-of-concept |
| `docker-expert` (18.9K) | → Steady | Containerization remains the standard deployment pattern for agent services |

### Install Trends by Category

Marketing skills continue to dominate install counts (1.8M+ for the `marketingskills` pack alone), but infrastructure and security skills are growing fastest week-over-week. The pattern: teams install marketing skills first (immediate value), then layer on security and infrastructure as they scale.

## What Was Considered But Not Added

Not every skill discovered makes it into the marketplace. This week's sweep identified one exclusion:

- **`gc-safe-coding`** from `facebook/hermes` (37 installs) — This is Meta's Hermes JavaScript engine, not the Nous Research Hermes Agent. Different project, different ecosystem. Excluded to avoid confusion.

Inclusion criteria: the skill must be compatible with Nous Research's Hermes Agent runtime, must install cleanly via `npx skills add`, and must not duplicate existing marketplace skills.

## How New Skills Are Discovered

The weekly discovery sweep queries the skills.sh REST API for new skill publications. The process:

1. **API sweep** — Query skills.sh for skills published since the last sweep date
2. **Compatibility check** — Filter out skills for incompatible agent runtimes (Meta Hermes JS engine, non-Hermes platforms)
3. **Installation test** — Install each candidate skill to verify it loads without errors
4. **Categorization** — Place the skill in the appropriate marketplace category
5. **Curation** — Write descriptions, document use cases, and identify ecosystem patterns
6. **Publish** — Add to the catalog and publish this update page

The sweep runs automatically every week. Major ecosystem discoveries (like the ClawPilot suite) get dedicated analysis. Minor additions are batched into weekly roundups.

## Installation Guide

### ClawPilot Skills

```bash
# Install all ClawPilot skills
npx skills add kcchien/clawpilot@clawpilot
npx skills add rethinking-studio/clawpilot-skills@clawpilot-pair
npx skills add rethinking-studio/clawpilot-skills@clawpilot-send
npx skills add rethinking-studio/clawpilot-skills@clawpilot-config
npx skills add rethinking-studio/clawpilot-skills@clawpilot-doctor

# Or install the full ClawPilot pack
npx skills add rethinking-studio/clawpilot-skills
```

### Setup Workflow

After installation, set up the ClawPilot ecosystem:

1. **Configure the host** — Run `clawpilot-config` to validate and fix host configuration
2. **Pair your phone** — Run `clawpilot-pair` to generate a pairing code, scan it with PocketClaw on iOS
3. **Test the connection** — Run `clawpilot-doctor` to verify everything is working
4. **Send a test file** — Use `clawpilot-send` to deliver a test file to your phone

### Prerequisites

- Hermes Agent, OpenClaw, or cc-connect running on the host machine
- PocketClaw iOS app installed on the mobile device
- Host and mobile device on the same network (or configured for remote access)
- The `clawpilot` skill loaded for security auditing

## Catalog Updates This Week

The native skills catalog was also updated this week with:

- **`kanban-worker`** — Added to the catalog (was previously installed but missing from the index). Covers pitfalls, examples, and edge cases for Hermes Kanban workers.
- **`subagent-resilience`** — Added to engineering skills. Checkpoint-based resilience patterns for subagents: save partial results, survive interruptions, and resume gracefully.

## Coming Next

Based on skills.sh publication velocity, upcoming sweeps are expected to surface:

- **More mobile integration skills** — The ClawPilot category is likely to grow with additional platform connectors
- **Agent memory systems** — Several repos are developing skills around persistent agent memory beyond Honcho
- **Multi-modal skills** — Image and audio processing for Hermes agents is an active development area

Have a skill you want added? [Submit it to the marketplace →](/hermes/skills/marketplace/#community-submissions)

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Index](/hermes/skills/marketplace/) →*

*↑ [June 2026 Discoveries](/hermes/skills/marketplace/new-june-2026/) | [June 15, 2026 ← Previous](/hermes/skills/marketplace/new-june15-2026/)*

*Powered by CorpusIQ*
