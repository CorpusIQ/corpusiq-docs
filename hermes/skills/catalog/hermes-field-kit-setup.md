---
title: "Hermes Field Kit — Field-Tested Hermes Operations Skill Suite Setup"
description: "asimons81/hermes-field-kit — 16 skills (13 stable + 3 experimental), 122 GitHub stars: a curated, versioned, field-tested operations kit for Hermes Agent covering stack health, gateway diagnosis, profile audits, token/cost auditing, skill audits, environment migration, and evidence-disciplined reporting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-field-kit-setup/"
robots: "index,follow"
last_updated: "2026-08-19"
tags: ["hermes skill", "agent skill", "skill setup", "hermes operations", "stack doctor", "token audit", "gateway diagnosis", "skill audit", "x automation"]
---

# Hermes Field Kit — Setup Guide

**Source:** [asimons81/hermes-field-kit](https://skills.sh/asimons81/hermes-field-kit)
**GitHub:** [asimons81/hermes-field-kit](https://github.com/asimons81/hermes-field-kit)
**Skills:** 16 skills (13 stable + 3 experimental) · v1.0.1
**Category:** Hermes Operations
**First Seen:** August 19, 2026 evening sweep
**Quality Tier:** 🟡 Beta — 122 GitHub stars, Apache-2.0, SemVer-tagged releases, per-skill versioning, a dependency-free repository validator, and a published skill specification

Hermes Field Kit is the most disciplined Hermes-native operations suite on the marketplace. It is intentionally not a bulk skill dump: every stable skill must solve a real task, have been used in an actual workflow, and be reproducible by another person from the repository alone. The catalog organizes sixteen skills around an operational loop of inspect → diagnose → recover → migrate → verify, with three experimental skills marked while they accumulate field evidence. Eight skills are indexed on skills.sh (2-3 installs each); the rest are tap-discoverable from the repository.

---

## Installation

Install any published skill by its repository-qualified identifier:

```bash
hermes skills inspect asimons81/hermes-field-kit/hermes-stack-doctor
hermes skills install asimons81/hermes-field-kit/hermes-stack-doctor --yes
```

Replace `hermes-stack-doctor` with any skill from the published list. Start a new Hermes session after installation because skill discovery may be cached for the lifetime of an existing session.

Manual installation (clone and copy or symlink into the active profile's skills directory):

```bash
git clone https://github.com/asimons81/hermes-field-kit.git
cp -r hermes-field-kit/skills/hermes-stack-doctor ~/.hermes/profiles/<profile>/skills/
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent v0.19.0+** | Qualified identifier resolution through the skills.sh registry verified in v0.19.0 |
| **Linux / macOS / Windows** | Operations skills are cross-platform; `x-analytics-import` and `x-post-writer` are platform-agnostic |
| **Read access to the target install** | All skills are read-only by design — no automatic repair, no credential writes |

## What It Provides

| Skill | Status | Purpose |
|---|---|---|
| hermes-stack-doctor | stable | Top-level read-only health audit across installation, updates, gateways, cron, profiles, and persistence; reports GREEN / YELLOW / RED without repairs |
| hermes-gateway-doctor | stable | Diagnose messaging gateway failures from process state, adapters, credential posture, logs, delivery evidence, and service persistence |
| hermes-profile-audit | stable | Compare a profile's declared responsibilities with its actual tools, skills, persistence, access, and observed behavior |
| hermes-token-audit | stable | Audit token usage and cost with live schema discovery, aggregate-first privacy, and separation of estimates from provider billing |
| hermes-skill-audit | stable | Audit global and profile-local skills for dependencies, frontmatter, usage integrity, cron references, duplicates, and upstream drift |
| hermes-skill-consolidate | experimental | Safely consolidate or restructure overlapping skills with read-only planning, rollback snapshots, and staged writes |
| hermes-environment-migration | stable | Migrate Hermes environments between machines with staged archives, integrity manifests, secret separation, and rollback |
| hermes-update-doctor | stable | Investigate update failures across remote drift, repository divergence, process locks, stale caches, and partial installs |
| oss-tool-trust-audit | stable | Evaluate open-source tools for legitimacy — read source and release machinery, treat popularity as context rather than proof |
| pre-build-feature-audit | stable | Read-only duplicate check across source, history, branches, issues, PRs, and roadmaps before building a feature |
| repo-readiness-audit | stable | Determine whether a Git repository is ready for development, release, handoff, or contribution using independent evidence |
| x-analytics-import | stable | Validate, normalize, import, and compare X Analytics CSV exports through a private-by-default workflow |
| x-post-writer | stable | Draft, rewrite, and repurpose short-form X content with source fidelity, format routing, and claim verification |
| interview-me | stable | Ask one high-value question at a time and stop when more questions would not change the next action |
| what-have-we-done-today | experimental | Scan today's sessions, kanban boards, and cron runs across profile stores into an append-friendly daily markdown recap |
| dont-lie-to-me | experimental | Cross-cutting evidence discipline separating observed facts, sourced claims, inference, unknowns, and contradictions before strong claims |

## Quick Start

1. Inspect before installing: `hermes skills inspect asimons81/hermes-field-kit/hermes-stack-doctor`
2. Install the flagship: `hermes skills install asimons81/hermes-field-kit/hermes-stack-doctor --yes`
3. In a new session, say "run a stack health audit" — hermes-stack-doctor reports a GREEN / YELLOW / RED verdict without modifying anything
4. Add hermes-token-audit when cost attribution or billing discrepancies need investigation

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **System health audits** | hermes-stack-doctor maps directly to our system-auditor cadence — read-only GREEN/YELLOW/RED verdicts across the full stack |
| **Gateway failure diagnosis** | hermes-gateway-doctor covers Telegram/gateway failure modes we hit regularly; evidence-first, no blind repair |
| **Cost and token governance** | hermes-token-audit separates estimates from provider billing — matches our token-optimization discipline and budget tracking |
| **Skill library hygiene** | hermes-skill-audit + hermes-skill-consolidate match our quarterly skill audits and consolidation passes exactly |
| **X channel workflows** | x-post-writer and x-analytics-import cover our primary social channel: drafting with claim verification and private analytics import |
| **Evidence-disciplined reporting** | dont-lie-to-me and oss-tool-trust-audit encode our verify-before-assertion and help-first trust rules as reusable workflows |
| **Environment migration** | hermes-environment-migration's staged export / integrity manifest / rollback pattern matches our Spark-to-worker sync needs |

## Limitations / Verification

- Below the 20K install guide bar — drafted on cluster authority: a cohesive, versioned, Hermes-native suite with 122 GitHub stars and an explicit admission rule (no filler, no thin wrappers)
- Tap-backed search was not claimed as supported in the v0.19.0 validation environment; install by qualified identifier or manual copy
- Experimental skills (what-have-we-done-today, dont-lie-to-me, hermes-skill-consolidate) are explicitly not stable — use supervised
- All operations skills are diagnosis-only by design; they never auto-repair, which is intentional

```bash
hermes skills install asimons81/hermes-field-kit/hermes-stack-doctor --yes   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)
- [AtlasOmnia Hermes Custom Pack Setup](/hermes/skills/catalog/atlasomnia-hermes-custom-pack-setup/)
- [Buzz Skills — Hermes on Nostr Setup](/hermes/skills/catalog/buzz-skills-setup/)

*Powered by CorpusIQ*
