---
title: "MCP Server Discovery - November 28, 2026 (Night)"
description: "Two hundred and forty slugs arrived in one shard, 229 stamped with the same millisecond, four feed cards and fourteen filings yielding three guides."
category: "MCP Ecosystem"
last_updated: "2026-11-28"
---

# MCP Server Discovery - November 28, 2026 (Night)

Fired on the **03:00 MST** tick **six hours** after the evening capture, into the largest single arrival this surface has produced in three days: the thirteen numbered server maps returned **39,089** raw `<loc>` entries against **38,669** at the evening read, and the keyed union moved **24,830 to 25,069**, which is **240 additions and 1 removal**. The additions are not a slow accretion. **Two hundred and twenty-nine of them carry the identical lastmod, `2026-11-28T00:14:03.895Z`** - one write, one timestamp, to the millisecond - and every one landed inside `servers/13`, whose distinct count went from **830 to 1,068** while maps 1 to 12 held at their ceilings.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 15 server-bearing maps read
raw <loc>, all server maps    39,089   (evening read 38,669, +420)
  servers/1 ..... 4,077   distinct 1,987      servers/8 ..... 2,769   distinct 2,000
  servers/2 ..... 2,507   distinct 1,990      servers/9 ..... 2,566   distinct 2,000
  servers/3 ..... 2,949   distinct 1,994      servers/10 .... 2,574   distinct 2,000
  servers/4 ..... 3,169   distinct 1,999      servers/11 .... 2,519   distinct 2,000
  servers/5 ..... 3,335   distinct 1,996      servers/12 .... 2,404   distinct 2,000
  servers/6 ..... 2,842   distinct 2,000      servers/13 .... 1,235   distinct 1,068
  servers/7 ..... 5,885   distinct 2,000      priority .....   243   distinct 34
                                              remote .......    15   distinct 1
union of keyed slugs          25,069   (evening 24,830)
set diff vs 20261127_2100     +240 additions, -1 removal
added keys carrying lastmod   238 of 240
  identical stamp 00:14:03.895Z .. 229     newest added stamp 05:22:52Z (glideworth)
