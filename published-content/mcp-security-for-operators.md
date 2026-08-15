# Is MCP Safe? What Operators Should Know About AI Connecting to Business Data

The first question every operator asks about connecting AI to their business tools is the right one: is it safe?

It should be. You are giving an AI access to your Stripe account, your QuickBooks, your customer data. If the answer to "is it safe" is not an immediate and confident yes, you should not connect anything.

Here is what you need to know.

## Read-only by default

The MCP servers that connect to business tools are read-only. An AI connected to Stripe can list charges. It cannot create them. It can read invoices from QuickBooks. It cannot modify them. It can query your database. It cannot write to it.

This is not a setting you toggle. It is a property of how the connection is built. The OAuth tokens granted to the MCP server request read-only scopes. Stripe sees a request for read access and only grants read access. If the AI tried to create a charge, Stripe would reject it at the API level.

## Scoped retention

When you ask your AI a question, it queries your tools live and returns the answer. Direct MCP does not retain raw customer files or full connector response payloads. Operational query text, per-user tool-call metadata, and bounded outcome summaries may be retained for up to 30 days. CorpusIQ does not use customer data to train models; the selected AI client's policy applies to its conversation.

This differs from maintaining a replicated raw-data warehouse. Direct MCP retrieves live source records without retaining raw customer files or full connector response payloads. Operational logs, optional indexed search, compliance receipts, and the selected AI provider still have their documented processing and retention paths.

## Audit logging

Operational query text and per-user tool-call metadata may be logged for up to 30 days, together with bounded outcome summaries. Raw customer files and full connector response payloads are not written into that operational log.

For teams on business plans, this audit trail is essential for compliance. SOX, SOC 2, GDPR — auditors want to know who accessed what data and when. MCP connections provide that trail.

## OAuth, not API keys

Connecting your tools uses OAuth, the same standard that powers "Sign in with Google." You authorize the connection once through your tool's own login page. The MCP server never sees your password. You can revoke access at any time from your tool's settings.

This is better than API keys. API keys are long-lived secrets that can be leaked. OAuth tokens are scoped, time-limited, and revocable.

## Hosting and certification

CorpusIQ runs on Microsoft Azure with DEKRA CASA Tier 2 certification. For enterprise operators who need to know exactly where their data flows through, the infrastructure is audited and certified.

## The bottom line

The security model is straightforward. Read-only access to your tools. Scoped retention. OAuth authentication. Audit logging. Certified infrastructure.

If any MCP platform cannot answer "is it safe" with these five things, do not connect your business to it.

---

*CorpusIQ connects ChatGPT, Claude, and Perplexity to 40+ business tools. Read-only. Live retrieval with scoped retention. corpusiq.io/security*
