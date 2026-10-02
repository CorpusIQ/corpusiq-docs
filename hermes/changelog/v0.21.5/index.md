---
title: Hermes Agent v0.21.5 Patch Release
description: Hermes Agent v0.21.5 (v2026.9.24) - Patch release rolling up 460 PRs. Desktop plugin SDK wave, Simple/Advanced interface mode, Connectors page, French German Spanish catalogs.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.21.5/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.21.5 (v2026.9.24)

**Release Date:** September 24, 2026
**Since v0.21.4:** 1,610 non-merge commits · 4,828 changed files (+164,132 / −149,440) · 460 merged PRs · 475 closed issues

> Patch release. This tag rolls up the ~460 PRs merged since v0.21.4 into a stable tagged release for downstream consumers (Docker images, Hermes Cloud, hosted deployments).

---

## Highlights

- **Desktop plugin SDK wave** - composer draft API, session-list and row-decoration slots, sidebar nav preferences, model-pill label providers, typed settings/skills/toolsets/profiles bridges, a sandboxed embed primitive, an appearance-settings slot, and a public event bridge for plugin backends
- **Simple/Advanced interface mode** for the Desktop app
- **The Connectors page replaces the MCP tab**, with "Connect now" for a freshly installed plugin's MCP servers, and installed plugins' tools and skills going live in every open chat
- **Onboarding that offers catalog plugins** beside connectors
- **Complete French, German and Spanish Desktop catalogs** plus an RTL/LTR text direction setting
- **Custom model entry** from the composer and Settings pickers
- **Function-key and dictation voice shortcuts**
- **Per-profile stop/start/restart** under the host multiplexer, and `gateway.standalone` to opt a profile out

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.9.21...v2026.9.24](https://github.com/NousResearch/hermes-agent/compare/v2026.9.21...v2026.9.24)

---

*← [v0.21.4 - Patch Release](/hermes/changelog/v0.21.4) | [Changelog Home](/hermes/changelog) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
