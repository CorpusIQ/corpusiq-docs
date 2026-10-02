---
title: "Legalize MCP - Point-in-Time Legislation with Git Provenance"
description: "Consolidated legislation as data from the Legalize corpus: list countries, search laws, read a law as of any date, and diff reforms between two dates with git SHAs for citation. Seven read-only tools over Streamable HTTP with OAuth 2.1 sign-in."
category: IP/Legal
stars: 0
added: 2026-08-26
source: "mcp.so GitHub issue #3781"
relevance: ★★★
tags: [legal, legislation, compliance, point-in-time, git, oauth, remote-mcp, law]
---

# Legalize MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1) for Legalize - consolidated legislation published as data.** Every law is a Markdown file, every reform a git commit carrying its real publication date, covering every country in the Legalize corpus. The connector exposes seven read-only tools, and the one that matters is `law_at_date`: it answers what a norm said on a given day and returns the git SHA of that version, so the quote can be checked against the public repository rather than taken on trust. `diff_law` returns a unified diff between two dates with both SHAs. The endpoint returns HTTP 401 for anonymous probes, confirming the OAuth gate is live; the tool catalogue is readable without a token at legalize.dev/mcp/tools.json.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration (sign-in required)
Endpoint: https://legalize.dev/mcp
Tools: 7 (all read-only)
Pricing: Allowances listed on legalize.dev/mcp
Category: IP/Legal
Built by: Legalize (registry dev.legalize/legalize)
```

## Why This Matters for Operators

Point-in-time law is the question a search engine cannot answer: what did this regulation say on the date my contract was signed, my incident happened, or my product shipped. Consolidated "law in force today" sources silently rewrite history. Legalize's model - every reform is a commit with its real publication date - makes the temporal question answerable with a verifiable SHA.

**Two honesty properties are enforced by the tools, not just documented.** A date resolves to what was *published* on or before that day, not to what was in force; and a corpus held `as_enacted` rather than consolidated comes back flagged, never passed off as the law in force.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_countries` | Lists the countries Legalize covers and how many laws each one has |
| `search_laws` | Finds a norm by words in its title or by its official number (e.g. '2/2011') inside one country's corpus |
| `get_law` | Reads what a norm says today, full Markdown body or one article with `article=` |
| `law_at_date` | Returns what a norm said on a given day, with the git SHA of that version for citation |
| `diff_law` | Returns a unified diff of a norm between two dates, with both SHAs |
| `reform_history` | Lists which norms amended this law, when, and what each says it touched, newest first |
| `law_stats` | Reports corpus size and movement: how many laws, how many recorded amendments |

## Installation

Add the hosted endpoint and complete the OAuth sign-in flow from your MCP client:

```json
{
  "mcpServers": {
    "legalize": {
      "url": "https://legalize.dev/mcp"
    }
  }
}
```

Website: https://legalize.dev/mcp · Connector repo: https://github.com/legalize-dev/mcp (MIT) · Open corpus & pipeline: https://github.com/legalize-dev/legalize

## Configuration

Authentication is OAuth 2.1 with dynamic client registration - a browser sign-in per client, no long-lived API key to store. The tool catalogue at legalize.dev/mcp/tools.json is readable without a token, so tool schemas can be inspected before signing in. Current plan allowances are listed on legalize.dev/mcp.

## Business Relevance

For compliance work, the `law_at_date` plus SHA pattern converts a legal question into a citable artifact: the agent quotes the norm as of the relevant date and attaches the repository SHA so counsel can verify it independently. For products operating across jurisdictions, `list_countries` plus `search_laws` gives a programmatic map of which regimes are covered and how their corpora move. The `reform_history` tool answers "why did this change and what amended it" without a legal research subscription.

## Integration with CorpusIQ

Legalize complements CorpusIQ's business data with the regulatory layer: an agent can pull operating context (revenue, jurisdictions, contracts) from CorpusIQ connectors and then pin the exact regulatory text that applied at each relevant date. Both surfaces are read-only, and Legalize's SHA-cited outputs fit the same citation-first pattern as CorpusIQ's source-linked answers.

## Limitations

- Sign-in required (OAuth 2.1 with DCR) - no anonymous tier beyond the tools.json catalogue.
- A date resolves to what was *published* on or before that day, not to what was *in force* - a semantic limit of every legislation corpus, surfaced honestly rather than hidden.
- Coverage depends on the Legalize corpus; check `list_countries` for your jurisdictions before committing to the tool.
- Connector repo is brand new (created Aug 26, 2026, 0 stars).

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Corpus Law MCP](/hermes/mcp/servers/external/corpus-law-mcp)
- [Lawstronaut MCP](/hermes/mcp/servers/external/lawstronaut-mcp)
- [Taiwan Law MCP](/hermes/mcp/servers/external/taiwan-law-mcp)
