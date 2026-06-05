# Metric Specs

A metric spec is a small, user-declared recipe for one business number. You
write it once. CorpusIQ resolves it live every time anyone asks for that
number across Claude, ChatGPT, or any other MCP client pointed at your
account. The number is computed the same way every time, against current
vendor data, with a one-line audit trail attached.

This page is the onboarding guide. By the end you should be able to declare
your first spec, ask Claude for its value, read the provenance footer, and
know what the warnings mean when they show up.

## What is a metric spec?

A metric spec describes **how to compute** a number. It does not store the
number, and it does not store any of the underlying data. The next call
runs against fresh vendor responses. There is no warehouse and no cache.

A spec has a key (`mrr`), a label (`Monthly Recurring Revenue`), a
description (the paragraph you wrote so future-you remembers what counted),
an expression in the mini-DSL (the actual recipe), an expected unit, and
some optional bookkeeping (ownership, freshness budget, cross-source peers).

Specs are not the same thing as Truth Sources. A Truth Source tells the
system *where the answer lives* — your finance workbook, your KPI doc,
your CEO's head. A metric spec tells the system *how to compute the
answer* from connector data. Both flavors live in the same Canonical
store, with the same versioning and approval gates. When the same key
has both a spec and a truth source, the spec wins by default. (There's a
forward-compat flag for flipping that, covered in the pitfalls section.)

## Why we built this

Anthropic published a story about how they unify analytics on top of a
single warehouse with a semantic layer that compiles to SQL. The semantic
layer is the only place "MRR" is defined; every dashboard, prompt, and
report dereferences the same definition. They call the absence of
ambiguity "no drift."

