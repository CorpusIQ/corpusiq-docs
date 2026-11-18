---
title: "MCP Server Discovery - November 18, 2026 (Midday Supplement)"
description: "Both directory surfaces flat to the key, five queue arrivals in the hour, and one hosted telephony server whose safety checks live in the schema."
category: "MCP Ecosystem"
last_updated: "2026-11-18"
---

# MCP Server Discovery - November 18, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed. Both directory surfaces came back identical rather than merely quiet: the twelve numbered server maps returned **66,342** raw `<loc>` entries, map for map, the distinct key set read **22,440** on both captures, and no `lastmod` row carried a stamp at or after the cutoff. The feed carried **zero** cards in the hour. The submission queue carried **five** arrivals, and one of them is a hosted telephony and mailbox server whose dangerous operations are guarded by required arguments.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,342   against 66,342 at the 17:00Z midday capture
  servers/1  ..... 7,588   held    servers/7  ..... 9,351   held
  servers/2  ..... 5,949   held    servers/8  ..... 6,590   held
  servers/3  ..... 6,518   held    servers/9  ..... 4,024   held
  servers/4  ..... 6,744   held    servers/10 ..... 2,608   held
  servers/5  ..... 6,954   held    servers/11 ..... 2,637   held
  servers/6  ..... 6,756   held    servers/12 ..... 623     held
priority-servers.xml          299 raw,  34 distinct keys   held
remote-mcp-servers.xml         15 raw,   0 distinct keys   held
distinct keys, twelve maps    22,440 against 22,440  = 0 additions, 0 removals
distinct keys, union w priority 22,474 on both sides
lastmod rows at or after cutoff   0
mcp.so /feed                  200 at 157,608 bytes, 37 anchors (35 server,
                              1 agents, 1 clients), 30 stamps, 0 above cutoff
submission queue              #7600 to #7604, five arrivals, bodies in one call
```

Three readings agree and one of them is new for this window: the midday pass could only say the raw count rose by four inside `servers/12` while the key set held, and this pass returns the per-map counts identical to the entry as well, so the four extra forms have stopped arriving too. The `lastmod` scan is **zero** rows above the cutoff, against eighteen rows in the previous window that collapsed to two held listings.

## The feed did not move

The newest card is still `mdexa` at **16:50Z**, which predates the 17:00Z midday capture and was dispositioned there. The read carries **37** anchors: **35** server cards, one `/agents/` card (`saascity-io` at 10:15Z) and the `/clients/` sponsor card at 04:22Z. **30** stamps against **35** server anchors is the same shape every recent pass has recorded, and pairing each stamp to the nearest preceding anchor of any family keeps the sequence readable through the two non-server cards.

One practical note for anyone re-running this: the relative-time text now reads `Submitted N hours ago` and the machine-readable time lives in the `title` attribute as `M/D/YYYY, HH:MM AM/PM` in UTC. A parser keyed on `Added N minutes ago` returns zero cards and reports a flat feed that is actually a stale selector.

## What shipped

### [Hail MCP - A Phone Number and an Inbox for an Agent](/hermes/mcp/servers/external/hail-mcp/)

Hosted at `https://mcp.hail.so` on the root path, with no `/mcp` suffix to guess. *hail* **0.1.3** on protocol **2025-06-18**. **46** tools listed to a keyless caller, of which **27** are read-only, **12** write and **7** destructive; zero resources and zero prompts.

The vendor ships the numbers, the calls, the texts, the mailbox, the saved agents that answer them and the carrier registration that decides whether a number works in a given country - behind one prepaid account rather than four vendors.

**The evidence tier is discovery-open and execution-gated.** `initialize` answered **200** with no credential and returned an `instructions` block written for a model: rules first, then a four-step start order, then the paging convention. `tools/list` returned all 46 schemas with `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint` and `execution.taskSupport` on the task-capable tools. Every `tools/call` then answered **401**, four for four, with `resource_metadata` naming `https://mcp.hail.so/.well-known/oauth-protected-resource`. That document is complete, and the authorization server document is complete on the **other host** at `hail.so/.well-known/oauth-authorization-server/api/auth` - issuer, authorization, token, jwks, registration, introspection and revocation endpoints, code response type, and three grant types. The same well-known route 404s on the MCP host, which is what a split deployment is supposed to look like.

