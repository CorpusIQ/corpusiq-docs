---
title: "Astro Skills - Contributor and PR Workflows Setup"
description: "withastro/astro - 3.6K combined installs: contributor skills for the Astro monorepo covering PR writing, triage, code review, merge, and changesets."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/astro-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "astro", "contributor workflows", "code review"]
---

# Astro Skills - Setup Guide

**Source:** [withastro/astro](https://www.skills.sh/withastro/astro) via skills.sh - 3.6K combined installs across 10 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [withastro/astro](https://github.com/withastro/astro) - 64,220 stars, NOASSERTION license field, last pushed Nov 26, 2026, main branch; the 10 skills live under .agents/skills/<name>/SKILL.md inside the official Astro framework monorepo.
**Category:** Framework Contributor Workflows (Astro)
**Quality Tier:** 🟡 Yellow - all 10 indexed listings sampled: no Fail verdicts, but six Warn cells (Socket and Snyk) across five skills.

withastro/astro is the official Astro framework monorepo, and these skills are its internal agent workflows for contributors rather than end-user web builders. The ten skills cover the maintainer loop: triaging bugs, writing pull requests, static code review, changesets, and merging main into next, plus two adversary-team skills used by Astro's Factory automation. Because they live inside a 7,000-plus file framework repository, they describe the Astro codebase itself (architecture, debugging, testing, comment style) and are most useful to anyone contributing to Astro, not to people building sites with Astro.

All 10 indexed listings have a matching .agents/skills/<name>/SKILL.md in the current tree. The default branch is main.

## Installation

The skills are not published as a standalone skill package; they sit in the .agents/skills/ directory of the Astro framework monorepo. The framework itself is installed with:

```bash
npm create astro@latest
```

To pull the skills via the skills.sh CLI, run `npx skills add withastro/astro`, which fetches only the skill files from .agents/skills/ rather than the whole repository. Confirm each .agents/skills/<name>/SKILL.md exists in the current tree before relying on it.

## What It Provides

skills.sh publishes per-skill install counts for all 10 indexed listings. The 8 most-installed skills are listed below; the remaining 2 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| astro-developer | 611 | guide for developing in the Astro monorepo: architecture, debugging, testing, and constraints |
| analyze-github-action-logs | 384 | analyze recent GitHub Actions workflow runs to spot patterns, mistakes, and improvements |
| triage | 381 | triage a bug report: reproduce it, diagnose the root cause, and attempt a fix |
| astro-pr-writer | 343 | write and update Astro pull requests with reviewer-friendly titles and high-signal bodies |
| astro-code-review | 326 | static, read-only code review of an Astro PR or branch against its stated requirements |
| changeset | 323 | create a changeset file to document a package version bump or changelog entry |
| merge | 320 | handle main-to-next merges: conflict resolution, changeset cleanup, and CI fix-ups |
| writing-comments | 316 | write JSDoc and inline comments in Astro source, for contributors |

The remaining 2 indexed listings range from 287 to 288 installs.

## Why This Matters for Hermes Agents

The suite encodes the maintainer loop that most projects leave to tribal knowledge: reproduce the bug, write the PR, review it read-only against its requirements, add a changeset, and merge main into next with conflict and CI cleanup. For an agent doing Astro contribution work, triage and astro-code-review are the most transferable, because they give concrete checklists for reproducing issues and deciding whether a change is merge-ready without ever running project code. astro-pr-writer and changeset encode the repository's exact PR and release conventions, which is the kind of procedural detail an agent otherwise gets wrong. The two adversary skills (purple and blue) are scoped to Astro's Factory automation and are not general-purpose; a Hermes agent would rarely use them outside that pipeline. The main caveat is that these skills are written for the Astro codebase specifically, so most of their value requires working inside that monorepo rather than building apps with Astro.

## Usage

| You say | What happens |
|---|---|
| Triage issue 1234 | Uses triage to reproduce, diagnose root cause, verify intent, and attempt a fix |
| Open a PR for this change | Uses astro-pr-writer for a reviewer-friendly title and high-signal body |
| Review this PR | Uses astro-code-review for a read-only check against its requirements |
| Add a changeset | Uses changeset to document the package version bump |
| Merge main into next | Uses merge for conflict resolution, changeset cleanup, and CI fix-ups |
| Analyze the CI failures | Uses analyze-github-action-logs to spot patterns and mistakes in workflow runs |

## Verification

Confirm the README and two representative skills resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/withastro/astro/main/.agents/skills/astro-developer/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/withastro/astro/main/.agents/skills/triage/SKILL.md | head -40
```

Both URLs return 200. After installing, review each .agents/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| astro-developer | Pass | Pass | Pass |
| analyze-github-action-logs | Pass | Pass | Warn |
| triage | Pass | Warn | Warn |
| astro-pr-writer | Pass | Pass | Pass |
| astro-code-review | Pass | Pass | Warn |
| changeset | Pass | Pass | Pass |
| merge | Pass | Pass | Pass |
| writing-comments | Pass | Pass | Pass |
| astro-adversary-purple | Pass | Pass | Warn |
| astro-adversary-blue | Pass | Pass | Warn |

Across the 10 sampled skills there are 24 Pass, 6 Warn, and 0 Fail cells. Five skills pass all three checks; triage carries two Warns (Socket and Snyk), and analyze-github-action-logs, astro-code-review, astro-adversary-purple, and astro-adversary-blue carry one each.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,579 combined installs across 10 indexed listings; 64,220 GitHub stars; NOASSERTION license field; last pushed Nov 26, 2026. Counts drift over time.
- These skills document the Astro monorepo itself, not end-user Astro app development; their value requires working inside withastro/astro.
- The skills live in one directory (.agents/skills/) of a very large framework repository, and `npx skills add` pulls only the skill files, not the rest of the codebase.
- astro-adversary-purple and astro-adversary-blue are scoped to Astro's Factory adversary teams and are not general-purpose review or QA skills.
- triage carries two Warn verdicts (Socket and Snyk); read its skills.sh security page before relying on it.

## Related

[Astro Skills - Island Architecture for Agents](/hermes/skills/catalog/astrolicious-astro-setup) | [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup) | [React Router Skills - Data and Framework Modes](/hermes/skills/catalog/react-router-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with triage to reproduce a bug before touching code; it walks diagnose, verify, and fix in order.
- astro-code-review is read-only by design and never runs tests or scripts, so it is safe to run on untrusted diffs.
- Keep astro-pr-writer and changeset paired so every PR lands with a reviewer-friendly body and a matching changeset entry.
- merge handles main-to-next tasks, including changeset cleanup and CI fix-ups, so do not hand-roll those steps.
- The two adversary skills only make sense inside Astro's Factory pipeline; skip them for general work.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
