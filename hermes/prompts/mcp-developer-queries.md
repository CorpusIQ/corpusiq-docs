# MCP developer prompts

These prompts are written for developers using CorpusIQ as an MCP server
— either from Claude Desktop, a custom MCP client, or an agent pipeline.
They go beyond operator-level queries and focus on programmatic access,
cross-connector joins, debugging, and building CorpusIQ into larger
workflows.

If you're new to MCP, see [how-it-works/mcp-architecture.md](../how-it-works/mcp-architecture.md).

---

## Querying business data programmatically

### "List all tools available for the Shopify connector."

**MCP call:** `resolve_connector` with intent "list Shopify tools"
**What this does:** Returns the exact tool schemas callable against
Shopify. Useful as a discovery step before building a pipeline that
needs specific Shopify fields.
**Developer use case:** Enumerate available actions before generating
tool-call code in your agent.

---

### "Fetch all orders from the last 30 days and return them as structured JSON."

**Connectors used:** Shopify or Amazon Seller.
**MCP tool:** `get_orders` with `created_after` date param.
**What this does:** Returns raw order objects with line items, amounts,
statuses. The MCP layer returns typed JSON — no parsing of prose needed.
**Developer use case:** Feed order data into a downstream analytics
pipeline or a fine-tuning dataset.

---

### "Pull GA4 sessions by channel for the last 90 days, grouped by date."

**Connectors used:** GA4.
**MCP tool:** `run_report` with dimensions `["date", "sessionDefaultChannelGroup"]`
and metric `["sessions"]`.
**What this does:** Returns a per-day, per-channel session matrix.
**Developer use case:** Build a channel attribution table without a
separate BI tool.

---

### "Return QuickBooks P&L for Q1 as structured data."

**Connectors used:** QuickBooks.
**MCP tool:** `get_profit_loss` with `start_date` and `end_date`.
**What this does:** Returns income, cost of goods, expenses, and net
profit as a structured report object.
**Developer use case:** Ingest into a spreadsheet, dashboard, or
financial model automatically.

---

### "Get all active HubSpot deals with their amounts and pipeline stage."

**Connectors used:** HubSpot.
**MCP tool:** `list_hubspot_deals` with pagination.
**What this does:** Returns deal ID, name, amount, stage, and owner
for every open deal.
**Developer use case:** Build a pipeline forecast tool that refreshes
from live CRM data.

---

### "List every Klaviyo campaign sent in the last 60 days with open and click rates."

**Connectors used:** Klaviyo.
**MCP tool:** `get_campaigns` with `start_date` and `end_date`.
**What this does:** Returns campaign objects with recipient count, open
rate, click rate, and revenue attribution.
**Developer use case:** Automate an email performance report that runs
on a schedule.

---

## Cross-connector joins

### "Join Shopify order revenue to Meta Ads spend by date and compute ROAS."

**Connectors used:** Shopify, Meta Ads.
**MCP tools:** `get_orders` (Shopify) + `get_account_insights` (Meta Ads)
with matching date ranges.
**What this does:** Two separate MCP calls return parallel date-keyed
datasets. Your agent joins on date and computes ROAS = revenue / spend.
**Developer use case:** Build a custom attribution model that doesn't
rely on Meta's self-reported ROAS.

---

### "Compare GA4 sessions on email send days to non-send days."

**Connectors used:** Klaviyo, GA4.
**MCP tool (built-in cross-source):** `correlate_email_vs_web_traffic`.
**What this does:** Returns a day-level table: email sent (bool), GA4
sessions, delta from baseline.
**Developer use case:** Validate email's halo effect on organic traffic
before attributing it as a channel.

---

### "Join QuickBooks invoices to HubSpot deals to find deals that closed but were never invoiced."

**Connectors used:** HubSpot, QuickBooks.
**MCP tools:** `list_hubspot_deals` (filter: stage=closed-won) +
`list_invoices` (QuickBooks).
**What this does:** Two lists, joined on company name or amount. Gaps
are deals with no matching invoice.
**Developer use case:** Revenue leakage audit — catch won deals that
slipped through billing.

---

### "Pull every Stripe charge and match to QuickBooks income lines."

**Connectors used:** Stripe, QuickBooks.
**MCP tools:** `list_charges` (Stripe) + `get_profit_loss` or
`list_invoices` (QuickBooks).
**What this does:** Stripe returns raw charges; QuickBooks returns
booked income. Mismatches surface timing gaps or missing entries.
**Developer use case:** Automated reconciliation check — run daily in
a CI pipeline.

---

### "Show me Klaviyo list growth alongside Facebook ad spend to see if paid ads are growing my list."

**Connectors used:** Klaviyo, Meta Ads.
**MCP tool (built-in cross-source):** `correlate_form_signups_vs_ad_traffic`.
**What this does:** Returns form submit counts and Meta spend per day.
**Developer use case:** Validate paid-to-list growth attribution.

---

## Debugging connector issues

### "Why is my Shopify connector returning zero orders?"

