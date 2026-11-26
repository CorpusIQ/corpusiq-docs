---
title: "Superpowers Laravel - Laravel Skills for Claude Code Setup"
description: "jpcaparas/superpowers-laravel - 7.2K combined installs: Laravel Superpowers plugin with TDD, Eloquent, queues, quality gates, and architecture skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/superpowers-laravel-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "laravel", "php", "claude code"]
---

# Superpowers Laravel - Setup Guide

**Source:** [jpcaparas/superpowers-laravel](https://www.skills.sh/jpcaparas/superpowers-laravel) via skills.sh - 7.2K combined installs across 57 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [jpcaparas/superpowers-laravel](https://github.com/jpcaparas/superpowers-laravel) - 157 stars, MIT license, last pushed Jul 2, 2026, main branch; 57 skill folders under skills/<name>/SKILL.md plus commands/, hooks/, docs/, and agents/.
**Category:** Backend Web Development (Claude Code / Laravel)
**Quality Tier:** 🟠 Orange - skills.sh publishes no security verdicts for any sampled listing: all 12 return "not parsed" on the Gen Agent Trust Hub, Socket, and Snyk.

jpcaparas/superpowers-laravel is a Laravel-focused Claude Code plugin built on the Superpowers skill framework: proven workflows for TDD, debugging, and planning, plus Laravel-specific guidance that works with or without Sail. It ships a skills library, slash commands, a SessionStart hook that detects Laravel apps (including monorepos with several apps), and Laravel 13 coverage. skills.sh indexes every skill with the laravel: plugin-namespace prefix (for example laravel:blade-components-and-layouts); the repository stores them on disk as skills/<name>/SKILL.md without that prefix, which is the plain name used in the table below.

The tree ships 120 files: 57 skill directories, a commands/ directory of thin slash-command wrappers, hooks/ with a SessionStart script, docs/, an agents/ directory, branding, and CI workflows. All 57 indexed listings have a skill directory, but seven directory names diverge from the listing names, noted in Limitations.

## Installation

Install as a Claude Code plugin from the marketplace:

```bash
# In Claude Code
/plugin marketplace add jpcaparas/superpowers-laravel
/plugin install superpowers-laravel@superpowers-laravel-marketplace
```

Verify the commands landed by running /help; you should see /superpowers-laravel:brainstorm, /superpowers-laravel:write-plan, /superpowers-laravel:execute-plan, and /superpowers-laravel:laravel-check among others. Codex support is experimental: copy the skills/ subfolders you want into your project's .claude/skills rather than installing the plugin.

## What It Provides

skills.sh publishes per-skill install counts for all 57 indexed listings. The 12 most-installed skills are listed below; the remaining 45 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| blade-components-and-layouts | 208 | Blade components and layouts |
| quality-checks | 190 | run quality gates with Pint, PHP Insights, and PHPStan |
| tdd-with-pest | 187 | test-first development with Pest or PHPUnit |
| performance-eager-loading | 180 | avoid N+1 queries via eager loading |
| eloquent-relationships | 179 | Eloquent relationships and loading |
| queues-and-horizon | 176 | background queues and Horizon dashboards |
| transactions-and-consistency | 174 | database transactions and consistency guarantees |
| performance-caching | 167 | caching strategy for faster reads |
| policies-and-authorization | 166 | authorization policies and gates |
| routes-best-practices | 164 | route organization and conventions |
| migrations-and-factories | 164 | migrations and model factories |
| form-requests | 154 | Form Request validation |

The remaining 45 indexed listings range from 37 to 147 installs.

## Why This Matters for Hermes Agents

This suite turns everyday Laravel work into repeatable, test-first procedures instead of ad hoc advice: tdd-with-pest enforces writing tests before implementation, quality-checks runs Pint, PHP Insights, and PHPStan gates, and the docs-intersection skills cover the cross-version patterns (form requests, policies, Eloquent loading, transactions, HTTP client resilience, and API resources) that are stable across Laravel 11.x through 13.x. The SessionStart hook is the differentiator for an agent: it scans a repository for every artisan entrypoint, detects the Laravel version and Sail availability per app, and marks the app in the current working directory as active, so an agent gets Sail-versus-host command guidance and only for the right app in a monorepo. The runner-selection skill plus the mandatory-workflow model means that when a skill exists for a task, using it is required rather than optional. The main gap is security signal: skills.sh has parsed no verdict for any sampled listing, so the marketplace carries no third-party trust data.

## Usage

| You say | What happens |
|---|---|
| Write this feature test-first | Uses tdd-with-pest to drive Pest or PHPUnit tests before implementation |
| Check my code quality | Uses quality-checks to run Pint, PHP Insights, and PHPStan gates |
| Brainstorm a design | Uses /superpowers-laravel:brainstorm for a Laravel-specific design discussion |
| Make an implementation plan | Uses /superpowers-laravel:write-plan to produce a step-by-step plan |
| Execute the plan | Uses /superpowers-laravel:execute-plan to implement the plan task by task |
| Fix my Eloquent queries | Uses eloquent-relationships and performance-eager-loading for relationships and N+1 fixes |
| Queue this background job | Uses queues-and-horizon for queues and Horizon dashboards |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/jpcaparas/superpowers-laravel/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/jpcaparas/superpowers-laravel/main/skills/blade-components-and-layouts/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and note that skills.sh has published no security verdict for this suite, so there is nothing to re-check on the security pages yet.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| laravel:blade-components-and-layouts | not parsed | not parsed | not parsed |
| laravel:quality-checks | not parsed | not parsed | not parsed |
| laravel:tdd-with-pest | not parsed | not parsed | not parsed |
| laravel:performance-eager-loading | not parsed | not parsed | not parsed |
| laravel:eloquent-relationships | not parsed | not parsed | not parsed |
| laravel:queues-and-horizon | not parsed | not parsed | not parsed |
| laravel:transactions-and-consistency | not parsed | not parsed | not parsed |
| laravel:performance-caching | not parsed | not parsed | not parsed |
| laravel:policies-and-authorization | not parsed | not parsed | not parsed |
| laravel:routes-best-practices | not parsed | not parsed | not parsed |
| laravel:migrations-and-factories | not parsed | not parsed | not parsed |
| laravel:form-requests | not parsed | not parsed | not parsed |

Across the 12 sampled skills there are 0 Pass, 0 Warn, and 0 Fail cells: skills.sh has not parsed a verdict for any of them, so this marketplace carries no third-party security signal.

## Limitations

- Snapshot data, verified Nov 26, 2026: 7,230 combined installs across 57 indexed listings; 157 GitHub stars; MIT license; last pushed Jul 2, 2026. Counts drift over time.
- skills.sh has parsed no verdict for any of the 12 sampled listings (all three columns read "not parsed"), so treat the suite as unaudited until you review the skills yourself.
- The tree ships 120 files total against 57 indexed listings, and all 57 listings have a skill directory, but seven directory names diverge from the listing names: eloquent-relationships is stored as eloquent-relationships-and-loading, form-requests as form-requests-and-validation, rate-limiting as rate-limiting-and-throttle, filesystem-uploads as filesystem-uploads-and-urls, ai-sdk as ai-sdk-essentials, vector-search as vector-semantic-search, and upgrade-13 as upgrade-to-laravel-13.
- Listings are indexed with the laravel: namespace prefix (and the Horizon and Nova skills carry an inner colon) that the repository drops on disk; the table above uses the plain skill names.
- Install counts sit in a narrow band from 37 to 208, consistent with one plugin unit pulling the whole skills library.

## Related

[Laravel Boost - Laravel AI Development Setup](/hermes/skills/catalog/laravel-boost-setup) | [Rails Skills - Ruby on Rails Agent Suite Setup](/hermes/skills/catalog/rails-skills-setup) | [Inertia Rails Skills - Inertia.js for Rails Setup](/hermes/skills/catalog/inertia-rails-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with runner-selection so the plugin picks Sail or host commands before any PHP or Composer run, and avoid mixing the two in one session.
- In a monorepo, cd into the app you intend to work on before starting your session so the SessionStart hook marks it as the active app.
- The README positions this suite as complementary to Laravel Boost; install both if you want MCP augmentation alongside the skills.
- Validate any skill edits with npx tsx scripts/validate_skills.ts before submitting a PR.
- When Sail is declared but its containers are not running, the plugin asks before starting them instead of silently running host commands.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
