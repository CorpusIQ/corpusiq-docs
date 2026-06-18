---
title: metric-spec-registry
description: Pattern for a canonical-layer metric subsystem — store KPI definitions, not data; resolve live; surface drift between sources; never cache; provenance every answer.
---

# Metric Spec Registry

When two systems in your stack compute "the same number" differently — Stripe says MRR is $X, QuickBooks recurring revenue says $Y, your dashboard widget says $Z — the question stops being "what's our MRR?" and becomes "which of these three is right, and why don't they match?"

This skill describes the substrate pattern that answers both questions: a **metric spec registry** that stores user-declared KPI definitions (the expression, the source calls, the variables) and a **resolver** that evaluates them live every time, never cached. Plus a **drift report** that walks every spec with a cross-source check, fires both sides, and surfaces only the ones that disagree past tolerance.

## When to load this skill

- You have a multi-source environment (Stripe + QBO + dashboards, Salesforce + HubSpot + sheets, etc.) where the same business question can be answered different ways
- You've been bitten by a "exec asked for ARR, three people gave three answers" incident
- You're about to build a "canonical KPI" layer and want a pattern that's been beaten on
- You want drift detection between source systems as a feature, not an end-of-quarter spreadsheet exercise

## The waterfall

Three layers, evaluated in order when a user asks "what's our <metric>?":

1. **Truth source** (highest authority) — a user-maintained workbook or document the user explicitly declared as the source for this metric. If a TruthSource entry exists AND the spec doesn't have `prefer_truth_source: false`, use the truth source's number
2. **Metric spec** — a declared expression in a mini-DSL that compiles to vendor API calls. Resolved live, never cached. Carries `cross_source_checks` for drift detection
3. **Raw connector data** (lowest authority) — only when no spec exists and the user didn't register a truth source. Labeled "estimate" in the response, not asserted as canonical

The waterfall is the discipline that makes the system trustworthy. Without it, every AI client computes the metric its own way and the user gets three different answers from three different chat windows.

## The data model

A `MetricSpec` is a frozen dataclass with these fields:

| Field | Purpose |
|---|---|
| `key` | Short stable identifier (`mrr`, `aov`, `monthly_active_customers`) |
| `label` | Human-readable name |
| `description` | The user's own definition — surfaced in the provenance footer |
| `expression` | The computation in the mini-DSL. Example: `stripe.list_subscriptions(status="active").aggregate(sum, field=plan.amount)` |
| `expected_unit` | Free-form: `USD`, `count`, `ratio`, `percent`, `days`. Renderer uses for formatting |
| `expected_freshness` | Free text the user accepts as staleness budget: `realtime`, `daily`, `monthly`. Metadata only — does NOT trigger caching |
| `cross_source_checks` | Other metric spec keys whose result should match this one within `tolerance_percent`. Populates the drift block on resolve |
| `tolerance_percent` | Absolute percentage tolerance for cross_source_checks. Default 1.0. 0.0 for exact |
| `variables` | Per-spec substitution table for `$user.<var>` references inside the expression |
| `prefer_truth_source` | If true, the v0.1 resolver uses the truth source instead of executing the expression |
| `version` | Bumped on every save (the pending-write commit creates a new version) |
| `owner_email` | Who is responsible for this definition (so reviewers know who to ping) |

## The resolve contract — never cached, always live, always provenance

When the user asks "what's our MRR?":

1. Look up the spec by key
2. Parse the expression DSL
3. For each source call in the expression, dispatch the matching connector tool
4. Aggregate per the expression
5. Evaluate `cross_source_checks` — fire each comparison spec, compare to the primary result, flag drift if outside tolerance
6. Return:
   - `value` — the canonical number
   - `unit` — `USD` / `count` / etc.
   - `provenance_footer` — a one-line human-readable summary (spec version, source calls, drift status, warnings) you MUST surface verbatim at the end of your answer
   - `drift` — populated when cross_source_checks disagree past tolerance; carries both values and a `hypothesis` field
   - `validation_warnings` — any parse failures, missing cross-checks, non-numeric diffs, you MUST surface inline

