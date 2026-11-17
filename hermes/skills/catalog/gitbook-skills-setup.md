---
title: "GitBook Skills - Docs Authoring, Review, and OpenAPI Setup"
description: "gitbookio/gitbook-skills - 4.4K combined installs across 6 indexed listings: six skills for authoring, configuring, and reviewing GitBook docs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gitbook-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "documentation", "openapi"]
---

# GitBook Skills - Setup Guide

**Source:** [gitbookio/gitbook-skills](https://www.skills.sh/gitbookio/gitbook-skills) via skills.sh - 4.4K combined installs across 6 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 27 stars, MIT license, `main` branch, last pushed 2026-11-13, six skills under `skills/<name>/` with a `references/` folder each
**Category:** Documentation tooling - GitBook authoring, configuration, and change requests
**Quality Tier:** 🟠 Orange - write-openapi fails Snyk and the two change-request skills carry Snyk warnings among the 6 sampled.

GitBook publishes six skills that let coding agents work with GitBook docs entirely outside the GitBook UI. `write-docs` authors Git-synced pages and GitBook blocks such as hints, tabs, steppers, and cards. `configure-site` scaffolds and configures whole sites through the REST API or MCP, from structure design through branding. `write-openapi` turns OpenAPI and Swagger specs into interactive API reference pages with the Test it runner. `cr-create` and `cr-review` are the two halves of a change-request loop over the raw REST API with curl, and `build-integration` scaffolds custom blocks, ContentKit UI, events, and OAuth apps.

The repo doubles as a plugin for Claude Code, Cursor, OpenAI Codex, and Grok, and ships an eval suite for each skill. The skills follow the Agent Skills format.

## Installation

With the skills CLI:

```sh
npx skills add GitbookIO/gitbook-skills
```

The installer is interactive; run it non-interactively when an agent installs on your behalf, or it hangs waiting for input:

```sh
npx -y skills add GitbookIO/gitbook-skills -y
```

Or in Claude Code 2.1.275 or later:

```sh
/plugin install gitbook --marketplace GitbookIO/gitbook-skills
```

Or by hand: copy `skills/<name>/` into your agent's skills directory, for example `.claude/skills/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| write-docs | 807 | Author and edit GitBook-flavored Markdown pages, blocks, frontmatter, and variables. |
| configure-site | 732 | Create and configure GitBook sites end to end via the REST API or MCP. |
| cr-review | 722 | Discover and comment on change requests over the raw REST API. |
| cr-create | 721 | Create change requests, push content, request review, and fix comments via curl. |
| write-openapi | 702 | Author and publish OpenAPI reference docs with the interactive Test it runner. |
| build-integration | 667 | Build and publish GitBook integrations with custom blocks, events, and OAuth. |

All 6 indexed listings appear in the table above; none sits below 500 installs.

## Why This Matters for Hermes Agents

For a Hermes agent that produces documentation, this suite removes the GitBook UI from the loop. `write-docs` covers the GitBook-flavored Markdown dialect, including blocks and frontmatter, so an agent can author pages that render correctly the first time. `configure-site` automates the tedious half of standing up a docs site: designing structure, scaffolding a Git monorepo, driving the API to create sites and spaces, and applying branding, leaving only the one Git Sync step GitBook does not expose programmatically. The `cr-create` and `cr-review` pair gives an agent a full docs change-request workflow over plain curl, which matters when no CLI is available. `write-openapi` turns a spec into interactive reference pages and exposes the `x-*` extensions agents rarely get right from memory. The site-level Git Sync preference is a concrete, opinionated default that avoids the per-space sprawl most agents would otherwise produce.

## Usage

| You say | What happens |
|---|---|
| "Create a new GitBook site for my product" | configure-site designs the structure, scaffolds the repo, creates the site and spaces, and hands off Git Sync. |
| "Write a Getting Started page with a stepper and tabs" | write-docs authors the page with GitBook blocks, hints, and tabs. |
| "Add an OpenAPI reference from this spec URL" | write-openapi generates the reference pages and wires the Test it runner. |
| "Open a change request and push my edits" | cr-create creates the CR, pushes content, requests review, and notifies Slack. |
| "What change requests are waiting on me?" | cr-review lists CRs, summarizes what changed, and lets you comment or approve. |
| "Add a custom block to our GitBook site" | build-integration scaffolds the integration, its manifest, and the ContentKit UI. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/gitbookio/gitbook-skills/main/skills/write-docs/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/gitbookio/gitbook-skills/main/skills/configure-site/SKILL.md | head -20
npx skills add GitbookIO/gitbook-skills
```

Each skill is one `SKILL.md` under `skills/<name>/` with a `references/` folder; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| write-docs | Pass | Pass | Pass |
| configure-site | Pass | Pass | Pass |
| cr-review | Pass | Pass | Warn |
| cr-create | Pass | Pass | Warn |
| write-openapi | Pass | Pass | Fail |
| build-integration | Pass | Pass | Pass |

All 6 skills pass the Gen Agent Trust Hub and Socket; write-openapi fails Snyk and the two change-request skills carry Snyk warnings.

## Limitations

- Snapshot data, verified Nov 16, 2026: 4,351 combined installs across 6 indexed listings; 27 GitHub stars; MIT; last pushed 2026-11-13. Counts drift over time.
- The 27-star repository carries less community vetting than larger catalogs.
- write-openapi fails Snyk, and cr-create and cr-review carry Snyk warnings, so check the scanner pages before relying on them.
- configure-site hands off Git Sync as a manual step because GitBook does not expose it programmatically.
- The installer is interactive and hangs waiting for input without the -y flags; agents installing on your behalf need them.

## Related

- [EventCatalog Skills](/hermes/skills/catalog/event-catalog-skills-setup)
- [Academic Writing Skills](/hermes/skills/catalog/academic-writing-skills-setup)
- [Plannotator](/hermes/skills/catalog/plannotator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the installer non-interactively with `npx -y skills add GitbookIO/gitbook-skills -y`; without the flags it hangs waiting for input.
- Prefer site-level Git Sync (a `gitbook-docs.yaml` mapping every space) over per-space sync unless a space needs its own repo.
- Use `write-docs` for page authoring and `configure-site` for structure; the two are deliberately split.
- Treat `configure-site/references/example-site` as a working template for structure, vars, and summaries.
- The OpenAPI skill triggers on GitBook plus OpenAPI even when the user does not name it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
