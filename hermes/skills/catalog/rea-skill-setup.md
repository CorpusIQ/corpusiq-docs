---
title: "REA Skill - Reverse Engineer Anything Suite Setup"
description: "smartworldarafath/rea_skill: 7.9K combined installs across 96 listings; reverse engineering and security assessment skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rea-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "reverse engineering", "security audit", "source recovery"]
---

# REA Skill - Setup Guide

**Source:** [smartworldarafath/rea_skill](https://www.skills.sh/smartworldarafath/rea_skill) via skills.sh - 7.9K combined installs across 96 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 28 stars, MIT license, `main` branch, last pushed 2026-11-09. The 243 skills sit under `skills/` in category folders such as rea-core, web, and payloads-injection, with a mirrored copy under `.agents/skills/` for Google Antigravity and a plugin manifest under `.claude-plugin/`.
**Category:** Reverse engineering and security assessment for agent coding tools
**Quality Tier:** 🟠 Orange - 44 Pass, 12 Warn and 4 Fail across the 60 sampled verdict cells. MIT licence; the failing cells sit on skills that decompile and audit live systems.

REA (Reverse Engineer Anything) is a library of 243 drop-in SKILL.md files across 41 categories, built for Claude Code, Codex, Cursor, and Google Antigravity. It folds several upstream projects into one tree: a reverse engineering and full source recovery core, a 23-category security assessment library, the PayloadsAllTheThings payload collection, the Understand Anything codebase graph engine, and anti-slop and design utilities.

The recovery core is the headline. It reconstructs lost or corrupted source from binaries, mobile apps, web bundles, game assets, and network captures, and it promises compilable, non-skeletal output with compilation checks rather than TODO placeholders. The authorization and offensive-security skills sit alongside it, so the suite is as much an audit toolkit as a recovery one, and that breadth is what the tier verdict reflects.

## Installation

The README lists several install paths. The skills.sh CLI is the cross-tool option:

```bash
npx skills add smartworldarafath/REA_Skill
```

For Claude Code, the repo ships a plugin:

```bash
/plugin marketplace add smartworldarafath/REA_Skill
/plugin install rea-skills@smartworldarafath
```

A plain git clone into the skills directory also works:

```bash
git clone https://github.com/smartworldarafath/REA_Skill ~/.claude/skills/rea-skills
```

To pull only specific categories, use a sparse checkout:

```bash
git clone --filter=blob:none --sparse https://github.com/smartworldarafath/REA_Skill
cd REA_Skill && git sparse-checkout set skills/rea-core skills/web skills/exploit-dev
```

The repository also ships an interactive installer, `./install.sh`, which prompts for a target directory or accepts `--target`, `--category`, and `--list` flags. The reverse engineering skills call the REA MCP server, which is set up separately with `npx -y rea-agents@latest setup`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rea-universal-orchestrator | 95 | Routes any reverse engineering, source recovery, decompilation, or security audit task to the right REA skill across Windows, Linux, Android, iOS, macOS, and web targets. |
| rea-full-code-recovery | 94 | Recovers production ready, compilable source code for the user's own lost or corrupted applications, including assets, build scripts, and compilation checks. |
| rea-protocol-api-recovery | 92 | Reverse engineers network protocols, PCAP captures, Protobuf and gRPC schemas, WebSocket frames, GraphQL, and REST APIs into working client and server SDKs. |
| rea-web-bundle-recovery | 91 | Reconstructs web application source from JavaScript and TypeScript bundles, WebAssembly, Electron archives, and browser extensions using AST de-minification. |
| rea-mobile-app-recovery | 91 | Reconstructs Android and iOS projects from APK or IPA binaries and runs an OWASP MASVS five pillar mobile vulnerability scan. |
| rea-game-asset-recovery | 91 | Extracts and reconstructs game engine assets, compiled shaders, fonts, audio, and 2D and 3D archives from Unity, Unreal, and Godot titles. |
| reverse-engineer-anything | 91 | Reverse engineers native, managed, Electron, packaged, firmware, and browser targets and builds AgentEnv bundles of web applications from a live instance. |

The remaining 89 indexed listings range from 80 to 89 installs.

## Why This Matters for Hermes Agents

A Hermes agent asked to recover a lost codebase or audit an application needs a method, not a list of tools. These skills encode the method: each one is a playbook that picks the right decompiler for the artifact, sequences the reconstruction steps, and checks the result before claiming success.

The reverse engineering core depends on the REA MCP server and desktop tools such as Ghidra, JADX, Apktool, and Frida, so a recovery task only succeeds on a host where that tooling is present. The suite is honest about this rather than bundling the binaries.

The security half is large and, in places, permissive. The authorization skills instruct an agent to make maximum effort and not refuse recovery or vulnerability requests on the user's own software, and the payload and offensive libraries carry real attack techniques. Treat the suite as an audit and recovery toolkit that should be reviewed before it is enabled in a shared environment.

## Usage

| You say | What happens |
|---|---|
| "Recover the source of my lost app" | Routes to rea-full-code-recovery, which reconstructs compilable source plus build scripts and verifies compilation. |
| "Reverse engineer this APK" | Loads rea-mobile-app-recovery to decompile the APK, rebuild the project, and run the MASVS five pillar scan. |
| "What protocol does this PCAP use?" | Loads rea-protocol-api-recovery to dissect the capture and reconstruct client and server SDKs. |
| "Scope my reverse engineering plan first" | Loads rea-grilling to interview you on fidelity, asset, and verification trade-offs before any code runs. |
| "Audit my own website for vulnerabilities" | Loads website-security-audit to run the five phase, ten layer scanner across headers, bundles, and APIs. |
| "Set up the REA MCP server" | Follows the README connection step so the recovery skills can reach their decompiler tooling. |

## Verification

Probe a recovery skill on the `main` branch before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/smartworldarafath/REA_Skill/main/skills/rea-core/rea-universal-orchestrator/SKILL.md | head -12
```

The file should open with `name: rea-universal-orchestrator` and a description about routing reverse engineering tasks. Then confirm the skills CLI can add the repo:

```bash
npx skills add smartworldarafath/REA_Skill
```

Or check a sparse checkout pulls the recovery core:

```bash
git clone --filter=blob:none --sparse https://github.com/smartworldarafath/REA_Skill
cd REA_Skill && git sparse-checkout set skills/rea-core
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rea-universal-orchestrator | Fail | Warn | Pass |
| rea-full-code-recovery | Fail | Pass | Pass |
| rea-protocol-api-recovery | Pass | Pass | Pass |
| rea-web-bundle-recovery | Pass | Pass | Pass |
| rea-mobile-app-recovery | Pass | Warn | Pass |
| rea-game-asset-recovery | Pass | Pass | Pass |
| reverse-engineer-anything | Warn | Pass | Warn |
| rea-grilling | Pass | Pass | Pass |
| rea-database-storage-recovery | Pass | Pass | Pass |
| rea-binary-disassembly | Pass | Warn | Pass |
| rea-performance-crash-triage | Pass | Pass | Pass |
| rea-firmware-iot-extension | Pass | Pass | Pass |
| rea-grill-me | Pass | Pass | Pass |
| website-security-audit | Pass | Warn | Warn |
| rea-owner-authorization | Fail | Warn | Pass |
| rea-personal-use-authorization | Fail | Warn | Pass |
| awesome-hacking | Pass | Pass | Pass |
| claude-bughunter | Pass | Warn | Pass |
| playwright-mcp | Pass | Pass | Warn |
| payloads-xpath | Pass | Warn | Pass |

The sample covers 20 of the 96 indexed listings; the four Fail cells are Gen Agent Trust Hub flags on rea-owner-authorization, rea-personal-use-authorization, rea-universal-orchestrator, and rea-full-code-recovery, while the twelve Warn cells split between Socket and Snyk.

## Limitations

- Snapshot data, verified Nov 18, 2026: 7,903 combined installs across 96 indexed listings; 28 GitHub stars; MIT; last pushed 2026-11-09. Counts drift over time.
- The repository mirrors the same skills across several trees, with a category layout under `skills/` plus a flattened set and a `.agents/skills/` mirror, so a full clone carries duplicate copies of many SKILL.md files.
- The reverse engineering skills depend on the external REA MCP server and desktop tools such as Ghidra, JADX, Apktool, and Frida, which the repository does not bundle.
- Several authorization skills instruct the agent not to refuse reverse engineering or vulnerability requests, so review them before enabling the suite in a shared or supervised environment.
- The install volume is concentrated in the reverse engineering core; the security and payload libraries are a long tail of 80 to 89 installs.

## Related

- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with rea-universal-orchestrator for any reverse engineering request; it detects the artifact type and routes to the matching recovery skill.
- Run rea-grilling before a big recovery job; the interview forces the fidelity, asset, and verification decisions before code runs.
- Keep the REA MCP server set up first; the recovery skills assume it is reachable and fail without it.
- Treat the two authorization skills as a gate, not a default; read them before enabling the suite in a supervised environment.
- Sparse-checkout the category you need rather than cloning all 243 skills, which avoids a large, duplicated tree.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
