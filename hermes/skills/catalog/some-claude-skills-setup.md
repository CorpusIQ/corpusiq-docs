---
title: "Some Claude Skills - 180+ Skill Collection Setup"
description: "Setup guide for curiositech/some_claude_skills - 27.1K combined installs. 180+ skills from Erich Owens across video, design, testing, and data."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/some-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "skill collection", "design", "video"]
---

# Some Claude Skills - Setup Guide

**Source:** [curiositech/some_claude_skills](https://www.skills.sh/curiositech/some_claude_skills) via skills.sh - 27.1K combined installs across 96 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [curiositech/some_claude_skills](https://github.com/curiositech/some_claude_skills) (244 stars, MIT license; pushed Sep 6, 2026; `.claude/skills/<name>/SKILL.md` layout)
**Category:** Skill Collection / Design / Media
**Quality Tier:** 🟡 Beta - 244-star MIT collection by Erich Owens; 180+ skills; mixed sampled verdicts - see Security

Erich Owens (ex-Meta ML engineer, 12 years, 12 patents) publishes one of the largest independent skill collections on skills.sh: a README-claimed 180+ production-ready skills for Claude Code, plus two MCP servers. The flagship listing, `video-processing-editing` at 1,310 installs, anchors a media and design cluster that includes `interior-design-expert` (987), `photo-composition-critic` (624), and `metal-shader-expert` (500). Other clusters cover engineering (testing, data pipelines, refactoring), coaching and personal development, health and neuroscience, and the meta layer that creates and orchestrates further skills.

Two naming notes matter when installing. The canonical repository is `curiositech/some_claude_skills`; GitHub redirects the `erichowens/some_claude_skills` alias used by the README's install commands to the same repository id, so both paths resolve to the same code. And the skills.sh index shows 96 listings (an API page cap) against the README's 180+ claim, so treat the index as a partial view of the collection.

---

## Installation

Plugin marketplace (the README's recommended path):

```text
/plugin marketplace add erichowens/some_claude_skills

# Install any single skill
/plugin install adhd-design-expert@some-claude-skills

# Or install the full collection
/plugin install some-claude-skills@some-claude-skills
```

Manual installation:

```bash
git clone https://github.com/erichowens/some_claude_skills.git
cp -r some_claude_skills/.claude/skills/* ~/.claude/skills/
```

Individual skills can also be browsed and downloaded as ZIP files from the project site's skills gallery. The two MCP servers (`prompt-learning-mcp` and `cv-creator-mcp`) are configured in `~/.claude/settings.json` or a project `.mcp.json`: `prompt-learning-mcp` needs Docker (Qdrant + Redis), Node.js 18+, and an OpenAI API key, while `cv-creator-mcp` needs only Node.js 18+.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| video-processing-editing | 1,310 | Video processing and editing workflows for agent-driven media tasks |
| interior-design-expert | 987 | Space planning, color theory, and lighting for interior design |
| cv-creator | 754 | ATS-optimized resumes in multiple formats; pairs with cv-creator-mcp |
| personal-finance-coach | 745 | Tax optimization and investment theory coaching |
| photo-composition-critic | 624 | Graduate-level visual aesthetics analysis for photo composition |
| pwa-expert | 523 | Progressive web app implementation guidance |
| metal-shader-expert | 500 | Real-time graphics, Metal shaders, and PBR rendering |

The remaining 89 indexed listings range from 182 to 491 installs. The index itself is capped at 96 listings against the README's 180+ claim, so the tail is deeper than skills.sh reports.

## Why This Matters for Hermes Agents

Breadth is the point: one collection spans video, design critique, frontend engineering, data, coaching, and meta-tooling, letting an agent pick a specialist voice instead of one generalist prompt. The media and design cluster is unusually strong for this category, covering video processing, photo critique, typography, color harmony, and shader work, and it pairs naturally with production content pipelines. The meta cluster (`skill-coach`, `skill-architect`, `agent-creator`, `orchestrator`) plus the `prompt-learning-mcp` server shows a maintainer who uses the collection to improve itself. Because every skill is a plain `SKILL.md` under `.claude/skills/`, the library is easy to audit, vendor, or trim to fit a context budget. Judgment is required: with 180+ skills at varying maturity, cherry-picking beats bulk installs for context economy.

## Usage

| You say | What happens |
|---|---|
| "Prep this video for publishing" | video-processing-editing walks the processing and editing workflow |
| "Critique the composition of this photo" | photo-composition-critic runs a graduate-level aesthetics analysis |
| "Redesign this room's lighting and palette" | interior-design-expert applies space planning, color theory, and lighting |
| "Tailor my resume to this job posting" | cv-creator produces an ATS-optimized version; cv-creator-mcp adds match and ATS scoring |
| "Make my prompts improve every week" | prompt-learning-mcp records feedback and optimizes prompts with APE, OPRO, and DSPy patterns |
| "Write a better skill for our team" | skill-coach guides creation of a high-quality skill through the collection's own methodology |
| "Audit the dark mode palette on this app" | dark-mode-design-expert reviews the palette against dark-mode design practice |

## Verification

```bash
# Manual installs land here; plugin installs show up in the Claude Code plugin listing
ls ~/.claude/skills/ | grep -E 'video-processing-editing|cv-creator'

# Review the layout-verified skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/curiositech/some_claude_skills/main/.claude/skills/video-processing-editing/SKILL.md | head -20
```

Individual skills are also downloadable as ZIPs from the project's skills gallery if you prefer to inspect them before installing.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-processing-editing | Warn | Warn | Pass |
| video-editing | - | - | - |
| ffmpeg | - | - | - |

The `video-processing-editing` sample scored Warn on two of three engines (Gen Agent Trust Hub and Socket), so review the skill's scripts and its ffmpeg dependencies before putting it in a production pipeline. Coverage is one skill out of 180+, so extend the check to anything you plan to run unattended.

## Limitations

- Personal-scale project: 244 stars, last pushed Sep 6, 2026; expect variable quality across 180+ skills.
- The skills.sh index is capped at 96 listings against the README's 180+ claim, so some skills have no public install counts.
- Sampled verdicts are mixed (Warn, Warn, Pass on video-processing-editing) and cover a single skill.
- The MCP servers bring their own footprint: prompt-learning-mcp needs Docker services and an OpenAI API key.
- Bulk-installing the full collection adds context overhead; the plugin flow is per-skill by design.
- Snapshot data, verified Oct 10, 2026: 27,067 combined installs across 96 indexed listings; 244 GitHub stars; MIT; last pushed Sep 6, 2026. Counts drift over time.

## Related

- [Media Use Setup - Agent Media OS for HyperFrames (182.7K installs)](/hermes/skills/catalog/media-use-setup) - the production media pipeline these skills can feed
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup) - pairs with the collection's design critique skills
- [Sleek Design Mobile Apps - AI Mobile App Design Skill Setup](/hermes/skills/catalog/sleek-design-mobile-apps-setup) - a mobile-focused design complement
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup) - broader skill-development context
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Cherry-pick with `/plugin install <skill>@some-claude-skills`; the full-collection install is convenient but pays context rent on every run.
- The `erichowens` alias in the README's commands and the canonical `curiositech` repo are the same repository; either path works.
- Browse the project's skills gallery before installing: categories, descriptions, and ZIP downloads make triage faster than reading raw SKILL.md files.
- Pair `cv-creator` with `cv-creator-mcp` for ATS scoring and keyword optimization instead of editing resumes by hand.
- Skip `prompt-learning-mcp` unless you want the Docker footprint; the `automatic-stateful-prompt-improver` skill covers lighter prompt tuning.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
