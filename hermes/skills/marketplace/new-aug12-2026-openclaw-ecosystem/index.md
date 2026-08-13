---
title: "August 12, 2026 — OpenClaw/Clawd/Hermes Ecosystem Sweep"
description: "Skills.sh sweep for Aug 12: openclaw/carapace design system (2.3K installs), Volces Hermes skills, OpenClaw Graph additions, official MCP OAuth remote"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "skill marketplace", "skills.sh"]

---

# August 12, 2026 — OpenClaw Ecosystem Sweep

**Date:** August 12, 2026
**New publishers:** 62
**New skills covered:** 78 (77 via API sweep + 1 surfaced on publisher page)
**Combined installs:** 3.8K+ (skills.sh API counts)
**Method:** 29 targeted API queries against skills.sh, cross-referenced against 1,561 docs files (6.9M chars). 388 unique skills surfaced; 122 not in docs; 77 relevant to the Hermes/OpenClaw/Clawd ecosystem after the false-positive filter.

Six weeks after the previous OpenClaw ecosystem sweep (June 30), this pass caught the largest gap: the official OpenClaw design system package (carapace), a ByteDance Volces skills registry mirror with Hermes-specific tooling, new skills from the 311-skill openclaw-graph repo, and an official Hermes Agent skill for MCP OAuth on remote gateways.

---

## 🆕 OpenClaw Carapace — Design System Package (openclaw/carapace)

