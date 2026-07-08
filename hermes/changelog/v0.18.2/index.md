---
title: Hermes Agent v0.18.2 — WhatsApp Baileys Fix
description: Same-day patch on v0.18.1. Unpins the WhatsApp Baileys bridge dependency from a git commit to the published npm 7.0.0-rc13 release, fixing tagged-release Docker builds. July 7, 2026.
---

# Hermes Agent v0.18.2 (v2026.7.7.2)

**Release Date:** July 7, 2026

> **Same-day patch on top of v0.18.1.** Picks up the WhatsApp Baileys dependency fix needed for tagged-release Docker builds.

---

## What's in this patch

- **fix(whatsapp): unpin Baileys from git commit, use published 7.0.0-rc13** ([#60643](https://github.com/NousResearch/hermes-agent/pull/60643)) — the WhatsApp bridge dependency now installs from the published npm release instead of a pinned git commit, making installs and Docker image builds reliable.

Full curated release notes for the entire post-v0.18.0 window ship with **v0.19.0**.

## Updating

```bash
hermes update        # existing installs
pip install -U hermes-agent
```

**Full Changelog**: [v2026.7.7...v2026.7.7.2](https://github.com/NousResearch/hermes-agent/compare/v2026.7.7...v2026.7.7.2)

---

*← [v0.18.1 — Infrastructure Patch](/hermes/changelog/v0.18.1/) | [Changelog Home](/hermes/changelog/) →*

*↑ [Changelog Home](/hermes/changelog/)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
