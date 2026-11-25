---
title: "Contentful Skills - Headless CMS Agent Setup"
description: "contentful/skills - 5.9K combined installs: official Contentful skills teaching agents the headless CMS APIs, apps, migrations and personalization."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/contentful-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "contentful", "headless cms", "next.js"]
---

# Contentful Skills - Setup Guide

**Source:** [contentful/skills](https://www.skills.sh/contentful/skills) via skills.sh - 5.9K combined installs across 12 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [contentful/skills](https://github.com/contentful/skills) - 43 stars, MIT license, last pushed Nov 25, 2026, main branch; skills under skills/<name>/SKILL.md (the two custom-app skills under skills/contentful-apps/) plus local-skills/ for skill-authoring and optimization-sdk-sync.
**Category:** Headless CMS (Contentful)
**Quality Tier:** 🟠 Orange - contentful-nextjs fails Socket, and contentful-personalization and exo-content-bindings fail Snyk; several other skills carry Warns.

contentful/skills is Contentful's official skill suite for teaching agents how to build on the headless CMS. The 12 indexed skills cover the API reference, core concepts and routing, Next.js integration, content model migrations, environment analysis, App Framework custom apps, personalization and A/B testing, Channels and Destinations, and Experience Orchestration content bindings. The README's framing is that agents already know how to code but know nothing about your content model, SDK patterns, or which of Contentful's APIs to reach for, and these skills fix that.

The index lists 12 listings at 5.9K combined installs. Ten skills ship under skills/<name>/SKILL.md (the two custom-app skills under skills/contentful-apps/), and two more, skill-authoring and optimization-sdk-sync, live under local-skills/. The Claude Code plugin also registers two MCP servers: contentful-mcp for CMS operations and contentful-personalization for structured workflows.

## Installation

The recommended path is the Claude Code plugin, which also wires the two MCP servers:

```text
/plugin marketplace add contentful/skills
/plugin install contentful@contentful
```

Run /reload-plugins to activate. The universal CLI works with Copilot, VS Code, Codex, Gemini CLI and 35+ other platforms:

```bash
npx skills add contentful/skills
```

Install a single skill, or run the plugin locally for testing:

```bash
npx skills add contentful/skills --skill contentful-personalization
claude --plugin-dir /path/to/contentful/skills
```

Gemini CLI users can run gemini skills install contentful/skills. Cursor users can add a remote rule pointing at contentful/skills.

## What It Provides

skills.sh publishes per-skill descriptions for all 12 indexed listings, and each has a matching SKILL.md in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| contentful-custom-app-from-scratch | 3,554 | design, scaffold, build and validate a new App Framework custom app |
| contentful-api | 435 | language-agnostic REST and GraphQL API reference with curl examples |
| contentful-guide | 411 | core concepts and routing to the right skill, API or doc |
| contentful-nextjs | 379 | integrate Contentful into a Next.js project with Draft Mode |
| contentful-migration | 356 | write and run content model migration scripts |
| contentful-personalization | 315 | personalization and A/B testing with the Experiences SDK |
| contentful-custom-app-enhancement | 256 | improve, debug and extend an existing custom app |

The remaining 5 indexed listings range from 1 to 64 installs.

## Why This Matters for Hermes Agents

Contentful is a widely used headless CMS, and its five APIs (CMA, CDA, Preview, Images, GraphQL) plus the App Framework and Experiences SDK are easy for an agent to get subtly wrong. This suite encodes the correct patterns so an agent produces working integrations on the first try: which API to reach for, how to structure a migration, how to wire Next.js Draft Mode, and how to scaffold an App Framework app. The skills are language-agnostic where it matters (a curl-based API reference) and framework-specific where it helps (Next.js, migrations). The Claude Code plugin also registers two MCP servers so the agent can operate against live spaces rather than only recite docs. For a builder, that means "add Contentful to this app" resolves to a curated reference plus a live connection instead of a hallucinated endpoint.

## Usage

| You say | What happens |
|---|---|
| Explain Contentful environments and aliases | Uses contentful-guide to explain concepts and route to the right skill |
| Add Contentful to my Next.js app | Uses contentful-nextjs for SDK setup, fetching and Draft Mode |
| Write a content model migration | Uses contentful-migration to script field and content type changes |
| Build a sidebar app for Contentful | Uses contentful-custom-app-from-scratch to scaffold an App Framework app |
| Fix my existing custom app | Uses contentful-custom-app-enhancement to triage and improve the app |
| Set up A/B testing with the Experiences SDK | Uses contentful-personalization for personalization workflows |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/contentful/skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/contentful/skills/main/skills/contentful-api/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| contentful-custom-app-from-scratch | Pass | Pass | Pass |
| contentful-api | Pass | Pass | Warn |
| contentful-guide | Pass | Pass | Pass |
| contentful-nextjs | Pass | Fail | Warn |
| contentful-migration | Warn | Pass | Warn |
| contentful-personalization | Pass | Warn | Fail |
| contentful-custom-app-enhancement | Pass | Pass | Warn |
| contentful-env-analysis | Pass | Pass | Warn |
| exo-content-bindings | Pass | Pass | Fail |
| channels-destinations | Pass | Pass | Warn |
| skill-authoring | Pass | Pass | Pass |
| optimization-sdk-sync | Pass | Pass | Pass |

Sampled 12 of 12 indexed listings. Three skills carry Fail verdicts: contentful-nextjs (Socket), contentful-personalization (Snyk) and exo-content-bindings (Snyk).

## Limitations

- Snapshot data, verified Nov 25, 2026: 5,870 combined installs across 12 indexed listings; 43 GitHub stars; MIT license; last pushed Nov 25, 2026. Counts drift over time.
- Three of 12 sampled skills carry Fail verdicts on skills.sh; review their security pages before relying on them in production.
- The README's What's inside table lists 10 skills while its badge and quickstart say 8; the index carries 12 listings (those 10 plus skill-authoring and optimization-sdk-sync under local-skills/).
- contentful-env-analysis requires Node.js 24.21+ and a CMA token with read access, and its snapshot files contain customer content that must be kept private.
- The personalization skill is a multi-step state machine built on @contentful/skill-kit; its local MCP server needs manual wiring outside the plugin path.

## Related

[Payload CMS Skills - Schema and Migration Setup](/hermes/skills/catalog/payloadcms-skills-setup) | [Sanity Agent Toolkit - Headless CMS Setup](/hermes/skills/catalog/sanity-agent-toolkit-setup) | [Sanity Context Skills - Structured Content Setup](/hermes/skills/catalog/sanity-context-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with contentful-guide to route to the right skill or API before writing code.
- Install via the Claude Code plugin to get both MCP servers (contentful-mcp and contentful-personalization) wired automatically.
- Pull a single skill with npx skills add contentful/skills --skill contentful-personalization when you only need one.
- Read skills/contentful-env-analysis/references/security.md before using the env-analysis skill, and delete snapshots when done.
- Remember both custom-app skills live under skills/contentful-apps/ in the tree, not at the top level.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
