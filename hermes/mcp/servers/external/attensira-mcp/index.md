---
title: "Attensira MCP - AI-Search Visibility Data for Agents"
description: "Attensira MCP connects AI assistants to Attensira workspace data over Streamable HTTP with OAuth 2.1 or a workspace-scoped API key. 33 tools across eight groups cover AI-search visibility analytics, prompt and competitor management, automations, inbox tasks and memory, with answer receipts and citation timelines. Endpoint mcp.attensira.com/mcp."
category: SEO
stars: n/a (new listing)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + vendor docs at mcp.attensira.com"
relevance: ★★★
tags: [ai-search, visibility, seo, analytics, marketing, oauth, remote-mcp, streamable-http]
---

# Attensira MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or workspace API key)** - the agent interface for Attensira, an AI-search visibility platform. Instead of switching to a dashboard to read which AI assistants mention a brand, an operator asks the same assistant that holds the numbers: query share of voice, compare windows, find prompts where a competitor appears and you do not, then add the missing prompts in the same conversation. 33 tools across eight groups, 17 read-only.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (interactive clients) or workspace-scoped static API key (headless callers)
Endpoint: https://mcp.attensira.com/mcp
Health: https://mcp.attensira.com/healthz (unauthenticated reachability check)
Tools: 33 across 8 groups (17 read-only, 3 destructive, 3 credit-spending)
Pricing: Workspace plan (credit-based for automations, prompt additions and ask)
Category: SEO
Built by: Attensira (attensira.com)
```

## Why This Matters for Operators

AI-search visibility is the metric every brand now tracks but almost no one acts on in real time. Attensira MCP closes the loop between noticing and changing: an operator editing a pricing page can ask which AI prompts mention a competitor and not the brand, then add three prompts covering the gap without leaving the conversation. The receipts behind every number (`answer_history`, `answer_slice`, `citation_timeline`) mean the visibility data is auditable, which is what makes it safe to act on inside a review cycle.

## Tools & Capabilities

| Group | Tools |
|---|---|
| Find and measure | `search`, `get_analytics`, `deciding_sources`, `win_plan`, `get_prompt`, `get_page` |
| Receipts | `answer_history`, `answer_slice`, `citation_timeline`, `page_history` |
| Track | `add_prompts`, `remove_prompt`, `add_competitor`, `remove_competitor` |
| Inbox | `list_inbox`, `resolve_inbox_task`, `approve_work_item`, `decline_work_item` |
| Automations | `list_automations`, `get_automation`, `create_automation`, `run_automation`, `delete_automation`, `update_automation` |
| Agent | `ask`, `get_session` |
| Account | `get_account`, `get_brief`, `get_ai_traffic_install`, `connect_github`, `update_settings` |
| Memory | `record_observation`, `write_skill` |

Destructive tools: `remove_prompt`, `remove_competitor`, `delete_automation`. Credit-spending tools: `add_prompts`, `run_automation`, `ask`. Every tool takes an optional `project` parameter, so one connection reaches every workspace an organization owns (an agency running three domains connects once).

## Installation

```bash
claude mcp add attensira --transport http https://mcp.attensira.com/mcp
```

Add the URL as a custom connector in Claude, Cursor, VS Code, Codex or ChatGPT and complete the browser OAuth sign-in. For headless callers (n8n, CI, scheduled scripts), mint a static key in Settings, Developer and attach it as the bearer Authorization header; those keys do not expire.

## Configuration

```json
{
  "mcpServers": {
    "attensira": {
      "url": "https://mcp.attensira.com/mcp"
    }
  }
}
```

Treat either credential as a workspace credential: an OAuth connection always carries write, and a read-write API key can delete prompts, competitors and automations plus spend credits. A 16-capability REST API is available for code-first integrations with the same key.

## Business Relevance

- **Marketing teams** pull share-of-voice windows, verify whether deltas are statistically real, and close prompt gaps in one assistant session.
- **Agencies** manage multiple client domains from one connection via the `project` parameter.
- **Product teams** track which prompts cite the product and which cite competitors before writing release notes.
- **SEO leads** get AI-traffic install data and citation timelines instead of dashboard screenshots.

## Integration with CorpusIQ

Attensira measures what AI assistants say about a business; CorpusIQ measures what is happening inside it. A CorpusIQ agent preparing a monthly growth report can pull Attensira share-of-voice via `get_analytics` and combine it with CorpusIQ revenue and funnel data in the same analysis, then use `add_prompts` to act on the visibility gaps it finds. The `citation_timeline` receipts give both platforms a common, auditable evidence model.

## Limitations

- New listing: no third-party track record, no public GitHub repo for the server itself.
- Write access is broad - destructive and credit-spending tools are one bad prompt away; scope keys read-only where possible.
- Credit costs for `add_prompts`, `run_automation` and `ask` are workspace-metered, not published in the docs.
- Streamable HTTP only; stdio-only clients need a bridge.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [CiteRank MCP - AI Search Visibility & GEO Audits for AI Agents](/hermes/mcp/servers/external/citerank-mcp)
- [SEOVally MCP - Scoped SEO and AI-Search Audits for Agents](/hermes/mcp/servers/external/seovally-mcp)
