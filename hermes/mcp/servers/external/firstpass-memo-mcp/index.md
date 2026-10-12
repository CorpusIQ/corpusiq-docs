---
title: "FirstPass Memo MCP - Business Listing Red Flags"
description: "Check any business-for-sale listing against 33 published red-flag rules and get payback, asking multiple vs comparables and questions for the seller."
category: Business Operations
stars: n/a (no public repo)
added: 2026-10-11
source: "mcpservers.org /all (Oct 11, 2026 evening sweep)"
relevance: ★★★
tags: [due-diligence, acquisitions, listings, screening, valuation, keyless, remote-mcp]
---

# FirstPass Memo MCP

**Remote MCP server (Streamable HTTP, no auth)** - a free listing checker for businesses for sale: connect ChatGPT, Claude, Cursor or any MCP client to `https://firstpassmemo.com/mcp`, paste a listing, and get payback, the asking multiple against comparables, every red flag that fired, and the questions to ask the seller.

```
Server type: Remote (Streamable HTTP)
Auth: None (free, no key, no account)
Endpoint: https://firstpassmemo.com/mcp
JSON API: https://firstpassmemo.com/api/check
Tools: 2 (check_listing, list_rules)
Rules: 33 published rules (rules.json)
Registry: com.firstpassmemo/listing-check (official MCP Registry)
Listing: mcpservers.org /all (Oct 2026)
```

## Why This Matters for Operators

Buying a small business starts with a marketplace listing - Flippa, Acquire.com, Empire Flippers - that is written to sell, and the first questions are always the same: how many months to pay back, is the asking multiple sane for the category, and what is the seller not saying. Running that screen by hand means holding ten heuristics in your head while reading between the lines.

FirstPass runs the same 33 published rules as its browser checker, from the assistant you already use. Paste the listing text and any numbers you have, and `check_listing` returns payback in months, the annual multiple measured against category benchmarks, each flag that fired with its severity and a link to the rule page, and a ready list of questions for the seller. **The screen happens before the spreadsheet: cheap, fast, and before any NDA or call.**

For operators on the other side - brokers and sellers - the same check runs on your own memo before it goes out, so the obvious flags are answered before a buyer asks them.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `check_listing` | Takes the listing text (up to 20,000 characters) plus optional numbers (asking price, monthly profit, monthly revenue, age, category, traffic sources) and returns payback in months, the annual multiple, the category's benchmark range, every flag with severity and rule link, and seller questions |
| `list_rules` | Returns the 33 red-flag rules, the same as `rules.json` |

The plain JSON API (`POST https://firstpassmemo.com/api/check`) exposes the same checks for scripts and custom GPT actions. Benchmarks are built from Empire Flippers public marketplace asking multiples (built October 6, 2026); some categories have small samples.

## Installation

```bash
claude mcp add firstpass-listing-check --transport http https://firstpassmemo.com/mcp
```

Claude web and desktop: Settings, Connectors, Add custom connector, paste the endpoint. ChatGPT in developer mode: add a connector with the URL and no authentication. Cursor and VS Code declare the same URL in `mcp.json`.

## Configuration

```json
{
  "mcpServers": {
    "firstpass-listing-check": {
      "type": "http",
      "url": "https://firstpassmemo.com/mcp"
    }
  }
}
```

No key, no account, no OAuth. The tool does not open links - paste the listing text itself.

## Business Relevance

- **Acquisition-minded operators** get a first-pass screen on any for-sale listing in seconds, in the same assistant they already work in
- **Brokers and sellers** can pre-check their own memos and answer the standard flags before buyers raise them
- **Buyers in the middle of diligence** get a structured seller question list, so call time goes to the questions that matter
- **Operators comparing targets** can run the same rules across multiple listings for a consistent read

## Integration with CorpusIQ

FirstPass is a screening layer that pairs naturally with the numbers a CorpusIQ user already holds. Your own QuickBooks, Stripe or Shopify connectors show what a healthy business in your model looks like - margins, seasonality, spend shape - which turns the listing's claims into something to compare rather than accept. Run the check, then bring the seller's follow-up answers back into the same thread and keep the question list with the rest of the deal notes.

For sellers: run your own memo through the same check before listing, and use CorpusIQ to pull the operating numbers the memo cites.

## Limitations

- Brand new - registry entry published October 11, 2026, no track record yet
- Screening only: the rules read what the seller published and verify nothing
- Not investment, legal, tax or valuation advice
- Text-only input (up to 20,000 characters); the tool does not open links
- Benchmarks come from one marketplace (Empire Flippers) and some categories have small samples
- The free keyless endpoint may rate-limit at high volume

## FAQ

### What does the check actually do?

It runs 33 published red-flag rules over the listing text plus any numbers you provide, and returns payback in months, the annual asking multiple against category benchmarks, every flag with its severity and rule page, and questions to ask the seller.

### Does it verify the seller's numbers?

No. The rules read what the seller published. Nothing is verified, and the output is not investment, legal, tax or valuation advice - it is a first-pass screen before real diligence.

### Does it need an account or an API key?

No. The MCP endpoint and the JSON API are free and keyless. Pasted listing text is processed in memory and discarded, not stored or logged.

### Where do the benchmarks come from?

Empire Flippers public marketplace asking multiples, built October 6, 2026, with category ranges; some categories carry small samples.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