The user should be able to see, in every answer, exactly which spec version produced the number and which source calls were dispatched. **No caching, ever** — a stale number is worse than a slow one.

## Drift as a feature

`metric_spec_drift_report` walks every spec with a non-empty `cross_source_checks`, resolves each one and its comparison, and returns ONLY the specs where the two values disagree beyond `tolerance_percent`. The "what's silently disagreeing in my numbers" dashboard.

An empty list is the green signal — everything is within tolerance. Not an error.

When drift IS reported, the response surfaces both values, the comparison spec, and the `hypothesis` field if present. Drift is not a bug; it's a signal that the truth-source story has degraded and someone needs to look. Hiding it (returning one number when two systems disagree) is the failure mode.

## The mini-DSL grammar

The expression syntax is the core surface. Minimum viable shape:

```
<source>.<method>(<args>).aggregate(<op>, field=<field>)
```

Example:

```
stripe.list_subscriptions(status="active").aggregate(sum, field=plan.amount)
```

The DSL parses to a typed AST. The resolver compiles each `<source>.<method>(<args>)` to a real MCP connector tool call (`stripe.list_subscriptions` → the `list_subscriptions` tool on the stripe connector). The aggregate operation runs in the resolver.

Soft eval gate: a spec whose expression fails to parse is still saved, but the resolver emits `validation_warnings` every time it tries to resolve. The warnings show in the user's answer. Don't reject at write time — the user might be drafting an expression they'll fix later, and rejecting forces them to throw away the description text they wrote. Soft gate at read time is the right discipline.

## Pending-write semantics (constitutional)

Saves do NOT happen immediately. `metric_spec_set` returns a `pending_write_id`. The user must explicitly confirm (`canonical_pending_commit`) before the spec lands. Never silently save inferred or guessed specs.

Same for delete (`metric_spec_remove`). Pending-write IDs are session-scoped and expire if unconfirmed.

This is the never-silently-modify-canonical rule. The metric spec is a canonical-layer entity; modifying it without explicit user consent breaks the trust contract the registry's existence depends on.

## Connector dispatch boundary

In a v0 implementation, the resolver supports a small fixed set of connectors (Stripe + Shopify is a sensible starting pair — recurring revenue + ecommerce revenue are the two sources users want to compare against each other for MRR/AOV).

Expanding the supported set is straightforward but each new connector needs:

- A DSL grammar entry mapping `<source>.<method>` → the underlying tool call
- A schema/coercion layer so the aggregate operations get typed inputs (numbers are numbers, not strings)
- A test fixture asserting the resolver returns the right number for a known input

Resist the temptation to expand the set in the same PR that ships the registry. The substrate is the lift; the connector additions are increments.

## Lockstep test — protect the renderer

The provenance footer is rendered by your response formatter. If your MCP server has dual render paths (one for raw HTTP, one for ChatGPT mega-tool), the footer string lives in both. See [mcp-architecture](../mcp-architecture/#dual-render-path-trap-serverpy-vs-chatgpt-app) for the dual-render-path pattern and the lockstep equality test.

Without a lockstep test, the next refactor will rendering-drift the provenance footer between paths, and customers will see different "powered by spec v3" footers on different clients. Tiny user-visible bug, hard to diagnose.

## When this pattern fits

You want the metric spec registry when:

- Multiple source systems can answer the same question
- "Which one is right" is a real business risk (board meetings, customer-facing pricing, financial close)
- Users would rather see "Stripe says X, QBO says Y, they disagree by 2%, here's the hypothesis" than a confidently-wrong single number
- You're already operating an MCP / multi-connector substrate where the source calls are addressable

You don't want it when:

- Single source of truth exists and is trusted (just use that source)
- The metric is purely operational (memory usage, cron status) — those don't need canonical resolution
- The user prefers fast/cached numbers over right ones (rare in B2B finance, common in operational dashboards)

## Related

- [consultant-connector-audit §9.6](../consultant-connector-audit/#96-parallel-code-path-trap-refactor-missed-sibling) — the dual-render-path trap the registry's renderer is vulnerable to
- [mcp-architecture](../mcp-architecture/) — the substrate the registry assumes you have


*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
