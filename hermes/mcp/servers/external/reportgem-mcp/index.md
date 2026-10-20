---
title: "ReportGem MCP - 16 Million Investment Bank Reports"
description: "ReportGem MCP searches 16 million global investment bank reports plus filings and earnings calls, returning page-cited excerpts agents can quote."
category: Finance
stars: 0
added: 2026-10-20
source: "mcp.so /feed page 1 (card posted 2026-10-20T01:40:36Z)"
relevance: ★★★
tags: [finance, investment-research, equity-research, sec-filings, earnings-calls, document-search, remote-mcp, oauth]
---

# ReportGem MCP

**Sell-side research is the most expensive document set per page and the least reachable by an agent. This one puts 16 million broker reports behind five tools that return the page, not a summary of the page.**

```
Server type: Remote (Streamable HTTP) at https://www.reportgem.com/mcp
Auth: OAuth with a free ReportGem account for reads; titles, URLs and failed or empty results are not charged
Live check: unauthenticated POST initialize returned HTTP 200, and tools/list returned the five tools named below (this sweep)
Registry: com.reportgem/global-research
Vendor: ReportGem (报告驿站), reportgem.com, with a Chinese-language front end at nash-ai.cn
```

## Why This Matters for Operators

An agent that can search the open web can find a headline about what a bank said. It cannot hand you the page the sentence came from. That distinction is the whole difference between a research note and a citation, and it is why investment professionals still pay for document terminals instead of asking a chatbot.

The coverage here is unusually wide for an MCP server: 16 million plus global investment bank reports from Goldman Sachs, Citi, HSBC, UBS, JPMorgan, Morgan Stanley, Barclays and Nomura with same-day realtime coverage and Chinese titles and translations, 5 million plus reports from 200 plus Chinese brokers and futures houses, 500,000 plus China company filings, SEC filings across 10-K, 10-Q, 8-K, 6-K and 20-F, earnings-call notes, academic papers, and the charts and tables inside the reports themselves.

For a business operator the practical use is competitive and financial intelligence with a source you can open: what a competitor's suppliers are saying about pricing, what the sell side models for a category you are entering, what management actually said on the last call.

## The Five Tools

| Tool | What it returns |
|---|---|
| `search_research` | Reports and papers by company, ticker, industry, theme or keyword, with source groups for global research, realtime research, Chinese research and academic papers, plus date bounds |
| `search_filings` | SEC and China company filings with verifiable internal source links, filterable by market and form type |
| `search_meetings` | Global and Chinese meeting notes and earnings-call records, distinguishing body evidence from index hits |
| `search_visuals` | Charts, tables, industry diagrams and research-relevant images with report and page provenance |
| `get_evidence` | Bounded real excerpts, or a continuous reading window for a whole document |

The behavioural detail that earns the entry is in the server's own instructions: prefer `get_evidence` before making a material or numeric claim, always preserve the returned source URL and page reference, and never present a document with no match as verified evidence. That is a citation contract rather than a search endpoint.

## Pricing and Limits

New accounts get 10 free credits, roughly 100,000 returned tokens, valid 30 days. Billing is by delivered content only: one credit per 10,000 returned tokens, and titles, URLs, failed or empty results are free. Packages run 400 credits for ¥169, 1,300 for ¥299 and 3,000 for ¥499, each valid 30 days with no auto-renewal.

Two honest limits. The interface and much of the coverage are Chinese-first, so an English-only workflow will see translated titles rather than native ones. And the reports are other publishers' copyrighted work: the service returns excerpts for your own research, and republication is a question for the publishers, not for the API.

## FAQ

### Is this different from an equity data feed?

Yes, and the difference is the unit of information. A market data feed returns numbers; this returns the document a person wrote around the numbers, with the page it came from. This catalog already carries read-only US equity research and screening ([fAlpha MCP](/hermes/mcp/servers/external/falpha-mcp)); this is the sell-side library behind the analysis.

### Does it work without an account?

`initialize` and `tools/list` answer without credentials, which is how the tool surface was verified here. Actual searches require the OAuth login and consume credits.

### Can an agent quote a report confidently?

Only if it follows the returned provenance. Every result carries a source URL and page reference, and the server instructs clients to keep them. A claim without the citation is the fetch you are trying to avoid.

### What is the best first question?

Something narrow and checkable: a named bank's view on a named company this week, a specific chart, or what management said about capacity on the last call. Broad theme questions return too many titles and burn credits on reads you did not need.

## See Also

- [fAlpha MCP - Read-Only US Equity Research for Agents](/hermes/mcp/servers/external/falpha-mcp)
- [Signal Nodus SEC Filings MCP](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
