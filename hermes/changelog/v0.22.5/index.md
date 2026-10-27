---
title: Hermes Agent v0.22.5 Patch Release
description: Hermes Agent v0.22.5 patch release - release notes, highlights, and security fixes.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.22.5/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.22.5

**Release Date:** October 22, 2026

> Patch release. This tag rolls up the ~81 PRs merged since v0.22.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.23.0.


## About this release

Measured at commit `bf0203a794a`, the window since v0.22.4 contains **231 non-merge commits** across **804 changed files** (+35,212 / −17,885), **81 merged PRs** and **30 closed issues**.

Also in the window, undocumented here on purpose: Nous sign-in reworked (every sign-in is the plain device login, the free-tier guest hands over to your account, the result shows who signed in, connectors offer sign-in instead of opening a guest), `hermes update` holding back a stable release it refuses instead of offering it, Windows `hermes update` no longer stuck on the old launcher after a Python repin, usage-window plan support (plan gauges, limit cards and model-switch recovery for window-based plans), pluggable delegation backends (route subagents by model map or profile, switchable per session), plugin slash commands that can ask you to pick an option, `hermes import-agent`, OpenClaw migration, `hermes mcp serve` and the Singularity backend moving out of core into plugins (setup offers the importer when it finds another agent), Desktop drag-to-pin in the sidebar and one-click plugin installs with tier badges, the Electron 44 upgrade, Pillow 13 and a batch of dependency security bumps, a clear message when a chat's working folder is gone, `hermes update` recovering paused gateways after a damaged `.git`, long Claude DirectSDK answers no longer cut off by the stall timer, Desktop group chats showing which bot is working again, and the experimental webhook-mode MCP events client.

**Full curated release notes for this window ship with v0.23.0**, which will document everything from v0.22.0 onward  -  highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

## Updating

- Microsoft Store app: updates through the Store.
- Desktop app installed from the installer (.exe / .dmg): no change in this release; it updates with the next bundled release.
- CLI: `hermes update`, or re-run the installer one-liner.
- Docker / Hermes Cloud: `nousresearch/hermes-agent:stable` (or `:latest`).

**Full Changelog**: [v0.22.4...v0.22.5](https://github.com/NousResearch/hermes-agent/compare/v0.22.4...v0.22.5)

## Frequently Asked Questions

### What changed in Hermes Agent v0.22.5?

Patch release. This tag rolls up the ~81 PRs merged since v0.22.4 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for...

### When was Hermes Agent v0.22.5 released?

October 23, 2026


---

*← [v0.22.4 - Patch Release](/hermes/changelog/v0.22.4) | [Changelog Home](/hermes/changelog) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
