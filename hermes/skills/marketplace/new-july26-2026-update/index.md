---
title: "New Skills — July 26, 2026 Marketplace Sweep (Update)"
description: "5 new publishers, 5 setup guides created, ~190K+ combined installs. Second sweep of skills.sh for Hermes-relevant skills from Neon, Anthropic, Figma"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-july26-2026-update/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "skill marketplace", "skills.sh"]

---

# New Skills — July 26, 2026 (Update)

## Summary

| Metric | Count |
|---|---|
| New publishers found | 5 |
| Setup guides created | 5 |
| Combined installs | ~190,000+ |
| Combined GitHub stars | 166,893 ⭐ |
| Quality: 🟢 Production | 5 |
| Quality: 🟡 Beta | 0 |
| Quality: 🔵 Community | 0 |

## New Skills

### Database / Serverless Platform

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Neon Agent Skills** | neondatabase/agent-skills | 75K+ | 81⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/neon-agent-skills-setup/) |

### AI / LLM Platform

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Anthropic Claude API** | anthropics/skills | 52.6K+ | 164,242⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/anthropics-claude-api-skills-setup/) |

### Design / Development

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Figma MCP Server Guide** | figma/mcp-server-guide | 23K+ | 1,809⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/figma-mcp-server-guide-setup/) |

### Observability / DevOps

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Grafana Skills** | grafana/skills | 16K+ | 200⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/grafana-skills-setup/) |

### Database / Infrastructure

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **PlanetScale Database Skills** | planetscale/database-skills | 15K+ | 556⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/planetscale-database-skills-setup/) |

## 🔑 Standout Finds

### neondatabase/agent-skills (75K+ installs, 81⭐)
The highest-install serverless database platform on skills.sh. The neon-postgres skill alone has 56.8K installs — more than any other database platform's single skill. Neon's database branching model (per-task isolated database copies) is uniquely suited to agent workflows. The AI Gateway skill provides one-API-key routing between Claude, GPT, Gemini, and open-source models — directly complementing CorpusIQ's multi-model strategy.

### anthropics/skills (52.6K installs, 164,242⭐)
The most-starred skills repository documented to date at 164K stars — surpassing all previously catalogued repos combined. While skills.sh only surfaces the `claude-api` skill, the GitHub repository is Anthropic's primary skills distribution channel for Claude Code. This is the definitive Claude API reference that should be loaded by any Hermes agent using Claude as a backend model.

### figma/mcp-server-guide (23K+ installs, 1,809⭐)
The bridge between design and code. The `implement-design` skill at 6K installs enables agents to read Figma designs and generate production code — closing the design-development gap. `figma-code-connect` enables bidirectional design-code synchronization, a capability unique to Figma among skills.sh publishers.

## Other Highlights

- **grafana/skills** (16K installs): Full observability stack — dashboards, PromQL, Loki, Mimir, Pyroscope, Beyla. The `assistant-mcp` skill enables natural language queries of observability data. Directly applicable to CorpusIQ's agent infrastructure monitoring.
- **planetscale/database-skills** (15K installs): The most balanced dual-database skills (MySQL 6.5K + Postgres 6.2K). Vitess is the only database sharding skill on skills.sh. Neki represents the emerging "agent-native" database tooling category.

## Discovery Method

Post-enterprise-sweep publisher scan: following the July 26 enterprise publisher sweep (Cloudflare, AWS, Google, HashiCorp, MongoDB, Databricks), this update targeted design, observability, and database platform publishers that had been missed. Used `npx skills find` with owner-scoped searches across 30+ additional publishers. Cross-referenced against 316 existing catalog entries. Confirmed 5 new publishers not previously catalogued.

Publishers checked but deprioritized: Netlify (7.8K, low stars), HuggingFace (8K, specialized ML), Qdrant (2.7K, niche), WorkOS (1.8K, niche), Weaviate (331, low installs), Liveblocks (758, low).

## Notes

- **anthropics/skills** at 164K GitHub stars is an outlier — Anthropic uses GitHub as their primary skills distribution, so the 52.6K skills.sh installs dramatically undercount actual usage
- **neon-postgres** (56.8K) surpasses even Supabase's individual skills — Neon has quietly become the most-installed database platform on skills.sh
- **figma/mcp-server-guide** is the only design-to-code skills publisher — unique positioning that no competitor covers
- **grafana/skills** is the only observability platform with agent skills — monitoring, logging, tracing, and profiling in one repo
- **planetscale/database-skills** offers the most balanced MySQL+Postgres coverage of any database platform
- 321 catalog entries now exist (up from 316 after this sweep)
- This sweep used `npx skills find` CLI tool instead of web search (Firecrawl unavailable) — validate with web search when Firecrawl is restored
