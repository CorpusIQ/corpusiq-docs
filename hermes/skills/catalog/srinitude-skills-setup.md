---
title: "Srinitude Skills - Portable Agent Skills Setup"
description: "Setup guide for srinitude/skills - 10.6K combined installs. 23 portable skills with validation suites and a bundled local MCP server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/srinitude-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "skill infrastructure", "mcp", "validation"]
---

# Srinitude Skills - Setup Guide

**Source:** [srinitude/skills](https://www.skills.sh/srinitude/skills) via skills.sh - 10.6K combined installs across 23 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [srinitude/skills](https://github.com/srinitude/skills) (2 stars, MIT; pushed 2026-09-30; layout `skills/<name>/SKILL.md` with root `plugin.json` and `mcp.json`)
**Category:** Skill Infrastructure / Agent Tooling
**Quality Tier:** 🟡 Beta - Agent Plugins v1.0.0 package; MIT; evaluation-driven; mixed sampled verdicts - see Security

srinitude publishes 23 portable skills as a single Agent Plugins v1.0.0 package: one canonical skills tree, root `plugin.json` and `mcp.json` manifests, a bundled read-only local MCP server, and trigger, behavior, failure, recovery, and speed evaluation suites behind the skills. The catalog is small but almost every listing is heavily used: 14 of the 23 sit at 500+ installs, led by `starting-point` (714), `reify` (691), `visual-design-system-extractor` (682), and `skill-factory` (681).

The skills cluster into three groups. Agent-behavior gates sharpen how an agent works: `starting-point` checks whether a prescribed method can actually reach the user's outcome, `outcome-bounded-work` separates outcomes from recipes, `logic-audit` hunts contradictions, `would-humans-actually` and `would-agents-actually` test action-dependent claims, `timebox` bounds effort, and `meaning-preserving-rewrite` protects meaning during edits. A skill-authoring cluster (`skill-factory`, `simplify-skill`, `dedupe`, `goal-prompt`) covers building and maintaining skills themselves. A design and utility group spans `visual-design-system-extractor`, `always-current-datetime` (558), and the design skills in the tail. MIT licensed, though the repository itself is young (first indexed Oct 9, 2026).

---

## Installation

Prerequisites: Node.js for the `npx` skills CLI; local development of the package targets Node 24+ and a `mise` toolchain.

```bash
# Inspect first, then install
npx skills add srinitude/skills --list
npx skills add srinitude/skills
```

Claude Code plugin route:

```text
/plugin marketplace add srinitude/skills
/plugin install srinitude-skills@srinitude-skills
```

Gemini CLI route:

```sh
gemini extensions install https://github.com/srinitude/skills
```

The README documents per-client routes (Codex, ChatGPT, Cursor, opencode, Continue, Aider, and a Hermes Agent adapter). Note: the CLI reports anonymous install telemetry to skills.sh unless `DISABLE_TELEMETRY=1` is set.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| starting-point | 714 | Start from the user's observable end state: pick the starting boundary and the completion proof before running a prescribed method |
| reify | 691 | Turn a vague idea, stray thought, or uncertain direction into a concrete outcome, tested design, decision record, or executable handoff |
| visual-design-system-extractor | 682 | Reverse-engineer reference images, screenshots, moodboards, or a live site URL into design tokens, art direction, motion rules, and a YAML style spec |
| skill-factory | 681 | Turn a workflow into a new agent skill: scaffolding, validation, evaluation, scripts, tests, and user-level or project-level variants |
| always-current-datetime | 558 | Refresh the current date and time when replying |
| outcome-bounded-work | 555 | Separate outcomes from recipes when instructions mix them |
| meaning-preserving-rewrite | 545 | Rewrite rules and instructions without losing meaning |
| timebox | 544 | Keep work inside a stated time limit |
| logic-audit | 544 | Find contradictions and reasoning gaps |
| would-humans-actually | 543 | Pressure-test claims that depend on people taking a real action |
| dedupe | 541 | Deduplicate bounded collections |
| simplify-skill | 540 | Simplify a skill without losing its behavior |
| would-agents-actually | 536 | Pressure-test claims that depend on an agent taking a real action |
| goal-prompt | 534 | Package source input for a standing goal |

The remaining 9 indexed listings range from 1 to 315 installs, led by mobile-first-website-design (315), prompt-enhancer (313), and tool-call-configuration-for (306), and ending at figma-code-connect-design-system with a single install.

## Why This Matters for Hermes Agents

Skills are only as good as their stopping conditions, and this package is built around exactly that failure mode: each skill encodes when it applies, when it does not, and what evidence counts as done. The evaluation discipline is the rare part: the repository ships trigger, behavior, failure, recovery, and speed suites behind the skills, though the README is precise that fixture results prove runner behavior only, not model behavior. The bundled MCP server is read-only by design (`list_skills`, `search_skills`, `get_skill`, `get_reference`, `get_eval_manifest`, `validate_skill`), confines paths to the repository skill tree, and has no write tool, telemetry, credentials, or network calls. For Hermes agents the value is reliability tooling: gates like `starting-point` and `would-humans-actually` catch wrong-metric and unproven-claim work early, while `skill-factory` turns repeated workflows into maintainable skills. One caveat: the sampled verdicts are mixed (a Socket Warn on `starting-point`; Socket and Snyk Warns on `visual-design-system-extractor`).

## Usage

| You say | What happens |
|---|---|
| "A/B test the signup button color" | starting-point checks whether the prescribed method reaches the real outcome (conversion) before doing the request as written |
| "Turn this rough idea into something concrete" | reify converts the fragment into an outcome, a tested design, a decision record, or an executable handoff |
| "Extract a design system from these screenshots" | visual-design-system-extractor produces design tokens, art direction, and a YAML style spec |
| "Make a skill for this workflow" | skill-factory scaffolds, validates, and evaluates the new skill, including variants |
| "Rewrite these rules more clearly, same meaning" | meaning-preserving-rewrite guards against meaning loss during the edit |
| "Will people actually use this feature?" | would-humans-actually tests the people-action assumption; would-agents-actually covers agent actions |
| "Keep this investigation inside 30 minutes" | timebox bounds the work and forces a stopping point |

## Verification

```bash
# Confirm installed (paths depend on your agent)
npx skills list | grep -i srinitude

# Review the flagship skill straight from GitHub before installing (returns 200)
curl -s https://raw.githubusercontent.com/srinitude/skills/main/skills/starting-point/SKILL.md | head -20
```

Package layout check: `skills/<name>/SKILL.md` for each skill, plus root `plugin.json` and `mcp.json` for Agent Plugins v1 clients. For MCP-capable clients, build the bundled server with `mise run build-mcp` from a checkout.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| starting-point | Pass | Warn | Pass |
| design-system-extractor | - | - | - |
| visual-design-system-extractor | Pass | Warn | Warn |

Mixed results: both skills with full verdicts carry a Socket Warn, and visual-design-system-extractor also carries a Snyk Warn. The bundled MCP server's design is explicitly read-only with paths confined to the skill tree, but the third-party verdicts above are what matter for supply-chain review.

## Limitations

- Mixed sampled verdicts: starting-point (Socket Warn) and visual-design-system-extractor (Socket Warn + Snyk Warn).
- Small repository: 2 GitHub stars, independent publisher, last pushed Sep 30, 2026.
- Eval honesty: fixture results prove runner behavior only; the README is explicit that they are not evidence about a language model.
- Local development workflow assumes Node 24+ and mise (`mise run bootstrap`, `mise run ci`); a plain skills CLI install needs less.
- The skills CLI reports anonymous install telemetry to skills.sh unless `DISABLE_TELEMETRY=1` is set.
- Snapshot data, verified Oct 10, 2026: 10.6K combined installs across 23 indexed listings; 2 GitHub stars; MIT; last pushed Sep 30, 2026. Counts drift over time.

## Related

- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup) - vet third-party skills before installing them
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup) - an alternative authoring pipeline to compare with skill-factory
- [Basic Memory Skills - Agent Knowledge Graph Suite Setup](/hermes/skills/catalog/basic-memory-skills-setup) - persist the learnings these workflow skills produce
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Inspect before installing with `npx skills add srinitude/skills --list`; the catalog is small enough to read in one pass.
- The package is deliberately single-source: every client route loads the same canonical SKILL.md files, so behavior stays consistent across Claude Code, Codex, Gemini CLI, Cursor, and Hermes.
- The bundled MCP server is for discovery and validation only (six read-only tools); it never writes and makes no network calls.
- Skills declare `metadata.scope: "user"` so they are available across projects by default; project scope exists as a variant.
- Run the local gate (`mise run validate`, `mise run eval`, `mise run ci`) when authoring or modifying skills from a checkout.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
