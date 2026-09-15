---
title: "New Skills - September 1, 2026 (PM)"
description: "skills.sh tiered sweep: 9 new official nousresearch/hermes-agent bundled skills surfaced by retry after 5 API timeouts - competitor-news-monitor (55), document-to-action-items (50), github-issue-to-pr (50), blocked-page-recovery (49), email-inbox-triage (48), weekly-review-planning (48), meeting-action-items (44), product-price-monitor (44), sdlc-review (44) - 432 combined installs, 1 cluster setup guide."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep1-2026/"
robots: "index,follow"
last_updated: "2026-09-01"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills", "nousresearch"]
sweep_id: "2026-09-01-pm"
new_publishers: 0
new_skills: 9
guides_drafted: 1
---

# New Skills - September 1, 2026 (PM)

Fifteen-query skills.sh API sweep with tiered cross-reference against the full hermes/ tree. First pass: 10 of 15 queries returned (474 unique skills; 63 NEW, 98 PARTIAL, zero ≥100-install NEW flags) while 5 queries hit API read timeouts. The timed-out queries were retried successfully, and the retry surfaced the find of the sweep: **9 official bundled skills from nousresearch/hermes-agent with zero docs-tree hits** - a batch first seen on skills.sh Aug 7-13, 2026 that every sweep since has missed because the flagship-repo query kept timing out or the names never matched a keyword sweep. Every other NEW flag mapped to standing rejections or one new verified rejection.

## New Skills - Official Hermes Agent Bundled Batch

| Skill | Category | Installs | First Seen | What It Does |
|---|---|---|---|---|
| `competitor-news-monitor` | Research | 55 | Aug 10, 2026 | Watch a declared company set for material news; cited digests with primary-source evidence |
| `document-to-action-items` | Productivity | 50 | Aug 7, 2026 | Extract cited obligations, deadlines, and tasks from documents (contracts, reports, scans) |
| `github-issue-to-pr` | GitHub | 50 | Aug 8, 2026 | Carry a GitHub issue to a tested, verified PR with honest CI state |
| `blocked-page-recovery` | Web | 49 | Aug 13, 2026 | Ladder recovery when a fetch fails: 403/429, paywall, WAF, bot wall - Wayback → archive.today → Jina → API pivot → browser |
| `email-inbox-triage` | Email | 48 | Aug 8, 2026 | Turn a mailbox into a bounded queue of decisions; thread-aware prioritization, safe draft replies |
| `weekly-review-planning` | Productivity | 48 | Aug 10, 2026 | Weekly reset: commitments, stalled work, next-week plan from calendar, tasks, and notes |
| `meeting-action-items` | Productivity | 44 | Aug 10, 2026 | Turn meeting notes/transcripts into cited decisions, owners, and tickets |
| `product-price-monitor` | Productivity | 44 | Aug 10, 2026 | Watch product, flight, or listing prices; alert on a normalized all-in price or availability |
| `sdlc-review` | DevOps | 44 | Aug 11, 2026 | Review Kanban handoffs and route verified outcomes; approve, request changes, or escalate |

All nine ship **bundled with Hermes Agent** (verified via the website's bundled-skill docs tree and the repo's recursive tree, 12,201 paths). Total: 432 combined installs across 5 categories.

**Install / reinstall:**

```bash
npx skills add nousresearch/hermes-agent --skill competitor-news-monitor
# or any of: document-to-action-items, github-issue-to-pr, blocked-page-recovery,
# email-inbox-triage, weekly-review-planning, meeting-action-items,
# product-price-monitor, sdlc-review
```

Full details, per-skill use cases, and CorpusIQ mappings: [Hermes Agent Official Skills - Bundled Batch Setup](/docs/hermes/skills/catalog/hermes-agent-official-skills-batch-setup)

## Method Notes

