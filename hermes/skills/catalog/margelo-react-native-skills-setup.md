---
title: "Margelo React Native Skills - Native Modules Setup"
description: "margelo/react-native-skills on skills.sh: 7.7K combined installs; Nitro module, Swift, Kotlin, C++ and VisionCamera skills for React Native agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/margelo-react-native-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "react native", "nitro modules", "mobile"]
---

# Margelo React Native Skills - Setup Guide

**Source:** [margelo/react-native-skills](https://www.skills.sh/margelo/react-native-skills) via skills.sh - 7.7K combined installs across 9 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 179 stars, no LICENSE file in the repository, last pushed 2026-08-21, 9 SKILL.md directories under skills/
**Category:** React Native native-module engineering for agents: Nitro modules, MMKV storage, VisionCamera, networking and Swift, Kotlin and C++ APIs
**Quality Tier:** 🟡 Beta - no LICENSE file in the repository; every sampled audit Pass; 179 stars.

Margelo publishes nine skills for React Native work, and they are narrow on purpose: each one is a router for a specific library rather than a general mobile guide. The set covers `react-native-mmkv` storage, Nitro Module construction with Nitrogen, `react-native-vision-camera` v5 plus a realtime pipeline skill, the `react-native-nitro-fetch` networking stack, and four language and API-design skills for Swift, Kotlin, C++ and TypeScript library surfaces.

The pattern in each skill file is the same. A short mental model, then a routing table that maps a problem to one `references/*.md` file, then an instruction not to load more than the matching reference. The `react-native-mmkv` file even opens by telling the agent to answer from the real APIs of the library instead of invented ones, which is the exact failure this directory is built to prevent.

## Installation

The README documents one install command, followed by an interactive picker:

```bash
npx skills add margelo/react-native-skills
```

Choose the skills you want from the selector rather than installing all nine. The set splits cleanly by project: a storage task needs `react-native-mmkv`, a camera task needs `react-native-vision-camera`, and the Swift, Kotlin, C++ and API-design skills are useful on their own for library work.

The skills are guidance only, so installing one does not add a runtime dependency. The matching npm packages are separate, and the `react-native-nitro-fetch` skill documents the library install for reference:

```bash
npm install react-native-nitro-fetch react-native-nitro-modules
```

After that install, the skill notes that the app has to be rebuilt (`pod install` for iOS and a fresh Gradle build for Android) and that nothing is wired automatically.

## What It Provides

Eight indexed listings, all above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| react-native-mmkv | 1,264 | Configuring MMKV instances, reading and writing value types, reactive hooks, encryption and AsyncStorage migration |
| build-nitro-modules | 1,246 | Building Nitro Modules with Nitrogen, HybridObject TypeScript specs, Nitro views and Swift, Kotlin and C++ bindings |
| api-design | 979 | Designing and reviewing predictable public APIs for TypeScript, JavaScript, React and React Native libraries |
| swift | 906 | Designing, implementing and reviewing Swift APIs, concurrency, actors and Swift-backed Nitro implementations |
| kotlin | 897 | Designing and reviewing Kotlin and Android APIs, nullability, coroutines, threading and Java interop |
| cpp | 874 | Designing and reviewing modern C++ APIs, RAII ownership, CMake, callbacks and platform bridges |
| react-native-vision-camera | 737 | VisionCamera v5 setup, migration from v4, capture, controls, outputs and basic frame processing |
| nitro-fetch | 639 | Native fetch, NitroWebSocket, prefetching, cold-start cache warming, axios adapters and network inspection |

The remaining 1 indexed listing is react-native-vision-camera-realtime at 128 installs, which covers production low-latency GPU, ML, CV, Skia and WebGPU pipelines and frame-coupled overlays.

## Why This Matters for Hermes Agents

Native module work is where an agent's confidence outruns its knowledge. A model that has seen a thousand React Native tutorials will happily invent an `init()` or `setup()` helper for a library that has neither, and the mistake only surfaces at build time on a device.

These skills are structured against that failure. The router pattern means the agent loads one focused reference with real file paths in it, and the `react-native-nitro-fetch` file states the test explicitly: a correct answer cites the API and a reference path, while a wrong one invents a helper that does not exist in the repository.

The language skills are the part that generalises beyond React Native. Swift concurrency and `MainActor` isolation, Kotlin nullability and coroutines, C++ ownership and callbacks are reviewed against written standards instead of the model's recollection, and `api-design` sits above all of them as the cross-language naming and error-behaviour layer.

The camera pair also encodes a version break properly: VisionCamera v5 is a Nitro rewrite with a new constraints API and an output-based architecture, and the skill says to treat it as a new API rather than an incremental upgrade. An agent that does not know that will migrate a v4 app into a non-compiling state.

## Usage

| You say | What happens |
|---|---|
| "Add encrypted key-value storage to this screen" | react-native-mmkv routes to the instance, hooks and encryption references |
| "Migrate our AsyncStorage calls to MMKV" | react-native-mmkv walks the documented migration path and the zustand or redux-persist integration |
| "Create a Nitro Module with a HybridObject spec" | build-nitro-modules scaffolds the spec, runs the Nitrogen generation step and fills the Swift, Kotlin and C++ sides |
| "Review this Swift API for concurrency problems" | swift checks actor isolation, `MainActor` usage and thread-affine state |
| "Why does this Kotlin property crash on null?" | kotlin reviews nullability, platform types and Java interop boundaries |
| "Set up VisionCamera v5 capture in this app" | react-native-vision-camera provides the v5 setup, permissions, outputs and capture flow |
| "Make our cold-start API call feel instant" | nitro-fetch routes to the prefetching reference and the `prefetchOnAppStart` pattern |

## Verification

Read the skill file before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/margelo/react-native-skills/main/skills/react-native-nitro-fetch/SKILL.md | head -8
```

It should open with `name: nitro-fetch` and a description naming `react-native-nitro-fetch`, `react-native-nitro-websockets` and `react-native-nitro-text-decoder`. Note the path: the indexed listing is called `nitro-fetch`, but the directory in the repository is `react-native-nitro-fetch`, so a raw URL built from the listing name alone returns 404. Then confirm what landed:

```bash
ls ~/.claude/skills | grep -E 'react-native|nitro'
```

You should see one directory per skill you selected. A functional check from the skill's own test list: ask "How do I prewarm a websocket connection in this repo?" and expect `prewarmOnAppStart` plus the Android `Application.onCreate` wiring, not a generic reconnect loop.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-native-mmkv | Pass | Pass | Pass |
| build-nitro-modules | Pass | Pass | Pass |
| kotlin | Pass | Pass | Pass |
| react-native-vision-camera-realtime | Pass | Pass | Pass |

All four sampled audits pass, and the skills are Markdown references with no executable payload. The open question is licensing rather than safety: the repository has no LICENSE file at its root, while individual skill files declare `license: MIT` in their frontmatter. Two skills that generate native code (`build-nitro-modules` and the camera guides) produce code you will compile into an app, so review the generated bindings as you would any dependency.

## Limitations

- Snapshot data, verified 2026-11-05: 7,670 combined installs across 9 indexed listings; 179 GitHub stars; no LICENSE file; last pushed 2026-08-21. Counts drift over time.
- No LICENSE file exists in the repository root. Individual SKILL.md files declare MIT in frontmatter, but without a root licence the redistribution terms are unclear, so treat this as source-available until the author resolves it.
- The install index and the tree disagree on one name: `nitro-fetch` is `skills/react-native-nitro-fetch` on disk, so scripted raw fetches need the longer path.
- Guidance only. The skills do not install the libraries; `react-native-nitro-fetch`, `react-native-mmkv` and VisionCamera are separate npm packages, and native changes need a rebuild before anything works.
- `react-native-vision-camera` covers v5 only and treats v4 as a different API. The realtime pipeline skill sits below the threshold at 128 installs, so most projects get the basic camera guidance only.
- 179 stars and a last push of 2026-08-21: a small, single-maintainer surface, so pin what you install and expect library versions to move faster than the skills.

## Related

- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)
- [Awesome Android Agent Skills - Compose and Kotlin Setup](/hermes/skills/catalog/awesome-android-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per project, not globally. The selector exists because a storage skill and a camera skill rarely belong in the same context window.
- Ask the routing question directly ("which reference covers prefetching?") when the first answer looks generic. The skills are built to name the reference file they used.
- Pair `api-design` with whichever language skill matches your module. The language skill covers mechanics, `api-design` covers naming, options objects and error behaviour across the boundary.
- For VisionCamera work, state the version in the prompt. The skill assumes v5, and v4 advice will not compile against it.
- Treat generated Nitro bindings as code under review. The skill produces the spec and the native skeleton, not a tested module.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
