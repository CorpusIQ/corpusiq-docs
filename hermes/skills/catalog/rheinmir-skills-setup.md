---
title: "Rheinmir Overstack - Vietnamese Agent Harness Setup"
description: "rheinmir/setup - 16.8K combined installs: a Vietnamese-language agent harness (overstack) with guardrails, skills and Orca orchestration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rheinmir-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "agent harness", "orchestration", "vietnamese"]
---

# Rheinmir Overstack - Setup Guide

**Source:** [rheinmir/setup](https://www.skills.sh/rheinmir/setup) via skills.sh - 16.8K combined installs across 95 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [rheinmir/setup](https://github.com/rheinmir/setup) - 10 stars, MIT license, orca branch, last pushed Nov 18, 2026; the 106 named skills live in a separate Rheinmir/skills repository (installed globally to ~/.claude/skills), while this repository carries the harness, llmwiki, fdk and mcp tooling plus a set of Vietnamese dym-* skills under .overstack/doyourmagic/.
**Category:** Personal Agent Harness (Vietnamese)
**Quality Tier:** 🟠 Orange - orca-onboard and query each fail the Gen Agent Trust Hub check, and caveman fails Snyk; the other 12 sampled skills pass or carry only Warn cells.

rheinmir/setup publishes overstack, a self-disciplined agent framework layered on top of a project for Claude Code, opencode, Antigravity and Cursor. It combines a project wiki for durable memory (llmwiki/), deterministic zero-token guardrails (harness/), packaged skills, and the Orca multi-agent dispatcher. The README and all installation documentation are written in Vietnamese; the commands below are quoted verbatim and are not translated.

The skills.sh index lists 95 listings at 16.8K combined installs, but the named skills themselves (106 SKILL.md files) live in the separate Rheinmir/skills repository, split from this repository on Oct 14, 2026 so skill fixes do not run the framework CI. This repository holds the harness, the llmwiki knowledge framework, the fdk (Framework Dev Kit), the mcp server, and a set of Vietnamese-language dym-* skills under .overstack/doyourmagic/. The installer can also pull an optional graph engine (orca-graph) from its own repository.

## Installation

The README is Vietnamese and documents a one-line bootstrap (macOS/Linux/WSL):

```bash
curl -fsSL https://raw.githubusercontent.com/Rheinmir/setup/orca/harness/poc-vendor-neutral/bootstrap.sh | bash
```

Windows (PowerShell) downloads the script first, then runs it:

```powershell
iwr -useb https://raw.githubusercontent.com/Rheinmir/setup/orca/harness/poc-vendor-neutral/install.ps1 -OutFile install.ps1
.\install.ps1
```

Skills-only install from the separate skills repository:

```bash
npx -y skills add rheinmir/skills#main --global --all
```

The bootstrap installs the harness, skills and llmwiki by default and prints a three-pillar status table. Flags include --harness-only, --clean and uninstall (PowerShell: -HarnessOnly and -Clean); --no-graph skips the optional orca-graph engine. The README also shows a paste-for-agent variant that wraps the same command in Vietnamese instructions.

## What It Provides

The named skills live in the separate Rheinmir/skills repository, so none of these listings has a SKILL.md counterpart in this repository's tree, and skills.sh publishes no per-skill descriptions for it. Use For cells are name-level.

| Skill | Installs | Use For |
|---|---|---|
| orca-onboard | 271 | onboarding a project through the Orca dispatcher |
| docs-site-macos | 269 | building and maintaining the docs site on macOS |
| verify-before-commit | 266 | verifying changes before committing |
| sync-template | 266 | syncing the project template and harness |
| query | 266 | querying the knowledge base |
| propose | 266 | proposing work items for dispatch |
| orca-workflow | 266 | the Orca propose-to-dispatch workflow |
| md-to-html | 266 | converting Markdown to HTML |
| onboard-codebase | 265 | onboarding a codebase |
| impact-check | 265 | checking the impact of a change |
| extract-site | 265 | extracting a website's content |
| caveman | 265 | the caveman workflow (name-level) |
| safe-change | 264 | making a safe change |
| lint | 264 | linting project files |
| ingest | 264 | ingesting knowledge into the wiki |
| caveman-stats | 264 | caveman workflow stats (name-level) |
| new-project-setup | 263 | setting up a new project |
| caveman-help | 263 | caveman workflow help (name-level) |
| tour-guide | 258 | the onboarding tour |
| orca-sec-scans | 256 | Orca security scans |
| join-project | 254 | joining an existing project |

The remaining 74 indexed listings range from 2 to 248 installs.

## Why This Matters for Hermes Agents

Overstack is a complete opinionated harness that packages the disciplined-agent pattern: a project wiki for durable memory, deterministic zero-token guardrails that block writes outside sanctioned paths, a skills layer, and Orca for multi-agent dispatch. For a builder assembling a Hermes agent, it is a worked reference for governance-by-hook (native hooks plus CI as the floor) rather than by prompt. The harness enforces structure deterministically, blocking raw/ writes and requiring an Origin section in wiki entries, which is the pattern to study if you want guardrails a prompt cannot override. The skills layer is separable: the README documents installing just the 106 skills from Rheinmir/skills with a single npx command. Adoption costs are real, since the README and docs are Vietnamese, the installer registers a remote MCP server by default, and three popular skills carry Fail cells in the sampled verdicts. Read it for the architecture rather than as a drop-in.

## Usage

| You say | What happens |
|---|---|
| Onboard me into this project | Uses orca-onboard and onboard-codebase to build the project wiki and register the project |
| Verify my change before I commit | Uses verify-before-commit to run the pre-commit checks |
| Convert this Markdown to HTML | Uses md-to-html |
| Show me the onboarding tour | Uses tour-guide |
| Extract this website's content | Uses extract-site |
| Set up a new project | Uses new-project-setup |
| Check the impact of this change | Uses impact-check |

## Verification

Confirm the README resolves on the orca branch:

```bash
curl -sL https://raw.githubusercontent.com/Rheinmir/setup/orca/README.md | head -40
```

Confirm a representative skill body in this repository is present before installing:

```bash
curl -sL https://raw.githubusercontent.com/Rheinmir/setup/orca/.overstack/doyourmagic/dym/SKILL.md | head -30
```

The 106 named skills live in the separate Rheinmir/skills repository, so review its SKILL.md files directly before installing the skills layer.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| orca-onboard | Fail | Warn | Warn |
| docs-site-macos | Pass | Warn | Pass |
| verify-before-commit | Pass | Pass | Pass |
| sync-template | Pass | Warn | Warn |
| query | Fail | Pass | Pass |
| propose | Pass | Pass | Pass |
| orca-workflow | Warn | Warn | Warn |
| md-to-html | Pass | Pass | Pass |
| onboard-codebase | Pass | Pass | Pass |
| impact-check | Pass | Pass | Pass |
| extract-site | Pass | Pass | Warn |
| caveman | Pass | Pass | Fail |
| safe-change | Pass | Pass | Pass |
| lint | Pass | Pass | Pass |
| ingest | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 16,840 combined installs across 95 indexed listings; 10 GitHub stars; MIT license; last pushed Nov 18, 2026. Counts drift over time.
- The README and all installation documentation are written in Vietnamese; the commands above are quoted verbatim, but the surrounding instructions and the docs site are Vietnamese-only.
- The install index outruns this repository's tree: the 106 named skills live in the separate Rheinmir/skills repository (split Oct 14, 2026), so no in-table listing has a SKILL.md counterpart in this repository's current tree.
- The pack ships no per-skill descriptions, so every Use For cell is name-level.
- The installer registers a remote MCP server by default and can pull the orca-graph engine from a separate repository, a larger trust surface than Markdown-only skills.
- Three sampled skills carry Fail cells: orca-onboard and query on Gen Agent Trust Hub, and caveman on Snyk.

## Related

- [Deep Agents - Batteries-Included Agent Harness Setup](/hermes/skills/catalog/deepagents-setup)
- [Wyatt Walsh Agents - Skill Governance and Orchestration](/hermes/skills/catalog/wyattowalsh-agents-setup)
- [Skill Repo Manager - Hermes Repository Setup Guide](/hermes/skills/catalog/skill-repo-manager-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read the README with a translation tool first; the install and operations documentation are Vietnamese.
- Install skills-only with npx -y skills add rheinmir/skills#main --global --all if you only want the 106 skills without the harness.
- Run the bootstrap with --no-mcp to skip the remote MCP registration until you have reviewed what it points at.
- Pass --no-graph to skip the optional orca-graph engine unless you need the dispatch UI.
- Treat the deterministic guardrails under harness/validators as the part worth studying, since they are the mechanism a prompt cannot override.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
