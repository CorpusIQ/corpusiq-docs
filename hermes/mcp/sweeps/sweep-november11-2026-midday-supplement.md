---
title: "MCP Server Discovery - November 11, 2026 (Midday Supplement)"
description: "The hour after the midday sweep: the sitemap came back byte-identical at 64,336 raw entries, the feed produced exactly one new card, and two"
category: MCP Ecosystem
added: 2026-11-11
last_updated: 2026-11-11
source: "the mcpservers.org sitemap index re-read at 2026-11-11T18:00Z with all fifteen maps fetched individually and each one's /servers/ URLs counted, the mcp.so homepage re-read cache-busted at 288,620 bytes and parsed card by card, the official MCP registry queried by candidate name and by exact namespaced name, the OpenAccountants endpoint driven in one live session of nine requests, the AnythingMCP OAuth documents read on the hosted host and a self-host attempted on this host with podman, and Docker Hub plus GitHub metadata for both repositories"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 11, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep read the same two surfaces at **17:00Z**. A supplement pass has one job that a full sweep does not: prove the hour rather than repeat it. Both large surfaces came back flat in the measurable sense, the feed contributed exactly **one** card, and the two servers that earned guides this pass were not arrivals in this window at all. They were listings the earlier pass read and left undispositioned, which is a different kind of find and is labelled as one.

```text
Surfaces:   /sitemap.xml 200, fifteen maps named, twelve carrying /servers/ URLs
            64,336 raw <loc> entries in those twelve, identical to the 17:00Z capture
            per-map counts identical: 299 / 7,588 / 5,948 / 6,518 / 6,744 / 6,952 /
            6,756 / 9,351 / 6,589 / 4,031 / 2,606 / 954
            newest lastmod 2026-11-11T11:25:56Z (weftcut), already inside the midday read
Feed:       288,620 bytes, 22 cards carrying an "Added" stamp, 1 above the 17:00Z stamp
Catalogued: 2 servers, 2 guides   Held: 1 measured, 6 by class
Crossref:   40+ candidate slugs against the registry, resolved by name and by namespace
```

## The window, proved by arithmetic

The sitemap index answered **200** and named fifteen maps again. Twelve carry `/servers/` URLs; `static.xml` (822) and `skills.xml` (12,579) are counted but not treated as servers, and `remote-mcp-servers.xml` carries 15. The count that matters is the twelve:

```text
priority    299   1.xml  7,588   2.xml  5,948   3.xml  6,518
4.xml     6,744   5.xml  6,952   6.xml  6,756   7.xml  9,351
8.xml     6,589   9.xml  4,031  10.xml  2,606  11.xml    954
```

Every one of those numbers is **identical** to the 17:00Z midday capture, which is the proof rather than a claim: a single arrival in `servers/11`, where the newest entries land, would have made it 955. The earlier pass recorded `servers/11` moving from 601 to 954 (+353) in its own window, so the map is still the fastest arrival signal on this surface and it did not move in this hour.

A 09:00Z cutoff was also run against every `<lastmod>` in the twelve maps and returned **53** entries, all of which are either locale variants of pages counted before (`/pt-BR/servers/...`, `/th/servers/...`) or entries the midday pass had already dispositioned. The newest lastmod on the surface is **2026-11-11T11:25:56Z** (`weftcut`), which predates the midday read. Nothing was published to this surface between 17:00Z and 18:00Z.

## The feed changed its own timestamp format, and one card arrived

The mcp.so homepage answered **200** at **288,620** bytes. It now carries **22** cards with an `Added` stamp, and the stamp is no longer ISO 8601: the relative-time span reads `title="11/11/2026, 08:00 AM"` with `Added 10 hours ago` as the visible text. A parser looking for the `title="YYYY-MM-DDTHH:MM"` attribute that earlier passes used returns **zero** cards on this page and would report a flat feed every hour. The selector is:

```text
<span class="ml-auto shrink-0" title="M/D/YYYY, HH:MM AM/PM">Added &lt;relative&gt;</span>
```

Every stamp on the page, newest first:

```text
2026-11-11T17:20Z  last-ehr                        40 minutes ago
2026-11-11T08:00Z  ctxvault, agent-vscreen, caprock, vibe-shield,
                   unslop-avivgerz-hue, usb-rea, dead-letter     10 hours ago
2026-11-02T12:45Z  442ball                         9 days ago
```

Exactly **one** card sits above the 17:00Z midday stamp: `last-ehr` at **17:20Z**, which the earlier pass could not have seen. The `08:00Z` cohort is the scheduled eight-card batch the overnight pass dispositioned in full, still the same eight, four hours older in the display string and unchanged in composition.

## Catalogued: 2 servers, 2 guides

