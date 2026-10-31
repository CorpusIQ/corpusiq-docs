---
title: Spark Inventory MCP - Stock, Forecasts and Draft POs
description: "Remote MCP that reads live inventory and per-SKU demand forecasts, recommends reorders sized to lead time and MOQ, and drafts purchase orders for review."
category: Commerce and Marketplace Operations
stars: n/a (new listing)
added: 2026-10-30
source: "mcp.so homepage recentServers block on 2026-10-30 at 22:19Z under the slug spark-inventory, verified featured, plus a keyless JSON-RPC tools/list probe on https://api.sparkinventory.com/mcp answering HTTP 401 Unauthorized, the vendor detail page carrying transport Streamable HTTP, authType oauth, category Productivity and the OAuth and ChatGPT app claims, and HTTP 200 reads on sparkinventory.com and sparkinventory.com/pricing/"
relevance: ★★★
tags: [inventory, ecommerce, demand-forecasting, purchase-orders, supply-chain, shopify, oauth, remote-mcp]
last_updated: "2026-10-30"
---

# Spark Inventory MCP

**Every inventory system can tell you what you have. Almost none can tell you what you will run out of, and that is the question a business owner actually asks the assistant.**

Spark Inventory publishes a remote MCP endpoint at `https://api.sparkinventory.com/mcp` over Streamable HTTP with OAuth. A keyless `tools/list` answers a flat **HTTP 401** `Unauthorized` in 0.4 seconds, which is the normal state for a connector bound to a vendor account rather than an API key.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.sparkinventory.com/mcp
Auth:        OAuth (sign in with your Spark account)
Category:    Productivity (vendor card)
Client:      official app inside ChatGPT, Claude connector announced as coming
Licence:     closed (no public repository on the card)
Site:        sparkinventory.com
```

The configuration is the one-entry shape that hosted services should have:

```json
{
  "mcpServers": {
    "spark-inventory": {
      "type": "http",
      "url": "https://api.sparkinventory.com/mcp"
    }
  }
}
```

## What it does

The vendor states the audience precisely, which is rarer than it should be: product brands, wholesalers and 3PLs. The connector is built to answer inventory questions from the live system rather than from an export someone emailed last Tuesday, and the described surface runs in four directions:

- **Stock and risk** by SKU, location and warehouse, including on hand, incoming, days of supply and stockout risk.
- **Demand forecasts** under the vendor's Demand ESP model, which picks a forecasting model per SKU by backtest, corrects for stockouts, and handles seasonality, new items and promotions, with a confidence level attached to each forecast.
- **Reorder recommendations and draft purchase orders**, sized to lead times and minimum order quantities, prepared for review rather than sent.
- **Operations reads and writes** across sales orders, suppliers, transfers, receiving, pick lists and reports.

The vendor also ships an SMS assistant, Sparki, so a draft purchase order can be confirmed by text. That is a second surface rather than a different product, and it matters for the same reason as the MCP one: the confirmation step is where the money leaves.

## The forecast is the product, and stockout correction is the detail that earns it

Inventory software is a solved shape. Counting units and adding them up is arithmetic. What separates a planning tool from a stock ledger is what happens to the history that a bad month left behind.

Two sentences in the vendor's description carry the design. A forecasting model is **picked per SKU by backtest**, which is an admission that one model does not fit a fast-moving consumable and a slow-moving spare part, and that the choice is testable instead of asserted. And the history is **corrected for stockouts**, which is the part most implementations skip: a SKU that sold out in week three recorded low sales for the remaining weeks not because demand fell but because there was nothing on the shelf. An uncorrected model reads that hole as falling demand, forecasts less, reorders less, and the next stockout is caused by the tool that was supposed to prevent it. A forecast with a confidence level attached is also the difference between an answer and a number, since the assistant can report the confidence instead of presenting every estimate with the same authority.

That is the reason this entry exists rather than a third opinion on storefront health. The catalogue reads stores, checks them and publishes into them. This one reasons about the future of a physical quantity, which is the only input a purchase order has.

## Reorder math is where an assistant stops being decorative

A reorder recommendation that ignores lead time buys the wrong quantity even when it buys at the right moment. The vendor describes recommendations sized to **lead times and MOQs**, which are the two constraints that turn a forecast into an order: the supplier takes three weeks, so the stock that must cover three weeks plus a buffer is the number that matters, and the supplier sells in cases of 24, so 61 units becomes 72 and the cost of that rounding is real.

This is a genuine MCP fit rather than a chat gimmick, because the answer requires a join across four things an operator keeps in four places: current stock, open purchase orders, supplier lead times and the forecast. An assistant that can reach all four can answer "what do I order this week and what will it cost me" in one turn. An assistant that cannot produces confident arithmetic over one of the four.

## Drafts, not sends, and governed writes

Two containment statements are on the card and they are the right ones. Changes go through **governed writes that you review and approve before anything is committed**, and purchase orders are **drafted** rather than issued.

For an agent surface this is the correct default and it is worth naming why. Receiving, transfers and sales orders change what the system believes exists, and a wrong correction propagates into every downstream report and forecast. A tool that drafts and waits keeps the irreversible step in human hands while leaving the expensive work, which is assembling the recommendation, to the agent. The check any buyer should run in a trial is whether the approval step can actually be bypassed by a client that never reads the instruction, because a review that is a policy in the description is not the same as a review enforced by the server.

## Platform support, stated as the vendor states it

Spark Inventory is an **official app inside ChatGPT**, connected by searching for it in the app directory, and the vendor describes a **Claude connector as coming soon**. Until that ships, Claude reaches the server as a custom remote MCP connector, which is the generic path an operator can complete themselves. This entry records the distinction because "works with Claude" and "has a Claude connector" are different support states and only one of them is one click.

## What this pass did not establish

The endpoint is live and the credential contract is OAuth, and that is the whole of what was driven here: `tools/list` needs a token, so the tool names, the tool count and the write surface are the vendor's published position and not a list this pass measured. Three things a trial should settle before anyone drafts a real purchase order: whether the forecast confidence is returned as a field the assistant can quote, whether a draft purchase order can be written into an existing ERP or only read back inside Spark, and what the connectors actually cover for a Shopify or 3PL source.

## FAQ

### Does it need a Spark Inventory account?
Yes. The OAuth consent authorises a Spark account, and the vendor offers a free plan to start on.

### Can the assistant send a purchase order to a supplier?
Not per the published description. Purchase orders are drafted and wait for a person to approve them. Treat the send path as unverified until driven.

### Which clients work today?
Any MCP client that speaks remote Streamable HTTP. ChatGPT has an official app in its directory, and the vendor lists a Claude connector as coming soon, so Claude currently connects as a custom connector.

### Is there a public repository?
No. The service is closed and the card carries no repository link, so this entry rests on the live endpoint, the probe result and vendor documentation.

## See Also

- [Store Canary MCP - WooCommerce Store Health Check](/hermes/mcp/servers/external/store-canary-mcp/) - the storefront these SKUs sell through
- [MarketPrint MCP - Print on Demand to Your Store](/hermes/mcp/servers/external/marketprint-print-on-demand/) - the supply side where a product is manufactured rather than replenished
- [Hustle Got Real MCP - Dropshipping in Plain Chat](/hermes/mcp/servers/external/hustle-got-real-mcp/) - the same supply loop without owned stock
- [Tuqui MCP - Odoo in Chat, Read-Only by Default](/hermes/mcp/servers/external/tuqui-odoo-mcp/) - the ERP reading the same stock records from the accounting side
