---
title: "ClauseAI MCP - Startup Legal Document Generation for Agents"
description: "Keyless remote MCP server that fills attorney-drafted legal templates (NDAs, MSAs, DPAs, privacy policies, offer letters and more) from General Legal's CC0 library. Agents list templates, inspect fields, and generate documents as PDF, ODT or Markdown - no account required."
category: Legal
stars: n/a (new listing)
added: 2026-09-11
source: "chatmcp/mcpso issue #4077"
relevance: ★★★
tags: [legal, contracts, nda, privacy-policy, startup, keyless, remote-mcp]
---

# ClauseAI MCP

**Remote MCP server (Streamable HTTP, keyless)** - generates startup legal documents from attorney-drafted templates with no account required. The gallery, JSON API, MCP server and agent skill all share one template engine fed by General Legal's CC0 template library, so an agent can generate an NDA, MSA, DPA, privacy policy, offer letter or terms of use and download it as PDF, ODT or Markdown.

```
Server type: Remote (Streamable HTTP)
Auth: None - no account required
Endpoint: https://clauseai.exe.xyz/mcp
Tools: Streamable HTTP tools for listing, inspecting and generating documents
Templates: 12 (advisor agreement, BAA, cookie notice, DPA global/US, employee offer letter CA, MSA, mutual NDA, one-way NDA, privacy policy GDPR/US, terms of use)
Formats: PDF, ODT, Markdown
Category: Legal
Built by: ClauseAI (wasauce/clauseai) - templates by General Legal, CC0
```

## Templates

| Slug | Document |
|---|---|
| mutual-nda | Mutual Non-Disclosure Agreement |
| one-way-nda | One-Way Non-Disclosure Agreement |
| master-services-agreement | Master Services Agreement (MSA) |
| dpa-global | Data Processing Addendum (Global) |
| dpa-us | Data Processing Addendum (U.S.) |
| privacy-policy-gdpr | Privacy Policy (GDPR Enhanced) |
| privacy-policy-us | Privacy Policy (U.S. Only) |
| terms-of-use | Terms of Use |
| cookie-notice | Cookie Notice |
| employee-offer-letter | Employee Offer Letter (California Exempt) |
| advisor-agreement | Advisor Agreement |
| business-associate-agreement | Business Associate Agreement (BAA) |

Documents can be downloaded at any time - even with nothing filled in. Templates are for general reference only and are not legal advice.

## Connection

1. Point any MCP client at the endpoint - Streamable HTTP, no account.
2. Claude Code one-liner - `claude mcp add clauseai --transport http https://clauseai.exe.xyz/mcp`
3. Or install as an agent skill - `npx skills add wasauce/clauseai --skill clauseai`
4. Ask the agent to generate a document (e.g. "Generate a mutual NDA from our company details") and pick PDF, ODT or Markdown on download.
5. Machine-readable surfaces: template catalog at /api/templates, OpenAPI at /openapi.json, agent index at /llms.txt, interactive docs at /docs.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed: the Streamable HTTP endpoint responds to JSON-RPC (session-gated initialize handshake, "Bad Request: Missing session ID" on a bare tools/list - the server enforces the MCP session protocol). The template catalog API returned all 12 templates live, matching the README. Repo wasauce/clauseai is public with the full FastAPI surface and the NDA walkthrough at clauseai.exe.xyz/examples/generate-nda.md.

## See Also

- [CourtListener MCP - US Legal Research for Agents](/hermes/mcp/servers/external/courtlistener-mcp)
- [Bynn MCP - KYC and Document Fraud Detection for Agents](/hermes/mcp/servers/external/bynn-mcp)
- [Wafeq MCP - Accounting Books for Agents](/hermes/mcp/servers/external/wafeq-mcp)
