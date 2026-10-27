---
title: Hermes Agent v0.20.6 Patch Release
description: Hermes Agent v0.20.6 patch release - release notes, highlights, and security fixes.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.20.6/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.20.6

**Release Date:** August 27, 2026

> Patch release. This tag rolls up the ~525 PRs merged since v0.20.5 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

---

## About this release

Since v0.20.5 (v2026.8.19, tagged August 21), this window landed **~1,313 commits** across **~1,557 files** (+177,113 / −21,682)  -  **~525 merged PRs** including consent-gated real-profile browsing (use your default Chromium profile for local browsing, with Windows close-with-approval flow); the desktop Browser getting its own OS window plus a managed SSH remote-update engine and fleet profile rail; a large remote MCP catalog expansion (50+ live-verified vendor-hosted servers incl. Cloudflare, Grafana Cloud, Better Stack, Railway); TTL result caching for web_search/web_extract; lean-tail compression as the default; multi-query tool_search with stemming; opt-in OS-keychain encryption for stored secrets (no more per-launch macOS Keychain prompts); updaters pausing gateways over the control socket instead of tree-killing them; image/package-managed installs refusing unsafe in-place updates (#91277 Phase 3); cron durable-incident acks and clearer code-skew failures; Slack link-unfurl controls; shared Docker container identities; pluggable terminal environment backends; and new models across the pickers (GLM-5.3-Flash, MiniMax M3 free, MiniMax H3 Max video).

**Full curated release notes for this window will ship with v0.21.0**, which will document everything from v0.20.0 onward  -  highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.

## Updating

- `hermes update` from an existing install
- Fresh install: `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

**Full Changelog**: [v2026.8.19...v2026.8.27](https://github.com/NousResearch/hermes-agent/compare/v2026.8.19...v2026.8.27)

## Frequently Asked Questions

### What changed in Hermes Agent v0.20.6?

Patch release. This tag rolls up the ~525 PRs merged since v0.20.5 into a stable tagged release for downstream consumers (Docker images, hosted deployments, fresh installs).

### When was Hermes Agent v0.20.6 released?

August 27, 2026


---

*← [v0.20.5 - Patch Release](/hermes/changelog/v0.20.5) | [v0.21.0 - The Pantheon Release](/hermes/changelog/v0.21.0) →*

*↑ [Changelog Home](/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
