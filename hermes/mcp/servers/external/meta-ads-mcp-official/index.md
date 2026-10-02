---
title: "Meta Ads MCP (Official) - Integration Guide"
description: "Meta's first-party remote MCP server for ads: campaign reporting, ad and catalog management, signals, and A/B tests from any MCP-compatible AI agent."
status: "Official (Meta-hosted, open beta)"
transport: Remote MCP
auth: OAuth (Facebook Login for Business) or pre-obtained token
category: Advertising and Marketing
added: 2026-09-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/meta-ads-mcp-official/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# Meta Ads MCP (Official) - Integration Guide

## Overview

Meta's first-party ads MCP server, remote-hosted at `https://mcp.facebook.com/ads`. It launched in open beta on April 29, 2026, and on September 22, 2026 Meta opened it to any developer with their own Meta app: platforms and tools can now connect their users to Meta ads capability directly, instead of writing and maintaining custom Marketing API integration code.

It is part of Meta's ads AI connectors family (the MCP server plus an ads CLI) and is free during the open beta.

## What it can do

The server exposes 29 tools grouped into seven categories:

| Category | What you can do |
| --- | --- |
| Comprehensive reporting | Pull detailed campaign performance and account insights |
| Ad creation and management | Create and edit ads, ad sets, and campaigns |
| Catalog creation and management | Create catalogs, add product data, troubleshoot feeds |
| Signals and datasets | Check signal health and quality to prioritize setup work |
| Help and troubleshooting | Search Meta Business Help Center articles |
| A/B tests and conversion lift | Create and manage tests and lift studies |
| Activity logs | Review ad account change history |

## Authentication and access

- OAuth via Facebook Login for Business handles tokens automatically, or you can pass a pre-obtained access token.
- Read and Manage scopes are granted per Meta account settings and can be revoked at any time.
- If you manage data on behalf of other businesses (agency or platform use), Meta requires app review for Advanced Access on the `ads_mcp_management` permission.
- Ads MCP server rules let admins define what an agent can and cannot do on a given ad account or catalog.

## Availability notes

- Open beta: free during beta, with no published rate limits at launch.
- Phased rollout: some ad accounts are still waitlisted for the connector.
- Clients validated by Meta: Claude Desktop, Claude Code, ChatGPT (Web), Codex (app and CLI), and Cursor (app and CLI).

## Why operators care

Instead of a manual sweep through Ads Manager, questions like "which ad set has the highest return this week" become a single conversation, with the agent working through Meta's structured, permission-scoped tools instead of screen scraping.

## See also

- [Meta Ads MCP (Pipeboard)](/hermes/mcp/servers/external/meta-ads-mcp) - a popular third-party alternative with a Meta Business verification badge.
- [Markifact Meta Ads MCP](/hermes/mcp/servers/external/markifact-meta-ads-mcp) - approval-gated campaign drafting.
- [Ryze Meta Ads MCP](/hermes/mcp/servers/external/ryze-meta-ads-mcp) - third-party read and write ads workflows.
