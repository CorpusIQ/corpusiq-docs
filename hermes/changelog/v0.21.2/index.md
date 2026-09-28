---
title: Hermes Agent v0.21.2 state.db Patch Release
description: Hermes Agent v0.21.2 (v2026.9.11) - The state.db patch release. Six PRs fix second-writer lock cancellation, false corruption reports, and bad-row crashes in the session store.
canonical: "https://www.corpusiq.io/docs/hermes/changelog/v0.21.2/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Hermes Agent v0.21.2 (v2026.9.11)

**Release Date:** September 11, 2026
**Since v0.21.1:** 947 non-merge commits · 1,869 changed files (+182,504 / −15,564) · 312 merged PRs · 140 contributors

> Patch release. v0.21.0 shipped a large rewrite of the session store's connection handling, and for some installs it made `state.db` fragile. This release closes that class of failure and rolls up everything else that landed on main in the four days since v0.21.1.

---

## Highlights

### state.db reliability campaign (six PRs, 44 issues closed)

If your `state.db` broke after v0.21.0, this is the release for you. Six PRs fix the root causes rather than the symptoms:

- **No more second writers** - profile gateways no longer write hosted-room state into the root `state.db` every 5 seconds (hosted rooms now live in `shared-state.db`), the dashboard opens read-only first, and cron's lifecycle guard goes through the tracked connection instead of a raw `open()` on a live database.
- **`doctor --fix` is safe** - it no longer checkpoints under a live holder.
- **Healthy databases stop being reported as corrupt** and one bad row no longer kills `sessions list`.

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.9.7...v2026.9.11](https://github.com/NousResearch/hermes-agent/compare/v2026.9.7...v2026.9.11)

---

*← [v0.21.1 - Patch Release](/docs/hermes/changelog/v0.21.1) | [v0.21.3 - Patch Release](/docs/hermes/changelog/v0.21.3) →*

*↑ [Changelog Home](/docs/hermes/changelog)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
