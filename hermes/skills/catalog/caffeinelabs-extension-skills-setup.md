---
title: CaffeineLabs Extension Skills — Agent Platform Extensions Setup
description: "caffeinelabs/skills — 39 extension skills at 259.4K installs: email calendar/marketing/verification/raw, Stripe, QR code, camera, object storage, authorization, HTTP outcalls, OpenAI, posting-to-X, OQL querying, Google Mail/Calendar connectors, and a Motoko series."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/caffeinelabs-extension-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "email", "stripe", "extensions"]
---

# CaffeineLabs Extension Skills — Setup Guide

**Source:** [caffeinelabs/skills](https://skills.sh/caffeinelabs/skills)
**GitHub:** [caffeinelabs/skills](https://github.com/caffeinelabs/skills)
**Skills:** 39 skills · 259.4K total installs
**Category:** Agent Platform Extensions & Connectors
**First Seen:** August 15, 2026 sweep
**Quality Tier:** 🟢 Production (largest extension-skill suite catalogued this week)

CaffeineLabs publishes a large suite of `extension-*` capabilities for an agent platform, plus connector and Motoko (Internet Computer language) series. The email surface is the standout for business operators: calendar events, marketing, verification, and raw SMTP-level access all ship as separate skills around 13K installs each. Stripe, object storage, authorization, HTTP outcalls, and X posting round out the platform-integration surface, with Google Mail and Google Calendar connectors in the 7-10K range.

---

## Installation

```bash
npx skills add caffeinelabs/skills
```

Install individual skills by name, for example:

```bash
npx skills add caffeinelabs/skills --skill extension-email-marketing
npx skills add caffeinelabs/skills --skill connector-googlemail
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the `skills add` installer |
| **Platform account** | The extension skills target the platform runtime the suite is built for (the Motoko series places it in the Internet Computer ecosystem) |
| **Service credentials** | Per-skill: Gmail OAuth, Stripe API key, X API keys as needed |

## What It Provides

| Skill | Installs | Notes |
|---|---|---|
| extension-email-calendar-events | 13.4K | Calendar event handling |
| extension-stripe | 13.1K | Payment processing |
| extension-email-marketing | 13.1K | Campaign and marketing email flows |
| extension-email-verification | 13.1K | Address verification |
| extension-email / extension-email-raw | 13.1K each | Standard and raw SMTP-level email |
| extension-posting-to-x | 13.1K | X/Twitter publishing |
| extension-openai | 13.1K | Model calls from the platform |
| extension-http-outcalls | 13.1K | External HTTP requests |
| extension-authorization | 13.1K | Auth and permission flows |
| extension-oql / extension-querying-oql | 12.6K / 9.9K | OQL data querying |
| connector-googlemail | 10.0K | Gmail connector |
| connector-googlecalendar | 7.1K | Google Calendar connector |
| writing-motoko, migrating-motoko, migrating-motoko-actors | ~1 each | Motoko (Internet Computer) development series |

## Quick Start

1. `npx skills add caffeinelabs/skills`
2. Pick the extension matching the capability you need (email-marketing for outreach, stripe for billing)
3. Configure service credentials in the platform environment
4. Ask the agent to exercise the capability: "send a verification email to x@y.com and log the result"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Email verification** | extension-email-verification for list hygiene before outreach sends |
| **Marketing sends** | extension-email-marketing patterns for campaign automation design |
| **Calendar operations** | extension-email-calendar-events for scheduling workflows |
| **Reference patterns** | Authorization and HTTP-outcall extension designs as templates for MCP connector architecture |

## Limitations / Verification

- The extension series targets a specific platform runtime, not raw Claude Code or Hermes sessions — treat it as a pattern reference plus capability set for that platform
- Motoko skills are for Internet Computer canister development, niche outside ICP work

```bash
npx skills add caffeinelabs/skills --skill extension-email-verification   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Resend Skills Setup](/hermes/skills/catalog/resend-skills-setup/) — email deliverability and templates

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
