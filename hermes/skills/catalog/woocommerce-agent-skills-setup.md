---
title: "WooCommerce Agent Skills - Store Development"
description: "woocommerce/woocommerce: 6.2K combined installs across 12 listings, official WooCommerce monorepo skills for backend, review and workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/woocommerce-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "woocommerce", "wordpress", "php"]
---

# WooCommerce Agent Skills - Setup Guide

**Source:** [woocommerce/woocommerce](https://www.skills.sh/woocommerce/woocommerce) via skills.sh - 6.2K combined installs across 12 indexed listings; first seen Nov 14, 2026 (this sweep)
**GitHub:** 10,599 stars, GPL-2.0 license, `trunk` branch, last pushed 2026-11-14, 11 `SKILL.md` files in `.ai/skills/<name>/`
**Category:** WooCommerce / WordPress commerce agent skills
**Quality Tier:** 🟡 Yellow - Snyk flags one sampled skill (woocommerce-code-review) with Warn.

The official WooCommerce monorepo ships agent skills for its own development workflow, stored under `.ai/skills/<name>/`. They cover backend PHP, code review, performance, the dev cycle (tests, linting, quality checks), copy guidelines and the Store API, plus a set of git-workflow helpers for commits and draft PRs.

Because the branch is `trunk` rather than `main` and the repo is a full plugin monorepo of 14,520 files, every raw URL below uses `trunk`, and the skill-level verdicts do not cover the codebase at large. The skills encode the project's own conventions, so an agent contributing to WooCommerce gets the maintainers' rules rather than a generic PHP checklist.

## Installation

The README getting-started prepares the monorepo for development:

```bash
pnpm install --frozen-lockfile
pnpm build
```

It does not document a `npx skills` command for the agent skills, so install them explicitly:

```bash
npx skills add woocommerce/woocommerce --skill 'woocommerce-backend-dev' -g
```

Install the full set with `--skill '*'` instead of a single name.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| woocommerce-backend-dev | 2,363 | Add or modify WooCommerce backend PHP code following project conventions. |
| woocommerce-code-review | 1,851 | Review WooCommerce code changes for coding-standards compliance. |
| woocommerce-performance | 369 | Find performance issues in WooCommerce PHP code that loads collections of objects. |
| woocommerce-dev-cycle | 301 | Run tests, linting and quality checks for WooCommerce development. |
| woocommerce-copy-guidelines | 261 | Write UI text and copy for WooCommerce: labels, buttons and messages. |

The remaining 7 indexed listings range from 53 to 247 installs.

## Why This Matters for Hermes Agents

The skills are written by the WooCommerce maintainers for their own monorepo, so they carry the project's real rules: coding standards in code review, the copy voice in copy-guidelines, and the exact test and lint commands in dev-cycle. An agent that loads them contributes in the style the project accepts instead of whatever a generic WordPress skill assumes.

Backend-dev is the most-installed skill at 2,363 and anchors the whole set: it routes new classes, methods and conventions into the patterns the codebase already uses. The Store API skill (247 installs) scopes route work to `/wc/store/v1/*`, which is the surface headless storefronts depend on.

The monorepo framing matters for agents too: a change in WooCommerce touches plugins, packages and tools, so the skills are written against a much larger tree than a standalone plugin would be.

## Usage

| You say | What happens |
|---|---|
| "Add a feature to WooCommerce core" | Runs woocommerce-backend-dev for the PHP patterns and conventions. |
| "Review my WooCommerce PR" | Runs woocommerce-code-review against the project's coding standards. |
| "Why is this query slow?" | Runs woocommerce-performance to find expensive collection loads. |
| "Run the tests before I commit" | Runs woocommerce-dev-cycle for tests, linting and quality checks. |
| "Write a button label for this screen" | Runs woocommerce-copy-guidelines for UI copy conventions. |
| "Add a Store API route" | Runs woocommerce-store-api for `/wc/store/v1/*` endpoints. |

## Verification

Probe skills on the `trunk` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/.ai/skills/woocommerce-backend-dev/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/.ai/skills/woocommerce-code-review/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/.ai/skills/woocommerce-performance/SKILL.md
```

Skills live at `.ai/skills/<name>/SKILL.md` on `trunk`; use `trunk`, not `main`, when constructing raw URLs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| woocommerce-backend-dev | Pass | Pass | Pass |
| woocommerce-code-review | Pass | Pass | Warn |
| woocommerce-performance | Pass | Pass | Pass |
| woocommerce-dev-cycle | Pass | Pass | Pass |
| woocommerce-copy-guidelines | Pass | Pass | Pass |
| woocommerce-store-api | Pass | Pass | Pass |

Five of the six sampled skills pass all three auditors; woocommerce-code-review carries a Snyk Warn. The sample covers 6 of the 12 indexed listings.

## Limitations

- Snapshot data, verified 2026-11-14: 6,189 combined installs across 12 indexed listings; 10,599 GitHub stars; GPL-2.0; last pushed 2026-11-14. Counts drift over time.
- The repo is a full plugin monorepo (14,520 files), so the skill-level verdicts cover the skills only, not the codebase they sit inside.
- The branch is `trunk`, not `main`; every raw URL must use `trunk`.
- The index lists 12 skills but the tree holds 11 `SKILL.md` files; woocommerce-git has no matching directory in the current tree.
- The README documents monorepo build commands but no `npx skills` command; the install line above is a fallback.
- GPL-2.0 applies to the codebase; review licence obligations before redistributing derived work.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [Liquid Skills - Shopify Theme Standards and A11y Setup](/hermes/skills/catalog/liquid-skills-setup)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `trunk` in every raw URL and checkout; the default branch here is not `main`.
- Pair backend-dev with code-review for contributions so the code lands in the maintainers' expected style.
- Run dev-cycle before committing to keep tests and linting green rather than discovering failures in CI.
- Keep the git helpers (commit, draft-pr, git) scoped to WooCommerce repos; their conventions are project-specific.
- The copy-guidelines skill is worth loading for any user-facing text, even on small changes.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
