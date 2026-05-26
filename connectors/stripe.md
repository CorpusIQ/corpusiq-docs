# Stripe

## What it unlocks
See your payment activity inside the conversation. Ask which customers paid this month, what your charge history looks like, why your last payout doesn't match the sum of charges, or whether a specific email shows up in your customer list — without leaving the chat or opening the Stripe dashboard.

If you keep your books in QuickBooks, CorpusIQ can now reconcile Stripe payouts against your bank deposits in conversation — the same exercise your bookkeeper does every month, in plain English.

## Before you connect
- A Stripe account (test or live mode both work).
- A **restricted API key** with read-only access on the resources listed below. Don't use your secret key — restricted keys are revocable per-scope and safer for AI integrations.
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
   - **Balance** → Read
   - **Balance transactions** → Read
   - **Payouts** → Read
   - **Refunds** → Read
   - **Disputes** → Read
7. Click **Create key**. Stripe shows the key once — copy it now (it starts with `rk_live_…` in live mode or `rk_test_…` in test mode).
<!-- screenshot: Stripe key reveal screen -->
8. Open your CorpusIQ dashboard and click **Connections**.
9. Find Stripe and click **Connect**.
10. Paste the restricted key and save.
<!-- screenshot: CorpusIQ Stripe API key form -->

You'll see Stripe change from gray to green in your CorpusIQ dashboard.

> **Already connected under an older key?** If you set up Stripe before May 2026, your restricted key probably only has Charges, Customers, and Accounts checked. The new reconciliation questions need five additional Read scopes. Edit the existing key in the Stripe dashboard and add Balance, Balance transactions, Payouts, Refunds, and Disputes — or create a fresh key with the full list above. Either path works; no CorpusIQ-side change required.

## What CorpusIQ can see
- **Account profile** — business name, country, default currency, capabilities.
- **Charges** — payments collected, with amounts, currency, status (succeeded / pending / failed), customer attribution, and timestamps.
- **Customers** — customer list with emails, names, balances, and creation dates. Filterable by exact-match email.
- **Payouts** — money Stripe sent to your bank account. Status (pending / paid / failed / in_transit), arrival date, method (standard or instant), and amount.
- **Balance transactions** — the canonical Stripe ledger. Every charge, refund, fee, and payout as one continuous timeline. Filterable by payout, which means CorpusIQ can answer "show me exactly what aggregated into yesterday's bank deposit."
- **Refunds** — refunds as first-class records (amount, reason, status, linked charge), not just a flag on the original charge.
- **Disputes** — chargebacks with status, reason, and evidence-due-by deadlines.
- **Balance** — your current available and pending balances, including instant-payout availability if you have it enabled.

Read-only. CorpusIQ never issues refunds, modifies subscriptions, or moves money. The restricted-key scopes enforce this at Stripe's side — the connector physically cannot perform write operations even if asked.

## Questions you can ask

### Day-to-day payments
- "How much did we collect on Stripe last week?"
- "Show me failed charges from the last 7 days."
- "Find the Stripe customer with email alice@example.com."
- "What account am I connected to on Stripe?"
- "List my 20 newest Stripe customers."
- "How many charges came in today?"

### Reconciliation
- "What's my current Stripe balance and how much is pending payout?"
- "Show me Stripe payouts from October."
- "When does my next payout arrive in the bank?"
- "Why doesn't last week's Stripe payout match the sum of charges?"
- "Show me every fee Stripe charged me in October."
- "What was in payout `po_1Oa2b3...`?" (the answer is every single charge, refund, and fee that rolled up into that one bank deposit)

### Refunds and disputes
- "Show me refunds from the last 30 days."
- "Which charges got refunded last month?"
- "List open Stripe disputes."
- "Which disputes need evidence in the next 7 days?"
- "What was the reason on dispute `du_1Oa2b3...`?"

## Cross-source questions
Stripe pairs cleanly with other connectors for richer questions:
- "Reconcile my Stripe payouts against QuickBooks deposits last month" (Stripe + QuickBooks). The reconciliation block makes this real — same exercise your bookkeeper runs at month-end.
- "Compare Stripe revenue to Shopify orders this week" (Stripe + Shopify)
- "Show me Shopify orders where the Stripe charge ended up in a dispute" (Stripe + Shopify)
- "Which Klaviyo email campaigns drove the most Stripe revenue last month?" (Stripe + Klaviyo)
- "GA4 purchase events vs Stripe successful charges yesterday — where's the gap?" (Stripe + GA4 — surfaces analytics tagging failures)
- "What's our current cash position across Stripe balance and QuickBooks bank accounts?" (Stripe + QuickBooks)

## Troubleshooting

**"Stripe permission denied" on a specific tool**
The restricted key may be missing a scope the tool needs. This is the most common error after a connector upgrade — the new reconciliation tools each need their own Read scope (Balance, Balance transactions, Payouts, Refunds, Disputes). The error message will say something like *"Having the 'rak_xxx' permission would allow this request to continue"* — go back to the Stripe dashboard, edit the key, and add the missing scope. Save, then retry.

**`get_stripe_account` returns 403 even though "Accounts → Read" is set**
This is a known nuance with some Stripe account types. The "Accounts → Read" toggle in the dashboard does not always grant the specific `rak_accounts_kyc_basic_read` permission that `/v1/account` requires. The other Stripe tools work normally — only the account-profile tool is affected. If you need the account details and the toggle isn't enough, contact Stripe support to ask about granting `rak_accounts_kyc_basic_read` explicitly on your account type.

**"API key invalid" or "API key expired"**
The restricted key was deleted or rotated in the Stripe dashboard. Create a fresh restricted key and re-save it in CorpusIQ via the Connections page.

**"No charges in date range" / "No payouts in date range"**
Not an error — Stripe genuinely returns zero results when there's no activity in the window you asked about. Try a wider date range or check the Stripe dashboard to confirm.

**Stripe rate limit (429)**
Stripe allows ~100 requests/second on live mode (~25 on test mode). Heavily paginated queries can hit this. The connector retries automatically with backoff; if it persists, ask narrower questions or limit pagination depth.

**Payout total doesn't match my QuickBooks deposit**
That's exactly the question the reconciliation tools were built for. Ask CorpusIQ "show me every balance transaction in payout `po_xxx`" — you'll see the charges, refunds, and fees that aggregated into that one deposit, broken out by type. Stripe fees, instant-payout fees, and refunds issued during the payout window are the usual culprits.

## Key revocation
You control access. To remove CorpusIQ's access to Stripe, go to **Developers → API keys** in your Stripe dashboard, find the restricted key, and click **Delete** (or **Revoke**). CorpusIQ will get a `401 api_key_expired` error on the next call and report it to you — no further coordination needed.

## What's still on the roadmap
- **Subscriptions and invoices** as first-class objects — for SaaS billing analysis. Planned next.
- **Single-resource drill-downs** for charges and customers (today you can list them; soon you'll be able to ask for one specific charge or customer's full detail).
- **Modern payment objects** — payment intents, checkout sessions, payment links. For newer integrations that don't use the legacy charges object directly.
- **Stripe Connect OAuth** for agencies managing multiple Stripe accounts.
- **Write tools** for refunds and subscription mutations, gated by an explicit human-approval step.
- **Webhook ingestion** for real-time payment events (currently pull-only).
- **Stripe Sigma / custom Reports API** — likely out of scope; ask if you need it.

If you need any of the above sooner, ask CorpusIQ support.
