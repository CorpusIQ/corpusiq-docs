---
title: Tailwind 4 Docs Skill — Local Docs Snapshot Setup
description: "lombiq/tailwind-agent-skills — tailwind-4-docs (10.1K installs): navigate a locally synced Tailwind CSS v4 documentation snapshot for development, migration, and review questions with official guidance. Snyk audit: Warn."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tailwind-4-docs-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "tailwind", "css", "documentation"]
---

# Tailwind 4 Docs Skill — Setup Guide

**Source:** [lombiq/tailwind-agent-skills](https://skills.sh/lombiq/tailwind-agent-skills)
**GitHub:** [lombiq/tailwind-agent-skills](https://github.com/lombiq/tailwind-agent-skills) (62 stars)
**Skills:** 1 skill (`tailwind-4-docs`) · 10.1K installs
**Category:** Frontend Documentation
**First Seen:** Feb 3, 2026 (catalogued August 15, 2026 midday sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub and Socket pass; Snyk Warn on the skill page)

tailwind-4-docs teaches an agent to answer Tailwind CSS v4 questions — utilities, variants, config, migration, compatibility, implementation, refactors, and reviews — from a locally synced snapshot of the official documentation, instead of stale training data.

---

## Installation

```bash
npx skills add lombiq/tailwind-agent-skills --skill tailwind-4-docs
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **One-time snapshot init** | The skill requires initializing the docs snapshot into references/docs/ |

## What It Provides

| Capability | Notes |
|---|---|
| Local docs snapshot | references/docs/ with an index at references/docs-index.tsx |
| Topic routing | Utility, variant, config, migration, compatibility, implementation, refactor, review |
| Freshness gate | Stops and asks for re-initialization if the snapshot is older than one week |
| Engineering playbook | references/engineering-playbook.md for implementation and refactor work |

## Quick Start

1. Install: `npx skills add lombiq/tailwind-agent-skills --skill tailwind-4-docs`
2. Run the one-time initialization to sync the docs snapshot
3. Ask: "which Tailwind v4 utilities changed from v3, and how do I migrate this config?"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Tailwind projects** | Official-guidance answers for v4 work instead of model memory |
| **Migration work** | v3-to-v4 migration questions for client frontends |
| **Docs-style grounding** | A proven pattern for local-docs-snapshot skills we can copy for our own docs |

## Limitations / Verification

- Snyk audit Warn (named on the skill page) — install into a reviewed environment
- Upstream Tailwind docs are source-available, not open-source; you must initialize the snapshot yourself and comply with the upstream license
- Requires re-initialization when the snapshot is older than one week

```bash
npx skills add lombiq/tailwind-agent-skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
