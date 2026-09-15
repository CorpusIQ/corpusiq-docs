---
title: "Vigiles - Agent Harness Quality Suite Setup"
description: "zernie/vigiles - 21 skills, 12.3K combined installs. Lighthouse for your agent harness: verify CLAUDE.md/AGENTS.md files, skills, and hooks are real and tested, then tighten guidance rules into enforced linter rules."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vigiles-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "agent quality"]
---

# Vigiles - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/zernie/vigiles) (12.3K combined installs)
**GitHub:** [zernie/vigiles](https://github.com/zernie/vigiles) (15⭐, MIT)
**Category:** Agent Quality & Harness Verification
**First Seen:** June 6, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

"Like Lighthouse for your agent harness" - Vigiles verifies that your CLAUDE.md/AGENTS.md, skills, and hooks are real and tested, then hardens them. The core loop: `strengthen` scans spec files for `guidance()` rules and proposes `enforce()` replacements backed by actual linter rules (free wins auto-applied, costly changes presented as tradeoffs); `verify-docs-findable` checks agents can actually discover the docs; `test-harness` and `debug-my-harness` validate the harness itself; `dogfood-cli` closes the loop by testing your own tooling. A governance-first cluster in the same family as CorpusIQ's internal audit skills.

---

## Installation

```bash
npx skills add zernie/vigiles --skill strengthen
npx skills add zernie/vigiles --skill verify-docs-findable
npx skills add zernie/vigiles --skill test-harness
npx skills add zernie/vigiles --skill deep-research
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| strengthen / edit-spec / adopt-spec / migrate-to-spec | 1.3-1.5K | Spec lifecycle: create, edit, adopt, and harden rules |
| test-harness / debug-my-harness | 1.5K / 973 | Validate and debug the agent harness itself |
| linter-docs / add-a-linter / generate-rule / pr-to-lint-rule | 30-1.4K | Linter rule management from docs and PRs |
| verify-docs-findable / review-docs / audience-check | 250-534 | Documentation discoverability and audience fit |
| deep-research | 670 | Structured deep-research workflow |
| audit-feedback-loop / enforce-rules-format / code-quality | 298-344 | Quality gates and rule formatting |
| screenshot / generate-logo / landing-site | 205-317 | Visual assets for tooling and sites |
| dogfood-cli | 30 | Test your own CLI like a user |

## Prerequisites

- None - prompt-skill suite; no API keys or services
- A spec/AGENTS.md file in the target repo unlocks the strengthen/adopt-spec workflows

## CorpusIQ Use Cases

- **Agent-harness hygiene** - verify-docs-findable and test-harness mirror CorpusIQ's own system-auditor and stack-doctor sweeps, as a cross-check methodology
- **Governance hardening** - the guidance → enforce upgrade loop is a concrete pattern for CorpusIQ's governance baselines (turn prose rules into enforced checks)
- **Docs findability** - audience-check and review-docs pair with CorpusIQ's docs SEO/AEO/GEO passes

## Limitations / Verification

- Small repo (15⭐, 12.3K installs) - early-stage publisher; skills are stable but the ecosystem around them is thin
- Vigiles targets Claude Code conventions (CLAUDE.md/AGENTS.md); adapt paths when applying to Hermes profiles
- Verify install: `npx skills list | grep -E "strengthen|test-harness"`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/zernie/vigiles/strengthen/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/zernie/vigiles/strengthen/security/socket) · [Snyk: Pass](https://www.skills.sh/zernie/vigiles/strengthen/security/snyk)

## Related

- [Trail of Bits Skills Curated - Agent Security Suite](/docs/hermes/skills/catalog/trailofbits-skills-curated-setup)
- [Review Loop Setup](/docs/hermes/skills/catalog/review-loop-skill-setup)
- [Planning With Files Setup](/docs/hermes/skills/catalog/planning-with-files-setup)