**[OpenAccountants MCP](/hermes/mcp/servers/external/openaccountants-mcp/)** is a keyless remote server at `https://www.openaccountants.com/api/mcp` and the first entry in this catalogue that answers a tax question with a citation requirement built into the protocol. `initialize` returned **200** as `openaccountants-mcp` **1.4.0** on protocol `2025-03-26`, `tools/list` returned **12** tools, and nine calls were driven in one session. `validate_vat_number` on `LU26375245` returned the live VIES record for **AMAZON EUROPE CORE S.A R.L.** with the address, a millisecond timestamp, the source URL and a next action that separates the verified fact from the inference: the check confirms the number, **not the tax treatment** of the supply. `search_rules` returned eight passages wrapped in an authority order plus *values come from sources you fetch in this session, not from recall*, and it is recorded as imperfect retrieval because a request for a MT/IE/DE rate table came back with Maltese instalment passages. `list_jurisdictions` returned the per-country counts (GLOBAL 83, US 73, AU 60, ES 53, CA 47, GB 34, MT 34, DE 30) with named reviewers beside six of them, and the field `accountant_verified_skills` reading **0** on every row is recorded as a defect of the field rather than an absence of reviewers. `compute` exposes **15 versioned engines**, each `needs_input` reply carrying the engine's `code_url`, `tests_url`, `figures_url` and `node --test` command, and it is **broken over MCP in 1.4.0**: two engines both answered `missing input 'tax_year'` with `tax_year` supplied as the enum value they ask for, reproducer recorded in the guide. Licence is AGPL-3.0 for code with skill content under its own licence, the listing carries a lastmod of **11:15Z** and registry record `io.github.openaccountants/openaccountants` **1.0.0** declares the same remote. It enters beside [honest-vies-mcp](/hermes/mcp/servers/external/honest-vies-mcp/) and [casus-mcp](/hermes/mcp/servers/external/casus-mcp/) and is the cross-border rulebook those two do not carry.

**[AnythingMCP](/hermes/mcp/servers/external/anythingmcp/)** is the closest thing in this catalogue to a company-wide connector platform: an AGPL-3.0 self-hosted gateway that registers tools at runtime from 696 catalog connectors plus your own REST/OpenAPI, SOAP, GraphQL, OData, SQL, IMAP/SMTP or MCP sources, keeps a company knowledge graph that links a customer across systems, and gates every call with per-tool permissions and response mapping that drops fields before the model sees them. The hosted endpoint answers a keyless `initialize` with **401** and a JSON-RPC `-32001 Authentication required` beside a full set of OAuth metadata; the finding in those documents is that the **protected-resource declares no scopes at all** while the authorization server advertises `openid` and `email`, so a client cannot discover what its connection will carry, and `client_credentials` sits in the grant list beside the two it needs. The self-host install was attempted rather than described: Postgres 17 came up healthy on a podman network, and the app image **refused to pull** on this arm64 host (`no image found in image index for architecture arm64`), then pulled under `--arch amd64` and exited with `exec /usr/local/bin/docker-entrypoint.sh: exec format error` because no amd64 binfmt handler is registered. Nothing was driven, so the guide states every capability as the vendor's and records three different connector counts (732 in the README header, 696 in its feature table, 255 in the registry record, against 732 in the repository's own `server.json` at **0.53.0** while the registry still holds **0.10.0**). The operator-facing reason for the page is the surface, not the vendor: 60,677 image pulls, 775 stars, and a permission model an operator can point at in a security review.

## Also identified this pass (not catalogued)

One held on measurement, the rest on class with the owner named, each recorded so the next pass does not re-triage it:

