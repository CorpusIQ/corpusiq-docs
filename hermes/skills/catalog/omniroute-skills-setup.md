---
title: "OmniRoute Skills - 70.9K⭐ AI Gateway Suite Setup"
description: "Setup guide for diegosouzapw/OmniRoute - 44 agent skills for the free MIT AI gateway: 359 providers, 1200+ models, token compression, MCP/A2A, skill importing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/omniroute-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes skill", "agent skill", "skill setup", "ai gateway", "llm routing", "mcp"]
---

# OmniRoute Skills - Setup Guide

**Source:** [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) (70,907⭐, MIT, pushed Sep 27, 2026)
**Skill:** `diegosouzapw/OmniRoute` (44 installable skills, ~26K combined installs)
**Homepage:** [omniroute.online](https://omniroute.online)
**Category:** AI Gateway / LLM Infrastructure
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 28, 2026)

OmniRoute is a free MIT-licensed AI gateway: one endpoint serving 359 providers (150+ free) and 1,200+ models (Kimi, Claude, GPT, Gemini, GLM, DeepSeek, MiniMax), with quota-aware auto-fallback, RTK+Caveman compression (15-95% token savings), MCP/A2A support, and desktop/PWA clients. It works with Claude Code, Codex, Cursor, OpenCode, Cline and Copilot. The bundled agent skills let an agent configure, monitor, and operate the gateway from inside Hermes - including `omni-github-skills`, which searches, scores, malware-scans, and imports agent skills from GitHub.

---

## Installation

```bash
# Full suite
npx skills add diegosouzapw/OmniRoute

# Single domain
npx skills add diegosouzapw/OmniRoute --skill cli-setup
```

## Roster - Core Skills

| Skill | Installs | Does |
|---|---|---|
| omni-combos-routing | 738 | Provider combo routing strategies |
| cli-setup | 721 | Gateway setup and first-run configuration |
| omni-mcp | 675 | MCP server management on the gateway |
| omni-auth | 657 | Provider authentication and key management |
| cli-routing | 657 | Routing rules and fallback chains |
| cli-providers | 657 | Provider inventory and enable/disable |
| omni-providers | 637 | Provider platform operations |
| omni-inference | 630 | Model inference and generation calls |
| cli-keys | 624 | API key administration |
| cli-serve | 620 | Run the local gateway server |
| cli-cost-usage | 620 | Spend tracking and usage reports |
| cli-models | 615 | Model catalog management |
| omni-compression | 608 | RTK+Caveman token compression |
| cli-health | 603 | Gateway health checks |
| omni-budget | 591 | Budget caps and quota enforcement |
| cli-chat | 591 | Chat through the gateway |
| config-codex-cli | 587 | Codex CLI integration config |
| cli-skill-collector | 565 | Collect and manage installed skills |
| omni-github-skills | 573 | Search, score, scan, import agent skills from GitHub (malware + secret scanning) |
| omni-resilience | 582 | Fallback and resilience configuration |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Model routing** | `cli-routing` + `omni-combos-routing` mirror CorpusIQ's Qwen-first/DeepSeek-escalation routing on a self-hosted gateway |
| **Token cost reduction** | `omni-compression` (15-95% savings) applies to high-volume sweeps and research crons |
| **Skill catalog operations** | `omni-github-skills` automates the same search/score/scan/import loop as the daily skills.sh sweep |
| **Cost attribution** | `cli-cost-usage` provides per-provider spend attribution for the $250/month budget |
| **Infra resilience** | `omni-resilience` + `cli-health` add quota-aware fallback to cron pipelines |

## Limitations / Verification

- Skills operate the OmniRoute gateway; the gateway itself is a separate install (omniroute.online)
- 70.9K⭐ repo with active releases; API surfaces change between releases (release/v3.8.51 at sweep time)
- Verify: `npx skills add diegosouzapw/OmniRoute --list` shows 44 skills

## Security

No skills.sh security audits published (verified Sep 28, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Hermes Agent Official Skills Setup](/hermes/skills/catalog/hermes-agent-official-skills-batch-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
