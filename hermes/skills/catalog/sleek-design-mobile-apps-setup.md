---
title: "Sleek Design Mobile Apps - AI Mobile App Design Skill Setup"
description: "designed-by-ai/skills (sleekdotdesign/agent-skills) - design-mobile-apps, 680.6K installs, 572 GitHub stars. Sleek's official agent skill for designing mobile apps and UI screens via the sleek.design REST API - projects, chats, components, and screenshot rendering with device-flow API key auth."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sleek-design-mobile-apps-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "mobile design", "design", "sleek"]
---

# Sleek Design Mobile Apps - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/designed-by-ai/skills) (680.6K installs, Oct 8, 2026)
**GitHub:** [sleekdotdesign/agent-skills](https://github.com/sleekdotdesign/agent-skills) (572⭐, MIT)
**Category:** Design / Mobile App Development
**First Seen:** Sep 4, 2026 (skills.sh listing under designed-by-ai/skills)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass; Snyk verdict changed to Fail - see Security)

Sleek is an AI-powered mobile app design tool, and this is its official agent skill. An agent describes what should be built in plain language, and the skill drives Sleek's REST API (`/api/v1/*`) to create projects, run design chats, pull components, and render screenshots. The SKILL.md is a complete API reference with device-flow key onboarding, so the end user never handles a raw API key. The skills.sh listing source is `designed-by-ai/skills`; the GitHub repo the README ships from is `sleekdotdesign/agent-skills` (same content, 572⭐ canonical repo).

---

## Installation

```bash
npx skills add designed-by-ai/skills --skill design-mobile-apps
```

The GitHub-URL form shown on the skill page is equivalent:

```bash
npx skills add https://github.com/designed-by-ai/skills --skill design-mobile-apps
```

Note (from the publisher README): `npx skills add` installs into `.agents/skills/` in the working directory. If your agent does not discover skills there, point it at the installed `SKILL.md` explicitly. Manual install keeps the bundle intact wherever the platform expects skills.

## Prerequisites

| Requirement | Details |
|---|---|
| **Sleek account** | Free accounts get one-time trial credits (about one design run); sustained use needs Pro or higher ($49.99/month, or $30/month billed yearly with 20,000 monthly AI credits) |
| **SLEEK_API_KEY** | Environment variable. Created at sleek.design/agents/setup or managed at sleek.design/dashboard/api-keys |
| **Device-flow auth** | If no key is set, the skill runs the device flow: POST `/api/v1/device/start` → show the user the verification URL + user code → poll `/api/v1/device/poll` until approved. Keys expire after 15 minutes |
| **Network scope** | Single host: all requests go exclusively to `https://sleek.design`; no third-party endpoints |

## What It Provides

| Capability | How It Works |
|---|---|
| **Project management** | Create, list, get, and delete projects (`projects:read` / `projects:write` scopes) |
| **Design chats** | Send plain-language messages that describe what to build; runs return rendered screens (`chats:read` / `chats:write`) |
| **Component library** | List components in a project (`components:read`) |
| **Screenshot rendering** | Render component screenshots to images (`screenshots` scope) |
| **Minimal-scope keys** | Create API keys with only the scopes a task needs; prefer short-lived or revocable keys |
| **Contract self-discovery** | OpenAPI spec at `https://sleek.design/api/v1/spec.json`; browsable docs at `https://sleek.design/api/v1/docs` |

## Quick Start

1. Install the skill (above)
2. Run it; it will trigger the device flow for the API key on first use (user approves at the printed URL, key lands in `SLEEK_API_KEY`)
3. Ask for a design: create a project, send a chat message describing the app or screens wanted, and pull the returned rendered screens
4. Iterate with follow-up chat runs; use the screenshots scope to render components for review
5. Export assets or implement the design in code (HTML, React Native, SwiftUI) per the SKILL.md guidance

## CorpusIQ Use Cases

- **UGC visual assets** - generate app-screen mockups for content and landing-page visuals without a designer in the loop
- **Product concept exploration** - prototype mobile UI concepts for CorpusIQ feature pitches and investor decks in minutes
- **Client-facing demos** - render example dashboards or screens for outreach and onboarding material
- **Content production** - the HyperFrames/UGC pipeline can feed Sleek-rendered screens into video compositions
- **Competitive teardowns** - mock up competitor flows side by side to sharpen product positioning docs

## Limitations / Verification

- **Paid ceiling:** free tier is one-time trial credits; sustained use requires a Pro plan. State pricing plainly before any payment step (the SKILL.md mandates this).
- **Single-vendor lock:** the skill only talks to sleek.design. It is not a general design tool.
- **Listing quirk:** skills.sh indexes the publisher as `designed-by-ai/skills` while the README's canonical repo is `sleekdotdesign/agent-skills` - both GitHub repos resolve (HTTP 200) and carry identical content. Install via the skills.sh source name.

## Security

Security audits (Oct 8, 2026 re-check):

| Audit | Sep 7, 2026 | Oct 8, 2026 |
|---|---|---|
| Gen Agent Trust Hub | Pass | Pass |
| Socket | Pass | Pass |
| Snyk | Pass | Fail |

The Snyk verdict changed from Pass (Sep 7, 2026) to Fail (Oct 8, 2026). Before installing in sensitive environments, review the Snyk report linked on the skill page; the details page itself was returning a server error at re-check time.

## Related

- [HyperFrames - Video Composition Skill](/hermes/skills/catalog/hyperframes-setup) (visual production pipeline)
- [Meng To Skills - Frontend & Motion Design Suite Setup](/hermes/skills/catalog/mengto-skills-setup)
- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Discovery Page](/hermes/skills/marketplace/new-sep7-2026) →*
*Powered by CorpusIQ*
