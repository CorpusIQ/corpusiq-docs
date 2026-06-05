# Changelog

What's shipped to production, newest first. Customer-facing changes only —
internal refactors and infrastructure work live in the engineering tracker, not
here. Dates are when the change went live on production.

This is a curated log. For the full commit-level history, see the
[multi-source-mcp repo](https://github.com/CorpusIQ/multi-source-mcp).

---

## June 2026

### New features

- **Metric Spec Registry** — declare a business number once (MRR, AOV,
  active customers, whatever), with the recipe written in a small DSL
  that resolves live against your connector data. Every AI client gets
  the same answer, every time, with a one-line provenance footer and
  optional cross-source drift checks against a peer metric. No
  warehouse, no caching — just a definition the system honors
  consistently. Read the onboarding guide:
  [how-it-works/metric-specs.md](../how-it-works/metric-specs.md).
- **Drift report tool** — `metric_spec_drift_report` walks every spec
  with a `cross_source_checks` peer set and surfaces only the pairs
  currently outside their tolerance. Useful when Stripe and QuickBooks
  disagree about recurring revenue and you want to know before the
  board call.
- **Soft eval gate with surfaced warnings** — specs whose golden-value
  eval doesn't match get saved anyway, but the warnings ride along on
  every answer derived from that spec. Silent acceptance defeats the
  purpose; loud warnings beat hidden ones.

---

## May 2026

### New connectors

- **Close** — Close CRM. Leads, opportunities, and sales-pipeline questions.
- **Notion** — your workspace wiki and databases as a queryable source.
- **Stripe** — payment intelligence: charges, payouts, reconciliation, customer
  revenue. Reconciliation tooling expanded over several releases.
- **LinkedIn Ads** — B2B ad performance alongside your other ad accounts.
- **PostHog** — product analytics: funnels, events, retention.
- **Ahrefs** and **Semrush** — SEO: backlinks, keyword positions, competitor
  visibility.
- **GunBroker** and **eBay** — marketplace seller accounts: listings, orders,
  sell-through.

### Reliability & correctness

- **Multi-replica OAuth state** — reworked how login and connector-auth state is
  stored so it's shared across server instances. Fixes intermittent "invalid
  state" and spurious sign-out errors under load. (A large multi-phase effort
  across the month.)
- **Device-login fix** — resolved an outage on the Claude/ChatGPT device-login
  path and added guardrails so that class of bug can't recur silently.
- **Google account-mismatch fix** — connecting a Google source now correctly
  binds to the account you actually authorized, even if you're signed into
  several.
- **Per-connector error surfacing** — when a vendor returns an error (rate
  limit, expired token, no data), CorpusIQ now tells you what happened instead
  of returning an empty result. No more silent blanks.

### Platform

- **Public tokens-saved counter** — the running estimate of tokens CorpusIQ has
  saved across all users is now exposed as a public, PII-free endpoint
  (`/api/v1/usage/public-counter`). The badge at the top of this docs site is
  live data, refreshed every 5 minutes. (Phase B of the docs/community surface.)
- **Usage stats** — see what you've asked, which connectors you lean on, and an
  estimate of the tokens CorpusIQ saved your assistant by fetching data
  directly. Ask: *"show me my CorpusIQ usage."*
- **Canonical Layer** — declare authoritative business facts (your real MRR
  definition, your fiscal calendar, your pricing) so answers stay consistent
  across sources.

---

## A note on this log

We started keeping a public changelog in May 2026. Connectors and fixes that
predate it aren't all listed individually — the [Connectors index](../connectors/)
is the source of truth for everything currently live. Going forward, every
customer-facing change lands here.

Want to know when something specific ships? Watch the
[Roadmap](../roadmap/) or subscribe to the **Announcements** category in
[Discussions](https://github.com/CorpusIQ/corpusiq-docs/discussions).

Powered by CorpusIQ.
