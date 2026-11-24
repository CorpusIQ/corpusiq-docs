---
title: "FuDesign2008 Open Skills - Jira, Git and Workflow Setup"
description: "fudesign2008/open-skills - 4.6K combined installs: 87 agent skills for Jira, Git, debugging and workflow discipline."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fudesign-open-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "jira", "git", "workflow"]
---

# FuDesign2008 Open Skills - Jira, Git and Workflow Setup

**Source:** [fudesign2008/open-skills](https://www.skills.sh/fudesign2008/open-skills) via skills.sh - 4.6K combined installs across 87 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [fudesign2008/open-skills](https://github.com/fudesign2008/open-skills) - 6 stars, MIT license, main branch, last pushed Nov 23, 2026; one SKILL.md per skill under skills/<name>/SKILL.md, plus .claude/agents/ and OpenSpec helper skills under .claude/skills/.
**Category:** Developer Workflows and Engineering Discipline
**Quality Tier:** 🟠 Orange - jira-fix-workflow, solve-workflow and opsx-jira-fix-workflow each carry a Snyk Fail cell; six more sampled skills carry Warn cells and the rest pass.

FuDesign2008's open-skills is a broad library of 87 agent skills centered on Jira bug-fix workflows, Git release and commit discipline, and systematic debugging. The most distinctive pieces are the two staged workflow families: jira-fix-workflow and solve-workflow run end-to-end processes with a manual mode that pauses for confirmation at each stage, and their OpenSpec-flavored counterparts (opsx-jira-fix-workflow, opsx-solve-workflow) persist decisions into OpenSpec change artifacts instead of leaving them only in chat context. Around those sit Git helpers, debugging toolkits, TypeScript checks, article writing, web research and a set of engineering discipline gates.

The library is MIT-licensed but young: 6 GitHub stars and first catalogued Nov 24, 2026. Its install distribution is a long thin tail, with the top listing at 98 installs and the bottom at 1, so treat the tail as exploratory rather than battle-tested. Several skills trigger on Chinese phrases alongside English, and the README is offered in both English and Chinese.

## Installation

The README recommends a non-interactive global install via git clone and the bundled installer script:

```bash
git clone https://github.com/FuDesign2008/open-skills.git
cd open-skills
node scripts/install-skills.mjs
```

Or install through the skills.sh CLI for a single agent:

```bash
npx skills add FuDesign2008/open-skills -g
```

Update later with:

```bash
npx skills update
```

The repo does not ship slash commands, hooks, or marketplace plugins.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| jira-fix-workflow | 98 | end-to-end Jira bug-fix workflow from a Jira link through merge and writeback |
| solve-workflow | 96 | eight-stage PDCA problem solving for bugs, refactors and features |
| opsx-solve-workflow | 95 | OpenSpec-flavored PDCA workflow that persists decisions to OpenSpec artifacts |
| opsx-jira-fix-workflow | 94 | OpenSpec-flavored Jira fix workflow with behavioral-contract traceability |
| typescript-check | 93 | TypeScript type checking when tsc errors or type issues appear |
| android-webview-debug | 93 | toggling Android WebView remote debugging on and off across a project |
| git-commit | 92 | unified git commit entry point that writes commit messages |
| jira-read | 91 | reading Jira issue data from cache or API and downloading attachments |
| think-big | 90 | strategic thinking on whether something is worth doing and its risks |
| git-release-start | 89 | creating release branches with consistent naming across repos |
| unbox-anything | 88 | unpacking archives, installers, app bundles and nested containers |
| git-conflict-resolve | 88 | resolving Git merge and rebase conflicts with semantic analysis |
| article-writer | 87 | writing technical articles for blogs and self-media from existing docs |
| test-guide-from-code | 86 | generating a manual test guide for human testers from a diff or MR |
| effective-web-research | 86 | routed web research with source-credibility checks and browser escalation |
| solution-review | 85 | reviewing a proposed solution (name-level) |
| go-deploy | 85 | deploying Go services (name-level) |
| git-release-finish | 84 | finishing and closing a release branch (name-level) |
| essence-diagnosis | 83 | diagnosing the core of a problem (name-level) |
| multi-agent-debate | 82 | running a multi-agent debate to stress-test a decision (name-level) |
| browser-debug-toolkit | 82 | debugging browser issues with a toolkit (name-level) |
| hybrid-debug | 81 | hybrid debugging (name-level) |
| runtime-evidence-debug | 80 | debugging from runtime evidence (name-level) |
| code-design-review | 80 | reviewing code design (name-level) |

The remaining 63 indexed listings range from 1 to 78 installs.

## Why This Matters for Hermes Agents

The staged workflow skills are a working reference for governed agent execution: they default to a manual mode that pauses for confirmation at each stage, and the OpenSpec-flavored variants write decisions into versioned change artifacts for later review. Both patterns map directly onto how a Hermes agent should run non-trivial tasks with checkpoints and an audit trail instead of a single autonomous burst. The discipline skills are reusable guardrail patterns such as merge discipline, test-first discipline and completion-evidence discipline that can be studied and adapted for local rules. The debugging toolkits browser-debug-toolkit, hybrid-debug and runtime-evidence-debug show an evidence-first approach, insisting on observable proof before concluding a fix. The library is small and young (6 stars, a long thin install tail), so the best use is as a pattern library to learn from, with the handful of higher-install workflow skills worth actually installing. The MIT license keeps the reading and adaptation low-friction.

## Usage

| You say | What happens |
|---|---|
| Fix this Jira bug (URL) | jira-fix-workflow drives the intake-to-writeback loop with confirmations between stages |
| Resolve this merge conflict | git-conflict-resolve analyzes the conflict and suggests a semantic resolution |
| Create a release branch | git-release-start creates release/X.Y.Z branches with consistent naming |
| Run a type check on this TypeScript project | typescript-check runs the type-check workflow and reports errors |
| Unbox this installer file | unbox-anything unpacks the container into a manifest-tracked directory |
| Write a test guide from this MR | test-guide-from-code generates a manual test guide from the diff |
| Do strict research on this topic | effective-web-research runs a source-credibility evaluated research pass |

## Verification

After installing, confirm the skill directories landed under the agent skills directory, then review one raw SKILL.md before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/FuDesign2008/open-skills/main/skills/jira-fix-workflow/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| jira-fix-workflow | Pass | Pass | Fail |
| solve-workflow | Pass | Warn | Fail |
| opsx-solve-workflow | Pass | Pass | Warn |
| opsx-jira-fix-workflow | Pass | Pass | Fail |
| typescript-check | Pass | Pass | Pass |
| android-webview-debug | Pass | Pass | Pass |
| git-commit | Pass | Pass | Pass |
| jira-read | Pass | Warn | Warn |
| think-big | Pass | Pass | Pass |
| git-release-start | Pass | Pass | Pass |
| unbox-anything | Pass | Pass | Warn |
| git-conflict-resolve | Pass | Pass | Pass |
| article-writer | Pass | Pass | Warn |
| test-guide-from-code | Pass | Warn | Warn |
| effective-web-research | Pass | Warn | Warn |

Three sampled skills carry a Snyk Fail cell (jira-fix-workflow, solve-workflow, opsx-jira-fix-workflow), and six more carry Warn cells. Every sampled skill passes the Gen Agent Trust Hub check.

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,559 combined installs across 87 indexed listings; 6 GitHub stars; MIT license; last pushed Nov 23, 2026. Counts drift over time.
- The install distribution is a long thin tail: the top listing has 98 installs and the bottom 1, so most skills are exploratory rather than battle-tested.
- Per-skill descriptions cover only 15 of the 87 listings, so the other 72 (including nine that appear in the table above) are name-level and grounded only in the skill name.
- Several skills use Chinese trigger phrases alongside English, which can limit auto-triggering in English-only agent setups.
- The repo ships an additional set of OpenSpec helper skills under .claude/skills/ beyond the main skills/ directory.

## Related

- [Git PR Review (skills.sh) - Automated PR description](/hermes/skills/catalog/git-pr-review-skills-sh-setup)
- [Code Review Skill - 20+ Language Review Guides](/hermes/skills/catalog/code-review-skill-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)
- [Cron Design Workflow - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/cron-design-workflow-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the specific skills you need; the full 87-skill tree is too much to add to every agent.
- Choose the OpenSpec-flavored variants (opsx-*) when you need an audit trail, and the plain workflows for quick fixes.
- Read a skill's SKILL.md triggers before relying on auto-triggering, since several are Chinese-phrase gated.
- Treat the sub-20-install tail as reference patterns to study, not tested behavior.
- Use the git-clone plus install-skills.mjs path for a non-interactive global install.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