no lastmod on the addition     2  (remote-mcp-servers/clockwise; servers/doxtract-manoonlabs-com)
lastmod rows at/after 04:00Z   47 rows, 46 distinct keys, 3 new to the baseline
newest lastmod anywhere        2026-11-28T07:50:09Z
```

**The arithmetic of the shard is the finding.** Maps 1 to 12 are capped - each holds exactly **2,000** distinct keys except `servers/1` at **1,987** and `servers/4` at **1,999** - so all growth has to land in the newest shard, and it did: **+238 distinct keys in `servers/13`**. The union delta and the shard delta agree to within the two additions that arrived elsewhere (`remote-mcp-servers/clockwise` and the renamed doxtract slug), which is how a reader knows the wave is real rather than a re-shard of existing material.

**The stamps say the wave was written at a publish time, not at our read time.** Nine additions carry distinct stamps after the millisecond cluster - `01:13:03Z` (cellmath), `01:19:07Z` (fastqa), `01:33:42Z` (seniormode), `01:53:58Z` (arete), `02:33:27Z` (postkeep), `03:27:39Z` (acorn-scan), `04:28:07Z` (brickscape), `05:22:52Z` (glideworth) - and only **three** of the 240 are new to this baseline *and* stamped at or after the 04:00Z cutoff. So a detector keyed on the stamp window alone would have reported **three arrivals** against a directory that took **240**. This is the seventh distinct shape this surface has produced in nine passes: re-shard, restamp wave, stamped arrivals, duplicate wave, byte-stability, silent backfill, in-place pruning, and now a single-write bulk ingest with a shared millisecond.

**One addition is a rename, not a product.** `doc2json-manoonlabs-com` left and `doxtract-manoonlabs-com` arrived in the same window from the same publisher, so the net new products in the wave are **239**, and the rename is recorded rather than counted twice.

## The feed carried four cards and lost its stamp attribute

`mcp.so/feed` answered **200** at **158,024** bytes with **37** card anchors - **36** `/servers/`, **one** `/agents/`, no navigation links in the counted set - and the body text still reads *Submitted N hours ago*. The `title` attribute that carried a minute-resolution stamp at the evening read is **gone** from the anchors, so this pass ordered cards by position and by the relative text rather than by an absolute stamp, which is recorded because a reader keyed on that attribute would now silently match nothing.

| Card | Position | What it is | Disposition |
|---|---|---|---|
| `loop-voice` | 1 | Loop Voice AI phone agents, calls and texts | Held, vertical |
| `printpipe-io` | 2 | HTML to PDF and screenshots, templates, merges | Held, document conversion class |
| `tyrvar` | 3 | Security questionnaire answers from a trust profile | Held, GRC drafting class |
| `farmacia-premier` | 4 | Mexican online pharmacy, remote | Held, regional consumer vertical |

Below them the page repeats the evening's cards (`hypro`, `nutrinomist`, `corsair`, `my-job-fleet`, `winly-mcp`), then a stable block of framework servers (`playwright-mcp`, `figma-context-mcp`, `github-mcp-server`, `pixellab-mcp`, `next-devtools-mcp`, `blockbench-mcp-plugin`, `supabase-mcp`) that has not moved in days.

## The queue carried fourteen filings

`chatmcp/mcpso` issues **#8274** to **#8287**, newest filed **2026-11-28T09:31:17Z**, read with titles and bodies. The sequence is unbroken from #8273, which was the evening pass's top.

| Issue | Product | Disposition |
|---|---|---|
| #8274 | **Shellway** - remote computer use on your own Mac, Windows or Linux box, 22 tools, OAuth 2.1 with dynamic registration, free 50 actions a day then from $5/month | Held, agent-infrastructure class |
| #8275, #8276 | Yoya, Fecto (makloai) | Held, publisher pair |
| #8277 | **OpenBox China Futures & Options** - 33 read-only tools, IV, Black-76 greeks, GEX, member positions, static bearer token | Held, market-data class, account-gated |
| #8278 | Kingy AI Facts | Held, consumer |
| #8279, #8280, #8282 | **Yotta** Verify, Dev and Present - one publisher, three filings in twenty minutes | Held as a fleet, one line |
| #8281 | BTC.com Museum | Held, consumer curiosity |
| #8283 | Privara Unmask, Android malware sandbox recovering C2 | Held, security tooling |
| #8284 | **Asctrl** - Windows UI automation, 40 of 40 real tasks claimed, plan-level programs | Held, computer-use class |
| #8285, #8286 | **g-digital by Garrigues** EAD Enterprise Suite and GoCertius - signatures, evidence, dossiers, 19 environment variables | Held as a fleet, enterprise e-signature, partnership-gated |
| #8287 | **fatturapa-mcp** - Italian e-invoices, two tools, local stdio | **Catalogued** |

## Three guides

- [FatturaPA MCP - Italian E-Invoices Read Locally, Eight Calls Driven](/hermes/mcp/servers/external/fatturapa-mcp/) - **cloned, installed and driven, not quoted.** `initialize` **0.07 s** as `fatturapa-mcp` **1.0.0**, two tools, fourteen `tools/call` attempts against the author's ten fixtures. `S1` returned **1075 / 221.5 / 1296.5** with the VAT summary split at **10 percent on 125** and **22 percent on 950**; `S3` returned two invoices from one file labelled *fattura 1 di 2*; `S9` reproduced a professional's **20 percent** withholding (**200**), **4 percent** cassa (**40**) and **2** stamp duty into a total of **1320.8** and a payable of **1120.8**; the `.p7m` fixture parsed through its signature envelope and the ZIP through its archive; `S8` refused with the root element named (`Libro`). **The CSV formula-injection guard was tested rather than trusted:** a crafted `=HYPERLINK(...)` description came back as `"'=HYPERLINK(...)"`, apostrophe-prefixed inside a quoted cell. **Five defects:** `files` takes objects and a string array fails the validator with `-32602`; the MCP layer caps a file at **20 MB** while the shared core sets **50 MB** and **200 MB**; `npm audit` reports **zod < 4.6.6**, GHSA-mrhx-c7xc-m3w5, high; installation is a `git clone` because the package is not on npm; and the field names are Italian abbreviations (`ced`, `ces`, `imp`, `iva`, `tot`) which an English-speaking agent will either translate or paste raw. Also recorded: `pag.imp` equals total minus withholding and does **not** add the cassa on the author's own fixture - check it against a real invoice before treating it as the amount owed.
- [MailMergic MCP - PDF Mail Merge From a Chat, Ten Tools Behind OAuth](/hermes/mcp/servers/external/mailmergic-mcp/) - **the first mail-merge entry here, and the OAuth chain was walked end to end without an account.** `initialize` **401** with `resource_metadata` naming the RFC 9728 document, which answered **200** with four scopes (`templates:read`, `templates:write`, `merge`, `email:send`); the authorization-server metadata answered **200** with code-only, **S256**, refresh tokens and a registration endpoint; a **DCR POST answered 201** and issued a `client_id` anonymously; the authorize endpoint answered **200** as the sign-in page, which is the boundary - **the token needs a person.** Ten tools read from the vendor's public contract, and the permission split is the design worth copying: `preview_row` beside `start_merge`, and a connection granted `templates:read` without `merge` can look but cannot generate a thousand documents. Five limits recorded: **one credit per document and per test email**, no anonymous tier at all, **500 rows and 50 columns** for chat-typed data, **25 MB** uploads with a **30-minute** one-time upload page and **one-hour** download links, and column names travelling to the model as data.
- [Yellow Stake Agent Desk MCP - Can This Lead Be Called, and When](/hermes/mcp/servers/external/yellowstake-agent-desk-mcp/) - **the first surface here that answers may-I-call-this-person rather than who-is-this-person**, keyless at every layer, seven tools, fifteen calls driven. Florida rules returned **8 a.m. to 8 p.m.** with a **3 calls per person per 24 hours** cap and the FTSA citation; Texas returned **Sunday noon to 9 p.m.**; `check_calling_window` refused a Sunday **11:00 CST** call and opened at **1:00 PM**; `check_lead_data` called a `555-01xx` phone **"Likely returnable"** with a ready return request; `insurance_lead_cost` reproduced its own arithmetic exactly (**45 per lead, 35 percent contact, 8 percent close, 600 commission → 2.8 policies per 100 leads, 35.71 leads per policy, 1607.14 cost per policy, 16.8 break-even, -28.2 profit per lead**); `check_outreach_message` flagged a missing sender identification and a guaranteed-approval claim, and told an opt-out-less text to add one citing **FCC 26-67 from November 25, 2026**. **The defect is a contradiction inside one answer:** the enforced Florida gate opens at **9:00 a.m.** while the same response prints **8 a.m.** for weekdays, Saturday and Sunday - it reproduces at 8:00 and 8:59 and flips at 9:00, so the tool blocks an hour it says is legal and its own text is not evidence of its own behaviour. Two smaller ones: a Central-time panhandle ZIP prints one local time where an Eastern ZIP prints two, and `check_outreach_message` accepts only `text` (a `message` key returns *"Paste the message..."* as an error).

## Also identified this pass (not catalogued)

The **239 net arrivals** were cross-referenced against every sweep page, the catalog index and the four `.last-sweep` ledgers: **88 matched** already-dispositioned material or an on-disk guide, and **152 were unledgered**. The unledgered set was resolved through the official MCP registry where a record existed and probed where a remote was declared.

- **Resolved and probed keyless 200.** `drawsql.app/mcp` (1 tool, `visualize_schema`), `clearbounce.net/mcp` (**6** tools, email verification and find), `spamlyze.com/mcp` (**4** tools, quick and deep spam/deliverability reports with a balance), `mcp.sportsdatahq.com/mcp` (**4** router tools), `mcp.therundown.io/mcp` (sports odds and markets, many `v2*` tools, with a companion docs server at `docs.therundown.io/mcp`), `checkneatly.com/mcp` (**15** tools for billing disputes, deadlines and evidence), `watchfor.io/api/mcp` (**20+** monitoring tools with create/update/pause), `mcp.headlesslaw.com/mcp` (EU financial and digital regulation search), `mcp.shprd.us/mcp` (7 Bible tools), `cellmath.ai.studio/api/mcp` (memory vault), `listomancy.com/mcp` (4 list tools). Every one of these is **held with its class owner named**: email verification behind `how.is` and the mailers-scan trio; sports data as a vertical; billing disputes as consumer claims; monitoring behind **Cronitor, Runheed and uptrack**; regulation corpora behind **LegalCode and Patsnap**; memory behind the five agent-memory entries; developer schema tooling behind the diagram entries; consumer verticals otherwise.
- **Refused on a key.** `mcp.leadfeeder.com/mcp` **401** (visitor identification, OAuth - the biggest brand in the wave and still a documented-only tier tonight), `clerkfield.com/mcp` **401** with an API-key instruction, `acerdp.io/mcp` **401**, `www.calliopelabs.co/api/mcp` **401 `invalid_token`**, `mcp.feedbaky.com` **401** with an empty body, `boostmails.com/api/mcp` **401 `Missing or malformed bearer token`**, `groundbasecrm.com` **401 `UNAUTHORIZED`** at its API host, `api.openboxskill.cn/mcp` **401** in Chinese explaining that it uses a static bearer and offers no OAuth discovery, `mcp.getshellway.com/mcp` **401**, and `api.mailmergic.com/v1/mcp` **401** (catalogued at the documented tier above). `storek.io` publishes a wildcard remote `https://{workspace}.storek.io/mcp` that does not resolve as given, and `simplepost.social/mcp` answers a **308** to `/mcp/`.
- **Fleets, held as one line each under the standing one-tool-per-actor ruling.** `learnsomethingdaily` **ten** slugs of educational games, `metiutek` **three** media editors, `mambalabsdev` **five** (Europages suppliers, HubSpot/Salesforce partner directory, sanctions screening, SEC Form 4, Spain company directory - the sixth wave of that publisher), `apify-cliqtomedia` **five** marketplace scrapers, `z9systems` **two**, `bbscs` **two** China filings feeds, `g-digital-by-Garrigues` **two** at the queue.
- **Named holds worth a later pass.** `kkvlabs-ga4-gsc-mcp` is the only new slug in the wave aimed straight at this catalog's home turf - Google Analytics 4 plus Search Console behind a tool - and it is held on **access rather than merit**: the mcpservers.org detail page answered the standing **403** Cloudflare interstitial from this network, and no vendor documentation path resolved that names an MCP endpoint, so nothing was probed and no capability claim is written. `jeremy665/theseoagent-mcp` resolved to `io.github.jeremy665/theseoagent-mcp` **1.0.0** with **no remote declared**, on the SEO class that this catalog already carries twenty guides deep. `docs-simplepost-social-mcp` on social scheduling, `outreachtoday/mcp` on outreach, `neurlead-com-connect-docs` on the field-service CRM catalogued two passes ago, `open-patsnap-com` on the patent class, `mscode-pl/email-lint` and `mscode-pl/feed-lint` as developer linting, `nameocean`-class domain tooling, and the consumer remainder (`lyricsmove`, `nilyo`, `nano2image`, `iforgot-ai`, `simplemuscle`, `vitalitynode`, `taxhavenlist`, `whatsyourequity`, `travelino`, `carpool` variants) on verticals.

