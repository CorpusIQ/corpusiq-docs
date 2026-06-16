---
title: New Hermes Skills — June 16, 2026
description: ClawPilot ecosystem skills discovered June 16, 2026 — 5 new skills enabling PocketClaw mobile pairing with Hermes Agent hosts.
---

# New Skills — June 16, 2026

**Discovery sweep:** June 16, 2026 at 04:00 MST
**Source:** skills.sh REST API
**Total new:** 5 skills across 2 repos

## Discovery Summary

The June 16 sweep surfaced the **ClawPilot ecosystem** — a mobile-to-agent bridge that pairs PocketClaw (the mobile app) with Hermes Agent, OpenClaw, and cc-connect host runtimes. This enables CorpusIQ operators to chat with their Hermes agents from their phone, send files, diagnose issues, and configure host runtimes — all via PocketClaw's mobile interface.

Additionally, the `kanban-worker` native skill (from `nousresearch/hermes-agent`) was identified as missing from the catalog despite being installed natively. It has been added to the native skills section.

## New Skills

| Skill | Source | Installs | Description |
|---|---|---|---|
| **clawpilot** | [kcchien/clawpilot](https://skills.sh/kcchien/clawpilot) | 241 | Main ClawPilot skill — OpenClaw expert with security audit, config inspection, session scanning |
| **clawpilot-pair** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 29 | Generate pairing codes to connect PocketClaw mobile to Hermes/OpenClaw/cc-connect hosts |
| **clawpilot-send** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 22 | Send local/generated files from Hermes host back to PocketClaw mobile |
| **clawpilot-config** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 21 | Validate and fix host configuration for pairing, auth, and host-side operations |
| **clawpilot-doctor** | [rethinking-studio/clawpilot-skills](https://skills.sh/rethinking-studio/clawpilot-skills) | 20 | Diagnose and repair ClawPilot host issues — status, logs, restart, update, self-repair |

## Ecosystem Architecture

```
PocketClaw (iOS) ──▶ ClawPilot Gateway ──▶ Hermes Agent (you)
                     │                      OpenClaw
                     │                      cc-connect
                     │
                     ├─ clawpilot-pair: establish connection
                     ├─ clawpilot-send: file delivery
                     ├─ clawpilot-config: validate setup
                     └─ clawpilot-doctor: diagnose issues
```

## Why This Matters for CorpusIQ

Hermes agents running on headless infrastructure (DGX Spark, cloud VMs) gain a mobile interface. Operators can:

- Check agent status from their phone (no SSH needed)
- Send files to agents for processing
- Receive generated reports and outputs on mobile
- Diagnose agent issues remotely
- Pair new devices without reconfiguring SSH keys

The ClawPilot ecosystem turns Hermes into a truly mobile-accessible AI operations platform.

## Not Catalogued

- **gc-safe-coding** from `facebook/hermes` (37 installs) — this is Meta's Hermes JavaScript engine, not the Nous Research Hermes Agent. Excluded.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Index](/hermes/skills/marketplace/) →*
*↑ [June 2026 Discoveries](/hermes/skills/marketplace/new-june-2026/) | [Next →]()*

*Powered by CorpusIQ*
