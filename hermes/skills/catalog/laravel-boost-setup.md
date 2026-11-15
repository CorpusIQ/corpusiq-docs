---
title: "Laravel Boost - Laravel AI Development Setup"
description: "laravel/boost: 3.3K combined installs across 3 listings, the official Laravel package that installs agent skills, guidelines and MCP tools into a project."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/laravel-boost-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "laravel", "php", "livewire"]
---

# Laravel Boost - Setup Guide

**Source:** [laravel/boost](https://www.skills.sh/laravel/boost) via skills.sh - 3.3K combined installs across 3 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 3,691 stars, MIT license, `main` branch, last pushed 2026-11-14, five skill directories under `.ai/` (Laravel, Pennant, two Tailwind versions and deployments)
**Category:** Laravel and PHP application development
**Quality Tier:** 🟢 Green - both sampled skills pass all three auditors.

Laravel Boost is the framework's own answer to agent-assisted development. It is a Composer package rather than a skill repository, and that changes the install story: the skills arrive as part of your application's dependencies, and the same package registers MCP tooling and version-aware guidelines that read the project it is installed into.

The skills themselves live under `.ai/` in the package, one directory per topic: `laravel-best-practices`, `pennant-development`, `tailwindcss-development` for Tailwind 3 and 4, and `deploying-to-cloud`. Because the package version is pinned in `composer.json`, the guidance an agent reads matches the framework version the application actually runs.

## Installation

Add the package to an application's development dependencies, then run the installer:

```bash
composer require laravel/boost --dev
php artisan boost:install
```

The installer writes the skill files and guidelines into the project and asks which agents to configure. Keep the package current with `boost:update`, which refreshes the generated guidance after a framework upgrade.

The package requires PHP 8.2 or later, `illuminate` components from Laravel 12.41 or 13, and pulls in `laravel/mcp` for its MCP surface.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| laravel-best-practices | 2,500 | Laravel application code: conventions, structure and framework-specific patterns for the version in use. |
| livewire-development | 487 | Livewire component work, from the same package's skill set. |
| test-skill | 274 | The package's own test fixture, indexed on skills.sh as a listing. |

The remaining 2 indexed listings range from 274 to 487 installs.

## Why This Matters for Hermes Agents

Most skill collections teach a framework in the abstract. Boost installs into the application, which means the guidance the agent reads is generated from the installed package versions: a Laravel 13 project gets Laravel 13 rules, and the Tailwind skill that lands is the one matching the application's major version rather than the newest one.

For a Hermes agent working in a PHP codebase, this removes a category of confidently wrong advice. Framework conventions change between majors, and a model trained on an older release will happily apply retired patterns. Boost's version detection closes that gap without the agent having to infer the version from a lockfile.

The MCP surface is the second half. The package ships `laravel/mcp`, so the project can expose its own tools to the agent alongside the skills, which is the pattern this catalog recommends for project-specific capabilities: put the read-only knowledge in skills and the live queries behind a tool.

One caveat worth knowing before you install: `test-skill` is the package's test fixture and appears in the install index with real counts. It is not a skill you want an agent to add.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a resource controller for invoices" | Applies the Laravel best-practices skill for the installed framework version. |
| "Convert this component to Livewire" | Uses the Livewire skill for component structure and state handling. |
| "Style this view with Tailwind" | Picks the Tailwind 3 or 4 skill that matches the project's installed major version. |
| "What do I need before deploying to Laravel Cloud" | Uses the deploying-to-cloud skill for the pre-flight steps. |
| "Should this be a feature flag?" | Uses the Pennant skill for flag definition and rollout patterns. |
| "Upgrade Laravel and refresh the guidance" | Runs `php artisan boost:update` so the generated skills match the new version. |

## Verification

Check the package and the generated skill directories after install:

```bash
composer show laravel/boost
curl -fsSL https://raw.githubusercontent.com/laravel/boost/main/.ai/laravel/skill/laravel-best-practices/SKILL.md | head -20
php artisan boost:install --help
```

The skill files ship inside the package at `.ai/<topic>/skill/<slug>/SKILL.md`, so a raw path that starts at the repository root without `.ai/` will 404.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| laravel-best-practices | Pass | Pass | Pass |
| test-skill | Pass | Pass | Pass |

Boost is a first-party Laravel package with a published security policy, installed through Composer like any other dependency. The installer writes files into your application, so review the diff on first install as you would for any package that generates configuration.

## Limitations

- Snapshot data, verified 2026-11-14: 3,261 combined installs across 3 indexed listings; 3,691 GitHub stars; MIT; last pushed 2026-11-14. Counts drift over time.
- It is not a standalone skill repository. There is no `npx skills add` path here: the skills only arrive through the Composer package inside a Laravel application.
- The package requires PHP 8.2 or later and Laravel 12.41 or 13, so older applications cannot use it.
- `test-skill` is a fixture from the package's test suite. It carries install counts on skills.sh but is not a usable skill.
- The listing count is small because the package publishes five topic skills, not a large library. Coverage beyond the framework itself comes from the community.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the installer, then commit the generated files: the diff shows exactly which rules and skills the agent will follow.
- Re-run `php artisan boost:update` after every framework major, rather than trusting guidance generated for the old version.
- Keep `--dev` in the Composer command so the package never reaches production.
- Ask the agent to name the Laravel version it is targeting before it writes code; the skills make that answer checkable.
- If you only want the skills and not the MCP surface, install them at the agent level from the package directory instead of wiring the server.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
