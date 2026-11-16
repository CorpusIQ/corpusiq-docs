---
title: "Pandoscope Skills - Agentic Engineering Library"
description: "pandoscope/skills - 14.6K combined installs across 14 indexed listings: specs, ADRs, TDD, domain modeling and decisions for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pandoscope-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "adrs", "tdd", "domain modeling"]
---

# Pandoscope Skills - Setup Guide

**Source:** [pandoscope/skills](https://www.skills.sh/pandoscope/skills) via skills.sh - 14.6K combined installs across 14 indexed listings; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 1 star, MIT license, `main` branch, last pushed 2026-11-10, `SKILL.md` files under `original/<name>/` and `derived/<name>/`
**Category:** Agentic engineering - specs, ADRs and domain modeling
**Quality Tier:** 🟡 Yellow - one sampled skill (grilling) fails the Gen Agent Trust Hub; the rest pass or carry minor warns.

Pandoscope is a canonical agent skills repository that treats itself as the single source of truth: consumer repos install copies via `npx skills` and never edit skills locally. The layout separates four concerns: `original/` holds skills authored here, `derived/` holds condensed vendor derivations pinned via `metadata.derived-from`, `docs/` carries the architecture and a glossary of ubiquitous language, and `tests/` holds pressure scenarios and fixtures that are never shipped.

The skills are deliberately tool-agnostic. No consumer-repo tooling such as tracker CLIs is hardcoded, and skill descriptions state triggers only ("Use when ..."), never workflow. Prose follows the `original/writing-prose` rules, and its `check.sh` runs the rules code can judge.

## Installation

From a consumer repo:

```sh
# list available skills
npx skills add pandoscope/skills --list

# install selected skills (project scope, Claude Code)
npx skills add pandoscope/skills --skill documenting-decisions -a claude-code -y

# restore on a fresh clone
npx skills experimental_install

# update
npx skills update -p -y
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| caveman | 1,970 | Terse chat mode: drop filler and hedging while keeping technical accuracy. |
| documenting-decisions | 1,942 | Route human attention to decisions in agent-generated code with DECISION markers. |
| tdd | 1,877 | Red-green-refactor with an auditable commit protocol. |
| domain-modeling | 1,827 | Build and sharpen the project's domain model and ubiquitous language. |
| to-spec | 1,732 | Turn the conversation into a spec published to the tracker, no interview. |
| writing-adrs | 1,723 | Format, numbering and when-to-write criteria for ADRs in docs/adr/. |
| to-tickets | 1,710 | Break a plan or spec into tracer-bullet tickets with blocking edges. |
| grilling | 1,694 | Stress-test a plan through scored multiple-choice questions. |

The remaining 6 indexed listings range from 5 to 47 installs.

## Why This Matters for Hermes Agents

The strongest idea in this collection is that decisions, not code, are what drift. documenting-decisions plants DECISION markers in code comments so a reviewer, human or agent, sees what changed and why. writing-adrs gives those decisions a durable home in `docs/adr/`. Together they attack the exact failure a long-running agent has: it makes a sensible call today and nobody can reconstruct the reasoning next month.

The `derived/` discipline matters too. Vendor derivations are pinned via `metadata.derived-from` to a full commit URL, so a derivation stays diffable against upstream. That is a rare and useful pattern for an agent that maintains skills over time rather than just installing them.

The glossary of ubiquitous language, one file per term resolved through `uvx disambiguate <term>`, gives the agent a shared vocabulary instead of letting each session invent its own names for the same concept.

## Usage

| You say | What happens |
|---|---|
| "Turn our conversation into a spec" | to-spec synthesizes the discussion into a spec published to the tracker. |
| "Write an ADR for this decision" | writing-adrs applies the numbering and when-to-write rules to docs/adr/. |
| "Implement this feature test-first" | tdd drives red-green-refactor with an auditable commit protocol. |
| "Split this spec into tickets" | to-tickets breaks it into tracer-bullet tickets with blocking edges. |
| "Stress-test my plan" | grilling runs scored multiple-choice questions against the idea. |
| "Pin down what this term means here" | domain-modeling records the term in the domain model and glossary. |
| "Talk in caveman mode" | caveman drops filler and hedging while keeping technical accuracy. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/pandoscope/skills/main/derived/grilling/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/pandoscope/skills/main/derived/caveman/SKILL.md | head -20
npx skills add pandoscope/skills --list
```

Derived skills live under `derived/<name>/` and original skills under `original/<name>/`; confirm the path exists in the current tree before installing a specific skill.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| caveman | Pass | Pass | Pass |
| documenting-decisions | Pass | Pass | Warn |
| tdd | Pass | Pass | Pass |
| domain-modeling | Pass | Pass | Pass |
| to-spec | Warn | Pass | Pass |
| writing-adrs | Pass | Pass | Pass |
| to-tickets | Pass | Pass | Warn |
| grilling | Fail | Pass | Pass |

grilling is the only skill with a Gen Agent Trust Hub Fail in the sample; it asks scored multiple-choice questions about the user's own plan, so review what it does before enabling it unsupervised.

## Limitations

- Snapshot data, verified 2026-11-15: 14,554 combined installs across 14 indexed listings; 1 GitHub star; MIT; last pushed 2026-11-10. Counts drift over time.
- grilling carries the only Gen Agent Trust Hub Fail in the sample. Treat it as supervised-use and re-check its skills.sh security page before production.
- derived/ skills are vendor derivations pinned via `metadata.derived-from`; original/ skills are the canonical authors. Do not edit skills in consumer repos, they are overwritten on update.
- The repository has 1 GitHub star at snapshot, so it carries less community vetting than larger suites.
- The glossary resolves through `uvx disambiguate <term>`, which needs the uv toolchain available on the host.

## Related

- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)
- [Stark AI Agent Skills - Engineering Workflow Kit](/hermes/skills/catalog/stark-ai-agent-skills-setup)
- [Sentimony Agentic Workflow - Spec to PR Setup](/hermes/skills/catalog/sentimony-agentic-workflow-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Edit skills only in the canonical repo; local copies in consumers get overwritten on update.
- Keep descriptions as triggers only ("Use when ..."), never workflow.
- Put test artifacts in `tests/`, never inside skill folders; name fixture manifests `SKILL.fixture.md` so discovery ignores them.
- For discipline-enforcing skills, baseline-test against an agent without the skill first.
- Keep SKILL.md short and split heavy reference into separate files inside the skill folder.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
