---
title: "REA - Reverse Engineer Anything Skill Setup"
description: "REA: 16.8K combined installs. One MCP server that inspects binaries, Electron apps, .NET assemblies and live sites, with evidence."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rea-setup/"
robots: "index,follow"
last_updated: "2026-10-25"
tags: ["hermes skill", "agent skill", "skill setup", "reverse engineering", "mcp", "binaries"]
---

# REA - Setup Guide

**Source:** [morluto/rea](https://www.skills.sh/morluto/rea) via skills.sh - 16.8K combined installs across 6 indexed listings; new to this catalog in the Oct 25, 2026 morning sweep

**GitHub:** [morluto/rea](https://github.com/morluto/rea) - 381,166 stars, MIT, last pushed 2026-10-25, branch main, five skill directories under `.agents/skills/`, with the MCP server and CLI shipped as the `rea-agents` npm package

**Category:** Reverse Engineering / Binary and Application Analysis

**Quality Tier:** 🟡 Beta - a large, actively released analysis platform whose static paths hold no credential and whose runtime paths are the flagged risk, with one Gen Agent Trust Hub warning on unpinned runtime execution

REA is a single MCP server that gives an agent inspection tools for things it normally cannot read: native binaries, JavaScript and Electron applications, .NET assemblies, Android APKs, firmware images, model artifacts, packet captures and live websites. Analysis runs locally. Every finding comes back with the evidence behind it and the limitations of that evidence, which is the design decision that separates this from a wrapper around a decompiler.

The mechanism is contract-shaped. The agent asks a question about an artefact, REA answers with code, references and an explicit list of what it could not determine, and the agent uses that to explain behaviour or write an implementation. Nothing is asserted without a citation to the artefact, which is why the skill's instructions spend as much space on evidence discipline as on tool selection.

The coverage is unusually wide for one server, and it is organised by requirement rather than by marketing. Static inspection of Go binaries, GPU code objects, model headers, IL2CPP metadata, Godot archives, Rust crate metadata, PE certificates and Erlang BEAM files needs no external tool at all. Deep native analysis reuses an existing Hopper, Ghidra or IDA install. JavaScript, browser and capture work needs Node and, on Linux, a Chrome-family browser and a `ps`.

## Installation

The setup command registers the MCP server with your agent and installs the matching workflow instructions, with backups of any configuration it changes:

```bash
npx rea-agents setup
```

Choose the agents to configure, review the proposed changes and approve them, then restart the agent. Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and other hosts, and the README documents manual MCP registration for anything outside that list.

For regular CLI use, install the binary globally:

```bash
npm install --global rea-agents
rea --help
```

Update with `rea update`, or refresh an `npx`-based agent setup with `npx rea-agents@latest setup`. Bun global installs require Bun 1.2.17 or later.

MCP input schemas ship in a compact profile by default to keep context small. Setting `REA_MCP_INPUT_SCHEMA_PROFILE=full` in the MCP registration exposes the complete field guidance and nested validation detail, at a context cost.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| reverse-engineer-anything | 10,508 | Reverse engineering native, managed, Electron and JavaScript, packaged, firmware and browser targets, and building AgentEnv bundles of a web application from a live instance or a capture. |
| rea-tool-design | 1,891 | Designing or changing REA investigation tools themselves: CLI and MCP contracts, provider capabilities and the semantics of an evidence record. |
| rea-changelog-update | 1,802 | Preparing release changelogs and GitHub release notes from pinned Git history, with verified contributor thanks and Release Please synchronisation. |
| rea-ci-tests-audit | 1,519 | Auditing CI and test suites for correctness, fixture drift, false passes and measured performance, rather than debugging a single failing test. |
| rea-analysis-optimization | 1,025 | Optimising providers and shared analysis workflows for agent context, latency, CPU and memory while preserving correctness and evidence. |

The remaining 1 indexed listing sits below the threshold: rea-analysis (10 installs), an early listing with no directory under `.agents/skills/` in the current tree.

The four smaller skills are maintainer tooling. They matter if you contribute to REA or run a fork; they are noise in a normal install, and the setup command is what actually enables the analysis capability.

## Why This Matters for Hermes Agents

An agent asked to explain how a competitor's feature works, or why a vendor's update broke an integration, has two options without a tool like this: guess from training data, or read a marketing page. Both produce plausible prose with no grounding, which is the failure mode that makes agent research unusable in a decision.

REA replaces the guess with an artefact read. The agent can list a Go binary's embedded module versions and replacements, decode a Unity build's IL2CPP metadata to recover type and method names, inventory a Godot archive, inspect an APK's signing chain, or map an Electron app's IPC surface and route inventory from the extracted `app.asar`. Each answer arrives with the offsets, digests or file paths it came from, so a claim can be checked rather than believed.

The second capability is the one that maps most directly onto product work. AgentEnv bundles reconstruct a web application from a live instance or a capture, which means an agent can study how a specific flow behaves and then build a version of it rather than approximating it from screenshots.

The boundary to draw is legal and operational, not technical. Reading software you do not own or are not licensed to analyse is a decision for you and your counsel; the tool makes it possible, it does not make it appropriate. The static paths also need to be deliberately chosen over the runtime ones where a licence or a contract requires it, because REA runs the target when you ask it to capture behaviour.

## Usage

| You say | What happens |
|---|---|
| "How does this app handle search" | The agent selects the JavaScript application workflow, extracts modules, routes and IPC boundaries with evidence, and explains the flow with references to the files it read. |
| "What version of Go and which modules is this binary built from" | Static ELF or PE inspection returns the embedded compiler version, module list, replacements and build settings, with no Go installation needed. |
| "Why did this crash" | Apple crash report, recorded Linux crash or kernel module inspection returns threads, registers, images and documented crash classes rather than a guess. |
| "Build me an AgentEnv of this web app" | The agent reconstructs an environment bundle from a live instance or a capture, with the routes and assets it observed. |
| "Audit this APK's signature" | Signature inspection returns v1 to v3.1 signers, certificate fingerprints, key rotation and digest self-consistency, statically. |
| "What does this firmware image contain" | Region and extraction results with the native analysis handoff, using binwalk or unblob on Linux. |
| "Compare these two releases and tell me what changed" | Version comparison across the artefacts, with the specific evidence behind each difference. |

## Verification

Confirm the layout on main before installing; every skill lives under `.agents/skills/`:

```bash
for s in reverse-engineer-anything rea-tool-design rea-analysis-optimization; do
  curl -sL -o /dev/null -w "%{http_code} .agents/skills/$s/SKILL.md\n" \
    "https://raw.githubusercontent.com/morluto/rea/main/.agents/skills/$s/SKILL.md"
done
```

Read the main skill before you let an agent loose on a target, because it decides which analysis path runs:

- https://raw.githubusercontent.com/morluto/rea/main/.agents/skills/reverse-engineer-anything/SKILL.md

After install, the MCP server appears in your agent's configuration as REA and the skills appear in the skills directory. `rea --help` confirms the CLI half is on the path. Because setup edits `mcp.json` and can replace the bundled skill, run it on a clean tree and read the diff it proposes.

## Security

skills.sh verdicts for sampled skills (verified October 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| reverse-engineer-anything | Warn | Pass | Pass |
| rea-tool-design | Pass | Pass | Pass |
| rea-changelog-update | Pass | Pass | Warn |
| rea-ci-tests-audit | Pass | Pass | Pass |
| rea-analysis-optimization | Pass | Pass | Pass |
| rea-analysis | Pass | Warn | Pass |

The main listing carries a MEDIUM warning on four counts. `REMOTE_CODE_EXECUTION` because diagnostics and setup run `npx -y rea-agents@latest`, an unpinned fetch from the registry. `DYNAMIC_EXECUTION` because setup is documented as able to replace the bundled skill and rewrite client MCP configuration. `INDIRECT_PROMPT_INJECTION` because the analysis surface deliberately ingests untrusted artefacts, and strings, comments, metadata and page content inside a target are all attacker-controlled if the target is hostile.

That last point is the one to act on. A skill that reads arbitrary binaries and websites will eventually read text written to manipulate the model reading it. Treat every REA output as data, not instruction, and keep an agent that holds credentials away from targets you do not trust.

`rea-analysis` records a Socket anomaly on unpinned `npx` execution and on capability scope: not credential theft, but a large capability expansion with an install-trust dependency. `rea-changelog-update` carries Snyk `W011` because it reads GitHub pull request text and commit messages authored by others, which is structural to what it does.

The static inspection paths are the safe subset. Model headers, IL2CPP metadata, Godot archives, PE certificates, ELF notes and .NET metadata are parsed without executing anything; runtime capture and process interaction are the paths that run the target with your permissions.

## Limitations

- Snapshot data, verified October 25, 2026: 16,755 combined installs across 6 indexed listings; 381,166 GitHub stars; MIT; last pushed 2026-10-25. Counts drift over time.
- The board row for this source read 519 installs. A publisher query returned 16,755 across six listings, a 32x difference; the largest listing alone is 10,508.
- Deep native analysis is not self-contained. Hopper, Ghidra or IDA must already be installed and configured; REA does not install or update a provider.
- Node.js 22.x (22.23.4 or newer), 24.x (24.22.1 or newer) or 26.12.1+ is required, and Linux analysis of Ghidra, JADX and firmware targets needs a procps-compatible `ps` for process ownership checks.
- Runtime capture runs or interacts with the target using your user permissions. Whether that is acceptable is a licensing and contractual question, not a technical one.
- The four maintainer skills carry most of the listing count and almost none of the user value. Do not read the six listings as six capabilities.
- Analysis quality depends on the provider for native work. Two decompilers given the same binary will produce different pseudocode and different confidence.

## Related

- [Chrome DevTools MCP Skills - Browser Debugging & Automation Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup)
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Open Browser Use Skills - Browser Automation Setup](/hermes/skills/catalog/open-browser-use-setup)
- [Setup Guide: cantinaxyz/clawdstrike - Agent Red-Team Security Testing (486 Installs)](/hermes/skills/catalog/clawdstrike-setup)

## Pro Tips

- Start with the static paths. Model headers, PE certificates, .NET metadata and Electron source maps need no provider and no execution, and they answer most "how is this built" questions.
- Keep REA in a profile that does not hold production credentials. The injection surface is real and the agent reads attacker-controlled text by design.
- Pin the npm version in your MCP registration instead of relying on `@latest`, so a registry compromise or a bad release does not reach the agent automatically.
- For client work, capture the artefact first and analyse the copy. It keeps the evidence stable and keeps the runtime path off a production system.
- Read the `disclaimer` and the per-target docs before the first real investigation. The tool documents its own limitations more honestly than most.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
