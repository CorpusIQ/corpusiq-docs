---
title: "Nearius MCP - Verified Spanish and EU Case Law"
description: "Spanish and EU case law for AI agents: 4M+ official documents with verifiable ECLI citations, BOE validity checks and deadline calculation."
category: IP/Legal
stars: n/a (hosted platform, nearius.com)
added: 2026-10-05
source: "mcp.so /feed (Nearius, verified featured listing)"
relevance: ★★
tags: [legal, case-law, spain, eu, ecli, citations, compliance, remote-mcp]
---

# Nearius MCP

**Verified Spanish and European case law for AI assistants.** Nearius serves more than 4 million official legal documents from seven courts (TS, TC, AN, TSJ, AP, TJUE, TEDH) plus the BOE gazette, BORME commercial registry and Catastro, and its pitch is narrow and operator-friendly: every citation that comes back is verifiable. Responses carry ECLI identifiers linked to the official source, referenced articles are checked against the consolidated BOE text for existence and current validity, and judicial deadlines can be calculated. Hosted at `mcp.nearius.com/mcp` with OAuth.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://mcp.nearius.com/mcp
Scale: 4,000,000+ official documents, 7 courts, BOE / BORME / Catastro sources
Tools: 240+ agent tools
Pricing: EUR 29.99 per month, no commitment; on-premise option for data sovereignty
Built by: nearius.com
```

## Why This Matters for Operators

"Ghost case law" is now a real cost of using AI for legal work: courts have sanctioned filings built on invented citations. For companies operating in Spain and the EU, Nearius turns the citation question into a checkable step: each answer arrives with its ECLI and a link to the official source, and article references are validated against the consolidated BOE text, including the version in force at the date of past facts.

That makes it useful for the legal-adjacent work operators actually do: reviewing contracts, preparing compliance positions, and checking that a claim in a document rests on a judgment that exists.

## Tool Surface

240+ tools wrap the document corpus and its verification layers:

| Capability | What it covers |
|---|---|
| Case law search | Judgments across TS, TC, AN, TSJ, AP, TJUE and TEDH |
| Citation verification | ECLI lookup with a link to the official source |
| BOE article checks | Existence, current validity and literal text of referenced articles |
| Temporal validity | The redaction in force at the date facts occurred |
| Deadline calculation | Judicial and procedural deadline maths |
| Registries and gazettes | BOE, BORME and Catastro documents in the same corpus |

## Authentication

OAuth against the vendor account; the endpoint answers unauthenticated requests with a 401 carrying the resource metadata pointer. An on-premise deployment option exists for teams that cannot send data to a hosted service, which the vendor frames as data sovereignty for professional firms.

## Installation

Claude Code:

```bash
claude mcp add nearius --transport http https://mcp.nearius.com/mcp
```

Cursor, VS Code and other clients:

```json
{
  "mcpServers": {
    "nearius": {
      "type": "http",
      "url": "https://mcp.nearius.com/mcp"
    }
  }
}
```

Sign in when the client opens the OAuth flow; the subscription is per account.

## Business Relevance

- **Operators in Spain and the EU** verify legal citations before filings, contracts or compliance documents ship.
- **Legal and compliance teams** run first-pass research with a citation trail they can hand to counsel.
- **Professional firms** that cannot use hosted AI for client data can deploy on-premise.

## Integration with CorpusIQ

CorpusIQ's connectors answer what the business data says; Nearius answers what the law says. Composed, an agent can pull a question from the books or from contracts and check it against verified case law and current BOE article text in one session, with the legal side carrying its own citations. The verification habit maps well onto operators who already require sourced answers from their data connectors.

## Limitations

- The corpus is Spanish and EU focused; other jurisdictions are out of scope.
- The vendor states it is a legal-research support tool and not legal advice; each citation is verifiable, but the tool's promise is verification, not infallibility.
- Pricing is in euro and per month; the on-premise option is a vendor conversation.
- Tool-level detail beyond the published capability groups surfaces at connect time.

## FAQ

### What stops the assistant inventing case citations?

Answers come back with ECLI identifiers linked to the official source, and article references are checked against the consolidated BOE text, so a citation can be verified rather than trusted.

### Does it cover past versions of the law?

Yes. Temporal validity retrieval returns the redaction in force at the date of the facts, not only the current text.

### Is there a way to keep data off hosted infrastructure?

Yes. The vendor offers an on-premise deployment for data sovereignty.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [TaiLexi AI MCP - Taiwan Legal Research for Agents](/hermes/mcp/servers/external/tailexi-mcp/)
- [CourtListener MCP - US Legal Research for Agents](/hermes/mcp/servers/external/courtlistener-mcp/)
- [Lawstronaut MCP - Global Legal & Regulatory Document Access for AI Agents](/hermes/mcp/servers/external/lawstronaut-mcp/)
