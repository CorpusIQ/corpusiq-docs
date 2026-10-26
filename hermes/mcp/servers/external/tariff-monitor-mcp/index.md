---
title: "Tariff Monitor MCP - Stacked US Import Duty by HTS Code"
description: "A US import tariff calculator over 19,856 HTS code lines that stacks MFN, Section 301 and Section 232 duties and prices the exposure in dollars."
category: Business Operations / Trade
stars: n/a (npm, free public API)
added: 2026-10-24
source: "mcpservers.org /all p1-20 fresh cohort (late sweep, October 24 2026) + npm package driven locally over stdio"
relevance: ★★★
tags: [tariff, hts, customs, imports, duty, section-301, section-232, landed-cost, ecommerce, trade-compliance]
last_updated: "2026-10-24"
---

# Tariff Monitor MCP

**A US tariff calculator an operator can actually interrogate.** Ask what a product is classified as, what the stacked duty is from each origin country, and what that costs at the import volume the business actually runs, without opening the Harmonized Tariff Schedule and reading footnotes.

```
Server type: Local (stdio, node, npm tariffmonitor-mcp 1.3.0, MIT)
Upstream: free public API at https://adcreator-ai.com/api/tem (no key, no signup)
Tools: 3 (lookup_hts_code, calculate_tariff, compare_origins)
Schedule: 19,856 ten-digit HTS code lines from the official USITC export
Transport options: stdio, or the packaged HTTPS mode that serves the same tools at /mcp
Registry: io.github.daleweaver1981/tariffmonitor-mcp 1.3.0, active
Built by: Dale Weaver (0xpi.com)
```

## Why This Matters for Operators

Duty is a cost of goods line that most operators model on a spreadsheet once a year and then stop watching. The problem is that the number moves. The Section 301 China product exclusions currently run through 11:59 p.m. eastern daylight time on November 9, 2026, and a 2026 Section 301 forced-labor tariff adds 10 percent or 12.5 percent by origin on top of the base rate for 60 economies. A landed cost built in January is wrong by summer.

The second problem is sourcing decisions. "Should we move this product out of China" is a question about a rate difference, and the difference is not the same for every product. On the men's footwear line tested in this sweep, China carries 30.50 percent while Mexico carries 20.50 percent. That gap is the entire margin on a low-margin import.

## What It Actually Does

Driven locally in this sweep: the npm package was installed, the stdio server started, `initialize` returned `serverInfo` `tariffmonitor` 1.3.0 on protocol 2025-06-18 with the tools capability, and `tools/list` returned three tools.

| Tool | Arguments | What it answers |
|---|---|---|
| `lookup_hts_code` | `query` (product words or a numeric prefix) | the candidate HTS lines, up to 12, with the heading named when a shopping word was mapped to it |
| `calculate_tariff` | `hts_code`, `origin_country`, optional `annual_import_value_usd` | the full stacked rate for that code from that origin, each layer named with its heading, plus the dollar exposure |
| `compare_origins` | `hts_code`, `origin_countries`, optional `annual_import_value_usd` | the same rate across several origins, sorted cheapest first |

Three real calls, quoted from the run:

**Classification.** `lookup_hts_code` with "athletic footwear" came back stating that no code description contains the whole phrase, so it searched "footwear" instead, and returned 12 lines starting `6812801000 Footwear`, `6401929030 Work footwear` and `6402993135 Work footwear`. It names the compromise it made instead of pretending the phrase matched.

**One origin.** `calculate_tariff` on HTS 6404112030 from CN at 800,000 dollars a year returned a stack of MFN base 10.5 percent, Section 301 China List 4A (heading 9903.88.15) 7.5 percent and the 2026 Section 301 forced-labor tariff 12.5 percent, for a total of 30.50 percent, and annual duties of 244,000 dollars. It also stated that no rate change is projected for this code and origin when the China exclusions end, and that the Section 232 layers are only detected by chapter for steel, aluminum and copper.

**Several origins.** `compare_origins` on the same code returned Mexico 20.50 percent (forced-labor layer at 10 percent, heading 9903.05.55), India 20.50 percent (9903.05.44), Vietnam 23.00 percent (9903.05.84), Thailand 23.00 percent (9903.05.77) and China 30.50 percent, with the USMCA assumption spelled out: goods entered free of duty under USMCA are exempt under U.S. note 52(h) and 9903.05.94, the tool cannot tell whether a good qualifies, so the layer is applied until the operator says otherwise.

## Installation

Claude Desktop or Cursor, one block:

```
{
  "mcpServers": {
    "tariffmonitor": {
      "command": "npx",
      "args": ["-y", "tariffmonitor-mcp"]
    }
  }
}
```

No API key and no account. The package calls the free public API at `https://adcreator-ai.com/api/tem`. It also ships an HTTPS mode that serves the identical tools at `/mcp` on a local port, so a team can run one instance and point several clients at it.

## Business Relevance

This is the first entry in the catalog that answers a product-level duty question rather than a shipment-level one. Plain Freight prices one all-in delivered-duty-paid number for a China to US shipment, EximAgent carries HS classification and compliance checks inside an import-export sales workflow, and both are catalogued. Neither lets an operator ask what a specific product would cost from five different countries before choosing a factory.

For a brand deciding next season's sourcing, that comparison is the decision.

## Integration with CorpusIQ

Duty is a cost input, so it belongs beside revenue and stock rather than in a separate spreadsheet. An operator connecting this server alongside a store and an accounting system can ask what a duty change does to gross margin on a product line, and get the rate and the ledger in one answer.

## Limitations

- United States only. No other country's tariff schedule is modelled.
- Section 232 detection is by chapter for steel, aluminum and copper only, so a downstream product using those inputs is not caught.
- Individual Section 301 exclusions are not modelled, which the answer says explicitly.
- USMCA, CAFTA-DR, civil aircraft and pharmaceutical exemptions depend on facts the tool cannot see, so they are returned as assumptions rather than settled rates.
- A missing MFN base rate is counted as zero and flagged as a possible understatement instead of being estimated.
- The answer ends with a generated explanation paragraph, and it can misread the code. In this sweep the structured stack was correct for HTS 6404112030 while the paragraph described the item as men's clothing. Read the rate stack and the headings, not the prose.
- The upstream is a third party's free API with no published SLA, and a rate is per code and origin, not a quote for a shipment.

## FAQ

### What does the tariff tool actually calculate?

The stacked ad valorem rate for one HTS line from one origin country: the MFN base rate, any Section 301 China list duty, Section 232 where the chapter is detected, and the 2026 Section 301 forced-labor layer, plus the yearly dollar cost when an import value is supplied.

### Can I compare sourcing countries for one product?

Yes. `compare_origins` takes one HTS code and several origin countries and returns the total for each, sorted cheapest first, with the heading cited for every layer that applied.

### Does it need an API key or a paid plan?

No. The npm package is MIT licensed and calls a free public endpoint. There is no account, no key and no per-call charge.

### How current is the rate data?

Every answer carries the date the underlying data was checked, and the tool names the Federal Register document behind each layer. The China exclusions end date is stated in the answer itself rather than assumed.

## See Also

- [Plain Freight MCP - Freight and Duty, One Delivered Price](/hermes/mcp/servers/external/plainfreight-mcp/)
- [EximAgent MCP - Export-Import Sales Team for Agents](/hermes/mcp/servers/external/eximagent-mcp/)
- [3Dsellers MCP - Six Marketplaces, 150+ Tools](/hermes/mcp/servers/external/3dsellers-mcp/)
