---
title: Rivet Skills — Real-Time Backend & Agent Infrastructure Setup
description: "rivet-dev/skills — 22 skills, 65.3K installs: sandbox-agent, RivetKit SDK clients (JavaScript, React, Swift, SwiftUI, Rust, TypeScript), multiplayer, cron jobs, AI agent workspaces, per-tenant databases, live cursors, and VPC air-gapped deploys."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rivet-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "realtime", "backend", "multiplayer", "actors", "agent infrastructure"]
---

# Rivet Skills — Setup Guide

**Source:** [rivet-dev/skills](https://skills.sh/rivet-dev/skills)
**GitHub:** [rivet-dev/skills](https://github.com/rivet-dev/skills)
**Skills:** 22 skills · 65.3K total installs
**Category:** Real-Time Backend & Agent Infrastructure
**First Seen:** catalogued August 15, 2026 midday sweep
**Quality Tier:** 🟢 Production (first-party publisher — Rivet, the VC-backed real-time backend company)

Rivet publishes skills for building on its actor-based real-time backend: sandboxed agent execution, multiplayer games, chat rooms, collaborative editors, live cursors, cron jobs, per-tenant databases, and VPC air-gapped deployments, plus RivetKit SDK client guides. Queued at a 10.1K API estimate, the publisher page shows 65.3K across 22 skills — including sandbox-agent at 10.1K alone.

---

## Installation

```bash
npx skills add rivet-dev/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Rivet account** | For deployment targets (rivet.gg) |
| **SDK runtime** | JavaScript, React, Swift, or Rust depending on the client skill |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| sandbox-agent | 10.1K | Sandboxed agent execution environment |
| rivetkit | 7.7K | Core RivetKit toolkit |
| rivetkit-client-javascript | 7.6K | JS SDK client guide |
| rivetkit-client-react | 7.5K | React SDK client guide |
| rivetkit-client-swiftui / -swift | 7.3K each | SwiftUI and Swift client guides |
| multiplayer-game | 7.2K | Multiplayer game architecture |
| cron-jobs | 1.2K | Scheduled jobs on Rivet |
| ai-agent / ai-agent-workspace | 1.2K each | Agent deployment patterns |
| chat-room | 1.2K | Realtime chat reference |
| per-tenant-database | 1.1K | Tenant-isolated data layout |
| collaborative-text-editor / live-cursors | 1.1K each | CRDT-style collaboration references |
| vpc-air-gapped | 1.1K | Air-gapped VPC deployment |
| rivet-actors / rivet-agentos / rivet-workflows | 86 / 85 / 84 | Actor runtime, agent OS, and workflow concepts |

## Quick Start

1. Install: `npx skills add rivet-dev/skills`
2. Load sandbox-agent for agent execution or rivetkit for SDK work
3. Ask: "scaffold a sandboxed AI agent workspace on Rivet"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent sandboxing** | sandbox-agent as a reference for isolated agent execution |
| **Realtime product features** | Multiplayer, chat, and live-cursor patterns for client builds |
| **Cron and agent infrastructure** | cron-jobs and ai-agent-workspace patterns map to our fleet scheduling |
| **Architecture reference** | Actor-model backend patterns from a proven vendor |

## Limitations / Verification

- Multi-skill suite; individual security-audit pages not fetched this sweep
- Requires a Rivet account for deployment skills; conceptual skills are readable standalone
- Long-tail skills (rivetkit-actors at 6 installs) are new and minimally validated

```bash
npx skills add rivet-dev/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
