---
title: Hermes Agent Changelog
description: Version history and release notes for NousResearch Hermes Agent. Track new features, breaking changes, and upgrades.
---

# Hermes Agent Changelog

Track every Hermes Agent release. New versions are auto-detected and documented within 24 hours of publication.

## Releases

| Version | Date | Name | Highlights |
|---------|------|------|------------|
| [v0.16.0](/hermes/changelog/v0.16.0/) | June 5, 2026 | The Surface Release | Desktop app, remote gateway, web admin panel, fuzzy model picker, `/undo`, 简体中文, leaner skills, NVIDIA/skills tap |

---

## How Updates Are Detected

Three crons monitor Hermes Agent releases:
| Cron | Schedule | Action |
|------|----------|--------|
| `hermes-release-monitor` | 02:00, 10:00, 18:00 UTC | Check GitHub releases for new versions |

When a new release is detected, a changelog page is drafted, committed to `CorpusIQ/corpusiq-docs`, and reported via Telegram.

---

*← [Home](/hermes/) | [Architecture](/hermes/architecture/) →*
