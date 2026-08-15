---
title: Swift Testing Pro Skill — Swift Testing Suite Setup
description: "twostraws/swift-testing-agent-skill — swift-testing-pro (7.5K installs): write and review Swift Testing code with modern API usage, async tests, confirmations, actor isolation, and XCTest migration guidance from Paul Hudson. All three security audits pass."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/swift-testing-pro-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "swift", "testing", "xctest"]
---

# Swift Testing Pro Skill — Setup Guide

**Source:** [twostraws/swift-testing-agent-skill](https://skills.sh/twostraws/swift-testing-agent-skill)
**GitHub:** [twostraws/swift-testing-agent-skill](https://github.com/twostraws/swift-testing-agent-skill) (407 stars)
**Skills:** 1 skill (`swift-testing-pro`) · 7.5K installs
**Category:** Testing (Swift)
**First Seen:** Mar 11, 2026 (catalogued August 15, 2026 midday sweep)
**Quality Tier:** 🟢 Production (all three security audits pass; publisher is Paul Hudson of Hacking with Swift)

Swift Testing Pro writes and reviews Swift Testing code for correctness, modern API usage, and project conventions — and reports only genuine problems, without nitpicking. It targets Swift 6.2+ with modern concurrency, covers async tests, confirmations, time limits, actor isolation, networking mocks, and raw identifiers, and provides migration guidance from XCTest.

---

## Installation

```bash
npx skills add twostraws/swift-testing-agent-skill --skill swift-testing-pro
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Swift 6.2+ project** | The skill targets modern Swift concurrency |

## What It Provides

| Capability | Notes |
|---|---|
| Core rules | references/core-rules.md for Swift Testing conventions |
| Better tests | references/writing-better-tests.md for structure and assertions |
| Async testing | references/async-tests.md — confirmations, time limits, actor isolation, mocks |
| New features | references/new-features.md — raw identifiers, test scopes, exit tests, attachments |
| XCTest migration | references/migrating-from-xctest.md |
| Honesty doctrine | Report only genuine problems — no invented issues |

## Quick Start

1. Install: `npx skills add twostraws/swift-testing-agent-skill --skill swift-testing-pro`
2. Ask: "review these Swift tests against Swift Testing conventions and migrate this XCTest file"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Swift client work** | Test review and migration for Swift codebases |
| **Test quality standard** | The no-nitpick doctrine matches our verification standards |
| **Modern API guidance** | Swift 6.2 concurrency and async testing patterns |

## Limitations / Verification

- Swift Testing does not support UI tests — XCTest must be used there
- Single-skill cluster; all three security audits pass (verified on skill page)
- Publisher: Paul Hudson (twostraws), 407 GitHub stars

```bash
npx skills add twostraws/swift-testing-agent-skill   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
