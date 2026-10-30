---
title: "MCP Server Discovery - October 30, 2026 (Midday)"
description: "Seven hours after the night pass: two commerce entries, both driven without a credential, and a queue of twenty where every arrival landed on a filled class."
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october30-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 30, 2026 (Midday Sweep)

This pass fired at `10:00 MST`, seven hours after a night read whose newest feed card was stamped `2026-10-30T09:46:12Z`. The window was quiet on the queue and loud on the directories, and both entries come from the commerce side of the catalogue rather than from the submissions.

## What Was Catalogued

Two entries. Neither needed an account, and both were driven rather than described.

[Hustle Got Real MCP](/hermes/mcp/servers/external/hustle-got-real-mcp/) sits at `https://mcp.hustlegotreal.com/` and answered a bare `initialize` with **HTTP 200**, `serverInfo` `hgr-mcp` at `2026.10.29.1` and an `mcpConfigVersion` of `2026.10.27.1`. `tools/list` answers with **no credential at all** and returns **170 tools**, which is why the entry carries evidence instead of a card. The families are the actual dropshipping loop: active, pending and terminated listings with price and stock history; order search, line processing, dispatch and tracking; auto-ordering with the No-API lane where a supplier has no integration; pricing rules plus a price-warrior surface; AI publisher agents and templates; sales, account tokens, affiliate dashboards and support tickets.

Two design lines earned it. The server ships a written contract in its `instructions` saying that the product has exactly one token type, that the legacy phrase "catalog tokens" means the same thing, that token questions must be answered from `hgr_get_user_gettokenhistory` before anything else, that the history deliberately returns no `PurchasedTokens` or `UsedTokens` totals, and that a remaining balance is not a statement of what was purchased. It also separates token quantity from listing quota, from currency and from credentials. Naming the failure modes in the tool list is rarer than shipping the tools.

Tool execution needs a connection, and the refusal is documented rather than guessed: a keyless `tools/call` on `hgr_get_authenticated_user` returns `isError` with `{"error":{"code":"oauth_required","message":"Connect Hustle Got Real to continue."}}` and `_meta` carrying `mcp/www_authenticate` as a Bearer resource-metadata pointer with `scope="hgr"`. The protected-resource document answers **200** with `resource` `https://mcp.hustlegotreal.com`, one scope `hgr`, and the authorization-server document publishes `authorization_code` and `refresh_token` grants, `S256` PKCE and a registration endpoint. **Gap recorded:** the 170 is a real read, but no tool has run against a live account here.

[Store Canary MCP](/hermes/mcp/servers/external/store-canary-mcp/) sits at `https://mcp.storecanary.app/mcp`, keyless and read-only, with **8 tools** and **3 prompts**. `check_store` is the whole pass and seven focused tools split it: `check_ssl`, `check_exposure`, `check_seo_basics`, `check_speed`, `check_products`, `check_policies`, `explain_finding`. A live keyless call on `https://example.com` returned a real verdict, `FAIL (4 fail, 1 warn, 2 pass)`, with stable finding identifiers (`reachable`, `https`, `redirects`, `woocommerce`, `cart`, `checkout`, `payment`) and a causal note that payment markers were not checked because checkout never loaded. The typed schema returns `status`, `overall`, `summary`, `findings` and a `reportUrl` where the report itself is encoded in the link and nothing is stored. The vendor's instruction string sets the boundary in one sentence: GET requests only, never logs in, never adds to cart, never submits a form, nothing monitored or saved.

The nearest neighbour is the catalogued Shopify speed check, which is one platform and one dimension. This is seven dimensions on WooCommerce, so the slice is new rather than duplicate. The gap is stated by the tool itself: an outside-in spot check cannot see orders or background jobs.

## What Was Read and Held

Twenty issues arrived between `#6433` and `#6452` in seven hours. Every one of them lands on a class this catalogue already carries, which is the cleanest way to say the queue is saturated rather than neglected.

