---
title: Honest Elf MCP - Texas Court E-Filing for Agents
description: "Remote MCP server letting an AI agent prepare, submit and track Texas court e-filings through a certified Electronic Filing Service Provider."
category: Legal
stars: n/a (hosted service, honestelf.com)
added: 2026-10-01
source: "mcpservers.org /all (www-honestelf-com-docs-mcp)"
relevance: ★★
tags: [legal, e-filing, courts, texas, compliance, legal-ops, remote-mcp]
---

# Honest Elf MCP

**Court filings an agent can prepare while a human approves.** Honest Elf is a certified Texas Electronic Filing Service Provider, and its MCP server exposes the filing workflow to any MCP-capable client: look up courts and their rules, search the court record, assemble a draft, get a real fee quote, and submit for clerk review after explicit user approval.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with PKCE and dynamic client registration (scope: efile)
Endpoint: https://mcp.honestelf.com/mcp
Tools: 39 (court lookup, case search, filing assembly, fee quotes, submission, tracking)
Pricing: requires a Honest Elf account
Category: Legal
Built by: Zhakhan LLC (Honest Elf)
```

## Why This Matters for Operators

E-filing is a form-heavy, rule-sensitive workflow that benefits from an assistant and is dangerous to hand one without a gate. Honest Elf threads that needle: the agent does the lookup, the drafting and the fee quoting, but submission waits for explicit user approval, and the filing then goes through the same state-mandated Tyler Technologies Odyssey File & Serve pipeline every Texas provider uses. Courts see an ordinary submission from a certified EFSP, reviewed by a clerk like any other.

For a legal-ops team, the value is the assembly work - matching a cause to the right court, resolving its filing rules, building the document set and quoting the fee - moving into the agent while the judgment call stays with the person.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Court lookup | Find Texas courts and their filing rules |
| Case search | Search existing cases in the court record |
| Filing assembly | Build filing drafts with PDF documents |
| Fee quote | Obtain an official fee quote before submitting |
| Submission | Submit for clerk review after explicit user approval |
| Tracking | Track filing outcomes |

The server documents 39 tools; the vendor's reference page publishes the endpoint, transport, auth model and tool categories. The guide describes the capability groups rather than inventing individual tool identifiers.

## Installation

```
claude mcp add --transport http honestelf https://mcp.honestelf.com/mcp
```

Sign in with the Honest Elf account when prompted; the agent then acts on behalf of that signed-in user, within that user's firm and jurisdiction.

## Configuration

```json
{
  "mcpServers": {
    "honestelf": {
      "type": "http",
      "url": "https://mcp.honestelf.com/mcp"
    }
  }
}
```

## Business Relevance

- **Legal-ops and paralegal teams** can move court lookup, rule resolution and draft assembly into the agent while keeping the approval with a person.
- **Small firms without a filing specialist** can quote real fees and prepare a compliant filing set in seconds instead of a manual portal session.
- **Compliance and risk review** can keep submissions behind an explicit approval gate, so an agent never files unreviewed.
- **AI agents** get a jurisdiction-bounded legal workflow with a natural human checkpoint built into the tool design.

## Integration with CorpusIQ

CorpusIQ supplies the business context - matter value, client data, engagement terms from the Finance and CRM connectors - and Honest Elf supplies the filing workflow. An agent can pull a client's engagement details, check the court record through Honest Elf and assemble a draft with the fee quote attached, so the legal step is composed with the business record rather than run in a separate portal.

## Limitations

- Texas courts only, across all Tyler-served e-filing courts; other states are out of scope.
- Requires a Honest Elf account and a certified-EFSP relationship; this is not a keyless public server.
- Submission is gated on explicit user approval by design, so it is not a fully autonomous filing path.
- The public listing describes 39 tools by capability group rather than publishing the full identifier list at catalog time.

## FAQ

### What does the Honest Elf MCP server do?

It lets an AI agent look up Texas courts and their rules, search case records, assemble filings, get official fee quotes and submit e-filings for clerk review after explicit user approval.

### Can an agent file a court document without approval?

No. Submission is gated on explicit user approval; the agent prepares and quotes, the person approves and submits.

### Which courts does it cover?

Texas courts served by the Tyler Technologies Odyssey File & Serve Electronic Filing Manager.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
