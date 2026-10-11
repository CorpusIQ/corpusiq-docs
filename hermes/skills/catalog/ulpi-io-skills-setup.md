---
title: "ulpi Skills - Browse, SEO & Dev Utilities Setup"
description: "Setup guide for ulpi-io/skills - 10.7K combined installs. 60 skills: stealth browsing, SEO/AEO/GEO audits, Laravel toolkit, dev workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ulpi-io-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "seo", "developer workflow"]
---

# ulpi Skills - Setup Guide

**Source:** [ulpi-io/skills](https://www.skills.sh/ulpi-io/skills) via skills.sh - 10.7K combined installs across 60 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [ulpi-io/skills](https://github.com/ulpi-io/skills) (5 stars, NO LICENSE FILE; pushed 2026-08-31; layout: one top-level directory per skill, such as `frontend-design-ui-ux/SKILL.md`)
**Category:** Web Tooling / SEO / Dev Workflow
**Quality Tier:** 🟡 Beta - 60-skill toolkit; NO LICENSE file; browse tooling notable; mixed sampled verdicts - see Security

ulpi-io publishes a 60-skill toolkit for AI coding agents, and its identity comes from the browse family. `browse` is a persistent headless Chromium daemon with 76+ commands and ref-based interaction; its README claims 13x fewer tokens than `@playwright/mcp` because every action returns a one-line result instead of dumping page context. The set reaches 10.7K combined installs across 60 indexed listings, led by `frontend-design-ui-ux` at 2,393 installs, and covers stealth browsing (`browse-stealth` via the camoufox runtime, with Turnstile and DataDome bypass plus proxy rotation), SEO/AEO/GEO/QA audits driven through the same browser, and `codemap` for code search and architecture analysis.

The rest is a complete dev-workflow loop: `cost-estimate` (299 installs) for costing a repo or branch, `code-simplify` (185) and `branch-review-before-pr` (166) for review, `bugfix` (175) for red-green fixes, `find-bugs` (168) for a security pass on a diff, git skills (`commit`, `create-pr`, `git-merge-expert`, plus a worktree variant at 159), learnings-propagation skills, and framework references for Laravel, Filament, Next.js, Node.js, NestJS, Rust, and Docker. The launch-* family prepares Product Hunt, Hacker News, X, and LinkedIn launches as composable skills. One caveat up front: the repository carries NO LICENSE FILE.

---

## Installation

Prerequisites: Node.js for the `npx` skills CLI. The browse skills need extra global installs: `npm install -g @ulpi/browse` for the browser daemon, and `npm install camoufox-js && npx camoufox-js fetch` for `browse-stealth`.

```bash
# Install the full suite
npx skills add https://github.com/ulpi-io/skills

# Or a single skill (recommended for this toolkit)
npx skills add https://github.com/ulpi-io/skills --skill browse
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| frontend-design-ui-ux | 2,393 | Locked design language and UX/UI spec in `.ulpi/design`: anti-slop rules, browse-driven inspiration, design-system routing, a11y; delegates the build (no code) |
| laravel-filament | 431 | Filament v5 admin panels: resources, schemas, tables, actions, widgets, and the v3-to-v5 migration |
| cost-estimate | 299 | Estimate the dev cost of a repo, branch, or commit |
| browse | 272 | Headless browser CLI: 76+ commands, ref-based interaction, 13x fewer tokens than @playwright/mcp |
| code-simplify | 185 | Review code for reuse, quality, and efficiency |
| git-merge-expert | 182 | Merge branches, resolve conflicts, and roll back |
| nextjs | 181 | Installed-version-aware Next.js App Router reference: i18n, trusted data access, public-page contracts |
| bugfix | 175 | Red-green bug fixing: reproducer, root cause, minimal fix, regression tests |
| map-project | 174 | Generate CLAUDE.md from a codebase scan |
| plan-founder-review | 169 | Technical founder review of a plan before execution |
| find-bugs | 168 | Security audit and bug finding on a branch diff |
| plan-to-task-list-with-dag | 167 | Decompose features into parallel-ready task DAGs |
| branch-review-before-pr | 166 | Structural review before a PR: race conditions, trust boundaries |
| codemap | 164 | Code search and architecture analysis: hybrid vector/BM25, dependency graphs, PageRank |
| update-claude-learnings | 162 | Extract behavioral learnings into CLAUDE.md |
| update-agent-learnings | 160 | Propagate learnings to agent files |
| map-project-monorepo | 160 | Per-package CLAUDE.md for monorepos |
| nodejs | 159 | Node.js/Bun backend reference: TS-first, pino, Zod, async, queues, testing |
| git-merge-expert-worktree | 159 | Isolated merges in git worktrees |
| commit | 158 | Smart conventional commits, pre-commit checks, secret scanning |
| update-skill-learnings | 155 | Propagate learnings into skill files |
| create-pr | 155 | Auto-generate PR title and body, push, create via gh |
| start | 151 | Session init: discover skills, select agent persona |

The remaining 37 indexed listings range from 51 to 149 installs. The browse family continues just below the table line: browse-qa (146), browse-stealth (125), browse-seo (109), browse-aeo (109), browse-geo (109), and browse-config (106), while the launch-* set sits at 51 to 54 installs each.

## Why This Matters for Hermes Agents

Most agent browser integrations are context sinks: Playwright MCP dumps roughly 16K tokens per action, while `browse` returns a one-liner (the README's example session runs about 12K tokens over 10 steps versus 146K, 13x less). For a Hermes agent that reads pages, fills forms, or scrapes structured data, that ratio decides whether a long session stays usable. The audit skills point the same browser at SEO, AEO, and GEO surfaces, which is where discoverability is increasingly decided. `codemap` gives the agent hybrid vector/BM25 search plus dependency graphs and PageRank when a repo is too large to read directly. The dev-workflow cluster covers a full loop: cost the work, plan it as a task DAG, review the branch against race conditions and trust boundaries, fix with red-green discipline, and merge cleanly. Two caveats belong up front: the repository has no license file, and the sampled verdicts are mixed (a Snyk Warn on frontend-design-ui-ux, a Socket Warn on laravel). `browse-stealth` exists to get around bot detection, which can conflict with site terms of service; treat it as a tool for sites you are allowed to automate.

## Usage

| You say | What happens |
|---|---|
| "Audit this landing page for SEO and fix the meta tags" | browse-seo runs the on-page audit: meta tags, headings, schema, Core Web Vitals, mobile rendering |
| "Check how my brand shows up in AI search" | browse-aeo audits answer-engine surfaces and browse-geo monitors generative-engine visibility |
| "Open this site and pull the product listing data" | browse drives the persistent Chromium daemon with @ref-based interaction and one-line outputs |
| "Review this branch before I open a PR" | branch-review-before-pr checks race conditions and trust boundaries; find-bugs adds a security pass on the diff |
| "Turn this feature plan into parallel work" | plan-to-task-list-with-dag decomposes the feature into a task DAG |
| "Fix this bug with a proper reproducer" | bugfix runs the red-green loop: reproduce, root-cause, minimal fix, regression tests |
| "Merge this branch and resolve the conflicts" | git-merge-expert merges, resolves conflicts, and can roll back; the worktree variant does it in isolation |

## Verification

```bash
# Confirm the suite installed (paths depend on your agent)
npx skills list | grep -i ulpi

# Review the top skill straight from GitHub before installing (returns 200)
curl -s https://raw.githubusercontent.com/ulpi-io/skills/main/frontend-design-ui-ux/SKILL.md | head -20

# Smoke-test the browse daemon after the global install
browse goto https://example.com
```

If `browse` returns a one-line navigation result, the daemon is up; if not, reinstall `@ulpi/browse` globally. For `browse-stealth`, confirm camoufox fetched its runtime during install.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frontend-design-ui-ux | Pass | Pass | Warn |
| laravel | Pass | Warn | Pass |
| vue | - | - | - |

Two of the three sampled skills carry a Warn on one engine each: frontend-design-ui-ux on Snyk, laravel on Socket. vue returned no verdict data. Only three skills were sampled out of 60; the browse family in particular was not sampled, so audit it directly for your use case.

## Limitations

- NO LICENSE file in the repository: there is no explicit license grant; confirm terms with the publisher before commercial use.
- Mixed security profile: frontend-design-ui-ux has a Snyk Warn and laravel a Socket Warn in the sampled set; most of the 60 skills are unsampled.
- Small repository: 5 GitHub stars, last pushed Aug 31, 2026; independent and young.
- The browse skills need separate global installs (`@ulpi/browse` daemon; camoufox for stealth), so setup is heavier than a plain skill.
- Stealth browsing (anti-detection, proxy rotation) can conflict with site terms of service; use it only where automation is permitted.
- Snapshot data, verified Oct 10, 2026: 10.7K combined installs across 60 indexed listings; 5 GitHub stars; NO LICENSE FILE; last pushed Aug 31, 2026. Counts drift over time.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup) - a lighter browser-CLI alternative to the browse daemon
- [Claude SEO - 31-Skill Universal SEO Suite Setup](/hermes/skills/catalog/claude-seo-setup) - deeper classic-SEO coverage alongside browse-seo
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup) - the GEO/AEO counterpart for AI-answer visibility
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per skill: 60 listings is a lot of context; use `npx skills add https://github.com/ulpi-io/skills --skill <name>` for just what you need.
- The browse family shares one daemon: install `@ulpi/browse` once, then use `browse goto` and `browse snapshot -i` for @ref-based interaction that returns token-light output.
- The 76+ browse commands include 150+ device emulation profiles, cookie import from real browsers, command recording, and cursor-interactive detection.
- Use codemap for architecture questions on large repos: hybrid vector/BM25 search, dependency graphs, PageRank ranking.
- The launch-* family composes: launch-copy feeds the platform skills (Product Hunt, Hacker News, X, LinkedIn) and launch-analytics handles UTM/GA4 attribution.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
