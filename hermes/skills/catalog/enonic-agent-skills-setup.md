---
title: "Enonic Agent Skills - Enonic XP Development Setup"
description: "webmaxru/enonic-agent-skills: 5.9K combined installs across 16 listings; agent skills for Enonic XP CMS development, Guillotine, and Next.XP."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/enonic-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "enonic xp", "cms", "graphql"]
---

# Enonic Agent Skills - Setup Guide

**Source:** [webmaxru/enonic-agent-skills](https://www.skills.sh/webmaxru/enonic-agent-skills) via skills.sh - 5.9K combined installs across 16 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 0 stars, no LICENSE file, `main` branch, last pushed 2026-11-11. Eight Enonic skills live under `skills/` and four tooling skills under `.github/skills/`.
**Category:** Enonic XP CMS development
**Quality Tier:** 🟠 Orange - 1 Fail among 12 sampled skills (enonic-app-manager); no LICENSE file.

Enonic Agent Skills is a maintained collection of agent skills for teams developing on Enonic XP 7, the enterprise content platform, and its headless Next.XP framework. The skills cover the core Enonic surface: the server-side `/lib/xp/*` API reference, content type schemas, bulk content management, Guillotine GraphQL queries, Next.js integration, controllers, events and webhooks, and the Enonic CLI.

The repo also ships four general tooling skills under `.github/skills/` for operating and publishing skill collections themselves, including APM, skill deploy, GitHub Agentic Workflows, and a skill-creator. It follows the agentskills.io style: lean `SKILL.md` files with progressive disclosure through `references/` and `assets/`, and deterministic helper scripts. It is an independent community effort, not affiliated with Enonic.

## Installation

The recommended path is the webmaxru/ai-native-dev plugin marketplace, which installs the whole enonic-skills plugin:

```bash
/plugin marketplace add webmaxru/ai-native-dev
/plugin install enonic-skills@webmaxru-ai-native-dev
```

To install individual skills, use Agent Package Manager (APM) or the skills npm package:

```bash
apm init
apm install webmaxru/enonic-agent-skills/skills/SKILL_NAME
```

```bash
npx skills add webmaxru/enonic-agent-skills --skill SKILL_NAME
```

Replace `SKILL_NAME` with the skill directory name, for example `enonic-library-reference`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| enonic-nextxp-integration | 507 | Set up and troubleshoot the Next.js and Enonic XP headless integration (Next.XP): adapter config, content-type-to-component mapping, Guillotine data fetching, and Content Studio preview. |
| enonic-content-type-generator | 504 | Generate Enonic XP content type XML schemas from natural-language descriptions, covering input types, mixins, item sets, and inheritance. |
| agent-skill-deploy | 504 | Deploy a skills collection from a GitHub repo with a /skills folder to GitHub releases and the Claude Code, VS Code, and Copilot marketplaces. |
| enonic-guillotine-query-builder | 502 | Compose, debug, and optimize Guillotine GraphQL queries for Enonic XP headless content delivery. |
| agent-package-manager | 498 | Install, configure, audit, and operate Agent Package Manager (APM) in repositories. |
| enonic-controller-generator | 496 | Generate Enonic XP controllers and paired XML descriptors for pages, parts, and layouts. |
| skill-creator | 496 | Author and structure agent skills following the agentskills.io spec. |
| github-agentic-workflows | 496 | Author, review, install, and debug GitHub Agentic Workflows. |

The remaining 8 indexed listings range from 141 to 340 installs.

## Why This Matters for Hermes Agents

For a team running Enonic XP, the high-cost mistakes are version mismatches between the CLI, the libraries, and the headless adapter, and hand-writing content types or Guillotine queries that the platform could generate deterministically. These skills carry that knowledge in the SKILL.md files and their references, so an agent stops guessing at API signatures and version compatibility.

The split matters too: the Enonic skills under `skills/` are for building on the platform, while the four `.github/skills/` entries are for maintaining and shipping skill collections themselves, so a team that only builds Enonic sites can install just the platform half.

The skills are plain files plus helper scripts, so any harness that loads skill files, including Hermes, can use them even though the one-line installers target plugin marketplaces and APM.

## Usage

| You say | What happens |
|---|---|
| "Generate a content type for a news article" | enonic-content-type-generator returns an XML schema from your field descriptions. |
| "Write a Guillotine query for this type" | enonic-guillotine-query-builder composes and type-checks the GraphQL query. |
| "Set up a Next.js frontend on Enonic" | enonic-nextxp-integration walks through adapter config and component mapping. |
| "Scaffold a page controller" | enonic-controller-generator emits the controller and its XML descriptor. |
| "Migrate content between environments" | enonic-content-management writes a bulk migration script with task progress. |
| "Look up a lib-content function signature" | enonic-library-reference returns the signature, parameters, and an example. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/webmaxru/enonic-agent-skills/main/skills/enonic-library-reference/SKILL.md
```

Then install the plugin marketplace or a single skill:

```bash
/plugin marketplace add webmaxru/ai-native-dev
/plugin install enonic-skills@webmaxru-ai-native-dev
```

After install, ask your agent to generate a content type or a Guillotine query and check the next response changes.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| enonic-nextxp-integration | Pass | Warn | Pass |
| enonic-content-type-generator | Pass | Pass | Pass |
| agent-skill-deploy | Pass | Pass | Pass |
| enonic-guillotine-query-builder | Pass | Pass | Pass |
| agent-package-manager | Pass | Pass | Pass |
| enonic-controller-generator | Pass | Pass | Pass |
| skill-creator | Pass | Pass | Pass |
| github-agentic-workflows | Pass | Pass | Pass |
| enonic-content-management | Pass | Pass | Pass |
| enonic-library-reference | Pass | Pass | Pass |
| enonic-event-manager | Pass | Pass | Pass |
| enonic-app-manager | Fail | Pass | Warn |

The sample covers 12 of the 16 indexed listings; one fails (enonic-app-manager).

## Limitations

- Snapshot data, verified Nov 18, 2026: 5,933 combined installs across 16 indexed listings; 0 GitHub stars; no LICENSE file; last pushed 2026-11-11. Counts drift over time.
- The repo carries no LICENSE file, so treat it as source-available rather than under a standard permissive licence.
- The eight skills shown above carry most of the install volume; the other eight indexed listings sit between 141 and 340 installs.
- Four indexed listings (enonic-sandbox-manager, enonic-webhook-integrator, enonic-content-migration, enonic-api-reference) carry install counts but have no matching directories in the current tree.
- This is a community effort with no affiliation to Enonic, and it targets Enonic XP 7 specifically.
- The one-line installers target plugin marketplaces and APM; outside those, copy individual `SKILL.md` files into your agent's skills directory.

## Related

- [Payload CMS Skills - Schema and Migration Setup](/hermes/skills/catalog/payloadcms-skills-setup)
- [EmDash CMS Skills - Astro CMS Agent Suite](/hermes/skills/catalog/emdash-cms-skills-setup)
- [Claude Code Extensions - Agents, Skills & Hooks Setup](/hermes/skills/catalog/nodnarbnitram-claude-code-extensions-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the platform half (`skills/`) if you build Enonic sites and do not maintain skill collections.
- Use enonic-library-reference as the first stop for any API question; its references are split per library.
- Run the find-targets helper scripts to confirm a workspace is actually an Enonic project before generating code.
- Keep the CLI, libraries, and Next.XP adapter versions aligned; the compatibility references list the pairing.
- Treat the no-LICENSE state as a blocker for redistribution until you confirm terms with the author.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
