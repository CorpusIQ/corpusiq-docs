---
title: mcp-architecture
description: Field guide for operating a 50k+ LOC MCP server with multi-connector substrate. Where files live, the per-connector pattern, deployment topology, dual-render-path traps, and the discipline that keeps it from rotting silently.
---

# MCP Architecture — operating-scale orientation

A skill for the team building and maintaining an MCP (Model Context Protocol) server with 30+ connectors, multiple client paths (stdio, raw HTTP, ChatGPT mega-tool), and the operational discipline that comes with serving real customer traffic through it.

This is not "how MCP works" — that's covered by Anthropic's MCP docs. This is "how to keep a customer-facing MCP server from rotting in 50,000+ lines."

## Endpoint topology — there are usually only TWO backends

Most multi-environment MCP deployments have **exactly two distinct backends** (dev + prod), but often **three+ hostnames** resolve to them because:

- ChatGPT app submissions pin a hostname at approval time; rather than re-submit/re-verify, the team aliases the old hostname to prod
- DNS migrations leave behind aliases

Get this wrong in customer/exec comms and you'll claim "deployed to three environments" when you actually mean two. The lesson came from a misframed announcement email.

**Implications:**
- For customer/exec comms — use two-environment framing: "dev (`mcp-dev`) and prod (`mcp`)." Never describe an alias as "legacy dev" or imply it's separate
- For verification — probing a hostname and its alias returns identical results by design. Listing them as separate verifications is redundant noise, not extra coverage. Verify against the canonical dev hostname for dev, canonical prod hostname for prod, full stop

## The per-connector triplet

For every connector you maintain, you have (at minimum) three files:

```
auth/<connector>_auth.py              # OAuth or credential paste, TokenManager
data_sources/<connector>_adapter.py   # HTTP client, vendor methods
secure_workspace_mcp/tools/<connector>_tools.py   # Tool() schemas
```

Plus dispatch wiring in `server.py` and registry entries in `config/connector_registry.json`. The registry parity test (see [consultant-connector-audit](../consultant-connector-audit/) §4) enforces that the registry and the tool files agree.

When a connector author skips one of these three files, you get a "tool exists in registry but no real implementation" silent failure that only surfaces when a customer invokes the tool. The audit catches it at PR time, not customer time.

## Credential-paste connectors (Path A)

For OAuth connectors (HubSpot, QuickBooks, Shopify, etc.) the OAuth flow handles the connection UX. For credential-paste connectors (Stripe, Semrush, GunBroker, API-key databases, BYOK), **the credential-store methods on your server class are NOT enough.** You must also register HTTP routes in both API files so the user can actually hit a setup form.

### The failure mode this prevents

Real bug: a Phase 1 PR shipped a full credential-paste connector (adapter + auth + tools + 4 server-class credential methods + error payload pointing users to `/api/v1/<x>/connect`)... but **zero HTTP routes were registered.** User clicks Connect → 404 Not Found. The credential-store methods were orphaned in Python — callable from the codebase, invisible over HTTP. Lived in production for a month.

### The required routes

Mirror an existing credential-paste connector's route block. For our pattern, that's 5 routes per API file:

```
GET    /api/v1/<x>/connection   → get_<x>_connection      (masked status JSON)
POST   /api/v1/<x>/connection   → set_<x>_connection      (save credentials, JSON body)
DELETE /api/v1/<x>/connection   → delete_<x>_connection   (remove credentials)
GET    /api/v1/<x>/connect      → get_<x>_connect_help    (HTML setup form)
POST   /api/v1/<x>/connect      → get_<x>_connect_help    (same handler, processes form submit)
```

Plus 5 mirror routes under `/api/v2/custom-app/<x>/...` for the ChatGPT Actions path.

### Audit checklist for every credential-paste connector PR

```bash
# Should be ≥5 (3 connection + 2 connect routes)
grep -c "/api/v1/<name>/" api/rest_api.py

# Should be ≥5 (same shape, v2 prefix)
grep -c "/api/v2/custom-app/<name>/" api/custom_app_api.py

# Should be 4 handlers per file
grep -c "async def \(get\|set\|delete\)_<name>_\|async def get_<name>_connect_help" api/rest_api.py
grep -c "async def \(get\|set\|delete\)_<name>_\|async def get_<name>_connect_help" api/custom_app_api.py
```

If any count comes back zero or low, you've shipped an orphaned credential store. The connector-status response will still cheerfully tell users where to connect — but the URL will 404.

## Dual-render-path trap (server.py vs ChatGPT app)

Symptom: a feature ships, CI green, dev deploy green, you smoke against the deployed surface and the new behavior is **missing** from the response.

Pattern: many MCP servers serving both raw `tools/list` clients (Claude desktop, stdio, raw HTTP) AND ChatGPT mega-tool clients have two render paths for response wrapping:

| Path | File | Reaches |
|---|---|---|
| stdio + raw HTTP path | `server.py:_tool_data_contract_text` | Claude desktop, raw MCP clients, ChatGPT mega-tool body |
| Claude/widget path | `openai_app/response_formatter.py:_build_data_contract` | Claude.ai, VS Code Insiders, widget-aware clients |

Adding a render directive to one path and not the other ships a feature that's invisible to half your customers.

**The fix is architectural debt management, not code:** when intentional duplication can't be collapsed to a single source, add a **lockstep equality test** that asserts the two copies are equal. CI red on edit-one-copy is the durable fix. Pattern below; full discussion in the [consultant-connector-audit §9.6](../consultant-connector-audit/#96-parallel-code-path-trap-refactor-missed-sibling).

```python
def test_X_constants_in_lockstep_across_render_paths() -> None:
    from server import _X_CONSTANT_A, _X_CONSTANT_B
    from openai_app.response_formatter import (
        _OPENAI_X_CONSTANT_A, _OPENAI_X_CONSTANT_B,
    )
    assert _X_CONSTANT_A == _OPENAI_X_CONSTANT_A
    assert _X_CONSTANT_B == _OPENAI_X_CONSTANT_B
```

## Server.py change patterns

A 50k+ LOC `server.py` has **three** distinct change patterns. Use the right one for the situation:

| Pattern | When | How |
|---|---|---|
| **New connector scaffolding** | Adding a fresh connector | Delegate to a subagent with explicit file paths and conventions; review the diff carefully |
| **Few cross-cutting sites with reasoning** | Changes that touch 2-5 sites, each requiring understanding of context | Surgical hand-patches. Never delegate — subagent iteration cap kicks in before they finish reasoning across all sites |
| **15+ mechanical mirror-edits** | E.g. `dict[k]=v` → `store.put(k,v)` across every connector | One-shot regex transformer, stage to `.staged`, diff-review, mv |

The regex-transformer-then-stage pattern is the highest-leverage of the three. Cost ~5 minutes to write the transformer, cost ~30 seconds to review the diff, ships 15+ sites with zero hand-edits and zero risk of "I missed one." The trap: comments that look like code can match too — always preview the diff before applying.

## Local lint discipline (matters more than you'd think)

If your CI runs `black --target-version py311` and `flake8 --jobs=1`, the local equivalents matter:

```bash
# MUST match CI's target version — local Python 3.14 black formats differently
.venv/bin/python -m black --target-version py311 <file>

# MUST run with --jobs=1 on files like server.py (Python 3.14 has a recursion issue
# with the default parallel flake8 on 50k+ LOC files)
.venv/bin/python -m flake8 --jobs=1 <file>
```

If CI's Black step fails, CI's Flake8 step skips — so a `# noqa` you added and a Black mismatch you missed can both bite at once and you'll only see the Black failure.

## Branch protection + deploy discipline

If you have branch protection requiring PRs to both your Development and main branches:

- Push to `Development` → CI fires dev deploy to dev hostname
- Push to `main` → CI fires prod deploy to prod hostname (most workflows watch only main)
- Use the §12 release-promotion pattern from [consultant-connector-audit](../consultant-connector-audit/#12-release-promotion-prs-must-cut-from-origin-not-local) for Dev → main promotions — cut from `origin/Development`, never from local Development
- After deploy, verify the deployed image's bytes match what you intended to ship (`git show <deploy_sha>:<file>` vs `git show HEAD:<file>`) — the image-SHA-to-bytes check catches both the stale-local trap AND the rarer case where the deploy step itself shipped a stale build artifact

## Marketing site is a separate repo (verification trap)

If your marketing site (homepage, connector list, docs) lives in a separate repo from your MCP server, MCP ship cycles do NOT update the marketing site. After merging an MCP change that touches a customer-visible surface (new connector, renamed tool, new endpoint), verify the marketing site directly:

```bash
curl -s https://www.<your-domain>/<page> | grep <new-thing>
```

Symptom of failing this: a customer reads the marketing site, sees the old surface, tries the new one, hits "connector not found." You shipped the MCP change but the marketing site is wrong.

## Reference material

The substantive pitfalls from the source skill — each one earned the hard way — covered as separate sections in this Hermes Hub:

- [consultant-connector-audit](../consultant-connector-audit/) — the audit checklist that catches what this skill describes how to prevent
- [api-development](../api-development/) — Cloud Run + database backend patterns when your MCP server has a sibling FastAPI surface
- [scheduled-jobs](../scheduled-jobs/) — cron operating manual for the agent that operates the MCP server

## When to load this skill

- About to add a new connector
- About to refactor server.py
- A consultant submitted a connector PR and you're about to merge
- Hit a "feature works in dev but missing in prod" symptom
- About to do a Dev → main promotion
- Customer reports a tool returns the wrong shape — but your tests are green

If you're just running existing tools, you don't need this skill loaded.
