---
title: "Runway Dev Skills - AI Media Generation Setup"
description: "runwayml/skills: Runway Dev skills and MCP for building AI video, image and audio generation into apps - 7.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/runway-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "runway", "ai video", "media generation", "mcp"]
---

# Runway Dev Skills - AI Media Generation Setup

**Source:** [runwayml/skills](https://www.skills.sh/runwayml/skills) via skills.sh - 7.9K combined installs across 38 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [runwayml/skills](https://github.com/runwayml/skills) - 76 stars, MIT license, main branch, last pushed Oct 30, 2026; seven active skills under skills/ (mirrored in claude/skills/) with root, claude/ and .cursor-plugin/ plugin configuration files and MCP configuration.
**Category:** AI Video, Image and Audio Generation
**Quality Tier:** 🟠 Orange - 1 Fail cell and 6 Warn cells across the 20-skill sample: Gen Agent Trust Hub Fails on rw-generate-video, and Snyk Warns on six integration and reference skills.

Runway Dev helps a coding agent build AI video, image and audio generation into applications with the Runway API, using Runway's own models alongside the best from other labs. The repository is the plugin: its root configuration and MCP connection load the seven active skills in skills/, and Claude Code uses a separate claude/ folder with its own configuration and skill copies.

The included Runway Dev MCP connects an agent to the Runway Developer Portal so it can look up available models, prices and limits, set up Model Routers by cost, speed or quality with an optional credit cap, and manage real-time avatars. The skills show the agent how to integrate the API through the official SDKs and how to build with models, Model Routers, Recipes, Workflows and real-time avatars. Installing the plugin does not configure an application's API key or create a Runway account.

## Installation

Install through the Runway-maintained Claude Code marketplace:

```sh
claude plugin marketplace add runwayml/skills
claude plugin install runway-api@runway-dev
```

Standalone installation works for compatible agents without the plugin:

```sh
npx skills add runwayml/skills --skill runway-dev --skill runway-dev-models --agent cursor claude-code codex
```

Codex uses `codex plugin marketplace add runwayml/skills` followed by `codex plugin add runway-api@runway-dev`, and Replit installs the setup, foundation and surface skills separately from its MCP connection. The install ID is runway-api and the display name is Runway Dev.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| runway-dev | 951 | building, modifying and debugging Runway Dev app integrations through the official SDK |
| runway-dev-models | 846 | adding and maintaining direct Runway Dev model endpoints for image, video, audio or task handling |
| rw-generate-video | 591 | generating video with Runway |
| use-runway-api | 364 | using the Runway API |
| rw-generate-image | 324 | generating images with Runway |
| rw-check-org-details | 316 | checking organization account details |
| rw-generate-audio | 309 | generating audio with Runway |
| rw-api-reference | 262 | referencing the Runway API surface |
| rw-integrate-uploads | 247 | integrating uploads into an app |
| rw-integrate-video | 241 | integrating video generation into an app |
| rw-setup-api-key | 240 | setting up the Runway API key |
| rw-fetch-api-reference | 230 | fetching the Runway API reference |
| rw-integrate-image | 225 | integrating image generation into an app |
| rw-recipe-full-setup | 223 | setting up a full Recipe pipeline |
| rw-integrate-characters | 222 | integrating real-time Characters into an app |
| rw-check-compatibility | 220 | checking SDK compatibility |
| rw-integrate-documents | 218 | integrating document generation into an app |
| runway-dev-recipes | 217 | implementing documented Recipe pipelines |
| rw-integrate-audio | 216 | integrating audio generation into an app |
| rw-integrate-character-embed | 211 | integrating character embedding into an app |

The remaining 18 indexed listings range from 31 to 177 installs.

## Why This Matters for Hermes Agents

An agent that builds against Runway without these skills will hardcode model names and prices that drift, and will mishandle the API credential. The skills replace that with the live contract: runway-dev defines the shared server boundary and keeps credentials server-side, and runway-dev-models pins the exact endpoint contract for image, video, audio and task handling. The MCP is the highest-value piece for an operator, since it looks up available models, prices and limits and can set up Model Routers by cost, speed or quality. The credential model is explicit and worth enforcing in any integration: MCP uses browser OAuth and must not carry an API key, while the application keeps its own server-side RUNWAYML_API_SECRET out of browser bundles, chat and source control. No model catalog or prices are pinned in the README, so the agent should always fetch the current docs rather than trust a remembered figure.

## Usage

| You say | What happens |
|---|---|
| Connect my Runway account | Run the runway-dev-setup skill and complete browser sign-in and consent yourself |
| Add video generation to my app | The runway-dev-models skill drives the model endpoint through the official SDK |
| Set up a Model Router by cost or quality | The runway-dev-model-routers skill and MCP configure the router with a credit cap |
| Generate an image | The rw-generate-image path generates an image through the Runway API |
| Integrate a documented Recipe | The runway-dev-recipes skill reads the live Recipe guide for inputs, version and SDK method |
| Add real-time avatars | The runway-dev-characters skill integrates Characters and Sessions |
| Check which models are available | The MCP looks up models, prices and limits from the Developer Portal |

## Verification

Confirm the foundation skill resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/runwayml/skills/main/skills/runway-dev/SKILL.md | head -30
```

Confirm the model endpoint skill body is present:

```bash
curl -sL https://raw.githubusercontent.com/runwayml/skills/main/skills/runway-dev-models/SKILL.md | head -30
```

Spot-check the Recipe skill to confirm the skills/ layout:

```bash
curl -sL https://raw.githubusercontent.com/runwayml/skills/main/skills/runway-dev-recipes/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| runway-dev | Pass | Pass | Pass |
| runway-dev-models | Pass | Pass | Pass |
| rw-generate-video | Fail | Pass | Pass |
| use-runway-api | Pass | Pass | Warn |
| rw-generate-image | Pass | Pass | Pass |
| rw-check-org-details | Pass | Pass | Pass |
| rw-generate-audio | Pass | Pass | Pass |
| rw-api-reference | Pass | Pass | Warn |
| rw-integrate-uploads | Pass | Pass | Pass |
| rw-integrate-video | Pass | Pass | Warn |
| rw-setup-api-key | Pass | Pass | Pass |
| rw-fetch-api-reference | Pass | Pass | Warn |
| rw-integrate-image | Pass | Pass | Warn |
| rw-recipe-full-setup | Pass | Pass | Warn |
| rw-integrate-characters | Pass | Pass | Pass |
| rw-check-compatibility | Pass | Pass | Pass |
| rw-integrate-documents | Pass | Pass | Pass |
| runway-dev-recipes | Pass | Pass | Pass |
| rw-integrate-audio | Pass | Pass | Pass |
| rw-integrate-character-embed | Pass | Pass | Pass |

The only Fail cell is Gen Agent Trust Hub on rw-generate-video; Snyk Warns on six integration and reference skills, and 18 of the 38 indexed listings were outside the 20-skill sample.

## Limitations

- Snapshot data, verified Nov 23, 2026: 7,889 combined installs across 38 indexed listings; 76 GitHub stars; MIT license; last pushed Oct 30, 2026. Counts drift over time.
- The install index lists 38 names but the repository ships seven active skills under skills/; most rw-* listings (rw-generate-video, rw-integrate-image and others) have no matching directory in the current tree, and the plain-name listings such as api-reference and integrate-image are near-duplicates of their rw-* counterparts.
- The Claude plugin lives in claude/ with its own configuration, MCP endpoint and skill copies; its MCP omits the create_avatar tool, and there is no generated copy step, so a change to skills/ must be mirrored in claude/skills/ by hand.
- No model catalog or prices are pinned in the README; agents must fetch the current docs at docs.dev.runwayml.com for live contracts.
- The Anthropic-managed runway-api@claude-plugins-official listing may pin a different version from the Runway-maintained marketplace.

## Related

- [ai-video-generation - AI Video Production (196K installs)](/hermes/skills/catalog/ai-video-generation-setup)
- [HeyGen Skills - Avatar Video Production Setup](/hermes/skills/catalog/heygen-skills-setup)
- [Replicate Skills - Model Discovery and Inference](/hermes/skills/catalog/replicate-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pick one install path per skill (plugin or standalone) to avoid duplicate copies; standalone skills do not automatically configure MCP.
- Run runway-dev-setup first to connect the account, and complete browser sign-in and consent yourself.
- Keep RUNWAYML_API_SECRET server-side and out of browser bundles, chat and source control; API generations may consume credits.
- Use the MCP for live model, price and limit lookup instead of hardcoding values into an integration.
- For real-time avatars, create them in the Developer Portal; the Claude MCP endpoint omits the create_avatar tool.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
