---
title: Engineering Skills
description: Platform construction skills for Hermes agents — MCP server architecture, connector audits, API development, frontend patterns, scheduled jobs, Honcho memory, and metric specs. Born from operating a 50k+ LOC multi-connector server in production.
---

# Engineering Skills

These are skills for **building the platform itself** — distinct from [development skills](/hermes/skills/development/), which cover using the platform (GitHub PRs, code review, repo management). Engineering skills capture patterns earned through operating a multi-connector MCP server at production scale: what broke, how it was fixed, and the discipline that prevents recurrence.

Every skill here is a fence around a hole the team already fell into.

## Connector and MCP Discipline

### `consultant-connector-audit`

The single most-loaded engineering skill. A 13-section audit pass for any connector code authored by a non-core contributor. Born from a painful 9-PR cycle where a vendor connector passed CI but silently failed on first customer call, triggering round-trip after round-trip of "customer hits bug → core team fixes → customer hits next bug."

The audit covers:

1. **Auth flow completeness** — Does token refresh actually work, or does the connector assume tokens never expire?
2. **Error surface coverage** — Are all API error codes handled, or do some fall through to "success"?
3. **Schema compliance** — Do returned fields match the declared schema, or does the connector invent fields?
4. **Edge case inventory** — Empty results, rate limits, malformed responses, connection drops — handled or swallowed?
5. **Tool description accuracy** — Do the tool descriptions in the connector match what the tools actually return?
6. **Pagination correctness** — Are paginated endpoints handled correctly, or will the connector return only the first page?
7. **Timezone handling** — Are dates returned in the correct timezone, or does UTC silently corrupt local times?
8. **Unit handling** — Are currency amounts in the correct unit (cents vs. dollars), or will reports be off by 100x?
9. **Rate limit awareness** — Does the connector back off on 429s, or hammer the API until banned?
10. **Logging hygiene** — Are secrets, tokens, or PII logged anywhere?
11. **Dependency freshness** — Are dependencies pinned to known-good versions, or will a minor bump break everything?
12. **Test coverage of failure paths** — Not just happy-path tests — are error paths tested?
13. **Documentation for the next auditor** — Can the next person understand the connector without reading all the source?

The audit takes roughly 30 minutes. It catches the class of bugs that survive CI but die on first production use — the most expensive class of bugs.

### `mcp-architecture`

Operating-scale field guide for a 50k+ LOC MCP server. Covers the architectural patterns that emerge when a single server exposes dozens of connectors:

- **Per-connector triplet pattern** — Every connector consists of: (1) the connector module, (2) the tool schema declarations, (3) the authentication handler. Understanding this triplet is the key to navigating the codebase.
- **File map** — The directory structure, naming conventions, and which files are "hot" (changed frequently) vs. "cold" (stable infrastructure).
- **Dual-render-path trap** — The server renders differently depending on whether it's called from the Hermes agent or from a web dashboard. Numbers that look correct in one render path may be silently wrong in the other. Always verify from both.
- **Bulk-regex migration recipe** — When a pattern changes across all connectors (e.g., a new error handling convention), how to safely migrate 50+ files with regex without breaking anything.
- **New connector onboarding** — The checklist for adding a new connector: auth setup, tool schema, error taxonomy, test fixtures, and the audit pass.

### `metric-spec-registry`

The canonical-layer metric subsystem. When two systems disagree about a number (e.g., MRR from Stripe vs. MRR from QuickBooks), the metric spec registry's drift report tells you which one to trust and why.

Key concepts:

- **Declared definitions** — Every KPI has an owner, an expression (in a mini-DSL), an expected unit, and a tolerance for cross-source disagreement.
- **Live resolution** — Metrics are computed fresh on every query, never cached. If Stripe's API is down, the resolution reports it rather than serving stale numbers.
- **Drift detection** — Cross-source checks compare the same metric computed from different systems. If Stripe MRR and QuickBooks MRR disagree beyond the tolerance threshold, the drift report surfaces the discrepancy with both values and the computed gap.
- **Provenance footer** — Every resolved metric carries a footer showing: which sources were queried, how many rows each returned, which version of the spec definition was used, and when it was resolved.

## API and Backend Development

### `api-development`

