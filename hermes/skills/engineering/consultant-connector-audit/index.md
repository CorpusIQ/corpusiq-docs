---
title: consultant-connector-audit
description: Full-stack audit pass that MUST run before shipping any fix on a connector authored by a non-core contributor. Replaces the fix-forward-on-symptom anti-pattern with one inventory + one PR. The single highest-leverage skill for any team running a multi-connector substrate.
---

# Consultant Connector Audit

## When to invoke

Any one of:

1. A connector under your data adapter layer was authored by someone other than the core team, AND you've just hit at least one bug in it in production.
2. A customer-facing surface has reported a connector failure that traces to non-core code.
3. You're about to merge a new contributor-authored connector PR (preempt — audit BEFORE merge, not after the first customer-reported bug).
4. CI failed in any way related to that connector (silent import, registry parity, formatting that masks a real bug).
5. A contributor claims they "fixed" something in auth, billing, security, MCP routing, the token store, or any non-connector code path. Same discipline applies — verify the claim before nodding.

If trigger 1 or 2 fires, **stop the fix-forward instinct.** Do not push a fix for the symptom you just saw. The cost of "one more PR" is not engineering time, it is the customer's perception of churn. Read the rest of this skill, run the audit, file ONE issue with the full bug inventory, fix in ONE PR, then tell the affected human "try again."

## The Mailchimp pattern (the bug class this prevents)

A real incident on the team's connector substrate, captured here so the pattern stays visible:

