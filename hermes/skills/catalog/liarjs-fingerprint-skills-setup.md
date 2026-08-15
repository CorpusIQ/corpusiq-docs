---
title: LiarJS Skills — Browser Fingerprint & Playwright Stealth Setup
description: "liarjsdev/liarjs-skills — 4 skills at 51.9K installs: fingerprint-ci-gate, playwright-stealth-verify, browser-fingerprint-audit, and fingerprint-failure-triage for anti-bot detection and stealth verification."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/liarjs-fingerprint-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "playwright", "fingerprinting", "anti-bot"]
---

# LiarJS Skills — Setup Guide

**Source:** [liarjsdev/liarjs-skills](https://skills.sh/liarjsdev/liarjs-skills)
**GitHub:** [liarjsdev/liarjs-skills](https://github.com/liarjsdev/liarjs-skills)
**Skills:** 4 skills · 51.9K total installs
**Category:** Browser Automation & Anti-Detection
**First Seen:** August 15, 2026 sweep
**Quality Tier:** 🟢 Production

Four tightly-scoped skills around browser fingerprinting and Playwright stealth, each at 13.0K installs. Together they form a complete loop: audit a fingerprint (browser-fingerprint-audit), verify Playwright stealth posture (playwright-stealth-verify), gate CI on fingerprint health (fingerprint-ci-gate), and triage failures when detection regresses (fingerprint-failure-triage). Directly relevant to any agent that drives browsers against Cloudflare-protected or anti-bot sites.

---

## Installation

```bash
npx skills add liarjsdev/liarjs-skills
```

Individual skills:

```bash
npx skills add liarjsdev/liarjs-skills --skill playwright-stealth-verify
npx skills add liarjsdev/liarjs-skills --skill browser-fingerprint-audit
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the installer |
| **Playwright** | For stealth verification workflows |
| **CI pipeline** | For the fingerprint CI gate |

## What It Provides

| Skill | Installs | Notes |
|---|---|---|
| fingerprint-ci-gate | 13.0K | Gate CI runs on fingerprint health |
| playwright-stealth-verify | 13.0K | Verify Playwright stealth posture |
| browser-fingerprint-audit | 13.0K | Audit browser fingerprint signals |
| fingerprint-failure-triage | 13.0K | Triage detection regressions |

## Quick Start

1. `npx skills add liarjsdev/liarjs-skills`
2. Run the audit: "audit my Playwright browser context's fingerprint and flag detectable signals"
3. Wire the CI gate into the automation repo so stealth regressions fail the pipeline

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Mac Mini Playwright stack** | Stealth verification for the persistent-context browser used on Cloudflare-protected sites |
| **Anti-bot evasion QA** | Fingerprint audits before each platform-automation rollout |
| **Regression triage** | fingerprint-failure-triage when a platform starts blocking our automation |
| **CI hygiene** | Gate automation repos on fingerprint health before deploy |

## Limitations / Verification

- Stealth techniques evolve against detection — re-audit after platform updates
- Skills assume a Playwright/CI toolchain is already present

```bash
npx skills add liarjsdev/liarjs-skills --skill browser-fingerprint-audit   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Playwright Social Media Automation](/hermes/skills/) — browser automation doctrine
- [Chrome DevTools MCP Skills Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup/) — browser inspection

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
