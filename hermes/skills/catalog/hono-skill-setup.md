---
title: "Hono Skill — Edge Web Framework Setup by the Hono Author"
description: "yusukebe/hono-skill — 1 skill, 11.7K installs: inline Hono framework knowledge plus the npx hono request endpoint-testing CLI, authored by Hono's creator."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hono-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "hono", "web framework", "edge", "api"]
---

# Hono Skill — Setup Guide

**Source:** [yusukebe/hono-skill](https://skills.sh/yusukebe/hono-skill)
**GitHub:** [yusukebe/hono-skill](https://github.com/yusukebe/hono-skill)
**Skills:** 1 skill · 11.7K total installs
**Category:** Web Development
**First Seen:** January 21, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟡 Trusted — Snyk Warn on the hono skill (named); Gen Agent Trust Hub Pass and Socket Pass; 157 GitHub stars

Hono is a fast, lightweight web framework for the edge (Cloudflare Workers, Deno, Bun, Node.js), and this skill is authored by its creator, Yusuke Wada (yusukebe). It gives agents inline API knowledge for building Hono applications and teaches the `npx hono request` command, which tests endpoints without starting an HTTP server (using `app.request()` internally). The skill also coordinates with the optional hono-docs MCP server, preferring its tools over the inline reference when configured, and it warns against passing credentials directly in CLI arguments.

---

## Installation

```bash
npx skills add yusukebe/hono-skill
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/yusukebe/hono-skill --skill hono
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer and the `npx hono request` CLI |
| **Optional** | The hono-docs MCP server for live documentation instead of the inline reference |

## What It Provides

- Inline Hono API knowledge for agents: routing, middleware, bindings, and edge deployment patterns
- `npx hono request` endpoint testing without starting a server:
  ```bash
  npx hono request [file] -P /path
  npx hono request [file] -X POST -P /api/users -d '{"name": "test"}'
  ```
- Guidance to use `workers-fetch` when Cloudflare Workers bindings (KV, D1, R2) are required
- Credential hygiene: environment variables for sensitive values, never CLI arguments
- Preference for the hono-docs MCP server tools when configured

## Quick Start

1. Install: `npx skills add yusukebe/hono-skill`
2. Test an endpoint without a server: `npx hono request [file] -P /path`
3. For Workers bindings, use `workers-fetch` instead of `hono request`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Edge API work** | Hono is the standard for lightweight edge APIs — directly relevant to MCP server and connector endpoints |
| **Agent-built services** | Inline framework knowledge means agents scaffold correct Hono apps without web lookups |
| **Fast endpoint testing** | `npx hono request` gives quick route verification during agent builds |
| **Authoritative source** | Skills written by the framework's creator carry canonical patterns |

## Limitations / Verification

- Security audits on the hono skill: Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn (named in the tier)
- Publisher-page total verified (11.7K on the single skill); 157 GitHub stars as of the sweep
- Below the 20K install guide bar — drafted on framework-author authority (Hono's creator is the publisher) and direct relevance to agent-built edge services
- Single-skill cluster; the inline reference is a snapshot and the skill itself defers to the hono-docs MCP server when available

```bash
npx skills add yusukebe/hono-skill   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
