---
title: "Philtz JP Skills - Japanese Business Dev Suite Setup"
description: "philtzjp/skills - 12.2K combined installs: 23 canon skills for Japanese business teams, from Hono APIs and Postgres to Git flow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/philtzjp-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "japanese", "hono", "typescript"]
---

# Philtz JP Skills - Japanese Business Dev Suite Setup

**Source:** [philtzjp/skills](https://www.skills.sh/philtzjp/skills) via skills.sh - 12.2K combined installs across 23 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [philtzjp/skills](https://github.com/philtzjp/skills) - 2 stars, MIT, main branch, last pushed Nov 18, 2026; one SKILL.md per skill under .agents/skills/<name>/, with .claude/skills/<name> as relative symlinks into them.
**Category:** Japanese Business Engineering and Developer Conventions
**Quality Tier:** 🟡 Yellow - no Fail cells in the 20-skill sample; Warn cells on Socket and Snyk for api-design, data-migration, e2e-testing, commit-and-git, google-analytics, issue-branch-pr-flow and refresh-skills, plus Snyk-only Warn cells for e2etest, github and japanese-writing.

philtzjp/skills is the canon repository of context-dependent skills that Philtz members give to their AI agents, covering Claude Code, Codex CLI, GitHub Copilot and Cursor. The repository is maintained in Japanese and read by a Japanese business and engineering team; this guide is written in English, and the skill names below are kept verbatim as the repository names them. All 23 listings sit in a narrow band because the set is installed as a bundle rather than one skill at a time.

The useful structure is the split between canon and convenience. Each skill lives once under .agents/skills/<name>/SKILL.md, and the .claude/skills/<name> entries are relative symlinks into that directory. Many listings are thin wrappers that route to a consolidated skill: api-design routes to hono, commit-and-git and issue-branch-pr-flow route to github, data-migration routes to db, e2e-testing routes to e2etest, google-analytics routes to analytics, and japanese-writing routes to japanese. An agent should follow the routing rather than act on the older name.

## Installation

Skills are installed per working repository and are not committed. Manual install from the repo root:

```bash
DISABLE_TELEMETRY=1 pnpm dlx skills add philtzjp/skills -a claude-code -a codex -a cursor -s github -s japanese -s turborepo -y
```

To onboard an agent, point it at the startingpoint document and let it follow the steps there:

```bash
curl -fsSL https://raw.githubusercontent.com/philtzjp/startingpoint/main/START.md
```

The three default skills are github, japanese and turborepo. Add task-specific skills only when the work calls for them, using skill-selection to decide and refresh-skills to update. Installed skill directories (.agents/skills/, .claude/skills/) and skills-lock.json go in gitignore, not the repo.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| japanese | 544 | writing, translating, correcting and reviewing Japanese to match reader and purpose |
| api-design | 544 | API endpoint design and implementation; routes to the hono skill (use hono) |
| analytics | 544 | access analytics: Google Analytics plus Consent Mode, cookie banners and Cloudflare Web Analytics |
| db | 541 | database selection, schema, connections and migrations; Postgres via Neon, SQLite via D1, Drizzle ORM |
| data-migration | 541 | bulk data conversion and schema migration; routes to the db skill (use db) |
| cursor-hook-authoring | 541 | Cursor Cloud Agent Git hook chains, commit-msg and Co-authored-by handling |
| conventions | 541 | commit-message format checker called from the git commit-msg hook |
| e2e-testing | 540 | main user flows and UI changes; routes to the e2etest skill (use e2etest) |
| commit-and-git | 540 | commit, push, branch, merge and rebase; routes to the github skill (use github) |
| e2etest | 539 | E2E tests via agent-browser with Playwright fallback and explicit waits |
| errorpage | 537 | error responses: 404/410/301, soft 404 avoidance, RFC 9457 Problem Details |
| github | 535 | Issue to PR to merge flow, type(scope) commit messages, squash merge via bot |
| hono | 534 | Hono HTTP APIs with zod-openapi, RFC 9457 errors, Bearer auth and @hono/mcp |
| japanese-writing | 533 | Japanese commit messages, PR descriptions, docs and UI copy; routes to the japanese skill (use japanese) |
| google-analytics | 533 | Google Analytics, Consent Mode and cookie banners; routes to the analytics skill (use analytics) |
| issue-branch-pr-flow | 532 | Issue, branch, PR and merge for non-patch work; routes to the github skill (use github) |
| knowledge-elicitation | 530 | drawing out user tacit knowledge with eight interview techniques |
| m4l-project | 529 | Max for Live devices, Max JS, MIDI/Audio I/O and Ableton User Library packaging |
| refresh-skills | 523 | keeping skills current and reconciling canon, symlinks and the skill table |
| skill-escalation | 513 | proposing skill improvements back to the canon repo instead of editing local copies |
| skill-selection | 512 | choosing which skills to install, starting from the default github, japanese and turborepo set |
| turborepo | 502 | Turborepo and pnpm monorepos, apps/packages split, turbo.json tasks and caching |
| typescript-monorepo | 497 | monorepo layout and tsconfig; routes to the turborepo skill (use turborepo) |

All 23 indexed listings clear the 400-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

An agent writing code or prose for a Japanese business team inherits two things from this set: language rules and workflow conventions. The japanese and japanese-writing skills stop an agent from producing literal, over-simplified or wordy Japanese, and the github, commit-and-git and conventions skills pin down the exact commit-message format, squash-merge flow and Co-authored-by handling the team expects. For the engineering stack, hono, db and turborepo decide the API, database and monorepo shape before any code is written, which is where an agent working from general knowledge drifts fastest.

The routing layer is the part to internalise. Half the listings are wrappers that point at a consolidated skill, so an agent that opens api-design should follow it to hono rather than acting on a stale body. knowledge-elicitation is the standout for product work: it packages eight interview techniques for drawing out tacit knowledge, which a coding agent rarely carries by default. m4l-project is the odd one out, covering Max for Live devices, a reminder that this is a real organisation's canon rather than a generic toolset.

## Usage

| You say | What happens |
|---|---|
| Write this commit message in Japanese | Uses japanese-writing (routed to japanese) for tone and terminology |
| Set up the API for this service | Uses hono for OpenAPI, RFC 9457 errors and Bearer auth |
| Add analytics and a cookie banner | Uses analytics for Consent Mode and cookie-banner wiring |
| Design the Postgres schema and a migration | Uses db for Neon and D1 plus Drizzle, with data-migration routing to it |
| Create an issue, branch, PR and squash merge | Uses github for the standard Issue to PR to merge flow |
| Help me understand what the user actually needs | Uses knowledge-elicitation with interview techniques |
| Set up the monorepo with Turborepo | Uses turborepo for the apps/packages split and turbo.json tasks |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/philtzjp/skills/main/README.md | head -40
```

Confirm the Hono skill body is present before API work:

```bash
curl -sL https://raw.githubusercontent.com/philtzjp/skills/main/.agents/skills/hono/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| japanese | Pass | Pass | Pass |
| api-design | Pass | Warn | Warn |
| analytics | Pass | Pass | Pass |
| db | Pass | Pass | Pass |
| data-migration | Pass | Warn | Warn |
| cursor-hook-authoring | Pass | Pass | Pass |
| conventions | Pass | Pass | Pass |
| e2e-testing | Pass | Warn | Warn |
| commit-and-git | Pass | Warn | Warn |
| e2etest | Pass | Pass | Warn |
| errorpage | Pass | Pass | Pass |
| github | Pass | Pass | Warn |
| hono | Pass | Pass | Pass |
| japanese-writing | Pass | Pass | Warn |
| google-analytics | Pass | Warn | Warn |
| issue-branch-pr-flow | Pass | Warn | Warn |
| knowledge-elicitation | Pass | Pass | Pass |
| m4l-project | Pass | Pass | Pass |
| refresh-skills | Pass | Warn | Pass |
| skill-escalation | Pass | Pass | Pass |

The three listings outside the sample, skill-selection, turborepo and typescript-monorepo, carry no verdict cells in this sample, so check their own pages before installing them.

## Limitations

- Snapshot data, verified Nov 23, 2026: 12,225 combined installs across 23 indexed listings; 2 GitHub stars; MIT licence; last pushed Nov 18, 2026. Counts drift over time.
- The install band is flat: all 23 listings sit between 497 and 544 installs, so the table is not a popularity ranking, it reflects a set installed as one bundle.
- The README and skill descriptions are in Japanese; this guide is written in English and the Use For cells translate those descriptions.
- Several listings are wrappers that route to a consolidated skill (api-design to hono, commit-and-git and issue-branch-pr-flow to github, data-migration to db, e2e-testing to e2etest, google-analytics to analytics, japanese-writing to japanese); install the target skill rather than the wrapper.
- Three listings, skill-selection, turborepo and typescript-monorepo, sit outside the verdict sample and carry no security cells in this guide.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup](/hermes/skills/catalog/dot-skills-setup)
- [Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup](/hermes/skills/catalog/claude-mpm-skills-setup)
- [Skill From Masters - Domain Expert Methodology Suite Setup](/hermes/skills/catalog/skill-from-masters-setup)
- [Trussary Vietnamese Language - Professional Copy Setup](/hermes/skills/catalog/trussary-vietnamese-language-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Follow the routing: api-design, commit-and-git, data-migration, e2e-testing, google-analytics, issue-branch-pr-flow, japanese-writing and typescript-monorepo are wrappers; open the target skill, not the wrapper.
- Install the three defaults first (github, japanese, turborepo), then add task-specific skills only when the work calls for them.
- Install per working repo and do not commit the skill files; add .agents/skills/, .claude/skills/ and skills-lock.json to gitignore.
- When a skill disagrees with new information you find, use skill-escalation to propose the change upstream instead of editing the installed copy.
- Run refresh-skills at the start of long work to reconcile the canon, symlinks and the skill table before relying on a stale copy.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
