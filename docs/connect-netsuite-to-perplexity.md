---
title: "Connect NetSuite to Perplexity via MCP"
description: "Connect NetSuite to Perplexity through CorpusIQ MCP. Ask about P&L by subsidiary, inventory below reorder point and open purchase orders from your own ERP"
category: Perplexity Integrations
tags: ["connect NetSuite to Perplexity", "NetSuite Perplexity integration", "MCP NetSuite connector", "NetSuite data to AI", "ask NetSuite in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-14"
canonical: "https://www.corpusiq.io/docs/connect-netsuite-to-perplexity"
robots: "index,follow"
---

# How to Connect NetSuite to Perplexity with CorpusIQ MCP

Perplexity is good at the world outside the ERP: supply chain news, freight rates, the announcement from a vendor you depend on.

It cannot see your inventory position, your open purchase orders, or your P&L by subsidiary, because none of that is public.

Connecting NetSuite through CorpusIQ MCP puts both in one thread. Perplexity answers the ERP question from your own account, read-only, and names the records it read.

### Why Connect NetSuite to Perplexity?

- **Margin in context.** "Our gross margin by subsidiary for the quarter is on screen. What moved in our input costs this quarter?" Both halves answered in one thread.
- **Inventory versus demand.** "Which SKUs are below their reorder point, and which of those suppliers had lead time warnings this month?"
- **Procurement.** "Which purchase orders are open past their expected delivery date, by vendor?"
- **Subsidiary consolidation.** Ask across entities without a saved search for each one.
- **Order to cash.** "What is our order to cash cycle by subsidiary?" instead of a workbook built by hand.
- **Read-only by role.** Token-based authentication with a read-only role. The retrieval tools documented on this page are read-only.

### How It Works

1. **Create a read-only integration role in NetSuite** and generate token-based authentication tokens.
2. **Connect NetSuite to CorpusIQ** with the account ID, consumer key, consumer secret, token ID and token secret.
3. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
4. **CorpusIQ reads** the records that answer the question through the SuiteTalk REST API.
5. **Perplexity answers** from that result, with the surrounding market context you asked for.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In NetSuite**

1. Ask a NetSuite administrator to create an **integration record** for CorpusIQ.
2. Build a role that carries read permissions only, on the record types you want answerable.
3. Generate the **token-based authentication** credentials for that role: consumer key, consumer secret, token ID and token secret.

**In CorpusIQ**

4. Open your dashboard and go to **Connectors**.
5. Select **NetSuite** and enter the **Account ID**, **Consumer Key**, **Consumer Secret**, **Token ID** and **Token Secret**.
6. Choose which record types are reachable. The connector turns green.

**In Perplexity**

7. Open **Settings** and find the **MCP servers** section.
8. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

9. Connect and approve the CorpusIQ authorization page once.
10. Start a new thread and ask a question about your ERP data.

The setup is a one-time token entry with a NetSuite admin. There is no SuiteScript to write and no saved search to maintain.

### Example Perplexity Questions

**Financials**

- "Show me the P&L by subsidiary for last quarter, and tell me which line moved most against the same quarter last year."
- "What is our AP aging, and which vendors are we paying late?"
- "Which departments are over budget this month?"

**Inventory and supply chain**

- "Which SKUs are below their reorder point across all warehouses, sorted by how far below?"
- "What is inventory turnover by product category?"
- "Which locations hold excess inventory relative to the last 90 days of movement?"

**Orders and procurement**

- "Show me open purchase orders by expected delivery date."
- "Which sales orders have not been fulfilled, and how old are they?"
- "What is our average order to cash cycle time?"

**Cross-source**

- "Compare NetSuite revenue by month to Stripe collections for the same months." (requires the Stripe connector)
- "Which NetSuite customers also have open Salesforce opportunities this quarter?" (requires the Salesforce connector)
- "Does the demand we see in Google Analytics match the order volume in NetSuite?" (requires the Google Analytics connector)

### Security

- **Read-only role.** A dedicated NetSuite role limited to read permissions decides what the connector can reach. It never sees a record type you did not grant.
- **No stored credentials on your side.** CorpusIQ holds the encrypted token credentials; you can revoke the tokens in NetSuite at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between NetSuite, CorpusIQ and Perplexity.

### Comparison: NetSuite Saved Searches vs NetSuite in Perplexity

| Aspect | NetSuite saved searches | CorpusIQ MCP with Perplexity |
|---|---|---|
| Who builds it | A NetSuite admin or consultant | Anyone with the connector |
| Input | Search criteria in NetSuite | A question in plain language |
| Outside context | Leave NetSuite and search separately | Same thread, same answer |
| Cross-system | Export and reconcile by hand | Asked across connectors |
| Change the question | Edit the search | Ask it again |
| Write access | Yes, for a role that has it | None through the retrieval tools |

A saved search is a good answer to a question that will be asked the same way every month. It is no help to the question that has never been asked before.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change anything in NetSuite?</strong></summary>

No. The retrieval tools documented on this page are read-only, and the integration role carries read permissions. Transactions, inventory and vendor records are untouched.
</details>

<details>
<summary><strong>Does this cover multi-currency and multi-subsidiary accounts?</strong></summary>

Yes. Transactions return at line level with their original currencies, and answers can be scoped to a subsidiary or asked across all of them.
</details>

<details>
<summary><strong>Which NetSuite API does the connector use?</strong></summary>

The SuiteTalk REST API with token-based authentication. OneWorld accounts consolidate through the same path.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the current state of the account, so a receipt posted this morning appears in the next answer. Verify time-sensitive figures against the cited record.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. NetSuite is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>What happens when the tokens rotate?</strong></summary>

Rotate the tokens in NetSuite and re-enter them in CorpusIQ. Questions stop working until the new credentials are in, so keep the rotation on a known schedule.
</details>

<details>
<summary><strong>Where is the NetSuite data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect NetSuite to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
