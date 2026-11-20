---
title: "Bagisto Agent Skills - Official Ecommerce Platform Setup"
description: "Setup guide for bagisto/agent-skills: 5.4K combined installs across 30 listings; official Bagisto skills for ecommerce packages, APIs, and themes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bagisto-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "bagisto", "laravel", "ecommerce"]
---

# Bagisto Agent Skills - Setup Guide

**Source:** [bagisto/agent-skills](https://www.skills.sh/bagisto/agent-skills) via skills.sh - 5.4K combined installs across 30 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** 14 stars, no LICENSE file, `main` branch, last pushed 2026-11-16. Skills are SKILL.md directories under `skills/`, with the three API skills grouped under `skills/api-platform-development/`; `AGENTS.md` is assembled from versioned `rules/` fragments and `bin/` holds the lint and build scripts.
**Category:** Ecommerce platform development (Bagisto / Laravel)
**Quality Tier:** 🟠 Orange - no LICENSE file; 3 Fail cells and 6 Warn cells across 16 sampled verdicts (package-development Gen Agent Trust Hub Fail; Snyk Fail on bagisto-coding-standards and bagisto-package-development).

bagisto/agent-skills is the Bagisto team's official collection of agent skills for building on Bagisto, a Laravel-based open-source ecommerce platform. The 30 indexed listings span the full extension surface: package, payment, shipping, product-type, and theme development, the admin and storefront APIs, plus testing, coding standards, documentation, and the change-verification gate.

The install curve is top-heavy on the four core extension types (package-development 318, payment-method-development 287, shipping-method-development 270, shop-theme-development 267), with the bagisto- prefixed variants of the same domains sitting in the 150-190 range. This is not a pure skill library: AGENTS.md is generated from versioned rules fragments (Bagisto 2.4 and 2.5), so skills carry version-specific guidance in their text rather than as separate installs.

## Installation

Distributed through skills.sh; the `skills` CLI needs no global install because `npx` fetches it each time. Run it inside the project so skills install per-project and are recorded in that project's `skills-lock.json`:

```bash
# everything, into every agent it detects, without prompting
npx skills add bagisto/agent-skills --all

# just one skill
npx skills add bagisto/agent-skills --skill "bagisto-coding-standards"

# see what a repo offers before committing to it
npx skills add bagisto/agent-skills --list
```

A fork, company mirror, or private repo works the same way:

```bash
npx skills add your-org/agent-skills
npx skills add https://github.com/your-org/agent-skills
```

Add `--global` only for skills you want in every project; per-project installs are what let a Bagisto 2.4 checkout and a 2.5 checkout hold different sets. By default the installer symlinks each skill into every agent directory it finds, so pass `--copy` to write real files instead.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| package-development | 318 | Create or change a Bagisto package: service providers, migrations, models, repositories, routes, controllers, views, admin menus, ACL, system config. |
| payment-method-development | 287 | Build a Bagisto payment method: payment class, config, checkout redirect and callback flow, gateway integration such as Stripe or PayPal. |
| shipping-method-development | 270 | Build a Bagisto shipping method and integrate carriers such as FedEx, UPS, DHL, or any third-party provider. |
| shop-theme-development | 267 | Create or change a Bagisto storefront theme: theme package, shop layouts, Blade overrides, and the Vite asset pipeline. |
| bagisto-api-admin | 253 | Build an admin app or UI on the Bagisto Admin API: order, catalog, customer, marketing, CMS, and settings screens. |
| bagisto-api-shop | 248 | Build a storefront app or UI on the Bagisto Shop API: catalog, cart, checkout, customer account, wishlist, and reviews. |
| bagisto-api-develop | 245 | Work inside the bagisto-api package: install or remove it, add or change REST or GraphQL endpoints and resources. |
| admin-theme-development | 233 | Create custom admin themes, admin layouts, admin theme packages, and admin panel styling. |
| pest-testing | 225 | Write Pest PHP tests (Pest 3 on Bagisto 2.4, Pest 5 on 2.5): unit and feature tests, assertions, mocking, architecture tests. |
| product-type-development | 221 | Create custom product types, define product behaviors, and implement specialized product logic. |
| bagisto-coding-standards | 184 | Apply Bagisto PHP and Blade conventions: Laravel idiom, code style, comments, data access, security, and localization. |
| bagisto-package-development | 162 | Create or change a Bagisto package: providers, migrations, models, repositories, routes, controllers, views, ACL, system config. |
| bagisto-shop-theme-development | 157 | Create or change a Bagisto storefront theme: theme package, shop layouts, Blade overrides, Vite assets. |
| bagisto-payment-method-development | 157 | Create or change a Bagisto payment method: payment class, config, checkout redirect and callback flow. |
| bagisto-pest-testing | 156 | Write or change a Bagisto Pest test: feature or unit tests, assertions, datasets, mocking, architecture tests. |
| bagisto-change-verification | 156 | Run the completion gate before a change is called done: code style, tests, end-to-end tests, and translation checks. |
| bagisto-shipping-method-development | 151 | Create or change a Bagisto shipping method and its carrier integration. |
| bagisto-attribute-development | 151 | Work with the EAV attribute system: attributes, families, groups, options, and how values are stored. |

The remaining 12 indexed listings range from 50 to 150 installs.

## Why This Matters for Hermes Agents

Bagisto is a Laravel application with strong opinions, and agent-written code drifts from those opinions quickly when the agent reimplements conventions from generic Laravel knowledge. These skills encode the platform's own rules as reusable context, so a Hermes agent building an extension follows Bagisto's service-provider, migration, repository, and ACL patterns instead of inventing its own.

The collection covers the two failure points that matter most in ecommerce work. Payment and shipping skills keep checkout integrations on the platform's redirect and callback flow rather than hand-rolled gateway code. The coding-standards, pest-testing, and change-verification skills close the loop: an agent that writes a feature can also be asked to lint it, test it, and run the completion gate before anyone calls the change done.

The API skills are the notable addition: bagisto-api-admin and bagisto-api-shop give an agent the exact endpoint shapes for building headless admin and storefront clients on top of Bagisto, with the api-docs treated as the source of truth. For a Hermes agent, these are plain SKILL.md directories with reference files, so they load like any other skill.

## Usage

| You say | What happens |
|---|---|
| "Add a new payment method to this Bagisto checkout" | payment-method-development guides the payment class, config, and redirect or callback flow, including Stripe or PayPal integration. |
| "Create a custom product type for this store" | product-type-development steps through product behaviors and specialized product logic. |
| "Build a storefront theme for my Bagisto install" | shop-theme-development covers the theme package, shop layouts, Blade overrides, and Vite assets. |
| "Add a new admin grid for orders" | package-development covers the DataGrid, admin menu, ACL, and system configuration for the package. |
| "Is this change ready to commit?" | bagisto-change-verification runs the gates: pint, pest, playwright, and translation completeness. |
| "Build a headless admin app on the Bagisto API" | bagisto-api-admin supplies the Admin API endpoint shapes, treating the api-docs as the source of truth. |

## Verification

Confirm skills landed in the agent skills directory after install, and probe one SKILL.md on the `main` branch before reviewing (returns 200):

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/bagisto/agent-skills/main/skills/bagisto-coding-standards/SKILL.md
```

```bash
npx skills list
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

Three of the 16 sampled skills carry a Fail cell (package-development Gen Agent Trust Hub; Snyk on bagisto-coding-standards and bagisto-package-development), and four others carry Warn cells, so review those pages before relying on the skills in production.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| package-development | Fail | Pass | Pass |
| payment-method-development | Pass | Warn | Warn |
| shipping-method-development | Pass | Pass | Pass |
| shop-theme-development | Pass | Pass | Pass |
| bagisto-api-admin | Pass | Warn | Warn |
| bagisto-api-shop | Pass | Pass | Warn |
| bagisto-api-develop | Pass | Pass | Pass |
| admin-theme-development | Pass | Pass | Pass |
| pest-testing | Pass | Pass | Pass |
| product-type-development | Pass | Pass | Pass |
| bagisto-coding-standards | Pass | Pass | Fail |
| bagisto-package-development | Pass | Pass | Fail |
| bagisto-shop-theme-development | Pass | Pass | Pass |
| bagisto-payment-method-development | Pass | Pass | Warn |
| bagisto-pest-testing | Pass | Pass | Pass |
| bagisto-change-verification | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 19, 2026: 5,424 combined installs across 30 indexed listings; 14 GitHub stars; no LICENSE file; last pushed 2026-11-16. Counts drift over time.
- The install index carries 30 listings but the tree holds 22 SKILL.md files (one nested under bagisto-shop-advance-theme-development). Nine listings use short names (package-development, payment-method-development, shipping-method-development, shop-theme-development, admin-theme-development, pest-testing, product-type-development, blade-conventions, shop-advance-theme-development) with no matching directory, since the tree ships bagisto- prefixed directories.
- There is no LICENSE file, so treat the repo as all-rights-reserved rather than open source until terms are confirmed with Bagisto.
- `add` always takes the repository's default branch; there is no `--ref`, `--branch`, or `--tag`, so a 2.4 and a 2.5 project receive identical skills and version differences are labeled inside the skill text.
- The three API skills are grouped under `skills/api-platform-development/`, which the one-line installer detects; `--full-depth` searches nested directories when a root SKILL.md exists.

## Related

- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup)
- [Magento 2 Agent Skills - Adobe Commerce Suite](/hermes/skills/catalog/magento2-agent-skills-setup)
- [Laravel Boost - Laravel AI Development Setup](/hermes/skills/catalog/laravel-boost-setup)
- [Hyva AI Tools - Magento Front-End for Agents](/hermes/skills/catalog/hyva-ai-tools-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per-project, not `--global`: a Bagisto 2.4 checkout and a 2.5 checkout need different skill sets.
- Start with `bagisto-coding-standards` when an agent is new to the codebase; it teaches the conventions the other skills assume.
- Keep `bagisto-change-verification` in the loop before every commit; it runs pint, pest, playwright, and translation checks in one pass.
- Use `--skill` to pull a single skill instead of `--all`; the whole suite is a lot of context for a small task.
- Watch the Fail and Warn cells on package-development and the coding-standards and package-development Snyk pages before relying on those skills unattended.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
