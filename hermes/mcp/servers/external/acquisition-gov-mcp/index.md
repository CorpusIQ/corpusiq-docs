---
title: "Acquisition.gov MCP: FAR Overhaul and Agency Deviations"
description: "Deterministic read-only MCP access to official Acquisition.gov FAR Overhaul model-part pages, the posted agency-deviation index, official deviation PDFs, and a allowlisted set of RFO guidance resources. Five stdio tools return source text with canonical URLs, retrieval timestamps, SHA-256 content hashes and extraction warnings. uvx install, no credentials, MIT licensed, published by 1102tools-dev."
category: Compliance
stars: n/a (new listing)
added: 2026-08-24
source: "chatmcp/mcpso issue #3720"
relevance: ★★★
tags: [government, procurement, far, acquisition, compliance, stdio, federal-contracting]
---

# Acquisition.gov MCP

**Read-only, deterministic MCP access to the official Acquisition.gov FAR Overhaul model-part pages, posted agency-deviation documents, and RFO guidance resources.** Published by `1102tools-dev` as `com.1102tools/acquisition-gov-mcp` (v1.0.2 on PyPI), the server reports source text and metadata without deciding which rule governs a procurement. Model deviation text is never treated as operative for an agency that lacks a posted deviation, and every retrieved source carries its canonical URL, UTC retrieval time, SHA-256 content hash, extraction status, and warnings.

```
Server type: stdio (Python, local install)
Auth: None (read-only, no credentials)
Install: uvx acquisition-gov-mcp==1.0.2
Registry: com.1102tools/acquisition-gov-mcp (official MCP registry)
Repo: github.com/1102tools-dev/federal-contracting-mcps (MIT, 20 stars, Apr 2026)
Tools: 5 verified (list_rfo_parts, get_rfo_part, list_rfo_agency_deviations, get_rfo_agency_deviation, get_rfo_guidance)
```

## Why This Matters for Operators

FAR Overhaul is restructuring the Federal Acquisition Regulation into a new model-part framework, and agencies are posting deviations that override model text on a rolling basis. An operator bidding on federal contracts, or a compliance team supporting one, must know which text applies to which agency on which date. Acquisition.gov MCP makes that answer deterministic and citable: an agent can pull the current model part, check the posted deviation index for a specific agency, and read the deviation PDF itself, each with a content hash and canonical URL to back the answer. No more guessing from outdated PDF exports.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_rfo_parts(part?, agency?, updated_since?)` | Lists FAR Overhaul model parts with official source dates and matching posted-deviation counts |
| `get_rfo_part(part, section?, cursor?, max_characters?)` | Retrieves parsed, paginated model text for one FAR part |
| `list_rfo_agency_deviations(agency?, part?, limit?)` | Discovers posted deviation documents; at least one filter is required |
| `get_rfo_agency_deviation(source_id, page_start?, page_end?)` | Resolves an indexed source ID into page-numbered PDF text with document-found applicability language |
| `get_rfo_guidance(resource, heading?, cursor?)` | Retrieves the RFO FAQ, policy-and-guidance page, or FAR Council deviation-guidance PDF |

Agency PDF dates and applicability are returned only when labeled language is found inside the document; filenames are never used to infer them. Duplicate and conflicting index entries come back with warnings instead of being silently resolved.

## Installation

```bash
uvx acquisition-gov-mcp==1.0.2
```

The server uses stdio, requires no credentials, and defaults to a three-second cross-process interval between Acquisition.gov requests. `FEDERAL_API_MIN_INTERVAL_SECONDS` can adjust that interval for controlled testing; production clients should retain three seconds.

## Configuration

No configuration beyond the install. The server only permits `https://acquisition.gov` and `https://www.acquisition.gov` as fetch targets; redirect targets are revalidated, credentials and private-IP targets are rejected, responses are bounded by content type and byte limits, and HTTP 429 responses are not burst-retried (Retry-After is honored in the shared pacing state). The safety boundary is enforced in code, not promised in prose.

## Example Prompts

- "List the FAR Overhaul model parts and flag any with posted agency deviations."
- "Get the current model text for FAR Part 7 and cite the official source URL."
- "Which agencies have posted deviations for Part 16, and what does DOD's deviation actually change?"
- "Pull the RFO guidance FAQ and summarize the deviation process for a proposal manager."

## Business Relevance

- **Government contractors** resolve which FAR text governs a specific procurement before pricing a bid
- **Compliance and legal teams** produce audit-ready answers with content hashes and canonical URLs
- **Proposal managers** check agency deviation indexes so proposals cite the operative text, not the superseded model
- **Consultants** answer FAR Overhaul questions with primary-source citations instead of secondary summaries

## Integration with CorpusIQ

CorpusIQ answers questions about the business's own data (revenue, contracts, pipeline). Acquisition.gov MCP adds the external regulatory layer: an agent can resolve the FAR model part and agency deviations that govern a federal opportunity, then cross-check that opportunity against the company's pipeline, contract history and vendor records in CorpusIQ. Same split already running with Truth Bear GAUGE, Corpus Law, and AwardCast: regulation and public data from the specialist server, commercial truth from CorpusIQ.

## Limitations

- Read-only by design; the server explicitly does not decide which rule governs a procurement.
- New listing (Aug 24, 2026) with a young publisher account; repo stars are modest (20).
- US federal procurement scope only; state and local procurement rules are out of scope.
- stdio transport means local install rather than a hosted endpoint.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [mcp-sam-gov MCP](/hermes/mcp/servers/external/sam-gov-mcp) - 150-tool US government contracting and spending server
- [AwardCast MCP](/hermes/mcp/servers/external/awardcast-mcp) - SAM.gov solicitations and recompete radar
- [Corpus Law MCP](/hermes/mcp/servers/external/corpus-law-mcp) - US legal search and business formation
- [Truth Bear GAUGE MCP](/hermes/mcp/servers/external/truth-bear-gauge) - verifiable government data with cryptographic proof
