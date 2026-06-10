---
title: Engineering Skills
description: Skills for building and maintaining the CorpusIQ platform — MCP servers, connector substrates, multi-repo coordination, and the discipline that keeps a 51k-LOC server.py from rotting silently.
---

# Engineering Skills

These are the skills for **building** the platform, distinct from `development/` which covers using the platform (GitHub PR mechanics, code review, repo management).

Born from operating a multi-connector MCP server through customer pull, vendor API churn, and consultant-authored contributions that needed audit before merge. Each one captures a pattern earned the hard way — a class of bug that bit, the audit that surfaced it, and the discipline that prevents recurrence.

**Single most important pattern:** when a consultant or non-core contributor ships connector or auth code, run the audit before clicking merge. The cost of "one more PR" is not engineering time — it is the customer's perception of churn. The Mailchimp 9-PR cycle that gave birth to half these skills was nine round-trips of "Ben hits bug → I fix bug → Ben hits NEXT bug." A 30-minute audit after the first bug would have shipped everything as one PR.

## Connector & MCP Discipline

| Skill | What It Does |
|-------|-------------|
| [`consultant-connector-audit`](./consultant-connector-audit/) | 13-section audit for any non-core-authored connector. The single most-loaded skill in this section — catches Mailchimp-style silent-failure clusters before they ship to customers. |
| [`mcp-architecture`](./mcp-architecture/) | Orientation for a 50k+ LOC MCP server: file map, per-connector triplet pattern, bulk-regex migration recipe, dual-render-path trap (server vs ChatGPT app). |
| [`metric-spec-registry`](./metric-spec-registry/) | The "metric spec waterfall" — when two systems disagree about MRR, the registry's drift report tells you which one to trust and why. |

## Repo & Platform Coordination

| Skill | What It Does |
|-------|-------------|
| [`api-development`](./api-development/) | Cloud Run + Supabase patterns, FastAPI test-fixture recipe (JSONB compile hook ordering, UUID type matching, MCP JWT key bootstrap). Born from a real consultant audit. |
| [`frontend-development`](./frontend-development/) | Vercel deploy parity rules, marketing-site discipline, dashboard widget patterns, the "marketing site is in a separate repo" verification check. |
| [`scheduled-jobs`](./scheduled-jobs/) | Cron operating manual: server-local time (not UTC), gateway architecture, in-prompt-curl trap, deliver-script pattern. |

## Cross-Session Memory

| Skill | What It Does |
|-------|-------------|
| [`honcho-memory-usage`](./honcho-memory-usage/) | When and how to read/write Honcho across sessions. The substrate-level memory pattern that survives session reset. |

## Why These Are Distinct From `development/`

The `development/` section covers tools every dev uses: GitHub PRs, code review, repo cloning, syntax checks. Generic, well-trodden, mostly automatable.

These are different. They're the patterns that emerge when you operate a customer-facing platform at the size where:

- One silently swallowed error compounds into nine PRs of churn
- A consultant who didn't write to your constitution introduces a connector that passes CI but breaks at first customer call
- Two systems (server-side vs ChatGPT mega-tool) compute "the same number" differently and you have to figure out which one is wrong
- Branch protection rules, release-promotion discipline, and image-SHA verification turn into the difference between "shipped" and "actually changed prod"

Every skill here is a fence around a hole the team already fell into. Read them when you're about to do the thing they describe; patch them immediately when the hole moves.

## Naming Conventions

- Skills with patterns generalizable to any MCP / connector / multi-repo team: no prefix (`consultant-connector-audit`)
- Skills specific to CorpusIQ infrastructure (paths, vendor IDs, internal tools): prefixed `corpusiq-*` in the source profile, but stripped here when contributed
- References to specific PR numbers, customer incidents, or internal vendor IDs in the original skills have been generalized for this section — the PATTERN is the value, the specific repo paths are noise

## Source

These skills are maintained in the CorpusIQ engineering agent's Hermes profile. Updates land here via PR.

---

*← [Skills Overview](/hermes/skills/) | [Catalog](/hermes/skills/catalog/) → | ↑ [Home](/hermes/)*
