---
title: "VTEX Skills — Commerce Platform Development Suite Setup"
description: "vtex/skills — 51 skills, 32.6K installs: VTEX's official ecommerce development suite covering VTEX IO apps, FastStore storefronts, headless BFFs, payments, and marketplace integrations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vtex-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "ecommerce", "vtex", "faststore", "marketplace"]
---

# VTEX Skills — Setup Guide

**Source:** [vtex/skills](https://skills.sh/vtex/skills)
**GitHub:** [vtex/skills](https://github.com/vtex/skills)
**Skills:** 51 skills · 32.6K total installs
**Category:** Ecommerce Development
**First Seen:** March 17, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, and Snyk Pass on the vtex-io-react-apps flagship; official VTEX org; 39 GitHub stars

VTEX is a major ecommerce platform, and this is its official agent skill suite for building on it. The 51 skills map the platform's surfaces: VTEX IO apps (React frontends, service apps, GraphQL APIs, auth, master data, events, observability), FastStore storefront development (theming, state management, data fetching, overrides), headless commerce architecture (BFF patterns, checkout proxy, caching, intelligent search), payments (provider protocol, PCI security, idempotency, async flows), and marketplace operations (order hooks, catalog sync, rate limiting, fulfillment). Each skill carries explicit decision rules and cross-references sibling skills when a task belongs elsewhere.

---

## Installation

```bash
npx skills add vtex/skills
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/vtex/skills --skill vtex-io-react-apps
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **VTEX account** | A VTEX workspace for platform work; skills assume VTEX IO CLI tooling context |
| **App framework knowledge** | React/TypeScript for storefront skills, Node for service apps |

## What It Provides

| Skill Group | Examples | Purpose |
|---|---|---|
| VTEX IO frontend | vtex-io-react-apps, vtex-io-admin-react, vtex-io-storefront-react | React components, interfaces.json, contentSchemas.json, Site Editor blocks |
| VTEX IO backend | vtex-io-service-apps, vtex-io-graphql-api, vtex-io-events-and-workers | Service apps, GraphQL resolvers, events and workers |
| VTEX IO platform | vtex-io-auth-and-policies, vtex-io-rbac, vtex-io-masterdata, vtex-io-observability-and-ops | Auth, RBAC, master data, observability |
| FastStore | faststore-storefront, faststore-theming, faststore-state-management, faststore-data-fetching | Headless storefront development |
| Headless architecture | headless-bff-architecture, headless-checkout-proxy, headless-caching-strategy | Headless commerce patterns |
| Payments | payment-provider-protocol, payment-pci-security, payment-idempotency, payment-async-flow | Payment integrations and compliance |
| Marketplace | marketplace-order-hook, marketplace-catalog-sync, marketplace-rate-limiting, marketplace-fulfillment | Marketplace seller integration |

Top skills by installs: vtex-io-react-apps (1.0K), vtex-io-masterdata (860), vtex-io-service-apps (859), vtex-io-graphql-api (855).

## Quick Start

1. Install: `npx skills add vtex/skills`
2. Load vtex-io-react-apps for storefront component work or vtex-io-service-apps for backend services
3. Ask the agent to scaffold the component or service — the skill's decision rules route tasks to the correct sibling skill

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Ecommerce operator integrations** | Marketplace and payment skills map to the connector-heavy workflows CorpusIQ serves |
| **Headless commerce builds** | FastStore and BFF skills support modern storefront architecture projects |
| **Payment compliance context** | payment-pci-security and payment-idempotency encode the patterns operators need for reliable checkouts |
| **Platform-documented agent work** | Official VTEX skills mean agent-generated code matches platform documentation |

## Limitations / Verification

- Security audits on the vtex-io-react-apps flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass
- Publisher-page total verified (32.6K across 51 skills); 39 GitHub stars as of the sweep
- Skills assume VTEX platform context (IO CLI, workspaces) and are not general-purpose ecommerce guides
- First seen March 17, 2026; the suite has grown steadily since

```bash
npx skills add vtex/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
