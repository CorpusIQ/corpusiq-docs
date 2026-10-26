---
title: "drift MCP - Pre-Action Mandate Enforcement for AI Agents"
description: "Apache-2.0 MCP server that re-checks every agent action against a signed payment mandate before it happens: six rules in fixed order, deny-by-default, tamper-evident chain fingerprint."
category: Compliance
stars: 0
added: 2026-10-19
source: "mcpservers.org /all page 1 (mrpkk/drift)"
relevance: ★★
tags: [agent-governance, mandates, ap2, payments, spend-limits, deny-by-default, approvals, audit-trail, remote-mcp]
last_updated: "2026-10-19"
---

# drift MCP

**A mandate gate that sits between an agent's decision and the money leaving** - every proposed action is checked against the signed payment mandate before it executes, not once at signing. Six rules run in a fixed order (amount, payee, audience, currency, window, intent), the default answer is DENY, and a batch of decisions produces a fingerprint that breaks if any earlier decision is rewritten or reordered.

```
Server type: Remote (Streamable HTTP, JSON-RPC 2.0, protocol 2025-06-18) at https://drift.rta.lat/mcp
Endpoint: https://drift.rta.lat/mcp (no auth on the hosted endpoint)
Tools: 3 - drift_check, drift_session, drift_explain (all annotated read-only, idempotent, no open-world access)
Requirements: none to call the hosted server; Python 3.11+ if you self-host
License: Apache-2.0 (github.com/mrpkk/drift, default branch master)
Pricing: hosted free tier 100 checks a day, paid per call via x402 on Base; self-hosting is free
```

## Why This Matters for Operators

An agent gets authority once: pay this supplier, up to this amount, in this currency, until this date. The protocol that carries that authority (AP2) verifies it at the moment the mandate is signed and then steps out of the way. Between the signature and the payment there is nothing holding the agent inside the authority it was given.

drift is that missing check, and it is deliberately narrow. It does not verify signatures (AP2 does), it does not execute anything, and it keeps no state. You hand it a mandate and an action, it hands back ALLOW or DENY plus the name of the rule that fired. That narrowness is why it is cheap enough to call before every action rather than once per session.

The order of the rules is the part worth understanding. If a payment is both over the limit and going to the wrong payee, the refusal says `amount`, because that is the more serious fact. A refusal you can explain in one word is a refusal an operator will accept; a refusal that says "policy violation" is one they will route around.

## Tools & Capabilities

| Tool | Input | Returns |
|---|---|---|
| `drift_check` | one `mandate` and one `action` | `{verdict: ALLOW|DENY, rule, report}` where the report carries submitted/allowed/denied counts, `breach_by_rule` and a `fingerprint` |
| `drift_session` | one `mandate` and a list of `actions` | the per-action decisions in order, the same report shape, and a chain fingerprint over the whole sequence |
| `drift_explain` | nothing | the six rules in the order they are applied, each with a plain-language reason, plus `default: DENY` |

The mandate shape is fixed: `payee_id`, `audience` (the merchant URI bound into the mandate), `max_amount_minor` (integer minor units, cents - never floats), `currency` (ISO-4217), `valid_from`, `valid_until` (unix seconds, inclusive bounds) and `allowed_intents`. The action carries the same fields plus `intent` and `at`.

Rule order, verified against the live endpoint:

| # | Rule | Fires when |
|---|---|---|
| 1 | `amount` | the action exceeds `max_amount_minor` |
| 2 | `payee` | `payee_id` is not the one the mandate names |
| 3 | `audience` | the action is aimed at a merchant URI the mandate does not name - the exact substitution the AP2 SDK was measured accepting |
| 4 | `currency` | the currency was swapped |
| 5 | `window` | the action falls outside `valid_from` to `valid_until` |
| 6 | `intent` | the intent is not on `allowed_intents` |

## Installation

The hosted endpoint needs nothing but an HTTP client. Ask it for its tools:

```bash
curl -s -X POST https://drift.rta.lat/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"1.0"}}}'
```

To add it to a client:

```bash
npx add-mcp 'https://drift.rta.lat/mcp'
```

Cursor, VS Code, Windsurf and anything else that reads an MCP config file:

```json
{
  "mcpServers": {
    "drift": { "type": "http", "url": "https://drift.rta.lat/mcp" }
  }
}
```

**Read this before you run the README's install command.** The README says `pip install drift`. The name `drift` on PyPI already belongs to an unrelated CMS content-editing package (0.0.7, published from a Bitbucket repository, last release long before this project existed), and `drift-mcp` does not exist on PyPI (404 at probe time). `pip install drift` therefore installs the wrong library, and `python3 -m drift.http_server` will fail or, worse, import something else. Self-host from the repository instead:

```bash
git clone https://github.com/mrpkk/drift && cd drift
pip install -e .
python3 -m drift.http_server --http 8080
```

Self-hosting needs Python 3.11+ and nothing else: `dependencies = []` in `pyproject.toml`, standard library only, no HTTP framework. There is also a `Dockerfile`, and a `windmill_script.py` for Windmill users.

## Configuration

