---
title: "PeterHdd Agent Skills - Role-Based Engineering Setup"
description: "peterhdd/agent-skills - 2.9K combined installs: nine role-based engineering agent skills for Claude Code and Codex."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/peterhdd-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "engineering", "role-based", "claude code"]
---

# PeterHdd Agent Skills - Setup Guide

**Source:** [peterhdd/agent-skills](https://www.skills.sh/peterhdd/agent-skills) via skills.sh - 2.9K combined installs across 19 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [peterhdd/agent-skills](https://github.com/peterhdd/agent-skills) - 12 stars, MIT license, last pushed Mar 9, 2026, main branch; nine engineering skills under skills/<name>/SKILL.md, each with a references/ and scripts/ directory.
**Category:** Role-Based Engineering Agent Skills (Claude Code and Codex)
**Quality Tier:** 🟡 Yellow - 19 of 19 listings sampled: 15 pass all three checks, and 4 carry a single non-Pass cell each (two Socket Warns, one Snyk Warn, one Socket None).

peterhdd/agent-skills is a collection of role-based agent skills that give Claude Code and Codex deep domain expertise through decision rules, production-grade code patterns, reference material, and runnable scripts. Built to the Agent Skills Spec, the repo ships nine engineering role packs: security engineer, senior developer, backend architect, system designer, devops automator, frontend developer, mobile app builder, ML engineer, and rapid prototyper.

The install band has a sharp head and a long small tail. The nine in-tree engineering skills hold 652 to 189 installs, while ten additional indexed listings (design, testing, support, project management, marketing, and data roles) sit at 2 to 3 installs each with no counterpart in the current skills/ tree.

## Installation

The README documents the skills CLI, with a single-skill form and an all-skills form:

```bash
# Install a single skill
npx skills add PeterHdd/agent-skills --skill engineering-frontend-developer

# Install all 9 skills
npx skills add PeterHdd/agent-skills --all
```

Requirements are Claude Code or the Codex CLI, the skills CLI (npx skills, no install needed), Python 3.8+ for the Python scripts, and Bash for the shell scripts. After installing, the skill is available in Claude Code sessions automatically.

## What It Provides

skills.sh publishes per-skill install counts for all 19 indexed listings. The nine most-installed skills are listed below; the remaining ten are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| engineering-security-engineer | 652 | threat modeling, OWASP Top 10 remediation, secrets management, and compliance (SOC 2, GDPR, HIPAA) |
| engineering-senior-developer | 372 | lead implementation, architecture decisions, code review, and production-safe rollout across any stack |
| engineering-backend-architect | 371 | scalable backend systems, database schemas, APIs, and cloud infrastructure |
| engineering-system-designer | 367 | distributed system design, capacity planning, sharding, and system design documents |
| engineering-devops-automator | 288 | Terraform, Docker, Kubernetes, and CI/CD for reliable deployments |
| engineering-frontend-developer | 267 | React, Vue, Angular, or Svelte apps with performance and accessibility |
| engineering-mobile-app-builder | 198 | native and cross-platform iOS and Android apps, offline-first and platform integration |
| engineering-ml-engineer | 190 | ML models with PyTorch, HuggingFace Transformers, and scikit-learn |
| engineering-rapid-prototyper | 189 | functional prototypes and MVPs at speed to validate ideas |

The remaining 10 indexed listings range from 2 to 3 installs.

## Why This Matters for Hermes Agents

Each skill is a self-contained directory with a SKILL.md of when-X-do-Y decision rules, a references/ directory of deep patterns, and a scripts/ directory of runnable CLI tools. The role framing means an agent can adopt a specific engineering persona and its decision rules rather than starting from general advice. The security engineer skill is the most-installed, at 652 installs, and bundles threat modeling, OWASP Top 10 remediation with test payloads, and compliance checklists for SOC 2, GDPR, and HIPAA. The system designer skill turns a prompt like a URL shortener into capacity calculations, a sharding strategy, and a full design document. The devops automator produces multi-stage Dockerfiles, Kubernetes deployments with health probes, and Prometheus monitoring. Because every script supports --help and outputs structured markdown, an agent can run the tooling non-interactively and cite concrete output rather than prose.

## Usage

| You say | What happens |
|---|---|
| Review this auth service for vulnerabilities | Uses engineering-security-engineer for OWASP Top 10 and secrets scanning |
| Design the API layer for a multi-tenant SaaS app | Uses engineering-backend-architect for distributed patterns, pagination, and rate limiting |
| Set up CI/CD for our Node.js app with Docker and Kubernetes | Uses engineering-devops-automator for multi-stage Dockerfiles, HPA, and GitHub Actions |
| Build a dashboard with a sortable, filterable data table | Uses engineering-frontend-developer for React patterns and bundle size checks |
| Build an offline-first React Native app with push notifications | Uses engineering-mobile-app-builder for offline sync and state management |
| Design a URL shortener that handles 100M URLs per month | Uses engineering-system-designer for capacity calculations and sharding |
| Prototype a feature idea to validate it fast | Uses engineering-rapid-prototyper for MVP scaffolding and scope limits |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/peterhdd/agent-skills/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/peterhdd/agent-skills/main/skills/engineering-security-engineer/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn and None cells noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| engineering-security-engineer | Pass | Pass | Pass |
| engineering-senior-developer | Pass | Pass | Pass |
| engineering-backend-architect | Pass | Warn | Pass |
| engineering-system-designer | Pass | Pass | Pass |
| engineering-devops-automator | Pass | Pass | Pass |
| engineering-frontend-developer | Pass | Pass | Pass |
| engineering-mobile-app-builder | Pass | Pass | Pass |
| engineering-ml-engineer | Pass | Pass | Pass |
| engineering-rapid-prototyper | Pass | Warn | Pass |
| xr-developer | Pass | Pass | Warn |
| testing-api-tester | Pass | Pass | Pass |
| support-executive-summary-generator | Pass | None | Pass |
| project-manager-senior | Pass | Pass | Pass |
| marketing-app-store-optimizer | Pass | Pass | Pass |
| design-ui-designer | Pass | Pass | Pass |
| design-image-prompt-engineer | Pass | Pass | Pass |
| design-brand-guardian | Pass | Pass | Pass |
| data-analytics-reporter | Pass | Pass | Pass |
| testing-evidence-collector | Pass | Pass | Pass |

Across the 19 sampled skills there are 53 Pass, 3 Warn, 1 None, and 0 Fail cells. Fifteen skills pass all three checks; four carry a single non-Pass cell each (two Socket Warns, one Snyk Warn, one Socket None).

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,923 combined installs across 19 indexed listings; 12 GitHub stars; MIT license; last pushed Mar 9, 2026. Counts drift over time.
- The install band has a sharp head and a long small tail: nine engineering skills hold 652 to 189 installs, while the other ten indexed listings sit at 2 to 3 installs each.
- The install index outruns the tree: xr-developer, testing-api-tester, support-executive-summary-generator, project-manager-senior, marketing-app-store-optimizer, design-ui-designer, design-image-prompt-engineer, design-brand-guardian, data-analytics-reporter, and testing-evidence-collector carry install counts but have no matching directory in the current skills/ tree.
- skills.sh sampled all 19 listings, and four carry a single non-Pass cell: two Socket Warns, one Snyk Warn, and one Socket None. Re-check the security pages before production use.
- The README's install commands use the capitalized PeterHdd spelling, which differs from the lowercase skills.sh listing; GitHub owner names are case-insensitive, so both resolve.

## Related

[Agent Reference Skills - 174 Role Playbooks](/hermes/skills/catalog/agent-reference-skills-setup) | [Zhaono1 Agent Playbook - 24-Role Agent Workflow Suite Setup](/hermes/skills/catalog/zhaono1-agent-playbook-setup) | [Awesome LLM Apps Skills - Role-Based Agent Skills Setup](/hermes/skills/catalog/awesome-llm-apps-skills-setup) | [Herman Skill Playbook Setup](/hermes/skills/catalog/herman-skill-playbook-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with engineering-senior-developer for ambiguous tasks; it encodes planning, estimation, and rollout rules.
- Install a single skill with --skill <name> when you only need one role.
- Run the scripts/ tools with --help; each outputs structured markdown an agent can cite.
- Prefer the all-skills install (--all) only when you want the full nine-role suite.
- Re-check the security pages on skills.sh for backend-architect, rapid-prototyper, xr-developer, and support-executive-summary-generator.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
