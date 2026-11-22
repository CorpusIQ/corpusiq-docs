---
title: "MobileBuildMCP - iOS and macOS Build Suite Setup"
description: "getsentry/mobilebuildmcp: MCP server and CLI for building, testing and running iOS and macOS projects from an agent - 2.8K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mobilebuildmcp-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "ios", "macos", "mcp"]
---

# MobileBuildMCP - iOS and macOS Build Suite Setup

**Source:** [getsentry/mobilebuildmcp](https://www.skills.sh/getsentry/mobilebuildmcp) via skills.sh - 2.8K combined installs across 24 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [getsentry/mobilebuildmcp](https://github.com/getsentry/mobilebuildmcp) - 6,596 stars, MIT, main branch, last pushed Nov 19, 2026; two official skills under skills/mobilebuildmcp/SKILL.md and skills/mobilebuildmcp-cli/SKILL.md, nine code-review skills and two Warden skills under .agents/skills/, with the TypeScript MCP server under src/ and tools declared in manifests/tools/.
**Category:** iOS and macOS Build Automation
**Quality Tier:** 🟡 Yellow - 0 Fail and 3 Warn cells in the 20-skill sample: Snyk Warn on warden and warden-sweep, and a Socket Warn on mobilebuildmcp-runtime-boundary-review; every other cell Pass.

MobileBuildMCP is a Model Context Protocol (MCP) server and CLI that gives an agent tools for working on iOS and macOS projects, from building, testing and running apps to simulator and device control, debugging, coverage and UI automation. It ships as a single package with two modes, a CLI for direct terminal use and an MCP server for AI coding agents, installable through Homebrew or npm. Two optional agent skills, one for the MCP server and one for the CLI, prime an agent on how to drive the tools, and the repository also carries a Warden pre-commit review tool and a set of code-review skills used by the project's own maintainers.

The skills.sh index still tells the project's older story. The top two listings carry the former xcodebuildmcp name (xcodebuildmcp at 1,268 installs and xcodebuildmcp-cli at 720), while the renamed mobilebuildmcp and mobilebuildmcp-cli listings sit further down at 156 and 52 installs. The Homebrew tap and the docs repository both still reference xcodebuildmcp, so the old name persists in tooling even though the package is now MobileBuildMCP. Nine code-review skills also appear twice in the index, once under the xcodebuildmcp- prefix at 41 to 49 installs and again under the mobilebuildmcp- prefix at 6 installs each.

## Installation

MobileBuildMCP ships as one package with two modes: a CLI for direct terminal use and an MCP server for AI coding agents. Either install method gives both.

```bash
brew tap getsentry/xcodebuildmcp
brew install mobilebuildmcp
```

Or through npm on Node.js 18+:

```bash
npm install -g mobilebuildmcp@latest
```

Verify the install:

```bash
mobilebuildmcp --help
```

Most MCP clients can also run the server on demand without a global install:

```bash
npx -y mobilebuildmcp@latest mcp
```

To install the optional agent skills, use the init command:

```bash
mobilebuildmcp init
```

Or without a global install:

```bash
npx -y mobilebuildmcp@latest init
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| xcodebuildmcp | 1,268 | the MCP server listing under the project's older name |
| xcodebuildmcp-cli | 720 | the CLI listing under the project's older name |
| mobilebuildmcp | 156 | official MCP skill: primes the agent on the server's build, test, run, debug, log and UI automation tools |
| mobilebuildmcp-cli | 52 | official CLI skill: primes the agent on navigating the unified CLI |
| warden | 52 | run Warden to analyze code changes before committing |
| warden-sweep | 52 | full-repository sweep that scans every file, verifies findings and drafts pull requests |
| xcodebuildmcp-test-boundary-review | 49 | reviews tests for correct unit, snapshot, schema, smoke and external process boundaries |
| xcodebuildmcp-tool-contract-review | 48 | reviews tool contract changes across implementation, manifests, workflow membership and output schema |
| xcodebuildmcp-structured-output-review | 48 | reviews structured output schema changes, schema versioning and JSON fixture compatibility |
| xcodebuildmcp-snapshot-fixture-review | 48 | reviews snapshot fixture changes for MCP, CLI and JSON output contracts |
| xcodebuildmcp-docs-release-review | 48 | code-review skill for documentation and release changes |
| xcodebuildmcp-runtime-boundary-review | 47 | reviews runtime boundary changes across MCP, CLI, daemon-routed tools and the Xcode IDE bridge |
| xcodebuildmcp-rendering-streaming-review | 47 | code-review skill for rendering and streaming changes |
| xcodebuildmcp-packaging-resource-review | 47 | code-review skill for packaging and resource changes |
| xcodebuildmcp-docs-command-review | 41 | code-review skill for documentation and command changes |

The remaining 9 indexed listings range from 6 to 6 installs.

## Why This Matters for Hermes Agents

An agent that can build, test and run an iOS or macOS app end to end stops being a code assistant and becomes the build pipeline itself, and MobileBuildMCP is a complete MCP surface for that job on Apple platforms. The tools are manifest-driven: each capability is declared in a YAML manifest under manifests/tools/ with a versioned structured-output schema, so the server exposes a typed contract an agent can call and inspect instead of shelling out to xcodebuild by hand. The same package runs two ways, as a CLI for humans and as an MCP server for agents, keeping an operator's interactive workflow and the agent's automated one on identical behavior. Device targets are the sharp edge: installing and launching on a physical device require code signing configured in Xcode, so an agent granted device access should run behind a review gate. The security sample is clean by community standards, with Pass verdicts nearly everywhere and only three Warns, all on the project's own Warden and code-review skills rather than the installable build tools.

## Usage

| You say | What happens |
|---|---|
| Build my iOS app for the simulator | Runs the simulator build with the scheme and project path and returns build output |
| Run the macOS app | Builds and launches the macOS target through the build and run tool |
| Scaffold a new iOS project | Generates a starter Xcode project with the scaffold tool |
| Take a screenshot of the simulator | Captures the current simulator screen with the screenshot tool |
| Check my Xcode environment | Runs the doctor tool to report Xcode, simulator and build settings health |
| List every tool the CLI exposes | Prints the available tool catalog from the unified CLI |

## Verification

Review the MCP skill's instructions before wiring it into an agent:

```bash
curl -sL https://raw.githubusercontent.com/getsentry/mobilebuildmcp/main/skills/mobilebuildmcp/SKILL.md | head -40
```

Review the CLI skill the same way:

```bash
curl -sL https://raw.githubusercontent.com/getsentry/mobilebuildmcp/main/skills/mobilebuildmcp-cli/SKILL.md | head -40
```

Inspect a tool manifest to confirm the typed contract before relying on it:

```bash
curl -sL https://raw.githubusercontent.com/getsentry/mobilebuildmcp/main/manifests/tools/build_sim.yaml | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| xcodebuildmcp | Pass | Pass | Pass |
| xcodebuildmcp-cli | Pass | Pass | Pass |
| mobilebuildmcp | Pass | Pass | Pass |
| mobilebuildmcp-cli | Pass | Pass | Pass |
| warden | Pass | Pass | Warn |
| warden-sweep | Pass | Pass | Warn |
| xcodebuildmcp-test-boundary-review | Pass | Pass | Pass |
| xcodebuildmcp-tool-contract-review | Pass | Pass | Pass |
| xcodebuildmcp-structured-output-review | Pass | Pass | Pass |
| xcodebuildmcp-snapshot-fixture-review | Pass | Pass | Pass |
| xcodebuildmcp-docs-release-review | Pass | Pass | Pass |
| xcodebuildmcp-runtime-boundary-review | Pass | Pass | Pass |
| xcodebuildmcp-rendering-streaming-review | Pass | Pass | Pass |
| xcodebuildmcp-packaging-resource-review | Pass | Pass | Pass |
| xcodebuildmcp-docs-command-review | Pass | Pass | Pass |
| mobilebuildmcp-tool-contract-review | Pass | Pass | Pass |
| mobilebuildmcp-test-boundary-review | Pass | Pass | Pass |
| mobilebuildmcp-structured-output-review | Pass | Pass | Pass |
| mobilebuildmcp-snapshot-fixture-review | Pass | Pass | Pass |
| mobilebuildmcp-runtime-boundary-review | Pass | Warn | Pass |

The sample covers 20 of the 24 indexed listings; the only Warn cells sit on the project's own Warden and review skills.

## Limitations

- Snapshot data, verified Nov 21, 2026: 2,777 combined installs across 24 indexed listings; 6,596 GitHub stars; MIT; last pushed Nov 19, 2026. Counts drift over time.
- The index still carries the project's older name: xcodebuildmcp (1,268) and xcodebuildmcp-cli (720) dominate the install counts, while the current mobilebuildmcp and mobilebuildmcp-cli listings hold 156 and 52 installs. The Homebrew tap and the docs repository still reference xcodebuildmcp.
- Nine code-review skills are listed twice, once under the xcodebuildmcp- prefix at 41 to 49 installs and again under the mobilebuildmcp- prefix at 6 installs each; the mobilebuildmcp- copies carry the 6-install counts in the remaining-listings line above.
- The 20-skill security sample carries no Fail cells and three Warn cells: Snyk Warn on warden and warden-sweep, and a Socket Warn on mobilebuildmcp-runtime-boundary-review.
- The tools require macOS 14.5 or later and Xcode 16 or later, device targets need code signing configured in Xcode, and the package sends internal runtime-error telemetry to Sentry with an opt-out.

## Related

- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [Dimillian Skills - Apple Platform Engineering Suite Setup](/hermes/skills/catalog/dimillian-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pick the install method that matches your setup: Homebrew needs no Node.js, while npm install -g requires Node.js 18 or later.
- Use npx -y mobilebuildmcp@latest mcp when you only need the MCP server and do not want a global install.
- Start with simulator targets before device targets; device install and launch need code signing configured in Xcode.
- Run mobilebuildmcp init (or npx -y mobilebuildmcp@latest init) to drop the optional agent skills into your agent's skill directory.
- Treat the xcodebuildmcp-* and mobilebuildmcp-* review skills as maintainer tooling, not end-user installs; the current package is MobileBuildMCP.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
