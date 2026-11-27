---
title: "Expo Skills - React Native App Development Suite"
description: "expo/skills: 1227.3K combined installs. Official Expo skills for building, deploying, upgrading and debugging React Native and EAS apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/expo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "expo", "react native", "eas"]
---

# Expo Skills - Setup Guide

**Source:** [expo/skills](https://www.skills.sh/expo/skills) via skills.sh - 1227.3K combined installs across 41 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [expo/skills](https://github.com/expo/skills) - 4,248 stars, MIT, branch main, last pushed 2026-11-27; skills live under `plugins/expo/skills/<name>/SKILL.md`, with `expo-skill-eval` in `.claude/skills/` and the experimental pair (expo-mascot, expo-migrate-module) in `plugins/expo-experiments/skills/`.

**Category:** Expo and React Native app development, EAS deployment, upgrades and debugging for agent runtimes

**Quality Tier:** 🟠 Orange - Socket fails four sampled listings and Snyk warns on nine more.

Expo Skills is the official agent-skill suite from the Expo team, published as an Expo plugin with a companion skills.sh listing. It teaches an agent how Expo work gets done: when to use Expo APIs, how to structure common workflows, and which Expo, EAS, React Native, iOS and Android constraints matter. The README is explicit that Expo documentation, the Expo CLI and the EAS CLI remain the source of truth, and these skills exist to help an agent apply them correctly.

The suite splits into a free, open-source framework group and a paid EAS services group, with each services skill opening on a costs and plan-limits note. The index tracks 41 listings, but several names (building-native-ui, expo-tailwind-setup, native-data-fetching and others) carry install counts while having no SKILL.md in the current tree, so the live suite is a subset of the index.

## Installation

The README splits installation by runtime. For Claude Code and Codex, install the plugin so the official marketplace handles updates; for every other agent, use the skills CLI:

```text
npx skills@latest add expo/skills --skill '*'
```

`--skill '*'` selects every Expo skill without selecting every agent. Add `--agent <agent>` to target one agent directly, then restart or refresh the session so the runtime discovers the installed SKILL.md files. Claude Code and Codex use their official plugin marketplaces instead:

```text
claude plugin install expo@claude-plugins-official
codex plugin add expo@openai-curated
```

The Claude Code equivalent is the `/plugin install expo@claude-plugins-official` slash command, and Codex users can install `expo` from the OpenAI-curated marketplace under `/plugins`. Plugin installs update through those marketplaces; skills CLI installs refresh with `npx skills@latest update`, or per skill with `npx skills@latest update expo-router`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| expo-dev-client | 79,130 | Build and distribute Expo development clients locally or via TestFlight for internal testing. |
| building-native-ui | 58,099 | Building native-feeling Expo screens: Apple HIG styling, semantic colors, native controls, SF Symbols, media, animations and visual effects. |
| expo-tailwind-setup | 53,559 | Setting up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling. |
| expo-module | 52,763 | Create Expo native modules and views with the Expo Modules API in Swift, Kotlin and TypeScript. |
| native-data-fetching | 46,367 | Any network request or data fetching task: the fetch API, React Query, SWR, error handling, caching and offline behaviour. |
| eas-update-insights | 43,034 | Check the health of published EAS updates: crash rates, launch counts, payload size, embedded vs OTA split. |
| upgrading-expo | 42,164 | Upgrading Expo SDK versions and fixing the dependency issues that follow. |
| expo-native-ui | 41,777 | Build native-feeling screens: Apple HIG styling, semantic colors, native controls, SF Symbols, media and gradients. |
| expo-ui | 40,285 | Native UI with @expo/ui: real SwiftUI on iOS and Jetpack Compose on Android. |
| expo-deployment | 40,177 | Shipping to production with EAS: builds and submissions to the iOS App Store, Google Play and TestFlight, plus eas.json configuration. |
| expo-cicd-workflows | 39,234 | Understanding and writing EAS workflow YAML for CI/CD in an Expo project. |
| expo-api-routes | 37,203 | Creating API routes in Expo Router with EAS Hosting. |
| expo-router | 36,357 | Expo Router navigation: file-based routes, groups, dynamic routes, native Stack, modals, form sheets and tabs. |
| expo-data-fetching | 36,290 | API calls, React Query, SWR, caching, retries, offline support and Expo Router data loaders. |
| expo-upgrade | 36,226 | Upgrade Expo SDK versions and fix dependency issues. |
| expo-brownfield | 33,783 | Add Expo and React Native to an existing native iOS or Android app. |
| expo-examples | 33,722 | The expo/examples repo of with-* integrations to adapt, or to scaffold a new project from. |
| eas-app-stores | 30,354 | Build and submit iOS and Android apps with EAS to TestFlight, the App Store or Google Play. |
| use-dom | 30,337 | Running web code in a webview on native and as-is on web with Expo DOM components, migrating incrementally. |

The remaining 21 indexed listings range from 162 to 28,953 installs.

The index also carries one space-named listing the table cannot render: Expo UI SwiftUI (12,853).

Eight of the nineteen listings above (building-native-ui, expo-tailwind-setup, native-data-fetching, upgrading-expo, expo-deployment, expo-cicd-workflows, expo-api-routes and use-dom) carry skills.sh install counts but have no SKILL.md in the current repo tree; their Use For cells come from the description on each skills.sh listing page rather than from a file in the repository.

## Why This Matters for Hermes Agents

Expo Skills is a model of the plugin-first pattern: a single `expo` plugin bundles every skill plus an MCP configuration, so the runtime gets both the knowledge and the live tooling in one install. The README states the Expo MCP server gives an agent live access to read the latest Expo docs, run `npx expo install`, trigger and monitor EAS builds, pull TestFlight crash data and screenshot a running app in a simulator. For a Hermes-style builder, that is the difference between an agent that quotes Expo documentation and one that can act on a real project.

The framework-versus-services split is the useful discipline to copy. Every free, open-source skill is separated from every paid EAS skill, and each services skill opens with a plan-limits note, so an agent can reason about cost before it proposes a paid workflow. The experimental pair ships in a separate `expo-experiments` plugin rather than polluting the stable set, which is a clean release-isolation pattern.

The README also encodes the trust boundary clearly: these skills are guidance, not a source of truth. Expo documentation, the Expo CLI and the EAS CLI remain authoritative, and the skills teach the agent to apply them. That is the right posture for any vendor-authored suite, because it keeps the skill layer disposable as the platform evolves.

For a builder wiring this into a router, the entry point matters: `expo-overview` is documented as the skill to load first for any Expo or EAS task, then route to the specific skill. Installing the whole set without that routing hint leaves the agent guessing which of the 41 listings to open.

## Usage

| You say | What happens |
|---|---|
| "Build a native-feeling Expo Router screen with tabs, modals and animations" | Loads expo-overview to route, then expo-router and expo-animation for the specific pieces. |
| "Create an EAS workflow that builds previews on pull requests" | Uses eas-workflows to write the EAS workflow YAML for CI/CD builds. |
| "Help me upgrade this app to the latest Expo SDK" | Uses expo-upgrade to step through the SDK upgrade and dependency fixes. |
| "Check whether this EAS Update rollout is healthy" | Uses eas-update-insights to read crash rates, launch counts and payload size. |
| "Add a custom native module to my app" | Uses expo-module to create the module with the Expo Modules API in Swift, Kotlin or TypeScript. |
| "Submit my app to the App Store" | Uses eas-app-stores to build and submit via EAS with the signing and versioning steps. |
| "Run my app on a cloud simulator" | Uses eas-simulator to drive a remote iOS or Android simulator from the CLI or an agent. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-dev-client/SKILL.md
```

After a clone, confirm the plugin layout and the number of in-tree skills:

```bash
git clone --depth 1 https://github.com/expo/skills.git /tmp/expo-skills
ls /tmp/expo-skills/plugins/expo/skills/ | wc -l
ls /tmp/expo-skills/plugins/expo-experiments/skills/
head -3 /tmp/expo-skills/plugins/expo/skills/expo-router/SKILL.md
```

The first count should print 23 skill directories, the experiments listing should show expo-mascot and expo-migrate-module, and head should show the expo-router frontmatter. The index names more than 30 listings, so do not expect the tree to hold every indexed name.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| expo-dev-client | Pass | Pass | Warn |
| building-native-ui | Pass | Pass | Pass |
| expo-tailwind-setup | Pass | Pass | Pass |
| expo-module | Pass | Pass | Warn |
| native-data-fetching | Pass | Pass | Pass |
| eas-update-insights | Pass | Pass | Warn |
| upgrading-expo | Pass | Pass | Warn |
| expo-native-ui | Pass | Pass | Pass |
| expo-ui | Pass | Pass | Pass |
| expo-deployment | Pass | Pass | Warn |
| expo-cicd-workflows | Pass | Pass | Warn |
| expo-api-routes | Pass | Pass | Warn |
| expo-router | Pass | Pass | Pass |
| expo-data-fetching | Pass | Pass | Pass |
| expo-upgrade | Pass | Pass | Fail |
| expo-brownfield | Pass | Pass | Fail |
| expo-examples | Pass | Pass | Fail |
| eas-app-stores | Pass | Pass | Warn |
| use-dom | Pass | Pass | Pass |
| expo-project-structure | Pass | Pass | Pass |
| eas-workflows | Pass | Pass | Warn |
| expo-skill-eval | Pass | Pass | Pass |
| expo-dom | Pass | Pass | Pass |
| eas-simulator | Pass | Pass | Fail |

This guide is Orange because Socket fails four sampled listings (expo-upgrade, expo-brownfield, expo-examples and eas-simulator) and Snyk warns on nine more. The Gen Agent Trust Hub passes every sampled listing. The repository is mostly Markdown skills plus TypeScript scripts under `scripts/` and an `.eas/workflows/` CI definition, so the Socket flags are worth reading on the skills.sh security pages rather than treating this suite as inert documentation.

## Limitations

- Snapshot data, verified 2026-11-27: 1,227,285 combined installs across 41 indexed listings; 4,248 GitHub stars; MIT; last pushed 2026-11-27. Counts drift over time.
- The install index outruns the tree: fifteen listings, including eight above the table cut-off, carry install counts but have no SKILL.md in the current repo tree.
- The EAS services skills (eas-app-stores, eas-hosting, eas-workflows, eas-observe, eas-update, eas-update-insights, eas-simulator) describe paid Expo Application Services workflows; the free-versus-paid boundary is documented per skill, not at the repo level.
- The suite is a plugin: full functionality, including the bundled MCP configuration, arrives through the Claude Code or Codex plugin marketplace, not through a bare skills CLI install on those runtimes.
- Expo documentation, the Expo CLI and the EAS CLI are the stated source of truth; the skills are guidance layered on top and can drift as the platform releases.
- Four of the twenty-four sampled listings fail the Socket audit; the failure reasons are not published beside the verdicts, so check the security pages on skills.sh before installing into a production profile.

## Related

- [Mobile App UI Design Skill - Mobile Interface Setup](/hermes/skills/catalog/mobile-app-ui-design-skill-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `expo-overview` first, then route to the specific skill. The README documents it as the entry point, and it is the cheapest way to avoid the agent opening the wrong listing from 41 names.
- Use the plugin on Claude Code and Codex, not the skills CLI, so the MCP configuration and updates arrive through the official marketplace.
- When the tree and the index disagree, trust the tree: the current SKILL.md files are what installs, and several indexed names have no counterpart on disk.
- Separate free from paid in your own routing. The services skills carry a plan-limits note, so surface that note before an agent proposes an EAS-heavy workflow.
- Keep the "source of truth" framing in your prompts: Expo docs, Expo CLI and EAS CLI win over any skill, which keeps the skill layer safely disposable.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
