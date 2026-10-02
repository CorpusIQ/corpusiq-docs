---
title: CTlogs.io MCP - Certificate Transparency Search for Agents
description: Hosted MCP server that puts the Certificate Transparency record inside an AI assistant. Five read-only tools search subdomains, certificate history and hostname keywords across public CT logs for security, brand protection and infrastructure work. OAuth browser sign-in with no key to copy, operated by Lyalpha GmbH.
category: Security
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [certificate-transparency, subdomains, security, brand-protection, reconnaissance, oauth, remote-mcp]
---

# CTlogs.io MCP

**Remote MCP server (Streamable HTTP)** - the Certificate Transparency index, queryable from a conversation. Agents ask which subdomains a domain has, who issued the certificate on a hostname and when it expires, and whether a brand name appears in any logged hostname. Read-only by design; five tools, OAuth browser sign-in, no key to copy.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser sign-in (no key); endpoint 401-verified live in this sweep
Endpoint: https://mcp.ctlogs.io/mcp
Tools: 5 (find_subdomains, lookup_certificates, search_hostnames, index_status, account_quota)
Operator: Lyalpha GmbH, Dusseldorf (ABTdomain.com technology)
```

## Why This Matters for Operators

Certificate Transparency logs are the public record of every TLS certificate ever issued - and most operators never look at them. The logs answer questions that matter operationally: what subdomains does this acquisition target actually run, which CA issued the cert on our API host, when does it expire, and is someone standing up lookalike hostnames with our brand in them. **CTlogs makes those questions conversationally askable instead of requiring CT-log APIs and certificate parsers.**

The impersonation and typosquat angle is the growth-adjacent use: `search_hostnames` finds any logged hostname containing a word, so a brand owner can hunt for phishing infrastructure that reused the brand name before abuse reports arrive.

## Tools & Capabilities

| Tool | The question it answers |
|---|---|
| `find_subdomains` | Which subdomains of a domain exist in the record, and when each was last seen |
| `lookup_certificates` | Certificate history of one hostname, or the certificate behind a fingerprint |
| `search_hostnames` | Which hostnames contain a word - impersonation and typosquat hunting |
| `index_status` | How large and how fresh the index is |
| `account_quota` | How much of the plan allowance is left |

Every tool is read-only - nothing the assistant calls changes anything. The service is built for asking, not bulk export (the REST API covers bulk).

## Installation

```bash
claude mcp add --transport http ctlogs https://mcp.ctlogs.io/mcp
```

Then run `/mcp` inside Claude Code to complete the browser sign-in. The client opens CTlogs, the operator signs in and approves the connection once - no key to copy, nothing in the config file.

## Configuration

```json
{
  "mcpServers": {
    "ctlogs": {
      "url": "https://mcp.ctlogs.io/mcp"
    }
  }
}
```

One account serves every client (laptop, editor, server) with usage counted once. Plans and allowances are on the pricing page; results are sized for conversation.

## Business Relevance

- **Brand protection** hunts lookalike hostnames and phishing infrastructure continuously.
- **Infrastructure teams** audit which certificates and CAs cover their hosts and when they expire.
- **Due diligence** maps an acquisition target's real subdomain footprint from public logs.
- **Security research** traces certificate issuance history by hostname or fingerprint.

## Integration with CorpusIQ

CorpusIQ's data connectors answer "what is the business doing"; CTlogs answers "what is the domain footprint behind it". A CorpusIQ agent researching a company can pair financial context with CT-log evidence of its infrastructure - the same pairing brand-protection workflows use to connect a phishing domain to the actor behind it.

## Limitations

- New service (repo created Sep 2, 2026); plans and limits are still settling per the pricing page.
- CT data shows which names had certificates issued, not whether a host is live or what it serves.
- Conversation-sized results by design; bulk work requires the REST API.
- No personal-information lookups - queries are domain, hostname, fingerprint or word-in-hostname only.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [EuroDNS MCP - Domain, DNS and SSL Registrar Operations](/hermes/mcp/servers/external/eurodns-mcp)
- [Bug Bounty Intelligence MCP - Smart Contract Security Analysis](/hermes/mcp/servers/external/bug-bounty-intelligence-mcp)
