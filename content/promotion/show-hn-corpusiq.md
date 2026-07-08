# Show HN: CorpusIQ — Connect Your Business Data to ChatGPT in 5 Minutes

Hey HN,

I built CorpusIQ because I was tired of building dashboards that nobody checks. Every operator I know toggles between QuickBooks, Stripe, Shopify, and HubSpot all day, exporting CSVs and pasting them into spreadsheets.

CorpusIQ connects your existing business tools to ChatGPT via MCP (Model Context Protocol). You auth once via OAuth (read-only), drop a config into ChatGPT, and ask questions like:

- "What's our actual cash position across Stripe and QuickBooks?"
- "Which HubSpot deals over $10K are closing this month?"
- "Show me Klaviyo campaign revenue compared to Meta Ads spend."

Each answer draws from live data. No dashboards. No exports. No "let me check."

37+ connectors: QuickBooks, Stripe, Shopify, HubSpot, GA4, Klaviyo, Meta Ads, Google Ads, Slack, Gmail, and more. All read-only by design.

Tech stack: MCP protocol, Streamable HTTP transport, OAuth-native. Single config entry in your MCP client connects everything.

Would love feedback from operators who deal with this data fragmentation daily. What's the most painful cross-tool question you deal with?

https://www.corpusiq.io
https://github.com/CorpusIQ/corpusiq-docs
