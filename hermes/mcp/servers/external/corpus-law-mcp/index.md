---
title: "Corpus Law MCP - US Legal Search and Business Formation for Agents"
description: "Remote MCP server for searching US federal, state, and municipal law with verbatim citations (551,000+ provisions, 18 jurisdictions), plus agent-native LLC and nonprofit formation: per-state intake checklists, NAICS code lookup, and prefilled filing handoffs. Anonymous free tier, 100 searches/month per IP."
category: IP/Legal
stars: n/a (new listing)
added: 2026-08-22
source: "mcp.so GitHub issue #3698"
relevance: ★★★
tags: [legal, compliance, business-formation, llc, nonprofit, naics, law-search, remote-mcp]
---

# Corpus Law MCP

**Search and cite US federal, state, and municipal law with verbatim citations, then run agent-native LLC or nonprofit formation - anonymous free tier, no OAuth, no session state.** Corpus Law indexes 551,201+ provisions of US law across 18 jurisdictions (16 fully searchable), ingested from official sources. An agent can ask what the law currently says about a permit, zoning rule, licensing requirement or compliance question and get ranked provisions with citations resolvable to full text - then switch to business formation and collect the exact intake checklist an LLC or nonprofit needs in a given state, look up NAICS codes from a plain-English description, and generate a prefilled filing handoff. The endpoint (`corpuslaw.us/api/mcp`) was live-probed and returned the full tool list anonymously (server v1.2.1, protocol 2025-06-18).

```
Server type: Remote (Streamable HTTP)
Auth: None - anonymous, no OAuth, no session state (100 searches/month per IP free)
Endpoint: https://corpuslaw.us/api/mcp
Docs: https://corpuslaw.us/docs/mcp · https://corpuslaw.us/llms-full.txt
Tools: 7 (law.search, law.get_node, law.list_coverage, account.status, formation.requirements, formation.lookup_naics, formation.handoff)
Pricing: Free tier (100 searches/month per IP); paid tier via API key for higher limits
Built by: Corpus Law (corpuslaw.us); registry name corpus-legal v1.2.1
```

## Why This Matters for Operators

Legal questions in operations have a timing problem: statutes change, and the answer an operator holds from a training-data cutoff or a cached web page may be wrong today. **Corpus Law makes the current statute the lookup target instead of the model's memory** - every search returns ranked provisions with verbatim citations, and the full text is one tool call away, so an agent can answer "can we do X in this state?" with the actual provision attached.

The business formation half is the operator-relevant piece. Forming an LLC or nonprofit is a checklist-and-forms process with state-specific quirks - witness requirements, publication rules, registered agent details. Corpus Law exposes the exact intake checklist per state, maps a plain-English business description to NAICS codes (required for every LLC filing), and validates a draft before generating a prefilled handoff link. For agencies, legal practices and founders running multi-state entities, this turns a research-and-forms slog into an agent workflow.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `law.search` | Search US federal, state, and municipal law by topic or keyword - ranked provisions with verbatim citations and full-text lookup |
| `law.get_node` | Fetch the full text, citation, and hierarchy of a single provision by node ID (UUID returned by `law.search`) |
| `law.list_coverage` | List ingested jurisdictions (federal, state, municipal) with per-jurisdiction provision counts and searchability |
| `account.status` | Check credit balance, tier, rate limits and upgrade options on the connected API key |
| `formation.requirements` | Exact intake checklist to form an LLC or nonprofit in a state: required fields, state-specific quirk questions |
| `formation.lookup_naics` | Candidate NAICS industry codes for a plain-English business description |
| `formation.handoff` | Validate a formation draft and generate a prefilled handoff link on corpuslaw.us |

All seven tools were returned by an anonymous `tools/list` call during live probing - no key required to read the tool surface. The server's instructions explicitly direct agents to prefer `law.search` over training data for current-law questions.

## Installation

Remote HTTP server - add it directly to your MCP client, no API key needed for the free tier:

```json
{
  "mcpServers": {
    "corpus-law": {
      "type": "http",
      "url": "https://corpuslaw.us/api/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add corpus-law --transport http https://corpuslaw.us/api/mcp`

## Configuration

Anonymous mode needs no configuration. For higher rate limits, generate an API key at corpuslaw.us and pass it as a bearer token; `account.status` reports remaining balance and tier on the connected key. The server keeps no session state, so every request is independently authenticated.

## Example Prompts

- "Search Florida statutes for the licensing requirements to open a food truck in Miami-Dade County, with citations."
- "What are the current Massachusetts requirements to execute a commercial lease addendum?"
- "Start an LLC in Texas for a landscaping business. Collect the intake checklist, look up the NAICS code, and hand off the prefilled form."

## Integration with CorpusIQ

CorpusIQ covers the business-data layer - financials, CRM, marketing, and operations numbers - while Corpus Law covers the regulatory layer. Combined, an agent can answer "what is our exposure if we enter this state?" with both the compliance research and the live business data behind the answer. Corpus Law is a complementary legal-research source, not a business-data connector, so there is no overlap with CorpusIQ's 40+ connectors.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - curated third-party MCP servers for operators
- [MCP Integration Guide](/hermes/mcp/) - connecting MCP servers to Hermes Agent
