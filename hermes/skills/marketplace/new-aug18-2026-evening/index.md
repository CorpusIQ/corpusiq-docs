---
title: "New Skills — August 18, 2026 Evening"
description: "skills.sh sweep: Claude for Legal (54.4K, 118), PCL Domain Experts (36.2K, 104), VTEX Skills (32.6K, 51), Genshijin (19.2K, 7), Hono Skill (11.7K, 1), Capawesome (11.4K, 37), Wyatt Walsh Agents (2.1K, 85) — 7 publisher clusters, 403 skills, 7 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug18-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-18-evening"
new_publishers: 7
new_skills: 403
guides_drafted: 7
---

# New Skills — August 18, 2026 Evening

Evening sweep of August 18. The API surface stayed fully caught up (39 of 40 queries, 3,854 unique skills; the one email query timed out). The plain diff returned only two candidates, both noise (a superpowers fork whose family is already guided via obra, and PCL flagged only by the substring-match trap). The real batch came from hot-page triage of vendor clusters, following the steady-state pattern: hot-page owner triage plus publisher-page verification is the primary discovery channel.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| anthropics/claude-for-legal | 118 | 54.4K | 🟢 | [Claude for Legal Skills Setup](/hermes/skills/catalog/claude-for-legal-skills-setup/) |
| personamanagmentlayer/pcl | 104 | 36.2K | 🟡 | [PCL Domain Expert Skills Setup](/hermes/skills/catalog/pcl-domain-expert-skills-setup/) |
| vtex/skills | 51 | 32.6K | 🟢 | [VTEX Skills Setup](/hermes/skills/catalog/vtex-skills-setup/) |
| interfacex-co-jp/genshijin | 7 | 19.2K | 🟢 | [Genshijin Skills Setup](/hermes/skills/catalog/genshijin-skills-setup/) |
| yusukebe/hono-skill | 1 | 11.7K | 🟡 | [Hono Skill Setup](/hermes/skills/catalog/hono-skill-setup/) |
| capawesome-team/skills | 37 | 11.4K | 🟡 | [Capawesome Skills Setup](/hermes/skills/catalog/capawesome-skills-setup/) |
| wyattowalsh/agents | 85 | 2.1K | 🟢 | [Wyatt Walsh Agents Setup](/hermes/skills/catalog/wyattowalsh-agents-setup/) |

## Method Notes

- anthropics/claude-for-legal surfaced from the hot page (amendment-history 1+1) and read 54.4K across 118 skills on its publisher page — official Anthropic, 9.2K GitHub stars, all three audits Pass on legal-writing.
- personamanagmentlayer/pcl came from the API diff (finance-expert 6.2K via API, 36.2K across 104 skills on the publisher page). Snyk Warn on finance-expert; 41 stars.
- vtex/skills surfaced on the hot page (marketplace-order-hook 1+1); publisher page reads 32.6K across 51 skills, official VTEX org, all three audits Pass.
- interfacex-co-jp/genshijin at #2 on the hot page (genshijin-commit 13+13 1H) with 19.2K across 7 skills; drafted below the 20K bar on hot momentum plus Japanese corporate publisher. SKILL.md content is Japanese — flagged in the guide per the wecomteam precedent.
- yusukebe/hono-skill at 11.7K on one skill; drafted below the bar on framework-author authority (Hono's creator). Snyk Warn.
- capawesome-team/skills at 11.4K across 37 skills; drafted below the bar on ecosystem-team authority (Capacitor plugin vendor). Snyk Fail on the flagship.
- wyattowalsh/agents at 2.1K across 85 skills; drafted below the bar on platform-founder authority (skills.sh's founder) and the unique skill-lifecycle governance category it covers (budget linter, compat matrix, quality dashboard, lifecycle manager). All three audits Pass on orchestrator.
- Mac Mini still unreachable — sweep ran entirely from the Spark canonical clone, push auth via gh auth token.
- Carried-over queue re-verified on this sweep's hot page and re-parked; five new queue entries added from this sweep's triage (see Evaluated and Queued).

## Evaluated and Queued

| Cluster | Skills | Installs | Reason parked |
|---|---|---|---|
| fission-ai/openspec | 13 | 8.5K | Spec-driven dev workflow, 10K-star-class repo; watch for growth |
| whytryharder/superpowers | 2 | 8.3K | Superpowers fork; obra family already guided |
| uni-stack/uniwind | 6 | 5.4K | Flat since Aug 15 |
| amazonappdev/devices-agent-skills | 18 | 5.2K | Fire TV niche |
| asksurf-ai/surf-skills | 2 | 3.8K | Crypto-adjacent |
| sentimony/skills | 10 | 3.1K | Unknown publisher; web-debug 571 top |
| ningzimu/codex-ppt-skill | 1 | 3.6K | Niche |
| dmmulroy/anti-slop | 2 | 2.4K | Family already guided |
| streakyc/googleworkspacecli | 95 | 1.8K | Top skill 391 installs |
| amplitude/mcp-marketplace | 27 | 1.6K | Official Amplitude, brand watch |
| prismicio/skills | 1 | 1.1K | Official Prismic, watch |
| steel-dev/skills | 1 | 1.3K | Browser-automation vendor, brand watch |
| modelscope.cn (site) | — | — | Site publisher, docx skill on hot |
| developer.paddle.com (site) | — | — | Site publisher, paddle-subscription-sync on hot |

## Notable Signals for CorpusIQ

- **Claude for Legal** is the largest official-Anthropic workflow suite catalogued after anthropics/skills — 118 skills covering the full legal matter lifecycle with a self-governing skill-manager pattern worth studying for our own skill pack governance.
- **PCL** demonstrates the persona-layer category: 104 domain-expert personas (finance 6.2K, telecom 1.8K) that pair naturally with connector data for vertical operator questions.
- **VTEX** extends our ecommerce skill coverage to a major platform, matching the connector-heavy ecommerce workflows CorpusIQ serves.
- **Wyatt Walsh's agents** is the platform founder's own toolkit, including the only dedicated skill-lifecycle governance suite on skills.sh — directly relevant to maintaining large skill collections like ours.

## Index State After Sweep

- catalog/index.md: +7 entries
- marketplace/index.md: header 895 → 902, footer 946 → 953
- last_updated on both indexes: 2026-08-18