- **`last-ehr`** (the single fresh card, `io.github.cbetz/last-ehr` **0.5.1**, Apache-2.0, npm `@lastehr/mcp`): FHIR chart tools, read-only by default, writes gated by elicitation with the human seeing the Observation before it saves and the agent getting a read-back diff after. Genuinely the closest surface in this batch to a first of class, since there is no clinical entry here, and held on its own statement of state: the README's first status line reads **early / alpha, use synthetic data only**, the Epic and Oracle sandbox adapters sit behind `LASTEHR_EXPERIMENTAL_FHIR_ADAPTERS=1` because those sandboxes cannot delete an approved write and the safety eval cannot clean up, and the vendor is explicit that this is not a clinical or compliance claim. A re-check wants a real chart and a clinic, not another read.
- **`livecrm`** (Salesforce and HubSpot dedupe, normalize, enrich, mass update behind OAuth with `dedup:merge`, `runs:dispatch`, `runs:reverse` and `audit:read` scopes): a **prior disposition**, held on the sales-CRM class on **14 October**, carried forward rather than re-judged. The scopes were re-read in this pass and confirm the design, writes are runs that can be reversed, and nothing in them changes the class ruling.
- **The Bitrix24 fleet** (`io.github.bitrix24/bitrix24` **1.0.0**, `RCS-kz/bitrix24-mcp` with 55 tools and a published threat model, `dev.wirecat/bitrix24-cli`): held on the saturated CRM class already carried by [Salesforce](/hermes/mcp/servers/external/salesforce-mcp/), [Perfex](/hermes/mcp/servers/external/perfex-crm-mcp/), [QoreNext](/hermes/mcp/servers/external/qorenext-crm-mcp/), [AccountHub](/hermes/mcp/servers/external/accounthub-mcp/) and [CRMSolid](/hermes/mcp/servers/external/crmsolid-mcp/). The RCS build is the most careful of the three, confirm-gated with per-tenant rate limits and a keychain-held webhook token, and it is proprietary and cloud-only, so a re-check needs a portal.
- **`mcphub`** (`samanhappy/mcphub`, self-hosted MCP gateway and control plane with scoped credentials, per-user visibility, logs and health monitoring): held on the agent-gateway class carried by [kosa8](/hermes/mcp/servers/external/kosa8-mcp/), [AgentKeyGate](/hermes/mcp/servers/external/agentkeygate-mcp/), `Herald` and `Shellway Relay`, with AnythingMCP catalogued this pass as the endpoint-plus-brain variant. It is the strongest open-source control-plane candidate seen since kosa8 and is named here rather than dismissed.
- **`jfs` / JFSecure** (`io.github.theone55/jfs` **2.10.0**): secrets an agent uses without ever receiving, approved per use in a desktop app. Held on the local-install tier and on the credential class that AgentKeyGate and `offprompt` already own; it needs an unlocked JFSecure application, so no probe from here is meaningful.
- **`cloud-finops-skills`** (OptimNow, CC BY-SA 4.0, seven MCP tools and a Claude plugin over AWS, Azure, GCP, AI and data-platform billing): held on the FinOps class, which has become crowded inside a single day: `io.costory/finops` was published **15:19Z today**, `com.omnitoolcalc/llm-finops-suite` at **07:46Z**, and OptimNow's own `io.github.OptimNow/ai-pricing-hub` is already the catalogue's OptimToken entry. A class with four owners inside a week needs a driven comparison, not a fourth listing.
- **The rest of the batch, by class**: `forgejo` (self-hosted git, developer infrastructure), `godotwright`, `unity-mcp`, `davinci-resolve-mcp`, `weftcut` (media and game tooling), `pokemontcgapi` (collectibles, per the PokeInvest hold), `nonecap` (captcha solving, the anti-bot class), `che-ical-mcp` (macOS Calendar and Reminders, the calendar class), `alterlab-mcp-server` (scraping with anti-bot bypass, the scraping class), `llmtrim` (an LLM traffic compressor, the proxy and cost class), `mcp-techtrend` (news briefing, the research class), `contextnest` and `synaplan` (memory and RAG), `runemap` (weather), `logseq`, `mongo-server`, `django-orm-lens` (developer tooling), `cloudbase-ai-toolkit` (Tencent backend, geography), `design-os-studio` (design class), `hollow` (a Chinese agent-workface project), `riskmodels` (quant finance), `beancount` and `actual-mcp` (ledger and personal budget, the accounting class), `openproject` and `basecamp` (project management, the saturated PM class), `singitai`, `skim402` and `openany` (x402 and pay-per-call classes), `souls` (agent identity).

## Ops details that held, and two that did not

- **The supplement's baseline is the sweep page's read time, not the ledger.** `.last-sweep` is appended oldest-to-newest across three files (`mcp/`, `servers/`, `servers/external/`), so its **head** is not the newest pass. The reliable baseline is the most recent file under `sweeps/` by mtime. Reading the ledger head cost this pass a false start on a body of November 7 text.
- **A registry search by product name is not a search by namespace.** `search=anythingmcp` returned **no** records; `search=io.github.HelpCode-ai%2Fanythingmcp` returned the record immediately. When a slug is `author/name`, query the namespaced form before concluding a product is unpublished.
- **Registry records drift behind the repository.** AnythingMCP's record holds **0.10.0** with a 255-connector description while its `server.json` on main declares **0.53.0** and 732. Read `server.json` on the default branch before quoting a version.
- **The mcp.so stamp format changed under the parsers.** `title="M/D/YYYY, HH:MM AM/PM"` in the relative-time span, UTC, with `Added N hours ago` as the text. A missing card count is now a parser symptom, not a flat feed.
- **Check the architecture before planning a container install.** `podman pull` on aarch64 refuses an amd64-only manifest; forcing `--arch amd64` lands the image and then fails at exec with `exec format error` when no binfmt handler is registered. The refusal is the useful signal and it arrives before the pull, not after.

## Counts

Canonical **64,336** against **64,336** with **0** additions and **0** removals across twelve server maps and fifteen documents; newest lastmod **2026-11-11T11:25:56Z**; feed **288,620** bytes, **22** stamped cards, **1** above the midday stamp; **40+** candidate slugs cross-referenced, **2** servers catalogued with **2** guides, **1** held on measurement and **6** by class with the owner named; **9** live requests to one endpoint across seven tools, **1** self-host attempted through pull, forced pull, a healthy Postgres and an exec failure; guide tree **1,149** directories before this pass and **1,151** after, **1,293** entries before and **1,295** after, **1,570** Markdown files under `hermes/mcp/` before and **1,573** after.
