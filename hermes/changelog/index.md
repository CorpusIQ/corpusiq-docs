---
title: Hermes Agent Changelog
description: Version history and release notes for NousResearch Hermes Agent. Track new features, breaking changes, and upgrades.
---

# Hermes Agent Changelog

Track every Hermes Agent release. New versions are auto-detected and documented within 24 hours of publication.

## Releases

| Version | Date | Name | Highlights |
|---------|------|------|------------|
| [v0.18.0](/hermes/changelog/v0.18.0/) | July 1, 2026 | The Judgment Release | P0/P1 clean sweep (100% resolved), Mixture-of-Agents as first-class model, verification & completion contracts, `/learn` skill distillation, `/journey` learning timeline, desktop coding Projects, background fan-out, scale-to-zero gateway, Google Vertex AI, security hardening |
| [v0.17.0](/hermes/changelog/v0.17.0/) | June 19, 2026 | The Reach Release | iMessage via Photon, Raft agent network, background subagents, image editing, Automation Blueprints, desktop overhaul, Skills Hub rehaul, WhatsApp, Telegram rich text |
| [v0.16.0](/hermes/changelog/v0.16.0/) | June 5, 2026 | The Surface Release | Desktop app, remote gateway, web admin panel, fuzzy model picker, `/undo`, 简体中文, leaner skills, NVIDIA/skills tap |

---

## How Updates Are Detected

Three crons monitor Hermes Agent releases:
| Cron | Schedule | Action |
|------|----------|--------|
| `hermes-release-monitor` | 02:00, 10:00, 18:00 UTC | Check GitHub releases for new versions |

When a new release is detected, a changelog page is drafted, committed to `CorpusIQ/corpusiq-docs`, and reported via Telegram.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
