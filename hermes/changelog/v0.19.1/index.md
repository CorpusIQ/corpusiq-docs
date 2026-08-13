---
title: Hermes Agent v0.19.1 Patch Release
description: Hermes Agent v0.19.1 (v2026.7.30) — Patch release rolling up ~3,087 commits since v0.19.0. Gateway fixes, voice subsystem stabilisation, Telegram media reliability, FLUX3 video pipeline, and Buzz/Nostr channel support. July 30, 2026.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.19.1/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.19.1 (v2026.7.30)

**Release Date:** July 30, 2026
**Since v0.19.0:** ~3,087 commits · ~300 files changed · 46 contributors

> Patch release. This tag rolls up the ~1,000+ PRs merged since v0.19.0 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

---

## About This Release

Since v2026.7.20 (v0.19.0, July 20): **~3,087 commits · ~300 files changed** on `main`. This window is dominated by bug-fix and salvage waves across the gateway, voice subsystem, desktop app, and installer, plus continued platform work:

- **Gateway & Core:** Stability fixes, crash recovery hardening, durable delivery ledger improvements
- **Voice Subsystem:** Regression fixes for voice-mode interactions, audio pipeline stabilisation
- **Desktop App:** Performance patches and UI refinements building on the Quicksilver speed overhaul
- **Telegram:** Media delivery reliability improvements
- **FLUX3:** Video generation and delivery pipeline refinements
- **Buzz/Nostr:** New social channel support for decentralised networks
- **Installer:** Self-healing and fresh-install reliability patches

**Full curated release notes for this window will ship with v0.20.0**, which will document everything from v0.19.0 onward — highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.7.20...v2026.7.30](https://github.com/NousResearch/hermes-agent/compare/v2026.7.20...v2026.7.30)

---

*← [v0.19.0 — The Quicksilver Release](/hermes/changelog/v0.19.0/) | [Changelog Home](/hermes/changelog/) →*

*↑ [Changelog Home](/hermes/changelog/)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*

