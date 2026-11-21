---
title: "Hanoi Rainbow - Spec-Driven Engineering Skills Setup Guide"
description: "dauquangthanh/hanoi-rainbow: 41 spec-driven engineering skills - 3.0K combined installs for design review, cloud and legacy migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dauquangthanh-hanoi-rainbow-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "legacy migration", "cloud platform"]
---

# Hanoi Rainbow - Spec-Driven Engineering Skills Setup Guide

**Source:** [dauquangthanh/hanoi-rainbow](https://www.skills.sh/dauquangthanh/hanoi-rainbow) via skills.sh - 3.0K combined installs across 41 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [dauquangthanh/hanoi-rainbow](https://github.com/dauquangthanh/hanoi-rainbow) - 18 stars, MIT license, main branch, last pushed Jan 23, 2026; canonical skills under `skills/<name>/SKILL.md` plus a `rainbow` CLI and 15 slash commands for spec-driven development.
**Category:** Spec-Driven Engineering
**Quality Tier:** 🟡 Yellow - sampled 20 of 41 skills return Pass on Gen Agent Trust Hub with 5 Warn cells on Socket and Snyk and no Fails.

`hanoi-rainbow` is an enterprise engineering skill set from dauquangthanh built around spec-driven development: an agent specifies, clarifies, designs, breaks down and implements instead of coding by trial and error. Its 41 bundled skills span cloud platforms, architecture and design review, backend and frontend work, code quality and legacy mainframe modernization.

The repository ships all 41 skills under a canonical `skills/<name>/SKILL.md` tree, plus 15 slash commands and a `rainbow` CLI that bootstraps projects for Claude Code, Codex, Cursor, Gemini, Copilot and other supported agents. Install through the Agent Skills CLI or the publisher's uv-based CLI; the skills.sh listing indexes every skill with its install count. First seen in the Nov 20, 2026 evening sweep.

## Installation

Install the 41 skills through the Agent Skills CLI:

```bash
npx skills add dauquangthanh/hanoi-rainbow
```

The publisher also ships a `rainbow` CLI that bootstraps the full spec-driven workflow plus the skills for your agent. It needs uv, Python 3.11 or higher, Git and a supported AI agent:

```bash
uv tool install rainbow-cli --from git+https://github.com/dauquangthanh/hanoi-rainbow.git
rainbow init my-project --ai claude
rainbow check
```

Upgrade with the same source and `--force`, or run once without installing via `uvx --from git+https://github.com/dauquangthanh/hanoi-rainbow.git rainbow init my-project`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| frontend-ui-ux-design | 541 | Create UI/UX designs, design systems, component libraries and accessible responsive layouts |
| frontend-design-review | 463 | Review UI/UX quality, accessibility, design systems and responsive patterns |
| keycloak-administration | 335 | Administer Keycloak realms, SSO, RBAC, user federation and security hardening |
| oracle-cloud | 152 | Provision and design OCI compute, networking, storage, databases and IAM |
| backend-design | 130 | Design REST APIs, microservices, database schemas and scalability patterns |
| requirement-review | 129 | Validate requirement completeness, clarity, consistency and testability |
| cobol-migration-analyzer | 78 | Analyze COBOL and JCL for migration to modern Java |
| architecture-design-review | 75 | Review system architecture, patterns, quality attributes and scalability |
| backend-design-review | 73 | Review API design, database architecture and microservices patterns |
| code-quality-review | 57 | Detect code smells, technical debt and maintainability issues |
| bug-analysis | 51 | Analyze bugs, root causes, severity and fix recommendations |
| architecture-design | 50 | Design system components, tech stacks and deployment models |

The remaining 29 indexed listings range from 21 to 49 installs.

## Why This Matters for Hermes Agents

The set covers the two places a general agent is weakest without guidance: turning a vague idea into a disciplined build, and knowing platform-specific or legacy-specific detail. The rainbow workflow makes an agent specify, clarify, design, taskify and implement instead of coding by trial and error, while the review skills for architecture, backend, frontend, code quality and requirements give it checklists and report formats instead of gut feel. The legacy migration analyzers for COBOL, RPG, PL/I and JCL let an agent extract business logic from mainframe source and produce a Java implementation strategy, a capability rarely present by default. The cloud skills encode OCI, AWS, GCP, Azure, IBM and Alibaba configuration and Terraform patterns so an agent provisions against the right service instead of guessing.

## Usage

| You say | What happens |
|---|---|
| Review this system design for scalability and quality attributes | Runs architecture-design-review to validate patterns, quality attributes and technology choices |
| Design the backend API and database schema for this service | Runs backend-design to produce API specs, schemas and implementation guides |
| Analyze this COBOL program for migration to Java | Runs cobol-migration-analyzer to extract business logic and generate a Java strategy |
| Harden our Keycloak realm and set up SSO and RBAC | Runs keycloak-administration for realm, client, federation and hardening guidance |
| Critique this UI design for accessibility and responsiveness | Runs frontend-design-review to score and recommend fixes |

## Verification

```bash
# after install, confirm the skills landed in your agent's skills folder
ls .claude/skills/ 2>/dev/null || ls .github/agents/skills/ 2>/dev/null
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/dauquangthanh/hanoi-rainbow/main/skills/frontend-ui-ux-design/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. The canonical tree lives under `skills/<name>/SKILL.md` with all 41 skills; the skills.sh page lists each with its install count.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frontend-ui-ux-design | Pass | Pass | Pass |
| frontend-design-review | Pass | Pass | Pass |
| keycloak-administration | Pass | Warn | Pass |
| oracle-cloud | Pass | Warn | Warn |
| backend-design | Pass | Pass | Pass |
| requirement-review | Pass | Pass | Pass |
| cobol-migration-analyzer | Pass | Pass | Pass |
| architecture-design-review | Pass | Pass | Pass |
| backend-design-review | Pass | Pass | Pass |
| code-quality-review | Pass | Pass | Pass |
| bug-analysis | Pass | Pass | Warn |
| architecture-design | Pass | Pass | Pass |
| ibm-mainframe | Pass | Pass | Pass |
| google-cloud | Pass | Pass | Pass |
| technical-writing | Pass | Pass | Pass |
| database-design | Pass | Pass | Pass |
| rpg-migration-analyzer | Pass | Warn | Pass |
| alibaba-cloud | Pass | Pass | Pass |
| requirements-gathering | Pass | Pass | Pass |
| backend-code-review | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 3,004 combined installs across 41 indexed listings; 18 GitHub stars; MIT license; last pushed Jan 23, 2026. Counts drift over time.
- The repository was last pushed Jan 23, 2026, roughly ten months before this snapshot, so cloud platform, framework and migration guidance can lag as those targets evolve.
- Only 20 of the 41 listings carry skills.sh verdicts; the other 21 are unverified on that platform.
- Install counts on skills.sh are cumulative totals, not recent adoption, so a high count reflects accumulated downloads rather than current activity.

## Related

- [Code Review Skill - Review Workflow Setup](/hermes/skills/catalog/code-review-skill-setup)
- [GitHub Code Review - PR Review Setup](/hermes/skills/catalog/github-code-review-setup)
- [Alibaba Open Code Review - Review Skills Setup](/hermes/skills/catalog/alibaba-open-code-review-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `rainbow check` after install to confirm git and your agent CLIs are present before initializing a project.
- Start greenfield projects with `/rainbow.regulate` and brownfield projects with `/rainbow.assess-context` so principles and context land before any code.
- Run `/rainbow.clarify` before `/rainbow.design` to close underspecified requirements and avoid downstream rework.
- For legacy migration work, run the analyzer (COBOL, RPG, PL/I or JCL) against a sample file first to calibrate the Java output before committing to a full migration.
- Prefer a one-time `uv tool install` plus `--force` upgrades over repeated `uvx` one-off runs so the CLI stays available everywhere.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*