---
title: Hermes Agent v0.21.4 Patch Release
description: Hermes Agent v0.21.4 (v2026.9.21) - Patch release rolling up 1,812 PRs. Gateway singleton lock, stream-json CLI output, skills.auto_load, session_search bounds, new video catalogs.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.21.4/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.21.4 (v2026.9.21)

**Release Date:** September 21, 2026
**Since v0.21.3:** 5,071 non-merge commits · 5,169 changed files (+312,961 / −62,855) · 1,812 merged PRs · 2,116 issues closed

> Patch release. This tag rolls up the ~1,800 PRs merged since v0.21.3 into a stable tagged release for downstream consumers (Docker images, Hermes Cloud, hosted deployments).

---

## Highlights

- **Host-wide gateway singleton lock** with a rendezvous record; the Desktop app now attaches to the running host backend instead of spawning a second one
- **One backend-owned connector operation** with a setup card on Desktop, TUI and CLI
- **`--format stream-json`** structured JSONL output for the CLI
- **`skills.auto_load`** pins skills into every new session's prompt
- **Desktop quality of life** - a chat/UI font picker, one-click local engine updates, and plugin uninstall from the Plugins hub
- **A `decline` unauthorized-DM behavior** for the gateway
- **Configurable MCP discovery connect cap** (`mcp.discovery_concurrency`)
- **`session_search` after/before bounds** plus OR-relaxed recall retry, and `hermes sessions set-journal-mode`
- **Video catalog additions** - LTX 2.5 and Kling O3
- **A website page for every catalog plugin and author**, with pinned-commit READMEs and added/updated sorting
- **A dozen new community plugins** in the catalog

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.9.14...v2026.9.21](https://github.com/NousResearch/hermes-agent/compare/v2026.9.14...v2026.9.21)

---

*← [v0.21.3 - Patch Release](/docs/hermes/changelog/v0.21.3) | [v0.21.5 - Patch Release](/docs/hermes/changelog/v0.21.5) →*

*↑ [Changelog Home](/docs/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
