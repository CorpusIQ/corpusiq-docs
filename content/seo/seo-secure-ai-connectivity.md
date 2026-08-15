# Secure AI Data Connectivity — Read-Only Changes Everything

The #1 objection to connecting business data to AI: "What if it messes something up?"

Fair question. Here's why read-only design makes that impossible — and what else you should look for.

## The read-only guarantee

Every CorpusIQ connector is read-only by design. The AI can query your QuickBooks P&L but cannot create a transaction. It can pull Stripe charges but cannot issue a refund. It can search HubSpot but cannot modify a deal.

This isn't a setting you can accidentally change. It's architectural. The OAuth scopes only request read access. The API calls only use GET methods. There is no write path.

## What else matters for security

**OAuth-native authentication:** No API keys to manage, rotate, or leak. Each user authenticates via their own OAuth flow. Revoke access instantly from your Google/QuickBooks/admin console.

**Scoped retention:** Direct MCP does not retain raw customer files or full connector response payloads; operational logs may persist for up to 30 days.

**Disclosed processors:** CorpusIQ runs on Microsoft Azure and uses the selected AI client to answer the request. Each provider's published data policy applies to its part of the flow.

**CASA Tier 2 certified:** Independent security certification verifying read-only access controls, OAuth security, and data handling practices.

**SOC 2 aligned:** Security controls mapped to the framework; formal SOC 2 Type II certification is not claimed.

## The questions to ask any AI data platform

| Question | Why it matters |
|----------|---------------|
| Is it read-only by default? | Can't accidentally modify your data |
| Where does my data go? | Should flow directly to AI, not stored |
| How is auth handled? | OAuth > API keys. Per-user > shared. |
| Is it independently audited? | CASA, SOC 2, or equivalent |
| Can I revoke access? | Should be instant from your admin console |
| Who processes my data? | No third parties between you and the AI |

## The bottom line

Connecting business data to AI doesn't have to be scary. Read-only design, OAuth-native auth, scoped retention, and independent certification make it safer than giving an intern a CSV export.

---

*CorpusIQ: 37+ connectors, read-only by design, CASA Tier 2 certified. [corpusiq.io](https://www.corpusiq.io)*
