---
title: "Agent Desktop - Computer Use for Agents Setup"
description: "vercel-labs/agent-desktop via skills.sh: 5.1K combined installs across 6 listings. Computer use for agents through the OS accessibility tree."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-desktop-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "computer use", "desktop automation", "accessibility"]
---

# Agent Desktop - Setup Guide

**Source:** [vercel-labs/agent-desktop](https://www.skills.sh/vercel-labs/agent-desktop) via skills.sh - 5.1K combined installs across 6 indexed listings; first documented November 3, 2026 (evening sweep, trending board)
**GitHub:** 13,273 stars, Apache-2.0, last pushed 2026-11-03, 8 SKILL.md directories
**Category:** Computer use for agents: see and drive macOS, Windows and Linux desktop apps through the OS accessibility tree
**Quality Tier:** 🟡 Yellow - jev-desktop carries a Socket Warn while the five agent-desktop listings pass all three auditors

agent-desktop is a computer use CLI and C library from Vercel Labs. It gives an agent a way to read a desktop application instead of guessing at pixels: it walks the operating system accessibility tree, returns that tree as JSON, and tags every element the agent can act on with a ref.

The loop stays in your agent. agent-desktop carries no model inside: the agent takes a snapshot, clicks or types on a ref, snapshots again to check the result, and repeats. Each command prints a single JSON envelope, so a tool call and its result stay inspectable.

## Installation

Install the package globally with npm, then confirm what the current platform supports:

```bash
npm install -g agent-desktop
agent-desktop status
```

On macOS, the permissions command walks through the Accessibility grant that the accessibility tree requires:

```bash
agent-desktop permissions --guide
```

Bun, Yarn and pnpm install the same package. It ships native binaries and platform helpers for x64 and ARM64. Homebrew works on macOS and Linux with `brew install agent-desktop`. For direct execution without a JavaScript launcher, download the matching native archive from GitHub Releases and keep its helper beside the executable. There is no official Scoop package yet, and the repository no longer maintains a custom Homebrew tap or Scoop bucket.

## What It Provides

The repository publishes one core skill plus a per platform split, an FFI binding, and one third party entry that indexes under the same source. Installs are the skills.sh figures indexed on November 3, 2026.

| Skill | Installs | Use For |
|---|---|---|
| agent-desktop | 3,909 | Core CLI and library: snapshot an app, act on a ref, re-read the UI |
| agent-desktop-windows | 453 | Windows desktop surfaces through the same accessibility tree contract |
| agent-desktop-macos | 328 | macOS apps, including the Accessibility permission grant path |
| agent-desktop-linux | 151 | Linux desktop apps on the accessibility tree |
| agent-desktop-ffi | 127 | Direct C library calls when a JavaScript launcher is not wanted |
| jev-desktop | 109 | Third party desktop entry indexed under the same source |

All 6 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Computer use usually arrives as a screenshot loop: capture an image, ask a model where to click, click, capture again. Every step spends vision tokens, and every step inherits a coordinate guess that drifts when a window moves or a font renders differently. agent-desktop replaces the guess with a structured tree, so a click targets a named element rather than a pixel offset.

That shape fits tool calling well. A snapshot is one JSON envelope with a ref per actionable element, which means the agent can decide on a ref, act on it, and read the result back in two more calls. Refs carry their snapshot id, so a stale click is reported as an error instead of silently landing somewhere else.

Actions are headless by default: no pointer movement and no focus change, which keeps an automation run from stealing the foreground on a shared machine. Pass `--headed` when physical input is what you actually want to test. Because the same contract covers macOS, Windows and Linux, one procedure can be written once and run against the matching platform skill.

## Usage

| You say | What happens |
|---|---|
| "Open Finder and list what is in Downloads" | Snapshot the app with interactive elements only, returning a ref for every actionable element |
| "Click the Documents folder" | Click the ref from that snapshot, then snapshot again to confirm the view changed |
| "Now type the file name into the search field" | Type into the focused ref and re-read the tree to verify the result |
| "That click failed, what happened" | Reports STALE_REF or AMBIGUOUS_TARGET when the UI moved, then takes a fresh snapshot |
| "Do it with the real mouse and keyboard" | Repeats the same steps with `--headed` so the input is physical |
| "Is this app actually accessible to you" | Runs `agent-desktop status` to show platform, permissions and supported surfaces |
| "Run the same flow on Windows" | Uses the agent-desktop-windows skill against the same snapshot and ref contract |

## Verification

Confirm the CLI is installed and can see the platform before trusting any automation run:

```bash
agent-desktop status
```

Then read the core skill file straight from the repository to confirm the published instructions match what you installed:

```bash
curl -fsSL https://raw.githubusercontent.com/vercel-labs/agent-desktop/main/skills/agent-desktop/SKILL.md
```

That path resolves on branch `main`: https://raw.githubusercontent.com/vercel-labs/agent-desktop/main/skills/agent-desktop/SKILL.md

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| agent-desktop | Pass | Pass | Pass |
| agent-desktop-windows | Pass | Pass | Pass |
| agent-desktop-macos | Pass | Pass | Pass |
| agent-desktop-linux | Pass | Pass | Pass |
| agent-desktop-ffi | Pass | Pass | Pass |
| jev-desktop | Pass | Warn | Pass |

Snapshots, clipboard reads, screenshots, command output and debug artifacts can contain private desktop content. Keep them out of public logs and uploads.

## Limitations

- Snapshot data, verified November 3, 2026: 5,077 combined installs across 6 indexed listings; 13,273 GitHub stars; Apache-2.0; last pushed 2026-11-03. Counts drift over time.
- The repository tree holds 8 SKILL.md directories against 6 indexed listings: .agents/skills/architecture-diagram and .agents/skills/technical-writer have no indexed listing.
- Refs are snapshot scoped. A bare ref fails with INVALID_ARGS, and an action on a changed UI returns STALE_REF or AMBIGUOUS_TARGET.
- The tool has no model inside. Planning, retries and loop control are the calling agent's job.
- Actions are headless by default, so physical pointer and focus behavior only appears with `--headed`.
- Accessibility coverage depends on the target app. Apps that expose little through the OS accessibility tree expose little to the agent.

## Related

- [Browser Use Automation](/hermes/skills/catalog/browser-use-automation-setup)
- [Open Computer Use](/hermes/skills/catalog/open-computer-use-setup)
- [Playwright Skill](/hermes/skills/catalog/playwright-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `agent-desktop status` on every new machine, since a missing Accessibility grant looks like a broken snapshot.
- Use the platform specific skill (windows, macos, linux) when you know the target host, and the core skill when one procedure has to travel.
- Treat STALE_REF as normal traffic rather than a failure: take a new snapshot and retry against its refs.
- Keep snapshots small with the interactive only flag, then widen only when an element you need is missing from the tree.
- Reach for agent-desktop-ffi only after the CLI path works, since it loads the same native helpers without the launcher.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
