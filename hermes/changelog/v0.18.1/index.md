---
title: Hermes Agent v0.18.1 — Infrastructure Patch
description: Stable tagged release rolling up ~660 PRs merged since v0.18.0. Bug fixes, hardening, and in-progress feature work for Docker images, hosted deployments, and PyPI installs. July 7, 2026.
---

# Hermes Agent v0.18.1 (v2026.7.7)

**Release Date:** July 7, 2026
**Since v0.18.0:** ~660 PRs · ~990 files changed · +89,500 / −10,400 lines

> **Infrastructure-driven patch tag.** This release rolls up the ~660 PRs merged since v0.18.0 into a stable tagged release for downstream consumers — Docker images, hosted deployments, and PyPI installs. Full curated release notes for this window will ship with **v0.19.0**.

---

## What's in this patch

This is a non-curated roll-up of all work on main since v0.18.0 shipped six days earlier. Highlights of what was in-flight:

- **Installer/updater self-healing** on Windows
- **Dashboard and gateway fixes**
- **WhatsApp dashboard pairing**
- **MCP and provider fixes**
- **Stability hardening** across the platform

~667 commits landed across roughly 990 files. Nothing in this window is skipped — it will all be documented in the next minor release.

## Updating

```bash
hermes update        # existing installs
pip install -U hermes-agent
```

**Full Changelog**: [v2026.7.1...v2026.7.7](https://github.com/NousResearch/hermes-agent/compare/v2026.7.1...v2026.7.7)

---

*← [v0.18.0 — The Judgment Release](/hermes/changelog/v0.18.0/) | [v0.18.2 — WhatsApp Fix](/hermes/changelog/v0.18.2/) →*

*↑ [Changelog Home](/hermes/changelog/)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
