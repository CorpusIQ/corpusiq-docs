---
title: "Shopify Hydrogen Skills - Weaverse Storefront Agent Skills"
description: "weaverse/shopify-hydrogen-skills: 1.8K combined installs. Agent skills for building, upgrading and maintaining Shopify Hydrogen storefronts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shopify-hydrogen-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "shopify", "hydrogen", "weaverse"]
---

# Shopify Hydrogen Skills - Setup Guide

**Source:** [weaverse/shopify-hydrogen-skills](https://www.skills.sh/weaverse/shopify-hydrogen-skills) via skills.sh - 1.8K combined installs across 14 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [Weaverse/shopify-hydrogen-skills](https://github.com/Weaverse/shopify-hydrogen-skills) - 98 stars, no LICENSE file in the repo (the README declares MIT but the GitHub license field is empty), branch main, last pushed 2026-11-25; skills live under `skills/<name>/SKILL.md` with a `.claude-plugin/marketplace.json` and a hosted Weaverse MCP server manifest.

**Category:** Agent skills suite - Shopify Hydrogen storefront building, upgrading and maintenance plus Weaverse CMS integration for coding agents

**Quality Tier:** 🟠 Orange - Snyk fails hydrogen-upgrades, theme-update and hydrogen-analytics-tracking (the last also carries the only Socket Warn); all 14 listings pass the Gen Agent Trust Hub, and the repo carries no LICENSE file.

weaverse/shopify-hydrogen-skills is the Weaverse team's skill collection for building, upgrading and maintaining Shopify Hydrogen storefronts. The 14 indexed listings span the core Hydrogen 2026.10 APIs, feature cookbooks, framework version upgrades, Pilot theme updates, analytics tracking, market localization and the Weaverse CMS integration layer. They target Hydrogen 2026.10 with React Router 7 and `@weaverse/hydrogen` 6, with Next.js storefronts covered through `@weaverse/hydrogen/next`.

The README frames these as agent-optimized knowledge that a coding agent loads before a task, and pairs them with zero-dependency live doc-fetching scripts instead of static API docs that go stale. The skills work with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, OpenClaw and Gemini CLI, and any agent that reads markdown skill files.

## Installation

The README installs the suite through a Claude Code plugin marketplace for Claude users, and through `npx skills add` for everything else.

```bash
claude plugin install weaverse --marketplace Weaverse/shopify-hydrogen-skills
```

The plugin installs every skill in `skills/` and registers the hosted Weaverse MCP server at `https://mcp.weaverse.io/mcp` (no Content API key needed). Plugin skills are invoked with names such as `/weaverse:setup-weaverse-project`.

To add only the store connection when the skills are already installed:

```bash
claude mcp add --transport http weaverse https://mcp.weaverse.io/mcp
```

For Codex, Cursor and other agents the skills-only install is:

```bash
npx skills add Weaverse/shopify-hydrogen-skills
```

Codex and Cursor store access runs through the local `npx -y @weaverse/mcp` server with a `WEAVERSE_API_KEY`. The README also recommends pairing the suite with Shopify's own version-matched skills via `npx @shopify/hydrogen skills sync`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| shopify-hydrogen | 168 | Core Hydrogen 2026.10 APIs: server.ts request lifecycle, routing, Storefront client, cart store, CSP and production checklist. |
| hydrogen-cookbooks | 164 | Step-by-step feature guides: bundles, combined listings, customer accounts, 3D models and performance. |
| hydrogen-upgrades | 158 | Upgrade guides between Hydrogen versions with breaking changes, code diffs and migration steps. |
| weaverse-hydrogen | 150 | Build Hydrogen storefronts with Weaverse: components, schemas, loaders, theming and deployment. |
| theme-update | 145 | Safely update a Weaverse Pilot theme, preserving customizations and verifying the build. |
| hydrogen-analytics-tracking | 144 | GTM, GA4, Meta Pixel and CAPI, Google Ads and consent mode tracking on Hydrogen. |
| cloning-websites-to-weaverse | 144 | Recreate a reference website as Hydrogen plus Weaverse pages with section mapping. |
| weaverse-integration | 143 | Integrate Weaverse into an existing Hydrogen project, converting components to sections. |
| generating-weaverse-project-json | 138 | Generate import-ready Weaverse project export JSON from specs or existing exports. |
| setup-weaverse-project | 114 | Set up a new Weaverse Hydrogen storefront locally, from demo boot to credentials and GitHub push. |
| weaverse-content-api | 111 | Read and update live Weaverse content over the REST Content API. |
| figma-to-weaverse | 109 | Turn a Figma design into Weaverse sections via Figma MCP with visual checks. |
| hydrogen-markets-localization | 64 | Shopify Markets localization: locale routes, translations, hreflang, RTL and localized cart. |
| weaverse-nextjs | 2 | Weaverse on the Next.js App Router for Hydrogen storefronts. |

All 14 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

This repository is a clean example of a vendor skill suite layered on top of a framework's own skills. The README recommends running Shopify's version-matched skills first (`npx @shopify/hydrogen skills sync`) and then adding the Weaverse, Pilot and Forward specifics on top, which is a useful pattern for how a Hermes agent should stack a platform skill under a domain skill.

The core shopify-hydrogen skill encodes the server.ts request lifecycle, the routes Hydrogen owns, and the Storefront and cart APIs that a Hydrogen agent needs to avoid hallucinating. Instead of baking static API docs into SKILL.md files, the repo ships zero-dependency Node scripts that query shopify.dev and docs.weaverse.io at runtime, with the references/ folders as an offline fallback, so an agent stays current without reinstalling.

The hydrogen-upgrades and theme-update skills carry real migration steps and release diffs for each Hydrogen version, which is exactly the versioned knowledge a build agent should load before touching a storefront several releases behind.

The main caveat for builders is the security spread: three skills carry Snyk failures and the repo has no LICENSE file, so this suite is a source of patterns and procedures to inspect rather than a blind install into a production profile.

## Usage

| You say | What happens |
|---|---|
| "Set up a new Hydrogen storefront for my Shopify store" | Uses setup-weaverse-project to scaffold locally, boot a demo store, then link credentials and push to GitHub. |
| "Upgrade this storefront from Hydrogen 2026.1 to 2026.10" | Uses hydrogen-upgrades to apply the release-specific migration steps and code diffs. |
| "Add Google Analytics and Meta Pixel tracking" | Uses hydrogen-analytics-tracking to wire GTM, GA4 and Meta Pixel plus CAPI and consent mode. |
| "Recreate this reference site as a Weaverse storefront" | Uses cloning-websites-to-weaverse to map sections and rebuild the pages. |
| "Turn this Figma file into storefront sections" | Uses figma-to-weaverse to convert the design into Weaverse sections with visual checks. |
| "Update the Pilot theme to the latest release" | Uses theme-update to detect the version, plan changes and verify the build. |
| "Translate the storefront into French and German" | Uses hydrogen-markets-localization to add locale routes, translations and hreflang. |

## Verification

The cleanest pre-install check is to fetch a skill's SKILL.md directly and read its frontmatter. The layout on branch main is `skills/<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/Weaverse/shopify-hydrogen-skills/main/skills/shopify-hydrogen/SKILL.md
```

After a clone, confirm the skill directories and the plugin manifest:

```bash
git clone --depth 1 https://github.com/Weaverse/shopify-hydrogen-skills.git /tmp/shopify-hydrogen-skills
ls /tmp/shopify-hydrogen-skills/skills/
cat /tmp/shopify-hydrogen-skills/.claude-plugin/marketplace.json
```

The `skills/` directory should list 14 skill folders, and the repo root also carries `INSTALL.md`, `AGENTS.md` and the `.claude-plugin/` manifest.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| shopify-hydrogen | Pass | Pass | Warn |
| hydrogen-cookbooks | Pass | Pass | Warn |
| hydrogen-upgrades | Pass | Pass | Fail |
| weaverse-hydrogen | Pass | Pass | Warn |
| theme-update | Pass | Pass | Fail |
| hydrogen-analytics-tracking | Pass | Warn | Fail |
| cloning-websites-to-weaverse | Pass | Pass | Warn |
| weaverse-integration | Pass | Pass | Pass |
| generating-weaverse-project-json | Pass | Pass | Pass |
| setup-weaverse-project | Pass | Pass | Warn |
| weaverse-content-api | Pass | Pass | Pass |
| figma-to-weaverse | Pass | Pass | Warn |
| hydrogen-markets-localization | Pass | Pass | Warn |
| weaverse-nextjs | Pass | Pass | Warn |

All 14 listings were sampled. This guide is Orange because Snyk fails hydrogen-upgrades, theme-update and hydrogen-analytics-tracking. The Gen Agent Trust Hub passes all 14, and the only Socket Warn sits on hydrogen-analytics-tracking. The repo carries no LICENSE file, so confirm terms before use.

## Limitations

- Snapshot data, verified 2026-11-28: 1,754 combined installs across 14 indexed listings; 98 GitHub stars; no LICENSE file; last pushed 2026-11-25. Counts drift over time.
- No LICENSE file: the README declares MIT but the repo carries no LICENSE file and the GitHub license metadata is empty, so confirm terms before redistributing.
- The install surface is small and flat: every listing sits under 200 installs and the combined total is 1.8K, so this is a young suite with limited adoption rather than a widely deployed one.
- Three skills carry Snyk failures (hydrogen-upgrades, theme-update and hydrogen-analytics-tracking), so re-check the security pages before pulling the suite into a production profile.
- The skills pin Hydrogen 2026.10 with React Router 7 and @weaverse/hydrogen 6; earlier Hydrogen versions appear only in the upgrade and migration guides.

## Related

- [Shopify Development - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/shopify-development-setup)
- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a skill's SKILL.md before installing the plugin: the frontmatter name and description define what it does, and the body is the instruction set the agent follows.
- Prefer the Claude Code plugin install for Claude users, since the marketplace manifest registers the hosted Weaverse MCP server and updates through the plugin system.
- Run `npx @shopify/hydrogen skills sync` alongside this suite so Shopify's version-matched skills sit underneath the Weaverse specifics.
- Use the live doc scripts (`search_shopify_docs.mjs`, `search_weaverse_docs.mjs`) rather than trusting cached API references, since the references/ folders are only an offline fallback.
- Because three skills carry Snyk failures, re-check the skills.sh security pages before pulling the suite into a production profile.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
