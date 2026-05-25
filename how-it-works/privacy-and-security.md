# Privacy and security

The short version: CorpusIQ reads your business data when you ask it to,
stores nothing it doesn't need, and lets you disconnect at any moment.
It never writes to your vendor accounts. It never sells or resells your
data to anyone.

This page is plain English. The technical version lives in the
authentication and architecture docs.

## What CorpusIQ does NOT do

- It does **not** sell your data. There is no advertising business, no
  third-party data resale, no aggregated-anonymized-data side business.
- It does **not** train AI models on your data. Your tokens and your
  query results stay scoped to your account.
- It does **not** write to your vendor accounts. Every connector is
  authenticated with **read-only** scopes. CorpusIQ cannot place an
  order in Shopify, send an email in Klaviyo, or post a message in
  Slack.
- It does **not** copy your data into a giant warehouse. When you ask a
  question, CorpusIQ queries your tools live, uses the result to answer
  you, and discards it.
- It does **not** share data across tenants. Your tokens and data are
  isolated to your user account. Other CorpusIQ users cannot see them.

## What CorpusIQ does

**Authenticates each connector via OAuth.** You log in with the vendor
(Google, Shopify, QuickBooks) — not with CorpusIQ. The vendor shows you
the exact permissions being requested and you approve. CorpusIQ never
sees your vendor passwords.

**Stores your access tokens encrypted.** Tokens are held in Azure Key
Vault and encrypted at rest. They are keyed to your CorpusIQ user
identity and not accessible to other users or to CorpusIQ staff in plain
text.

**Reads only what a query needs.** When you ask "what were last week's
Shopify orders?", CorpusIQ asks Shopify for last week's orders.
Nothing more.

**Refreshes tokens automatically.** Most OAuth tokens expire every hour.
CorpusIQ uses the refresh-token flow (where the vendor provides one) so
you don't have to re-authenticate constantly. The refresh token is also
encrypted at rest.

**Honors disconnect immediately.** When you disconnect a connector,
CorpusIQ deletes the stored token. Future requests to that connector
fail until you reconnect. Most vendors also let you revoke the
authorization from their own admin panel.

## Where the data is

CorpusIQ runs on Microsoft Azure. Tokens are in Azure Key Vault. Logs
are in Azure with standard retention. The infrastructure is multi-tenant
but the data is single-tenant per user — every read uses your user
identity to scope the query.

## Authentication, in two layers

There are two authentications happening when you use CorpusIQ. They are
independent.

**Layer 1 — Who you are to CorpusIQ.** You sign into CorpusIQ once. This
gives you an identity token. Every request you make from Claude or
ChatGPT carries that identity so CorpusIQ knows it's you.

**Layer 2 — CorpusIQ's link to each vendor.** Separately, each connector
holds its own OAuth token scoped to your CorpusIQ identity. When you
ask a question, CorpusIQ looks up the right vendor token, makes the
read-only call, and returns the result.

If Layer 1 fails, you can't use CorpusIQ at all. If Layer 2 fails for a
specific connector (token expired, vendor revoked, scopes changed),
only that connector stops working — the others are unaffected.

## What the AI assistant sees

When you ask Claude or ChatGPT a question through CorpusIQ, the
assistant only sees:

- The tools CorpusIQ exposes to it (the connectors you've authorized).
- The query results CorpusIQ returns for the specific question.

The assistant does not see your raw tokens. It does not have direct
network access to Shopify or QuickBooks. Every external call goes
through CorpusIQ's server, which enforces the read-only contract.

## What to do if something feels wrong

- **Disconnect first, ask questions later.** Disconnect from the
  CorpusIQ status panel and the token is gone. You can reconnect any
  time.
- **Revoke from the vendor side too.** Google, Microsoft, Shopify, and
  most other vendors have a "Connected apps" page where you can revoke
  CorpusIQ's access directly. That's belt and suspenders.
- **Email security questions to the CorpusIQ team.** They get answered.

## Disconnect anytime

This is the bottom line: CorpusIQ only works for as long as you let it.
Pull the plug on any connector at any time and it stops reading that
tool immediately. No retention. No "but we already have a copy."

That's the deal.
