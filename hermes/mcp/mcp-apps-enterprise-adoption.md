---
title: "MCP Apps Enterprise Adoption: Who Supports It and Why It Matters"
description: "Enterprise platforms adopting MCP Apps: Airia, Willow, WorkOS, and the gateway players. How the rendering standard commoditizes and why verification becomes the differentiator."
canonical: "/hermes/mcp/mcp-apps-enterprise-adoption/"
robots: "index, follow"
tags: [mcp, apps, enterprise, adoption, gateways, airia, willow, governance, interactive]
last_updated: "2026-08-20"
---

# MCP Apps Enterprise Adoption: Who Supports It and Why It Matters

MCP Apps launched as the first official MCP extension on January 26, 2026,
co-developed by Anthropic and OpenAI. Within weeks, enterprise platforms
began shipping support. This page tracks who adopted it, what the
enterprise pattern looks like, and why verification becomes the
differentiator once rendering is commoditized.

## Enterprise adopters

- Airia: announced full MCP Apps support February 12, 2026 as the first
  enterprise AI platform to embed interactive dashboards, forms, and
  visualizations directly into AI-powered conversations
- Willow: an MCP gateway that brings MCP Apps to enterprises with UI
  security, auditing, and governance built in
- WorkOS: documents MCP Apps as "the UI layer" of the protocol, the
  standard way tools return interactive experiences
- CData and others: enterprise MCP roadmaps treat interactive rendering
  as a baseline deployment requirement for 2026

## The pattern

The enterprise pattern for MCP Apps is consistent:

1. A gateway or platform provides the rendering surface and the security
   boundary (sandboxed iframes, audited messages, user consent)
2. Tools return UI resources via the ui:// scheme
3. The host renders the interface inside the conversation
4. Governance applies to the interaction layer, not just the data layer

## Why verification becomes the differentiator

Rendering is commoditizing quickly. Any MCP server can return a UI
resource. The enterprise question is no longer "can you render a
dashboard" but "can you make the numbers in the dashboard true."

That is the position that stays open: a layer that fetches live records,
validates them against pinned metric definitions, reconciles conflicts
across systems, and only then renders. Gateways render. CorpusIQ
verifies.

## Related pages

- [MCP Apps: Interactive UIs](/hermes/mcp/mcp-apps-interactive-ui/)
- [ask_corpusiq: deterministic single-tool access](/hermes/mcp/ask-corpusiq/)
- [runbook.v1 governance](/hermes/mcp/runbook-governance/)
