---
title: "COG Second Brain - Self-Evolving Knowledge Setup"
description: "huytieu/cog-second-brain - 6.0K combined installs: a self-evolving second brain with AI skills, worker agents and a people CRM on plain Markdown."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cog-second-brain-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "second brain", "knowledge management", "personal knowledge"]
---

# COG Second Brain - Setup Guide

**Source:** [huytieu/cog-second-brain](https://www.skills.sh/huytieu/cog-second-brain) via skills.sh - 6.0K combined installs across 41 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain) - 1,518 stars, MIT license, last pushed Oct 23, 2026, main branch; 43 skill directories under skills/<name>/SKILL.md mirrored to .claude/skills/ and .agents/skills/, 10 agent definitions under .claude/agents/, and 7 role packs under .claude/roles/.
**Category:** Personal Knowledge Management (Second Brain)
**Quality Tier:** 🟡 Yellow - all 15 sampled skills pass the Gen Agent Trust Hub and Socket checks; nine carry a Warn cell on Snyk and none carries a Fail.

COG (Cognition + Obsidian + Git) is a self-evolving second brain built from Markdown files, agent skills, worker agents, and version control instead of a database. It ships a daily capture-to-synthesis loop (braindump, daily brief, weekly check-in, monthly consolidation), a product management workflow, and a V-model verification harness where six workers execute and four read-only verifiers grade the artifact rather than the worker's summary. It is inspired by Garry Tan's gstack and gbrain and targets Claude Code, Antigravity, Cursor, Kiro, Gemini CLI, and OpenAI Codex, with AGENTS.md as a universal fallback.

The skills.sh index lists 41 listings at 6.0K combined installs. The repository tree carries 43 skill directories under skills/, so two in-tree skills (review-cockpit and slop-gate) have no indexed listing while every indexed listing maps to a skills/<name>/ directory. Personal content (braindumps, profiles, notes) lives in numbered vault folders (00-inbox through 06-templates) and stays separate from framework files during updates.

## Installation

Clone the repository and run onboarding in your agent:

```bash
git clone https://github.com/huytieu/COG-second-brain.git
cd COG-second-brain
```

Onboarding is triggered per agent: Claude Code (run `code .` then "Run onboarding", reading .claude/skills/), Antigravity (open the folder then "Run onboarding", reading .agents/skills/ plus .agents/rules/cog.md), Cursor (open the folder, reading .cursor-plugin/ plus .cursorrules), Kiro (open the folder then "setup COG", reading .kiro/powers/), Gemini CLI (run `gemini` then /onboarding, reading GEMINI.md plus .gemini/commands/), and OpenAI Codex (run `codex` then "Run onboarding", reading AGENTS.md).

Or install through the skills directory:

```bash
npx skills add huytieu/COG-second-brain
```

Updates separate framework files from personal content: run ./cog-update.sh (with --check, --dry-run or --force) or say "Update COG". Check the version with cat COG-VERSION and validate the packaged agent surfaces with ./scripts/validate-agent-surface.sh.

## What It Provides

skills.sh publishes per-skill descriptions for 15 of the 41 indexed listings, and every skill in the table below has one. All 41 indexed listings have a matching skills/<name>/ directory in the current tree, which also ships two more skills (review-cockpit and slop-gate) with no indexed listing.

| Skill | Installs | Use For |
|---|---|---|
| weekly-checkin | 231 | cross-domain pattern analysis and strategic reflection for weekly review |
| braindump | 220 | capturing raw thoughts with domain classification and competitive intelligence extraction |
| auto-research | 217 | decomposing strategic questions into parallel research threads and synthesizing sourced analysis |
| knowledge-consolidation | 215 | building frameworks from scattered insights across braindumps and notes |
| onboarding | 213 | personalizing COG with profile, interests and watchlist files (run first) |
| daily-brief | 213 | generating personalized news intelligence with verified, sourced stories |
| update-cog | 210 | applying upstream COG framework updates without touching personal content |
| update-knowledge-base | 208 | maintaining the product knowledge base from releases, features and project changes |
| comprehensive-analysis | 207 | deep 7-day analysis across all data sources for weekly reviews and board prep |
| url-dump | 204 | capturing URLs with automatic extraction, insights and categorization into knowledge booklets |
| meeting-transcript | 204 | processing recordings and notes into structured decisions, actions and team dynamics |
| scout | 203 | evaluating URLs and tools for vault coverage, relevance and a save-or-skip recommendation |

The remaining 29 indexed listings range from 24 to 199 installs.

## Why This Matters for Hermes Agents

COG is a worked example of the disciplined-agent pattern: a Markdown vault as durable memory, a skills layer for repeatable workflows, and a verification harness where the worker never grades its own homework. The parts worth studying are the closed-loop skill (plan, build, component verify, integration verify, acceptance) and the read-only verifiers, which receive paths rather than the worker's output so they classify evidence instead of a summary. Framework files are separated from personal content, so updates never overwrite your notes, and the update path (./cog-update.sh or the update-cog skill) is reproducible. The multi-agent support surface demonstrates one set of skills shipped across several agents through parallel .claude/, .agents/, .kiro/, and .gemini/ directories plus AGENTS.md. Adoption costs are modest: the skills are plain Markdown, but team skills expect the GitHub CLI and optionally Linear, Slack, and PostHog integrations, and nine sampled skills carry a Warn cell on Snyk.

## Usage

| You say | What happens |
|---|---|
| Run onboarding | Uses onboarding to create your profile, interests and watchlist files |
| I need to braindump | Uses braindump to capture and classify raw thoughts |
| Give me my daily brief | Uses daily-brief to generate sourced news intelligence |
| Save this URL | Uses url-dump to extract content and categorize it into knowledge booklets |
| Weekly review | Uses weekly-checkin for cross-domain pattern analysis |
| Research this strategic question | Uses auto-research to decompose it into parallel threads and synthesize findings |
| Run this build through the closed loop | Uses closed-loop with separate verifiers so the worker does not grade its own work |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/huytieu/COG-second-brain/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/huytieu/COG-second-brain/main/skills/onboarding/SKILL.md | head -40
```

Both URLs return 200. After installing, run onboarding in your agent, then check the version with cat COG-VERSION and validate the packaged agent surfaces with ./scripts/validate-agent-surface.sh.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| weekly-checkin | Pass | Pass | Pass |
| braindump | Pass | Pass | Pass |
| auto-research | Pass | Pass | Warn |
| knowledge-consolidation | Pass | Pass | Pass |
| onboarding | Pass | Pass | Pass |
| daily-brief | Pass | Pass | Warn |
| update-cog | Pass | Pass | Pass |
| update-knowledge-base | Pass | Pass | Warn |
| comprehensive-analysis | Pass | Pass | Warn |
| url-dump | Pass | Pass | Warn |
| meeting-transcript | Pass | Pass | Pass |
| scout | Pass | Pass | Warn |
| generate-release-notes | Pass | Pass | Warn |
| generate-prd | Pass | Pass | Warn |
| create-user-story | Pass | Pass | Warn |

Nine sampled skills carry a Warn cell on Snyk; none carries a Fail. 15 of the 41 indexed listings were sampled; the rest were not.

## Limitations

- Snapshot data, verified Nov 24, 2026: 6,013 combined installs across 41 indexed listings; 1,518 GitHub stars; MIT license; last pushed Oct 23, 2026. Counts drift over time.
- The install index and the tree do not fully agree: the tree carries 43 skill directories, so review-cockpit and slop-gate have no indexed listing while all 41 indexed listings map to a skills/<name>/ directory.
- The README counts 43 skills (and 33 native Claude Code skills in its Agent Support Matrix), while the directory description mentions 35; the count has drifted as skills were added.
- Nine of the 15 sampled skills carry a Warn cell on Snyk (auto-research, daily-brief, update-knowledge-base, comprehensive-analysis, url-dump, scout, generate-release-notes, generate-prd, and create-user-story); none carries a Fail.
- Team skills (team-brief, meeting-transcript, and the PM workflow) expect the GitHub CLI and work best with Linear, Slack, and PostHog MCP integrations; they degrade gracefully with GitHub alone.
- Everything is local Markdown, but the agent's API is still called when a skill runs; the README states no data is stored on external servers.

## Related

[Claude Obsidian - Self-Organizing Second Brain Setup](/hermes/skills/catalog/claude-obsidian-setup) | [Supermemory Skills - Agent Memory API Suite](/hermes/skills/catalog/supermemory-skills-setup) | [Letta Skills - Shared Agent Knowledge Base Setup](/hermes/skills/catalog/letta-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run onboarding first; it writes the profile, interests and watchlist files the daily skills read.
- Install skills-only with npx skills add huytieu/COG-second-brain if you want the skills without cloning the full vault.
- Keep personal content in the numbered vault folders; update-cog and ./cog-update.sh never touch those files.
- Start team skills with GitHub alone, then add Linear, Slack, and PostHog MCP integrations as needed.
- Turn the verification harness on per request (or with verification_harness: on in 00-inbox/MY-PROFILE.md) rather than running every build through it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
