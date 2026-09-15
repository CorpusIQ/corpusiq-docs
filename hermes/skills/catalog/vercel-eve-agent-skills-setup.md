---
title: "Vercel Eve Agent Skills - Official Eve Agent Framework Skills Setup"
description: "vercel/eve - 4 first-party skills from Vercel's open Eve agent framework: the eve skill itself, gh-pr-description, technical-writing, and human-writing. 6.9K skills.sh installs, 5K-star repo. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vercel-eve-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "vercel", "eve", "agents", "backend"]
---

# Vercel Eve Agent Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/vercel/eve) (4 skills, ~6.9K combined installs)
**GitHub:** [vercel/eve](https://github.com/vercel/eve) (5,042⭐, 527 forks, Apache-2.0, pushed Sep 11, 2026 - same-day active)
**Category:** Agent Development / Backend
**First Seen:** Jun 17, 2026 on skills.sh (surfaced in the Sep 11, 2026 sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub Pass / Socket Warn / Snyk Warn on the flagship skill)

Four skills published from Eve - Vercel's open framework for building durable backend AI agents. The flagship `eve` skill teaches an agent to build, edit, and debug Eve projects (agent instructions, skills, tools); the other three are the framework's own engineering-hygiene skills for PR descriptions, technical writing, and human-sounding prose. Drafted below the 20K install bar on first-party platform-org authority (the `vercel` org, 5K-star repo, same-day commits).

---

## Installation

```bash
npx skills add vercel/eve
```

Skill file locations in the repo: `skills/eve/SKILL.md` and `.agents/skills/{gh-pr-description,technical-writing}/SKILL.md`. Copy any of them into an agent skills directory to use without the CLI:

```bash
git clone https://github.com/vercel/eve.git
cp eve/skills/eve/SKILL.md ~/.hermes/skills/eve/
```

## Skill Roster

| Skill | Installs | What It Does |
|---|---|---|
| `eve` | 5.5K | Build durable backend AI agents with the eve framework - agent instructions, skills, tools, and debugging; points at `node_modules/eve/docs/` reading order before writing code |
| `gh-pr-description` | 661 | Generate structured GitHub PR descriptions |
| `technical-writing` | 623 | Documentation quality with content-type, editing, style, and review references |
| `human-writing` | 145 | Writing that does not read as AI-generated |

## Quick Start

1. Install the suite - no API keys required
2. `eve` skills any eve project: create agents, wire skills and tools, debug; the skill insists on reading the framework docs first
3. `gh-pr-description` and `technical-writing` work standalone on any repo or docs task

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Backend agent stack** | Eve's durable-agent architecture is a direct reference for CorpusIQ's own agent infrastructure decisions |
| **PR and docs hygiene** | `gh-pr-description` and `technical-writing` are immediately useful on the corpusiq-docs and MCP-server repos |
| **Content voice** | `human-writing` aligns with CorpusIQ's anti-AI-slop content standards |

## Limitations / Verification

- **Sub-20K bar, platform authority:** 6.9K installs is below the 20K drafting bar; drafted on first-party platform-org authority (official `vercel` org - the Aug 16 precedent for vendor orgs) plus 5,042⭐ and same-day repo activity.
- **Two audit Warnings:** the flagship `eve` skill renders Socket Warn and Snyk Warn - review-first for anything beyond the docs-hygiene skills.
- **Framework coupling:** the `eve` skill is only useful on eve projects; the three hygiene skills are the general-purpose value.

```bash
# Verify skill installed
ls ~/.hermes/skills/eve/SKILL.md
```

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Warn |
| Snyk | Warn |

## Related

- [Next.js Agent Skills - Official Vercel Skill Suite Setup](/docs/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/docs/hermes/skills/catalog/vercel-agent-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/docs/hermes/skills/catalog/vercel-ai-skills-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
