---
title: "CorpusIQ Governance and Controls"
description: "CorpusIQ MSR governance: the Metric Spec Registry, how a business number is defined once, how resolution works, drift detection, versioning, and what the audit trail records."
category: "Documentation"
tags: ["corpusiq governance", "msr", "metric spec registry", "drift detection", "provenance", "audit trail"]
last_updated: "2026-10-31"
canonical: "https://www.corpusiq.io/governance"
robots: "index,follow"
---
# MSR Governance

MSR means the **Metric Spec Registry**. It is where a business number is defined once for an account: MRR, average order value, new customers, or any other number you want every assistant to answer the same way.

A metric spec is a small, user-declared recipe. You write it once. Every later question resolves that same recipe against current vendor data, with a one-line provenance footer attached to the answer.

## What the registry holds

| Item | What it defines |
|------|-----------------|
| Key | Stable identifier such as `mrr` |
| Label | Human-readable name shown in the provenance footer |
| Description | Your own paragraph on what counted and what did not |
| Expression | The recipe, compiled to connector calls |
| Unit | USD, count, ratio, percent, or days |
| Cross-source peers | Other specs whose value should agree |
| Tolerance | How much disagreement is allowed before drift is flagged |

## How a value is resolved

1. The question names a number, for example "what is our MRR".
2. The registry resolves the matching spec against live connector data.
3. The value returns with a provenance footer: label, value, spec version, review age, and the connector calls with row counts.
4. When cross-source peers are declared and disagree beyond tolerance, a drift block is appended to the same answer.

Resolution is bounded by connector coverage. Starter templates ship for Stripe first, and a spec can only reference tools that exist in the connector layer.

## What the registry does not do

- **No warehouse and no replicated source data.** Every resolve calls the vendor.
- **No result caching.** Two calls thirty seconds apart both hit the source.
- **No semantic correctness guarantee.** The registry computes the recipe you wrote. If the recipe is wrong, the number is wrong, which is why the description and the review date exist.
- **No automatic spec writing.** An assistant can draft one, but every save passes through a pending-write commit that the account owner approves.

## Versioning and audit trail

Every committed spec change increments a version number, and that version appears in the provenance footer of each answer that uses it. Operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for a limited retention window. Raw customer files and full connector response payloads are not retained.

## When two sources disagree

1. Read the drift block. It names the peer spec, both values, and the percent difference.
2. Check that both specs describe the same period, the same filters, and the same field.
3. Add a hypothesis to the spec when the disagreement is known and expected, for example one vendor including trialing subscriptions while the other excludes them.
4. Re-attest the spec with a new review date once the definition is correct.

## Related pages

- **[Metric Specs](/how-it-works/metric-specs)** - full onboarding guide, expression grammar, and pitfalls
- **[CorpusIQ Architecture](/architecture)** - MCP endpoint and connector layer design
- **[CorpusIQ Security Overview](/security)** - authentication and encryption
- **[CorpusIQ Reporting](/reporting)** - instant reports and trend analysis
- **[CorpusIQ Onboarding Guide](/onboarding)** - AI chat and agent setup in 10 minutes

*Powered by CorpusIQ - business answers you can trust, cited from your own sources.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
