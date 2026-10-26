---
title: Hermes Agent v0.20.4 Patch Release
description: Hermes Agent v0.20.4 patch release - release notes, highlights, and security fixes.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.20.4/"
robots: "index,follow"
last_updated: "2026-10-19"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.20.4

**Release Date:** August 18, 2026

> Patch release. This tag rolls up the ~74 PRs merged since v0.20.3 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

---

## About this release

Since v0.20.3 (v2026.8.16.2, tagged August 17), this window landed **~146 commits** across **~265 files** (+21,697 / −2,217)  -  **~74 merged PRs** including the desktop glass/translucency surface work (matte glass, frost picker, macOS pre-select), the tabbed SESSIONS|BOTS sidebar with per-bot hide/unhide, Bot Mode group-chat fixes (long-running member turns, Markdown rendering, cross-machine routing), NVIDIA SkillEvaluator Tier 1 advisory scanning on skill installs (license + security checks), cron media-send hardening (configurable timeout, manual-run attachments, missed-fire surfacing), SessionDB event-loop-thread and contention fixes, `hermes update` parked-branch honesty, and kanban native OS notifications.

**Full curated release notes for this window will ship with v0.21.0**, which will document everything from v0.20.0 onward  -  highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

## Updating

- `hermes update` from an existing install
- Fresh install: `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

**Full Changelog**: https://github.com/NousResearch/hermes-agent/compare/v2026.8.16.2...v2026.8.18

## Frequently Asked Questions

### What changed in Hermes Agent v0.20.4?

Patch release. This tag rolls up the ~74 PRs merged since v0.20.3 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

### When was Hermes Agent v0.20.4 released?

August 18, 2026


---

*← [v0.20.3 - Patch Release](/hermes/changelog/v0.20.3) | [v0.20.5 - Patch Release](/hermes/changelog/v0.20.5) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
