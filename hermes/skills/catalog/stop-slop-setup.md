---
title: "Stop Slop — AI-Prose Pattern Cleaner Setup"
description: "hardikpandya/stop-slop — 1 skill, 10.6K installs: eliminates predictable AI writing patterns from prose. 15.7K GitHub stars, 3/3 security audit passes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/stop-slop-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "writing", "content quality", "anti-slop"]
---

# Stop Slop — Setup Guide

**Source:** [hardikpandya/stop-slop](https://skills.sh/hardikpandya/stop-slop)
**GitHub:** [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
**Skills:** 1 skill · 10.6K installs
**Category:** Content Quality
**First Seen:** catalogued August 17, 2026 sweep (stop-slop on skills.sh since January 20, 2026)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass (3/3)

Stop Slop eliminates predictable AI writing patterns from prose: filler phrases, formulaic structures, passive voice, vague declaratives, and narrator-from-a-distance framing. Its seven core rules read like a compressed style guide for human-sounding output — and it even bans em dashes, matching our own public-content rule.

---

## Installation

```bash
npx skills add hardikpandya/stop-slop
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/hardikpandya/stop-slop --skill stop-slop
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Prose to clean** | Any draft — post, email, doc, or page copy |

## What It Provides

The skill's seven core rules:

1. Cut filler phrases, emphasis crutches, and adverbs
2. Break formulaic structures (binary contrasts, negative listings, rhetorical setups)
3. Active voice — every sentence has a human subject doing something
4. Be specific — no vague declaratives or lazy extremes
5. Put the reader in the room — "you" beats "people"
6. Vary rhythm — mix sentence lengths; no em dashes
7. Trust readers — state facts directly, skip hand-holding

Reference files (`references/phrases.md`, `references/structures.md`) carry the concrete pattern lists.

## Quick Start

1. Install: `npx skills add hardikpandya/stop-slop`
2. Ask: "run stop-slop on this draft"
3. Apply the seven rules; the pattern references guide the rewrite

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Public content gate** | Pairs with our content-voice rules and slop scoring — a second pass before anything ships publicly |
| **Email quality** | Benoit-facing and outreach emails read human at first pass |
| **UGC script cleanup** | Video scripts and captions lose the AI rhythm before recording |

## Limitations / Verification

- Security audits on stop-slop: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — clean across all three
- Publisher-page install counts verified (10.6K single skill); GitHub 15.7K stars on the repo
- Single-skill cluster — the whole value is the seven rules plus the two reference files
- Complementary, not competitive, with avoid-ai-writing: stop-slop is the compressed ruleset; avoid-ai-writing is the audited multi-mode workflow

```bash
npx skills add hardikpandya/stop-slop   # verify install works
```

## Related

- [Avoid AI Writing Setup](/hermes/skills/catalog/avoid-ai-writing-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
