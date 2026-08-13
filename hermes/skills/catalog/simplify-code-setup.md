---
title: Simplify Code — Skill Setup Guide
description: Install and configure simplify-code, the official Hermes Agent skill for parallel code review and cleanup with four focused reviewers — 187 installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/simplify-code-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Simplify Code — Parallel Review & Cleanup Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/simplify-code) (187 installs)
**Category:** Development / Code Quality
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent, git repository with recent changes

Run four focused code reviewers in parallel against your recent changes. Each reviewer hunts for one class of problem — reuse opportunities, quality issues, efficiency waste, and code altitude — without diluting its focus. This is a cleanup pass, not a bug hunt. It finds duplication, flattens needless complexity, cuts dead code, and deepens band-aid fixes.

---

## What It Does

| Reviewer | Focus | Catches |
|----------|-------|---------|
| **Reuse** | DRY violations | Duplicate logic, copy-pasted blocks, missing abstractions |
| **Quality** | Maintainability | Unclear naming, missing error handling, brittle patterns |
| **Efficiency** | Performance waste | Unnecessary allocations, N+1 queries, blocking calls |
| **Altitude** | Architecture | Over-engineering, wrong abstraction level, scope creep |

All four run concurrently — you pay the latency of one review, not four.

---

## How It Works

```
┌──────────────────┐
│  git diff HEAD~3 │
└────────┬─────────┘
         │
    ┌────▼─────┬─────────┬──────────┬──────────┐
    │  Reuse   │ Quality │Efficiency│ Altitude │  ← All run in parallel
    └────┬─────┴────┬────┴────┬─────┴────┬─────┘
         │          │         │          │
         └──────────▼─────────▼──────────┘
                    │
            ┌───────▼───────┐
            │  Aggregated   │
            │  Findings +   │
            │  Fixes Applied│
            └───────────────┘
```

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill simplify-code
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/development/simplify-code ~/.hermes/skills/
```

---

## Basic Usage

After a coding session, trigger the cleanup:

```
> Load simplify-code skill
> Review my last 3 commits with simplify-code
```

Or specify scope:

```
> Simplify the auth module — focus on the /src/auth/ directory
```

Hermes spawns four reviewers concurrently, each searching the codebase for its specific problem class. After all four complete (in parallel), findings are aggregated and fixes applied.

---

## When to Use vs When Not

| ✅ Use After | ❌ Don't Use For |
|-------------|-----------------|
| Feature completion — before PR | Bug hunting (use `requesting-code-review`) |
| Multi-commit sessions | Security audits |
| Before merging to main | Correctness verification |
| Refactoring prep — see what to clean | First-draft code (finish it first) |
| Reducing technical debt sprints | Generated/auto-formatted code |

---

## Tips

- **Run after `requesting-code-review`:** That catches bugs. This catches waste.
- **Scope matters:** Narrow the file/directory scope for focused cleanup; broad for architectural review
- **Review findings are actionable:** Each issue comes with a suggested fix, not just a flag
- **Don't apply blindly:** The altitude reviewer may suggest refactors — evaluate before applying

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Reviewers time out | Codebase too large | Narrow scope to specific directories |
| Too many findings | First run on old codebase | Apply fixes iteratively, re-run |
| Altitude reviewer too aggressive | Large architectural suggestions | Evaluate; this reviewer has the widest lens |

---

## Comparison with `requesting-code-review`

| Aspect | simplify-code | requesting-code-review |
|--------|--------------|----------------------|
| **Purpose** | Cleanup, reduce waste | Bug detection, correctness |
| **Reviewers** | 4 parallel (reuse, quality, efficiency, altitude) | Comprehensive code review |
| **When** | After feature works | Before feature is "done" |
| **Output** | Fixes + suggestions | Bug reports + issues |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
