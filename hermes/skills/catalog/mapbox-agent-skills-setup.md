---
title: "Mapbox Agent Skills - Location Development Suite Setup"
description: "Mapbox Agent Skills: 33.9K combined installs. 20 official skills for web, iOS, Android and Flutter maps, styles, search and token security."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mapbox-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "maps", "geospatial", "location"]
---

# Mapbox Agent Skills - Setup Guide

**Source:** [mapbox/mapbox-agent-skills](https://www.skills.sh/mapbox/mapbox-agent-skills) via skills.sh - 33.9K combined installs across 20 indexed listings; new to this catalog in the Oct 22, 2026 sweep

**GitHub:** [mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills) - 82 stars, MIT license, last pushed 2026-10-01, branch main

**Category:** Developer Tooling / Geospatial and Maps

**Quality Tier:** 🟢 Production - MIT, published by Mapbox itself, 20 indexed listings against 20 skill directories one to one, a changelog and CI checks in the repo, and Pass from all three auditors on every sampled skill

Mapbox Agent Skills is Mapbox's own skill library for location work. It covers the whole delivery surface a maps feature touches: web integration for React, Vue, Svelte and Angular, native patterns for iOS, Android and Flutter, styling and cartography, search and geocoding, data visualization, store locators, navigation, token security, and two MCP integrations for agents that need geospatial tools at runtime.

This guide covers installation, what each of the 20 indexed skills does, and where the suite fits in a Hermes workflow. Installation counts come from the October 22, 2026 sweep of skills.sh.

## Installation

The README offers the skills CLI and a plugin route:

```bash
# Skills CLI
npx skills add mapbox/mapbox-agent-skills

# A single skill
npx skills add mapbox/mapbox-agent-skills --skill mapbox-web-performance-patterns

# As an Open Plugins or Claude Code plugin
/plugin marketplace add mapbox/mapbox-agent-skills
/plugin install mapbox
```

Installing a single skill is usually the right call when a project only needs one surface, for example performance work on an existing web map. The full install is the better default for a new project, because the style, cartography and token security skills are most useful while the map is being designed rather than after it ships.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mapbox-web-integration-patterns | 2,585 | Official integration patterns for Mapbox GL JS across popular web frameworks (React, Vue, Svelte, Angular). Covers setup, lifecycle management, token handling, search integration and common pitfalls. Based on the create-web-app scaffolding tool. |
| mapbox-web-performance-patterns | 2,449 | Performance optimization patterns for Mapbox GL JS web applications. Covers initialization waterfalls, bundle size, rendering performance, memory management and web optimization, prioritized by impact on user experience. |
| mapbox-style-patterns | 2,327 | Common style patterns, layer configurations and recipes for typical mapping scenarios including restaurant finders, real estate, data visualization, navigation and delivery or logistics. Use when implementing a specific map use case or looking for proven style patterns. |
| mapbox-geospatial-operations | 2,212 | Expert guidance on choosing the right geospatial tool based on problem type, accuracy requirements and performance needs. |
| mapbox-data-visualization-patterns | 2,087 | Patterns for visualizing data on maps including choropleth maps, heat maps, 3D visualizations, data-driven styling and animated data. Covers layer types, color scales and performance optimization. |
| mapbox-cartography | 2,084 | Expert guidance on map design principles, color theory, visual hierarchy, typography and cartographic best practices for effective and beautiful maps. Use when designing map styles, choosing colors or making cartographic decisions. |
| mapbox-style-quality | 1,964 | Expert guidance on validating, optimizing and assuring the quality of Mapbox styles through validation, accessibility checks and optimization. Use when preparing styles for production, debugging issues or enforcing map quality standards. |
| mapbox-token-security | 1,893 | Security best practices for Mapbox access tokens, including scope management, URL restrictions, rotation strategies and protecting sensitive data. Use when creating, managing or advising on token security. |
| mapbox-search-integration | 1,864 | Complete workflow for implementing Mapbox search in applications, from discovery questions through to a production-ready integration with best practices. |
| mapbox-search-patterns | 1,792 | Expert guidance on choosing the right Mapbox search tool and parameters for geocoding, POI search and location discovery. |
| mapbox-store-locator-patterns | 1,671 | Common patterns for building store locators, restaurant finders and location-based search applications with Mapbox. Covers marker display, filtering, distance calculation and interactive lists. |
| mapbox-mcp-devkit-patterns | 1,493 | Integration patterns for the Mapbox MCP DevKit Server in AI coding assistants. Covers setup, style management, token management, validation workflows and documentation access through MCP. Use when building Mapbox applications with AI coding assistance. |
| mapbox-ios-patterns | 1,450 | Official integration patterns for the Mapbox Maps SDK on iOS. Covers installation, adding markers, user location, custom data, styles, camera control and featureset interactions. Based on official Mapbox documentation. |
| mapbox-android-patterns | 1,428 | Official integration patterns for the Mapbox Maps SDK on Android. Covers installation, adding markers, user location, custom data, styles, camera control and featureset interactions. Based on official Mapbox documentation. |
| mapbox-google-maps-migration | 1,400 | Migration guide for developers moving from Google Maps Platform to Mapbox GL JS, covering API equivalents, pattern translations and key differences. |
| mapbox-mcp-runtime-patterns | 1,379 | Integration patterns for the Mapbox MCP Server in AI applications and agent frameworks. Covers runtime integration with pydantic-ai, mastra, LangChain and custom agents. Use when building AI-powered applications that need geospatial capabilities. |
| mapbox-maplibre-migration | 1,358 | Guide for migrating from MapLibre GL JS to Mapbox GL JS, covering API compatibility, token setup, style configuration and the benefits of Mapbox's official support and ecosystem. |
| mapbox-location-grounding | 1,259 | Composes Mapbox MCP tools to produce grounded, cited, location-aware responses from live data instead of training data. |
| mapbox-flutter-patterns | 782 | Official integration patterns for the Mapbox Maps Flutter SDK. Covers installation, iOS and Android platform setup, access token configuration, MapWidget initialization, camera control, annotations with tap handling, user location and loading GeoJSON. Based on official Mapbox documentation. |
| mapbox-navigation-patterns | 392 | Navigation implementation patterns for turn-by-turn directions, route optimization, real-time traffic, multi-stop routing and voice guidance across web, iOS and Android platforms. |

All 20 indexed listings clear the 300-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Location is one of the most common places an agent has to leave its training data behind. An agent that answers "where is the nearest store" or "what is at this address" needs live geocoding, a style it can render, and a token that is scoped to the calling surface. This suite supplies guidance for all three as skills, so the agent loads the pattern it needs instead of reconstructing an integration from vendor prose.

The two MCP skills are the more direct fit for Hermes. mapbox-mcp-runtime-patterns covers wiring the Mapbox MCP Server into agent frameworks including pydantic-ai, mastra, LangChain and custom agents, and mapbox-location-grounding covers composing those MCP tools into grounded, cited answers from live data. Together they describe the path from a Hermes tool call to an answer with a location behind it rather than a guess.

## Usage

The skills are documentation-shaped, so the loop is: install, then ask for the task in the vocabulary of the skill names.

- For a new web map, start with mapbox-web-integration-patterns, then design against mapbox-style-patterns and mapbox-cartography.
- Before launch, run mapbox-web-performance-patterns and mapbox-style-quality against the implementation.
- For search and locators, pair mapbox-search-integration with mapbox-store-locator-patterns.
- For token work, use mapbox-token-security to set scopes, URL restrictions and a rotation plan.
- For agent features, use mapbox-mcp-runtime-patterns at runtime and mapbox-location-grounding when answers must be cited.

## Verification

Each skill has its own SKILL.md on main, so a raw fetch is enough to confirm the install target exists:

```bash
for s in mapbox-web-integration-patterns mapbox-web-performance-patterns mapbox-style-patterns; do
  curl -sL -o /dev/null -w "%{http_code} $s\n" \
    "https://raw.githubusercontent.com/mapbox/mapbox-agent-skills/main/skills/$s/SKILL.md"
done
```

The three paths can also be read directly when a pattern question comes up:

- https://raw.githubusercontent.com/mapbox/mapbox-agent-skills/main/skills/mapbox-web-integration-patterns/SKILL.md
- https://raw.githubusercontent.com/mapbox/mapbox-agent-skills/main/skills/mapbox-web-performance-patterns/SKILL.md
- https://raw.githubusercontent.com/mapbox/mapbox-agent-skills/main/skills/mapbox-style-patterns/SKILL.md

The listings and the tree line up one to one at 20 skills, so a local directory count is a valid second check after `npx skills add`.

## Security

Sampled verdicts from skills.sh, verified October 22, 2026:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mapbox-web-integration-patterns | Pass | Pass | Pass |
| mapbox-web-performance-patterns | Pass | Pass | Pass |
| mapbox-style-patterns | Pass | Pass | Pass |
| mapbox-geospatial-operations | Pass | Pass | Pass |
| mapbox-data-visualization-patterns | Pass | Pass | Pass |

Every sampled skill passes all three auditors. The two operational risk areas sit outside that sample. mapbox-mcp-devkit-patterns covers token management through the MCP DevKit Server, and mapbox-mcp-runtime-patterns wires the Mapbox MCP Server into agent runtimes including pydantic-ai, mastra and LangChain. Neither was sampled, so the all-Pass result does not speak for them. Read both, plus mapbox-token-security, before an agent is given a live token, and keep tokens scoped per surface rather than shared across web, mobile and agent use.

## Limitations

- Snapshot data, verified October 22, 2026: 33869 combined installs across 20 indexed listings; 82 GitHub stars; license MIT; last pushed 2026-10-01. Counts drift over time.
- The star count is low at 82, and it should not be read as a quality signal in either direction. This is the official Mapbox repository, so the install base and the auditor results are the more meaningful indicators.
- The repository has no description field, so positioning has to come from the skills themselves rather than from a repo summary.
- The last push is 2026-10-01, three weeks before this snapshot. Recent enough to be maintained, old enough that a specific pattern may lag the current SDK release.
- The suite is patterns and guidance, not a runtime library. Nothing here ships an SDK; the skills describe how to use the Mapbox SDKs themselves.

## Related

- [MCP Use Setup - Fullstack MCP Framework for Hermes](/hermes/skills/catalog/mcp-use-setup)
- [Chrome DevTools MCP Skills - Browser Debugging & Automation Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup)
- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)

## Pro Tips

- Install the full suite for a new project. The style and cartography skills change decisions early, and installing them later means redesigning layers.
- Read mapbox-token-security before you create the first token, not after the first leak. URL restrictions are cheap to set and painful to retrofit.
- When migrating, the two migration skills are the ones to load: mapbox-google-maps-migration for Google Maps Platform and mapbox-maplibre-migration for MapLibre GL JS.
- Use mapbox-style-quality as a pre-launch gate alongside the performance patterns; both catch issues that do not show up in a functional test.
- For agent work, start from mapbox-location-grounding. It frames the answer shape first, which makes the MCP wiring decisions obvious.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
