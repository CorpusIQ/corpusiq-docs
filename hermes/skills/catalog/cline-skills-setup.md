---
title: "Cline Skills - Official Cline 43-Skill Collection Setup"
description: "cline/skills - the official Cline org's 43 Agent Skills: frontend-design, skill-creator, review-team, data-analyst, vibe-prospecting, cloud databases, and more. 20K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cline-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "cline", "coding agent", "frontend", "cloud"]
---

# Cline Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/cline/skills) (43 skills, ~20.0K combined installs)
**GitHub:** [cline/skills](https://github.com/cline/skills) (23⭐, 3 forks, Apache-2.0, pushed Jul 21, 2026)
**Category:** Agent Development / Cloud Engineering
**First Seen:** Jun 19, 2026 on skills.sh (surfaced in the Sep 11, 2026 sweep)
**Quality Tier:** 🟢 Production (all three skills.sh audits Pass on the flagship skill)

The official skill collection from Cline - the autonomous coding agent with 67.8K GitHub stars. Published under the first-party `cline` org, these 43 skills cover frontend design, cloud data platforms, research, and agent operations. The README states they work with any agent that supports the Agent Skills standard, naming Cline, Claude Code, Cursor, OpenCode, OpenAI Codex, and Pi. Combined installs sit just under the 20K bar; drafted on first-party vendor-org authority per the HubSpot (17.8K) precedent.

---

## Installation

```bash
npx skills add cline/skills
```

Alternate paths from the README: `npx skills add https://github.com/cline/skills`, or Claude Code plugin marketplace (`/plugin install cline@cline`), or Cursor Marketplace.

For Hermes Agent, copy skill folders from a clone:

```bash
git clone --recurse-submodules https://github.com/cline/skills.git
cp -r skills/*/ ~/.hermes/skills/
```

## Skill Roster (top 20 of 43)

| Skill | Installs | What It Does |
|---|---|---|
| `frontend-design` | 2.7K | Distinctive, production-grade frontend interfaces with high design quality |
| `skill-creator` | 1.5K | Guide for creating effective skills |
| `review-team` | 1.2K | Multi-perspective code review simulation |
| `knowledge-catalog-discovery` | 959 | Discover and map knowledge catalogs |
| `playground` | 818 | Cline playground workflows |
| `desktop-commander-overview` | 765 | Desktop control via commander tooling |
| `data-analyst` | 750 | Data analysis workflows |
| `convex-design` | 728 | Convex backend design patterns |
| `site-specification` | 720 | Site spec production |
| `exa-search` | 671 | Exa-powered web search |
| `building-pydantic-ai-agents` | 635 | Pydantic AI agent construction |
| `session-report` | 511 | Session summary and report generation |
| `vibe-prospecting` | 473 | Outbound prospecting research |
| `searching-sourcegraph` | 461 | Sourcegraph code search |
| `endor-setup` | 449 | Endor dependency lifecycle tooling |
| `linear-sdk-scripting` | 442 | Linear SDK automation |
| `mintlify` | 371 | Mintlify docs authoring |
| `amplify-workflow` | 367 | AWS Amplify deployment workflows |
| `sentry-cli` | 319 | Sentry error tracking CLI |
| `dataproc-skills` | 312 | Google Dataproc (Spark) operations |

Remaining 23 cover cloud data platforms (OracleDB, Firestore, Spanner, CosmosDB, ClickHouse), AWS/GCP (Bedrock, Amazon Location, GCP-to-AWS), enterprise (SAP Fiori, UI5, TeamCity), and niche tools (save-to-spotify, math-olympiad, attorney-assist).

## Quick Start

1. Install the suite - most skills are self-contained workflows with no API keys
2. `frontend-design` is the flagship: ask for a page or component and it produces distinctive, production-grade UI
3. Platform skills (dataproc, firestore, oracledb) activate when their service appears in the conversation

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Product UI work** | `frontend-design` raises the bar for CorpusIQ dashboard and landing-page work |
| **Outbound intel** | `vibe-prospecting` and `data-analyst` feed lead research and list analysis |
| **Engineering hygiene** | `review-team`, `session-report`, and `sentry-cli` map to our PR-review, recap, and error-tracking loops |
| **Cloud ops** | Dataproc, Spanner, Firestore, and BigQuery-adjacent skills cover the cloud data stack |

## Limitations / Verification

- **Sub-20K bar, vendor authority:** 20.0K combined installs sits just under the 20K drafting bar; drafted on official Cline org authority (67.8K-star product org) per the HubSpot precedent.
- **Small skills repo:** the skills repo itself has 23 stars - traction flows through skills.sh and Cline's in-product channel, not GitHub.
- **Mix of quality:** five trailing skills carry 1 install each (artifact-management, reading-data-dict, plotting, clickhouse, steering-user-elicitation) - treat the long tail as community-grade.
- **Some submodules:** the README documents submodule-based installation for parts of the collection - use `--recurse-submodules` on clone.

```bash
# Verify skill installed
ls ~/.hermes/skills/frontend-design/SKILL.md
```

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Pass |

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup/)
- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup/)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
