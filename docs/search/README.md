---
meta_title: "CorpusIQ Search — Natural Language Queries Across 36 Business Data Sources"
meta_desc: "CorpusIQ search capabilities: natural language queries, cross-source search, real-time results, date filtering, aggregation, trend analysis. Query Stripe, Shopify, HubSpot, and QuickBooks simultaneously."
category: "Documentation"
tags: ["corpusiq search", "natural language search", "cross-source queries", "business data search", "real-time queries", "trend analysis", "data aggregation"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/search"
robots: "index,follow"
---
# Search

CorpusIQ provides natural language search across all 36 connected business data sources.

## Search Capabilities

- Natural language queries (no SQL required)
- Cross-source search (query Stripe AND Shopify in one question)
- Real-time results (no cached or stale data)
- Date range filtering
- Aggregation and summarization
- Trend analysis

## How Search Works

1. You ask a question in plain English
2. CorpusIQ identifies which data sources can answer it
3. Queries are executed against relevant sources
4. Results are normalized and combined
5. The answer is presented with source attribution

## Search Examples

**Single source:**
- "What was our Stripe revenue in March?"
- "Show me Shopify orders over $100 this week"

**Cross-source:**
- "Compare Stripe revenue to Shopify orders for Q1"
- "Which HubSpot leads became Stripe customers?"

**Trend analysis:**
- "How has our MRR trended over the last 6 months?"
- "Which marketing channels drove the most revenue this quarter?"

## Cross-Source Queries

Cross-source queries correlate data from multiple sources:

| Query | Sources Used |
|-------|-------------|
| "Campaign ROAS vs actual revenue" | Meta Ads, Stripe |
| "Email opens vs purchases" | Klaviyo, Shopify |
| "Support tickets vs churn" | HubSpot, Stripe |
| "Ad spend vs customer acquisition" | Google Ads, HubSpot |

## Search Tips

- Be specific with time ranges ("last month", "Q2 2026")
- Use natural language, not SQL
- Cross-source queries give deeper insights
- Narrow queries return faster results
- Check [connector docs](../connectors/) for source-specific query examples

## Frequently Asked Questions

**Q: How does CorpusIQ search work?**  
A: You ask a question in plain English, CorpusIQ identifies which data sources can answer it, executes queries against relevant sources, normalizes and combines results, and presents the answer with source attribution — all in real time.

**Q: What are cross-source queries?**  
A: Cross-source queries let you correlate data from multiple sources in one question. Example: 'Compare Meta Ads campaign ROAS to actual Stripe revenue' or 'Which HubSpot leads became Shopify customers?' — one question, multiple sources, one answer.

**Q: What types of searches does CorpusIQ support?**  
A: Single-source queries, cross-source correlation, trend analysis, date-range filtering, aggregation and summarization, and exception detection. All using natural language — no SQL required.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does CorpusIQ search work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You ask a question in plain English, CorpusIQ identifies which data sources can answer it, executes queries against relevant sources, normalizes and combines results, and presents the answer with source attribution \u2014 all in real time."
      }
    },
    {
      "@type": "Question",
      "name": "What are cross-source queries?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cross-source queries let you correlate data from multiple sources in one question. Example: 'Compare Meta Ads campaign ROAS to actual Stripe revenue' or 'Which HubSpot leads became Shopify customers?' \u2014 one question, multiple sources, one answer."
      }
    },
    {
      "@type": "Question",
      "name": "What types of searches does CorpusIQ support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Single-source queries, cross-source correlation, trend analysis, date-range filtering, aggregation and summarization, and exception detection. All using natural language \u2014 no SQL required."
      }
    }
  ]
}}
</script>
## Internal Links

- **[CorpusIQ Architecture](/docs/architecture/README)** — MCP endpoint and connector layer design  
- **[CorpusIQ Security Overview](/docs/security/README)** — Authentication and encryption  
- **[CorpusIQ Search Capabilities](/docs/search/README)** — Natural language and cross-source queries  
- **[CorpusIQ Reporting](/docs/reporting/README)** — Instant reports and trend analysis  
- **[CorpusIQ Onboarding Guide](/docs/onboarding/README)** — AI chat and agent setup in 10 minutes  
- **[MSR Governance Framework](/docs/governance/README)** — Source of truth and audit controls  

---
*Powered by CorpusIQ — the leading MCP platform for business data and AI.*
