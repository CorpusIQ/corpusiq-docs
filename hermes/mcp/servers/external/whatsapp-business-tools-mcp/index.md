---
title: "WhatsApp Business Tools MCP (Official) - Integration Guide"
description: "Meta's remote MCP server for the WhatsApp Business Platform: onboard numbers, manage templates, configure webhooks, and send messages from an AI agent."
status: "Official (Meta-hosted, beta)"
transport: Remote MCP
auth: OAuth (per-business sign-in)
category: Messaging and Customer Communication
added: 2026-09-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/whatsapp-business-tools-mcp/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# WhatsApp Business Tools MCP (Official) - Integration Guide

## Overview

Meta's remote MCP server for the WhatsApp Business Platform (Cloud API), announced September 15, 2026 and rolling out gradually. It lets an AI agent act on the apps and businesses you administer: discover businesses and WhatsApp accounts, onboard and register phone numbers, create and manage message templates, configure webhooks, and send messages.

Remote endpoint: `https://mcp.facebook.com/whatsapp_business_tools`

## What it can do

- Discover the businesses and WhatsApp accounts you administer
- Onboard and register phone numbers
- Create and manage message templates
- Configure webhooks
- Send messages

## Requirements

- A WhatsApp-enabled app you are an admin of (WhatsApp Business Messaging use case), connected to the business. Admin access on the app itself is required, not only on the business.
- Accepted WhatsApp Business Cloud API Terms of Service for that business. Messaging and number registration are blocked until an admin accepts.

## Connecting

Any client that supports remote MCP servers can connect to the endpoint directly. For clients that only support local (stdio) servers, Meta documents using the `mcp-remote` bridge to proxy the remote server over stdio.

## Availability notes

- Beta: Meta states the interface and tool set may change, and the server is rolling out gradually, so it may not be available on every account yet.

## Why operators care

WhatsApp Business setup (number registration, template approvals, webhook wiring) is normally a dashboard slog across Business Manager screens. This server puts that work into the same agent conversation where the rest of the stack is managed.

## See also

- [WhatsMCP MCP](/docs/hermes/mcp/servers/external/whatsmcp-mcp) - third-party WhatsApp numbers for AI agents.
- [Meta Ads MCP (Official)](/docs/hermes/mcp/servers/external/meta-ads-mcp-official) - Meta's ads server.
