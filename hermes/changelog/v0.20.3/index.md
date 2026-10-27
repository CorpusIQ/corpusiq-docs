---
title: Hermes Agent v0.20.3 Patch Release
description: Hermes Agent v0.20.3 patch release - release notes, highlights, and security fixes.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.20.3/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.20.3

**Release Date:** August 16, 2026

> Patch release. This tag rolls up the ~125 PRs merged since v0.20.2 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

---

## About this release

Since v0.20.2 (v2026.8.16, tagged earlier today), this window landed **~250 commits** across **~461 files** (+42,613 / −1,641)  -  **~125 merged PRs** including the MCP 2.x SDK migration and 2026-07-28 stateless protocol support, the bundled Bot Mode (hermes-bots) plugin with the core teammate protocol, the CommandCode provider plugin, subprocess Python runtime ownership hardening (PYTHONHOME/PYTHONPATH isolation), Cua Driver 0.20 runtime contracts for computer use, kanban worktree/dispatch fixes, cron continuity flags, desktop remote-gateway headers and connection self-healing, cron scheduler self-heal (EMFILE recovery, stale-claim reconciliation, wedged-job re-arm), session handoff data-loss fixes, plus a wave of ports from the ecosystem scout slate (plugin install security scanning, /worktree, /rollback hand-edit preservation, UTF-16 file reads, Gemini 3 tool-call ID preservation, and more).

**Full curated release notes for this window will ship with v0.21.0**, which will document everything from v0.20.0 onward  -  highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

## Updating

- `hermes update` from an existing install
- Fresh install: `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

**Full Changelog**: https://github.com/NousResearch/hermes-agent/compare/v2026.8.16...v2026.8.16.2

## Frequently Asked Questions

### What changed in Hermes Agent v0.20.3?

Patch release. This tag rolls up the ~125 PRs merged since v0.20.2 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

### When was Hermes Agent v0.20.3 released?

August 17, 2026


---

*← [v0.20.2 - Patch Release](/hermes/changelog/v0.20.2) | [v0.20.4 - Patch Release](/hermes/changelog/v0.20.4) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
