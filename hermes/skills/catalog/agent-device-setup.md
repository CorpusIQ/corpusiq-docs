---
title: "Agent Device - Mobile Device Control for Agents"
description: "callstack/agent-device: 43.9K combined installs. Skills plus a CLI, MCP server and Node API that let agents drive iOS, Android, TV and desktop apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-device-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "mobile testing", "ios simulator", "android emulator", "mcp"]
---

# Agent Device - Setup Guide

**Source:** [callstack/agent-device](https://www.skills.sh/callstack/agent-device) via skills.sh - 43.9K combined installs across 5 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [callstack/agent-device](https://github.com/callstack/agent-device) - 5,248 stars, MIT, branch main, last pushed 2026-11-03; four skill directories under `skills/` (agent-device, android-emulator, dogfood, ios-simulator), each holding a single `SKILL.md`

**Category:** Device control for coding agents: driving mobile, TV, web and desktop apps on simulators, emulators and physical devices

**Quality Tier:** 🟡 Yellow - Snyk warns on the sampled `agent-device` listing while Gen Agent Trust Hub and Socket pass all three sampled skills, and the repository does ship a LICENSE file (MIT)

Agent Device is published by Callstack, the React Native consultancy, and it takes the position that a coding agent should be able to prove a change in the running app rather than reason about a diff. The project is a device layer rather than a test runner: a CLI, a built-in stdio MCP server and a typed Node.js API, all over the same execution path, with sessions, accessibility snapshots and saved evidence as the shared model.

The repository ships four skills around that layer. `agent-device` is the general one: it covers Apple platforms, Android including Android TV and Fire OS, and Amazon Vega OS TV apps, and it is written as a command discipline (start a session, act on refs, read the diff, close) rather than a command reference. `ios-simulator` and `android-emulator` specialise the same discipline per platform, and `dogfood` turns it into exploratory testing: explore the app, find bugs and UX issues, collect evidence.

## Installation

There are two layers to install, and they are independent. The CLI is an npm package, and the README requires Node.js 22.12 or newer, with web automation needing 24 or newer:

```bash
npm install -g agent-device@latest
agent-device doctor
agent-device help workflow
```

Run `doctor` yourself before handing the CLI to an agent. The README is explicit about that ordering, and it is the step that surfaces a missing simulator runtime or a broken ADB bridge before an agent fails on it mid task.

The skills come from skills.sh through the vercel-labs installer. The listing page documents the repository level command, and the `skills/` tree lets you install one skill at a time:

```bash
npx skills add callstack/agent-device
npx skills add callstack/agent-device --skill dogfood
```

For a Hermes profile, a clone plus a copy is the route that keeps the skill text under your control:

```bash
git clone --depth 1 https://github.com/callstack/agent-device.git /tmp/agent-device
cp -r /tmp/agent-device/skills/agent-device ~/.hermes/profiles/corpusiq/skills/
```

If you would rather expose the same commands as structured tools than as shell text, the README documents the MCP server, which runs over stdio:

```json
{
  "mcpServers": {
    "agent-device": {
      "command": "agent-device",
      "args": ["mcp"]
    }
  }
}
```

Pick one route per agent. The MCP server and the CLI share an execution path, so installing both gives the model two ways to do the same thing and a decision to make on every step.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| agent-device | 19,825 | Driving any supported target: iOS, tvOS, macOS, Android including Android TV and Fire TV, and Vega OS TV apps. Navigating apps, snapshotting, driving TV remotes, tapping, typing, scrolling, extracting UI info, collecting evidence, planning CLI commands. |
| dogfood | 11,934 | Exploratory testing of a mobile app on iOS or Android to find bugs, UX problems and rough edges, when asked to dogfood, QA, bug hunt or test the app on a device. |
| ios-simulator | 5,695 | Verifying and debugging native, React Native, Expo or Flutter apps on an iOS Simulator: launch, inspect the live UI, tap, type, scroll, validate a code change, collect failure evidence, reproduce a workflow on iPhone or iPad. |
| android-emulator | 5,169 | The same verify and debug loop on an Android Emulator or virtual device, including launching, inspecting live UI, acting on elements, validating a change and capturing failure evidence. |
| react-devtools | 1,308 | Indexed listing that carries the agent-device description; there is no react-devtools directory in the repository tree, so treat it as an alias for the main skill. |

No indexed listings fall below the threshold; all 5 appear above.

The instruction style is worth reading before you install it. `agent-device` tells the agent to start immediately with `agent-device open <app> --foreground`, which returns the initial interactive snapshot with refs, and it forbids the usual probe sequence of `--help`, `--version`, `devices`, `appstate`, `snapshot` and `screenshot`. Reaching an off-screen element is one command (`scroll down --until <selector>`), not a scroll and check loop, and refs are to be copied byte for byte including any `@` prefix and `~sN` suffix. When a snapshot comes back sparse, the skill says the refs are invalid and tells the agent to take a screenshot, use coordinates, then retry.

Support depth is explicitly uneven, and the skill tells the agent where to check: `agent-device capabilities --platform <platform>` reports what a target supports, and the README names HarmonyOS and Vega OS as backends that cover a subset of commands. Behind the commands sit different transports per platform: an accessibility bridge and XCTest on Apple platforms, ADB on Android, HDC with ArkUI `uitest` on HarmonyOS, the Vega CLI on Vega virtual devices, a local helper on macOS including Electron apps, and AT-SPI on Linux.

## Why This Matters for Hermes Agents

A coding agent that cannot see the app is limited to static reasoning about code, and screenshots alone are a poor interface: expensive in tokens, ambiguous about what is tappable, and hard to assert against. The accessibility snapshot model this suite documents gives the agent a token efficient text tree with refs it can act on, plus a diff after each action, which is a much better fit for an agent loop than an image.

The session model is what makes multi-agent work possible. Sessions are scoped to the caller's git worktree, and host local device claims stop parallel agents from taking over each other's simulators. `agent-device device status` inspects ownership without a daemon, and `agent-device device release --stale` releases claims whose owner is no longer running. On a machine running several Hermes subagents, that is the difference between parallel work and a queue of conflicting taps.

Evidence is a first class output. Screenshots, video, logs, traces, network data, performance samples and crash details can be captured per run, and working steps can be saved as `.ad` scripts for local use or CI, with strict Maestro YAML export when a team already runs Maestro. That turns an agent's verification into something a reviewer can inspect rather than take on faith.

## Usage

| You say | What happens |
|---|---|
| "Open the Contacts app on the iOS simulator and add a contact" | `agent-device open Contacts --platform ios` starts the session and returns the snapshot, then press and fill act on refs with `--settle` after each step. |
| "Explore the checkout flow and tell me what is broken" | `dogfood` drives the flow on a simulator or device, records bugs and UX issues, and collects evidence for each finding instead of only reporting the first failure. |
| "Does this change break the settings screen on Android?" | `android-emulator` launches the app on a virtual device, inspects the live UI, exercises the change, and captures failure evidence if it breaks. |
| "Take a screenshot and a snapshot of what is on screen now" | `agent-device snapshot -i` returns the interactive tree with refs, and `agent-device screenshot` returns an image for the cases where the accessibility tree is sparse. |
| "Save this flow as a script I can run in CI" | The agent records the working steps into an `.ad` replay script, which runs locally or in CI, with Maestro YAML available when the pipeline expects it. |
| "Run the same checks on BrowserStack" | A remote proxy plus a device cloud connection points the same session and evidence model at hosted devices instead of local ones. |
| "Which commands does the Vega target support?" | `agent-device capabilities --platform <target>` answers from the installed CLI, which is the documented way to check a partial backend before scripting it. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/callstack/agent-device/main/skills/agent-device/SKILL.md
```

After a clone, confirm the four skills and the shape of each one:

```bash
git clone --depth 1 https://github.com/callstack/agent-device.git /tmp/agent-device
ls -d /tmp/agent-device/skills/*/ | wc -l
find /tmp/agent-device/skills -name SKILL.md | wc -l
head -3 /tmp/agent-device/skills/dogfood/SKILL.md
```

Both counts should print 4, and `head` should show `name: dogfood` followed by the description the runtime routes on. Then check the CLI layer, which is what the skills actually call:

```bash
agent-device --version
agent-device doctor
agent-device device status
```

`doctor` reports the platform tooling it can find, and `device status` should list no outstanding claims on a quiet machine. If `doctor` fails, the skills will load and every command in them will fail at the first device call, so fix that before installing the skill text.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| agent-device | Pass | Pass | Warn |
| dogfood | Pass | Pass | Pass |
| ios-simulator | Pass | Pass | Pass |

The skill files themselves are Markdown only: four directories, four `SKILL.md` files, no scripts and no references folder. The risk sits in what they instruct. Every skill drives a real device through a globally installed npm package that ships native helpers for macOS, Android and Linux, executes simulators and emulators, and can read app contents through the accessibility layer. Treat that as privileged local automation: it can tap anything on a booted device and capture whatever is on screen, including credentials a human types during a run.

The repository is a full TypeScript monorepo with native components under `apple/`, `android/`, `linux/` and `bin/`, so this is not a Markdown-only install. Pin the CLI version you validated rather than tracking `@latest` on a machine that agents control, and read `SECURITY.md`, which supports only the latest release and asks that reports go through GitHub Security Advisories rather than a public issue.

Remote targets move app data off the host. The README names BrowserStack, AWS Device Farm, TestMu AI and Limrun as supported device clouds, so anything captured from a session against those providers leaves your machine and is subject to their terms. Decide that per project before wiring an agent to a cloud device.

## Limitations

- Snapshot data, verified 2026-11-03: 43,931 combined installs across 5 indexed listings; 5,248 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- The index carries five listings but the tree has four skill directories. `react-devtools` reuses the `agent-device` description verbatim and has no directory, so its 1,308 installs point at instructions that live in the main skill.
- Node.js 22.12 or newer is required for the CLI, and web automation needs 24 or newer. A host pinned to an older runtime will install and then fail.
- Support depth varies by target. HarmonyOS and Vega OS cover a subset of commands, and the skills send the agent to `agent-device capabilities --platform <platform>` rather than promising parity.
- The skills assume the CLI is already installed, on `PATH`, and has passed `doctor`. None of them installs it, and the failure mode when it is missing is a wall of command errors rather than a clear message.
- A tapped or observed device is a live environment. Sessions claim hardware, and two agents on one host can block each other until `device release --stale` clears a claim whose owner is gone.

## Related

- [Open Browser Use Skills - Browser Automation Setup](/hermes/skills/catalog/open-browser-use-setup)
- [Midscene Skills - AI-Powered Visual Browser Automation Setup](/hermes/skills/catalog/midscene-skills-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [Limrun Skills - Cloud iOS & Android Simulator Setup](/hermes/skills/catalog/limrun-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `agent-device doctor` on every machine before an agent touches it. It is the documented first step and it catches the missing runtime that otherwise looks like a broken app.
- Install `ios-simulator` or `android-emulator` for day to day work rather than the general skill. The scoped text is shorter, which matters when four device skills sit in one context window.
- Keep the session habit: open, act with `--settle`, read the diff, close. Leaving sessions open across tasks is what produces stale refs and confusing failures.
- Use `agent-device device release --stale` when parallel agents seem stuck. A claim from a dead worktree blocks the next agent silently.
- Prefer snapshots to screenshots for reasoning and keep screenshots for evidence. The snapshot is the cheaper input, and the skill only falls back to images when the accessibility tree is sparse.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
