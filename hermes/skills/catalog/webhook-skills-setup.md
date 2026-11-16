---
title: "Webhook Skills - Provider Webhook Receivers and Verification"
description: "hookdeck/webhook-skills - 10.0K combined installs across 96 indexed listings: webhook receivers, signature verification and event handling for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/webhook-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "webhooks", "integration", "signatures"]
---

# Webhook Skills - Setup Guide

**Source:** [hookdeck/webhook-skills](https://www.skills.sh/hookdeck/webhook-skills) via skills.sh - 10.0K combined installs across 96 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 102 stars, MIT license, `main` branch, last pushed 2026-11-16, `SKILL.md` files under `skills/<provider>-webhooks/`
**Category:** Integration - webhook receivers, signature verification and event handling
**Quality Tier:** 🟠 Orange - webhook-handler-patterns carries the only Snyk Fail in the sample; six other sampled skills carry Snyk Warns.

Webhook Skills is Hookdeck's catalog of provider-specific skills for AI coding agents that receive, verify, sign and handle webhooks. Each skill bundles step-by-step setup guidance, signature verification code and runnable example handlers for Express, Next.js and FastAPI, and works with Claude Code, Cursor, VS Code Copilot and any assistant supporting the Agent Skills specification.

The index spans 96 listings. The bulk of installs concentrate in Stripe and GitHub plus the cross-provider patterns and the Hookdeck Event Gateway, while the long tail covers roughly eighty further providers at name level.

## Installation

```bash
# list available skills
npx skills add hookdeck/webhook-skills --list

# install one provider skill
npx skills add hookdeck/webhook-skills --skill stripe-webhooks

# install several at once
npx skills add hookdeck/webhook-skills --skill stripe-webhooks --skill shopify-webhooks
```

In Claude Code the repo ships as a plugin marketplace:

```text
/plugin marketplace add hookdeck/webhook-skills
/plugin install stripe-webhooks@webhook-skills
/plugin install webhook-skills@webhook-skills
```

For local development, run the Hookdeck CLI tunnel without an account:

```bash
npx hookdeck-cli listen 3000 stripe --path /webhooks/stripe
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| stripe-webhooks | 604 | Receive and verify Stripe webhooks; handle payment events like payment_intent.succeeded. |
| github-webhooks | 512 | Receive and verify GitHub webhooks; handle push, pull_request, issues and release events. |
| webhook-handler-patterns | 455 | Handler best practices: verify first, parse second, idempotency, retries and replay. |
| shopify-webhooks | 291 | Receive and verify Shopify webhooks; orders/create, products/update and customers/create. |
| resend-webhooks | 266 | Receive and verify Resend webhooks; email.sent, email.delivered, email.bounced and inbound. |
| paddle-webhooks | 258 | Receive and verify Paddle webhooks; subscription and transaction events. |
| sendgrid-webhooks | 253 | Receive and verify SendGrid webhooks; email delivery events. |
| elevenlabs-webhooks | 237 | Receive and verify ElevenLabs webhooks; call transcription events. |
| hookdeck-event-gateway | 214 | Hookdeck Event Gateway: guaranteed delivery, retries, replay, rate limiting and filtering. |
| woocommerce-webhooks | 213 | Receive and verify WooCommerce webhooks; order, product and customer events. |
| clerk-webhooks | 210 | Receive and verify Clerk webhooks; user, session and organization events. |
| vercel-webhooks | 204 | Receive and verify Vercel webhooks; deployment and project events. |
| postmark-webhooks | 203 | Receive and process Postmark webhooks; bounces, opens, clicks and spam complaints. |
| openai-webhooks | 202 | Receive and verify OpenAI webhooks; fine-tuning jobs and batch completions. |
| deepgram-webhooks | 200 | Receive and verify Deepgram webhooks; transcription callbacks. |
| cursor-webhooks | 200 | Receive and verify Cursor Cloud Agent webhooks; status change events. |

The remaining 80 indexed listings range from 31 to 199 installs.

## Why This Matters for Hermes Agents

The collection's real value is the discipline it encodes: verify the signature first, parse the body second, and handle the event idempotently. That sequence is where hand-rolled webhook code most often goes wrong, and it is spelled out per provider rather than left to inference. Each skill documents the exact auth model a provider uses (HMAC-SHA256, Ed25519, an unsigned secret header, or no signature at all), so an agent does not guess at a scheme it has not seen before.

The runnable Express, Next.js and FastAPI examples turn each skill from a description into a starting point, and webhook-handler-patterns plus the Hookdeck Event Gateway generalize the hard parts (idempotency, retries, replay) beyond any single provider. For an agent that integrates services, this is reference material worth having loaded before touching a webhook endpoint.

## Usage

| You say | What happens |
|---|---|
| "Set up Stripe webhook handling in my Express app" | stripe-webhooks provides verification code and an Express example handler. |
| "Verify GitHub webhook signatures in Next.js" | github-webhooks walks HMAC-SHA256 over the raw body with a timing-safe compare. |
| "Make my webhook handler idempotent" | webhook-handler-patterns covers the verify-parse-handle sequence, retries and replay. |
| "I need retries and replay without building a queue" | hookdeck-event-gateway replaces the queue with guaranteed delivery and replay. |
| "Handle Shopify order events" | shopify-webhooks verifies signatures and parses orders/create and products/update. |
| "Process Resend delivery events" | resend-webhooks handles email.sent, email.delivered and email.bounced. |
| "Test webhooks on localhost" | npx hookdeck-cli listen forwards events to the local server with an inspect UI. |

## Verification

Inspect the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/hookdeck/webhook-skills/main/skills/stripe-webhooks/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/hookdeck/webhook-skills/main/skills/github-webhooks/SKILL.md | head -20
npx skills add hookdeck/webhook-skills --list
```

Each skill lives at `skills/<provider>-webhooks/` with `SKILL.md`, a `references/` directory (overview, setup, verification) and `examples/` handlers for Express, Next.js and FastAPI. The repository is large, so confirm a provider's directory path exists in the current tree before installing.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| stripe-webhooks | Pass | Pass | Warn |
| github-webhooks | Pass | Pass | Pass |
| webhook-handler-patterns | Pass | Pass | Fail |
| shopify-webhooks | Pass | Pass | Pass |
| resend-webhooks | Pass | Pass | Warn |
| paddle-webhooks | Pass | Pass | Warn |
| sendgrid-webhooks | Pass | Pass | Pass |
| elevenlabs-webhooks | Pass | Pass | Warn |
| hookdeck-event-gateway | Pass | Pass | Pass |
| woocommerce-webhooks | Pass | Pass | Warn |
| clerk-webhooks | Pass | Pass | Warn |
| vercel-webhooks | Pass | Pass | Pass |

webhook-handler-patterns carries the only Snyk Fail in the sample; review its skills.sh security page before enabling it unsupervised. Signature verification only works with the provider's signing secret or webhook configuration, which these skills assume you already hold.

## Limitations

- Snapshot data, verified Nov 16, 2026: 10,021 combined installs across 96 indexed listings; 102 GitHub stars; MIT; last pushed 2026-11-16. Counts drift over time.
- webhook-handler-patterns carries the only Snyk Fail in the sample. Treat it as supervised-use and re-check its skills.sh page before production.
- The repository tree is large (17,681 files) and the indexed tree listing was truncated, so this guide cites only paths confirmed by direct fetch.
- Verification requires the provider's signing secret or webhook configuration; the skills cannot authenticate events without it.
- The skill generator (scripts/generate-skills.sh) keeps adding providers, so coverage and counts move faster than this guide.

## Related

- [Webhook Subscriptions](/hermes/skills/catalog/webhook-subscriptions-setup)
- [Stripe Link CLI Skills](/hermes/skills/catalog/stripe-link-cli-setup)
- [Zapier Agent Skills](/hermes/skills/catalog/zapier-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the provider skills you actually receive webhooks from; each is roughly 200 KB.
- The Claude Code bundle namespaces skills as webhook-skills:stripe-webhooks, while a granular install exposes stripe-webhooks:stripe-webhooks.
- Use npx hookdeck-cli listen for local development; no Hookdeck account is required.
- Verify the signature before parsing the body; the verify-first discipline lives in webhook-handler-patterns.
- Scaffold a missing provider with the skill generator: ./scripts/generate-skills.sh generate "name=https://docs.example.com/webhooks" --create-pr.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
