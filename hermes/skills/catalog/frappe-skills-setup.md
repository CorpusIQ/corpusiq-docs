---
title: "Frappe Skills - ERP Development and Review"
description: "frappe/skills: 7.3K combined installs across 11 listings, Frappe and ERPNext app development, code review, security advisories and merged-ready shipping."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/frappe-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "frappe", "erpnext", "code review"]
---

# Frappe Skills - Setup Guide

**Source:** [frappe/skills](https://www.skills.sh/frappe/skills) via skills.sh - 7.3K combined installs across 11 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 168 stars, no LICENSE file in the tree, `main` branch, last pushed 2026-11-13, 12 `SKILL.md` files under `skills/`
**Category:** Frappe Framework and ERPNext application development
**Quality Tier:** 🟡 Yellow - one of the two sampled skills carries a Snyk Warn while the other passes all three auditors, and the repository ships no licence file.

Frappe Framework is the open-source base under ERPNext, and this is the platform team's own skill collection for changing applications built on it. It combines two kinds of skill: framework-specific ones (`frappe-app-dev`, `frappe-code-review`) and general engineering ones (`code-style`, `technical-writing`, `ui-design`), which is a deliberate split the README explains.

The framework skill is narrowly grounded: it covers running and changing a Frappe app with Pilot, benches, a test site for a pull request, tests, and the Frappe behaviours agents get wrong. That last phrase is the honest part. The value here is not teaching an agent Frappe, it is correcting the specific mistakes a general model makes inside a bench.

## Installation

Install every skill in the repository:

```bash
npx skills add frappe/skills
```

A single skill:

```bash
npx skills add frappe/skills --skill frappe-app-dev
```

Or several at once, since skills are matched by the `name` field in each frontmatter and live under `skills/<name>/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| frappe-app-dev | 1,389 | Running and changing Frappe apps with Pilot: benches, a test site per PR, tests and the framework behaviours agents get wrong. |
| code-style | 1,091 | General code style rules applied across the repository's languages. |
| ui-design | 1,038 | General UI and UX design principles for application screens. |
| technical-writing | 721 | Documentation, READMEs, commits, pull requests and release notes in Simplified Technical English. |
| draft-security-advisory | 685 | Writing a publication-ready GitHub Security Advisory: summary, details, proof of concept, impact, CVSS, CWE, versions and credits. |
| resolve-backport-conflicts | 638 | Resolving conflicts while backporting a fix to a release branch. |
| quality-code-review | 554 | A review pass over a change before it is considered finished. |
| frappe-code-review | 481 | A Frappe-specific review checklist: correctness, security, performance, concurrency, readability, API design and testing. |
| deep-app-audit | 415 | Multi-agent audit of a Frappe app for security, correctness and customisation defects, with every candidate verified. |
| ship-it | 284 | Taking finished work to a merge-ready PR: intent, a fresh review pass, live test, docs, lint, PR with evidence, then CI watch. |

The remaining 1 indexed listing is frappe-dev (37 installs).

## Why This Matters for Hermes Agents

The collection is shaped like a delivery pipeline rather than a knowledge base, and that is what makes it worth installing. `frappe-app-dev` gets an agent into a working bench; `frappe-code-review` and `quality-code-review` check the change; `deep-app-audit` verifies the results with independent subagents; `ship-it` carries it to a pull request with evidence; `resolve-backport-conflicts` handles the release path; and `draft-security-advisory` covers the case where the review found a vulnerability.

Several of these are marked user-invoked only, which is a meaningful design choice: an agent will not start a multi-agent audit or open a PR unasked. The guard skill goes further and states that the agent does not push when its review has P0 findings, which is the kind of hard stop most skill collections leave to the host.

Simplified Technical English in `technical-writing` is a small detail with outsized effect: commit messages and release notes come out readable, which is what makes the rest of the pipeline reviewable.

## Usage

| You say | What happens |
|---|---|
| "Fix this bug in our Frappe app" | Uses `frappe-app-dev` for the bench, test-site and framework conventions. |
| "Review this change before we merge" | Runs the Frappe review checklist, then the general quality pass. |
| "Audit this app for security defects" | Runs `deep-app-audit`, which dispatches subagents and verifies each candidate before reporting. |
| "Open a pull request with evidence" | Uses `ship-it` for the intent, review, live test, docs and CI watch sequence. |
| "We found a vulnerability, write the advisory" | Uses `draft-security-advisory` for a GHSA-format write-up with CVSS and CWE. |
| "Backport this fix to the release branch" | Uses `resolve-backport-conflicts` for the conflict path. |

## Verification

Read the framework skill and the shipping skill before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/frappe/skills/main/skills/frappe-app-dev/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/frappe/skills/main/skills/ship-it/SKILL.md
```

Skills sit at `skills/<name>/SKILL.md`. Some listings in the index, including `quality-code-review` and `frappe-dev`, have no matching directory in the current tree, so check the path before assuming a broken clone.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frappe-app-dev | Pass | Pass | Warn |
| code-style | Pass | Pass | Pass |

The framework skill carries a Snyk Warn. The collection also includes skills that push code and open pull requests, so review what an agent is allowed to merge before enabling `ship-it` unattended.

## Limitations

- Snapshot data, verified 2026-11-14: 7,333 combined installs across 11 indexed listings; 168 GitHub stars; no LICENSE file; last pushed 2026-11-13. Counts drift over time.
- No licence file in the tree, so reuse terms are unstated.
- The index and the tree disagree in both directions: `quality-code-review` and `frappe-dev` are listed without a directory, while `fix-issue`, `guard-review` and `review-ui-states` exist in the tree with no install count on skills.sh.
- `guard-review` needs the Guard MCP server, and `deep-app-audit` and `ship-it` are user-invoked only by design.
- Several skills assume ERPNext-adjacent tooling (Pilot benches, a test site per PR) that a plain Frappe install may not have.
- One sampled skill carries a Snyk Warn.

## Related

- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup)
- [WordPress Agent Skills - Official WP Development Setup](/hermes/skills/catalog/wordpress-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the pipeline order: develop, review, audit, ship. Each skill assumes the previous step's output.
- Keep `ship-it` user-invoked. An agent that opens PRs on its own is a policy decision, not a productivity gain.
- Run `deep-app-audit` before a release rather than after: it dispatches fresh subagents and verifies candidates, which catches what a single pass misses.
- Adopt `technical-writing` for commit messages alone; it improves review speed more than any lint rule.
- Check for the Guard MCP server before relying on `guard-review`, since it is a hard dependency.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
