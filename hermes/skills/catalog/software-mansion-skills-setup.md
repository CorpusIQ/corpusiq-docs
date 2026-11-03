---
title: "Software Mansion Skills - React Native Suite Setup"
description: "software-mansion-labs/skills: 14.9K combined installs. React Native and Expo skills for Reanimated, Gesture Handler, Fishjam, Radon and worklets."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/software-mansion-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "react native", "expo", "reanimated", "mobile"]
---

# Software Mansion Skills - Setup Guide

**Source:** [software-mansion-labs/skills](https://www.skills.sh/software-mansion-labs/skills) via skills.sh - 14.9K combined installs across 27 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [software-mansion-labs/skills](https://github.com/software-mansion-labs/skills) - 299 stars, no licence file anywhere in the repository (the plugin manifest and eleven SKILL.md frontmatter blocks say MIT, but no LICENSE ships), branch main, last pushed 2026-10-15; 26 SKILL.md files in all: 11 top-level skills under `skills/`, plus 15 sub-skill files nested under `skills/fishjam/references/` (6) and `skills/react-native-best-practices/references/` (9)

**Category:** React Native and Expo development patterns, from debug tooling and build speed to real-time video, haptics and WebGPU shaders

**Quality Tier:** 🟡 Yellow - all three sampled listings pass every auditor, but the repository carries no licence file at all, so the MIT claim exists only in metadata

Software Mansion maintains this suite as a Claude Code plugin, and the README says so in its first line: production-ready patterns for React Native development, packaged as a plugin and optimised for Claude models. The coverage is broad rather than deep in one place: animations, gestures, SVG, on-device AI, rich text, multithreading, audio, JSI, the Radon IDE debug tools, Fishjam real-time video, Detour deep linking, Meta Quest builds, haptics and TypeGPU shaders.

The shape of the repository is worth understanding before installing. It holds 26 `SKILL.md` files but only 11 top-level entry points. Two of those entry points are routers: `react-native-best-practices` is a 25-line index that tells the agent to read `references/<topic>/SKILL.md`, and `fishjam` is a 32-line router to six platform and SDK sub-skills. The rest are single files, with `typegpu` the longest at 458 lines. That split is why the same repository produces 27 indexed listings for 11 install targets.

## Installation

The README documents the plugin route first and calls it recommended:

```
/plugin marketplace add software-mansion-labs/skills
/plugin install skills@swmansion
/reload-plugins
```

Updates come through the same plugin manager with `/plugin marketplace update swmansion`. The second documented route is the skills CLI, which is the one that fits a Hermes profile:

```bash
npx skills add software-mansion-labs/skills
```

For a single skill, clone once and copy the directory you want. Copy the whole directory, never just the file:

```bash
git clone --depth 1 https://github.com/software-mansion-labs/skills.git /tmp/swm-skills
cp -r /tmp/swm-skills/skills/react-native-best-practices ~/.hermes/profiles/corpusiq/skills/
```

That last point is not a style preference. `react-native-best-practices/SKILL.md` is 25 lines and most of those lines are a table pointing at nine reference files; the same holds for `fishjam`, whose six SDK sub-skills live under `references/`. Install the directory, then confirm the references landed next to the router.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| react-native-best-practices | 5,784 | The entry point for React Native and Expo work on the New Architecture, routing to nine sub-skills for animations, gestures, SVG, on-device AI, rich text, multithreading, Bundle Mode, audio and JSI. |
| typegpu | 1,634 | Type-safe WebGPU in TypeScript: use gpu shader functions, tgpu.fn, buffers, textures, bind groups, compute and render pipelines, and the @typegpu/react hooks. |
| radon-mcp | 1,495 | Driving Radon IDE MCP tools against a running app: screenshots, application logs, component tree, network inspector, reload, and React Native doc lookups. |
| expo-horizon | 1,202 | Adding Meta Quest and Horizon OS support to an Expo app: expo-horizon packages, Quest build variants, panel sizing, head tracking and store publishing. |
| rnrepo | 1,100 | RNRepo pre-built native artifacts: setup, prebuild configuration and slow-build troubleshooting, advertised as up to 2x faster native builds. |
| fishjam | 789 | Router for Fishjam hosted WebRTC, pointing to platform fundamentals, the four SDK sub-skills and stream compositions. |
| detour-onboarding | 789 | Detour deferred deep linking from zero: account and dashboard setup, Universal Links, App Links, and SDK install for React Native, iOS, Android and Flutter. |
| migrate-to-detour | 752 | Moving deep linking off Branch or AppsFlyer onto Detour: concept mapping, dashboard configuration, the SDK swap and analytics migration. |
| react-native-moq | 434 | Media over QUIC in React Native: sub-second-latency playback, camera, microphone and screen publishing, and data tracks over a MoQ relay. |
| pulsar-haptics | 422 | Pulsar haptics across React Native, iOS, Android, Kotlin Multiplatform, Flutter and Web, including the Figma MCP haptic bindings. |
| moq-kit | 330 | The native side of MoQ: Swift MoQKit and Kotlin com.swmansion.moqkit SDKs for playback, capture and data tracks on iOS and Android. |
| animations | 34 | Reanimated 4, Skia and WebGPU patterns: CSS transitions, shared values, layout and scroll-driven animation, particles, SDF rendering and 120fps tuning. |
| gestures | 25 | Gesture Handler patterns for tap, pan, pinch, rotation, swipe, long press, fling, hover and drag, with composition and testing notes. |
| multithreading | 23 | react-native-worklets: Worker Runtimes, scheduleOnUI and scheduleOnRN, shared memory, and moving heavy work off the JS thread. |
| svg | 22 | React Native SVG for icons, charts, illustrations and filters, including the SvgUri, SvgXml and SvgCss loading paths. |
| jsi | 14 | The C++ JavaScript Interface: HostObject, HostFunction, NativeState, zero-copy ArrayBuffer, CallInvoker and threading safety. |
| rich-text | 12 | Rich text editing and rendering with react-native-enriched-html and react-native-enriched-markdown: mentions, GFM tables, LaTeX math. |
| on-device-ai | 10 | On-device AI with React Native ExecuTorch: LLMs, vision, OCR, segmentation, speech to text and text to speech, embeddings. |
| audio | 10 | react-native-audio-api: playback, recording, effects, real-time analysis and visualization, audio worklets and session handling. |
| fishjam-react-native-client | 6 | The Fishjam React Native and Expo client: permissions, foreground service, CallKit, RTCView, audio routing and the Expo config plugin. |
| fishjam-react-client | 6 | The browser React client: FishjamProvider, the hook catalog, simulcast, data channels, VAD, livestream playback and a ts-client escape hatch. |
| fishjam-python-server-sdk | 6 | The Python backend SDK for FastAPI, Flask and aiohttp: rooms, peer tokens, notifiers, webhook decoding, voice agents and compositions. |
| fishjam-platform | 6 | Fishjam domain model and auth: room types, management versus peer tokens, Sandbox versus production, notification events and REST endpoints. |
| fishjam-js-server-sdk | 6 | The Node and TypeScript backend SDK: createRoom, createPeer, the notifier, FishjamAgent, livestream tokens and CompositionClient. |

The remaining 3 indexed listings range from 2 to 5 installs.

Two things follow from that table. First, installs cluster at the router: `react-native-best-practices` alone accounts for 5,784 of the 14,921 total, which fits a skill marked MUST USE whenever a `package.json` lists react-native, expo or expo-router. Second, the Fishjam family appears as six separate listings, so the suite's apparent 27-listing breadth is partly one WebRTC product split by SDK language.

## Why This Matters for Hermes Agents

React Native churn is the specific problem here. Reanimated moved to a worklets runtime, the New Architecture changed how native modules are registered, and a model reciting 2023 gesture or audio APIs produces code that compiles in its head and fails on a device. A skill file pinned to the current library generation is cheaper than a retry loop against a Metro bundler.

The router design also fits how a Hermes agent pays for context. Loading `react-native-best-practices` costs 25 lines; the nine reference files behind it are only read when a topic actually comes up. That is the difference between holding a React Native manual in every prompt and opening one chapter on demand.

The suite is strongest where the answer is not derivable from first principles. `radon-mcp` documents named MCP tools for a live app session, so the agent can read logs and screenshots before guessing at a UI bug. `expo-horizon` deliberately ships no vendor documentation and instructs the agent to fetch the current README and Meta pages, which is the honest way to handle hardware that moves faster than a snapshot.

One structural caveat belongs up front: this is a Claude Code plugin first. The slash commands, `/reload-plugins` and the `skills@swmansion` plugin name all belong to that runtime, and the skills CLI route installs the same Markdown without them.

## Usage

| You say | What happens |
|---|---|
| "Add pinch to zoom to this product image" | Picks react-native-best-practices, follows the router to the gestures sub-skill, and writes a Gesture Handler composition for the installed version. |
| "This list janks while scrolling on a 120Hz phone" | Opens the animations sub-skill for Reanimated 4 and scroll-driven patterns, then uses Radon MCP logs to check what is running on the UI thread. |
| "Our iOS build takes twelve minutes, can we cut that?" | Loads rnrepo for prebuilt artifact setup and reads the project's Gradle and CocoaPods configuration against the prebuild options. |
| "We need a video call room with a Python backend" | Reads fishjam-platform for rooms and tokens, then fishjam-python-server-sdk for token minting and webhook handling in FastAPI. |
| "Write a WebGPU shader that averages this buffer" | Uses typegpu for the d.* schema, the compute pipeline and the reference pages on loops and builtins. |
| "Add haptics to the checkout confirmation" | Reads pulsar-haptics for the preset and composer API on the platforms the app ships. |
| "Can we run this Expo app on a Quest 3?" | Follows expo-horizon for expo-horizon-core setup, Quest build flavors and runtime device detection. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/software-mansion-labs/skills/main/skills/react-native-best-practices/SKILL.md
```

After a clone, confirm the file count and that the two routers really do have their references:

```bash
git clone --depth 1 https://github.com/software-mansion-labs/skills.git /tmp/swm-skills
find /tmp/swm-skills/skills -name SKILL.md | wc -l
ls /tmp/swm-skills/skills/react-native-best-practices/references
ls /tmp/swm-skills/skills/fishjam/references
```

The count should print 26, the first listing nine topic directories, and the second six sub-skill directories. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/react-native-best-practices/references
grep -n 'MUST USE' ~/.hermes/profiles/corpusiq/skills/react-native-best-practices/SKILL.md
```

The reference listing should match the clone, and the grep should show the trigger sentence the router uses. A missing `references/` tree is the failure that matters: the skill still loads, then has nothing to route to.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-native-best-practices | Pass | Pass | Pass |
| typegpu | Pass | Pass | Pass |
| radon-mcp | Pass | Pass | Pass |

Loading a skill here runs nothing. The skill directories are Markdown plus a few reference pages; there is no install hook, no dependency and no script that executes when a skill is read. The only code in the repository sits outside `skills/`, in a Go linter under `lint/` and a Go evaluation harness under `evals/`, both built through `Taskfile.yml` by a developer who asks for them. A consuming agent never builds either.

The licence position is the real risk, not the code. There is no `LICENSE` file at the repository root and none anywhere else in the tree, so the default copyright rules apply and the MIT strings in the plugin manifest and in eleven `SKILL.md` frontmatter blocks are declarations rather than a shipped grant. Read that as unresolved for redistribution: run the skills locally, and talk to the maintainer (the plugin manifest lists a swmansion.com contact) before repackaging them into another product.

Two content-level cautions are worth keeping. `expo-horizon` explicitly instructs the agent to fetch vendor READMEs and Meta documentation at run time, so answers depend on network access and on those pages staying up. The Fishjam material states one rule that should survive any refactor: the management token never leaves the backend, and a leaked one is regenerated from the dashboard.

## Limitations

- Snapshot data, verified 2026-11-03: 14,921 combined installs across 27 indexed listings; 299 GitHub stars; no licence file; last pushed 2026-10-15. Counts drift over time.
- The repository has no licence file at all. MIT appears in metadata only, so redistribution and modification rights are not settled by anything in the tree.
- The 27 indexed listings map to 11 install targets. Five of them are Fishjam SDK sub-skills and nine are reference sub-skills inside react-native-best-practices, so install counts partly reflect one product split into parts.
- Both routers are thin by design. Copying only `SKILL.md` gives a 25-line or 32-line index with no content behind it; the `references/` trees are the skill.
- `expo-horizon` ships no bundled documentation and tells the agent to fetch vendor pages, so its output is only as current as the network and those pages.
- The documented first-class route is the Claude Code plugin manager. Outside Claude Code, the slash commands and the plugin update path do not exist, and the skills CLI or a manual copy is what you get.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `react-native-best-practices` first and treat it as the door. It is the highest-install skill in the suite and the only one that decides which of the nine topic files to open.
- Copy directories, not files. The two routers are indexes, and a file-only install leaves an agent with a table of contents and no chapters.
- Say which platform you mean. The Fishjam listings split by SDK language, so "a React Native client with a Node backend" lands on three different skills and saves a wrong first guess.
- Point the agent at Radon MCP before it edits UI code. Reading logs and a screenshot first turns a speculative fix into a measured one.
- Skip the release notes and check the target version. `typegpu` states it targets TypeGPU 0.12 and asks the agent to verify API availability on older releases, which is the pattern to expect elsewhere in the suite.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