**Skills:** 6 · **Combined installs:** 2.3K · **First seen:** July 21, 2026
**Source:** [skills.sh](https://skills.sh/openclaw/carapace) · [GitHub](https://github.com/openclaw/carapace) (4⭐)
**Category:** Design System / UI Engineering

The official OpenClaw design system, split into six focused skills. `openclaw-design` is the router that dispatches to the right branch for the task; the others carry the actual guidelines.

| Skill | Installs | Use For |
|---|---|---|
| openclaw-brand | 379 | Identity decisions, typography, logos, imagery, voice |
| openclaw-design | 379 | Router — selects the correct design branch per task |
| openclaw-design-audit | 379 | Design drift, token misuse, accessibility, recurring audits |
| openclaw-marketing-pages | 379 | Public pages, landing/content composition, SEO, responsive layout |
| openclaw-design-system | 378 | v0.1.x compatibility alias for upgrading skill locks |
| openclaw-carapace | 369 | App UI, semantic tokens, themes, component reuse, framework adapters |

Security: Gen Agent Trust Hub Pass, Socket Pass (Warn on openclaw-design), Snyk Pass.

[Full Setup Guide →](/hermes/skills/catalog/openclaw-carapace-setup/)

---

## 🆕 OpenClaw Graph — 3 New Skills (alphaonedev/openclaw-graph)

**Skills:** 3 · **Combined installs:** 144 · **First seen:** March 7, 2026
**Source:** [skills.sh](https://skills.sh/alphaonedev/openclaw-graph) · [GitHub](https://github.com/alphaonedev/openclaw-graph) (6⭐)

The openclaw-graph repo (311 skills, 19.7K installs) is already heavily catalogued. This sweep caught three skills the earlier passes missed.

| Skill | Installs | Use Case |
|---|---|---|
| procedural-generation | 50 | Perlin/simplex terrain, BSP dungeons, seeded procedural content |
| arkit-advanced | 48 | iOS AR scene reconstruction, 3D object tracking, RealityKit |
| testing-integration | 46 | Supertest, httpx, Testcontainers, Pact contract testing |

[Full Setup Guide →](/hermes/skills/catalog/openclaw-graph-new-skills-setup/)

---

## 🆕 Volces Skills Registry — Hermes & OpenClaw Cluster (skills.volces.com)

**Skills:** 9 · **Combined installs:** 21
**Source:** [skills.sh publisher pages](https://skills.sh) (detail pages 404 — Volces registry mirror)

ByteDance's Volces platform mirrors agent skills into the skills.sh ecosystem. Nine Hermes/OpenClaw-relevant skills surfaced, including installer and memory tooling not available anywhere else.

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

[Full Setup Guide →](/hermes/skills/catalog/volces-hermes-openclaw-skills-setup/)

---

## 🆕 Official Hermes Agent — MCP OAuth Remote Gateway (nousresearch/hermes-agent)

**Skill:** mcp-oauth-remote-gateway · **Installs:** 1 · **First seen:** ~August 4, 2026
**Source:** [skills.sh](https://skills.sh/nousresearch/hermes-agent/mcp-oauth-remote-gateway) · **Repo:** 229K⭐

A new official skill from the Hermes Agent repo. Solves the exact problem every remote-gateway deployment hits: the built-in MCP OAuth client listens on `127.0.0.1`, which breaks when Hermes runs in a container/VPS because the browser resolves loopback to the user's laptop. The skill performs the OAuth dance manually and writes tokens into the exact files Hermes' token storage expects, so `/reload-mcp` picks them up without the browser flow.

[Full Setup Guide →](/hermes/skills/catalog/hermes-mcp-oauth-remote-gateway-setup/)

---

## 🆕 Mnemosyne — Hermes Memory Providers (mnemosyne-oss/mnemosyne)

**Skill:** hermes-memory-providers · **Installs:** 4 · **First seen:** July 14, 2026
**Source:** [skills.sh](https://skills.sh/mnemosyne-oss/mnemosyne/hermes-memory-providers) · **Repo:** 2.3K⭐

Local-first memory layer that replaces Hermes' MEMORY.md/USER.md system with SQLite-backed vector + FTS5 hybrid search, episodic consolidation, temporal knowledge graphs, 20 injected memory tools, and 3 lifecycle hooks. 100% local, zero cloud.

[Full Setup Guide →](/hermes/skills/catalog/mnemosyne-hermes-memory-providers-setup/)

---

## 🆕 Honcho Ecosystem Integrations (plastic-labs)

**Skills:** 8 across 3 repos · **Combined installs:** 19

| Skill | Installs | Repo |
|---|---|---|
| honcho-setup | 8 | plastic-labs/openclaw-honcho |
| honcho-vercel-ai-sdk | 6 | plastic-labs/vercel-ai-sdk |
| honcho-setup / honcho-status / honcho-interview / honcho-config | 1 each | plastic-labs/cursor-honcho |
| honcho-setup (sillytavern) | 1 | plastic-labs/sillytavern-honcho |
| honcho-status / honcho-interview | 1 each | jaykaycodes/cursor-honcho |

Honcho (the session memory layer CorpusIQ runs) now has integration skills for OpenClaw, Cursor, the Vercel AI SDK, and SillyTavern. The plastic-labs variants are the primary copies; jaykaycodes/cursor-honcho is a fork.

---

## 🆕 cnife/skills — Hermes Skill Auditor

**Skill:** audit-hermes-agent-skills · **Installs:** 13 · **First seen:** April 22, 2026
**Source:** [skills.sh](https://skills.sh/cnife/skills/audit-hermes-agent-skills) · [GitHub](https://github.com/cnife/skills)

Audits installed Hermes skills for usage frequency via Hermes' internal API (`_find_all_skills`, `_read_manifest`, `HubLockFile`), classifies each skill by source (hub/builtin/local/external), and generates an XLSX cleanup report. UI and docs are in Chinese. Directly useful for Hermes skill-pruning cycles.

[Full Setup Guide →](/hermes/skills/catalog/cnife-audit-hermes-agent-skills-setup/)

---

## Community Long-Tail — 48 Skills from 43 Repos

Single-install community skills across the Clawd ecosystem. Worth cataloguing for completeness; most are personal configs, backups, or niche integrations. Duplicates/mirrors are flagged inline.

| Skill | Installs | Publisher |
|---|---|---|
| `github-ssh-token-workflow` | 6 | `adityahimaone/hermes-agent-rtk-caveman` |
| `openclaw-extend` | 14 | `anthemflynn/ccmp` |
| `pulse-collaboration` | 1 | `arturcrmbot/clawpilot-pulse-bundle` |
| `hermes-s2s` | 1 | `baladithyab/hermes-s2s` |
| `hermes-memory-bridge` | 1 | `baoyu0/skills` (mirror of volces skill) |
| `hermes-atlas-navigator` | 2 | `bytheby72/hermes-atlas-navigator` |
| `hermes-email-setup` | 3 | `claw.163.com/hermes-email-setup` |
| `mcp-server-management` | 1 | `dazfx/hermes-skills` |
| `hermes-configure` | 2 | `enconvo/skills` |
| `workbench-hermes-docs-sync` | 8 | `fearvox/multica-ultimate-workbench` |
| `openclaw rp plugin` | 1 | `garfeildma/openclaw-tavern` |
| `clawdbot-setup` | 7 | `goodrahstar/dailyhackerskills` |
| `telegram-triage` | 1 | `guilhermepelido/hermes-optimization-guide` |
| `clawdbot-monitor` | 13 | `krishagel/geoffrey` |
| `telegram-winwhisper-tts` | 1 | `linbenyi/hermes-custom-skills` |
| `hermes-ubuntu-stack-migration` | 1 | `liuli263/hermes-config` |
| `screen-monitor` | 19 | `ljt-520/openclaw-backup` |
| `openclaw-plugin-dev` | 2 | `majoson-chen/openclaw-plugin-dev` |
| `openclaw-plugin-dev` | 3 | `majoson-chen/skills` (duplicate listing) |
| `clawdbot-filesystem` | 1 | `matrix.openharmony.cn/clawdbot-filesystem` |
| `clawdbot-logs` | 1 | `matrix.openharmony.cn/clawdbot-logs` |
| `live-model-proof-triage` | 1 | `maxbush6299/artofclawpilot` |
| `foundry-runtime-surfaces` | 1 | `maxbush6299/artofclawpilot` |
| `hosted-observability-review` | 1 | `maxbush6299/artofclawpilot` |
| `guidance-mode-validation` | 1 | `maxbush6299/artofclawpilot` |
| `hermes-agent-consult` | 2 | `minpeter/minpeter-skills` |
| `nemoclaw-contributor-update-hermes` | 1 | `nvidia/nemoclaw` |
| `coach-nemoclaw-hermes` | 1 | `nvidia/nemoclaw-community` |
| `hermes-mythic-design` | 1 | `nylasdev/hermes-mythic-design` |
| `telegram-triage` | 2 | `onlyterp/hermes-optimization-guide` (dup with above) |
| `integrate-openclaw` | 15 | `patterai/skills` |
| `payram-openclaw-integration` | 1 | `payram/payram-mcp` |
| `hermes-config-backup` | 1 | `samuelbonifacio015/hermes-personal-config` |
| `hermes-api-client` | 1 | `scottermonk/agentautoflow` |
| `hermesemailskill` | 1 | `sequenzy/skills` |
| `clawdbot-cli` | 1 | `smithery.ai/clawdbot-cli` |
| `clawdbot-ui-development` | 1 | `smithery.ai/clawdbot-ui-development` |
| `openclaw-profanity` | 1 | `smithery.ai/openclaw-profanity` (mirror of volces skill) |
| `clawdbot-ui-development` | 2 | `ssujitx/clawdbot-ui` |
| `clawdbot-cli` | 1 | `ssujitx/clawdbot-ui` |
| `clawdbot-skill-update` | 11 | `sundial-org/awesome-openclaw-skills` |
| `clawdbot-release-check` | 6 | `sundial-org/awesome-openclaw-skills` |
| `hermes-github-backup` | 1 | `tuananh4865/hermes-backup` |
| `hermes-telegram-fix` | 1 | `unclehowell/unclehowell` |
| `clawdbot-filesystem` | 1 | `whisolla/whistant-skills` (mirror of openharmony skill) |
| `clawteam` | 11 | `win4r/clawteam-openclaw` |
| `nanami-openclaw-integration` | 1 | `yangyus8/nanami` |
| `build-openclaw-plugin` | 2 | `yigitkonur/skills-by-yigitkonur` |

---

## Why This Matters for CorpusIQ

- **MCP OAuth remote gateway** is the official solution for the exact problem CorpusIQ hits when Hermes runs behind a remote gateway: loopback redirect URIs that never reach the container. Complements our existing `corpusiq-mcp-oauth-auth` workflow.
- **Mnemosyne memory providers** is a serious local-first alternative to MEMORY.md with vector search, relevant to our memory-layer architecture work.
- **Carapace** matters if CorpusIQ builds any OpenClaw-facing UI surfaces; the design-audit skill is reusable methodology.
- **cnife skill auditor** automates the skill-pruning cycles we currently run manually.

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*
*Powered by CorpusIQ*