We can't ship that architecture. CorpusIQ doesn't have a warehouse, by
design — we never copy your data. We talk to 30+ vendor APIs live, on
every request. Two of those vendors will sometimes disagree about a
number (your Stripe MRR and your QuickBooks recurring revenue won't
always reconcile, and that's interesting), and we want to surface that
honestly rather than pretending one of them is right.

So we kept Anthropic's idea — the user-declared computation is the
canonical definition — and changed the substrate. The DSL compiles to
connector tool calls, not SQL. Lineage is a graph of vendor reads, not
tables. Drift is vendor-vs-vendor disagreement we expose, not stale views.

Same outcome (you trust the number). Smaller surface area. No
storage-tenet betrayal.

## Anatomy of a spec

Here's `monthly_paid_revenue_stripe.json` from the starter template pack.
Every field annotated.

```json
{
  "key": "monthly_paid_revenue_stripe",
  "label": "Monthly Paid Revenue (Stripe)",
  "description": "Sum of successful Stripe charge amounts in the trailing 30 days. Includes one-time charges, recurring subscription charges, and metered overages — anything Stripe successfully captured. Excludes failed, pending, and refunded charges.",
  "expression": "stripe.list_charges(status=\"succeeded\", days_back=30).aggregate(sum, field=amount)",
  "expected_unit": "USD",
  "expected_freshness": "daily",
  "cross_source_checks": [],
  "tolerance_percent": 0.0,
  "owner_email": "",
  "last_reviewed_at": "",
  "variables": {},
  "prefer_truth_source": false
}
```

| Field | What it does |
|---|---|
| `key` | Stable identifier the AI uses when calling `metric_spec_resolve`. Lowercase, underscores. Pick a name your future-self will recognize. |
| `label` | Human-readable name that shows up in the provenance footer. |
| `description` | Free-text paragraph. Write it for a teammate joining six months from now who has to know what counted. |
| `expression` | The DSL recipe. See the grammar section below. |
| `expected_unit` | One of `USD`, `count`, `ratio`, `percent`, `days`. Drives how the value is formatted in answers. |
| `expected_freshness` | One of `realtime`, `daily`, `monthly`. **Metadata only**. The resolver does not cache anything and does not enforce freshness — the field exists so a future drift check can flag "your spec says daily but the underlying vendor is 11 days stale." |
| `cross_source_checks` | Other spec keys whose result should agree with this one within `tolerance_percent`. Triggers automatic drift detection. |
| `tolerance_percent` | How much disagreement is acceptable before drift is flagged. `2.0` means "within 2% is fine." |
| `owner_email` | Who's responsible for this definition. Surfaces in audits. |
| `last_reviewed_at` | When the owner last re-attested. Specs older than 90 days get a "stale" annotation in the provenance footer. |
| `variables` | Per-spec substitution table for `$user.<var>` references in the expression. Lets you parameterize without leaking config into the DSL. |
| `prefer_truth_source` | Forward-compat flag, currently inert. See pitfalls. |

The two blank fields in the template (`owner_email`, `last_reviewed_at`)
are intentionally empty — you fill them in when you adopt the spec.

## The mini-DSL grammar

The expression language is small. It covers four operations and nothing
else, because the entire point of the registry is that you can read a
spec and know what it does without running it.

```
expression  := atom | aggregate | union | arith | metric_ref
atom        := <connector>.<tool>(<kwargs>).<field>?
aggregate   := <atom>.aggregate(<op>, field=<field>, where=<pred>?)
union       := union_distinct(<atom>, <atom>, ...)
arith       := arith(<expr> <op> <expr>)
metric_ref  := metric(<key>)
agg_op      := sum | mean | count | min | max
op          := + | - | * | /
```

### Connector tool call (atom)

```
stripe.get_balance().available[0].amount
```

Calls the connector tool, returns the field path. Atoms are the
building blocks; everything else composes them.

### Aggregate

```
stripe.list_charges(status="succeeded", days_back=30).aggregate(
  sum,
  field=amount
)
```

Calls the tool, pulls every row, applies the op (`sum`, `mean`, `count`,
`min`, `max`) over the named field. Optional `where=<predicate>` filters
rows in memory before the aggregate.

### Union (distinct)

```
union_distinct(
  shopify.list_orders(financial_status="paid", days_back=30).customer.email,
  stripe.list_charges(status="succeeded", days_back=30).customer_email
).count()
```

Builds a deduplicated set across multiple source lists, then counts it.
This is the canonical "distinct customers across all my payment rails"
shape. The trailing `.count()` is a shorthand for
`.aggregate(count, ...)` when the input is a flat list.

### Arithmetic and metric refs

```
arith( metric(stripe_revenue) - metric(stripe_refunds) )
```

`metric(<key>)` resolves another spec and uses its value. `arith(...)`
lets you combine values with `+ - * /`. Both forms make it cheap to
build composite numbers (net revenue, gross-minus-fees, blended CAC)
from primitive specs without restating the underlying recipes.

## Declaring your first spec

You don't write JSON by hand. The flow is conversational.

### Step 1 — Copy a template

Three starter templates ship today, all Stripe-only:
`monthly_paid_revenue_stripe`, `active_paying_customers_stripe`, and
`new_customers_last_30_days`. They're intentionally narrow — Stripe is
the connector we have the cleanest dispatch audit on. A Shopify pack is
on the short list. Ask `support@corpusiq.io` if you want a copy of a
specific template up front, or just hand Claude the JSON in §"Anatomy
of a spec" above and ask it to customize for your use case.

Fill in the two blanks (`owner_email`, `last_reviewed_at`). Edit the
`key` and `label` if you want something more specific to your business.
Adjust the description so it reflects what you actually mean by this
number, not what the template author meant.

### Step 2 — Hand it to Claude

```
You: Save this as a metric spec.

  {
    "key": "monthly_paid_revenue_stripe",
    "label": "Monthly Paid Revenue (Stripe)",
    "description": "Sum of successful Stripe charges in the trailing 30 days.",
    "expression": "stripe.list_charges(status=\"succeeded\", days_back=30).aggregate(sum, field=amount)",
    "expected_unit": "USD",
    "expected_freshness": "daily",
    "cross_source_checks": [],
    "tolerance_percent": 0.0,
    "owner_email": "you@yourco.com",
    "last_reviewed_at": "2026-06-05",
    "variables": {},
    "prefer_truth_source": false
  }

Claude: Calling metric_spec_set...
        Returned pending_write_id pcw_8c3f...
        validation_warnings: []
        Do you want to commit this spec? (y/n)

You: yes

Claude: Calling canonical_pending_commit(pending_write_id="pcw_8c3f...")
        Committed. Spec monthly_paid_revenue_stripe is now active at version 1.
```

The two-step `metric_spec_set` → `canonical_pending_commit` pattern is
the same one canonical facts and truth sources use. The first call
proposes the change and returns a pending-write id plus any
`validation_warnings`. Nothing is durable until you commit. If the spec
fails its eval (and there is one — see the soft eval gate section), the
warnings show up here, before the commit; you get to read them and
decide whether to ship anyway.

### Step 3 — Confirm it landed

```
You: list my metric specs

Claude: Calling metric_spec_list...
        1. monthly_paid_revenue_stripe (USD, daily) v1 — Monthly Paid Revenue (Stripe)
```

### Step 4 — Use it

```
You: what is our monthly paid revenue?

Claude: Calling metric_spec_resolve(key="monthly_paid_revenue_stripe")...

        $47,312
        Monthly Paid Revenue (Stripe) $47,312 · spec v1 · 1 Stripe call (847 rows)

        Powered by CorpusIQ
```

The value is on its own line. The provenance footer is the italic line
right below it. Claude is contractually required to render the footer
verbatim — the data-contract text on the tool response pins that rule
("Do not paraphrase it, do not split it across lines, do not strip the
bullet separators. It is the audit trail.").

## The provenance footer

The footer tells you exactly what happened on the last resolve. Here's
the basic shape:

```
Monthly Paid Revenue (Stripe) $47,312 · spec v2 (reviewed 23 days ago) · 1 Stripe call (847 rows)
```

Parsed left to right:

- **Label + value with unit**: `Monthly Paid Revenue (Stripe) $47,312`. USD formats as currency; counts as integers; ratios and percentages format appropriately.
- **Spec version + review age**: `spec v2 (reviewed 23 days ago)`. The age comes from `last_reviewed_at`. Past 90 days you should re-attest — write the date back and confirm the description still matches your intent.
- **Source-call summary**: `1 Stripe call (847 rows)`. This is row count and connector count only — never row data. Multiple connectors get grouped with `+`. A spec that hit Stripe twice and QuickBooks once would render `2 Stripe calls (910 rows) + 1 Quickbooks call (84 rows)`.

When `cross_source_checks` is set and the peer disagrees, a drift block
appends:

```
MRR $47,312 · spec v3 (reviewed 23 days ago) · 1 Stripe call (847 rows) · drift vs qbo_recurring_revenue: 0.89% (OUTSIDE TOLERANCE)
```

When `validation_warnings` is non-empty, a warning section appends:

```
New Customers (Last 30 Days) 42 · spec v1 · 1 Stripe call (42 rows) · ⚠ eval golden value mismatch: expected 38, got 42
```

The warning marker (`⚠`) is intentional — it makes the surface visible
when an answer scrolls past in chat. The renderer truncates long
warnings to 80 chars each and shows at most three, with a `+N more`
suffix when there are extras.

If you don't see a footer at all on a KPI answer, the AI either rolled
its own aggregate from raw connector data (in which case there's no
spec being honored, and you may want to declare one), or the rendering
contract was stripped somewhere upstream. Both are worth filing.

## Cross-source drift

Declaring two specs that should agree, and letting the resolver yell
when they don't:

```json
// spec 1
{
  "key": "stripe_recurring_revenue",
  "label": "Stripe Recurring Revenue (30d)",
  "expression": "stripe.list_subscriptions(status=\"active,trialing\").aggregate(sum, field=plan.amount_monthly_normalized)",
  "expected_unit": "USD",
  "cross_source_checks": ["qbo_recurring_revenue"],
  "tolerance_percent": 2.0,
  ...
}

// spec 2
{
  "key": "qbo_recurring_revenue",
  "label": "QBO Recurring Revenue (30d)",
  "expression": "quickbooks.report_pnl(account=\"4000-recurring\", days_back=30).aggregate(sum, field=amount)",
  "expected_unit": "USD",
  "cross_source_checks": ["stripe_recurring_revenue"],
  "tolerance_percent": 2.0,
  ...
}
```

When you call `metric_spec_resolve(key="stripe_recurring_revenue")`, the
resolver computes both specs, diffs them, and populates `result.drift`
when the absolute difference exceeds tolerance. The Skill template
renders the drift block under the answer with both values, the peer's
key, the percent difference, and your hypothesis text if you wrote one.

For a portfolio-level view, call `metric_spec_drift_report`. It runs
every spec with a `cross_source_checks` entry and returns only the
drifting ones, sorted by percent_diff descending. Specs that failed to
resolve (vendor down, connector unauthorized, expression parse error)
land in a `skipped` section — the contract says the AI must not silently
omit them, because a spec that can't even compute is one you can't trust
either.

The `drift` object also carries an optional `hypothesis` field —
free-text you write on the spec to document the known reason for a
recurring disagreement. ("QBO recurring excludes trialing subscriptions;
Stripe includes them.") When present, it renders alongside the diff.
This is how you stop having the same drift conversation every Monday.

## The soft eval gate

When you save a spec, the system runs an eval against any golden values
attached to it. If the eval fails, the result is NOT a refusal. The save
proceeds, the spec lands, the resolver works. What changes is that
`validation_warnings[]` on the `metric_spec_set` response and on every
subsequent `metric_spec_resolve` result is non-empty. The Skill
renderer's contract requires those warnings to be surfaced inline —
silent acceptance defeats the entire purpose of having a gate.

This is the §13.Q2 decision in the registry spec, made explicit: hard
enforcement would punish iteration. Soft enforcement plus mandatory
surfacing keeps the iteration loop fast and forces the user to read the
warning before trusting a new number.

A practical translation: when you propose a spec and the pending-write
response carries warnings, read them. They're either "your expression
won't compute" (parser-level), "your expression computes but doesn't
match what we expected" (eval-level), or "we couldn't even run the eval
against fixtures" (infra-level). The first two are usually informative.
The third sometimes means a connector is down for everyone.

## What metric specs do NOT do

- **No data warehouse.** We don't copy Stripe / QuickBooks / Shopify / anything else into our own store. Every resolve hits live vendor APIs.
- **No result caching.** Two calls 30 seconds apart will both hit Stripe. `expected_freshness` is metadata; it does not implement a TTL.
- **No semantic correctness guarantee.** The system honors the recipe you wrote. If you defined MRR wrong, the resolver will faithfully compute a wrong number. That's why the description field, the `last_reviewed_at` re-attestation, and the eval gate exist — they push the responsibility back to the human who knows the business.
- **No team sharing in v0.** Specs are per-user. Multi-user sharing is a v1.5 design discussion and the data model leaves room for it.
- **No LLM-authored specs.** The AI can scaffold a draft for you, but every commit goes through the pending-write approval gate. We won't write specs you didn't approve.

## Pitfalls

Real ones, learned through real fixes.

### Don't use `stripe.get_account()` for a value query

The Stripe account endpoint is the connector you reach for when you want
to confirm "yes, the integration is connected." It is not safe to use
as the source for a metric spec value today. The dispatch path returns
`{"raw": null}` for that single-record read; an aggregate against null
silently produces an empty number. Tracked as issue #437.

Use `stripe.list_charges`, `stripe.list_subscriptions`,
`stripe.list_customers`, or any other list-shaped Stripe tool for value
work. The starter templates all do this for exactly this reason.

### `expected_freshness` is metadata, not enforcement

Setting `expected_freshness: "daily"` does not create a daily cache, a
TTL, or a refresh schedule. The resolver runs every call. The field
exists so a future drift-detection pass can flag "your spec says daily
but the underlying vendor is 11 days stale" — useful, but not the same
as caching. If you need vendor latency tracking now, ask the AI to
include the most recent timestamp from the source rows alongside the
spec value.

### `cross_source_checks` is empty by default

Drift detection costs you nothing in setup terms — but it costs you
nothing because the default `cross_source_checks: []` means no peer is
ever consulted. Make sure both sides of the pair list each other if you
want the check to fire from either direction.

(Listing the peer on only one side works fine when you call that one,
and silently does nothing when you call the other. Easy to miss.)

### `prefer_truth_source` is forward-compat scaffolding

The field exists on the model so adding the behavior in v0.1 doesn't
require a schema migration. **In v0 it does nothing.** A spec with
`prefer_truth_source: true` will still execute its expression and
return the resolver's value — the truth-source override path isn't
wired yet. If you want the truth source to win today, don't declare
the spec.

When v0.1 ships the wiring, the rule is: if the spec sets the flag AND
there's a Truth Source whose `answers[]` list contains the spec key,
the resolver fetches the truth source instead of executing the spec.
Until then, the spec always wins.

## FAQ

**Can I share a spec with my team?**

Not in v0. Each user's specs are private. The data model partitions on
`user_id`, so multi-user sharing is a v1.5 design conversation (do
specs live at the team level? are they copy-on-import? who owns the
`last_reviewed_at` clock?) rather than a code change. We'd rather have
that conversation than ship the wrong primitive.

**What happens if the underlying vendor schema changes?**

The resolver compiles the expression on every call and dispatches
through the same path as raw connector tools. If Stripe renames a field
your spec references, the next resolve fails with a parser or
dispatch-level error and `metric_spec_drift_report` surfaces it in the
`skipped` section. We don't catch schema drift before it bites — but
we also don't hide it after. Vendor-side adapter tests in the
CorpusIQ connector layer catch a separate class of drift before it
reaches your specs.

**How do I know if my number is fresh?**

The provenance footer reports the moment the resolve ran (implicit in
its `computed_at` field on the underlying `MetricSpecResult`) and tells
you how many rows came from each connector. There is no "last cache
update" because there is no cache. If you want to know how stale the
underlying vendor data is, ask the AI to surface the most recent row
timestamp alongside the value — that's a one-line addition to the
question.

**Can I version a spec?**

Yes — every `metric_spec_set` commit increments the spec's version.
Old versions aren't preserved for replay (the spec is a definition, not
an artifact), but the version number is part of the provenance footer
so you can tell which definition produced a number you screenshotted
last month.

**My spec saved but the warnings say the eval failed. What do I do?**

Read the warnings. The Skill contract requires them to be surfaced
inline, so they'll be in the output. Three common cases: the expression
is syntactically wrong (`metric_spec_set` shouldn't have accepted it
— file a bug); the expression is valid but produced a value the eval
didn't expect (your number is probably right; the golden was probably
generated against fixture data that doesn't match yours); the eval
couldn't run at all (infra problem, retry).

**Can I undo a spec?**

Yes. `metric_spec_remove(key="...")` returns a pending-write id, same
as set. You commit the removal via `canonical_pending_commit`. Removed
specs aren't recoverable from the API — re-declare from your local
copy if you change your mind.

**How do I see the expression for a spec I already saved?**

`metric_spec_get(key="...")` returns the full declaration including the
expression. `metric_spec_list` returns the labels and metadata but not
the expressions, so you don't get a wall of DSL when you just want to
know what specs exist.

## Where to ask for help

CorpusIQ support: `support@corpusiq.io`. We read the inbox often.

If you hit a connector-level issue (Stripe returns nothing, GA4
authorization expired, QuickBooks rate-limits you), that's usually a
connector problem rather than a spec problem — but `support@` is still
the right starting point. Include the spec key and the exact question
you asked Claude, and we can usually find the dispatch in the logs.
