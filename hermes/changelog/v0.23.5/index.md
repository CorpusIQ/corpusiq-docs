---
title: Hermes Agent v0.23.5 Patch Release
description: Hermes Agent v0.23.5 patch release - release notes, highlights, and security fixes.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.23.5/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.23.5

**Release Date:** November 27, 2026

> Patch release. This tag rolls up the ~338 PRs merged since v0.23.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.


## About this release

Measured at commit `a428f5344f77`, the window since v0.23.4 contains **1,262 non-merge commits** across **1,146 changed files** (+57,989 / −5,346), **338 merged PRs** and **92 closed issues**.

Also in the window, undocumented here on purpose: the CLI and TUI support the OSC 7577 program resume protocol, idle gateway chats compact in the background on every route, `read_file` tails with a negative offset and lists directories, `search_files` says when a content search is the whole answer, a bounded default-plugins preflight before the local gateway starts (Desktop, Docker and CLI), plugin OAuth entries that can pin their redirect URI, the Solstice provider moved to the stateless Interactions API, new plugin API surfaces (turn origin, how a session was created, cron scheduling, gateway silence helpers), the dashboard's "your dashboard is moving" notice, raw arrow keys working in the sessions and plugins pickers, and a long series of fixes that keep plugin work bound to the right profile when a profile is renamed, moved or removed.

**Full curated release notes for this window ship with v0.24.0**, which will document everything from v0.23.0 onward - highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

## Updating

- Microsoft Store app: updates through the Store.
- Desktop app installed from the installer (.exe / .dmg): no change in this release; it updates with the next bundled release.
- CLI: `hermes update`, or re-run the installer one-liner.
- Docker / Hermes Cloud: `nousresearch/hermes-agent:stable` (or `:latest`).

**Full Changelog**: [v0.23.4...v0.23.5](https://github.com/NousResearch/hermes-agent/compare/v0.23.4...v0.23.5)

## Frequently Asked Questions

### What changed in Hermes Agent v0.23.5?

Patch release. This tag rolls up the ~338 PRs merged since v0.23.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.

### When was Hermes Agent v0.23.5 released?

November 27, 2026


---

*← [v0.23.4 - Patch Release](/hermes/changelog/v0.23.4) | [Changelog Home](/hermes/changelog) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
