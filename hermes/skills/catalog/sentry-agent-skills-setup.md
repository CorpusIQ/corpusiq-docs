---
title: "Sentry Agent Skills — Security & Code Review Suite Setup"
description: "getsentry/skills — 31 skills, 85.3K installs: security review, code simplification, bug finding, PR automation, and GitHub Actions security review from the Sentry team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sentry-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "security", "code review", "sentry"]
---

# Sentry Agent Skills — Setup Guide

**Source:** [getsentry/skills](https://skills.sh/getsentry/skills)
**GitHub:** [getsentry/skills](https://github.com/getsentry/skills)
**Skills:** 31 skills · 85.3K total installs
**Category:** Code Review & Security
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟢 Production (official org — Sentry, the application monitoring vendor)

Sentry's official agent skill suite encodes the review and release hygiene its own engineers use: security review against OWASP-class issues, code simplification, bug finding, PR writing and iteration, GitHub Actions security review, and internal ops skills (agents-md, claude-settings-audit, sred work summaries). Queued in prior sweeps at a 20.7K API-sum estimate; the publisher page shows 85.3K — a 4x jump, which is why it leads this batch.

---

## Installation

```bash
npx skills add getsentry/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **GitHub CLI (`gh`)** | For `gha-security-review`, `gh-review-requests`, `iterate-pr`, `pr-link-issue` |
| **Django project** | For `django-perf-review` and `django-access-review` only |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| security-review | 13.8K | Full security review of code changes |
| code-simplifier | 7.4K | Simplify code without behavior changes |
| find-bugs | 5.0K | Hunt defects in changed code |
| agents-md | 4.8K | Maintain AGENTS.md guidance files |
| code-review | 4.4K | Systematic code review workflow |
| commit | 4.0K | Conventional commit messages |
| gha-security-review | 3.8K | Audit GitHub Actions workflows |
| iterate-pr | 3.8K | Iterate on PR feedback |
| claude-settings-audit | 3.8K | Audit agent settings files |
| pr-writer | 3.8K | Draft PR descriptions |
| create-branch / gh-review-requests | 3.6K each | Branching and review-request management |
| skill-scanner | 2.6K | Scan installed skills |
| blog-writing-guide | 2.3K | Sentry-style blog drafts |
| presentation-creator | 2.0K | Build slide decks |
| django-perf-review / django-access-review | 1.7K / 1.5K | Django performance and access control review |
| skill-writer / skill-creator | 1.7K / 426 | Author new skills |
| brand-guidelines | 1.6K | Sentry brand voice |
| doc-coauthoring | 1.5K | Collaborative documentation |
| sred-work-summary / sred-project-organizer | 1.4K each | SRE duty summaries and project tracking |
| prompt-optimizer | 1.3K | Optimize agent prompts |
| replay-ux-research | 816 | UX research via session replay |
| create-pr / pr-link-issue / document-api-endpoint | 633 / 586 / 495 | PR and API documentation helpers |
| triage-frontend-issues | 587 | Frontend issue triage |
| typing-exclusion-worker / warden-lint-judge | 910 / 37 | Lint and typing support |

## Quick Start

1. Install: `npx skills add getsentry/skills`
2. Start with `security-review` or `code-review` before merging any PR
3. Ask: "run a security review on my changes and draft the PR description"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **PR security gate** | security-review + gha-security-review as an agent-side review layer for our GitHub work |
| **Repo hygiene** | code-simplifier and find-bugs for maintenance passes on internal tooling |
| **PR automation** | pr-writer, iterate-pr, and gh-review-requests replace manual PR boilerplate |
| **Sentry integration pairing** | Natural fit when instrumenting projects with Sentry error monitoring |
| **Reference skills** | skill-writer and skill-creator as templates for our own skill packaging |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- Django-specific skills require a Django project to be useful
- `warden-lint-judge` (37 installs) is effectively brand-new — treat as untested

```bash
npx skills add getsentry/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