| # | What broke | Trigger |
|---|---|---|
| 1 | `from config.kv_mixins` typo (module doesn't exist) | Customer demo hits the Connect button, 404 |
| 2 | TokenManager.save_token missing required argument | Customer retried |
| 3 | Adapter __init__ signature mismatch | Customer retried |
| 4 | NameError: secrets in OAuth callback (affected 3 connectors at once) | Customer retried |
| 5 | Adapter has no `close` method, breaks async cleanup | Customer retried |
| 6 | Tokens written to local disk, not central secret store (constitution violation) | We noticed during 5's work |
| 7 | 40 of 43 tools named with consultant nickname instead of canonical | Team noticed |
| 8 | Same 40 tools missing from raw HTTP `tools/list` path | Team noticed |
| 9 | Dev deploy stuck on lint after rushed direct-to-main commit | Team noticed |

**Nine round-trips. Every single bug existed in the code at the moment of the first bug-fix PR.** A single 30-minute audit pass after bug #1 would have surfaced the full inventory; one PR, one "try again" call to the customer instead of nine, one "this product appears to be on fire" perception averted.

## The audit checklist

Run every item, in order, against the target connector. For each finding, append to a single Markdown checklist — do NOT open issues per-finding, that recreates the churn.

### 1. Import & loader (the silent-failure surface)

Does the auth module import cleanly in isolation? Does the adapter? What's in the try/except wrapper in your server entry point — does it log the import failure visibly, or swallow it?

Findings:
- [ ] Imports use canonical paths, not made-up paths
- [ ] The try/except in the server entry logs the import failure at WARNING with the full exception — never silent
- [ ] The connector's `<CONNECTOR>_AVAILABLE` (or equivalent) flag is truthy in a normal dev shell

### 2. Token storage (constitutional)

If you have a token-storage mixin or shared pattern (file + secret store dual-write, etc.), verify the connector actually uses it:

- [ ] TokenManager inherits the canonical mixin (not a re-implemented one)
- [ ] `save_token` / `load_token` / `delete_token` each call the corresponding helper method
- [ ] The connector-naming constant (KV suffix, secret prefix, etc.) is canonical — not the contributor's nickname for the connector
- [ ] Tokens actually land in the central store after a connect test — verify with the store's CLI directly, don't trust the code path

### 3. Connector-method signatures match the dispatch layer

The contributor's adapter `__init__` may take different args than the server.py dispatch passes. Common drift: positional vs kwarg, missing per-vendor optional params, extra `creds` parameter, sync vs async mismatch.

- [ ] `__init__` signature matches every call site
- [ ] `close()` exists and is `async` if dispatched from the async path
- [ ] `save_token` / `load_token` are async if your loader awaits them directly

### 4. Tool naming + registry parity

If you have a registry that lists tools per connector AND each connector's tool file declares `Tool(name=...)` entries, run the parity test that diffs the two. Plus a manual sanity check on naming convention:

- [ ] Every tool name matches `(get|search|list|delete|update|run)_<canonical_connector>_<noun>` — NOT `get_<consultant_nickname>_*`
- [ ] Registry's `tools[]` and `tool_schemas{}` keys match each other
- [ ] Every tool exists as a real `Tool(name=...)` entry in code

### 5. HTTP `tools/list` exposure (the dual-path trap)

Connectors can be visible via dynamic-manifest (one client path) but invisible via raw HTTP `tools/list` (another client path). Both must work.

**Naming-convention warning before you write a parity check:** different client paths may use different name shapes for the same tool (full names like `get_klaviyo_campaigns` on one path, prefix-stripped `get_campaigns` on another). A naive set-equality diff between paths will flag 100% of connectors as broken. Normalize both sides by stripping the connector token before diffing.

- [ ] Raw HTTP `tools/list` returns the expected count (i.e. all of them, not 3 of 43)
- [ ] Mega-tool / dynamic-manifest path exposes the same count
- [ ] Counts match between paths

### 6. Vendor error surfacing (TWO layers — both required)

Constitutional rule: vendor text errors (`ERROR NNN::MSG`, error JSON, `{"type":"...","status":4xx}`) must be hoisted to exceptions and surfaced as explicit error envelopes — NOT coerced to empty `{"data": []}` results AND NOT swallowed by the outer dispatch fall-through as `{"raw": null}`.

This is a TWO-layer check. The adapter raising correctly is necessary but not sufficient; the dispatch elif-block must catch that typed exception or the outer `except Exception` will log it and silently leave `tool_result = None`, which the widget formatter ships as `{"raw": null}`.

- [ ] **Layer 1 (adapter):** every HTTP call is followed by a vendor-error check; on error the adapter raises an explicit typed exception with status + resource + hint
- [ ] **Layer 2 (dispatch):** the connector's elif-block in the HTTP dispatch wraps its tool calls in `try/except <Typed>Error` and sets `tool_result = {"error": ..., "hint": ...}` on catch
- [ ] **Smoke test:** invoke a tool against a healthy account that should error. Response must be a structured envelope, NEVER `{"raw": null}`

### 6.5. Per-resource access-token plumbing

For vendors with sub-resource tokens (Facebook Pages, Slack bot vs user, Shopify shop-scoped, Google service-account vs delegated, GoHighLevel agency vs sub-account):

- [ ] If the vendor has per-resource tokens, the adapter accepts/caches/looks up that token rather than reusing `self.access_token` for every call
- [ ] The list-the-resources call captures the per-resource token in its return shape
- [ ] Smoke uses an account with at least one real piece of content on the sub-resource (empty results on a healthy resource is the canary)

### 7. Test value-level, not shape-level

Antipattern: `assert result["record_count"] == 2` passes even when the column mapping is wrong. Real test: `assert result["data"][0]["keyword"] == "expected value"`.

- [ ] At least one test per list-returning tool asserts a VALUE on row 0, not just `len()` or `record_count`
- [ ] OAuth callback test asserts the token landed in the central store with the right shape
- [ ] Adapter signature test exists — the kind that would have caught bug #3 instantly

### 8. OAuth redirect URI matches the vendor portal

Lesson from a real consultant pass: the contributor registered `https://mcp.example.com/oauth/<provider>/callback` in the vendor portal, but the infrastructure actually serves at `https://mcp2.example.com`. Result: 404 even after the code fix because the vendor portal was wrong.

- [ ] Vendor portal redirect URI is your PROD host exactly — verified by logging into the vendor portal directly, NOT by trusting the contributor's commit message
- [ ] If dev testing is needed, the vendor app supports multiple redirects OR there's a dedicated dev app
- [ ] The `redirect_uri` in `auth/<connector>_auth.py` matches what's in the vendor portal exactly (including trailing slash, host, scheme)

### 8b. Scopes — what the live authorize URL actually sends (dual-defaults trap)

Caught on a real Facebook Pages/IG extension: the PR correctly extended scopes from 5 → 10 in `auth/facebook_auth.py`, but `config/settings.py` ALSO defined a `facebook_scopes` field with its own default — in TWO places (the dataclass default AND the `os.getenv` fallback), both with the stale 5-scope string. The auth-module default was dead code; the settings one always won. Every connect produced an Ads-only token; every new Pages/IG tool would have 403'd silently.

The 30-second diagnostic that catches this: **fetch the live authorize URL and read its `scope=` parameter.** Don't trust grep on `auth/<connector>_auth.py` alone.

- [ ] Live authorize URL's `scope=` parameter contains every scope the connector's tool surface actually needs
- [ ] There is exactly ONE source-of-truth scope string. If config and auth both carry a default, they MUST match — preferably collapse to one
- [ ] The env-var fallback matches the source-of-truth default (silent killer: prod containers without the env var set)
- [ ] A regression-guard test exists asserting the live URL emits the full scope set

### 9. Vendor app-review / scope approval status

Discovered on a Facebook Pages + IG Business extension: tools wired cleanly, registry parity passed, dev+prod both green — but the OAuth scopes the new tools required weren't yet approved on the vendor app. Customers connecting via the standard flow hit "scope not authorized" or got empty results on the gated endpoints. **"Shipped" in code-land ≠ "usable by customers."**

#### Scope-PRESENCE ≠ scope-TRAFFIC (Meta dashboard gotcha)

Meta's App Dashboard tracks **call traffic per scope**, not just whether the scope is in your token grant. Two distinct things can fail audit:

| Symptom | Root cause | Fix |
|---|---|---|
| Scope shows zero calls but feature appears to work in your test | Scope is granted (in token) but no API endpoint you hit "counts" toward it. Meta attributes each call to its **most-specific** parent scope. | Add a tool that hits the scope's canonical endpoint. For `public_profile` that means a literal `/me?fields=id,name,email` — `/me/accounts` counts toward `pages_show_list`, not `public_profile`. |
| Scope shows zero calls AND OAuth dialog never asked for it | Dual-defaults trap from §8b, OR scope was just missed entirely. | Add to defaults, re-OAuth to get a new token with the grant. |
| Scope IS in token, IS being granted, IS in call URL, reviewer rejects | App Review needs **observed traffic from a test user**, not just code paths that could theoretically call it. | Exercise the tool against a real test account multiple times at least 24h before submission. |

- [ ] For every scope in the connector's scope list, check the vendor portal: `Approved`, `In Review`, or `Available with restrictions`?
- [ ] If any scope is unapproved, the audit issue MUST list it explicitly, and customer-facing messaging MUST NOT say "shipped" without qualification
- [ ] Smoke against a real account YOU own BEFORE telling any customer the tools work
- [ ] Honest framing: "tools live; X scopes pending vendor app review, customers will see Y behavior until approval lands (~N business days)"

The cost of skipping this is shaped like the consultant-connector-bug cost — customer tries, fails, retries, fails — except worse, because there's no fix you can ship in 30 minutes. The fix is a 3-7 day vendor review cycle.

### 9.5. Duplicate config-source trap (silent override)

Pitfall surfaced on Facebook: PR added 5 new scopes to `FB_DEFAULT_SCOPES` in `auth/facebook_auth.py`, but `config/settings.py` had its OWN field with the old string. The auth code did `getattr(settings, "facebook_scopes", None) or FB_DEFAULT_SCOPES` — `settings.facebook_scopes` ALWAYS won because it's a real attribute, never None. `FB_DEFAULT_SCOPES` was dead code.

For ANY connector-level constant (scopes, redirect URI, API base, version):

- [ ] Exactly ONE source of truth. If two: the one in `config/settings.py` will win — confirm by reading the actual `getattr(...) or DEFAULT` site
- [ ] When the contributor adds new values, they updated EVERY duplicate or deleted the duplicate
- [ ] Live verification (§5/§8) is what catches this — never trust code-reading alone

### 9.6. Parallel code path trap (refactor missed sibling)

Pitfall surfaced on Mailchimp: a fix correctly made the inline `server.py` loader async-aware, and a separate PR migrated the TokenManager to sync helpers. But `auth/mailchimp_auth.py` had THREE helper methods doing `await self.token_manager.load_token(...)` — a parallel code path the inline fix never touched. Every tool call hit `TypeError: object dict can't be used in 'await' expression`.

Recurred on a metric-spec ship: PR added contract strings to `server.py`'s data-contract render path. CI green, dev deploy green. First smoke against the deployed surface showed the directive MISSING — because the Claude-shaped render path is a near-duplicate in `openai_app/response_formatter.py` with its own override map. Server.py path was instrumented; openai_app path wasn't.

**Mitigation pattern (generalizable):** when intentional duplication can't be collapsed to a single source without architectural lift, add a lockstep equality test that asserts the two copies are equal. Drift becomes a static problem (CI red on edit-one-copy) instead of a runtime one (silent ship, customer-visible).

```python
def test_X_constants_in_lockstep_across_render_paths() -> None:
    """server.py and openai_app must carry IDENTICAL X strings.

    They're duplicated by design (different render paths, can't share a
    module without an architectural lift), so the only insurance against
    drift is a test that pins equality. If you edit one, the test forces
    you to edit the other.
    """
    from server import _X_CONSTANT_A, _X_CONSTANT_B
    from openai_app.response_formatter import (
        _OPENAI_X_CONSTANT_A, _OPENAI_X_CONSTANT_B,
    )
    assert _X_CONSTANT_A == _OPENAI_X_CONSTANT_A
    assert _X_CONSTANT_B == _OPENAI_X_CONSTANT_B
```

If you are editing one of the left-column files, you almost certainly also have to edit its right-column twin. Audit FIRST, edit BOTH, ship ONE PR.

| Concern | Path A (usually first instrumented) | Path B (the one that gets missed) | Lockstep guard |
|---|---|---|---|
| Token load/save/delete | `server.py` inline loader (async-aware) | `auth/<connector>_auth.py` helper methods (`get_access_token`, etc.) | None today — grep every `token_manager.(load|save|delete)_token` call site, confirm sync/async parity |
| Per-tool data contract text | `server.py:_tool_data_contract_text` (stdio + raw HTTP path) | `openai_app/response_formatter.py:_build_data_contract` (Claude/widget path) | A test like the above — string-equality assertion forces CI break on drift |
| Tool registration | `tools/<connector>_tools.py` (`Tool(name=...)`) | `config/connector_registry.json` (`tools[]` + `tool_schemas{}`) | Generalized parity test |
| Tool dispatch | `server.py` async elif-block | `server.py` HTTP dispatch elif-block for the same connector | None — grep both for every `name == "<tool>"` branch on a new tool |
| OAuth scope set | `auth/<connector>_auth.py:<CONNECTOR>_DEFAULT_SCOPES` | `config/settings.py:<connector>_scopes` (dataclass + env fallback) | §8b live-authorize-URL inspection |

The duplication is intentional in most cases. The architectural cost of unifying them is high; the operational cost of leaving them un-mirrored is the §9.6 trap. Lockstep tests + this table are the cheap insurance.

When you add a new sibling pair to this table, **add the lockstep test FIRST** so the table entry has a CI-enforced backing.

### 10. Live tool invocation smoke (NEVER skip)

Pitfall surfaced on Mailchimp (twice): "shipped" was claimed after verifying that tools appeared in `tools/list`. They did appear. They were also 100% non-functional at dispatch. Listing visibility is necessary but not sufficient. The customer hit the TypeError on the first real tool call.

**Before any "shipped" / "fixed" / "ready" claim:**

Get a JWT for a test user. Invoke at least ONE representative READ tool against the prod endpoint with that JWT. Confirm the response has actual data, not just an error envelope. For each connector, smoke at least one tool from each category present:

- **Account/profile read** (`get_<x>_account`, `get_<x>_profile`) — easiest signal of dispatch health
- **List read** (`list_<x>_<resources>`) — proves pagination/serialization
- **Detail read** (`get_<x>_<resource>` with an ID from the list) — proves parameter passing works

If the connector has write tools, do NOT smoke them in this audit. Stick to read-only.

#### What's required to mark §10 clean

| Result | Verdict |
|---|---|
| HTTP 200 + JSONRPC `result` + parseable JSON body + at least one expected field | ✅ clean |
| HTTP 200 + `Tool <name> error: …` in `content[0].text` | ❌ **DISPATCH BUG** — usually means async path doesn't match adapter signature. Do NOT ship. |
| HTTP 200 + auth-required envelope | ⚠ test user isn't authorized — re-auth and retry; not a code bug but smoke didn't complete |
| HTTP 401/403 | JWT expired — refresh and retry |
| HTTP 5xx | Container is unhealthy — separate issue |

#### Pitfall: error envelopes inside HTTP 200 responses

Many MCP servers wrap tool failures in `result.content[0].text` with the literal string `Tool <name> error: <message>`. The HTTP response is 200, the JSONRPC envelope has `result` not `error`, but the actual tool failed. **Always parse `content[0].text` and check for the error prefix** — do not stop at HTTP 200 or "JSONRPC result is present."

#### Pitfall: auth-required envelope is partial §10 evidence, NOT full

A successful smoke against an authenticated user is the whole picture. An auth-required envelope means dispatch wiring works (tool was found, gate fires cleanly) but the new vendor-facing code paths were never exercised. The honest status framing when you hit this:

> "Shipped to prod: deploy green, tools dispatched cleanly on `/mcp/tools/list`, CI value-level tests cover the new code paths. Vendor-side verification (real call returning the new envelope shape) is owed to the next authenticated session — instructions for what to look for in the issue comment."

Do not claim "fully verified end-to-end" without the real vendor response. Do not under-claim either — dispatch+CI is meaningful evidence, just not the whole picture.

#### Pitfall: "Retrieved 0 results." is NOT a failure signal

Some MCP wrappers inject a canonical data-contract footer into every tool response's `content[0].text` slot. It typically reads `Retrieved 0 results.\nData contract: ...\nPowered by <wrapper>`. **The real payload lives in `result.structuredContent.data`** — a dict with the actual adapter return value. A successful tool call shows `Retrieved 0 results.` in text AND has `structuredContent.data.<field> = <value>`. Do not flag the prose as failure; parse `structuredContent.data` and assert real fields.

This is the single highest-value check in the audit. If you have time for only one, do this one.

### 11. Dev AND prod deploy both green

Lesson: a direct-to-main style commit can leave Development behind. Always check BOTH environments after any connector-affecting merge.

- [ ] Last Development deploy is green
- [ ] Last main deploy is green
- [ ] `tools/list` on BOTH hosts returns the connector at expected count

### 11.5. OAuth scope drift — verify stored token scopes BEFORE blaming code

When a vendor connector returns "Application does not have permission" / "Invalid OAuth 2.0 Access Token" on tools that *should* work — and connector status says Connected, and the code looks right — **check the stored token's scope set BEFORE filing a code bug or delegating an audit**.

Failure mode: a recent PR added a new scope to the OAuth request. Users who authorized BEFORE that PR have valid-but-stale tokens — the right scopes were never granted. Status reports green; API calls needing the new scope fail.

**30-second diagnostic (Meta example):**

1. Grab the `access_token=` query value from any leaking error envelope URL
2. `GET https://graph.facebook.com/v21.0/debug_token?input_token=<T>&access_token=<T>`
3. Diff returned `scopes[]` against what your tool needs. The diff IS the explanation.

Generalize per vendor: Google = `tokeninfo` endpoint; Microsoft = decode the JWT; Slack = `auth.test` returns scopes header; Stripe = `ListPermissions`. Every major OAuth vendor exposes an introspection path.

**Fix is operational, not code:** reset the user's token + OAuth re-consent. Zero PRs.

**Add this as the FIRST check in any "this connector broke" investigation.** It goes BEFORE the code audit, BEFORE delegating a fix subagent, BEFORE reading server.py.

### 12. Release-promotion PRs MUST cut from origin, not local

Bit twice in one session. Pattern is identical and silent.

**The trap (do NOT do this):**

```bash
git checkout main && git pull          # main is fresh
git checkout -b release/X              # branch from local main
git merge Development --no-edit        # ← local Development is STALE
                                       #   (no `git pull` since the last
                                       #    Development merge happened)
git push -u origin release/X
gh pr create --base main && gh pr merge --admin --merge
# Deploy goes green. Image SHA changes. Container restarts.
# Code on prod is UNCHANGED because the merge had nothing to merge.
```

**The fix:**

```bash
git fetch origin -q
git checkout -b release/X origin/Development   # cut DIRECTLY from remote
git push -u origin release/X
gh pr create --base main ...
```

The `git checkout -b release/X origin/Development` form sidesteps the trap entirely — there's no local Development branch in the equation, so it can't be stale.

**Pre-promotion verification (catches the trap if you forget):**

```bash
# This should be NON-EMPTY for any file the new PRs touched
git fetch origin -q
git diff origin/main..origin/Development -- <changed_file_path>
# If empty when you expect changes, local Development is stale.
# Re-cut release branch from origin/Development directly.
```

**Why this fails silently:** the merge produces zero diff, the PR shows green CI, the deploy workflow ships the new commit SHA, the container restarts cleanly. Every signal says "shipped." But `git show <deploy_sha>:<changed_file>` returns the OLD bytes because the deploy SHA points to a merge commit with no changes underneath it. You only catch the failure when you actually invoke the tool and see the bug you just "fixed" still present.

**Pre-flight check for §11 deploy verification:** before declaring deploy green, confirm the deployed image SHA's bytes match what you intended to ship — not just that the workflow run reports success. The image-SHA-to-bytes check is mechanical (one git command) and catches both this trap and the rarer case where the deploy step itself shipped a stale build artifact.

### 13. Multi-round audits are not churn (vs the Mailchimp anti-pattern)

A single audit cycle CAN legitimately produce N rounds of fix-then-re-exercise, with each round revealing previously-hidden defects that the prior fix exposed. **This is not churn.** The discipline distinction:

| Anti-pattern (Mailchimp) | Healthy multi-round audit |
|---|---|
| Customer hits bug → fix bug → push → customer hits NEXT bug → repeat | Customer hits bug → run full audit → file ONE issue with N findings → ship ONE PR for all N → re-exercise → if new findings emerge, file ONE issue + ship ONE PR for them |
| Each round = one symptom-driven hotfix | Each round = one full-audit-driven consolidation |
| Customer-perceived "this product is on fire" | Internal "iterative discovery, each shipped cleanly" |
| Caused by skipping audit | Caused by AUDIT finding new things only the previous fix could expose |

**When in doubt:** if you've shipped 3+ PRs in one session for the same connector AND each one carried a single finding AND the user was the trigger ("retry"), STOP and run the full audit. If you've shipped 2-3 PRs AND each carried multiple findings AND the trigger was re-exercise revealing newly-reachable defects, you're on the healthy multi-round path.

## After the audit: file ONE issue, ship ONE PR

The output is a single GitHub issue titled `<Connector> connector audit — N findings`, body is the full checklist with every finding marked done/issue/n-a, and a `## Proposed fix plan` section listing every code change needed.

Then open **one** PR that addresses every finding. Even if the PR touches 10 files. The cost of "one big PR" is review time; the cost of "ten small PRs" is customer-perceived churn. The former is bounded and internal; the latter is unbounded and external.

The PR description must enumerate which audit findings it closes, and the PR must include the value-level tests from §7 above as regression guards.

## Personnel comms after a process finding

When the audit surfaces a process issue tied to an external collaborator — direct-to-main push, missed PR, no-tests-on-shipped-code, or any pattern that crosses into "the contributor should have done X" territory — file the technical fix and the regression-test PR as normal AND surface the process finding to your team lead in writing. **Do NOT initiate outbound comms to the contributor about the process issue.** Personnel-flavored conversations belong to the team lead.

The two are separate channels: the audit fix lands as normal engineering work via PR; the personnel conversation about *how* the change was shipped is the lead's. Offering to draft the contributor note is fine; sending it without explicit go-ahead is not.

## Before saying "try again" to the human

Don't ping the customer with "fixed, try again" until you've done the human's flow yourself. Concretely:

1. Get a fresh JWT for a test user
2. Hit the actual `/connect?connector=<connector>` endpoint, follow the redirect chain to `/oauth/<connector>/authorize`, confirm 302
3. After OAuth completes, call the dynamic-manifest mega-tool AND the raw `tools/list` from the same client
4. Invoke one representative read tool against a real account (or the test account if vendor allows)
5. Only then send the "try again" message — and frame it as "verified end-to-end on prod with my own test account, here's what to expect" not just "PR merged"

If you can't verify end-to-end (no test account, vendor portal blocks dev), the honest framing is "fix shipped, I couldn't fully verify because of X — please test and let me know what you see." Not "try again."

## When to merge a contributor PR going forward

Run this checklist BEFORE clicking merge on any contributor PR introducing or touching a connector. The audit on a fresh contribution catches the same bugs but BEFORE the customer hits them. The 30 minutes you spend on the checklist is the cheapest insurance available.

If the contributor pushes back ("this is overkill for a small change"), the right answer is the Mailchimp inventory above. Nine round-trips and a damaged customer relationship is what the alternative costs.

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
