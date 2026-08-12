---
title: MCP Billing Gateway
description: "Setup and usage guide for MCP Billing Gateway. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# MCP Billing Gateway

**Source:** mcp.so submission #3281 (July 23, 2026) · GitHub: [sapph1re/mcp-billing-gateway-sdk](https://github.com/sapph1re/mcp-billing-gateway-sdk)

## What It Does

Reverse proxy that adds Stripe fiat billing AND x402 crypto micropayments to any MCP server without touching upstream server code. Operators register their server, set per-call prices, and issue API keys. Clients authenticate with an API key; each tool call routes through the gateway for metering, payment verification, and transparent proxying.

**Key capabilities:**
- Stripe fiat billing + x402 crypto micropayments in one gateway
- Zero upstream server code changes required
- API key management and per-call metering
- Transparent proxying to upstream MCP server

## Relevance to Operators

Essential for MCP server operators who want to monetize:
- Wrap any MCP server with billing in minutes
- Offer both fiat (Stripe) and crypto (x402) payment options
- Track per-client usage and enforce rate limits
- No need to build billing logic into your server code

**Rating:** ★★ — Early stage (1 GitHub star, created April 2026). Addresses a growing need as the MCP ecosystem matures toward monetization. Part of the same developer's "sapph1re" suite alongside Feedback Synthesis MCP.

## Quick Integration

**Transport:** Reverse proxy (sits between client and upstream MCP server)  
**Auth:** API key per client  
**Pricing:** Free to deploy (gateway is open source); Stripe fees apply, x402 gas fees apply  

```bash
# Deploy the gateway
git clone https://github.com/sapph1re/mcp-billing-gateway-sdk
cd mcp-billing-gateway-sdk
npm install
npm run build

# Configure your upstream MCP server
export UPSTREAM_URL="https://your-server.com/mcp"
export STRIPE_SECRET_KEY="sk_live_..."
npm start
```

## Use Cases

1. **SaaS MCP Server:** Add Stripe subscriptions to your hosted MCP server
2. **Pay-per-call APIs:** Charge per tool invocation via x402 micropayments
3. **Freemium Gate:** Offer free tier to first N calls, then require payment

## Caveats

- 1 GitHub star, very early stage
- Adds latency overhead (one proxy hop)
- Requires Stripe account for fiat billing
- x402 payment ecosystem still nascent