- Standard 15-query sweep. First pass: `nousresearch/hermes-agent`, `aradotso/hermes-skills`, `hermes agent`, `hermes skill`, and `aradotso/devtools-skills` timed out (API read timeouts); the other 10 queries returned 474 unique skills with 63 NEW and 98 PARTIAL flags.
- All 63 first-pass NEW flags sat below 100 installs and mapped to the standing rejection batches (Aug 28 - Sep 1 AM: locaweb/cofounder 62, konglong87/superpm 42, zrr1999/skills 33, sidetoolco/org-charts dead, and ~40 more below-bar personal/Claude-only collections).
- The 5 timed-out queries were retried with `--max-time 25` and all succeeded. The retry batch (192 lines) cross-referenced against the tree flagged 17 items; 9 were the nousresearch PARTIAL batch (repo documented, skill names absent - the Aug 21 converse-of-cluster false-negative class), the rest 1-3-install below-bar items (mah92/hermes-persian-skills, alexai-mcp/hermes-ccc, etc.).
- Each of the 9 skills was verified end-to-end: repo tree path via GitHub trees API, SKILL.md frontmatter + body via raw.githubusercontent.com, and First Seen date via the skills.sh skill page.
- House bar cleared on precedent: the June 17/18 sweeps documented official nousresearch batches at 13-136 installs (native-mcp at 79, pptx-author at 14, duckduckgo-search at 14). Official bundled skills are the product's own feature set - an uncatalogued official skill is a docs gap regardless of install count.

## Evaluated and Queued

| Skill | Source | Installs | Disposition |
|---|---|---|---|
| refero-styles | clementwalter/refero-design | 13 | **Rejected (new)** - README installs via `npx skills add -a claude-code` into `~/.claude/skills/`; 2⭐, last commit Jun 15. Claude Code skill, below the 40-install floor. New standing rejection. |
| 60+ NEW flags (cofounder-tech-stack, pm-tech, tech-preferences, etc.) | locaweb, konglong87, zrr1999, sidetoolco, and ~35 more | 1-62 | Standing rejections re-confirmed from the Aug 28 - Sep 1 AM verified batches (dead sources sidetoolco/org-charts, junhyunny, opened-vault, lproux, musical-basics re-confirmed dead). |
| hermes-agent-maker | alpoxdev/hypercore | 8 | Parked below bar (brand-watch since Sep 1 AM) - Hermes-native SKILL.md that authors SOUL.md/AGENTS.md packages, but 4⭐ and 8 installs |
| b2b-sdr-hermes-skill | ipythoning | 14 | Parked below bar (brand-watch since Sep 1 AM) - explicit Hermes targeting + B2B SDR domain fit, below the calesthio floor |

## Notable Signals for CorpusIQ

- **`competitor-news-monitor`** is a one-to-one fit for the tech-research-sweeps workstream: declared-company watches, materiality thresholds, and source-hierarchy discipline already in use; the skill adds the `competitor-watch` automation blueprint for cron scaffolding.
- **`email-inbox-triage`** formalizes the dual-inbox discipline (media@ + info@) - thread-aware prioritization and safe draft-only replies match the existing email operating rules.
- **`document-to-action-items`** converts partnership/contract documents into cited obligations and deadlines - feeds the lead pipeline and investor outreach follow-through.
- **`github-issue-to-pr`** encodes the issue→verified-PR discipline with honest CI state - direct fit for docs repo maintenance and the Hermes ecosystem PR work.
- **`blocked-page-recovery`** gives research a formalized paywall/WAF ladder (Wayback → archive.today → Jina → API pivot → browser) that matches the existing search-resilience playbook.
- **`product-price-monitor`** enables automated competitive pricing watches on competitor SaaS pages - a research surface not currently covered.
- **`meeting-action-items`, `weekly-review-planning`, `sdlc-review`** round out the operator/governance loop: decisions to tickets, weekly resets, and Kanban review-lane verification.

## Index State After Sweep

- catalog/index.md: +1 entry (cluster setup guide: hermes-agent-official-skills-batch-setup)
- marketplace/index.md: Recent Sweeps entry added. Repo counts unchanged - nousresearch/hermes-agent is already a curated repo; this sweep added 9 of its skills, not a new publisher.
- PROGRESS.md: Skills catalog 411 → 412; Total Markdown files 2,066 → 2,068
