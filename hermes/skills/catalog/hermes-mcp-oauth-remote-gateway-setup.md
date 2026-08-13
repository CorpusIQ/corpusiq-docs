---
title: MCP OAuth Remote Gateway — Official Hermes Skill Setup Guide
description: Install and use mcp-oauth-remote-gateway, the official Hermes Agent skill for completing MCP OAuth flows on remote gateways (containers, VPS, bots) where the loopback redirect never reaches the server.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-mcp-oauth-remote-gateway-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# MCP OAuth Remote Gateway — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/mcp-oauth-remote-gateway)
**Repo:** 229K⭐ · **Skill installs:** 1 · **First Seen:** ~August 4, 2026
**Category:** MCP / Authentication / Infrastructure
**Security:** Gen Agent Trust Hub Pass · Socket Pass · Snyk Pass

The official Hermes Agent skill for the most common MCP OAuth failure mode in production deployments. Hermes' built-in MCP OAuth client runs a one-shot HTTP listener on `127.0.0.1:<port>` inside the Hermes process and registers that loopback address as the OAuth `redirect_uri`. That works on a local CLI. It breaks completely on a remote gateway (container, VPS, messaging bot), because the user's browser resolves `127.0.0.1` to their own laptop — the authorization code never reaches Hermes.

This skill performs the OAuth dance by hand and writes the resulting tokens into the exact files Hermes' token storage expects, so a subsequent `/reload-mcp` finds cached tokens and skips the browser flow entirely.

---

## When to Use

Use this skill when **all** of the following are true:

- Hermes runs as a remote gateway — container, VPS, or bot deployment, not a local CLI
- You need to connect an MCP server that requires OAuth 2.0 authorization (Google, GitHub, Slack, etc.)
- The built-in browser flow fails because the loopback redirect never reaches the Hermes process
- You can run the authorization code exchange manually and place tokens in Hermes' token storage

---

## Installation

```bash
# Via skills.sh
npx skills add https://github.com/nousresearch/hermes-agent --skill mcp-oauth-remote-gateway

# Direct from the Hermes Agent repo
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/infrastructure/mcp-oauth-remote-gateway ~/.hermes/skills/
```

---

## How It Works

1. The skill performs the OAuth authorization-code flow manually — outside the Hermes process
2. The redirect URI is registered as a public/remote endpoint (or handled via manual code paste)
3. The exchanged tokens are written into the exact files Hermes' token storage reads
4. `/reload-mcp` is issued; Hermes finds cached tokens and skips the browser flow

The result is identical to a successful local OAuth, but the token files are populated out-of-band.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Remote Hermes gateway | Container, VPS, or messaging-bot deployment |
| OAuth client credentials | Client ID/secret from the MCP server's provider console |
| Redirect URI control | Ability to register a non-loopback redirect URI, or capture the callback code manually |
| Hermes token storage access | Filesystem access to the Hermes profile directory |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Remote gateway OAuth** | Connect OAuth MCP servers when Hermes runs on the DGX Spark or Mac Mini behind a gateway |
| **Bot deployments** | Authorize MCP servers for Telegram-bot-driven Hermes instances |
| **Token seeding** | Pre-seed tokens in images before first boot, skipping interactive auth entirely |
| **Recovery flows** | Re-authorize a server whose refresh token expired without a browser session |

---

## Limitations / Verification

- Manual flow requires comfort with OAuth 2.0 authorization-code mechanics
- Skill is brand new (first seen early August 2026) — pin the install and re-check on Hermes upgrades
- Verify: after placing tokens and running `/reload-mcp`, confirm the MCP server shows as connected with `hermes mcp list` or the in-session MCP status view

---

## Related

- [Discovery Page — Aug 12 OpenClaw Ecosystem Sweep](/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/)
- [MCP Reference](/hermes/mcp/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
