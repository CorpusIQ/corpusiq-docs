---
title: "PubCrawl MCP - PubMed, Drug Labels and Trials for Agents"
description: "PubMed, Europe PMC, FDA and UK drug labelling and ClinicalTrials.gov for AI assistants, with US-UK label comparison and cited results."
category: Analytics & BI
stars: 15
added: 2026-09-29
source: mcpservers.org
relevance: ★★★
tags: [pubmed, drug-labels, clinical-trials, fda, healthcare, citations, literature, self-hosted]
---

# PubCrawl MCP

**Primary biomedical sources, directly inside your AI assistant.** PubCrawl connects Claude Desktop, Cursor or any MCP client to PubMed, Europe PMC (including preprints), FDA and UK drug labelling, and ClinicalTrials.gov. Every tool is a thin, deterministic wrapper over an official API - nothing invented, every result carrying its PMID, NCT ID or DOI. No API keys required.

```
Server type: Local stdio (npm)
Auth: None (optional free NCBI key raises PubMed rate limits)
Endpoint: npx -y @pharmatools/pubcrawl
Tools: 14 (literature search, abstracts, full text, drug labelling, US-UK label comparison, trials)
Pricing: Free (MIT)
Category: Analytics & BI
Built by: PharmaTools.AI (github.com/nickjlamb/pubcrawl)
```

## Why This Matters for Operators

The tool PubCrawl is known for is `compare_labels` - the only MCP tool that surfaces US versus UK drug labelling differences. Ask to compare labelling for a drug and it pulls the live US Prescribing Information from openFDA/DailyMed and the UK SmPC from the eMC, then maps equivalent sections side by side. A cardiovascular claim that is on-label in the US can promote an unlicensed indication in the UK; medical copy reviewers live inside that gap, and compare_labels makes it visible instead of assumed.

For everyone else, PubCrawl replaces open browser tabs: literature search with date and article-type filters, structured abstracts, open-access full text, related-article discovery, citation formatting in four styles, and trial lookup by condition, phase and recruitment status.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| search_pubmed | Search PubMed with date, article-type and sort filters; returns PMIDs, authors, journals, DOIs |
| search_europepmc | Search Europe PMC - broader corpus with preprints (bioRxiv, medRxiv) and patents |
| get_abstract | Structured abstract in labelled sections, with keywords and MeSH terms |
| get_full_text | Open-access full text from PubMed Central with parsed sections and captions |
| find_related | Similar articles via PubMed's neighbor algorithm, ranked by relevance |
| format_citation | APA, Vancouver, Harvard or BibTeX citation formatting |
| trending_papers | Recent papers on a topic, optionally filtered to high-impact journals |
| resolve_drug_name | Brand to generic (or reverse) via RxNorm/openFDA, with drug class and indications |
| get_uspi | US Prescribing Information sections via openFDA, cited to DailyMed |
| get_smpc | UK Summary of Product Characteristics from the eMC, with numbered sections |
| compare_labels | Side-by-side US versus UK labelling with equivalent sections paired |
| search_by_indication | Drugs approved for a condition, with UK availability cross-referenced |
| search_trials | ClinicalTrials.gov search by condition, intervention, status and phase |
| get_trial | Full trial record by NCT ID: eligibility, design, arms, outcomes, locations |

## Installation

```bash
claude mcp add pubcrawl -- npx -y @pharmatools/pubcrawl
```

No install step beyond npx; it fetches on first run. An optional free NCBI API key (ncbi.nlm.nih.gov) raises PubMed rate limits for heavy use.

## Configuration

```json
{
  "mcpServers": {
    "pubcrawl": {
      "command": "npx",
      "args": ["-y", "@pharmatools/pubcrawl"]
    }
  }
}
```

## Business Relevance

- **Medical copy and regulatory reviewers** check that claims are on-label in each market with compare_labels instead of manual SmPC reading
- **Pharma and medtech operators** track literature and preprints for a compound with cited, verifiable results
- **Clinical research teams** build trial landscapes with filters for phase, status and intervention
- **Consultants and analysts** produce cited evidence packs in client-ready citation styles

## Integration with CorpusIQ

PubCrawl covers the scientific record while CorpusIQ covers the business-data layer. A composed workflow: CorpusIQ pulls commercial context through its connectors - revenue, spend, pipeline - while PubCrawl grounds the clinical story in primary sources, and the two feeds join in one assistant session. For market-expansion work, pair CorpusIQ data with PubCrawl's US-UK label comparison to catch on-label versus off-label gaps before copy ships.

## Limitations

- Local stdio server; no hosted endpoint for teams without Node tooling
- Biomedical scope only - no general web search or business news
- PubMed rate limits apply without a free NCBI key
- Young project (15 GitHub stars); literature retrieval is gated by OpenGATE in CI, labelling and trials by an in-repo fidelity benchmark

## FAQ

### Does it need API keys?

No. Every tool runs without keys; an optional free NCBI key raises PubMed rate limits. Results always cite their PMID, NCT ID or DOI.

### How is compare_labels different from reading the labels myself?

It fetches both live labels and maps equivalent sections - US Indications and Usage against UK section 4.1 - so differences are paired side by side, with missing sides explained and truncated sections flagged.

### Which clients does it work with?

Any MCP client. The quick start documents Claude Desktop; the same npx command works in Cursor, Codex and other MCP-compatible tools.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
