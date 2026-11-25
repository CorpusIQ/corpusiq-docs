---
title: "NicePkg AI Workflow - Prebuilt Skill Library Setup"
description: "nicepkg/ai-workflow - 10.5K combined installs: 170+ prebuilt skills for Claude Code, Cursor and Codex covering marketing, SEO, trading and video."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nicepkg-ai-workflow-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "cursor", "marketing", "trading"]
---

# NicePkg AI Workflow - Setup Guide

**Source:** [nicepkg/ai-workflow](https://www.skills.sh/nicepkg/ai-workflow) via skills.sh - 10.5K combined installs across 96 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [nicepkg/ai-workflow](https://github.com/nicepkg/ai-workflow) - 296 stars, MIT license, last pushed Jan 20, 2026, main branch; a top-level .claude/skills/ directory with seven workflow-management skills plus six workflow folders (content-creator, marketing-pro, video-creator, stock-trader, product-manager, talk-to-slidev) that each bundle their own .claude/skills/ collection.
**Category:** Multi-Domain AI Workflow (Marketing, SEO, Trading, Video, PM)
**Quality Tier:** 🟠 Orange - 3 Gen Agent Trust Hub Fail cells and 14 Warn cells across the 15 sampled skills.

nicepkg/ai-workflow ships 170+ prebuilt skills as curated "workflows" that load domain expertise into an AI coding assistant in one command. The six workflows cover content creation, marketing, video production, stock trading, product management, and slide presentations, and the README positions the project as an answer to re-teaching the same frameworks at the start of every session. Seven workflow-management skills sit at the repo root for discovering, downloading, creating, and composing skills into new workflows.

The skills.sh index lists 96 listings at 10.5K combined installs, led by the seven workflow-management skills (each at 285 installs or more) and a long per-domain tail. The repository ships far more skill directories than the index covers: the README documents 170+ skills across the six workflows, so the index is a subset of the tree. The README was last updated alongside the Jan 20, 2026 push, so it may lag the newest AI tooling.

## Installation

The recommended path is to install a complete workflow with one command:

```bash
npx add-skill nicepkg/ai-workflow/workflows/content-creator-workflow
```

Install individual skills with the --skill flag, or list what a workflow offers first:

```bash
npx add-skill nicepkg/ai-workflow/workflows/stock-trader-workflow --skill a-share-analysis
npx add-skill nicepkg/ai-workflow/workflows/marketing-pro-workflow --list
```

Advanced flags: --global installs for every project, -a targets specific tools (for example -a claude-code -a cursor), and -y runs non-interactively for CI. The README lists install paths for 14+ assistants, including Claude Code (.claude/skills/), Cursor (.cursor/skills/), Codex (.codex/skills/), OpenCode (.opencode/skill/), Gemini CLI (.gemini/skills/) and Windsurf (.windsurf/skills/).

## What It Provides

The seven top-level .claude/skills/ skills are the seven listings at 200 installs or more; every other indexed listing sits below 200 installs.

| Skill | Installs | Use For |
|---|---|---|
| resource-scout | 361 | search marketplaces, GitHub and registries for skills and MCP servers |
| workflow-creator | 349 | create workflow directories with curated skills and generated docs |
| skill-downloader | 342 | download and install skills from GitHub, archives and direct URLs |
| skill-creator | 317 | create or update a skill with specialized knowledge and workflows |
| add-new-skills-to-workflow | 308 | add skills to a workflow and update its documentation |
| legacy-to-ai-ready | 295 | transform legacy codebases into AI-ready Claude Code projects |
| remove-old-skills-from-workflow | 285 | remove skills from a workflow and update its documentation |

The remaining 89 indexed listings range from 66 to 151 installs.

## Why This Matters for Hermes Agents

The useful part of this collection for a Hermes builder is the workflow layer, not any single skill. The seven root-level skills let an agent discover, download, create, add, and remove skills, then assemble them into a workflow directory with its own AGENTS.md and README, so a team can turn a loose set of domain skills into a repeatable project template. The six bundled workflows already do this for common business functions: content, marketing, video, trading, product management, and presentations. That matters because a Hermes agent pointed at this repo inherits 170+ skills worth of frameworks without a per-skill install ceremony. The install surface is a single npx add-skill command that targets 14+ assistants, so the same workflow can be reused across Claude Code, Cursor, Codex, and others. The tradeoff is breadth over depth: the collection is community-assembled from Anthropic, Vercel, and other sources, and the security sample carries three Gen Agent Trust Hub Fails, so it rewards review before you trust a workflow in production.

## Usage

| You say | What happens |
|---|---|
| Create a content workflow for my blog | Uses workflow-creator to scaffold a workflow directory with curated skills |
| Download and install a skill from a GitHub URL | Uses skill-downloader to fetch the skill from GitHub, an archive or a URL |
| Find skills for competitor analysis | Uses resource-scout to search marketplaces, GitHub and registries |
| Make this legacy codebase AI-ready | Uses legacy-to-ai-ready to generate CLAUDE.md, skills and agent config |
| Add this skill to my existing workflow | Uses add-new-skills-to-workflow to wire the skill in and update docs |
| Build a custom skill for my team | Uses skill-creator to define a new skill with knowledge and workflows |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/nicepkg/ai-workflow/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/nicepkg/ai-workflow/main/.claude/skills/resource-scout/SKILL.md | head -40
```

Both URLs return 200. After installing, review each SKILL.md before relying on it; the seven root-level skills are self-contained SKILL.md files, and each workflow folder carries its own AGENTS.md and README.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| resource-scout | Pass | Pass | Warn |
| workflow-creator | Pass | Warn | Warn |
| skill-downloader | Warn | Warn | Warn |
| skill-creator | Fail | Pass | Pass |
| add-new-skills-to-workflow | Pass | Warn | Warn |
| legacy-to-ai-ready | Fail | Warn | Pass |
| remove-old-skills-from-workflow | Pass | Pass | Pass |
| social-media-content-repurposer | Pass | Pass | Pass |
| a-share-analysis | Pass | Pass | Warn |
| canvas-design | Pass | Pass | Pass |
| content-trend-researcher | Pass | Pass | Warn |
| youtube-transcript | Fail | Pass | Warn |
| skill-navigator | Pass | Pass | Pass |
| content-brief | Pass | Pass | Warn |
| content-research | Pass | Pass | Warn |

Three sampled skills carry a Gen Agent Trust Hub Fail (skill-creator, legacy-to-ai-ready, youtube-transcript), and skill-downloader draws Warns on all three auditors; the sample covers 15 of 96 listings.

## Limitations

- Snapshot data, verified Nov 25, 2026: 10,463 combined installs across 96 indexed listings; 296 GitHub stars; MIT license; last pushed Jan 20, 2026. Counts drift over time.
- The README was last updated alongside the Jan 20, 2026 push and may lag current AI tooling; its "14+ AI coding assistants" list and per-workflow skill counts reflect that snapshot.
- The install index (96 listings) is a subset of the tree: the README documents 170+ skills across the six workflows, so most bundled skills have no skills.sh listing.
- The security sample (15 of 96) carries three Gen Agent Trust Hub Fails and Warns across most of the rest, so the seven workflow-management skills are cleaner than the domain tail.
- The stock-trader workflow covers US, China A-share, Hong Kong and Taiwan markets and bundles skills for the akshare and shioaji tooling; skills that reach live market data or a brokerage account deserve review before use.

## Related

[AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup) | [Gohypergiant Agent Skills - Engineering Collection](/hermes/skills/catalog/agent-skills-setup) | [Boring Marketing Skills - Marketing Operator Suite Setup](/hermes/skills/catalog/boring-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install a whole workflow with npx add-skill rather than picking skills one by one; the workflow folders ship their own AGENTS.md and README.
- Use --list before --skill so the agent sees the exact skill names a workflow offers.
- Point -a at the tools you actually use so the skills land in the right directories.
- Treat resource-scout and skill-downloader as the pair that fetches new skills from elsewhere; review anything they pull in before trusting it.
- Keep the stock-trader workflow away from a funded account until you have read its SDK and brokerage skills.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