## Core listing check, measured rather than inherited

The fresh canonical still carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. `mcpservers.org` detail pages answered the standing **403** Cloudflare interstitial for every path tried this pass, which is their edge policy toward this network rather than a delisting, and `mcp.so` remains unlisted with the submission route unchanged. The upstream registry was used as the resolver for this pass and returned records for **20** of the 30 survivor terms queried, which is the mechanism that let nine unledgered slugs be probed instead of merely named.

## Counts

Canonical **25,069** against **24,830** with **240 additions and 1 removal**, 238 of the additions carrying lastmods and **229 sharing one millisecond**; `servers/13` distinct **830 → 1,068** while maps 1 to 12 held at their ceilings; mcp.so **37** card anchors at **158,024** bytes with the stamp attribute gone and **four** cards above the evening set; queue **14** filings, #8274 to #8287; **30** registry lookups resolving **20** names; **28** endpoint probes - **13** keyless 200 with a tools list, **10** auth refusals, **2** 404s, **1** 308, **1** HTML page and **1** unresolvable wildcard - plus three metadata documents and one dynamic client registration against MailMergic; **239** net new products cross-referenced with **152** unledgered; **3** servers catalogued and **3** guides; guide tree **1,303 → 1,306** directories and **1,455 → 1,458** entries; Markdown files **4,486 → 4,489**.
