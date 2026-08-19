---
title: "New Skills — August 19, 2026"
description: "skills.sh sweep: openclaw/agent-skills — the official OpenClaw org's canonical agent workflow suite (8 skills, ~2.0K installs, autoreview 1,388) — 1 publisher cluster, 8 skills, 1 setup guide."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug19-2026/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-19"
new_publishers: 1
new_skills: 8
guides_drafted: 1
---

# New Skills — August 19, 2026

Morning sweep of August 19. The broad API surface was fully caught up: 40 queries, 3,944 unique skills, and the cluster-level diff against the hermes/ tree returned zero candidates at the 2,000-install and 500-install thresholds — all 120 top clusters already guided. The find came from the supplemental targeted pass: Hermes-ecosystem queries (`hermes`, `openclaw`, `gbrain`, `clawd`) surfaced one genuinely new publisher cluster that the broad pass ranked below the top band.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| openclaw/agent-skills | 8 | ~2.0K | 🟡 | [OpenClaw Agent Skills Setup](/hermes/skills/catalog/openclaw-agent-skills-setup/) |

## Method Notes

- The cluster-level diff script (full owner/repo grep, generic-name sibling check, 2,000-install floor) returned zero candidates. Lowering the floor to 500 also returned zero — the marketplace's top-120 cluster band is fully catalogued as of the Aug 18 evening sweep.
- The supplemental Hermes-ecosystem pass (10 targeted queries: hermes, openclaw, clawd, gbrain, honcho, nous, claude code skill, cursor rules, agent skill, n8n) flagged 7 candidate sources; 6 were noise or family-known (single-install gbrain forks, a 1-install digital-creature novelty, QuantumNous' new-api gateway skill at 980 installs — LLM infra, not Hermes agent tooling).
- `openclaw/agent-skills` is the official OpenClaw org repository: 1,057 GitHub stars, last commit August 18, 2026 (the day before this sweep). Eight skills across review, handoff, sessions, and documentation families. autoreview leads at 1,388 installs.
- Drafted below the 20K bar on official-org authority — the OpenClaw org's own canonical skill suite, matching the wyattowalsh and hono precedent (authority over install volume).
- Mac Mini still unreachable — sweep ran entirely from the Spark canonical clone, push auth via gh CLI token.

## Evaluated and Queued

| Cluster | Skills | Installs | Reason parked |
|---|---|---|---|
| quantumnous/skills (newapi) | 1 | 980 | "nous" substring false positive; New API gateway management, not Hermes agent tooling |
| imphillip/gbrain-openclaw | 5 | 5×1 | Single-install gbrain fork; garrytan/gbrain family already guided |
| laozhong86/gbrain | 1 | 1 | Single-install gbrain fork |
| morris-utrust/gbrain-knowledge | 1 | 1 | Single-install TCM niche fork |
| nexus9888/hermes-memory-skills | 1 | 1 | Single-install dreaming wrapper; Honcho family already guided |
| ad/hermes-digital-creature | 1 | 1 | Novelty skill, below bar |

## Notable Signals for CorpusIQ

- **autoreview** is the strongest single signal: a structured multi-engine code review workflow (Codex default, Claude/Amp/Pi/Kimi optional) whose default P0-only, advisory output maps directly to our verify-before-assertion discipline.
- **handoff + agent-transcript** cover the two halves of multi-agent context passing — standalone prompt construction and sanitized PR/issue transcript provenance — both directly relevant to our orchestration and public-content sanitization rules.
- The repo's `scripts/install-skills` installer (list, dry-run, selective, copy-vs-symlink, custom target) is a clean reference pattern for skill-suite distribution worth studying for our own pack governance.

## Index State After Sweep

- catalog/index.md: +1 entry
- marketplace/index.md: header 902 → 903, footer 953 → 954
- last_updated on both indexes: 2026-08-19
