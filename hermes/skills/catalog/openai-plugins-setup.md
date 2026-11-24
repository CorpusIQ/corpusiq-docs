---
title: "OpenAI Plugins - Codex Plugin Examples Setup"
description: "openai/plugins - 6.2K combined installs: OpenAI's Codex plugin examples for web, iOS, macOS and game building."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openai-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "openai", "codex", "plugin"]
---

# OpenAI Plugins - Codex Plugin Examples Setup

**Source:** [openai/plugins](https://www.skills.sh/openai/plugins) via skills.sh - 6.2K combined installs across 52 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [openai/plugins](https://github.com/openai/plugins) - 8,294 stars, no LICENSE file, main branch, last pushed Nov 18, 2026; one plugin per directory under plugins/ with a required .codex-plugin/plugin.json manifest, plus the plugin-creator skill under .agents/skills/.
**Category:** Developer Tooling and Plugin Examples
**Quality Tier:** 🟡 Yellow - frontend-testing-debugging carries one Warn cell (Snyk); the other 19 sampled skills pass all three checks.

This is OpenAI's own plugins repository, a curated collection of Codex plugin examples rather than a single skill library. Each plugin lives under plugins/<name>/ with a required .codex-plugin/plugin.json manifest and optional surfaces such as skills/, .app.json, .mcp.json, agents/, commands/, hooks.json and assets/. The default marketplace manifest at .agents/plugins/marketplace.json points at the standard plugins/ directory, and API-key login users get a separate marketplace at .agents/plugins/api_marketplace.json.

The collection spans iOS and macOS app building, web app building, data visualization, security scanning, Canva, Figma and game development. It is example-first: highlighted bundles cover Figma, Notion, build-ios-apps, build-macos-apps, build-web-apps, Expo, Netlify, Remotion and Google Slides. The repository carries no LICENSE file, so treat the examples as reference material rather than a clearly licensed dependency until you confirm terms with OpenAI.

## Installation

Add the skills with the Agent Skills installer:

```bash
npx skills add openai/plugins
```

For native Codex plugin use, the repository is itself a marketplace: .agents/plugins/marketplace.json points at the standard plugins/ directory, and each plugin carries its own .codex-plugin/plugin.json manifest, so Codex can add this repository as a marketplace and install plugins individually.

Because this is a many-plugin repository, install the specific plugins you need rather than the whole tree. Each plugin directory is self-contained, so a plugin can also be copied or linked into a local agent skill directory and read directly.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ios-memgraph-leaks | 1,595 | capturing and summarizing iOS memory graph leaks |
| frontend-app-builder | 408 | building frontend web apps |
| plugin-creator | 355 | scaffolding a new Codex plugin |
| android-emulator-qa | 350 | QA against the Android emulator |
| frontend-testing-debugging | 226 | frontend testing and debugging |
| game-ui-frontend | 204 | game UI frontend work |
| game-playtest | 144 | playtesting a game build |
| liquid-glass | 110 | the liquid glass UI effect |
| ios-app-intents | 108 | iOS App Intents |
| appkit-interop | 106 | AppKit interop in macOS apps |
| shadcn | 105 | shadcn UI component work |
| web-3d-asset-pipeline | 103 | the web 3D asset pipeline |
| signing-entitlements | 102 | code signing and entitlements |

The remaining 39 indexed listings range from 33 to 97 installs.

## Why This Matters for Hermes Agents

OpenAI's plugins repository is the reference point for how a Codex plugin is structured, which makes it the fastest way to learn the format by example. The plugin-creator skill documents the plugin.json spec and ships a script that scaffolds a basic plugin, so an agent asked to build a plugin can start from a working manifest instead of guessing the fields. For an operator who wants to extend an agent with a domain skill, the repository shows the full surface area a plugin can expose, skills, MCP servers, commands, hooks and assets, all in one place.

The example plugins are also immediately useful on their own. build-ios-apps and build-macos-apps carry the highest-install listing, ios-memgraph-leaks, alongside practical skills for App Intents, AppKit interop, signing and entitlements, and the liquid glass effect. build-web-apps covers frontend building and testing, shadcn and Stripe best practices, while the data visualization plugin ships a large reference library for charts, dashboards and interactive visualizations.

The tradeoff is that this is a broad example collection, not a hardened product. There is no LICENSE file, the README is a short index rather than install documentation, and most listings sit below 100 installs, so treat the popular subset as reliable and the long tail as exploratory.

## Usage

| You say | What happens |
|---|---|
| Scaffold a new Codex plugin | Uses plugin-creator for the spec and a basic plugin script |
| Find and fix an iOS memory leak | Uses ios-memgraph-leaks to capture and summarize a memgraph |
| Build a macOS settings window with AppKit | Uses appkit-interop for AppKit interop guidance |
| Add the liquid glass effect to my SwiftUI app | Uses liquid-glass for the effect |
| Build a product landing page | Uses frontend-app-builder for the web app structure |
| Test and debug a frontend build | Uses frontend-testing-debugging for the test and debug loop |
| Add a shadcn component to my React app | Uses shadcn for component guidance |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/openai/plugins/main/README.md | head -40
```

Confirm the plugin-creator skill body is present before scaffolding work:

```bash
curl -sL https://raw.githubusercontent.com/openai/plugins/main/.agents/skills/plugin-creator/SKILL.md | head -30
```

Confirm the memory graph skill body is present before iOS diagnostics:

```bash
curl -sL https://raw.githubusercontent.com/openai/plugins/main/plugins/build-ios-apps/skills/ios-memgraph-leaks/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ios-memgraph-leaks | Pass | Pass | Pass |
| frontend-app-builder | Pass | Pass | Pass |
| plugin-creator | Pass | Pass | Pass |
| android-emulator-qa | Pass | Pass | Pass |
| frontend-testing-debugging | Pass | Pass | Warn |
| game-ui-frontend | Pass | Pass | Pass |
| game-playtest | Pass | Pass | Pass |
| liquid-glass | Pass | Pass | Pass |
| ios-app-intents | Pass | Pass | Pass |
| appkit-interop | Pass | Pass | Pass |
| shadcn | Pass | Pass | Pass |
| web-3d-asset-pipeline | Pass | Pass | Pass |
| signing-entitlements | Pass | Pass | Pass |
| web-game-foundations | Pass | Pass | Pass |
| ios-ettrace-performance | Pass | Pass | Pass |
| game-studio | Pass | Pass | Pass |
| react-best-practices | Pass | Pass | Pass |
| sprite-pipeline | Pass | Pass | Pass |
| packaging-notarization | Pass | Pass | Pass |
| telemetry | Pass | Pass | Pass |

The single Warn cell sits on frontend-testing-debugging (Snyk). Every other sampled skill passes Gen Agent Trust Hub, Socket and Snyk.

## Limitations

- Snapshot data, verified Nov 23, 2026: 6,211 combined installs across 52 indexed listings; 8,294 GitHub stars; no LICENSE file; last pushed Nov 18, 2026. Counts drift over time.
- The repository carries no LICENSE file, so the examples are not clearly licensed for redistribution or reuse until you confirm terms with OpenAI.
- The README is a short index with no install commands, so the skills.sh installer command is the only fetched install source.
- The install index ships no per-skill descriptions, so every Use For cell is name-level and grounded only in the skill name and its plugin directory.
- Most listings sit well below 100 installs, and the long tail is exploratory rather than battle-tested.
- Some plugins bundle MCP servers and scripts (for example the codex-security and cloudflare plugins), which carry a larger audit surface than Markdown-only skills.

## Related

- [OpenAI Codex Skills Setup](/hermes/skills/catalog/openai-codex-skills-setup)
- [OpenAI Agents Python Skills Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [ChatGPT Skills Setup](/hermes/skills/catalog/chatgpt-skills-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one plugin at a time from this repository; the whole tree is too large to add to every agent.
- Read plugin-creator's plugin-json-spec reference before writing a manifest, and reuse its create_basic_plugin script as the starting point.
- Prefer the plugins with actual skill directories over metadata-only examples when you need working behaviour.
- Confirm the license situation with OpenAI before vendoring any example into a shipped product, since the repo has no LICENSE file.
- Treat the data visualization and codex-security plugins as their own audit surface, because they bundle MCP servers and scripts rather than Markdown-only skills.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
