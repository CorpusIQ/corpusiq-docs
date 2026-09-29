---
title: Hermes Agent Official Skills - Bundled Batch Setup Guide
description: "9 official bundled skills from nousresearch/hermes-agent (432 combined installs, first seen Aug 7-13 2026): competitor-news-monitor, document-to-action-items, github-issue-to-pr, blocked-page-recovery, email-inbox-triage, weekly-review-planning, meeting-action-items, product-price-monitor, sdlc-review - install paths, capabilities, and CorpusIQ use cases."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-agent-official-skills-batch-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "nousresearch", "productivity", "research", "bundled"]
---

# Hermes Agent Official Skills - Bundled Batch (September 2026)

**Source:** [skills.sh/nousresearch/hermes-agent](https://www.skills.sh/nousresearch/hermes-agent)
**GitHub:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Category:** Productivity · Research · Email · GitHub · Web · DevOps
**First Seen:** Aug 7-13, 2026 (skills.sh, per skill)
**Quality Tier:** 🟢 Production - official Nous Research skills, MIT license, bundled with Hermes Agent

Nine official skills published to the nousresearch/hermes-agent repo in early August 2026 and bundled with Hermes Agent itself. Discovered in the Sep 1 PM sweep after the flagship-repo API query had timed out on several prior runs. Most are authored by Ben Barclay for Hermes Agent; `sdlc-review` is by Jakub Wolniewicz with Hermes Agent. Together they cover the operator loop end to end: watch competitors, triage the inbox, extract obligations from documents, turn meetings into tickets, run weekly resets, monitor prices, recover blocked pages, carry issues to verified PRs, and verify Kanban handoffs.

---

## Installation

These skills ship **bundled with Hermes Agent** - no install required; they appear in the native skills list. To reinstall or pin a specific version from the source repo:

```bash
npx skills add nousresearch/hermes-agent --skill competitor-news-monitor
npx skills add nousresearch/hermes-agent --skill document-to-action-items
npx skills add nousresearch/hermes-agent --skill github-issue-to-pr
npx skills add nousresearch/hermes-agent --skill blocked-page-recovery
npx skills add nousresearch/hermes-agent --skill email-inbox-triage
npx skills add nousresearch/hermes-agent --skill weekly-review-planning
npx skills add nousresearch/hermes-agent --skill meeting-action-items
npx skills add nousresearch/hermes-agent --skill product-price-monitor
npx skills add nousresearch/hermes-agent --skill sdlc-review
```

Repo paths (verified via the GitHub trees API, Sep 1, 2026): `skills/research/competitor-news-monitor`, `skills/productivity/document-to-action-items`, `skills/productivity/weekly-review-planning`, `skills/productivity/meeting-action-items`, `skills/productivity/product-price-monitor`, `skills/web/blocked-page-recovery`, `skills/email/email-inbox-triage`, `skills/devops/sdlc-review`, and `skills/software-development/github/github-issue-to-pr` (bundled GitHub category).

## Core Skills

| Skill | Installs | First Seen | Use For |
|---|---|---|---|
| competitor-news-monitor | 55 | Aug 10, 2026 | Declared-company watches: funding, pricing, product launches, executive moves, incidents - with materiality thresholds and cited digests |
| document-to-action-items | 50 | Aug 7, 2026 | Contracts, reports, and scanned forms → cited obligations, deadlines, owners, and risks |
| github-issue-to-pr | 50 | Aug 8, 2026 | Issue → premise-validated, duplicate-swept, class-level-fixed PR with honest CI state |
| blocked-page-recovery | 49 | Aug 13, 2026 | Recovery ladder for failed fetches: Wayback → archive.today → Jina Reader → API-first pivot → real browser |
| email-inbox-triage | 48 | Aug 8, 2026 | Bounded inbox queue: thread-aware prioritization, disposition classes, safe draft-only replies |
| weekly-review-planning | 48 | Aug 10, 2026 | Weekly reset across calendar/tasks/notes: commitments vs slippage, next-week plan |
| meeting-action-items | 44 | Aug 10, 2026 | Notes/transcripts → cited decisions, owners, tickets, and board reconciliation |
| product-price-monitor | 44 | Aug 10, 2026 | Exact-item price/availability watches with variant, tax, fee, and currency normalization |
| sdlc-review | 44 | Aug 11, 2026 | Kanban review-lane verification: approve, request changes, or escalate - with evidence, not takeover |

## Roster Additions (Sep 29, 2026 sweep)

Eight additional nousresearch/hermes-agent listings surfaced in the Sep 29 sweep:

| Skill | Installs | Use For |
|---|---|---|
| hermes-agent | 870 | Hermes Agent core framework knowledge |
| design-md | 478 | DESIGN.md guidance for agent-driven projects |
| hermes-agent-skill-authoring | 405 | Authoring SKILL.md files for Hermes Agent |
| github-pr-workflow | 335 | GitHub pull request workflows |
| github-code-review | 330 | GitHub code review workflows |
| github-repo-management | 320 | GitHub repository management |
| github-issues | 310 | GitHub issues automation |
| github-auth | 309 | GitHub authentication setup |

## Prerequisites

| Requirement | Details |
|---|---|
| Hermes Agent | All nine are bundled; the repo versions track the same SKILL.md sources |
| Automation blueprints | `competitor-news-monitor` scaffolds a `competitor-watch` cron tick; `weekly-review-planning` scaffolds a `weekly-review` tick; `product-price-monitor` scaffolds a `price-watch` tick |
| Connector skills | `email-inbox-triage` pairs with `himalaya` or `google-workspace`; `document-to-action-items` pairs with `pdf`/`docx`; `meeting-action-items` pairs with `teams-meeting-pipeline`; `sdlc-review` requires the `kanban` toolset |
| Optional keys | `blocked-page-recovery` only uses Jina Reader when `JINA_API_KEY` is set - all other routes are keyless |

## CorpusIQ Use Cases

- **Competitor intelligence** - `competitor-news-monitor` replaces ad-hoc competitor checks in the tech-research-sweeps workstream with a declared watchlist, source hierarchy (newsroom → pricing → filings), and materiality thresholds. The `competitor-watch` blueprint makes it a cron tick.
- **Inbox operations** - `email-inbox-triage` matches the dual-inbox discipline for media@ and info@: disposition classes, thread-complete reads, and a default read+draft (never send/delete) mutation boundary that mirrors the existing email operating rules.
- **Contract and deal follow-through** - `document-to-action-items` turns partnership, affiliate, and investor documents into cited obligations with deadlines and owners, feeding the lead pipeline and outreach sequences.
- **Docs repo and ecosystem PR hygiene** - `github-issue-to-pr` encodes the issue→verified-PR discipline (premise validation, duplicate sweeps, honest CI state) used in corpusiq-docs maintenance.
- **Research resilience** - `blocked-page-recovery` formalizes the paywall/WAF recovery ladder already practiced ad hoc; its bundled `scripts/recover_page.py` runs the ladder in one shot with provenance.
- **Competitive pricing watches** - `product-price-monitor` automates competitor SaaS pricing-page watches with all-in price normalization (variants, taxes, fees, currencies) - a surface not previously covered.
- **Operator governance** - `meeting-action-items` (decisions → owners → tickets), `weekly-review-planning` (weekly reset cadence), and `sdlc-review` (independent Kanban verification) complete the operator loop for multi-agent workstreams.

## Limitations / Verification

- Verified Sep 1, 2026: repo tree paths via `api.github.com/repos/nousresearch/hermes-agent/git/trees/main?recursive=1` (12,201 paths), SKILL.md frontmatter + bodies via raw.githubusercontent.com, and First Seen dates from each skills.sh skill page.
- `blocked-page-recovery` is the only one with an optional key (JINA_API_KEY); everything else runs keyless.
- `sdlc-review` targets the Kanban toolset (`requires_toolsets: [kanban]`) - it is a review-lane verifier, not a general code reviewer.
- Author mix is honest in each SKILL.md: most skills are Ben Barclay + Hermes Agent; `sdlc-review` is Jakub Wolniewicz + Hermes Agent. No security-audit blocks observed on the skills.sh pages.

## Related

- [Native MCP - MCP Client Setup](/docs/hermes/skills/catalog/native-mcp-setup) - same official repo, MCP transport layer
- [Writing Plans + Subagent-Driven Development Setup](/docs/hermes/skills/catalog/writing-plans-subagent-development-setup) - same official repo, planning pair
- [Skills Marketplace - September 1, 2026 (PM) sweep](/docs/hermes/skills/marketplace/new-sep1-2026) - discovery page for this batch
- [Skills Operations - Email, Cron, and Video Ops Category](/docs/hermes/skills/operations) - connector-side skills that pair with inbox triage
