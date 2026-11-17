---
title: "Claude Skills Marketplace - Engineering Workflow Setup"
description: "mhattingpete/claude-skills-marketplace: 6.3K combined installs across 18 listings, engineering workflow skills for git, testing and code review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-skills-marketplace-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "software engineering", "git", "diagrams"]
---

# Claude Skills Marketplace - Setup Guide

**Source:** [mhattingpete/claude-skills-marketplace](https://www.skills.sh/mhattingpete/claude-skills-marketplace) via skills.sh - 6.3K combined installs across 18 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 695 stars, Apache-2.0 license, main branch, last pushed 2026-07-25, 18 skills across four plugin directories (engineering-workflow, visual-documentation, productivity-skills, code-operations), each at skills/<name>/SKILL.md
**Category:** Software engineering workflow skills for Claude Code
**Quality Tier:** 🟢 Green - near-clean verdicts: one Trust Hub Warn and two Socket Warns across 18 sampled skills, Snyk all Pass.

The mhattingpete/claude-skills-marketplace repository bundles Claude Code plugins for day-to-day software engineering: git automation, test fixing, code review, refactoring and a set of visual documentation skills that render flowcharts, architecture diagrams, dashboards and timelines as self-contained HTML. The 18 indexed skills sit inside four plugins and install through Claude Code's plugin marketplace.

The set is weighted toward automation. git-pushing writes conventional commits and pushes, test-fixing groups failing tests and fixes them systematically, and the code-operations plugin adds a local execution runtime that the README claims saves 90% to 99% of tokens on bulk operations across ten or more files. For an agent doing multi-file refactors or codebase documentation, the whole suite installs in one marketplace add.

## Installation

Install the full marketplace through Claude Code:

```text
/plugin marketplace add mhattingpete/claude-skills-marketplace
```

Install individual plugins instead of the whole set:

```text
/plugin marketplace add mhattingpete/claude-skills-marketplace/engineering-workflow-plugin
/plugin marketplace add mhattingpete/claude-skills-marketplace/visual-documentation-plugin
/plugin marketplace add mhattingpete/claude-skills-marketplace/productivity-skills-plugin
/plugin marketplace add mhattingpete/claude-skills-marketplace/code-operations-plugin
```

The code-operations plugin ships an execution runtime; set it up after install:

```bash
~/.claude/plugins/marketplaces/mhattingpete-claude-skills/execution-runtime/setup.sh
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| flowchart-creator | 755 | Render process flowcharts and decision trees as HTML with color-coded stages and swimlanes. |
| codebase-documenter | 595 | Generate documentation of a codebase: architecture, key components, data flow and guidelines. |
| architecture-diagram-creator | 522 | Create HTML architecture diagrams covering data flows, features and deployment. |
| file-operations | 418 | Analyze files for size, line counts, modification times and content statistics. |
| git-pushing | 412 | Stage, commit and push git changes with conventional commit messages. |
| test-fixing | 387 | Run tests and fix failures systematically using error grouping. |
| code-auditor | 344 | Audit a codebase across architecture, quality, security, performance and testing. |
| timeline-creator | 337 | Render project timelines and roadmaps with Gantt charts and milestones. |
| dashboard-creator | 337 | Create HTML dashboards with KPI cards, charts and progress indicators. |
| code-refactor | 304 | Bulk refactor code: rename identifiers and replace patterns across files. |

The remaining 8 indexed listings range from 173 to 297 installs.

## Why This Matters for Hermes Agents

The skills encode the mechanics an agent hits on every engineering task: staging and pushing work, fixing failing tests, implementing review feedback and documenting what changed. Loading them means an agent follows conventional commit formats and groups test failures before fixing, instead of improvising per task.

The visual-documentation plugin is the unusual part: flowchart-creator, architecture-diagram-creator, dashboard-creator and timeline-creator all emit self-contained HTML with no external dependencies and WCAG AA accessibility, so an agent can hand a stakeholder a readable artifact rather than a text description.

The code-operations plugin targets the token cost of bulk work: a local execution runtime runs Python against the codebase for ten-plus-file operations, which the README claims cuts 25,000 tokens of read and edit work to about 600. For Hermes agents doing cross-codebase refactors, that is the difference between a slow multi-round-trip task and a single scripted pass.

## Usage

| You say | What happens |
|---|---|
| "Push these changes" | Runs git-pushing to stage, commit with a conventional message and push. |
| "Fix the failing tests" | Runs test-fixing to group and fix failures systematically. |
| "Implement this review feedback" | Runs review-implementing to work through the comments. |
| "Draw a flowchart for our order process" | Runs flowchart-creator to render HTML with decision trees and swimlanes. |
| "Rename getUserData everywhere" | Runs code-refactor in execution mode for a bulk rename. |
| "Document this codebase" | Runs codebase-documenter for architecture, components and data flow. |

## Verification

Probe the skills on the main branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/visual-documentation-plugin/skills/flowchart-creator/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/productivity-skills-plugin/skills/codebase-documenter/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/engineering-workflow-plugin/skills/git-pushing/SKILL.md
```

Skills live at skills/<name>/SKILL.md inside one of the four plugin directories on main. Note the directory varies by skill: visual-documentation-plugin, productivity-skills-plugin, engineering-workflow-plugin or code-operations-plugin.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| flowchart-creator | Pass | Pass | Pass |
| codebase-documenter | Pass | Pass | Pass |
| architecture-diagram-creator | Pass | Pass | Pass |
| file-operations | Pass | Pass | Pass |
| git-pushing | Pass | Pass | Pass |
| test-fixing | Pass | Pass | Pass |
| code-auditor | Pass | Pass | Pass |
| timeline-creator | Pass | Pass | Pass |
| dashboard-creator | Pass | Pass | Pass |
| code-refactor | Warn | Pass | Pass |
| feature-planning | Pass | Pass | Pass |
| code-execution | Pass | Warn | Pass |
| review-implementing | Pass | Pass | Pass |
| conversation-analyzer | Pass | Pass | Pass |
| technical-doc-creator | Pass | Pass | Pass |
| ensemble-solving | Pass | Pass | Pass |
| project-bootstrapper | Pass | Pass | Pass |
| code-transfer | Pass | Warn | Pass |

The sample covers all 18 indexed listings. Fifteen pass every auditor; code-refactor carries a Trust Hub Warn and code-execution and code-transfer each carry a Socket Warn.

## Limitations

- Snapshot data, verified 2026-11-17: 6,330 combined installs across 18 indexed listings; 695 GitHub stars; Apache-2.0; last pushed 2026-07-25. Counts drift over time.
- The index lists 18 skills but the tree organizes them across four plugins plus a code execution runtime and MCP server, so skill files are not in one flat skills directory.
- The code-operations plugin's execution runtime runs Python locally against the codebase; review its sandbox and PII masking before trusting it on sensitive repos.
- The README markets 90% to 99% token savings from the execution runtime; treat that as a benchmark claim, not a guarantee.
- Last push is 2026-07-25, several months before this sweep; the suite is stable but not fast-moving.

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Sentimony Skills - Dev Workflow & Review Gates Setup](/hermes/skills/catalog/sentimony-skills-setup)
- [Caveman Skills - Agent Coding Workflow Suite Setup](/hermes/skills/catalog/caveman-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the plugin you need (for example engineering-workflow-plugin) rather than the whole marketplace when a single workflow is the goal.
- Pair git-pushing with test-fixing so commits only land after the suite is green.
- Keep the visual-documentation skills for stakeholder-facing artifacts; they emit self-contained HTML with no external dependencies.
- Use the execution runtime for ten-plus-file operations, but review its sandbox and PII masking first.
- Read the raw SKILL.md before installing to confirm the activation triggers match your workflow.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
