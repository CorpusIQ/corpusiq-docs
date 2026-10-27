---
title: "Epovest MCP: AI Visibility Measurement for Businesses"
description: "Official hosted MCP server for Epovest - measure how AI assistants answer your market's questions, which sources they cite, and the levers that shape those answers. Canon management, tracker results, response archives, surface checklists, source atlas and corroborations. OAuth 2.1 PKCE or API key."
category: SEO
stars: n/a (hosted; repo 0 stars)
added: 2026-08-23
source: "mcpservers.org /all + GitHub README"
relevance: ★★★
tags: [geo, aeo, ai-visibility, ai-search, citation-tracking, brand-monitoring, remote-mcp]
last_updated: "2026-10-24"
---

# Epovest MCP

**The official MCP server for Epovest, the platform that lets businesses make AI assistants recommend them - measuring how the engines answer the questions your market actually asks, which sources they cite, and giving you the levers that shape those answers.** Hosted, nothing to install: point your MCP client at the endpoint and your assistant gets the same tools the Epovest app itself is built on. Every tool acts on the account that owns the key.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: OAuth 2.1 with PKCE, or API key as Bearer token
Endpoint: https://mcp.epovest.com/mcp
Official registry: com.epovest/ai-visibility
Agent docs: epovest.com/docs/api.md
Category: SEO / GEO / AEO
Built by: Epovest
```

## Why This Matters for Operators

AI engines are becoming the front door to customers, but almost nobody can answer the question "what does ChatGPT actually say about us?" Epovest closes that gap with measurement instead of guesswork: trackers run your market's real questions against the engines on a schedule, every answer is archived with its cited sources and dates, and results come back as score series you can watch move. When a competitor's page starts getting cited instead of yours, you see it in the series instead of discovering it six months later in lost pipeline.

The workflow is built for operators who want leverage, not just monitoring. The Canon is a versioned reference text your brand keeps stable, and every answer is measured against it. Corroborations capture what third parties say about you, so you can build the citation graph engines actually use. And the surface checklists turn "improve our AI visibility" into a tickable list your assistant can execute.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Canon (reference text) | `list_projects`, `create_project`, `update_project_canon` |
| Tracking (measurement) | `list_trackers`, `create_tracker`, `update_tracker`, `start_tracker`, `pause_tracker`, `get_results` (score series), `get_responses` (raw engine answers) |
| Keyword discovery | `list_keyword_discoveries`, `accept_keyword_discovery`, `dismiss_keyword_discovery`, `restore_keyword_discovery` |
| Surfaces (your pages) | `list_surfaces`, `create_surface`, `update_surface`, `tick_surface_checklist`, `mark_surface_aligned`, `delete_surface`, `restore_surface` |
| Atlas (source map) | `list_sources`, `get_source` |
| Corroborations (third-party) | `list_corroborations`, `create_corroboration`, `update_corroboration` |

## Installation

```bash
claude mcp add epovest --transport http https://mcp.epovest.com/mcp
```

First connect triggers the OAuth flow; API key as Bearer token is supported for key-based clients. The vendor publishes a machine-readable agent reference at epovest.com/docs/api.md.

## Configuration

```json
{
  "mcpServers": {
    "epovest": {
      "type": "http",
      "url": "https://mcp.epovest.com/mcp"
    }
  }
}
```

## Business Relevance

- **Marketing leaders** get a measurable answer to "are the AI engines recommending us" with score series, raw answers and citations instead of anecdotes.
- **SEO/GEO teams** run the questions their market asks, see which sources win, and get keyword discoveries the measurement itself suggests.
- **Brand and comms teams** track how third parties describe the company across the sources engines listen to.
- **Product marketers** keep a versioned brand Canon that every answer is measured against, so positioning stays consistent everywhere AI answers appear.
