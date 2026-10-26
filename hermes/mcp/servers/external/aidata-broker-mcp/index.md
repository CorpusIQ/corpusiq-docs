---
title: "AIData.Broker MCP - AI Training Data Prices and Deals"
description: "Free read-only MCP server on what AI training data sells for: market rates, published prices, buyers, licensing deals, cases and software terms."
category: "Finance / Data Economy"
stars: n/a (new listing)
added: 2026-10-15
source: "mcpservers.org /all (October 15, 2026 evening sweep)"
relevance: ★★
tags: [ai-training-data, data-licensing, market-rates, benchmarking, public-data, keyless, legal]
last_updated: "2026-10-19"
---

# AIData.Broker MCP

**A cited price book for the AI data market. Nine read-only tools answer what a kind of training data actually sells for, who is buying, which licences were disclosed, what the courts have said, and what a business system's own terms allow. Every figure carries the publication that stated it, and every answer names the source and the page to cite. Free, read-only, no account.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://aidata.broker/mcp
Auth: None (no account, no key; all tools flagged read-only)
Server: AIData.Broker v2026.10.14
Works with: Claude, ChatGPT, Cursor, VS Code and any client that accepts a remote MCP server
Data: 912 published prices, 52 market rates, 36 buyers and their terms, 95 licensing deals, 68 lawsuits and rulings, terms of 18 business systems
Publisher: AIData.Broker (aidata.broker); open datasets under CC BY 4.0
Listing: mcpservers.org /all, October 15, 2026 evening sweep
```

## Why This Matters for Operators

Every company now sits on data an AI developer may want, and most have no price reference for it. The market is public but scattered across pricing pages, licensing press releases and court dockets. This server gathers those into one place and refuses to invent a number: if the evidence does not support a median, it says so.

## What You Can Do Today

| Tool | What it does |
|---|---|
| `get_market_rates` | Median, middle half and range per comparable unit (per hour of video or audio, per image, per task, per company) by kind of data and side of market |
| `search_prices` | The individual price observations behind the rates: what a lab, vendor, marketplace or court said data was worth |
| `value_data` | What published prices imply for a specific holding, as a low-to-high range in US dollars with the arithmetic shown |
| `find_buyers` | Organisations with a public way to sell them data, plus their own published terms |
| `find_vendors` | Companies selling training data, RL environments, evaluations, expert work and annotation to AI developers |
| `search_deals` | Data licences disclosed to AI companies since July 2023: licensor, licensee, content and use |
| `search_cases` | Lawsuits, rulings, settlements and regulatory actions over data used to train AI, with parties, claims and amounts |
| `check_software_terms` | What a named business system (Slack, Microsoft 365, Google Workspace, Salesforce, HubSpot, Zendesk, Zoom, GitHub and others) allows |
| `list_datasets` | The tables behind these tools as CSV and JSON downloads under CC BY 4.0 |

## Business Relevance

- **Data holders** - publishers, marketplaces, review sites, archives - get a defensible starting range before any conversation with a buyer
- **Legal and procurement** read the disclosed deals and the litigation record in the same assistant that holds the contract
- **Policy and compliance** check the software systems already in use, because a SaaS terms clause can decide whether the data can be licensed at all
- **Finance and strategy** get comparables for an asset class that rarely appears in a model
- **Cited by construction:** each answer points at the publication and page behind the figure, which is what makes it usable in a memo

## Integration with CorpusIQ

Data-monetisation questions have three inputs: what sits in your systems, what your software terms permit, and what the market pays. CorpusIQ covers the first over read-only connectors - analytics, commerce, CRM, documents, email - and this server covers the market. Connect both and a single conversation can move from a named system's terms to a range for the data inside it.

## Limitations

- **Evidence-bound:** the server reports published prices and refuses to model or project a figure the evidence does not support
- **Read-only:** no account, no writes, no deal flow - it informs a decision rather than executing one
- **Coverage:** medians exist only where enough published observations exist, so some kinds of data return no rate
- **Not a valuation:** the ranges are what comparable published prices imply, not an appraisal or a legal opinion
- **Market scope:** deals are those disclosed since July 2023 and cases are those captured in the dataset

## FAQ

### Do I need an account or an API key?

No. A keyless `initialize` call to `https://aidata.broker/mcp` returns 200 as `AIData.Broker` v2026.10.14, and all nine tools are flagged read-only.

### What does it cost?

Nothing to query. The published endpoints, tools and open datasets are free and carry no authentication.

### Can it tell me what my own data is worth?

`value_data` returns a low-to-high range in US dollars implied by published prices for a comparable holding, with the arithmetic behind it shown so the assumption is visible.

### Is the underlying data reusable?

Yes. `list_datasets` exposes every table behind the tools as CSV and JSON downloads under a CC BY 4.0 licence.
