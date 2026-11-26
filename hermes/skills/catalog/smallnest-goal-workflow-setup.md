---
title: "Goal Workflow Skills - AI-Driven Dev Workflow Setup"
description: "smallnest/goal-workflow - 8.8K combined installs: AI-driven development workflow with /prd, /goal, /review-it and /ship-it skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/smallnest-goal-workflow-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "dev workflow", "claude code", "spec-driven"]
---

# Goal Workflow Skills - Setup Guide

**Source:** [smallnest/goal-workflow](https://www.skills.sh/smallnest/goal-workflow) via skills.sh - 8.8K combined installs across 20 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [smallnest/goal-workflow](https://github.com/smallnest/goal-workflow) - 302 stars, MIT license, last pushed Sep 13, 2026, master branch; 20 skill folders under skills/<name>/SKILL.md.
**Category:** Developer Workflows (Claude Code)
**Quality Tier:** 🟠 Orange - 15 of 20 listings sampled: ten pass all three checks, review-it carries a Gen Agent Trust Hub Fail plus a Socket Warn, and four others carry Warns.

smallnest/goal-workflow is an AI-driven development workflow that takes a feature from a Product Requirements Document to shipped code inside Claude Code. The pipeline runs /prd to generate the requirements document, optionally /prd-to-spec for a technical spec, then /to-issues to slice it into tickets, then /loop-it to implement each issue end-to-end with the review and ship stages. Around that core loop sit supporting skills for design documents, dependency graphs, refactoring, Go modernization, code-smell detection, and a few documentation helpers.

All 20 indexed listings have a matching skills/<name>/SKILL.md in the current tree. The default branch is master, so every raw URL in this guide uses master.

## Installation

The README documents a single command via the skills CLI:

```bash
npx skills add smallnest/goal-workflow
```

The repository also ships a Claude Code plugin manifest (.claude-plugin/plugin.json and .claude-plugin/marketplace.json), so it can be installed as a plugin in Claude Code. Skills are Markdown files under skills/<name>/SKILL.md, several with helper scripts (for example review-it/scripts/review-it and understand/understand.py).

## What It Provides

skills.sh publishes per-skill install counts for all 20 indexed listings. The 9 most-installed skills are listed below; the remaining 11 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| smell | 871 | detect architecture bad smells, complexity hotspots, and anti-patterns with a markdown report |
| prd | 551 | generate a Product Requirements Document for a new feature or project |
| humanize-it | 548 | rewrite documents to remove AI traces, with strategies aimed at Chinese text |
| modern-go | 541 | modernize Go code with version-appropriate idioms and APIs, gofix-style |
| insight-diagram | 541 | generate UML, architecture, and flowchart diagrams rendered as HTML and SVG |
| refactor | 540 | expert code refactoring from Martin Fowler's catalog without changing behavior |
| review-it | 537 | code review closeout across Claude Code, Codex, OpenCode, DeepSeek TUI, and Antigravity CLI |
| prd-to-spec | 525 | transform a PRD into a technical SPEC with architecture, API design, and data model |
| ship-it | 508 | commit, create a PR, merge, and close the issue via GitHub CLI |

The remaining 11 indexed listings range from 89 to 494 installs.

## Why This Matters for Hermes Agents

This suite encodes the whole spec-to-ship loop a coding agent otherwise improvises per task: write the requirements, turn them into a spec and a queue of vertically-sliced issues with real blocking edges, then implement, review, and ship each one. /loop-it is the standout for agent work because it fetches open issues, sorts them by dependency, implements each end-to-end, and persists progress to .loop-state.json, so an interrupted batch resumes instead of restarting. /review-it and /ship-it close the loop with automated review and gh-based commit, PR, merge, and issue closure. The refactor, modern-go, and smell skills give an agent concrete checklists for code quality rather than vague advice, and prd-to-spec plus to-design produce the design artifacts a reviewer can actually check against. The caveat is that the pipeline is built around Claude Code's built-in /goal command, so on Hermes the surrounding skills are what carry the value, and review-it holds the sample's only Fail verdict.

## Usage

| You say | What happens |
|---|---|
| Plan this feature | Uses /prd to generate a Product Requirements Document |
| Turn the PRD into a spec | Uses /prd-to-spec for architecture, API design, and data model |
| Break this into tickets | Uses /to-issues to create vertically-sliced issues with blocking edges |
| Implement all open issues | Uses /loop-it to fetch, sort, implement, review, and ship each issue with checkpoint/resume |
| Review my changes | Uses /review-it for review closeout across Claude Code, Codex, and other CLIs |
| Commit and merge this | Uses /ship-it to commit, create a PR, merge, and close the issue |
| Find code smells | Uses /smell to detect architecture anti-patterns and complexity hotspots |

## Verification

Confirm the README and a representative skill body resolve on the master branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/smallnest/goal-workflow/master/README.md | head -40
curl -sL https://raw.githubusercontent.com/smallnest/goal-workflow/master/skills/prd/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Fail and Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| smell | Pass | Pass | Pass |
| prd | Pass | Pass | Pass |
| humanize-it | Pass | Pass | Pass |
| modern-go | Pass | Pass | Pass |
| insight-diagram | Pass | Warn | Pass |
| refactor | Pass | Pass | Pass |
| review-it | Fail | Warn | Pass |
| prd-to-spec | Pass | Pass | Pass |
| ship-it | Pass | Pass | Pass |
| code-to-spec | Warn | Pass | Pass |
| note-it | Pass | Pass | Pass |
| to-issues | Pass | Pass | Warn |
| listenhub-tts | Pass | Pass | Pass |
| loop-it | Pass | Warn | Warn |
| to-design | Pass | Pass | Pass |

Across the 15 sampled skills there are 38 Pass, 6 Warn, and 1 Fail cells. Ten skills pass all three checks; review-it carries the single Fail (Gen Agent Trust Hub) plus a Socket Warn, and four other listings carry Warns (loop-it carries two; insight-diagram, code-to-spec, and to-issues one each).

## Limitations

- Snapshot data, verified Nov 25, 2026: 8,759 combined installs across 20 indexed listings; 302 GitHub stars; MIT license; last pushed Sep 13, 2026. Counts drift over time.
- The default branch is master, not main; every raw URL in this guide uses master, and scripts that assume main will 404.
- skills.sh sampled only 15 of the 20 indexed listings; article-icons, graph, design-it, understand, and walkthrough carry no published verdict.
- review-it carries the sample's only Fail verdict (Gen Agent Trust Hub) plus a Socket Warn; read its skills.sh security page before relying on the review closeout.
- The pipeline is built around Claude Code's built-in /goal command, so that stage does not transfer to other hosts; the surrounding skills are what carry over.

## Related

[Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup) | [Writing Plans + Subagent-Driven Development Setup Guide](/hermes/skills/catalog/writing-plans-subagent-development-setup) | [Sentimony Skills - Dev Workflow & Review Gates Setup](/hermes/skills/catalog/sentimony-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Begin with /prd, then use /prd-to-spec for technical design and /to-issues to slice the work into implementable tickets with blocking edges before touching code.
- /loop-it persists progress to .loop-state.json, so an interrupted issue batch resumes from where it stopped instead of restarting.
- Run /smell, /refactor, and /modern-go as code-quality gates before /ship-it commits and merges.
- Read review-it's security page on skills.sh first; it carries the sample's only Fail verdict.
- Several skills (humanize-it, insight-diagram, listenhub-tts) have Chinese-only documentation and defaults, so verify the behavior matches your workflow.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