**What makes it worth a guide is that the guards are arguments.** `place_call`, `send_sms` and `send_email` require `recipient_consent` as the JSON boolean `true`, and the vendor states that `"true"` and `1` are refused before a request leaves the process. `acquire_number` takes `confirm_total_cents` and compares it with the offer it is about to buy: a mismatch fails **409** and charges nothing, and quotes expire in **10 minutes** so a purchase cannot ride a remembered price. `release_number` and `delete_agent` need `confirm_e164` and `confirm_name`. Retries carry the `idempotency_key` the first attempt returned.

**Four tool counts on one product, and only one of them is live.** The MCP documentation says the server exposes **36** tools, its own table lists **38** rows, the marketing page says **37**, and the endpoint serves **46**. The eight the table never mentions include `create_file_upload`, which hands an agent a one-time upload link to pass to a shell, and three read-only helpers for carrier verification. The version drifts the other way: the endpoint reports **0.1.3** while the registry carries **0.1.2**.

**The carrier verification family is the differentiator.** `get_verification_requirements` returns the fields, document slots and address requirement for a country, number type and subject type; `check_verification` and `check_verification_documents` dry-run the form and file nothing; `submit_verification` files under `attest_authorized: true`; `get_verification` is polled for `approved` or a named `rejection_reason`; `confirm_verification` enters the code a carrier texts to a person. The limits are published rather than discovered: 10 MiB per file, 29 MiB total, 20 files, 20 fields, and a duplicate submission for the same subject returned as **409**.

Published costs are prepaid with no subscription: **$0.10** a minute for US and Canada voice against the **$0.149** the same four parts cost when billed separately, **$0.01** more per recorded minute, **$0.018 / $0.035 / $0.20** per text by destination, **$1 per 1,000** emails, and a dedicated number from **$0.50** a month at carrier price. Detail, including the three cautions a deployment needs, is in the guide.

## Also identified this pass (not catalogued)

- **Realtimer** (**#7600**, `ai.realtimer/calls`) - **held.** Read-only sales and recruiting call transcripts from a Mac app, at the OAuth tier with a complete protected-resource document naming a `calls:read` scope, and a clean **401**. The surface cannot be measured without a Realtimer **Pro** account and the app that produces the calls, which is the same gate that held Highseat at the midday sweep. A gated endpoint with a good document is a listing until a tool list is measured.
- **Wellnizz** (**#7601**, `com.wellnizz/health`) - **held.** **34** tools over lab results, DNA files and wearables, with OAuth 2.1, DCR and a 401 carrying a resource metadata URL. Consumer health vertical, beside the **metri** and **Verateca** holds from the midday pass.
- **Llamly** (**#7602**, `com.llamly/wordpress`) - **held.** A WordPress plugin that turns a site into an MCP server over content only, with a change journal and one-click undo, registry **1.1.1**. The drive path needs a live WordPress install, and the WordPress content class is already carried by [Elementor](/hermes/mcp/servers/external/elementor-mcp-server/) and [miniOrange](/hermes/mcp/servers/external/miniorange-wordpress-mcp/).
- **worklore** (**#7603**) - **held.** Four of ten tools driven keyless: a keyword map of **269** stories in four editorial groups, a search, a project-suggestion call, and a capability x-ray that returned **T4** with `remote-exec` named at line 2, the evidence quoted and a sha256 on a deliberately hostile test input. That x-ray is real work. It is still a developer-story library rather than a business data surface, and the scanning role sits beside the prompt-injection class already carried by [GLC PromptGuard](/hermes/mcp/servers/external/glc-promptguard-mcp/) and [Poison Armor](/hermes/mcp/servers/external/poison-armor-mcp/).

`/all` was not re-read: **403** by edge policy, the standing condition since 4 November. The twelve sitemaps carry the window without it.

## Counts

Canonical **66,342** against **66,342** with **0 additions and 0 removals** on the twelve-map basis, **22,474** unioned with the priority map on both sides, **0** `lastmod` rows above the cutoff, feed **157,608** bytes with **35** server anchors, **30** stamps and **0** cards above the cutoff, **5** queue arrivals, **5** candidates evaluated with **1** catalogued and **4** held with the gate or class named, guide tree **1,210** directories before this pass and **1,211** after, `hermes/mcp` Markdown **1,658** to **1,660**.
