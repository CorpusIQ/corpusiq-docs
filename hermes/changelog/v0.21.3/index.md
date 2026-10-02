---
title: Hermes Agent v0.21.3 Patch Release
description: Hermes Agent v0.21.3 (v2026.9.14) - Patch release for remote Desktop and Cloud users. Fixes refresh-token replay that expired dashboard sessions, and duplicate state.db writer handles.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.21.3/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.21.3 (v2026.9.14)

**Release Date:** September 14, 2026
**Since v0.21.2:** ~338 merged PRs

> Patch release. This tag exists so the remote-gateway sign-in fixes below reach Cloud agents, which auto-update to the newest release tag.

---

## What this patch ships for remote Desktop / Cloud users

- **Remote dashboard sessions no longer expire on refresh bursts** (#110061, fixes #55712). Both refresh paths on the gateway (the cookie gate and the desktop's native bearer route) now coalesce concurrent requests carrying the same rotating refresh token, so a Desktop wake burst can no longer replay an already-rotated token and revoke the whole session. Refresh also runs off the event loop, so a slow identity provider no longer freezes `/api/status`.

## Also fixed in this tag

- **Long-lived processes stop leaking duplicate state.db writer handles** (#110934, fixes #100896 #103339). The gateway, dashboard/Desktop backend, ACP and CLI readers attach read-only, and in-process writers share the registry handle, so the `N live SessionDB handles` precursor stops firing on a healthy topology.

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.9.11...v2026.9.14](https://github.com/NousResearch/hermes-agent/compare/v2026.9.11...v2026.9.14)

---

*← [v0.21.2 - The state.db Patch Release](/hermes/changelog/v0.21.2) | [v0.21.4 - Patch Release](/hermes/changelog/v0.21.4) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
