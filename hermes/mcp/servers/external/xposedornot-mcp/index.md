---
title: "XposedOrNot MCP - Breach Intelligence by Domain"
description: "XposedOrNot MCP checks an email or a domain against 794 indexed breaches, keyless and free, and returns exposure counts an agent can act on."
category: "Security & Intelligence"
stars: 0
added: 2026-10-20
source: "chatmcp/mcpso issue window #5718 (submitted 2026-10-19T06:18:28Z)"
relevance: ★★★
tags: [security, data-breach, vendor-risk, due-diligence, credential-exposure, osint, remote-mcp, keyless]
---

# XposedOrNot MCP

**Vendor due diligence asks one question that almost never gets answered before signature: how much of this company's email has already been published. This answers it for a domain, without a key.**

```
Server type: Remote (Streamable HTTP) at https://api.xposedornot.com/mcp
Auth: none. Read-only, no key, no account, no session
Live check: unauthenticated POST initialize returned HTTP 200
  (serverInfo: XON_MCP, "XposedOrNot Breach Intelligence", version 2.0.0),
  tools/list returned the six tools below, and a live tools/call returned the catalog metrics
Vendor: XposedOrNot, xposedornot.com
```

## Why This Matters for Operators

A breach check is normally an individual's errand: type your own address into a free site and see whether your password leaked. The business version is different and much harder. Before you hand a vendor production access, or sign a data-processing agreement, or acquire a company, the exposure of its staff email is evidence about how it handles credentials, and it is evidence that no one assembles because the check is per address and a company has hundreds.

The domain view is the one that changes a decision. If a counterparty's domain appears in dozens of breaches with millions of affected accounts, a security questionnaire answer about "strong password policy" is worth less than it looked. If your own domain appears in a breach you did not know about, the response is a scoped password reset, not a press release.

The server also carries the catalog and the aggregate: which breaches exist, when they were added, what industries they hit, and the largest ones by record count. That makes it usable for monitoring a sector as well as checking a name.

## The Six Tools

| Tool | What it returns |
|---|---|
| `check_email_breaches` | Whether one email appears in the index, and the breaches it appears in |
| `get_breach_analytics` | Full breach history for one email: dates, descriptions, exposure detail |
| `list_breaches` | The breach catalog, filterable by breached company domain or breach ID |
| `domain_breach_summary` | Aggregate for a whole domain: number of breaches, affected account count, pastes, and the trend |
| `get_breach_metrics` | System-wide statistics: totals, breaches per year and industry, the largest breaches |
| `get_recent_breaches` | The most recently added breaches, newest first, with a summary and a source URL |

`domain_breach_summary` is the tool that earns the entry. It is the difference between a personal lookup and a diligence surface.

## What the Live Call Returned

A keyless `get_breach_metrics` call at the time of this sweep returned a catalog of 794 breaches holding 11,717,004,638 exposed records, a separate paste index, and a last-added timestamp of 2026-10-14. That recency matters more than the total: a breach index that stopped updating two years ago is an archive, and this one added entries this month.

## Honest Limits

- **Absence is not innocence.** A domain with no hits is missing from this index, which is not the same as never breached. Indexes depend on disclosure, and most breaches are never disclosed.
- **Presence is not compromise.** A leaked address is exposure of a credential at a point in time. It says nothing about whether that credential was used, whether it was reused, or whether the account still exists.
- **Emails are personal data.** Checking your own domain is operations. Checking a named individual's address, or bulk-checking a partner's staff, is processing personal data and belongs inside whatever agreement covers that relationship.
- **Read-only by design.** There is no write surface, so the credential risk of connecting it is the disclosure of what you queried, not of what it could change.

## FAQ

### How is this different from the OSINT server already in the catalog?

[OpenOSINT MCP](/hermes/mcp/servers/external/openosint-mcp) carries a breach check as one of nine tools, and it queries HaveIBeenPwned with an API key the operator supplies, one address at a time. XposedOrNot is the dedicated surface: keyless, free, and with a domain-level aggregate that no per-address check can produce.

### Should a breach hit block a contract?

No single signal should. What it changes is the follow-up: which accounts were exposed, whether the counterparty knew, and what they did after. Treat it as one line in diligence, weighted by what the vendor is about to receive.

### Can I monitor my own domain?

Yes, and that is the cheapest use of the server: a scheduled check of the company domain against `get_recent_breaches` turns breach monitoring into a recurring agent task instead of a news item someone forwards.

### Does it cost anything?

No. The server is free and read-only, with no key and no account, which is why it can be added to an agent today without a procurement step.

## See Also

- [OpenOSINT MCP - MCP-Native OSINT Framework](/hermes/mcp/servers/external/openosint-mcp)