There are no config keys: a mandate is an argument, not a stored object, and the server keeps no state between calls. What you decide instead, once, is the mandate itself:

| Field | Meaning | Trap |
|---|---|---|
| `max_amount_minor` | spending cap in minor units | integer only; `10000` is 100.00, and a float is rejected rather than rounded |
| `valid_from` / `valid_until` | unix seconds | both bounds are inclusive, so an action at exactly `valid_until` is allowed |
| `allowed_intents` | the allowlist of intents | **an empty list means "any intent"** - see Limitations |
| `audience` | the merchant URI bound into the mandate | compare it against what the agent actually calls, or the check is theatre |

The mandate object is a frozen dataclass in the reference implementation: changing a field means building a new mandate, so an edit cannot quietly widen the authority you already signed.

## Business Relevance

- **Any agent that spends money:** the gap between "we authorised a supplier up to $500" and "$500 went to that supplier" is where agent payments go wrong. This checks the second half of that sentence.
- **Accounts payable and procurement pilots:** a spend cap that is enforced per action, with a named rule on refusal, is a control you can describe to a finance reviewer without hand-waving.
- **Agent marketplaces and x402 flows:** when an agent pays per call, the mandate is the only thing bounding the bill. Rules run locally on the decision, so the cost of checking is a function call, not an API round trip.
- **Audit trails:** `drift_session` fingerprints a whole sequence. Reordering or editing any earlier verdict changes the hash, so "the log says it was allowed" becomes checkable rather than asserted.

## Integration with CorpusIQ

CorpusIQ's proposition is that the same business question should return the same answer in every AI client, with the source cited. That is a claim about what the agent reads. drift is a claim about what the agent does: the authority it was granted is re-checked at the moment of the action, not assumed from the signature.

They meet in the same place the approval gate meets the read path - the agent proposes, and a deterministic rule outside the model decides. For a business owner connecting an agent to a payment-adjacent system, "it was checked against the mandate before it ran, and here is the rule that stopped it" is a sentence they can repeat. "It has guardrails" is not.

## Limitations

- **It does not verify signatures.** That is AP2's job, and drift runs after signature verification. If nobody verified the mandate, drift is checking actions against an authority that may itself be forged.
- **It does not execute, and it does not record what happened.** It decides. `drift_session` reports what was *proposed*. Proving what actually occurred is `attest` (same author, complementary: drift bounds beforehand, attest proves afterwards).
- **`intent` is untrusted input from the agent.** An agent that lies about its intent and its amount stays inside the bound while lying about both. The vendor says this plainly, and it is the honest limit of a decision gate.
- **An empty `allowed_intents` disables the intent rule.** Verified live: a mandate with `allowed_intents: []` returned ALLOW for an intent called `transfer_everything`. The spec treats an empty list as an explicit "any intent" decision. Always populate it.
- **Very new and unproven.** Repository created October 4, 2026, last push October 20, 2026, zero stars, zero forks, no third-party use, one maintainer. The rules are simple enough to read in an afternoon - read them, and run the test suite, before you put it in front of a real payment rail.
- **The monetisation is a per-call toll on Base.** The free tier is 100 checks a day; above that, x402 per call. Checking every action of a busy agent is cheap per call but not free, and the price is denominated in crypto.
- **English tool descriptions, Russian spec and server metadata.** The README and the MCP tool descriptions are English; `SPEC.md` and the `server.json` description are Russian. If you plan to self-host or fork, expect to read one of them through a translator.

## FAQ

### How is this different from an approval gate?

An approval gate stops an action until a *person* agrees. drift stops an action that is *outside the mandate*, with no human in the loop and no latency. The two stack: drift refuses what was never authorised, the approval gate decides the things that were authorised but still need a human. If you want a named human's approval before an irreversible action, that is a different server (EMILIA Protocol, or the ACMP approval model); drift is the floor under it.

### What happens when an agent is denied?

Nothing executes. The tool returns `DENY` with the rule name and a report; the calling agent is expected to stop and say why. `drift_explain` exists for the case where the refusal did not make sense and you need to show the person whose mandate was rejected which rules ran, in what order.

### Can I check a whole plan before running it?

Yes, and that is the better use of it. `drift_session` takes a list of actions and returns each verdict plus `breach_by_rule` and one fingerprint over the sequence. Verified live on a three-action batch - one within the mandate, one over the amount, one to a different payee - it returned `{submitted: 3, allowed: 1, denied: 2, breach_by_rule: {"amount": 1, "payee": 1}}` with a single chain fingerprint.

### Does the hosted endpoint see my mandates?

It sees the mandate and the action you send it, in the request body, over TLS. It states that it keeps no state and no session; the tool annotations are read-only and idempotent. If a mandate is commercially sensitive, self-host - the code is small, dependency-free and Apache-2.0.

## See Also

- [AgenticRail Gate MCP - Step-Order Enforcement with Signed Receipts](/hermes/mcp/servers/external/agenticrail-gate-mcp)
- [Poison Armor MCP - Prompt-Injection Firewall](/hermes/mcp/servers/external/poison-armor-mcp)
- [ACMP MCP - On-Prem IT Management with Approval Gate](/hermes/mcp/servers/external/acmp-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
