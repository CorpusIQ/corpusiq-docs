---
title: "Tauri Skills - Desktop and Mobile App Development"
description: "full-stack-skills/tauri-skills - 31.1K combined installs across 56 indexed listings: Tauri v2 desktop and mobile app development skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tauri-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "tauri", "rust", "desktop apps"]
---

# Tauri Skills - Setup Guide

**Source:** [full-stack-skills/tauri-skills](https://www.skills.sh/full-stack-skills/tauri-skills) via skills.sh - 31.1K combined installs across 56 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 30 stars, Apache-2.0 license, `main` branch, last pushed 2026-10-03, `SKILL.md` files under `skills/<name>/` plus four OpenSpec workflow skills under `.agents/skills/`, `.kimi-code/skills/`, and `.zcode/skills/`
**Category:** Tauri v2 desktop and mobile app development - IPC, security, plugins, and cross-platform builds
**Quality Tier:** 🟡 Yellow - twelve sampled skills pass the Gen Agent Trust Hub and both scanners except tauri-config, which carries a Gen Agent Trust Hub Warn.

Tauri Skills is a curated collection of 52 agent skills for Tauri v2 cross-platform desktop and mobile app development, part of the Full Stack Skills ecosystem maintained by PartMe.AI. Each skill is a self-contained `SKILL.md` that an agent loads on demand, and the collection is deliberately tool-agnostic: no consumer-repo tooling is hardcoded, and each skill documents one area of the Tauri lifecycle.

The suite spans setup and prerequisites, project scaffolding, IPC and capabilities, configuration and windows, production builds and distribution, plus one skill per official plugin (dialog, file-system, shell, notification, clipboard, SQL, store, updater, and more). Four OpenSpec workflow skills (openspec-apply-change, openspec-propose, openspec-archive-change, openspec-explore) ride along in the dot-directories rather than under `skills/`, which is why the install index lists 56 listings against 52 Tauri skills.

## Installation

Install the whole repository, or pin a single skill:

```bash
npx skills add full-stack-skills/tauri-skills
npx skills add full-stack-skills/tauri-skills --skill <skill-name>
```

The README's manual route clones and copies the skill folders into Claude Code:

```bash
git clone https://github.com/full-stack-skills/tauri-skills.git
cp -r tauri-skills/skills/* .claude/skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tauri-ipc | 663 | Frontend invoke calls, Rust commands, and type-safe IPC bindings. |
| tauri-security | 661 | Capabilities, scope configuration, and ACL-based permission control. |
| tauri | 657 | Index that routes to specialized sub-skills: Rust backend, frontend integration, and the plugin ecosystem. |
| tauri-build | 630 | Production builds, signing, and distribution artifacts. |
| tauri-app-develop | 628 | The daily development workflow: debugging, resources, sidecar usage, and testing. |
| tauri-config | 615 | tauri.conf.json structure, lifecycle management, and CSP configuration. |
| tauri-window | 611 | Window creation, configuration, lifecycle, and custom titlebar UI. |

The remaining 49 indexed listings range from 261 to 598 installs.

## Why This Matters for Hermes Agents

The most valuable thing here is the security pair. tauri-security covers capabilities, scope configuration and ACL-based permission control, while tauri-framework-security covers the security model, baseline hardening and runtime authority controls. Tauri's permission surface is exactly where an agent guessing the defaults causes real damage, and these two skills encode the model rather than leaving it to memory.

The IPC skill matters for the same reason. Tauri's frontend-to-backend boundary is type-checked on the Rust side but not the JavaScript side, so a wrong invoke name or payload shape fails quietly at runtime. tauri-ipc documents the invoke calls, Rust commands and type-safe bindings so the agent writes the boundary correctly the first time.

The index skill, tauri, is the router: it points at the specialized sub-skills and ships local examples and templates. For an agent holding the whole suite, that routing beats loading all 52 skills at once, and the plugin-per-skill layout means the agent reads only the dialog skill when asked about dialogs.

## Usage

| You say | What happens |
|---|---|
| "Wire up a frontend-to-Rust call" | tauri-ipc documents the invoke calls, Rust commands, and type-safe bindings. |
| "Lock down this app's permissions" | tauri-security applies capabilities, scope configuration, and ACL-based permission control. |
| "Create a new Tauri v2 project" | tauri (with tauri-setup) walks prerequisites and the create-tauri-app scaffold. |
| "Build and sign this app for distribution" | tauri-build covers production builds, signing, and distribution artifacts. |
| "Configure tauri.conf.json and CSP" | tauri-config handles the config structure, lifecycle management, and CSP. |
| "Customize the window and titlebar" | tauri-window covers window creation, configuration, and custom titlebar UI. |
| "Add a system dialog to the app" | tauri-app-dialog documents the dialog plugin with native dialogs and unified API design. |

## Verification

The raw paths below returned 200 on branch main when this guide was written, and they are the fastest way to read a skill before installing it:

```bash
curl -fsSL https://raw.githubusercontent.com/full-stack-skills/tauri-skills/main/skills/tauri-ipc/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/full-stack-skills/tauri-skills/main/skills/tauri-security/SKILL.md | head -20
```

Skills live under `skills/<name>/`; confirm the path exists in the current tree before installing a specific skill. The four OpenSpec workflow skills live under `.agents/skills/`, not `skills/`.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tauri-ipc | Pass | Pass | Pass |
| tauri-security | Pass | Pass | Pass |
| tauri | Pass | Pass | Pass |
| tauri-build | Pass | Pass | Pass |
| tauri-app-develop | Pass | Pass | Pass |
| tauri-config | Warn | Pass | Pass |
| tauri-window | Pass | Pass | Pass |
| tauri-app-file-system | Pass | Pass | Pass |
| tauri-framework-security | Pass | Pass | Pass |
| tauri-setup | Pass | Pass | Pass |
| tauri-app-planning | Pass | Pass | Pass |
| tauri-app-dialog | Pass | Pass | Pass |

tauri-config carries the only non-Pass in the sample, a Gen Agent Trust Hub Warn, and no sampled skill fails any scanner.

## Limitations

- Snapshot data, verified Nov 16, 2026: 31,071 combined installs across 56 indexed listings; 30 GitHub stars; Apache-2.0; last pushed 2026-10-03. Counts drift over time.
- The install index lists 56 listings against 52 Tauri skills: four OpenSpec workflow skills (openspec-apply-change, openspec-propose, openspec-archive-change, openspec-explore) live under `.agents/skills/`, `.kimi-code/skills/`, and `.zcode/skills/` rather than under `skills/`.
- Those four OpenSpec skills sit at 261 to 263 installs, under 600 installs, so they appear in the tail rather than the table.
- The security sample covers 12 of 56 listings; the other 44 remain unaudited by that sample.
- The skills document setup across macOS, Windows, Linux, Android and iOS but do not install the Rust toolchain or platform prerequisites.

## Related

- [Rust Skills](/hermes/skills/catalog/rust-skills-setup)
- [Flutter Agent Plugins](/hermes/skills/catalog/flutter-agent-plugins-setup)
- [Margelo React Native Skills](/hermes/skills/catalog/margelo-react-native-skills-setup)
- [Actionbook Rust Skills](/hermes/skills/catalog/actionbook-rust-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install individual skills with `--skill` rather than the whole 52-skill suite to keep the agent's skill list lean.
- Read tauri (the index) first; it routes to the specialized sub-skills and ships local examples and templates.
- Treat tauri-security (capabilities and ACLs) and tauri-framework-security (baseline hardening) as two layers, and apply both when hardening an app.
- Probe a `SKILL.md` over raw.githubusercontent before copying it in; the suite is plain Markdown folders and nothing executes on install.
- Remember the four OpenSpec skills live outside `skills/`, so a path check based on that directory will miss them.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
