# Stripe

## What it unlocks
See your payment activity inside the conversation. Ask which customers paid this month, what your charge history looks like, or whether a specific email shows up in your customer list — without leaving the chat or opening the Stripe dashboard.

## Before you connect
- A Stripe account (test or live mode both work).
- A **restricted API key** with read-only access on Charges, Customers, and Accounts. Don't use your secret key — restricted keys are revocable per-scope and safer for AI integrations.
- About 3 minutes.

## How to connect
1. Log into [dashboard.stripe.com](https://dashboard.stripe.com).
2. Pick the account and mode (test or live) you want CorpusIQ to read.
3. Navigate to **Developers → API keys**.
4. Scroll to the **Restricted keys** section and click **Create restricted key**.
<!-- screenshot: Stripe restricted-key creation -->
5. Name it something recognizable (e.g. `CorpusIQ read-only`).
6. Set permissions to **None** by default, then flip exactly these rows to **Read**:
   - **Charges** → Read
   - **Customers** → Read
   - **Accounts** → Read
7. Click **Create key**. Stripe shows the key once — copy it now (it starts with `rk_live_…` in live mode or `rk_test_…` in test mode).
<!-- screenshot: Stripe key reveal screen -->
8. Open your CorpusIQ dashboard and click **Connections**.
9. Find Stripe and click **Connect**.
10. Paste the restricted key and save.
<!-- screenshot: CorpusIQ Stripe API key form -->

You'll see Stripe change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- Account profile: business name, country, default currency, capabilities.
- Charges: payments collected, with amounts, currency, status (succeeded / pending / failed), customer attribution, and timestamps.
- Customers: customer list with emails, names, balances, and creation dates. Filterable by exact-match email.

Read-only. CorpusIQ never issues refunds, modifies subscriptions, or moves money. The restricted-key scopes enforce this at Stripe's side — the connector physically cannot perform write operations even if asked.

## Questions you can ask
- "How much did we collect on Stripe last week?"
- "Show me failed charges from the last 7 days."
- "Find the Stripe customer with email alice@example.com."
- "What account am I connected to on Stripe?"
- "List my 20 newest Stripe customers."
- "How many charges came in today?"
- "Did Stripe charge customer_id `cus_XYZ` this month?"

## Cross-source questions
Stripe pairs cleanly with other connectors for richer questions:
- "Compare Stripe revenue to Shopify orders this week" (Stripe + Shopify)
- "Which Klaviyo email campaigns drove the most Stripe charges?" (Stripe + Klaviyo)
- "Reconcile my Stripe payouts against QuickBooks deposits" (Stripe + QuickBooks)

## Troubleshooting

**"Stripe permission denied" on a specific tool**
The restricted key may be missing a scope the tool needs. The error message will say something like *"Having the 'rak_xxx' permission would allow this request to continue"* — go back to the Stripe dashboard, edit the key, and add the missing scope. Save, then retry.

**`get_stripe_account` returns 403 even though "Accounts → Read" is set**
This is a known nuance with some Stripe account types. The "Accounts → Read" toggle in the dashboard does not always grant the specific `rak_accounts_kyc_basic_read` permission that `/v1/account` requires. The other Stripe tools (Charges, Customers) work normally — only the account-profile tool is affected. If you need the account details and the toggle isn't enough, contact Stripe support to ask about granting `rak_accounts_kyc_basic_read` explicitly on your account type.

**"API key invalid" or "API key expired"**
The restricted key was deleted or rotated in the Stripe dashboard. Create a fresh restricted key and re-save it in CorpusIQ via the Connections page.

**"No charges in date range"**
Not an error — Stripe genuinely returns zero results when there's no activity in the window you asked about. Try a wider date range or check the Stripe dashboard to confirm.

**Stripe rate limit (429)**
Stripe allows ~100 requests/second on live mode (~25 on test mode). Heavily paginated queries can hit this. The connector retries automatically with backoff; if it persists, ask narrower questions or limit pagination depth.

## Key revocation
You control access. To remove CorpusIQ's access to Stripe, go to **Developers → API keys** in your Stripe dashboard, find the restricted key, and click **Delete** (or **Revoke**). CorpusIQ will get a `401 api_key_expired` error on the next call and report it to you — no further coordination needed.

## What's not in v1
- Stripe Connect OAuth (for agencies managing multiple Stripe accounts) — planned for v2
- Write tools (issuing refunds, modifying subscriptions) — out of scope unless a customer asks for it
- Webhook ingestion (real-time payment events) — currently pull-only
- Additional read tools (payment intents, subscriptions, invoices, payouts, balance, revenue summaries) — planned for v2
- Stripe Sigma / custom Reports API — likely out of scope

If you need any of the above sooner, ask CorpusIQ support.
