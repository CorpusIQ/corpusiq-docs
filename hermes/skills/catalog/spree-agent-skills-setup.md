---
title: "Spree Agent Skills - Spree 6 Commerce Skill Suite"
description: "spree/agent-skills - 10.1K combined installs across 42 indexed listings: Spree Commerce skills for building and running Spree 6 stores."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/spree-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "spree", "ecommerce", "ruby on rails"]
---

# Spree Agent Skills - Setup Guide

**Source:** [spree/agent-skills](https://www.skills.sh/spree/agent-skills) via skills.sh - 10.1K combined installs across 42 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 10 stars, MIT license, `main` branch, last pushed 2026-11-13, `SKILL.md` files under `skills/<name>/`
**Category:** Ecommerce - Spree Commerce store development and operations
**Quality Tier:** 🟠 Orange - one sampled skill (spree-payments) fails a scanner, and one (spree-deployment) was not parsed.

spree/agent-skills is the Spree Commerce organization's agent-skill collection for Spree 6.x, the open-source Ruby on Rails ecommerce platform. It ships 39 skills spanning the store lifecycle - catalog, pricing, checkout, payments, fulfillment, promotions, marketplace, B2B and multi-tenant - plus a Claude subagent (spree-expert), two slash commands and two safety hooks.

The skills work with Claude Code, Codex, Cursor, Copilot, Cline, Aider, Zed, Windsurf, OpenCode and 60+ other agentic CLIs. `npx skills add` installs the skills; installing as a Claude Code plugin additionally delivers the subagent, slash commands, safety hooks and the spree-docs MCP server. Spree 5.x projects should install the v0.3.0 release instead.

## Installation

```bash
npx skills add spree/agent-skills
```

That is it; the skills CLI auto-detects which agents you have installed and copies the skill files into each agent's native location.

Preview what is available without installing:

```bash
npx skills add spree/agent-skills --list
```

Install a specific subset:

```bash
npx skills add spree/agent-skills --skill spree-api-v3 --skill spree-checkout
```

Update later:

```bash
npx skills update
```

Claude Code: also get the safety hooks by installing as a plugin from inside a Claude Code session:

```text
/plugin marketplace add spree/agent-skills
/plugin install spree@spree
```

The plugin path adds the subagent, two slash commands, two safety hooks and the spree-docs MCP server on top of `npx skills add`. Use one path or the other; do not double-install.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| spree-storefront | 333 | The optional Next.js storefront for Spree 6: pages, checkout, multi-region URLs, B2B portal and @spree/sdk integration. |
| spree-customization | 333 | Decision tree for where a customization belongs - hook vs subscriber vs provider vs decorator. Use first. |
| spree-catalog | 332 | Products, variants, option types, product types, categories vs collections, media, custom fields and search. |
| spree-performance | 329 | Slow carts, N+1 queries, search latency, queue tuning, Store API caching and OpenTelemetry tracing. |
| spree-api-v3 | 329 | REST API v3: Store, Admin and Seller surfaces, auth, scopes, prefixed IDs, envelopes and errors. |
| spree-testing | 328 | RSpec + Factory Bot specs, spree_dev_tools, the API v3 shared contexts and dashboard tests. |
| spree-security | 328 | Hardening: secrets and API keys, CORS/CSP, webhook HMAC, GDPR, IDOR and PCI scope. |
| spree-pricing | 328 | Prices per currency, compare-at prices, price lists, volume pricing and EU Omnibus price history. |
| spree-payments | 328 | Payment methods and gateways, sessions, capture and void, refunds, gift cards and store credits. |
| spree-checkout | 328 | Cart-to-order completion, the requirements feed, Checkout::Registry and checkout hooks. |
| spree-i18n | 327 | UI and data translations: Spree.t, YAML, Mobility, RTL and locale URLs. |
| spree-deployment | 327 | Deploying to Docker, Render, AWS: env vars, Solid Queue, the dashboard build and S3/CDN. |
| spree-decorators | 327 | Extending Spree models and controllers via Module#prepend decorators, the last resort. |
| spree-events-webhooks | 326 | Events, subscribers and outbound webhooks: HMAC signing, retries and delivery-log redaction. |
| spree-typescript-sdk | 325 | @spree/sdk, @spree/admin-sdk, @spree/seller-sdk: auth, types, webhooks and SDK extensions. |
| spree-resource | 325 | Adding a model or API endpoint via spree:api_resource and documenting it in OpenAPI via rswag. |
| spree-upgrade | 324 | The spree upgrade CLI, rake spree:upgrade manifests, retrying steps and production backfills. |
| spree-promotions | 323 | Promotion rules, actions, calculators, coupon codes and discount resolution. |
| spree-extensions | 323 | Installing Spree gems or building your own extension (Rails engine + dashboard plugin). |
| spree-dependencies | 321 | Swapping core services, workflows and serializers via Spree.dependencies. |

The remaining 22 indexed listings range from 8 to 206 installs.

## Why This Matters for Hermes Agents

For a Hermes agent, Spree is a large, opinionated Rails platform where the expensive mistakes are not syntax but placement: whether a customization is a decorator, a workflow hook, a subscriber, a provider or a whole new resource. spree-customization turns that into a decision tree, and spree-decorators and spree-dependencies document the seams where a change belongs - or warn when a decorator or service swap is overkill.

The suite also covers the operational side a store builder hits after code lands: spree-deployment and spree-performance address production scaling and slow carts, spree-security covers Spree-specific risks such as IDOR on carts and webhook HMAC, and spree-events-webhooks connects placed orders to ERPs and notifications.

The Claude Code extras matter for autonomous work: `/spree:doctor` diagnoses the local dev stack, `/spree:audit-upgrade` produces an upgrade-readiness checklist, and the safety hooks block destructive database commands and flag hardcoded secrets before they ship.

## Usage

| You say | What happens |
|---|---|
| "Where should this customization go?" | spree-customization routes the change to a hook, subscriber, provider or decorator. |
| "Add a checkout step" | spree-checkout walks the Checkout::Registry requirements and completion hooks. |
| "Why is my cart 404 after checkout?" | spree-api-v3 explains the cart-to-order split and statuses. |
| "Set up Stripe" | spree-payments covers payment methods, sessions and capture. |
| "Sync placed orders to my ERP" | spree-events-webhooks configures subscribers and outbound webhooks with HMAC. |
| "Add a Brand model with an API" | spree-resource scaffolds the model plus Store/Admin endpoints and OpenAPI docs. |
| "Deploy to Render" | spree-deployment covers env vars, Solid Queue and the dashboard build. |

## Verification

Preview what ships before installing:

```bash
npx skills add spree/agent-skills --list
curl -fsSL https://raw.githubusercontent.com/spree/agent-skills/main/skills/spree-api-v3/SKILL.md | head -30
```

Skills live under `skills/<name>/`. The subagent, slash commands and safety hooks only arrive with the Claude Code plugin install, not `npx skills add`.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| spree-storefront | Pass | Pass | Pass |
| spree-customization | Pass | Pass | Pass |
| spree-catalog | Pass | Pass | Pass |
| spree-performance | Pass | Pass | Pass |
| spree-api-v3 | Pass | Pass | Warn |
| spree-testing | Pass | Pass | Pass |
| spree-security | Pass | Pass | Pass |
| spree-pricing | Pass | Pass | Pass |
| spree-payments | Pass | Pass | Fail |
| spree-checkout | Pass | Pass | Pass |
| spree-i18n | Pass | Pass | Pass |
| spree-deployment | not parsed | not parsed | not parsed |

spree-payments carries the only Fail in the sample (Snyk); spree-deployment was not parsed by the scanners. Re-check both skills.sh security pages before production use.

## Limitations

- Snapshot data, verified Nov 16, 2026: 10,079 combined installs across 42 indexed listings; 10 GitHub stars; MIT; last pushed 2026-11-13. Counts drift over time.
- spree-payments carries the only scanner Fail in the sample (Snyk); spree-deployment was not parsed. Re-check both before production use.
- The index lists 42 listings, but the README What ships table and the current tree cover 39 skills: spree-admin, spree-shipping-fulfillment and spree-legacy-api-v2 carry install counts with no matching skill directory (all under 300 installs).
- Targets Spree 6.x only; Spree 5.x projects should install the v0.3.0 release instead.
- The subagent, slash commands and safety hooks only arrive via the Claude Code plugin install; `npx skills add` installs skills alone.

## Related

- [Medusa Agent Skills](/hermes/skills/catalog/medusa-agent-skills-setup)
- [Magento 2 Agent Skills](/hermes/skills/catalog/magento2-agent-skills-setup)
- [WooCommerce Agent Skills](/hermes/skills/catalog/woocommerce-agent-skills-setup)
- [Shopify Development](/hermes/skills/catalog/shopify-development-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/spree:doctor` (Claude Code) to diagnose the local dev stack before debugging a store issue blindly.
- Start every change with spree-customization; most work does not need a gem or a decorator.
- Remember `SPREE_HOOKS_DISABLE=1` as the escape hatch for the safety hooks.
- Prefer workflow hooks and events over decorators and service swaps where the skills recommend them.
- On Spree 5.x, install the v0.3.0 release rather than the current Spree 6.x skills.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
