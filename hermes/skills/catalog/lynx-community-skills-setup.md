---
title: "Lynx Agent Skills - DevTool and ReactLynx Setup"
description: "lynx-community/skills: 10.3K combined installs. Twenty Apache-2.0 listings for Lynx: DevTool CDP debugging, ReactLynx rules, traces and bundle size."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lynx-community-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "lynx", "reactlynx", "mobile", "debugging"]
---

# Lynx Agent Skills - Setup Guide

**Source:** [lynx-community/skills](https://www.skills.sh/lynx-community/skills) via skills.sh - 10.3K combined installs across 20 indexed listings; first documented 2026-11-02 (evening sweep)

**GitHub:** [lynx-community/skills](https://github.com/lynx-community/skills) - 28 stars, Apache-2.0, default branch `release`, last pushed 2026-11-03 (UTC); 18 skill directories, 16 of them under `skills/` plus two inside plugin folders, each holding a `SKILL.md` and most carrying a `references/` or `scripts/` folder

**Category:** Lynx cross-platform UI framework work for agents: device debugging, ReactLynx rules, API docs, trace and bundle analysis

**Quality Tier:** 🟡 Yellow - Snyk warns on `lynx-devtool`, which is 63 percent of the install base, although the licence is a clean Apache-2.0 and the repository is published by the framework's own community organisation

Lynx Agent Skills is the community skill collection for Lynx, the cross-platform UI framework, published under Apache-2.0 by the `lynx-community` organisation. The collection is not a single narrative skill but a set of specialised ones, and the split follows the framework's own shape: one skill for driving a real device through DevTool, one for the ReactLynx component model, one for the API documentation, and several narrower ones for CSS support checks, TypeScript problems, traces, bundle size and UI generation formats.

The install distribution is unusual and worth stating up front. Of the 10,307 indexed installs, 6,443 belong to `lynx-devtool` alone; every other listing sits between 466 and 3. The debugging skill is the collection's centre of gravity because it is the one that turns an agent from a code generator into something that can look at a running app, take a snapshot of the node tree, tap a ref, read a console log and screenshot the result.

## Installation

The README gives one command, with no per-skill variant:

```bash
npx skills add lynx-community/skills
```

There is a detail that catches people out before they read the rest of this guide: the repository's default branch is `release`, while the README states that pull requests must target `main`. Anything you fetch by hand, including a raw file path, has to name `release` explicitly, or you will be reading a branch that is not the one skills.sh indexes.

The repository also declares two Claude Code plugins in `.claude-plugin/marketplace.json`, named `lynx-debug` and `reactlynx` at version 0.1.1, pointing at `./plugins/lynx-debug` and `./plugins/reactlynx`. Those folders hold copies of two of the same skills, so a plugin-based install and a skills-based install can land the same content under two paths.

`lynx-devtool` has a runtime dependency the others do not. It drives the `agent-lynx` CLI, which must be on `PATH`, and the skill tells the agent to fall back to `npx --yes agent-lynx <command>` when `command -v agent-lynx` fails. The CLI connects to Lynx apps on Android, iOS and Desktop through a shared daemon, so a device or simulator has to be attached before any of its debugging commands produce data. A project-local `npm install agent-lynx` is only needed for the programmatic connector, not for CLI use.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lynx-devtool | 6,443 | Driving Lynx DevTool against a live app: clients and sessions, CDP and App commands, DOM and CSS inspection, runtime and console logs, evaluating JavaScript on a device, screenshots, heap snapshots, performance traces, page reload and app open, plus snapshot refs for taps, fills and scrolls. |
| rspeedy-bundle-size | 466 | Shrinking rspeedy and ReactLynx bundles: finding what makes a bundle large, choosing the right size lever, and moving background-only code out of the render path. |
| reactlynx-best-practices | 462 | Reviewing, writing and refactoring ReactLynx code and component libraries for dual-thread rules: background-only work, layout effects, tap events, main-thread annotations and component publishing. |
| lynx-typescript | 434 | Fixing common TypeScript problems in Lynx: environment configuration, type extension, event typing, components and ReactLynx advanced usage. |
| lynx-trace-analysis | 372 | Reading Lynx trace data to diagnose slow startup, white screens, scroll jank, dropped frames and regressions between builds. |
| lynx-trace-record | 363 | Recording a performance trace from a connected client, step by step, for later analysis. |
| lynx-ui | 299 | Using lynx-ui: component selection, public API checks, adapting examples, Luna theme configuration and motion packages. |
| lynx-debug-info-remapping | 298 | Mapping a `function_id:pc_index` from a runtime error back to a source position using a debug info JSON file. |
| habitat-usage | 234 | Managing multi-repo source and asset dependencies through `.habitat/DEPS` and `hab sync`, including common sync failures. |
| vanilla-lynx | 183 | Authoring or reviewing Vanilla Lynx source that uses Element PAPI directly, as a build-free `.lynxml` artifact or an rspeedy project. |
| lynx-check-css-support | 177 | Checking whether a CSS property or value is supported in Lynx, by rendering backend and framework version, from the bundled compat data. |
| lynx-api-docs | 158 | Authoritative answers on pages, templates, components, CSS, layouts, elements, web migration and rendering bugs, with a rule to search the installed docs before acting. |
| lynx-a2ui | 151 | Converting a natural-language UI request into A2UI v0.9 JSON protocol messages for an A2UI renderer. |
| lynx-openui | 140 | Generating OpenUI Lang v0.5 programs for the Lynx OpenUI renderer, including state, tool flows and streaming-friendly output. |
| debug-info-remapping | 68 | An alias listing carrying the same remap description as `lynx-debug-info-remapping`. |
| lynx-fiber-element | 25 | A listing with the same remap description and no corresponding directory in the current tree. |
| fiber-element | 22 | A second listing with the same remap description and no matching directory. |
| trace-analysis | 6 | A third listing with the same remap description and no matching directory. |
| lynx-recorder | 3 | Recording Lynx page interactions into a TestBench replay file with agent-lynx, including start, stop and troubleshooting capture. |
| lynx-recorder-fixture | 3 | Inspecting, decoding, editing and re-encoding existing Lynx Recorder and TestBench fixtures. |

All 20 indexed listings clear the threshold and appear in the table above.

The depth is concentrated in three skills. `lynx-devtool` runs 679 lines and documents a daemon-backed CLI surface: `snapshot` produces a node tree of the current screen, `tap @e3`, `fill @e1 "Alice"`, `clear`, `scroll @e2 --direction down`, `get text`, `get style`, `wait --text Ready` and `screenshot --annotate -o page.jpeg` all operate on refs that live in daemon memory between invocations, and `cdp -m <method>` and `app -m <method>` expose raw protocol calls when the convenience commands are not enough. `rspeedy-bundle-size` runs 200 lines around a three-layer model with explicit levers, a read-only default stance and a rule that every optimisation gets a log entry. `lynx-trace-analysis` runs 252 lines with a process section, output requirements and a decision strategy section for startup and smoothness investigations.

## Why This Matters for Hermes Agents

Most agent failures on a cross-platform framework are not syntax failures, they are assumptions carried over from the web. Lynx has its own dual-thread model, its own element API, its own CSS support matrix per rendering backend, and its own build tool in rspeedy. An agent working from React Native or web intuition will write code that type-checks and behaves incorrectly on device, and no amount of unit testing catches it.

The `lynx-devtool` skill is the answer to that, because it gives the agent eyes. A snapshot returns the actual node tree of the running page; `screenshot --annotate` draws numbered labels into one JPEG where label `[N]` maps to ref `@eN`, so the agent can inspect the image and immediately act on the matching ref. That loop, look then act, is what turns a code generator into a debugger, and it is also why this single skill accounts for most of the collection's installs.

The second useful property is that these skills refuse to guess. `lynx-api-docs` states that it requires searching the installed API docs before acting and has a section on why web knowledge fails. `lynx-check-css-support` queries the bundled compat data rather than asserting that a property works, and can tell you whether the bundled dataset is stale. `rspeedy-bundle-size` opens with a rule to verify against source instead of guessing. For a builder, that means the answer to "does this work on Lynx" comes from data shipped with the repo instead of from the model's memory of a framework it may never have seen.

The third is granularity. A trace tells you FCP, FMP and TTI, a remap file tells you which source line a runtime error came from, and a bundle analysis tells you which import is inflating `main-thread.js`. Each of those is a separate skill with its own small procedure, which keeps an agent from loading one enormous document and hoping the relevant paragraph survives.

## Usage

| You say | What happens |
|---|---|
| "The app is running on my Android emulator, tap the login button" | Uses `agent-lynx snapshot` to get refs, then `agent-lynx tap @e3 --snapshot`, without passing `--no-daemon`. |
| "Why is first paint slow on this build?" | Records a trace with the trace-record skill, then hands it to trace analysis, which reports FCP, FMP and TTI and looks for white-screen causes. |
| "Our rspeedy bundle is too big, where do I start?" | Applies the three-layer model, triages which lever applies, and proposes moving background-only SDK code out of the render path. |
| "Is this CSS property supported on the iOS backend in this Lynx version?" | Queries the bundled compat data by backend and version, and says whether the dataset itself is current. |
| "Review this ReactLynx component for dual-thread mistakes" | Applies the rule set: background-only work, layout effect usage, tap versus catch events, main-thread annotations, and component publishing shape. |
| "This crash gives me function_id 42 pc_index 1907, what line is that?" | Runs the debug info remap against the provided JSON and reports the original source position. |
| "Record this flow so we can replay it in TestBench" | Starts a recording with agent-lynx, captures the interactions, and stops it into a replay fixture. |

## Verification

The raw path below returned 200 on branch `release` on 2026-11-02, and so did the reference it links:

```bash
for p in skills/lynx-devtool/SKILL.md skills/lynx-devtool/references/screenshot-annotate.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/lynx-community/skills/release/$p"
done
```

After a clone, confirm the branch and the skill count. Note the explicit `--branch release`, which is the check that matters here:

```bash
git clone --depth 1 --branch release https://github.com/lynx-community/skills.git /tmp/lynx-skills
git -C /tmp/lynx-skills rev-parse --abbrev-ref HEAD
find /tmp/lynx-skills -name SKILL.md -not -path '*/.git/*' | wc -l
head -3 /tmp/lynx-skills/skills/lynx-devtool/SKILL.md
```

The branch should print `release`, the count should print 18, and `head` should show `name: lynx-devtool` with the description the runtime routes on. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/lynx-devtool/references | head -5
command -v agent-lynx || npx --yes agent-lynx skills list
```

The listing should show `cdp`, `app`, `get-console.md` and the screenshot references, and the second command confirms the CLI that the skill drives is reachable.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lynx-devtool | Pass | Pass | Warn |
| rspeedy-bundle-size | Pass | Pass | Pass |
| reactlynx-best-practices | Pass | Pass | Pass |

Two of the three sampled listings are clean on all three auditors, and the third carries a Snyk warn only. The warn sits on the skill that holds the most capability: `lynx-devtool` instructs an agent to attach to a live application over ADB or a device transport and then run commands against it.

That capability is legitimate and documented, but it deserves a scoped decision. The commands that follow a snapshot can tap buttons, type into fields, clear inputs, scroll and reload pages, and `evaluate` runs JavaScript on the device with a choice of thread. Point that at a production build with a real account signed in and an agent can do real damage in a way an ordinary code-writing skill cannot. Keep the DevTool skill for development builds on emulators or test devices, and read the skill's own warning about not passing `--no-daemon` to the snapshot commands before you debug a session that behaves unexpectedly.

The rest of the collection is Markdown plus a few small scripts. `lynx-check-css-support` ships a `scripts/` folder, `reactlynx-best-practices` ships `rules/` and `scripts/`, and `lynx-trace-analysis` ships `scripts/` with its own LICENSE. Read those scripts before running them, since they are the only executable content in the repository.

## Limitations

- Snapshot data, verified 2026-11-02: 10,307 combined installs across 20 indexed listings; 28 GitHub stars; Apache-2.0; last pushed 2026-11-03. Counts drift over time.
- The default branch is `release`, not `main`, and the README says pull requests must target `main`. Any raw URL, clone or pinned reference must say `release` explicitly or it will resolve against the wrong tree.
- The README's skill links point at `./packages/skills/<name>` and its MCP section at `packages/mcp-servers/`, but this revision has no `packages/` directory: the skills sit at `skills/` and the plugins at `plugins/`. Treat those links as stale documentation rather than paths that exist.
- Four of the 20 listings, `debug-info-remapping`, `lynx-fiber-element`, `fiber-element` and `trace-analysis`, carry the remap description verbatim and have no matching directory under `skills/`. There are 16 unique skill names in the tree against 20 indexed listings.
- Two skills exist twice. `reactlynx-best-practices` and `lynx-debug-info-remapping` appear under `skills/` and again inside `plugins/reactlynx/skills/` and `plugins/lynx-debug/skills/`, and the pairs are byte-identical, so a plugin install can duplicate what a skills install already placed.
- The whole collection sits at 28 stars, and one skill carries 63 percent of the installs. Adoption is real but shallow, so expect thinner issue history than a framework-official suite would have.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Callstack Agent Skills - React Native Skill Suite Setup](/hermes/skills/catalog/callstackincubator-agent-skills-setup)
- [Syncfusion React UI Skills - Component Suite Setup](/hermes/skills/catalog/syncfusion-react-ui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the collection, not just `lynx-devtool`. The debugging skill gets an agent to the running app, but the ReactLynx and API docs skills are what stop it writing web-shaped code once it is there.
- Ask for a snapshot before asking for a change. `agent-lynx snapshot` costs one call and turns "the button does not work" into a concrete ref the agent can tap and a tree it can read.
- Use `screenshot --annotate` when the layout is the problem. Label `[N]` in the image maps to ref `@eN`, so vision and refs point at the same element in one step.
- Keep the devtool skill on emulators and development builds. The commands it teaches change application state, and a production session with real credentials is the wrong target.
- When a new version supports a CSS feature, re-check rather than assume. The check-css-support skill can tell you whether the bundled compat dataset has fallen behind the release you are targeting.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
