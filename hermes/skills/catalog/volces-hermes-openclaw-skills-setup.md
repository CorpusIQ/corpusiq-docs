---
title: Volces Hermes & OpenClaw Skills — ByteDance Registry Cluster Setup Guide
description: "Install and use the Hermes/OpenClaw skill cluster from skills.volces.com (ByteDance Volces registry mirror): hermes-installer, openclaw-reference, openclaw-plugin-workbench, hermes-memory-bridge, and 5 more."
---

# Volces Hermes & OpenClaw Skills — Setup Guide

**Source:** skills.volces.com registry (mirrored on skills.sh)
**Category:** Registry / Platform Integrations
**First Seen:** Mixed — cluster surfaced in the Aug 12, 2026 sweep
**Security:** Low install counts; treat as Community tier

ByteDance's Volces platform mirrors agent skills into the skills.sh ecosystem. Nine Hermes/OpenClaw-relevant skills surfaced in the August 12 sweep, including installer and memory tooling not published elsewhere. Detail pages 404 on skills.sh because the skills are indexed from the Volces registry rather than GitHub repos.

---

## The Nine Skills

| Skill | Installs | Purpose |
|---|---|---|
| hermes-installer | 6 | One-shot Hermes installation helper |
| openclaw-onebot | 3 | OneBot protocol bridge for OpenClaw |
| openclaw-reference | 3 | OpenClaw reference documentation skill |
| openclaw-plugin-workbench | 2 | Plugin development workbench |
| openclaw-profanity | 2 | Content filtering for OpenClaw |
| hermes-memory-bridge | 2 | Memory provider bridge for Hermes |
| clawpilot-advisor | 1 | ClawPilot configuration advisor |
| openclaw-logfire | 1 | Logfire observability integration |
| openclaw-tavern | 1 | Tavern-style roleplay UI integration |

Mirror note: `openclaw-profanity` also appears under `smithery.ai/openclaw-profanity`, and `hermes-memory-bridge` under `baoyu0/skills`. Prefer the Volces listing for installation.

---

## Installation

```bash
# Via skills.sh (registry mirror)
npx skills add skills.volces.com/hermes-installer --skill hermes-installer
npx skills add skills.volces.com/hermes-memory-bridge --skill hermes-memory-bridge
npx skills add skills.volces.com/openclaw-reference --skill openclaw-reference

# Or via the Volces platform directly (volces.com skills marketplace)
```

When skills.sh detail pages 404, fetch the skill content from the Volces registry UI and install manually into `~/.hermes/skills/<skill-name>/`.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For skills.sh installs |
| Volces account | For the native Volces registry UI |
| OpenClaw runtime | For onebot, logfire, tavern, and profanity skills |
| Hermes Agent | For hermes-installer and hermes-memory-bridge |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Fresh-node provisioning** | `hermes-installer` as a reference for one-shot Hermes setup scripts |
| **Memory bridging** | `hermes-memory-bridge` pattern for wiring memory providers into Hermes |
| **Observability** | `openclaw-logfire` for OpenClaw deployments where Logfire is the telemetry backend |
| **Plugin development** | `openclaw-plugin-workbench` as scaffolding reference for plugin authors |

---

## Limitations / Verification

- Install counts are single-digit — all nine skills are Community tier, unvetted at scale
- skills.sh detail pages 404; content must be reviewed via the Volces registry before trusting
- Some skills are mirrors of GitHub-hosted originals — verify the canonical source before use
- Verify: `npx skills list | grep -i volces` shows installed entries; otherwise check the Volces registry UI

---

## Related

- [Discovery Page — Aug 12 OpenClaw Ecosystem Sweep](/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