**Connectors used:** Shopify.
**Debug approach:** Call `get_orders` with an explicit wide date range
(`created_after` = 90 days ago). If still zero, call
`get_connector_status` and check for token expiry or scope issues.
**Common causes:** Token revoked in Shopify admin, wrong store domain
configured, date filter is too narrow by default.

---

### "My GA4 report is returning empty rows — how do I debug it?"

**Connectors used:** GA4.
**Debug approach:** First call `list_accounts` to verify the property
is visible. Then call `list_properties` with the account ID. Then run a
minimal report: single dimension `date`, single metric `sessions`, last
7 days. If that works, add dimensions one at a time until the empty
response reappears.
**Common cause:** `property_id` has the format `properties/XXXXXXX` —
make sure you're passing just the numeric ID, not the full path.

---

### "Check whether my QuickBooks token is still valid."

**MCP tool:** `get_company_info` — this is the lightest QuickBooks
call. A valid token returns company name and fiscal year. An expired
token returns a 401 error, which tells you to re-authenticate via
`get_connector_status`.

---

### "List all connectors and their current auth status."

**MCP tool:** `get_connector_status` (no parameters).
**What this does:** Returns a table of every configured connector,
its auth state (connected / expired / not authenticated), and a
re-auth link where applicable.
**Developer use case:** Health check endpoint in an agent — run this
at session start to gate which connectors are usable.

---

### "Why are my Meta Ads impressions different between the account summary and the campaign-level report?"

**Connectors used:** Meta Ads.
**Debug approach:** `get_account_insights` aggregates across all
campaigns including deleted/archived. `list_campaigns` with `status_filter=ALL`
then `get_campaign_insights` per campaign will surface whether deleted
campaigns are inflating the account total.
**Fix:** Filter campaigns by `status_filter=ACTIVE` for apples-to-apples.

---

## Building agent workflows with CorpusIQ as the knowledge layer

### "Build an agent that answers CFO questions using live QuickBooks + Stripe data."

**Architecture:**
1. Connect Claude (or your LLM) to CorpusIQ MCP at `https://mcp2.corpusiq.io/mcp`.
2. Authenticate QuickBooks and Stripe connectors.
3. The agent calls `get_profit_loss`, `get_balance_sheet`, `list_charges`,
   and `get_balance` as needed, grounded in live data.
**No ETL required.** CorpusIQ handles the OAuth tokens, rate limiting,
and data normalization.

---

### "Build a daily business digest that fires at 8am and pulls from 5 connectors."

**Architecture:**
1. Cron job (or scheduler) sends a prompt to your MCP-connected LLM at 8am.
2. Prompt: "Run the executive snapshot skill."
3. CorpusIQ's `executive-snapshot` skill pulls QuickBooks, Shopify,
   HubSpot, ad accounts, and GA4 automatically.
4. The LLM returns a formatted digest. Push to Slack, email, or Notion.
**MCP skill trigger:** `invoke_skill` with `skill_name="executive-snapshot"`.

---

### "Build a Slack bot that answers revenue questions."

**Architecture:**
1. Slack bot receives a message like "how did we do last week?"
2. Bot forwards the message to an LLM with CorpusIQ MCP attached.
3. CorpusIQ calls Shopify + QuickBooks, returns structured revenue data.
4. LLM composes a Slack-formatted reply. Bot posts it.
**Key connector:** `get_profit_loss` + `get_orders` for revenue.
**Read-only guarantee:** CorpusIQ cannot post to Slack, only read.

---

### "Use CorpusIQ as the memory layer for a sales agent — give it access to all open deals and customer history."

**Architecture:**
1. Attach CorpusIQ MCP to your sales agent's LLM context.
2. On each call, the agent resolves which connectors to query via
   `resolve_connector`.
3. `list_hubspot_deals`, `get_hubspot_contact`, `list_invoices`
   (QuickBooks), and `list_gmail_messages` give the agent a 360-degree
   view of each account.
**Why MCP beats RAG here:** Data is live, not stale embeddings. The
agent always sees the current deal stage, latest invoice status, and
most recent email thread.

---

### "Expose CorpusIQ data to a custom dashboard without a backend."

**Architecture:**
1. Use any MCP client library (e.g. `@modelcontextprotocol/client-typescript`).
2. Connect to `https://mcp2.corpusiq.io/mcp` with your CorpusIQ JWT.
3. Call tools directly from your frontend or edge function.
4. Render the returned JSON in your dashboard components.
**No separate API to build.** CorpusIQ's MCP layer is the API.

---

### "Run a competitive SEO audit on demand from a CI pipeline."

**Connectors used:** Semrush, Search Console, GA4.
**MCP tools:** `get_domain_overview`, `get_competitors`, `get_performance`.
**Architecture:**
1. CI job calls your MCP-connected LLM with: "Run an SEO health check
   and flag any position drops > 5 places since last week."
2. CorpusIQ pulls live Semrush + GSC data, compares to prior run
   (stored in canonical facts), and returns a diff report.
3. CI job posts the report to Slack or opens a GitHub issue on regressions.


*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


*From the [Hermes Prompt Collection](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/prompts) — production prompts for AI agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
