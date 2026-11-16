---
title: "Wix Skills - Site, App and Design System Setup"
description: "wix/skills: 8.8K combined installs across 37 listings, Wix skills for app extensions, headless sites, the Design System and business management."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wix-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "wix", "headless", "web development"]
---

# Wix Skills - Setup Guide

**Source:** [wix/skills](https://www.skills.sh/wix/skills) via skills.sh - 8.8K combined installs across 37 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 40 stars, MIT license, `main` branch, last pushed 2026-11-13, 44 `SKILL.md` files under `skills/` in about twenty skill directories
**Category:** Website building, app extensions and headless commerce
**Quality Tier:** 🟡 Yellow - one of the two sampled skills carries a Snyk Warn while the other passes all three auditors, and the project labels itself experimental.

Wix's skills are aimed at the new Wix CLI and cover four jobs: building app extensions, managing a site's business solutions through REST recipes, standing up headless sites, and using the Wix Design System components correctly. The README opens with an experimental warning, which is worth taking literally: APIs and skill definitions are stated to change without notice.

The most useful thing in the collection is not a single skill but the pairing. `wix-docs` is a lookup skill that insists on confirming an exact endpoint, method, request shape, field or error before any Wix code is written, and `wix-manage` carries the REST recipes for stores, bookings, donations, payments and CMS. Together they replace the guesswork that produces Wix code that looks right and fails at the first call.

## Installation

Install the plugin in Claude Code:

```text
/plugin marketplace add wix/skills
/plugin install wix@wix
```

The same repository is installable in other hosts: Codex through its plugin directory, VS Code through Chat: Install Plugin From Source with the repository URL, Cursor through Settings, Rules, Add from Github, Gemini CLI with `gemini extensions install https://github.com/wix/skills`, and Antigravity through its plugin installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| wix-docs | 802 | Looking up the Wix API and SDK documentation to confirm an endpoint, method, request or response shape, field, enum or error before writing code. |
| wix-manage | 761 | REST recipes that configure and manage a site's business solutions: stores, bookings, donations, payments, CMS and content publishing. |
| wix-headless-kit | 443 | Building new Wix sites or putting an existing site online, with or without a Wix account, with pages as code. |
| wix-vibe-headless | 420 | Connecting an existing frontend to a live Wix site with client-only REST and its public client id, no SDK or backend. |
| wix-headless | 338 | Connecting Wix business services to a headless frontend: stores, bookings, donations, CMS, blog, events and forms. |
| wix-headless-templates | 288 | Shipped, verified code for headless sites, one folder per business solution: store, bookings, rentals, blog and CMS collections. |
| wix-app | 261 | Building and reviewing Wix CLI app extensions: dashboard pages, modals, plugins, widgets, Editor React components and site plugins. |
| wix-design-system | 218 | The Wix Design System component reference for `@wix/design-system`: components, props, examples and tests. |

The remaining 29 indexed listings range from 1 to 139 installs. Seventeen of those, including every `wix-cli-*` name, have no directory in the current tree.

## Why This Matters for Hermes Agents

Wix is an API-heavy platform with a large documentation surface, and models fill gaps in it with plausible invented fields. `wix-docs` exists specifically to stop that: it is a lookup skill whose instruction is to confirm the exact shape before writing code, which is the behaviour you want when a wrong field name means a failed publish rather than a warning.

The headless skills are the technically interesting part. Building a storefront against Wix's business services without an SDK means handling capabilities, cart, checkout and CMS through REST, and the templates skill ships verified code per solution rather than describing it. An agent with that folder can copy a working pattern instead of reconstructing one.

The Design System skill keeps generated UI inside the component library, which matters for a platform where a custom component can break theming, accessibility and future upgrades at once.

## Usage

| You say | What happens |
|---|---|
| "Add a product to this Wix store" | Confirms the endpoint through `wix-docs`, then applies the REST recipe from `wix-manage`. |
| "Build a headless storefront against our Wix catalog" | Uses the headless skills and the shipped template for stores. |
| "Connect this existing React app to Wix without a backend" | Uses `wix-vibe-headless` with client-only REST and the public client id. |
| "Create a dashboard page in our Wix app" | Uses `wix-app` for the CLI extension structure. |
| "Which component should I use for this table?" | Uses the Design System reference rather than writing a custom table. |
| "Publish this CMS content" | Uses `wix-manage` for the content publishing path. |

## Verification

Read the docs skill and confirm the plugin resolves before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/wix/skills/main/skills/wix-docs/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/wix/skills/main/skills/wix-manage/SKILL.md
```

The eight grounded skills sit at `skills/<name>/SKILL.md`. Many names in the install index have no directory in the current tree, so a 404 on a raw path is the drift described below, not a typo in your command.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wix-docs | Pass | Pass | Pass |
| wix-manage | Pass | Pass | Warn |

`wix-manage` is the skill that touches live site data: stores, payments and bookings. It carries a Snyk Warn. Scope the API credentials and test against a development site first.

## Limitations

- Snapshot data, verified 2026-11-14: 8,802 combined installs across 37 indexed listings; 40 GitHub stars; MIT; last pushed 2026-11-13. Counts drift over time.
- The install index outruns the tree by a wide margin: 37 listings against about twenty skill directories. Seventeen listed names, including the whole `wix-cli-*` family at 202 installs each, have no matching directory in the current tree.
- The project is labelled experimental in its own README: APIs, skill definitions and behaviour may change without notice.
- Everything targets the new Wix CLI. Projects on the older CLI are outside the documented scope.
- Headless work needs a Wix site and client id; the skills are not a substitute for an account or a business solution.
- One sampled verdict is a Warn, and it sits on the skill that writes to live site data.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Popular Web Designs - 54 Design Systems as HTML/CSS Templates Setup](/hermes/skills/catalog/popular-web-designs-setup)
- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Always let `wix-docs` confirm the endpoint before `wix-manage` writes anything; the pair is designed to be used in that order.
- Use the headless templates as starting code rather than as examples, since the repository states they are verified.
- Install the Design System skill before any UI work so generated components stay inside the library.
- Check the tree for a skill directory before installing a name from the index: much of the index is ahead of the repository.
- Test business-solution writes against a sandbox site; payments and bookings are not reversible operations.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
