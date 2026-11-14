---
title: "Umbraco Backoffice Skills - CMS Extension Setup"
description: "umbraco/umbraco-cms-backoffice-skills: 31.0K combined installs across 78 listings, official Umbraco backoffice extension skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/umbraco-backoffice-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "umbraco", "cms", "backoffice"]
---

# Umbraco Backoffice Skills - Setup Guide

**Source:** [umbraco/umbraco-cms-backoffice-skills](https://www.skills.sh/umbraco/umbraco-cms-backoffice-skills) via skills.sh - 31.0K combined installs across 78 indexed listings; first seen Nov 14, 2026 (sweep)
**GitHub:** 27 stars, no LICENSE file, `main` branch, last pushed 2026-10-04, 79 `SKILL.md` files across `plugins/umbraco-backoffice-skills/skills/`, `plugins/umbraco-testing-skills/skills/` and `.claude/skills/`
**Category:** Umbraco backoffice extension development and testing skills
**Quality Tier:** 🟡 Yellow - no LICENSE file in the repo, and the sampled verdicts include Warn results.

Umbraco Backoffice Skills is a Claude Code plugin marketplace for extending the Umbraco backoffice, published from the Umbraco GitHub org. It bundles a backoffice extension plugin and a testing plugin, plus a few dev-time skills under `.claude/skills/`. The README calls the project an experimental beta.

The skills map the backoffice extension surface: dashboards, trees, sections, workspaces, property editors, rich text (Tiptap), authentication, and a full testing pyramid. They are versioned to a single Umbraco major; `main` targets the latest (currently Umbraco 18) and older majors live on `vN/main` branches.

## Installation

Add the marketplace and install the plugins (Claude Code slash commands):

```text
/plugin marketplace add umbraco/Umbraco-CMS-Backoffice-Skills
/plugin install umbraco-cms-backoffice-skills@umbraco-backoffice-marketplace
/plugin install umbraco-cms-backoffice-testing-skills@umbraco-backoffice-marketplace
```

For an older Umbraco major, point the marketplace add at the matching branch, for example `https://github.com/umbraco/Umbraco-CMS-Backoffice-Skills.git#v17/main`.

Install all skills into another editor with the Vercel Skills CLI:

```bash
npx skills add umbraco/Umbraco-CMS-Backoffice-Skills --skill '*' -a cursor
```

The README also documents `-a github-copilot` and `-a windsurf`, and per-skill installs such as `npx skills add umbraco/Umbraco-CMS-Backoffice-Skills --skill umbraco-dashboard --skill umbraco-tree -a cursor`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| umbraco-backoffice | 457 | Backoffice extension customisation with complete working examples showing how extension types combine. |
| umbraco-dashboard | 429 | Implement dashboards in the backoffice using the official docs. |
| umbraco-controllers | 428 | Understand and create controllers in the backoffice, a foundational concept. |
| umbraco-extension-template | 423 | Create new backoffice extensions using the official dotnet template. |
| umbraco-quickstart | 416 | Quick setup for extension development: creates the instance, the extension, and registers it. |
| umbraco-property-editor-ui | 415 | Implement property editor UIs in the backoffice using the official docs. |
| umbraco-openapi-client | 415 | Set up the OpenAPI client for authenticated API calls, required for custom APIs. |
| umbraco-notifications | 413 | Understand and use notifications in the backoffice, a foundational concept. |
| umbraco-extension-registry | 413 | Understand and use the extension registry in the backoffice, a foundational concept. |
| umbraco-context-api | 412 | Understand and use the Context API in the backoffice, a foundational concept. |
| umbraco-add-extension-reference | 412 | Add a new extension project reference to the main Umbraco instance and solution. |
| umbraco-routing | 411 | Understand and use routing in the backoffice, a foundational concept. |
| umbraco-repository-pattern | 410 | Understand and use repositories in the backoffice, a foundational concept. |
| umbraco-mfa-login-provider | 410 | Implement MFA login providers for the backoffice using the official docs. |
| umbraco-menu-items | 410 | Implement menu items in the backoffice using the official docs. |
| umbraco-entity-create-option-action | 410 | Implement entity create option actions in the backoffice using the official docs. |

The remaining 62 indexed listings range from 148 to 409 installs.

## Why This Matters for Hermes Agents

Umbraco is a mature .NET CMS, and its backoffice is a rich extension surface with dozens of extension points that are easy to get subtly wrong. This pack encodes the official extension model into per-concept skills, so an agent extending the backoffice works from the same vocabulary the Umbraco docs use instead of guessing at manifest shapes.

The version guard is the key safety feature. Skills are pinned to a single Umbraco major because tree data sources, auth and OpenAPI registration differ between majors, and loading the wrong line produces confidently incorrect code. The umbraco-version-guard skill runs as a preflight inside the entry skills and stops with a warning on a major mismatch.

The skills are organised the way a developer thinks: a backbone skill (umbraco-backoffice) with working blueprints, entry-point skills for setup, foundational concepts, extension types, property editors, rich text, backend auth, and a full testing pyramid. An agent can drill into exactly the extension type the task needs rather than loading a wall of generic guidance.

## Usage

| You say | What happens |
|---|---|
| "Create a new dashboard for this site" | umbraco-dashboard generates the manifest and component using the official docs. |
| "Set up a new extension project" | umbraco-quickstart creates the instance and extension, then plans, builds and validates. |
| "Add a custom tree to Settings" | umbraco-tree scaffolds the tree, with umbraco-conditions controlling where it appears. |
| "Add two-factor login to the backoffice" | umbraco-mfa-login-provider implements an MFA login provider. |
| "Call my custom API from the backoffice" | umbraco-openapi-client sets up the OpenAPI client for authenticated calls. |
| "Write tests for this extension" | umbraco-testing routes to unit, mocked or E2E testing and runs the right helpers. |
| "Which major am I targeting?" | umbraco-version-guard verifies the site major matches the skills major. |

## Verification

Probe the skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/umbraco/umbraco-cms-backoffice-skills/main/plugins/umbraco-backoffice-skills/skills/umbraco-backoffice/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/umbraco/umbraco-cms-backoffice-skills/main/plugins/umbraco-backoffice-skills/skills/umbraco-dashboard/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/umbraco/umbraco-cms-backoffice-skills/main/plugins/umbraco-backoffice-skills/skills/umbraco-quickstart/SKILL.md
```

Skills live at `plugins/umbraco-backoffice-skills/skills/<name>/SKILL.md` and `plugins/umbraco-testing-skills/skills/<name>/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| umbraco-backoffice | Warn | Warn | Pass |
| umbraco-dashboard | Pass | Pass | Warn |
| umbraco-controllers | Pass | Pass | Warn |
| umbraco-extension-template | Pass | Pass | Pass |
| umbraco-quickstart | Pass | Pass | Pass |
| umbraco-property-editor-ui | Pass | Pass | Warn |

The sample covers only 6 of the 78 indexed listings and is not clean: four of the six carry a Warn in Snyk, and umbraco-backoffice carries Warn in both Gen Agent Trust Hub and Socket. Re-check the skills.sh pages before production use.

## Limitations

- Snapshot data, verified 2026-11-14: 31,007 combined installs across 78 indexed listings; 27 GitHub stars; no LICENSE file; last pushed 2026-10-04. Counts drift over time.
- The repo has no LICENSE file and GitHub reports no license, even though the README states MIT. Treat licensing as unconfirmed.
- 62 of the 78 indexed listings sit below 410 installs, ranging from 148 to 409 each.
- Skills are pinned to a single Umbraco major; `main` targets the latest and older majors live on `vN/main` branches, so pick the branch that matches your site.
- The README counts 67 skills across the two plugins, while the index lists 78 and the tree holds 79 SKILL.md files, so the install index outruns the README's own count.
- The project is an experimental beta and is evolving as the maintainers learn what works.

## Related

- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)
- [EmDash CMS Skills - Astro CMS Agent Suite](/hermes/skills/catalog/emdash-cms-skills-setup)
- [Plinth - Java Enterprise SDLC Toolkit Setup](/hermes/skills/catalog/jabrena-plinth-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with umbraco-backoffice for its complete extension map and working blueprints before touching individual extension-type skills.
- Match the skills to your Umbraco major: check the `Umbraco.Cms` version in `.csproj` or the `@umbraco-cms/backoffice` version in `Client/package.json`.
- Add the Umbraco CMS and Umbraco.UI source repos as working directories so the agent can reference real implementations.
- Use umbraco-version-guard directly any time you are unsure which major you are targeting.
- For custom API calls, umbraco-openapi-client is required; skip it and authenticated calls will not work.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
