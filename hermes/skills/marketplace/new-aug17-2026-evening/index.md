---
title: "New Skills — August 17, 2026 (Evening)"
description: "skills.sh evening sweep: Nx AI Agents Config (44.7K, 10), M. Collina Node Skills (52.4K, 12), Zhaono1 Agent Playbook (50.4K, 24) — 3 publisher clusters, 46 skills, 3 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug17-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-17-evening"
new_publishers: 3
new_skills: 46
guides_drafted: 3
---

# New Skills — August 17, 2026 (Evening)

Evening sweep of August 17. The API surface stayed fully caught up (40 queries, 3,943 unique skills, all top-120 clusters known even after the recovery pass excluding `new-aug17-2026*`), so the batch came from the two proven fallbacks: hot-page brand candidates the API never ranks and carry-over queue re-verification. Both paid.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| mcollina/skills | 12 | 52.4K | 🟢 | [M. Collina Node Skills Setup](/hermes/skills/catalog/mcollina-node-skills-setup/) |
| zhaono1/agent-playbook | 24 | 50.4K | 🟡 | [Zhaono1 Agent Playbook Setup](/hermes/skills/catalog/zhaono1-agent-playbook-setup/) |
| nrwl/nx-ai-agents-config | 10 | 44.7K | 🟢 | [Nx AI Agents Config Setup](/hermes/skills/catalog/nx-ai-agents-config-skills-setup/) |

## Method Notes

- mcollina/skills and nrwl/nx-ai-agents-config surfaced on the hot page (1H delta) with 2-install deltas each — exactly the API-omission trap from Aug 16: official vendor clusters invisible to install-ranked API queries. Publisher pages read 52.4K (fastify-best-practices 36.4K, Matteo Collina, 1.9K GitHub stars) and 44.7K (nx-workspace 31.4K, official Nx org). Both flagships pass 3/3 security audits.
- zhaono1/agent-playbook came from queue re-verification: parked with stale API numbers ("top skill guided via charon-fan; rest ≤1.2K"), the publisher page reads 50.4K total with self-improving-agent at 33.1K. Drafted the full 24-skill suite with the sibling charon-fan guide cross-referenced; flagship carries GATH Warn + Socket Warn (named).
- Re-verified flat and re-parked: uni-stack/uniwind 5.4K, asksurf-ai/surf-skills 3.8K, ningzimu/codex-ppt-skill 3.6K, amazonappdev/devices-agent-skills 5.2K (official but Fire TV niche), dmmulroy/anti-slop 2.4K, streakyc/googleworkspacecli 1.8K (95 skills), steel-dev/skills 1.3K.
- Security audits per flagship: mcollina 🟢 (3/3 Pass), nrwl 🟢 (3/3 Pass), zhaono1 🟡 (GATH Warn + Socket Warn, Snyk Pass).

## Evaluated and Queued (next sweep)

| Cluster | Installs | Reason parked |
|---|---|---|
| uni-stack/uniwind | 5.4K | Flat since Aug 15; RN tooling, at bar |
| amazonappdev/devices-agent-skills | 5.2K | Flat; Fire TV migration niche, official org |
| asksurf-ai/surf-skills | 3.8K | Flat; crypto-adjacent |
| ningzimu/codex-ppt-skill | 3.6K | Flat |
| dmmulroy/anti-slop | 2.4K | Below bar; family (stop-slop, avoid-ai-writing) already guided |
| streakyc/googleworkspacecli | 1.8K | 95 skills but top skill 391 installs |
| steel-dev/skills | 1.3K | Browser-automation vendor, brand watch |

## Notable Signals for CorpusIQ

- **mcollina/skills** is the canonical Fastify reference straight from the framework author — any agent-built Node service work now has a first-party pattern source.
- **nx-ai-agents-config** is the first official monorepo-navigation cluster catalogued; its read-only exploration posture matches our verification-before-assertion discipline.
- **zhaono1/agent-playbook** mirrors our own self-improvement loop (skill patching, session continuity) — useful cross-check for the audit-ready-agent-loop pattern.

## Index State After Sweep

- catalog/index.md: +3 entries
- marketplace/index.md: header 888 → 891, footer 939 → 942
- last_updated on both indexes: 2026-08-17
