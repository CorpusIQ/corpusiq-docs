---
title: "Shiplight Agent Skills - Test Automation Review Setup"
description: "shiplightai/agent-skills: 7.0K combined installs across 19 listings; test-automation and review skills for verifying and shipping with confidence."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shiplightai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "test automation", "code review", "e2e testing"]
---

# Shiplight Agent Skills - Setup Guide

**Source:** [shiplightai/agent-skills](https://www.skills.sh/shiplightai/agent-skills) via skills.sh - 7.0K combined installs across 19 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 2 stars, MIT licence, `main` branch, last pushed 2026-07-08; the repository is archived and read-only. Skills live as `skills/<name>/SKILL.md`, one directory per skill.
**Category:** Test automation and application review
**Quality Tier:** 🟠 Orange - 2 Fail cells among the 12 sampled skills (compliance-review, security-review); MIT licence; the repository is archived.

Shiplight Agent Skills is a set of AI-powered test-automation skills for coding agents: verify UI changes in the browser, create and triage YAML end-to-end tests, and run eight domain reviews through a single review entry point. Every skill depends on the Shiplight MCP server. The repository is archived and read-only, with development moved to ShiplightAI/agent-skills-v2.

On skills.sh the suite indexes as 19 listings. The eight review listings (security, privacy, compliance, design, resilience, performance, SEO, GEO) are the review orchestrator's domains rather than standalone skills: the current tree ships one skills/review/SKILL.md with the domain playbooks under skills/review/references/. The cloud skill needs a Shiplight subscription, and create-tests is a deprecated alias for create-yaml-tests.

## Installation

Install the skills and the Shiplight MCP server for Claude Code:

```bash
npx -y skills add ShiplightAI/agent-skills -a claude-code -y && \
npx -y add-mcp "npx -y @shiplightai/mcp@latest" -n shiplight --env PWDEBUG=console -a claude-code -y
```

For Cursor or Codex, swap the `-a` flag. Install to every detected agent with `--all`, or to a user-level directory with `-g`. Install a subset by name:

```bash
npx skills add ShiplightAI/agent-skills --skill verify --skill triage -a claude-code
```

Restart the agent after installing. Update with `npx skills update`. The cloud skill requires a Shiplight subscription.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| verify | 637 | Visually confirm UI changes in the browser after a code change, using Shiplight MCP tools. |
| review | 608 | Single entry point that triages an app and runs the right domain reviews (security, privacy, compliance, design, resilience, performance, SEO, GEO). |
| cloud | 593 | Sync local tests with Shiplight cloud: push and pull YAML test cases, templates and functions (subscription required). |
| triage | 584 | Triage failing Shiplight YAML tests: reproduce failures, inspect evidence, and apply minimal correct fixes. |
| create-tests | 495 | Deprecated alias for create-yaml-tests; redirects to the YAML test authoring workflow for backward compatibility. |
| privacy-review | 418 | Privacy review domain (PII, tracking, consent, GDPR/CCPA) of the review orchestrator; no standalone SKILL.md. |
| design-review | 418 | Design review domain (responsive, accessibility, typography, i18n) of the review orchestrator. |
| compliance-review | 418 | Compliance review domain (HIPAA, SOC 2, PCI-DSS, GDPR) of the review orchestrator. |
| seo-review | 416 | SEO review domain (meta, structured data, crawlability) of the review orchestrator. |
| resilience-review | 416 | Resilience review domain (error handling, degradation, API contracts) of the review orchestrator. |
| geo-review | 416 | GEO review domain (AI citation readiness, llms.txt, entity clarity) of the review orchestrator. |
| security-review | 409 | Security review domain (OWASP, auth, injection, access control, supply chain) of the review orchestrator. |
| performance-review | 407 | Performance review domain (Core Web Vitals, bundles, runtime) of the review orchestrator. |

The remaining 6 indexed listings range from 2 to 366 installs.

## Why This Matters for Hermes Agents

For an agent that changes UI and tests, the failure mode is shipping without looking: a code change lands, the tests pass, and nobody verified the actual rendered result. These skills close that loop, turning "verify the change in the browser" and "review the app before launch" into repeatable, auditable workflows instead of ad-hoc checks.

The review skill is the reusable pattern: one entry point that triages what needs reviewing and dispatches to the right domain playbook, with each domain backed by a named standard (OWASP for security, GDPR/CCPA for privacy, HIPAA/SOC 2/PCI-DSS for compliance, Core Web Vitals for performance). That single-orchestrator design is worth copying for any agent that must cover many review lenses.

The skills are plain `SKILL.md` files with reference docs, so the review playbooks are readable by any harness even though the one-line installers target Claude Code, Cursor and Codex. Note the repository is archived, so treat the install commands as point-in-time.

## Usage

| You say | What happens |
|---|---|
| "Verify this UI change" | verify opens the change in the browser and confirms it visually. |
| "Review my app before launch" | review triages the app and runs the relevant domain reviews, returning one report. |
| "This YAML test is failing" | triage reproduces the failure, inspects evidence, and applies a minimal fix. |
| "Write tests for this feature" | create-yaml-tests plans and scaffolds deterministic YAML end-to-end tests. |
| "Review our app's security" | review runs the security domain (OWASP, auth, injection, supply chain). |
| "Check our AI citation readiness" | review runs the GEO domain (llms.txt, entity clarity, citation readiness). |
| "Push our tests to the cloud" | cloud syncs local YAML tests with Shiplight for scheduled runs. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/ShiplightAI/agent-skills/main/skills/review/SKILL.md
```

Then install the skills and the MCP server, restart the agent, and ask it to verify a change to confirm the loop works. The archived repository means the tree will not change, so the probe stays stable.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| verify | Pass | Pass | Warn |
| review | Pass | Pass | Pass |
| cloud | Pass | Pass | Pass |
| triage | Pass | Pass | Pass |
| create-tests | Pass | Warn | Pass |
| privacy-review | Pass | Pass | Warn |
| design-review | Pass | Pass | Pass |
| compliance-review | Pass | Pass | Fail |
| seo-review | Pass | Pass | Warn |
| resilience-review | Pass | Pass | Warn |
| geo-review | Pass | Pass | Warn |
| security-review | Pass | Pass | Fail |

The sample covers 12 of the 19 indexed listings. The two Fail cells sit on the compliance-review and security-review domains; several other review domains carry a Snyk Warn, while the orchestrator review and the core test skills pass cleanly.

## Limitations

- Snapshot data, verified Nov 18, 2026: 7,041 combined installs across 19 indexed listings; 2 GitHub stars; MIT licence; last pushed 2026-07-08 (repository archived). Counts drift over time.
- The repository is archived and read-only; development moved to ShiplightAI/agent-skills-v2, so the skills here will not receive updates.
- The eight review listings are domains of the review orchestrator, not standalone skills; they have no individual SKILL.md in the current tree.
- create-tests is a deprecated alias for create-yaml-tests, and the shiplight-project listing has no counterpart in the current tree.
- Every skill depends on the Shiplight MCP server, and the cloud skill additionally needs a Shiplight subscription.

## Related

- [Security Hardening - AI Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [React Doctor - React Codebase Diagnostics Setup](/hermes/skills/catalog/react-doctor-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the skills and the MCP server together; the skills do nothing without the Shiplight MCP server.
- Use review as the single entry point and let it triage, rather than remembering which domain to call.
- Run verify after every UI change so the rendered result is checked, not just the tests.
- Read a domain playbook directly from skills/review/references/ to lift one lens into your own review flow.
- Prefer agent-skills-v2 for new installs since this repository is archived.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
