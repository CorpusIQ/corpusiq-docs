---
title: "tldraw Skills - Infinite Canvas SDK Setup"
description: "tldraw/tldraw - 5.1K combined installs across 28 indexed listings: skills for building and maintaining the tldraw infinite-canvas SDK."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tldraw-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "tldraw", "canvas", "sdk"]
---

# tldraw Skills - Setup Guide

**Source:** [tldraw/tldraw](https://www.skills.sh/tldraw/tldraw) via skills.sh - 5.1K combined installs across 28 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [tldraw/tldraw](https://github.com/tldraw/tldraw) - 51,584 stars, NOASSERTION license field, last pushed Nov 25, 2026, main branch; skills ship inside the SDK repository under skills/<name>/SKILL.md, with .agents/skills, .claude/skills, and .cursor/skills directories alongside.
**Category:** Infinite Canvas SDK (tldraw)
**Quality Tier:** 🟠 Orange - tldraw-migrate fails the Gen Agent Trust Hub check, and skill-creator, pr-walkthrough, write-release-notes, update-release-notes, and shepherd-pr carry Socket or Snyk warnings.

tldraw/tldraw is the repository for the tldraw infinite-canvas SDK, and its agent skills ship inside that repo rather than as a separate skills project. The 28 indexed listings are developer-workflow skills for maintaining the SDK: writing unit, E2E, and spec-driven tests, writing and reviewing docs, drafting release notes, creating examples, and shepherding pull requests. Each skill is a self-contained SKILL.md under skills/<name>/SKILL.md.

GitHub reports the license field as NOASSERTION, and the README describes the tldraw license (free to use in development, with a license key required for production), so treat the repo as source-available rather than under a standard OSI license. The skills are most directly useful to anyone contributing to tldraw or maintaining a similarly structured TypeScript monorepo.

## Installation

The skills are not published as a standalone package and the README documents no skill install command; they live in the SDK repository. To use them, clone the repo and point your agent at the skills directory, or copy the SKILL.md files into your agent's skill folder:

```bash
git clone https://github.com/tldraw/tldraw
```

Each skill is a self-contained SKILL.md under skills/<name>/SKILL.md. The repository also carries agent skill directories (.agents/skills, .claude/skills, .cursor/skills) and a .cursor-plugin/marketplace.json manifest, so the skills are wired into Claude Code, Cursor, and the Agent Skills standard when working inside the repo itself.

## What It Provides

skills.sh publishes per-skill descriptions for the indexed listings, and each listing maps to a skills/<name>/ directory in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| write-unit-tests | 508 | unit and integration tests for the SDK (Vitest, TestEditor) |
| write-docs | 496 | SDK documentation in apps/docs/content/ |
| write-example | 455 | examples for the tldraw SDK examples app |
| write-e2e-tests | 441 | Playwright E2E tests for browser and UI interactions |
| skill-creator | 440 | guidance for creating or updating agent skills |
| write-pr | 429 | pull request titles, descriptions, and pre-flight diff review |
| write-issue | 414 | GitHub issue title, body, label, and triage standards |
| review-docs | 403 | reviewing and improving SDK docs against the voice and docs guides |
| write-release-notes | 337 | release notes articles for SDK releases |
| pr-walkthrough | 231 | narrated video walkthrough of a pull request |

The remaining 18 indexed listings range from 1 to 173 installs.

## Why This Matters for Hermes Agents

tldraw is one of the most widely used React canvas SDKs, and these skills are the team's own maintenance playbook for it, published in agent-readable form. For a Hermes agent working inside a tldraw-adjacent TypeScript monorepo, they replace guesswork with the repo's real conventions: where tests live, how docs are structured, how release notes are written, and how a PR is expected to be titled and described. A task like "add tests for this function" resolves to the repo's Vitest and TestEditor patterns instead of a generic test file. The collection is cheap to review (28 listings, all Markdown SKILL.md files), and 14 of the 15 sampled skills pass every skills.sh check. The tradeoff is scope: they encode tldraw's internal workflow and paths, so their value is highest for tldraw contributors and for teams that want a worked example of agent-maintainable SDK documentation, testing, and release discipline.

## Usage

| You say | What happens |
|---|---|
| Add test coverage for this editor function | Uses write-unit-tests with Vitest and TestEditor patterns |
| Write docs for this new API | Uses write-docs to draft an article in apps/docs/content/ |
| Add a Playwright test for this UI flow | Uses write-e2e-tests to add browser coverage |
| Review my docs article for style | Uses review-docs to score and improve the article |
| Draft release notes for this version | Uses write-release-notes to structure the release article |
| Record a walkthrough of this PR | Uses pr-walkthrough to generate a narrated video |
| Create a new skill | Uses skill-creator for the skill authoring workflow |

## Verification

Confirm a representative skill body resolves on the main branch before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/tldraw/tldraw/main/skills/write-unit-tests/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/tldraw/tldraw/main/skills/write-docs/SKILL.md | head -40
```

Both URLs return 200. Review each skills/<name>/SKILL.md before use; the skills target tldraw's own paths (packages/editor, packages/tldraw, apps/docs/content).

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| write-unit-tests | Pass | Pass | Pass |
| write-docs | Pass | Pass | Pass |
| write-example | Pass | Pass | Pass |
| write-e2e-tests | Pass | Pass | Pass |
| skill-creator | Pass | Warn | Pass |
| write-pr | Pass | Pass | Pass |
| write-issue | Pass | Pass | Pass |
| review-docs | Pass | Pass | Pass |
| write-release-notes | Pass | Pass | Warn |
| pr-walkthrough | Pass | Warn | Warn |
| write-tbp | Pass | Pass | Pass |
| update-release-notes | Pass | Pass | Warn |
| shepherd-pr | Pass | Pass | Warn |
| tldraw-migrate | Fail | Pass | Pass |
| spec-driven-tests | Pass | Pass | Pass |

15 of 28 listings were sampled. 14 pass all three checks; tldraw-migrate fails the Gen Agent Trust Hub check, and skill-creator, pr-walkthrough, write-release-notes, update-release-notes, and shepherd-pr carry Socket or Snyk warnings.

## Limitations

- Snapshot data, verified Nov 25, 2026: 5,085 combined installs across 28 indexed listings; 51,584 GitHub stars; NOASSERTION license; last pushed Nov 25, 2026. Counts drift over time.
- GitHub reports NOASSERTION for the license field; the README describes the tldraw license (free in development, a license key required for production), not a standard OSI license.
- The skills ship inside the SDK repository, so they are scoped to tldraw's own maintenance workflows rather than general canvas-app authoring.
- The repository states it is not accepting contributions at this time, so the skills evolve with the SDK rather than as a community package.
- Each skill is a Markdown SKILL.md with no bundled scripts; the skill paths reference tldraw-specific directories (packages/editor, packages/tldraw, apps/docs/content).

## Related

[Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup) | [KV0906 CC Skills - Design and Diagram Agent Suite Setup](/hermes/skills/catalog/kv0906-cc-skills-setup) | [excalidraw - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/excalidraw-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Clone the repo and point your agent at skills/ to get the maintenance workflows without a separate install.
- Pair write-unit-tests with write-e2e-tests for coverage, and write-docs with review-docs for documentation.
- Read skills/<name>/SKILL.md before relying on a skill; each encodes tldraw's repo-specific conventions.
- Check the license before production use: development is free, production requires a license key.
- Adapt the patterns to another TypeScript monorepo by swapping the tldraw-specific paths.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
