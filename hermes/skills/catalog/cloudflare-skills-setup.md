---
title: "Cloudflare Skills — Edge Computing & Workers Platform"
description: Cloudflare's official agent skills — Wrangler CLI, Workers, Durable Objects, web performance, and Turnstile. 100K+ combined installs across 11 skills for building on the edge.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cloudflare-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Cloudflare Skills — Setup Guide

**Source:** [cloudflare/skills](https://skills.sh/cloudflare/skills) (100K+ combined installs)
**GitHub:** [cloudflare/skills](https://github.com/cloudflare/skills) (2,481 ⭐)
**Category:** Platform / Edge Computing
**Quality Tier:** 🟢 Production

Cloudflare Skills is the official agent skills collection for building on Cloudflare's edge platform. It covers Workers deployment, Wrangler CLI, Durable Objects, performance optimization, Turnstile anti-bot, D1, R2, and more. These skills teach Hermes agents how to deploy, manage, and optimize applications on the world's largest edge network.

---

## Installation

```bash
# Core platform skills (highest installs)
npx skills add cloudflare/skills --skill wrangler
npx skills add cloudflare/skills --skill workers-best-practices
npx skills add cloudflare/skills --skill web-perf

# Security & anti-bot
npx skills add cloudflare/skills --skill turnstile-spin

# MCP server deployment
npx skills add cloudflare/skills --skill building-mcp-server-on-cloudflare

# Advanced platform
npx skills add cloudflare/skills --skill durable-objects
npx skills add cloudflare/skills --skill agents-sdk
npx skills add cloudflare/skills --skill cloudflare
npx skills add cloudflare/skills --skill cloudflare-one
npx skills add cloudflare/skills --skill sandbox-sdk
npx skills add cloudflare/skills --skill cloudflare-email-service
npx skills add cloudflare/skills --skill cloudflare-one-migrations
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **wrangler** | 39.4K | Wrangler CLI — deploy Workers, manage KV/R2/D1, tail logs, configure bindings |
| **workers-best-practices** | 32.7K | Production Workers patterns — error handling, caching, routing, performance |
| **web-perf** | 28.9K | Web performance optimization — CDN caching, image optimization, HTTP/3 |
| **turnstile-spin** | 15.0K | Turnstile anti-bot integration — invisible CAPTCHA alternative, server-side validation |
| **building-mcp-server-on-cloudflare** | 3.6K | Deploy MCP servers on Workers — SSE transport, Durable Object state, D1 persistence |
| **agents-sdk** | — | Cloudflare Agents SDK — stateful AI agents with Durable Objects, real-time communication |
| **durable-objects** | — | Durable Objects — strongly consistent state, WebSocket coordination, transactional storage |
| **cloudflare** | — | General Cloudflare platform knowledge — zones, DNS, SSL/TLS, firewall rules |
| **cloudflare-one** | — | Zero Trust platform — Access, Gateway, WARP, browser isolation |
| **sandbox-sdk** | — | Sandbox SDK — isolated execution environments for untrusted code |
| **cloudflare-email-service** | — | Email Workers — programmatic email routing, parsing, and delivery |
| **cloudflare-one-migrations** | — | Zero Trust migration tooling — legacy to Cloudflare One migration patterns |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Cloudflare account** | Free tier available at https://dash.cloudflare.com/sign-up |
| **Wrangler CLI** | `npm install -g wrangler` (or `npx wrangler`) |
| **Node.js 18+** | Required for Workers runtime |
| **Cloudflare API Token** | Create at https://dash.cloudflare.com/profile/api-tokens |

---

## Key Capabilities

### Wrangler CLI
The primary interface for deploying and managing Cloudflare Workers. Covers `wrangler deploy`, `wrangler dev` (local development), `wrangler tail` (live logs), KV namespace management, R2 bucket operations, D1 database migrations, secret management, and environment configuration.

### Workers Best Practices
Production-grade patterns for Cloudflare Workers including error handling with `fetch` event lifecycle, smart caching strategies with Cache API, routing patterns for multi-worker architectures, performance profiling with `wrangler tail`, and cost optimization through request minimization.

### Web Performance
End-to-end web performance optimization using Cloudflare's CDN: automatic image resizing and format conversion (WebP/AVIF), tiered caching strategies, HTTP/3 and 0-RTT configuration, Early Hints for preload/preconnect, and performance budget enforcement.

### MCP Server Deployment
Step-by-step guide for deploying MCP (Model Context Protocol) servers on Cloudflare Workers. Covers SSE transport over Workers, Durable Object-backed state management, D1 for persistent storage, and integration with Claude Desktop and other MCP clients.

### Agents SDK
Build stateful AI agents using Cloudflare's Agents SDK with Durable Objects for session state. Supports WebSocket-based real-time communication, agent-to-agent coordination, and deployment across Cloudflare's global edge network.

---

## Quick Start

```bash
# 1. Install Wrangler CLI
npm install -g wrangler

# 2. Authenticate with Cloudflare
wrangler login

# 3. Add the wrangler skill
npx skills add cloudflare/skills --skill wrangler

# 4. Add Workers best practices
npx skills add cloudflare/skills --skill workers-best-practices

# 5. Deploy your first Worker
npx wrangler init my-agent-worker
cd my-agent-worker
npx wrangler deploy
```

---

## Hermes Integration Notes

- **Deploy MCP servers at the edge:** Use `building-mcp-server-on-cloudflare` to deploy CorpusIQ MCP servers globally with sub-50ms latency
- **Anti-bot for growth operations:** `turnstile-spin` provides CAPTCHA-free bot protection for CorpusIQ landing pages and tools
- **Edge caching for docs:** `web-perf` optimizes corpusiq-docs delivery across Cloudflare's CDN
- **Stateful agent backends:** `agents-sdk` + `durable-objects` enables real-time, stateful agent coordination at the edge
- **Zero Trust security:** `cloudflare-one` secures Hermes agent communication channels with Cloudflare Access

---

## Links

- **skills.sh:** https://skills.sh/cloudflare/skills
- **GitHub:** https://github.com/cloudflare/skills
- **Cloudflare Docs:** https://developers.cloudflare.com
- **Workers Docs:** https://developers.cloudflare.com/workers
