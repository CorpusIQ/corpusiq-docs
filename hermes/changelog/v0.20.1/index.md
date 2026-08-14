---
title: Hermes Agent v0.20.1 Patch Release
description: Hermes Agent v0.20.1 (v2026.8.13) — Patch release rolling up 1,444 commits and ~656 merged PRs since v0.20.0. Stabilization across the desktop app, gateway platforms, installers, tool system, and provider catalogs. August 13, 2026.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.20.1/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.20.1 (v2026.8.13)

**Release Date:** August 13, 2026
**Since v0.20.0:** 1,444 commits · ~656 merged PRs · 2,172 files changed (+233,872 / −75,244) · ~481 issues closed · 60+ contributors

> Patch release. This tag rolls up the ~656 PRs merged since v0.20.0 into a stable tagged release for downstream consumers (Docker images, hosted deployments, and anyone installing from the latest tag).

---

## About This Release

Since v2026.8.3 (v0.20.0, August 3): **1,444 commits · ~656 merged PRs · 2,172 files changed** on `main`. This is a broad stabilization-and-fixes rollup spanning the desktop app, gateway platforms, installers, tool system, and provider catalogs:

- **Desktop App:** Stability patches and refinements building on the v0.20.0 platform work (artifacts, plugin SDK, multi-window)
- **Gateway Platforms:** Fixes across gateway and messaging platform integrations for reliable delivery
- **Installers:** Installer and updater hardening for downstream consumers (Docker images, hosted deployments)
- **Tool System:** Tool-level reliability fixes, building on the v0.20.0 tool self-recovery work
- **Provider Catalogs:** Model/provider catalog updates and fixes
- **Issue Cleanup:** ~481 issues closed during the window

**Full curated release notes for this window will ship with v0.21.0**, which will document everything from v0.20.0 onward — highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.8.3...v2026.8.13](https://github.com/NousResearch/hermes-agent/compare/v2026.8.3...v2026.8.13)

---

*← [v0.20.0 — The Herald Release](/hermes/changelog/v0.20.0/) | [Changelog Home](/hermes/changelog/) →*

*↑ [Changelog Home](/hermes/changelog/)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
