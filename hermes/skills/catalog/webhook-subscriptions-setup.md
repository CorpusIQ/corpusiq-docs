---
title: Webhook Subscriptions — Skill Setup Guide
description: Install and configure webhook-subscriptions, the Hermes Agent skill for triggering agent runs from external services via webhook POST endpoints — 80 installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/webhook-subscriptions-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Webhook Subscriptions — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/webhook-subscriptions) (80 installs)
**Category:** Automation / Integration
**License:** MIT · **Platforms:** Linux, macOS
**Dependencies:** Hermes Agent, Hermes Gateway with webhook platform enabled

Create dynamic webhook subscriptions so external services can trigger Hermes agent runs by POSTing events to a URL. GitHub pushes, Stripe payment events, CI/CD pipeline completions, IoT sensor alerts — any service that can send an HTTP POST becomes a trigger for Hermes to take action.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Event-driven agent runs** | External service POSTs → Hermes processes event |
| **HMAC signature verification** | Prevents spoofed requests — only trusted sources trigger |
| **Payload-to-context injection** | Webhook body becomes agent context |
| **Per-subscription filtering** | Route different events to different profiles/skills |
| **Dynamic subscription management** | Create, list, delete subscriptions from Hermes |

---

## Architecture

```
┌──────────────┐   POST /webhook/abc123    ┌──────────────────┐
│  GitHub      │──────────────────────────▶│  Hermes Gateway  │
│  (push event)│   HMAC-SHA256 signature   │  :8742            │
└──────────────┘                           └────────┬─────────┘
                                                     │
┌──────────────┐   POST /webhook/def456    ┌────────▼─────────┐
│  Stripe      │──────────────────────────▶│  Agent Dispatch  │
│  (payment)   │   HMAC-SHA256 signature   │  (profile + ctx) │
└──────────────┘                           └──────────────────┘
```

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill webhook-subscriptions
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/automation/webhook-subscriptions ~/.hermes/skills/
```

---

## Setup

### Step 1: Enable the webhook platform

```bash
hermes gateway setup
```

Follow the prompts to:
- Enable webhooks
- Set the port (default: 8742)
- Set a global HMAC secret (used to verify incoming signatures)

Verify it's running:

```bash
hermes webhook list
```

If it returns a list (even empty), the platform is active.

### Step 2: Make gateway reachable (if external services)

For services like GitHub or Stripe to reach your local Hermes:

```bash
# Option A: Cloudflare Tunnel
cloudflared tunnel --url http://localhost:8742

# Option B: ngrok
ngrok http 8742

# Option C: Direct (if on a public server)
# Ensure firewall allows port 8742
```

### Step 3: Create a subscription

```
> Load webhook-subscriptions skill
> Create a webhook for GitHub push events on repo corpusiq/api
> Route to profile: corpusiq, skill: deploy-on-push
```

---

## Basic Usage

### Creating subscriptions

```
> Subscribe to GitHub push events for corpusiq/api
> Create a Stripe webhook for payment_intent.succeeded events
> Watch my CI pipeline — trigger on build complete
```

### Listing and managing

```
> List my webhook subscriptions
> Delete webhook subscription abc123
> Show the webhook URL for my GitHub subscription
```

### Testing

```
> Test webhook abc123 with a sample GitHub payload
```

---

## Security Model

| Layer | Protection |
|-------|-----------|
| **HMAC signatures** | Every incoming request must carry a valid HMAC-SHA256 signature matching the global secret |
| **Per-subscription secrets** | Optionally override global secret per subscription for provider-specific keys |
| **Payload validation** | Malformed JSON rejected before agent sees it |
| **Rate limiting** | Gateway-level rate limiting prevents abuse |

---

## Provider-Specific Setup

### GitHub

1. Repo → Settings → Webhooks → Add webhook
2. Payload URL: `https://your-domain/webhook/<subscription-id>`
3. Content type: `application/json`
4. Secret: Your HMAC secret
5. Events: Select "Just the push event" or choose specific events

### Stripe

1. Stripe Dashboard → Developers → Webhooks → Add endpoint
2. Endpoint URL: `https://your-domain/webhook/<subscription-id>`
3. Events to send: Select specific events (e.g., `payment_intent.succeeded`)
4. Signing secret: Your HMAC secret

---

## Tips

- **One subscription per event source:** Don't multiplex — create separate subscriptions for GitHub, Stripe, CI
- **Profile routing:** Route production events to your ops profile, dev events to your dev profile
- **Test with sample payloads:** Use the test command before wiring up live services
- **Monitor in gateway logs:** `hermes gateway logs` shows incoming webhook activity

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| "Webhook platform not enabled" | Gateway not configured | Run `hermes gateway setup` |
| 401 on incoming requests | HMAC mismatch | Verify secret matches between Hermes and sender |
| Gateway not reachable | Port not exposed | Use Cloudflare Tunnel or ngrok |
| Agent not triggering | Wrong profile/skill routing | Check subscription config with `hermes webhook list` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
