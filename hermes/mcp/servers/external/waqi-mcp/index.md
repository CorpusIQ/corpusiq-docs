---
title: "Waqi MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Hosted MCP privacy layer that redacts PII from Stripe, Xero, CRM and 16 business connectors before the AI sees it, with a provable audit log"
category: Data & Analytics
stars: n/a (new listing)
added: 2026-08-18
source: mcp.so homepage
relevance: ★★
tags: [privacy, security, pii, redaction, dlp, gdpr, compliance, audit, remote-mcp]
---

# Waqi MCP

**Hosted MCP server that sits between your business tools and your AI assistant — Waqi fetches data read-only from Stripe, Xero, your CRM, and 14 other connectors, strips names, card numbers, and personal details, writes a provable audit entry, and only then returns the cleaned data to the model.** Your AI gets real answers from real business data; your customers' personal data never reaches it. Commercial service by Bilazann, from £99/month.

```
Server type: Remote (HTTP, per-person token URLs)
Auth: Token embedded in URL (per team member, individually revocable)
Endpoint: https://waqi.bilazann.com/api/mcp/YOUR_TOKEN
Tools: Published tool list pending (16 business connectors)
Pricing: From £99/month (VAT-inclusive), annual and team plans
Category: Data & Analytics / Compliance
Built by: Bilazann (bilazann.com/waqi, repo: ajprolific/waqi-mcp)
```

## Why This Matters for Operators

The single biggest blocker to using AI on real business data is what else rides along with it — customer names, card numbers, personal details. Waqi attacks that directly: redaction happens before any response leaves the server, so the model only ever sees cleaned data, and the audit log is written after redaction so the log itself never holds sensitive values.

**The audit trail is the product, not a feature.** Every call is logged — who asked, which tool, what was caught. For accountants, agencies, and clinics where confidentiality is the business, that converts "has our data been through an AI?" from a reassurance into a record. Per-person tokens mean every team member gets their own URL with individual attribution and per-person revocation.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Connector management | Connect Stripe, Xero, Zoho, Slack, CRM, and more from the dashboard (16 connectors) |
| Redacted fetch | Read-only fetch with PII detection and replacement before the model sees anything |
| Audit log | Every call logged post-redaction: requester, tool, what was caught |
| Per-person tokens | Individual MCP URLs per team member, individually revocable |
| Credential vault | Connector keys stored encrypted and write-only — no read-back, even for the owner |

Read-only by design: Waqi fetches, it never writes to your tools. No self-host — it runs as a managed service.

## Installation

1. Sign up at bilazann.com/waqi — the dashboard issues each team member a personal MCP URL.
2. Connect a tool (Stripe, Xero, Zoho, Slack…) in the dashboard.
3. Paste the MCP URL into your client.

```json
{
  "mcpServers": {
    "waqi": {
      "type": "http",
      "url": "https://waqi.bilazann.com/api/mcp/YOUR_TOKEN"
    }
  }
}
```

Claude: Settings → Connectors → Add custom connector. ChatGPT: Settings → Connectors → Developer mode. Step-by-step guides at bilazann.com/waqi/docs.

## Configuration

The dashboard is the control surface: connectors per team, token issuance, revocation, and the audit trail. Credentials are write-only — not even the account owner can read them back. Data is fetched per request, redacted, and returned; only encrypted credentials and the already-redacted audit log are stored.

## Business Relevance

- **Accountants and agencies** give clients an auditable answer on AI exposure for every query
- **Compliance teams** get a GDPR-shaped DLP layer without re-architecting tool access
- **Finance operators** ask about real Stripe revenue and Xero invoices without exposing customer names or cards
- **Teams** get per-person attribution and per-person kill switches on AI access to business data

## Integration with CorpusIQ

CorpusIQ's MCP server is direct multi-source business data access — 40+ connectors answered in one surface, read-only, OAuth-scoped. Waqi is the privacy wrapper for cases where the raw record level must pass through: it adds redaction and an audit trail in front of individual tools like Stripe or Xero.

The composed posture: CorpusIQ for aggregate, multi-source business questions where no raw personal data needs to enter the prompt, and Waqi in front of specific connectors when a team must hand AI record-level access under a compliance regime. Both are read-only on the data plane; Waqi adds the DLP and audit layer CorpusIQ deliberately leaves to enterprise tooling.

## Limitations

- Commercial from £99/month — no free tier beyond trial
- Hosted only — no self-host option, vendor custody of the audit log
- No published tool list yet (mcp.so shows none detected) — surface must be evaluated in trial
- 16 connectors today, focused on payments, accounting, CRM, and communication
- Brand new listing (Aug 18, 2026)
