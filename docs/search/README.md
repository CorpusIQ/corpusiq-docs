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
