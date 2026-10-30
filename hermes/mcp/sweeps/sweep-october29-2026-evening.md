---
title: "MCP Server Discovery - October 29, 2026 (Evening)"
description: "Nine hours after the midday pass: two finds from a thirteen-issue window, a recruiting platform and a writing-voice library with release digests."
last_updated: 2026-10-29
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october29-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 29, 2026 (Evening Sweep)

This pass fired at `21:00 MST` against a midday read whose newest feed card was stamped `2026-10-29T16:55:43Z`. Nine hours is a normal evening gap, and the shape of the window was the same as the last three reads: the directories rotated without growing, the feed carried four cards, and the submission queue carried the substance.

## What Was Catalogued

Two entries, both from the **issue window**, which ran `#6404` to `#6416` with thirteen submissions between `16:48Z` and `01:44Z`. Both are first entries for their class in this catalogue, which is why they are in rather than held.

[Selenios MCP](/hermes/mcp/servers/external/selenios-mcp/) is the first recruiting and ATS surface here. `https://back.selenios.com/api/mcp` answered a bare `initialize` with **401** `{"error":"invalid_token","error_description":"Missing Authorization header"}`, and the protected-resource document returned **200** with resource `https://back.selenios.com/api/mcp`, authorization server `https://back.selenios.com/`, `resource_name` **Selenios MCP Server** and a single scope, `mcp:tools`. OAuth 2.1 with dynamic client registration, no API keys. The vendor's own documentation, published **21 October 2026**, states **45 tools** covering candidate search, vacancy shortlists ordered by AI score with per-criterion breakdown, interview transcripts with speaker identification, keyword search across every transcript at once, pipelines, average days per stage, organisation KPIs, and the write side: tag, note, email from a template, move stage, reject with a reason, recalculate a score, create a vacancy, add pipeline stages, edit screening questions. The design line that earns the entry is permission parity: each tool requires the same permission as its in-app equivalent, a tool the role cannot use is never offered, queries are limited to the caller's company, and confidential searches stay invisible. Discovery has a quirk worth recording: the host-root `/.well-known/oauth-protected-resource` returns **200** while the `/mcp` suffix form returns **404**, so a client that only guesses the suffix fails against a server that works.

[Silvertongue MCP](/hermes/mcp/servers/external/silvertongue-mcp/) is the first writing-voice surface, and it was driven to a full listing keyless. `initialize` answered **200** as `silvertongue` **0.1.2**, `resources/list` returned **27 `VOICE.md` profiles** of roughly 3 to 4 KB each across the tech, celebrity, comedy, classics and politicians lanes, and `tools/list` returned four: `search_voices`, `get_voice`, `get_voice_packet`, `get_changes`. Every response carries a `release_id` sha256 digest pinning the catalogue release, so a voice quoted in one campaign can be reproduced after the catalogue moves, and `get_changes` reports which voices were added, re-studied as a new edition or removed. The packet tool is the practical half: it returns the full VOICE.md plus an exact length target fitted to the platform's limit and the rules that keep the user's own facts, and it opens with a line that replaces any earlier voice, so switching voices mid-conversation is one call. Licensing splits by asset, Apache-2.0 for the code and CC BY 4.0 for the profiles, and the server states its own limit plainly: the profiles are unofficial studies of public writing technique and the people named did not write or endorse them.

## What Was Read and Held

Thirteen issues arrived and two became entries. The rest are dispositioned in the catalog so the next pass cannot read them as fresh.

`zsign` (`#6415`) sends documents for e-signature with a signed PDF, completion certificate and audit trail over OAuth 2.1, held because the e-signature class is already carried by the official **SignWell** entry plus **SignSimple** and `signer-mcp`; its per-envelope pricing is a commercial detail rather than a new surface. `Doseedo` (`#6414`) scores a film to picture with frame-exact cue sheets, tempo maps and one stem per part, the most specific audio tool in this window, held in the saturated media-generation class. `eroq` (`#6404`) is a video, image, voice and music aggregator over Seedance, Kling and Veo, held in the same class as **Varosity** and **Superpowers**. `Renor Engine` (`#6413`) is Markdown notes recalled over MCP for coding agents, held in the memory class this catalogue carries heavily. `TMSClinics` (`#6412`) is a healthcare directory over a `.fyi` domain, held on the register-fleet ruling and the **SleepStudies** healthcare-vertical precedent. `asms` (`#6411`) rents phone numbers for SMS verification with 12 tools and destructive hints on the ones that spend, held as a verification utility. `Cygnix SEO` (`#6409`) is a local SEO toolkit with keyword clustering and a Search Console cannibalization finder, already held on the **18 October** SEO ruling. `AI Resources` (`#6407`) searches 2,000 dated AI news briefings, held in the reference-library class. `GPU Finder` (`#6406`) is already catalogued as `gpufinder-mcp`. `Handoff` (`#6410`) was dispositioned in an earlier pass, `download.fan` (`#6405`) is a media-download utility, and `zsign`, `Selenios` and `Silvertongue` aside the window carried nothing else operator-shaped.

On the feed, four cards sat above the midday stamp. `whiteboard-animation` was dispositioned earlier in October, `mailtester-ninja` belongs to the email-verification class carried by the **MailTester** trio, `paddock-cards` prints and mails greeting cards, which is a consumer print vertical, and `phone-intel-mcp` returns a US phone number's carrier, line type, business, caller name and spam score for **$0.03 USDC per call over x402**, held on the phone-intelligence class already carried by **VeriRoute Intel** and **Numbers Online** plus the x402 pay-per-call ruling.

On `/all`, pages one to three carried **89 unique slugs** against 83 at the midday read while the counter did not move, so the churn was re-publication rather than growth. Page one rotated almost completely and every fresh slug resolved to a prior disposition once the names were grepped in space form rather than slug form: `DemandBird` (social writing, scheduling and analytics with approval links and agency workspace switching) is held against the six catalogued social schedulers, `Cleanvoice` against the media-production class, `OnlyDNS` and `WarpSearch` as developer infrastructure, `SMSPVA` as an SMS verification utility alongside `asms`, `Log-Forge` and `mybolide`'s coding-tools workspace as developer tooling, and `surveysparrow`, `Run it by`, `Noonlaunch`, `Autonnel`, `Quova`, `Nyria`, `Pencil`, `CreateOS`, `dotbrain`, `PlushSource`, `Bibooks`, `Dropify`, `Lebanese Legislation`, `Jet Cab`, `Feminiq Rides` and `AIR Bandenservice` were each already written down in earlier reports.

## Surfaces This Pass

| Surface | Reading | Delta |
| --- | --- | --- |
| mcpservers.org `/all` p1 to p3 | counter **18,230** flat, 89 unique slugs, page one rotated | composition churn, no records added |
| mcp.so `/feed` p1 | 30 cards, newest `2026-10-30T03:18:57Z` | four above the midday stamp |
| chatmcp/mcpso issues | `#6404` to `#6416` | 13 issues in nine hours |
| Live probes | seven endpoints | two driven keyless to full listings, two 401 with contracts, one 200 directory, one metadata path 404 |

## Catalog Movement

Catalog **1057** to **1059** servers, guides **1205** to **1207**.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [All sweep reports](/hermes/mcp/sweeps/)