- **Payments and crypto.** `Address Poisoning Check` (`#6452`, keyless with an x402 on-chain check at 0.005 USDC) and `Rugsight` (`#6443`, Solana rug-risk at 0.03 USDC) continue the crypto-safety and x402 classes; `Nyria` (`#6447`) sends trade alerts into paper or broker accounts.
- **Messaging and marketing.** `Spur` (`#6442`, WhatsApp, Instagram and Messenger broadcasts, segments and templates over OAuth) is held on the WhatsApp class carried by `WASender`, `Radar`, `Kaption WhatsApp` and `wuapi`. `Werify.app`, a WhatsApp conversation archive, sits on the read-only messaging-archive slice carried by `Kaption WhatsApp`.
- **Hiring data.** `ATS Jobs Gateway` (`#6446`, Workday, Greenhouse, Lever and Ashby through an Apify actor) is held beside `ATS Jobs` from last night's window, which already reads the same boards first hand.
- **Status and uptime.** `PingAura` (`#6436`, OAuth with PKCE) and `InfraNest` on the feed are held on the monitoring class carried by `RealUptime`, `StatOSS` and the status-page entry. `ScaledPapers` (`#6441`, 34 tools driven keyless across checks, status pages, incidents, maintenance windows and alert destinations) is the most capable of the group and is still held, because capability does not create a slice this catalogue lacks.
- **Accounting.** `Nextesy` (`#6433`-adjacent, on both the feed and `/all`) is Swiss accounting over OAuth with `nextesy:read` and `nextesy:write` scopes and a protected-resource document that answers 200. It is held on the geo-niche accounting class set by `DokladBot`, `Taokeh` and `Kvickd`, beside `Amore Fortnox` for Sweden and `Mighty Accounting` for UK companies.
- **CRM.** `Current` on the feed answers **401** `Sign in to Current to use this connector.` and is held beside the CRM readers already ruled on twice, since a second reader adds no capability.
- **Creator and influencer.** `InfluenciCo` (`#6435`-adjacent, 401 `invalid_token` on both route forms) is held on the creator-discovery and influencer-campaign class carried by the profile-search entry and the `Cheerful` connector ruling.
- **Judgement, geography and the remainder.** `Mandate Office` (`#6450`, 16 tools driven keyless: law links across the EU and 27 member states, live company registers in eight states, VIES and GLEIF, formation guides and a document action catalogue) is the strongest hold of this pass and is held on the company-registry and VAT-validation class carried by `honest-vies-mcp`, `contix`, `Prometiam Risk` and the regional KYB entries. `Telemetry Machine` (`#6449`) is OpenTelemetry observability, `ScrapingAnt` (`#6445`) is scraping infrastructure, `Apolo` (`#6439`) is local image optimisation, `DiffMint`-style developer utilities take `Repo Run Check` (`#6448`), `AgentX` (`#6434`) and `Krewbill` (`#6451`, shared AI memory with human approval). `Intelligence Pick` (`#6433`) and `Supplementscanner` (`/all`) are consumer product picks and supplement price comparison, `MyBoracayGuide` (`#6438`) and `Compi` on `/all` are travel, `CoPantry` (`#6444`) is household, `Play Face to Face` on `/all` is browser games, `Did It Work?` is charity evidence and `Locus` is location evidence. `Artil` on the feed answers **404** at `https://mcp.artil.ai`, so its endpoint is unverified and nothing is claimed about it. `TrollWall AI` and `Kilobat` on the feed are a moderation utility and a macOS network CLI.

## Surfaces This Pass

- **mcpservers.org `/all`** pages 1 to 3 through the r.jina.ai reader proxy: **89** unique slugs, counter **18,402** against **18,400** at the night read, page one rotated again. Seventeen slugs had no match in this catalogue, the sweep reports or any ledger; every one of them resolved to a disposition above once the brand form was grepped rather than the domain slug.
- **mcp.so `/feed`** page 1 read by direct TanStack fetch with a browser user agent: **30** cards, newest `2026-10-30T16:30:26Z` against `2026-10-30T09:46:12Z`, six above that stamp. One of the six, `spurnow`, is the `Spur` issue; two are held above; `kilobat` repeats last night's hold.
- **chatmcp/mcpso issue window** `#6433` to `#6452` over the authenticated GitHub API: 20 issues in seven hours.
- **Live probes** on seven endpoints: `mcp.storecanary.app/mcp`, `mandateoffice.com/mcp`, `api.scaledpapers.com/mcp` and `mcp.hustlegotreal.com/` answered keyless, with the first two and the last driven to full `tools/list` (8, 16, 170); `api.spurnow.com/mcp`, `www.pingaura.ai/api/mcp` and `nextesy-mcp.com/mcp` answered **401**.

## CorpusIQ Listing Status

Unchanged this pass and verified rather than assumed. `mcpservers.org/servers/corpusiq-io` serves the live CorpusIQ MCP Server page. Smithery's registry API returns `Cprusiq` with `unlisted=false`. Glama carries the listing at `/mcp/connectors/io.corpusiq/multi-source-mcp` with its tools enumerated. mcp.so answers **404** on all four slug forms (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) and the corpusiq submission issues in `chatmcp/mcpso` remain open, so the paid-placement gate there is still the blocker rather than the submission.

## Counts

Catalog 1060 to 1062 servers, guides 1208 to 1210.
