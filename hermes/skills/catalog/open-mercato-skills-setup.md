---
title: "Open Mercato Skills - Enterprise ERP Engineering Setup"
description: "Setup guide for open-mercato/skills - 79.0K combined installs. 63 enterprise ERP engineering skills: PR loops, upgrades, modules, and conventions."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/open-mercato-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "erp engineering", "pr automation", "code review"]
---

# Open Mercato Skills - Setup Guide

**Source:** [open-mercato/skills](https://www.skills.sh/open-mercato/skills) via skills.sh - 79.0K combined installs across 63 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [open-mercato/skills](https://github.com/open-mercato/skills) (231 stars, MIT; pushed Oct 5, 2026; skills live under skills/)
**Category:** Enterprise ERP / Ecommerce Engineering
**Quality Tier:** 🟡 Beta - company-backed (Open Mercato), MIT, active Oct 2026; Snyk Warn on sampled skills - see Security

Open Mercato Skills extracts the PR pipeline behind the Open Mercato ERP: inside that project the workflow produced ~800k lines of code with zero hand-written lines, 1700+ merged PRs, 4000 unit tests, 730 integration tests, and weekly releases with 100+ contributors. The repo ships 41 agent skills that run the full loop - plan, implement, review, QA gate, merge - stripped of everything product-specific so any team with a GitHub repo can run it with any coding agent.

Every skill reads one committed config file, .ai/agentic.config.json, written once per repo by om-setup-agent-pipeline, which inspects the default branch, validation scripts, and labels, then generates SDLC.md. The naming convention is the contract: the om-auto-* prefix means autonomous and non-interactive (safe to run on a schedule or in CI), while every skill without it is interactive and hands control back.

---

## Installation

```bash
# Install all of the skills (any of 22+ coding agents, via skills.sh)
npx skills add open-mercato/skills --skill '*'

# Update later, from the project directory (-g for global installs)
npx skills update -p
```

Then, once per repository, run the configurator inside your agent:

```
/om-setup-agent-pipeline
```

It inspects your repo (default branch, validation scripts, GitHub labels), asks a few questions, writes .ai/agentic.config.json, and generates SDLC.md - the ticket-flow doc every other skill reads. After updating skills, `/om-apply-upgrade-notes` applies UPGRADE_NOTES.md migrations while preserving local edits. Drop `--skill '*'` to cherry-pick interactively.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| om-apply-upgrade-notes | 2,773 | Post-upgrade migrator: applies UPGRADE_NOTES.md while preserving local edits |
| om-auto-continue-pr | 2,763 | Resumes an in-progress PR from its first unchecked step to completion |
| om-auto-create-pr | 2,748 | Task brief end-to-end: plan, worktree, commits, validation gate, labeled PR |
| om-auto-continue-pr-loop | 2,738 | Resumes loop runs from HANDOFF.md with per-step commits and checkpoints |
| om-auto-create-pr-loop | 2,730 | Long spec implementations: run folder, per-step commits, checkpoint verification |
| om-auto-fix-issue | 2,707 | The issue-to-PR entry point: classifies bug vs feature, then routes |
| om-auto-review-pr | 2,603 | Reviews a PR in an isolated worktree; autofix loop until merge-ready |
| om-approve-merge-pr | 2,541 | Approves and squash-merges a PR by number, with the QA-gate guard |
| om-auto-fix-pr | 2,461 | Drives one PR to merge-ready: review autofix, CI stabilization, UI QA |
| om-auto-implement-spec | 2,377 | Implements an existing spec, then review loop and UI screenshots on the PR |
| om-auto-manage-issues | 2,365 | Issue hygiene: labels, clarification comments, spec-coverage checks |
| om-auto-qa-pr | 2,325 | QAs a PR's UI in a real browser: screenshots and a pass/fail report, no merge |
| om-auto-update-changelog | 2,216 | Drafts a CHANGELOG entry per merged PR and ships it as a docs PR |
| om-code-review | 2,123 | The review checklist behind om-auto-review-pr: correctness, security, contracts |
| om-setup-agent-pipeline | 2,059 | One-per-repo configurator: config, SDLC.md, cross-skill coverage check |
| om-integration-tests | 2,036 | Integration/E2E tests against the running app: real locators, no hardcoded IDs |
| om-fix | 2,031 | Implements the minimal fix with regression tests; runs the validation gate |
| om-auto-write-spec | 2,015 | Turns a brief or feature issue into a finished spec PR with mockups |
| om-open-pr | 2,011 | Shared PR opener: commit, push, unified body, SDLC labels, chain markers |
| om-prepare-issue | 2,004 | Files one well-formed issue: dedupe, linked spec, SDLC labels on creation |

The remaining 43 indexed listings range from 1 to 1,969 installs.

## Why This Matters for Hermes Agents

This collection is a battle-tested PR pipeline an agent can drive end to end: hand it a brief, a spec, or an issue number and it plans, implements in an isolated worktree, runs your validation gate, self-reviews, QAs the UI in a real browser when needed, and finishes with a ready, fully labeled PR. The discipline is built in, which matters when agents work unattended - claim locks so concurrent agents back off instead of colliding, chain markers so skills hand off without duplicating work, and a QA gate that refuses to merge a needs-qa PR without qa-approved even when checks are green. It is stack-agnostic: the base branch, validation commands, and label taxonomy come from one committed config file, so the same pipeline runs on a Rust, Go, or TypeScript repo. The skills are designed to be extended rather than forked - repo-local overrides at .ai/skills/<skill-name>/SKILL.md take precedence, and custom tracker or browser providers plug in through committed descriptor files. One caveat to plan for: a few skills drive a real browser, and the README notes skills.sh validation may flag those as Medium or High risk - read them before you run them.

## Usage

| You say | What happens |
|---|---|
| "/om-setup-agent-pipeline" | Configures the repo: writes the config, generates SDLC.md, verifies cross-skill coverage. |
| "/om-auto-create-pr \"add rate limiting to the login endpoint\"" | Plans, implements phase by phase in a worktree, runs validation, self-reviews, opens a labeled PR. |
| "/om-auto-fix-issue 123" | Classifies the issue, then routes: bug to the autofix chain, feature to spec-then-implement. |
| "/om-auto-qa-pr 123" | Boots the app, drives the browser provider, and posts screenshots with a pass/fail report. |
| "/om-approve-merge-pr 123" | Approves and squash-merges; refused when needs-qa lacks qa-approved or a blocking label is set. |
| "/om-auto-update-changelog" | Drafts a CHANGELOG entry for every PR since the last release and ships it as a docs PR. |
| "/om-discover --mode client \"Benefits portal for SMB clients\"" | Builds a product-brief.md from real material, with evidence-tagged claims and owned decisions. |

## Verification

Confirm the skills are installed and the repo config exists, then fetch a skill's full source before running it:

```bash
# List installed skills
npx skills list | grep om-

# Confirm the repo config after the setup step
cat .ai/agentic.config.json

# Review a skill's full source before install
curl -sL https://raw.githubusercontent.com/open-mercato/skills/main/skills/om-apply-upgrade-notes/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| om-apply-upgrade-notes | Pass | Pass | Warn |
| om-auto-continue-pr | Pass | Pass | Warn |
| om-auto-create-pr | Pass | Pass | Warn |

## Limitations

- Snyk Warn on all three sampled skills: treat the pipeline as privileged automation and re-check the security pages on skills.sh before production use.
- Three skills (om-prepare-test-env, om-integration-tests, om-auto-qa-pr) drive a real browser; the README notes skills.sh validation may flag them Medium or High risk - read them before running.
- The pipeline expects a configured repo: without .ai/agentic.config.json (written by om-setup-agent-pipeline), skills run setup first or lack the context they need.
- The README frames the collection as 41 agent skills while skills.sh indexes 63 listings; treat the repo catalog as the canonical skill set.
- New publisher repo first seen Oct 9, 2026: external validation of the collection is still limited even though the workflow shipped a real product.
- Updates flow through npx skills update plus /om-apply-upgrade-notes; skip the upgrade skill and UPGRADE_NOTES.md migrations are not applied.

- Snapshot data, verified Oct 10, 2026: 79,035 combined installs across 63 indexed listings; 231 GitHub stars; MIT; last pushed Oct 5, 2026. Counts drift over time.

## Related

- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup) - ecommerce platform engineering adjacent to the ERP stack
- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup) - agent engineering counterparts for the pipeline's LLM layer
- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup) - monitoring for the CI and QA evidence the pipeline produces
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /om-setup-agent-pipeline once per repo before anything else; every skill reads the config it writes.
- Prefer the autonomous entry points: /om-auto-create-pr for a brief, /om-auto-fix-issue for an issue number.
- Extend without forking: drop a repo-local override at .ai/skills/<skill-name>/SKILL.md; local rules win but can never relax safety rules.
- After upgrading, run /om-apply-upgrade-notes so UPGRADE_NOTES.md migrations are applied without clobbering your local edits.
- Keep --skill '*' for the first install so cross-skill references and chain markers resolve; the pipeline composes.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
