---
title: "Simota Agent Skills - 90-Agent Suite Setup Guide"
description: "simota/agent-skills: 90 specialist agents with Nexus hub-spoke orchestration for Claude Code, Codex and Antigravity CLI - 8.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/simota-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent orchestration", "claude code", "ai agents"]
---

# Simota Agent Skills - Setup Guide

**Source:** [simota/agent-skills](https://www.skills.sh/simota/agent-skills) via skills.sh - 8.4K combined installs across 95 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [simota/agent-skills](https://github.com/simota/agent-skills) - 102 stars, MIT licence, main branch, last pushed Nov 18, 2026. One directory per skill at the repository root, each with a SKILL.md entry point plus a reference/ subdirectory (1,917 files in the tree).
**Category:** Multi-Agent Orchestration
**Quality Tier:** 🟠 Orange - 1 Fail among 20 sampled verdicts (echo: Gen Agent Trust Hub); 3 Warn (scout: Snyk, probe: Socket, nexus: Socket); MIT licence.

The agent-skills suite bundles 90 specialist agents plus 3 project-local extensions into a single tree for Claude Code, Codex CLI and Antigravity CLI. Every agent owns one domain, and the Nexus orchestrator routes each task to the right specialist, designs the minimum viable agent chain and runs it end to end. The suite is aligned with the Anthropic Agent Skills spec and ships hub-spoke orchestration through Nexus with 49 Recipes and 11 Skill Packs, spanning development, security, design, testing, FinOps, compliance, observability and AI/ML.

The make-based installer symlinks one working tree into all three CLI skill directories, so a single git pull updates every CLI at once. Skills load their reference files on demand, which keeps a 1,917-file repository from flooding an agent's context.

## Installation

```bash
git clone https://github.com/simota/agent-skills.git ~/repos/agent-skills
cd ~/repos/agent-skills
make link
```

`make link` symlinks each skill directory into `~/.claude/skills`, `~/.agents/skills` and `~/.gemini/antigravity-cli/skills` individually, so every CLI reads the same working tree. Existing skills are preserved: a name that already exists is reported and skipped, never overwritten. Use `make status` to see the link count per CLI, and `make unlink` to remove only the links this installer created.

When the target directory does not exist yet and only one CLI needs the skills, clone straight into that directory:

```bash
git clone https://github.com/simota/agent-skills.git ~/.claude/skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| voice | 736 | User feedback collection: NPS surveys, review and sentiment analysis, feedback classification and insight reports |
| muse | 721 | Design tokens and design system foundations: spacing, color, typography, dark mode and token systems applied to codebases |
| vision | 216 | Creative direction for UI/UX: redesigns, new designs, trend application, Design System construction and design-agent orchestration |
| gear | 164 | Dependencies, CI/CD, advanced GitHub Actions workflows, containers, secrets and operational config |
| growth | 137 | SEO (meta/OGP/JSON-LD), SMO, CRO and GEO (AI citation optimization) for search, conversion and AI visibility |
| sherpa | 114 | Task decomposition: breaking Epics into atomic steps under 15 minutes, with progress tracking and drift prevention |
| radar | 110 | Test coverage: edge-case tests, flaky-test repair and regression guards across JS/TS, Python, Go, Rust and Java |
| quill | 107 | Documentation: JSDoc/TSDoc additions, README updates and replacing any types with proper definitions |
| sentinel | 106 | Static security analysis (SAST): hardcoded secrets, SQL injection, input validation, security headers and dependency CVEs |
| polyglot | 106 | i18n and l10n: extracting hardcoded strings to t() calls, Intl API formatting and RTL layout support |
| scout | 101 | Bug root-cause analysis: reproduction steps and impact assessment, investigation only |
| gateway | 101 | API design and review: OpenAPI spec generation, versioning, breaking-change detection, REST and GraphQL |
| echo | 101 | Synthetic demand and flow evaluation: cognitive walkthroughs, feature requests, unmet needs and JTBD |

The remaining 82 indexed listings range from 45 to 99 installs (probe 99; zen, nexus and forge 98 each; palette and atlas 97 each).

## Why This Matters for Hermes Agents

Most agent setups treat each skill as an island. This suite is the opposite: ninety specialists that share one routing layer. The Nexus orchestrator classifies a task, selects the minimum chain of agents, runs it and verifies the result, so a single vague request can fan out into spec, prototype, implementation, tests and documentation without a human wiring each step. The hub-spoke design matters for builders because it keeps each SKILL.md small: a skill loads its own reference files on demand, so the whole tree never floods context at once. The roster spans the full delivery surface, from security and design through testing, FinOps, compliance and observability, which means one install covers the workflows a generic agent otherwise stumbles through. The shared `.agents/` directory and `_common/` protocols give agents a persistent memory and shared boundaries, so chains can hand off context between specialists. MIT licensing and the symlink installer keep adoption low-friction across Claude Code, Codex and Antigravity CLI.

## Usage

| You say | What happens |
|---|---|
| /Nexus I want to implement a login feature | Nexus classifies the task, picks the minimum agent chain, runs it and checks acceptance criteria |
| /Scout Investigate the cause of this bug | Scout does root-cause analysis: reproduction steps, fix location and impact, with no code changes |
| /Radar Improve test coverage | Radar adds edge-case and regression tests and repairs flaky tests across supported languages |
| /Vision I want to redesign the dashboard with a modern look | Vision drives design direction, then hands off to Muse, Palette, Flow and Forge for implementation |
| /Nexus add a user profile editing feature | Nexus runs the Spark, Sherpa, Forge, Builder, Radar, Quill chain end to end |
| /Sherpa plan an e-commerce checkout flow | Sherpa decomposes the Epic into atomic steps under 15 minutes each, with a progress tracker |

## Verification

```bash
# after install, confirm the links landed
make status
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/simota/agent-skills/main/voice/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| voice | Pass | Pass | Pass |
| muse | Pass | Pass | Pass |
| vision | Pass | Pass | Pass |
| gear | Pass | Pass | Pass |
| growth | Pass | Pass | Pass |
| sherpa | Pass | Pass | Pass |
| radar | Pass | Pass | Pass |
| quill | Pass | Pass | Pass |
| sentinel | Pass | Pass | Pass |
| polyglot | Pass | Pass | Pass |
| scout | Pass | Pass | Warn |
| gateway | Pass | Pass | Pass |
| echo | Fail | Pass | Pass |
| probe | Pass | Warn | Pass |
| zen | Pass | Pass | Pass |
| nexus | Pass | Warn | Pass |
| forge | Pass | Pass | Pass |
| palette | Pass | Pass | Pass |
| atlas | Pass | Pass | Pass |
| sweep | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 8,385 combined installs across 95 indexed listings; 102 GitHub stars; MIT licence; last pushed Nov 18, 2026. Counts drift over time.
- Only 20 of 95 listings have skills.sh verdicts; the other 75 are unverified on that platform.
- echo carries a Gen Agent Trust Hub Fail, and scout, probe and nexus carry Warns, so re-check those security pages before production use.
- The install index does not map 1:1 onto the tree: 95 indexed listings against 90 root-level skill directories plus the 3 project-local extensions (orbit, lore, darwin). 17 indexed names have no directory at all in the current tree (researcher, anvil, director, showcase, retain, hearth, arena, sketch, relay, horizon, titan, helm, latch, harvest, pipe, morph and accord), and 15 in-tree directories are not indexed on skills.sh (atelier, chain, chisel, compass, crypt, field, native, pdm, port, prune, seek, tome, trail, vector and vitrine).
- The README counts 90 global skills plus 3 project-local extensions (93 distinct skills), which is fewer than the 95 indexed listings because the marketplace index and the repository roster drift independently.

## Related

- [Blueprint Orchestration Setup](/hermes/skills/catalog/blueprint-orchestration-setup)
- [Oh My Hermes (OMH) Suite - Multi-Agent Orchestration Skills Setup](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup)
- [Subagent-Driven Development - Multi-Agent Task Dispatch Setup](/hermes/skills/catalog/subagent-driven-development-setup)
- [Ruflo - Multi-Agent Orchestration Platform Setup](/hermes/skills/catalog/ruflo-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with /Nexus for anything multi-domain: it designs the chain so you do not have to.
- Keep one working tree via make link so a single git pull updates every CLI at once.
- Run make status after install to confirm each CLI picked up the symlinks.
- For guarded runs, append NEXUS_GUIDED or NEXUS_INTERACTIVE so Nexus confirms at decision points.
- Read a skill's SKILL.md and Boundaries section before first use; shared rules live in _common/.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
