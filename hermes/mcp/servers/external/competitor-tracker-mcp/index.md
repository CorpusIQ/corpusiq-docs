---
title: "Competitor Tracker & Co. MCP — Integration Guide"
description: "Agentic competitor intelligence — ~50 tools for tracking competitor pricing, product, messaging, and corporate changes via weekly crawls, exposed as MCP"
category: mcp
tags: [mcp-server, competitive-intelligence, competitor-tracking, market-research, growth-operations, hermes-agent]
last_updated: 2026-08-10
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/competitor-tracker-mcp/"
robots: "index,follow"

---

# Competitor Tracker & Co. MCP — Agentic Competitive Intelligence

**Rating:** ★★★ | **Category:** Growth & Market Intelligence | **Transport:** Streamable HTTP

## What It Does

Competitor Tracker & Co. watches your competitors' websites and tells you what changed. Every week it crawls their pricing, product, messaging, and corporate pages, detects the changes that matter, and files a tagged, ranked dossier. The MCP server puts that same intelligence inside your AI assistant — subscribe to competitors, read the change feed, and pull page snapshots without leaving chat.

## Why Business Operators Need This

Competitive intelligence typically lives in a separate dashboard you check quarterly. Competitor Tracker & Co. makes it an agent-native capability: ask "what changed across my competitors this week?" and get a ranked answer with specific page snapshots showing before/after. For growth operators, product managers, and founders, this means competitive awareness becomes continuous and conversational — not a quarterly research project. ~50 tools covering reads, writes, and destructive operations with confirm-gates for safety.

**Competitive landscape:** The only MCP server purpose-built for competitive website intelligence. Closest analog is Competitor Tracker & Co.'s own web dashboard; this MCP server brings that data into agent workflows. Not a traditional SEO tool (Ahrefs, SEMrush) — focuses on website change detection, not keyword rankings.

## Quick Start

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **Endpoint** | `https://mcp.competitortracker.io/mcp` |
| **Authentication** | OAuth (sign in on first tool call) or `X-API-Key` header |
| **Tools** | ~50 (read, write, destructive with confirm gates) |
| **GitHub** | `CofounderGPT/competitor-tracker-mcp` (0★, created Jul 15, 2026) |

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "competitor-tracker": {
      "transport": "http",
      "url": "https://mcp.competitortracker.io/mcp"
    }
  }
}
```

### Claude Code

```bash
claude mcp add --transport http competitor-tracker https://mcp.competitortracker.io/mcp
```

### Headless / Automated (API Key)

```json
{
  "mcpServers": {
    "competitor-tracker": {
      "transport": "http",
      "url": "https://mcp.competitortracker.io/mcp",
      "headers": {
        "X-API-Key": "ct_your_key_here"
      }
    }
  }
}
```

## Key Tools

The server exposes ~50 tools across three permission tiers:

### Read Tools (No Confirm Required)

| Tool | Description |
|------|-------------|
| `list_competitors` | List all competitors your organization tracks |
| `get_competitor` | Fetch one competitor's details, categories, and labels |
| `get_competitor_timeline` | Chronological activity for a competitor |
| `list_org_changes` | Organization-wide change feed with filters |
| `list_competitor_changes` | Changes for a single competitor |
| `get_snapshot` | Retrieve a snapshot with HTML, markdown, and screenshot assets |
| `list_snapshots` | List snapshots for a tracked page |
| `list_snapshot_changes` | Changes attributed to a specific snapshot |
| `list_pages` | List tracked pages, optionally filtered by type |
| `get_balance` | Coin balance and renewal summary |

### Write Tools

| Tool | Description |
|------|-------------|
| `subscribe_competitor` | Start tracking a competitor by URL |
| `update_competitor` | Change display name or tracked categories |
| `create_label` / `update_label` | Manage labeling system |
| `assign_label` / `unassign_label` | Apply/detach labels from competitors |
| `mint_api_key` | Generate new API keys with scopes |
| `create_webhook` | Register webhook endpoints for change notifications |
| `create_dispatch` | Create notification with label scoping |

### Destructive Tools (Require `confirm: true`)

| Tool | Description |
|------|-------------|
| `unsubscribe_competitor` | Stop tracking a competitor |
| `delete_label` | Remove a label from all competitors |
| `revoke_api_key` | Disable an API key permanently |
| `delete_org` | Delete the organization (owner only) |

Full tool catalog: [competitortracker.io/docs/mcp/tools](https://competitortracker.io/docs/mcp/tools/)

## Example Usage

### Weekly Competitive Brief

Ask your agent: *"What changed across our competitors this week?"*

The agent calls `list_org_changes` with a date filter, returns ranked changes with page snapshots, and synthesizes a brief — pricing moves, new product pages, messaging shifts.

### Subscribe to a New Competitor

Ask your agent: *"Start tracking acme.com — pricing and product pages."*

The agent calls `subscribe_competitor` with the URL and category filters. Weekly crawls begin automatically.

### Pull a Pricing Page Snapshot

Ask your agent: *"Show me what Competitor X's pricing page looks like right now."*

The agent calls `get_snapshot` for the pricing page, returning HTML, markdown, and screenshot.

## Pricing

Competitor Tracker & Co. operates on a coin-based system. Coins cover competitor subscriptions, page tracking, and snapshot retrieval. Check [competitortracker.io](https://competitortracker.io) for current pricing.

## Repository & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | [github.com/CofounderGPT/competitor-tracker-mcp](https://github.com/CofounderGPT/competitor-tracker-mcp) |
| **Website** | [competitortracker.io](https://competitortracker.io) |
| **Docs** | [competitortracker.io/docs/mcp](https://competitortracker.io/docs/mcp/) |
| **Demo** | [competitortracker.io/demo/agent](https://competitortracker.io/demo/agent/) |
| **MCP Endpoint** | `https://mcp.competitortracker.io/mcp` |

## Verdict: ★★★ — Essential for Growth & Product Operators

Competitor Tracker & Co. is the first MCP server that makes competitive website intelligence an agent-native capability. For any operator running product or growth through AI agents, this removes the context-switch between "working in your agent" and "checking what competitors are doing." The ~50-tool surface with read/write/destructive tiers and confirm gates shows mature API design.

**Strengths:** ~50 tools covering full CI workflow, OAuth + API key auth, confirm-gated destructive operations, weekly automated crawls, page snapshots with HTML/markdown/screenshots, webhook support for programmatic alerts.

**Limitations:** Brand new (0 stars, created Jul 2026), coin-based pricing unclear at free tier, relies on website crawling (JavaScript-heavy sites may produce incomplete snapshots), no social media or ad monitoring (website-only).

**Best for:** Founders, product managers, growth operators, and competitive intelligence teams who want competitor monitoring integrated into their AI agent workflows rather than a separate dashboard.
