---
title: Petr Kindlmann QA Skills - 50-Skill Test Suite
description: "petrkindlmann/qa-skills - 50 skills, 25.3K combined installs. QA and test-automation skills for any Agent Skills Standard runtime: Playwright and Cypress automation, API/visual/accessibility testing, AI test generation, and release readiness."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/petrkindlmann-qa-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "qa"]
---

# Petr Kindlmann QA Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/petrkindlmann/qa-skills) (25.3K combined installs)
**GitHub:** [petrkindlmann/qa-skills](https://github.com/petrkindlmann/qa-skills) (102⭐, MIT)
**Category:** QA & Test Automation
**First Seen:** April 1, 2026 (skills.sh)
**Quality Tier:** 🟡 Beta (Gen Agent Trust Hub Warn on `playwright-automation`; Socket Pass / Snyk Pass)

The most comprehensive agent-native QA cluster on skills.sh: 50 skills covering the full testing lifecycle for Claude Code, Codex, Cursor, and any Agent Skills Standard runtime. The flagship `playwright-automation` skill asks discovery questions first (TypeScript vs JS, browsers, existing suite vs fresh, single vs multi-site), then scaffolds a Playwright project; around it sit strategy skills (test-strategy, risk-based-testing, shift-left), generation skills (ai-test-generation, unit-testing), and gates (release-readiness, qa-dashboard, quality-postmortem).

---

## Installation

```bash
npx skills add petrkindlmann/qa-skills --skill playwright-automation
npx skills add petrkindlmann/qa-skills --skill api-testing
npx skills add petrkindlmann/qa-skills --skill release-readiness
npx skills add petrkindlmann/qa-skills --skill ai-qa-review
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| playwright-automation | 798 | Browser E2E suites (TypeScript-first, multi-site fixtures) |
| api-testing | 602 | REST/API contract and integration tests |
| test-strategy / test-planning / risk-based-testing | 524-576 | Test strategy and planning |
| exploratory-testing / bug-reproduction | 573 / 501 | Manual-style exploratory passes and repro |
| ai-test-generation / ai-qa-review / ai-bug-triage | 529-566 | AI-assisted test authoring, review, triage |
| unit-testing / coverage-analysis | 529 / 489 | Unit tests and coverage |
| visual-testing / accessibility-testing | 558 / 528 | Visual regressions and a11y |
| agentic-browser-testing / ai-system-testing | 500 / 514 | Testing agent-driven systems |
| performance-testing / chaos-engineering / testing-in-production | 470-521 | Load, chaos, and production testing |
| security-testing / compliance-testing | 511 / 463 | Security and compliance gates |
| cypress-automation / selector-drift-recovery | 461 / 448 | Cypress suites and locator maintenance |
| contract-testing / service-virtualization | 488 / 460 | API contracts and virtual services |
| release-readiness / qa-dashboard / quality-postmortem | 524 / 487 / 465 | Release gates and quality reporting |
| (≈16 more) | <510 each | database, mobile, email, payment testing; CI/CD integration; test data management |

## Prerequisites

- Node.js for Playwright/Cypress suites (TypeScript recommended)
- Browser binaries via `npx playwright install chromium` for E2E work

## CorpusIQ Use Cases

- **Product quality gates** - `release-readiness` + `qa-dashboard` mirror CorpusIQ's pre-publish gate doctrine for product releases, not just content
- **Eval infrastructure** - the ai-qa-review / ai-test-generation patterns complement the corpusiq-agent-eval YAML dataset approach
- **Browser-UI verification** - selector-drift-recovery and visual-testing skills directly serve CorpusIQ's dashboard and connector UI testing
- **Agent-system testing** - agentic-browser-testing and ai-system-testing are rare, directly relevant skills for testing agent products like CorpusIQ itself

## Limitations / Verification

- Gen Agent Trust Hub flags a Warn on the flagship playwright-automation skill - review before production CI
- 50 skills overlap somewhat (qa-start vs qa-do vs qa-project-bootstrap); install flagships, pull others on demand
- Verify install: `npx skills list | grep playwright-automation`

## Security

[Gen Agent Trust Hub: Warn](https://www.skills.sh/petrkindlmann/qa-skills/playwright-automation/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/petrkindlmann/qa-skills/playwright-automation/security/socket) · [Snyk: Pass](https://www.skills.sh/petrkindlmann/qa-skills/playwright-automation/security/snyk)

## Related

- [Momentic QA Skills Setup](/hermes/skills/catalog/momentic-skills-setup)
- [Swift Testing Pro Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
