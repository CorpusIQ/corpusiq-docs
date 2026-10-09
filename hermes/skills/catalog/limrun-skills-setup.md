---
title: "Limrun Skills - Cloud iOS & Android Simulator Setup"
description: "Setup guide for Limrun's official agent skills: cloud iOS simulators and Android emulators for agents - Xcode, Gradle, Detox, Maestro, and Expo workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/limrun-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "limrun", "mobile development", "ios simulator", "android emulator"]
---

# Limrun Skills - Setup Guide

**Source:** [limrun-inc/skills](https://www.skills.sh/limrun-inc/skills) via skills.sh - ~74.6K combined installs across 10 indexed listings (8 active skills); first seen Oct 8, 2026 (evening sweep)
**GitHub:** [limrun-inc/skills](https://github.com/limrun-inc/skills) (MIT license; very active - pushed Oct 8, 2026; 8 SKILL.md files under `skills/`; generated plugin manifests with CI validation; 2 stars - publisher-authority justified)
**Category:** Mobile Development / Testing
**Quality Tier:** 🟡 Beta (official Limrun org, the vendor of lim.run cloud simulators; MIT; very active; sampled verdicts predominantly Pass, verified Oct 8, 2026)

Limrun's official skill suite lets a coding agent use remote mobile infrastructure - Xcode, iOS Simulator, and Android Emulator - without any change to its own environment. The repository also packages the skills, together with the Limrun MCP server, as a plugin for every major agent platform. Agents on Linux, Windows, inside containers, or on hosts without macOS tooling can run full mobile build, test, and interaction loops through the `lim` CLI against hosted simulators.

---

## Installation

```bash
# skills CLI (any agent)
npx skills add limrun-inc/skills
```

| Agent | Command |
|---|---|
| Claude Code | `/plugin marketplace add limrun-inc/skills` then `/plugin install limrun@limrun` |
| Codex CLI | `codex plugin marketplace add limrun-inc/skills` then `codex plugin install limrun` |
| Gemini CLI | `gemini extensions install https://github.com/limrun-inc/skills` |
| Cursor | Cursor Marketplace, or copy this repo to `~/.cursor/plugins/local/limrun` |

The plugin bundles all skills plus the remote MCP server at `https://mcp.limrun.com/mcp` (OAuth sign-in on first use, or an org API key as a bearer token).

The `lim` CLI installs the skills into whichever agent you use and keeps them updated:

```bash
npm install --global lim
lim skills install
```

Auth is `lim login` or a `LIM_API_KEY` environment variable. Sign up at [lim.run](https://lim.run) to get a key; if your work email domain has SSO configured and verified, use "Continue with SSO" in the console.

## What It Provides

| Skill | What it does | Installs |
|---|---|---|
| limrun-ios-simulator | Drive an app on a cloud iOS simulator: launch, tap, type, read the accessibility element tree, app logs and syslog, screenshot, record video, connect to local services, camera mocking, clipboard, notifications, timed action chains | 10,516 |
| limrun-detox-testing | Run Detox end-to-end tests against mobile builds on cloud devices | 10,510 |
| limrun-expo-development | Expo and React Native development loop on remote devices | 10,507 |
| limrun-xcode | Build iOS apps with xcodebuild on remote macOS compute | 10,506 |
| limrun-xcode-bazel | Build iOS apps from Bazel workspaces | 10,495 |
| limrun-maestro-testing | Run Maestro flows against mobile builds | 8,539 |
| limrun-gradle | Build Android apps with Gradle remotely | 7,398 |
| limrun-android-emulator | Drive Android emulator instances | 6,094 |

Two stale skills.sh index aliases (`limrun-xcode-and-ios-simulator`, 10 installs; `xcode-and-ios-simulator`, 5 installs) are legacy names of the unified skills above and are not part of the current repository.

## Why This Matters for Hermes Agents

Mobile build and test work normally requires a Mac with Xcode, or a local Android SDK and emulator - none of which exist on typical agent hosts. These skills move the entire loop to Limrun's cloud: the agent asks for a simulator, syncs a build, drives the app, reads logs, and captures screenshots or video, all through one CLI. Because the suite ships through the standard skills and plugin mechanisms, a Hermes agent adds it the same way it adds any other skill, and the bundled MCP server exposes the same capability to tool-calling agents.

## Usage

| You say | What happens |
|---|---|
| "Build the app and show me a screenshot on the simulator" | The build skills produce the bundle; limrun-ios-simulator attaches a simulator, installs it, and captures a screenshot |
| "Run the UI tests" | limrun-detox-testing or limrun-maestro-testing runs the E2E suite against the build |
| "Read the logs" | The iOS skill reads app logs and simulator syslog |
| "Reach my local server from the simulator" | Localhost bridging connects the app to services running in the agent's environment |
| "Record a video of that flow" | The simulator skill records video of the action chain |

The iOS skill is build-agnostic: keep builds in `limrun-xcode` (xcodebuild projects) or `limrun-xcode-bazel` (Bazel workspaces), and use `limrun-ios-simulator` for everything that happens after a build.

## Verification

```bash
# Running instances
lim ios list

# Is a simulator attached to the current build target?
lim xcode get

# Confirm the skills are installed
npx skills list | grep limrun
```

If a create output includes a signed stream URL, the skill shares it as a Markdown link so you can watch the simulator live in a browser.

## Security

skills.sh verdicts sampled across the suite (verified Oct 8, 2026):

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| limrun-ios-simulator | Pass | Pass | Pass |
| limrun-detox-testing | Pass | Pass | Pass |
| limrun-expo-development | Pass | Pass | Pass |
| limrun-xcode | Pass | Pass | Warn |
| limrun-android-emulator | Pass | Pass | Warn |

**Known caution:** these skills execute `lim` CLI commands that create cloud resources, sync builds, and drive emulators - several also invoke build tools (Xcode, Gradle, Bazel) remotely. The two Snyk warnings sit on skills whose workflows shell out to build systems; treat the skill as executing build commands and review them before running in environments you care about. All actions run against your own Limrun account.

## Related

- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup) - official React Native suite; pairs with these skills for the JS layer of mobile work
- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup) - OTA update workflow for React Native apps
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

1. **Let builds finish before driving.** `lim xcode get` shows whether a simulator is already attached to the current build target; attach with `lim ios create --attach` so the last build installs immediately instead of rebuilding.
2. **Share the signed stream URL.** It opens the live simulator without a console login; the console URL requires one. Prefer the signed URL when showing a human what the app is doing.
3. **Check before asking for a key.** `LIM_API_KEY` may already be set in the environment even when `.env` and the shell do not show it - check first.
4. **Use `--help` as the source of truth.** The CLI is the contract; if a flag errors or is missing, consult `lim ios <subcommand> --help` instead of guessing.
5. **Keep build concerns in build skills.** `limrun-xcode` and `limrun-xcode-bazel` own compilation; `limrun-ios-simulator` owns interaction. Mixing the two creates confusing failures.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
