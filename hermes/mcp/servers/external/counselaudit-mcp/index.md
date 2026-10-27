---
title: "CounselAudit MCP - Legal Bill Review for Your AI"
description: "Audit outside counsel invoices from Claude or ChatGPT: review legal bills against your guidelines, resolve flags, and track legal budgets and spend."
category: IP/Legal
stars: n/a (new listing)
added: 2026-10-11
source: "chatmcp/mcpso issue #5128 (Oct 11, 2026 midday sweep)"
relevance: ★★
tags: [legal, legal-ops, invoices, spend-management, oauth, remote-mcp]
last_updated: "2026-10-24"
---

# CounselAudit MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - brings legal bill review into Claude, ChatGPT or any MCP client: audit an invoice against your outside counsel guidelines, work through the flags, and answer spend questions, without leaving the chat.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration (sign in with a CounselAudit account)
Endpoint: https://app.counselaudit.com/api/mcp/mcp
Tools: invoice audits, flags, guidelines, budgets, approvals, spend questions
Pricing: API and MCP add-on at 200 USD a month; included on Enterprise
Built by: CounselAudit
Registry: com.counselaudit/counselaudit
```

## Why This Matters for Operators

Every in-house legal team runs the same monthly loop: the firms send invoices, someone reads them against the outside counsel guidelines, flags the misses, argues the exceptions and reconciles against the budget. CounselAudit is the review engine for that loop, and the MCP connector makes it a chat surface: queue an audit, read the flags with their severity, decide each one, and draft the response letter to the firm in the same conversation.

The connector works on data already in the account (documents are not uploaded through MCP), and every connection is scoped to the signed-in organization.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Audits | Queue a full invoice review against the guidelines; flags are usually ready in one to four minutes and say which fee arrangement the run used |
| Flags | Resolve each flagged item: approve, reject, adjust or escalate, with the flag list saying when the run is complete |
| Guidelines | Review a guideline set for gaps (missing sections, weak clauses), draft clause language, and draft the outside counsel guidelines letter to a firm |
| Invoices | Find invoices by number, firm, matter, status, assignee or dates; view one in full with line items in pages of 200 and flag counts |
| Spend | Ask plain-language questions about spend, invoices, firms, matters or flags with a written answer plus the underlying data |
| Budgets | List budgets with spend to date, remaining and percent used; see which period an invoice counts toward |
| Approvals | List fee arrangements and matter approvals with limits; get the monthly approvals report with rejections by reason |
| Timekeepers | Find firm timekeepers whose seniority could not be auto-verified |

## Installation

In Claude: Settings, Connectors, Add custom connector, then the URL below. A CounselAudit sign-in window opens; approve the connection and the tools appear. Claude Code, Cursor and other MCP clients connect with the same URL using their remote MCP server option.

```
https://app.counselaudit.com/api/mcp/mcp
```

The endpoint returns 401 until authenticated - the live probe returns the OAuth protected-resource metadata, which is expected, not an outage. You need a CounselAudit account with at least one uploaded invoice and a guideline set.

## FAQ

### Does the connector upload my invoices anywhere?
No. It works on the data already in the account; documents are not uploaded through MCP.

### What does it cost?
MCP access is included on Enterprise and available to other plans as the API and MCP add-on from the billing page (listed at 200 USD a month).

### Can the agent resolve flags by itself?
It can act on your direction: approve, reject, adjust or escalate, the same choices the review team uses. Nothing changes without an account with the right plan access.

### Which clients work?
Any MCP client with remote server support and the sign-in flow: Claude, Claude Code, Cursor and others. The docs page is at app.counselaudit.com/docs/mcp.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