Cloud Run + FastAPI patterns born from real production audits:

- **Test fixture traps** — JSONB fields in Postgres have compile-time hook ordering dependencies. A test that passes locally can fail in CI because the hooks fire in a different order. The fix: explicit hook registration order.
- **UUID type matching** — FastAPI path parameters vs. SQLAlchemy column types must agree on UUID representation (string vs. native). Mismatches produce 422 errors with no useful message.
- **MCP JWT key bootstrap** — The chicken-and-egg problem of JWT verification: the server needs the public key to verify tokens, but getting the public key requires an authenticated call. The bootstrap pattern solves this.
- **Self-destructing admin migrations** — Database migrations that run once and delete themselves to prevent accidental re-execution in production.
- **JWT JWKS contract** — When your API issues JWTs and multiple consumers verify them, the JWKS endpoint becomes a contract. Changes to the signing key must be coordinated with all consumers or they break silently.

### `frontend-development`

Next.js + Vercel patterns for marketing sites and dashboards:

- **Canonical-constant rule** — Company name, pricing, feature lists, and contact emails must be defined in exactly one place (a canonical constants file). Copy-pasting these values across components guarantees divergence.
- **Deploy verification** — After a Vercel deploy, verify that (1) the production URL responds, (2) the build hash matches the commit SHA, and (3) the marketing site and dashboard are in sync. "Deployed" and "actually changed prod" are different states.
- **Cross-repo boundary** — When the marketing site lives in a separate repo from the dashboard, shared components must be versioned explicitly. A dashboard deploy that silently changes marketing site behavior is the most common cross-repo bug.
- **Dashboard widget patterns** — Standard patterns for data-fetching widgets: loading states, error states, empty states, and refresh intervals. Every widget must handle all four.

## Scheduled Jobs

### `scheduled-jobs`

Cron operating manual for Hermes agents:

- **Server-local time trap** — Cron runs on the server's local timezone. If the server is in Arizona (MST, no DST) and your schedule is written assuming UTC, jobs will fire at the wrong time. Always verify `date` output on the server before writing cron schedules.
- **Profile vs. default split** — Hermes cron jobs run in a specific profile context. A job defined in the default profile won't have access to skills installed in a custom profile. Verify profile context before deploying.
- **No-agent watchdog** — Agent processes can hang. A watchdog cron checks that the agent is actually responding (not just running) and restarts if it's frozen. The watchdog itself is monitored by a separate health endpoint.
- **In-prompt-curl trap** — Using `curl` inside a Hermes prompt to hit a local endpoint seems convenient but breaks silently: the agent's network context may differ from the host's. Always use Python scripts with explicit network configuration instead.
- **Deliver-script pattern** — Crons call scripts, scripts verify output, verification produces a report. Never have a cron "fire and forget" — every cron must produce a deliverable that can be checked.

## Cross-Session Memory

### `honcho-memory-usage`

Server-side semantic memory via Honcho MCP — when and how to use it:

- **When it helps** — Cross-session context that survives agent restarts: user preferences, project state, decisions made, ongoing task status.
- **When it doesn't** — In-session working memory (use the agent's context window instead), volatile state (use files), structured data (use a database).
- **Read vs. write discipline** — Reads are cheap (semantic search retrieves relevant memories). Writes are expensive (they trigger background derivation tasks). Don't write every turn — write when a decision was made or a fact was established.
- **Cost discipline** — Honcho derivation tasks consume LLM tokens. Memory operations should be deliberate, not automatic — write after significant events, not after every message.

## Why These Are Distinct From Development Skills

The [development skills](/hermes/skills/development/) section covers tools every developer uses: GitHub PRs, code review, repo cloning, syntax checking. These are well-trodden, mostly automatable patterns.

Engineering skills capture a different class of knowledge — the patterns that emerge when you operate a customer-facing platform at the scale where:

- One silently swallowed error compounds into nine PRs of churn
- A contributor who didn't understand the architecture introduces a connector that passes CI but breaks at first customer call
- Two systems compute "the same number" differently and you have to figure out which one is wrong
- Branch protection, release-promotion, and image-SHA verification become the difference between "shipped" and "actually changed prod"

Read these skills when you're about to do the thing they describe. Patch them immediately when the hole moves.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
