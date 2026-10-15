---
title: "Corply MCP - Delaware C-Corp Formation from Chat"
description: "An agent-native rail to form and run a Delaware C-corp: e-signed filings, EIN, registered agent, equity splits and corporate actions over native OAuth."
category: "IP/Legal"
stars: n/a (new listing)
added: 2026-10-14
source: "mcpservers.org /all (October 14, 2026 evening sweep)"
relevance: ★★
tags: [incorporation, legal, delaware, c-corp, founder-ops, company-formation, oauth]
---

# Corply MCP

**An agent-native rail for forming and running a Delaware C-corp: the founder works with their assistant through company intake, review, signing and payment, and the same MCP connection then manages equity, corporate actions and compliance. Every Delaware filing is human-reviewed by Corply. Hosted Streamable HTTP with native OAuth sign-in.**

```
Server type: Hosted (Streamable HTTP)
Endpoint: https://corply.dev/mcp
Auth: OAuth (client's native login; whoami verifies the connected account)
Setup guide: https://corply.dev/skills.md (agent-readable)
Supported formation: Delaware C-corps
Typical tools: whoami, save_application, get_status, plus equity, corporate action and compliance tools
Billing: formation plus ongoing service pricing at corply.dev/pricing (checked at checkout)
Publisher: corply.dev
Listing: mcpservers.org /all, October 14, 2026 evening sweep
```

## Why This Matters for Operators

Starting and maintaining a US corporation is a paperwork operation with real legal weight: intake, entity configuration, filings with the state, an EIN, a registered agent, founder equity splits with vesting, board approvals, charter amendments, annual compliance. Most of it is structured data entry that a founder re-types between tools.

Corply puts formation and corporate-actions work behind MCP tools so the assistant the founder already uses can drive the process: collect and stage company facts, prepare the application, and then manage equity, corporate actions and compliance on the live entity. Formations are US Delaware C-corps, and every filing is human-reviewed before submission. This is the formation rail next to the venture-funding rail (Pitch Protocol) and the legal-search surface (Corpus Law) already in the catalog.

## Capabilities

| Area | What the agent can do |
|---|---|
| Company intake | Collect and stage formation facts with the founder ("incorporate me using Corply"), then reuse verified facts after sign-in |
| Application | Save and manage the formation application (save_application), review status (get_status) and follow the workflow contract the server returns |
| Identity | whoami verifies which account and company the connection acts as, before any authorized action |
| Equity | Manage founder equity splits and vesting on the formed company |
| Corporate actions | Manage corporate actions such as charter amendments and board changes |
| Compliance | Ongoing company compliance on the live entity |
| Client coverage | Claude Code, Codex CLI and desktop, Cursor, OpenCode and any other MCP client via native remote server settings |

## Setup

Add the hosted server and sign in once with the client's native OAuth flow; then verify the connection with `whoami` before running any authorized action.

- **Claude Code:** `claude mcp add --transport http corply https://corply.dev/mcp`, then `claude mcp login corply` to open the browser sign-in.
- **Codex CLI / Cursor / OpenCode / other clients:** add `https://corply.dev/mcp` as a remote (Streamable HTTP) server in the client's MCP settings, then authenticate natively. Cursor example: `{ "mcpServers": { "corply": { "url": "https://corply.dev/mcp" } } }`.
- The browser path works without any MCP client: https://corply.dev/signup covers intake, review, signing and payment directly.

A missing marketplace listing does not block setup; the server is added directly in client settings. Live pricing and checkout terms are on corply.dev/pricing and are confirmed at checkout.

## Business Relevance

- **Founders** get entity formation and equity setup as a conversation in their existing assistant, with the paper trail handled by a human-reviewed service
- **Small teams without in-house legal ops** get a supported default for Delaware incorporation, registered agent and ongoing compliance steps
- **Operators adding a US entity** alongside an existing business can run the whole intake from chat and verify each stage by status rather than by email threads
- **Equity and corporate-action changes** stay in one rail instead of being re-keyed between documents and tools

## Integration with CorpusIQ

CorpusIQ answers business questions from the data you connect - revenue, customers, project costs. Governance steps like formation and corporate actions sit beside that picture: the same assistant can query the business data through CorpusIQ while handling entity administration through Corply, without building an integration between them.

## Limitations

- **US Delaware C-corps only:** other entity types and jurisdictions are not supported by this rail
- **Account required:** every tool runs as the signed-in account, and the assistant should verify whoami before authorized actions
- **Human-reviewed filings:** Corply reviews and files; the service is not a self-serve instant incorporation, and timeframes follow its review process
- **Pricing changes:** formation and ongoing-service costs are defined on corply.dev/pricing and at checkout, not in this guide
- **Not legal advice:** the rail executes formation and administration; it does not replace counsel for complex structures or agreements
- **New listing (v1 at capture time):** capability details are as the publisher documents them on corply.dev

## FAQ

### Can I form a company that is not a Delaware C-corp?

No. At capture time the supported formation is Delaware C-corps.

### Does the agent collect everything before I can sign in?

No. The documented flow is to connect first, then let the founder supply facts; the assistant should verify whoami and match the intended account or company before acting.

### Do I need a marketplace plugin?

No. The server is added directly in the client's MCP settings as a remote Streamable HTTP server; a missing marketplace listing does not block setup.

### Who files the paperwork?

Corply. Every Delaware filing is human-reviewed before submission, and status is available through the connection.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [Corpus Law MCP - US Legal Search and Business Formation](/hermes/mcp/servers/external/corpus-law-mcp/)
- [Pitch Protocol MCP - Agent-Native VC Applications](/hermes/mcp/servers/external/pitch-protocol-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
