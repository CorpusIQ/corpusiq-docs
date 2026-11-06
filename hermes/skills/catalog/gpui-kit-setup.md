---
title: "GPUI Kit - Rust Desktop UI Components for Agents"
description: "longbridge/gpui-kit on skills.sh: 6.3K combined installs across 19 listings; GPUI component patterns and design guides for Rust desktop apps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gpui-kit-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "rust", "desktop ui", "gpui"]
---

# GPUI Kit - Setup Guide

**Source:** [longbridge/gpui-kit](https://www.skills.sh/longbridge/gpui-kit) via skills.sh - 6.3K combined installs across 19 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 19,462 stars, no licence detected by the index (the tree splits terms across LICENSE-APACHE for code and LICENSE-DOCS.md for prose rather than shipping a single LICENSE file), last pushed 2026-11-06, two SKILL.md directories under skills/
**Category:** Rust desktop UI for agents: GPUI component patterns and design guides for cross-platform applications
**Quality Tier:** 🟡 Review - no licence detected (no single LICENSE file; terms split across LICENSE-APACHE and LICENSE-DOCS.md) and the gpui-kit skill carries a Snyk Warn.

GPUI Kit is a Rust desktop application framework from Longbridge, built on GPUI, the UI framework behind Zed. It ships 75 or more documented components and primitives, WebAssembly support, AccessKit accessibility, headless UI integration testing and an optional JavaScript extension runtime, and it is used to build Longbridge Pro. One crate is the dependency; `gpui-base` holds unstyled behaviour and state, `gpui-component` holds the styled UI system, and `gpui-shell` adds the scripting host.

The two skills in the repository are a documentation layer for that framework rather than code generators. `gpui-kit` covers setup, the component catalogue, GPUI mechanics (elements, entities, async, focus, actions, tests) and the normative Coding Guides. `gpui-kit-design-guides` holds the Design Guides: layout, spacing, hierarchy, interaction states, overlays and interface copy.

## Installation

The README installs both skills with the Agent Skills CLI:

```bash
npx skills add longbridge/gpui-kit
```

That is the agent side. The application still depends on the crate, which is the same version the skills document:

```toml
[dependencies]
gpui-kit = "0.7"
```

Enable the optional fast core by naming the feature:

```toml
[dependencies]
gpui-kit = { version = "0.7", features = ["gpui-fast"] }
```

The README's own entry example shows the shape a generated app takes: `gpui_kit::application().run(...)`, `gpui_kit::init(cx)` before any component use, then `gpui_kit::open_window(WindowOptions::default(), cx, ...)` mounting a Base `Root`. The default `assets` feature bundles the Lucide icon set and is passed in with `gpui_kit::application().with_assets(gpui_kit::assets::Assets)`.

The repository also builds a component gallery, so you can read the components running rather than only described:

```bash
cargo run
cargo run -p example-dock
cargo run -p example-editor
```

## What It Provides

Two listings clear the 500-install threshold, and they are the two halves of the same contract: how to build it, and what it should look like when built.

| Skill | Installs | Use For |
|---|---|---|
| gpui-kit | 1,168 | Setup, the component catalogue, GPUI mechanics (elements, entities, async, focus, actions, tests) and the normative Coding Guides |
| gpui-kit-design-guides | 1,113 | The normative Design Guides: layout, spacing, hierarchy, interaction states, overlays, motion and interface copy |

The remaining 17 indexed listings range from 139 to 334 installs, and they are named for GPUI subsystems rather than for directories in the repository: gpui (334), gpui-layout-and-style (319), gpui-async (298), gpui-component (295), gpui-context (286), gpui-event (265), gpui-entity (247), gpui-action (246), gpui-style-guide (224), gpui-element (224), gpui-global (222), gpui-focus-handle (220), gpui-test (216), new-component (191), generate-component-documentation (167), github-pull-request-description (149), generate-component-story (139). None of them has a matching directory in the current `skills/` tree; their material lives inside the two shipped skills, whose `references/gpui/` directory carries one file per subsystem.

## Why This Matters for Hermes Agents

Rust desktop UI is a place where a confident agent produces code that compiles and looks wrong. GPUI has its own ownership model, its own entity and element split, and a component library with opinions about state ownership and callbacks. An agent working from general Rust knowledge will invent an API that almost exists, and the compiler will only catch some of it.

The design guides are the more unusual half. They are framed as requirements, not inspiration, and the skill instructs the agent to read the guide file itself rather than answer from a summary. That matters because the failure mode in UI work is not a missing component, it is a plausible screen that ignores spacing rules, hierarchy, interaction states and interface copy. A guide an agent must open before touching a visible surface is a direct check on that.

The reference layout is built for progressive disclosure. `skills/gpui-kit/references/` holds a conventions file, a recipes file, the coding guides, and a `gpui/` directory with focused files per subsystem: entity, element, action, async, focus-handle, test. A Hermes agent can pull the four files a change needs instead of loading a framework manual into the window.

There is also a tested application recipe, which is the difference between documentation and evidence. `examples/ai_recipes` is a consumer crate that imports only `gpui-kit`, the way an application does, and its interaction test types into an input, checks the owner received changes, forces an unrelated redraw and types again. That test exists because subscription and state-lifetime bugs are exactly what generated UI code gets wrong.

Finally, the suite is honest about what it cannot prove. The repository's own acceptance standards say the checks make failures reproducible and do not establish a model success rate, and that visual layout and OS accessibility still need native review. An agent that repeats that caveat is more useful than one that claims a green test means a good screen.

## Usage

| You say | What happens |
|---|---|
| "Set up a new gpui-kit app" | gpui-kit walks the crate dependency, `gpui_kit::init` order, window creation and asset wiring |
| "Which component should this be?" | The design guides pick the component family first, then the skill checks the specific component supports the capability |
| "Build this settings screen" | Design guides for layout, spacing and hierarchy run before any code, then the component catalogue supplies the controls |
| "Review this UI for design quality" | gpui-kit-design-guides reviews against the normative rules rather than taste |
| "Add a virtualised data table" | gpui-kit covers the data table component: virtual scrolling, fixed and resizable columns, sorting, cell selection |
| "Write an integration test for this panel" | gpui-kit covers headless test windows, pointer and keyboard input, and assertions on state, focus, layout and accessibility |
| "Document this component" | The index lists component documentation and story generation skills, though neither has a directory in the current tree |

## Verification

Confirm the skill index before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/longbridge/gpui-kit/main/skills/gpui-kit/SKILL.md | head -5
```

It should open with `name: gpui-kit` and a description naming the crate, the `gpui_kit::component`, `gpui_kit::base` and `gpui_kit::assets` layers, and the Coding Guides. Then confirm both skills landed with their reference trees:

```bash
ls ~/.claude/skills/gpui-kit ~/.claude/skills/gpui-kit-design-guides
ls ~/.claude/skills/gpui-kit/references/gpui | wc -l
```

The first listing should show SKILL.md and a `references/` directory; the second should print a count in the low twenties, one file per GPUI subsystem plus the best-practice and API variants.

If you are working inside the framework repository rather than consuming it, the example crate is the reference implementation, and its checks are the ones the project uses on submitted changes:

```bash
cargo run -p gpui-kit-recipes
cargo test -p gpui-kit-recipes
script/check-ai docs
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gpui-kit | Pass | Pass | Warn |
| gpui-async | Pass | Pass | Pass |
| gpui-action | Pass | Pass | Pass |
| gpui-test | Pass | Pass | Pass |
| generate-component-story | Pass | Pass | Pass |

The gpui-kit Warn is the one to look at, since it is the skill most projects install first. Read its `references/` files before letting an agent act on them; they are markdown, so the install surface itself is small, but instructions that tell an agent to follow a guide are still instructions an agent will follow.

The framework side is a different question from the skill side. Applications built with `gpui-kit` execute native code, ship a JavaScript extension runtime through `gpui-shell` with every capability granted explicitly, and the repository's own guidance is that shell `check` validates eager materialisation but does not prove deferred rendering, layout, paint or later interactions. A green skill install says nothing about a safe application.

The licence is also unresolved at the metadata level: no LICENSE file, terms split across two files, Apache-2.0 for software source and code examples plus CC BY 4.0 for documentation prose and original illustrations. Read both before redistributing anything from the repository.

## Limitations

- Snapshot data, verified 2026-11-05: 6,323 combined installs across 19 indexed listings; 19,462 GitHub stars; no licence detected; last pushed 2026-11-06. Counts drift over time.
- The install index outruns the tree. 19 listings carry install counts but `skills/` holds only `gpui-kit` and `gpui-kit-design-guides`; the other 17 names (gpui-event, gpui-entity, gpui-test and similar) have no directories of their own.
- No single LICENSE file. Software source and documentation code examples are Apache-2.0 via LICENSE-APACHE, documentation prose and original illustrations are also offered under CC BY 4.0 via LICENSE-DOCS.md, and third-party contributions keep their own terms. Tools that expect a root LICENSE will report nothing.
- The skills document version 0.7 of the crate. A project pinned to a different version will get advice for an API it does not have, and the README's feature flags (`gpui-fast`, `inspector`, `decimal`, `tree-sitter`) differ between versions.
- Accessibility and visual correctness still need native review. The repository states that the interaction test is a test-window check and that OS accessibility requires native verification.
- This is a UI framework skill set, not an application generator. It documents components and rules; it does not scaffold a full application, and the JavaScript extension host lives in a separate crate that applications add themselves.

## Related

- [Rust Skills - 265 Rules Across 26 Categories](/hermes/skills/catalog/rust-skills-setup)
- [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup)
- [Agent Desktop - Computer Use for Agents Setup](/hermes/skills/catalog/agent-desktop-setup)

## Pro Tips

- Read the design guides before the component catalogue. The guides decide which component a screen needs; starting from the catalogue produces a screen assembled from whatever was easiest to find.
- Point the agent at one `references/gpui/` file at a time. The directory exists so a task pulls four files, not the whole framework.
- Use the recipe crate as the skeleton. It is a consumer crate that imports only `gpui-kit`, which is the ownership shape an application is supposed to have.
- Ask for the interaction test with the feature. The example test catches dropped subscriptions and state lifetime regressions, which are the two failures generated UI code reproduces most reliably.
- Treat the component gallery as the source of truth for behaviour. `cargo run` runs the story crate with every component, which settles arguments about what a control actually does faster than reading about it.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
