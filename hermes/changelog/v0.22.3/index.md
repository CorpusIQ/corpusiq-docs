---
title: Hermes Agent v0.22.3 Patch Release
description: Hermes Agent v0.22.3 patch release - release notes, highlights, and security fixes.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.22.3/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.22.3

**Release Date:** October 21, 2026

> Patch release. This tag rolls up the ~620 PRs merged since v0.22.2 into a stable release for the CLI and installer, the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.23.0.


## About this release

Measured at commit `5b147ab036d`, the window since v0.22.2 contains **2,911 non-merge commits** across **4,206 changed files** (+360,278 / −64,308), about **620 merged PRs** and **326 closed issues**.

Also in the window, undocumented here on purpose: MCP progress notifications streamed as live tool progress, a refreshed classic CLI layout (glyph transcript, status line under the composer, two-line header), OAuth clients that plugins declare and Hermes signs in and refreshes, `hermes plugins update` offering every available plugin update plus an Update button for git-installed plugins in Desktop, steering and editing a queued prompt from Desktop, a guided subagent model and provider picker in Desktop, a live `/loop` countdown row in the CLI and TUI, opt-in Telegram DM topic transfer, a `post_compaction` plugin hook, a capabilities catalog, the Microsoft Store build going live automatically when a release publishes, session auto-prune back to opt-in with a one-time prompt when disk runs low, Nemotron 3.5 Bolt and one-slot DFlash drafts in the local runtime, and dozens of new plugin catalog entries.

**Full curated release notes for this window ship with v0.23.0**, which will document everything from v0.22.0 onward  -  highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

## Updating

- Microsoft Store app: updates through the Store.
- Desktop app installed from the installer (.exe / .dmg): no change in this release; it updates with the next bundled release.
- CLI: `hermes update`, or re-run the installer one-liner.
- Docker / Hermes Cloud: `nousresearch/hermes-agent:stable` (or `:latest`).

**Full Changelog**: [v0.22.2...v0.22.3](https://github.com/NousResearch/hermes-agent/compare/v0.22.2...v0.22.3)

## Frequently Asked Questions

### What changed in Hermes Agent v0.22.3?

Patch release. This tag rolls up the ~620 PRs merged since v0.22.2 into a stable release for the CLI and installer, the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship...

### When was Hermes Agent v0.22.3 released?

October 21, 2026


---

*← [v0.22.2 - Patch Release](/hermes/changelog/v0.22.2) | [v0.22.4 - Patch Release](/hermes/changelog/v0.22.4) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
