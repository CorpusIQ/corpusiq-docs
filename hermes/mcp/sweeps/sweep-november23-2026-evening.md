---
title: "MCP Server Discovery - November 23, 2026 (Evening)"
description: "A ten-minute 282-key ingestion wave, and four products: SEO data by the keyword, competitor ads by the ad, leads with no phone numbers, a connect gate to copy."
category: "MCP Ecosystem"
last_updated: "2026-11-23"
---

# MCP Server Discovery - November 23, 2026 (Evening)

Fired on the **21:00 MST** tick, eleven hours after the midday supplement and seventeen hours after the night pass. The directory did not trickle: `servers/12` took the entire wave, moving **2,031** to **2,356** raw entries, and all **282** new keys carry a stamp inside a **ten-minute** window, which is an ingestion batch rather than a morning of launches. The wave decomposed to four products worth a guide, and the best thing found this pass is not a data source at all but a refusal.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          37,769   against 37,535 at the 11:00 MST supplement capture  (+234)
  servers/1  ..... 4,171     servers/7  ..... 5,864
  servers/2  ..... 2,516     servers/8  ..... 2,739
  servers/3  ..... 2,936     servers/9  ..... 2,634
  servers/4  ..... 3,221     servers/10 ..... 2,575
  servers/5  ..... 3,327     servers/11 ..... 2,524
  servers/6  ..... 2,906     servers/12 ..... 2,356     sum 37,769 exact
distinct keys, maps 1-12      23,894   against 23,612 at 1.58 URLs per key  (+282)
union with priority           23,928   against 23,647
priority-servers.xml          252 raw, 34 distinct keys
remote-mcp-servers.xml         15 raw, 1 distinct key
baseline (04:31Z Nov 23)      23,646 keys -> +282 additions, 0 removals
lastmod, server maps          34,273 stamped pairs; 1,882 rows at or after 07:04:41Z, 1,297 keys
mcp.so /feed                  200, 159,603 bytes, 30 cards, 30 stamps, 12 above the cutoff
```

The raw count rose **234** while the key set rose **282**, which is the opposite of the usual re-shard signature and is the arithmetic of an arrival: new keys that bring their own locale forms instead of consuming existing slots. The additions are not spread across the day. Every one of the 282 keys carries a `lastmod` between **2026-11-24T00:16:53.347Z** and **00:27:03Z** - a **ten-minute** publish at 17:16 to 17:27 MST, inside a seventeen-hour window. The **1,882** stamped rows at or after the cutoff collapse to **1,297** keys because most of that number is re-stamping of pages already held, not arrival; the arrival test is the set difference, and the stamp window is what dates it.

The feed's markup changed under this pass, and the change is recorded rather than worked around: `mcp.so/feed` still answers **200** at **159,603** bytes, but it renders as a React shell whose cards carry no `/server/` hrefs in the served HTML. The card text, author and stamp are present and were read from the markup, **30** cards with **30** stamps and **12** above the cutoff.

## What the 282 are

A wave this size is not 282 products, and the decomposition is the honest count: **140** plain product slugs, **66** namespaced `owner/repo` slugs, **58** documentation or marketing mirrors (`-docs`, `-help`, `-agents`, `-developers`, `-connect`, `-integrations` forms), **12** sub-servers of one public-records repository tree, and **6** Apify actors. Two fleets inside the 66 namespaced slugs are re-entries rather than arrivals: the four `steadyscrape/*` products were new, but `abigaildavised/*` returned six products dispositioned on 2026-11-22 night under namespace forms, and `devart` filled **31** slugs across `www-devart-com-mcp-*` and `www-nuget-org-packages-devart-mcp-*` for one vendor's connector catalogue.

## Shipped (4, all driven)

- [SteadyScrape SEO Data MCP - SEO Priced Per Keyword](/hermes/mcp/servers/external/steadyscrape-seo-mcp/) - a canonical arrival, and the cleanest split of free and paid in this catalogue. `initialize` and `tools/list` answer **200** keyless as `steadyscrape-seo-data` **0.2.0** with **nine** read-only tools; every `tools/call` refuses in band with `-32001 "Sign in with Apify to use this tool."` The discovery chain is complete: a protected-resource document naming `https://console-backend.apify.com` with the single scope **`full_api_access`**, and an RFC 8414 document with authorization code, refresh and device grants plus PKCE **S256**. The published rate card is the story: **$0.039 per 10 keywords with data**, **$0.006 per 10 results of depth**, **$0.111 per 10 domains** for traffic, **$0.082 per call** for backlinks, a **$0.005** session fee on the first paying call, and a free-plan ceiling of about **$0.25 per UTC day**. Two procurement facts recorded: the SEO data is **DataForSEO under licence**, so a team already holding a DataForSEO contract pays twice, and `full_api_access` is the buyer's whole Apify account, not an SEO scope.
- [SteadyScrape Ads Intel MCP - Competitor Ad Libraries](/hermes/mcp/servers/external/steadyscrape-ads-intel-mcp/) - the same gate, four tools over public ad libraries: **$0.003** per advertiser account, **$0.001** per Google ad, **$0.0008** per TikTok ad from Creative Center, `get_results` free. Caps of **40 ads per target**, **3 targets**, **5 names**, **50 TikTok ads** and **60 calls a minute** make a three-competitor pull **$0.12**. The boundary is stated by the vendor and repeated in the guide: reads public libraries only, no spend, impressions, targeting or conversions, so nobody should budget a competitor's media spend from ad counts without saying so.
- [SteadyScrape Local Leads MCP - Businesses With No Site](/hermes/mcp/servers/external/steadyscrape-local-leads-mcp/) - the operator entry of the three. `find_local_businesses` carries **seventeen** parameters and the filters are the product (`website`, `unclaimed_only`, `rating_below`, `min_rating`, `reviews_below`, `min_reviews`, `first_seen_within_days`), priced at **$0.015 per run + $0.002 per business**, **$0.005** when a filter is used. The privacy contract is explicit and unusual: **no phone numbers**, free-text descriptions removed, **reviewer names masked inside review text**, avatars and photos never returned. Worked to a number: **500 filtered no-website businesses** in ten calls is **$2.65**, and three competitor review summaries at 200 reviews each is **$0.405**.
- [BoxTrack MCP - Home Inventory From Photos](/hermes/mcp/servers/external/boxtrack-mcp/) - a feed card, and the only one of the four with a fully driveable surface. **Seven** tools as `boxtrack` **1.0.0**: two keyless and five requiring a connected account. `show_home_inventory` returned **5 entries (135 things) in 2 places, about $4,052 to replace** across two rooms, and every figure reproduces by hand (1,400 + 1,300 + 120 x 8 = 3,660; 12 x 6 + 320 = 392; total 4,052), with `value` a **per-unit** price times `quantity`. The account tools answer **HTTP 200** with `isError: true`, a `structuredContent` carrying `view: connect` and the signup and app links, and a spec-shaped **`mcp/www_authenticate`** hint in `_meta` naming `insufficient_scope` and the protected-resource document - and the payload is **seasonally personalised** with a holiday-inventory line. Both shapes ship an MCP Apps template (`ui://widget/boxtrack-inventory-v1.html`). The protected-resource document offers one scope, `email`, so identity is the token and the connection is the boundary.

## Also identified this pass (not catalogued)

**Held with the gate or class named.** The closest miss is **wecantrack** at `https://app.wecantrack.com/mcp`, read-only affiliate earnings, sales, clicks, EPC and ad profitability across 450+ networks behind a bare **401 `{"message":"Unauthenticated."}`** with no `WWW-Authenticate` and no protected-resource document - a real operator product with no published contract, so nothing to certify beyond the refusal. **SocialDesk** (`https://app.socialdesk.ai/api/mcp`) answers **401 `invalid_token`, "No authorization provided"** under the same bare shape, on the saturated social publishing class. **Aakaar MCP**, an Amazon seller surface, answers **405 Not Allowed** from nginx to a JSON-RPC POST at both `aakaarai.com/mcp` and `mcp.aakaarai.com/mcp`, recorded as an infrastructure refusal rather than a product. **AI Twin** (`https://ai-twin.app/mcp`) answers **401 `{"error":"invalid_token"}`** with no challenge, held on the agent-memory class. **FormKiQ** and **TestingBot** ship local endpoints (`http://localhost:8000/mcp` and an npm package) and cannot be driven from here; both are recorded as self-hosted with their documentation links. **Foreclosure Data Hub** needs an eligible key before it will describe coverage, held on the real-estate class carried by West Kite, Hercules and BatchData.

**Fleets and re-entries.** The **12** `github-com-geminigeorge22-publicrecords-mcp-tree-main-servers-*` slugs are one repository's sub-servers (Ashby, Greenhouse, Lever, SmartRecruiters jobs; grants.gov; USAspending; EU TED and UK tenders; Legistar; Skool) held as a single public-records fleet on the jobs and procurement classes already carried. The **31** `devart` slugs are one vendor's database and CRM connectors, held as one catalogue. The six `abigaildavised/*` slugs are the 2026-11-22 night fleet under namespace forms. The six `apify-com-*` slugs (four ATS job monitors, a redirect checker and a Telegram channel scraper) sit on the standing Apify transport hold.

**Product slugs held on class.** `mofcloud-com-mcp` on the already-saturated GPU-pricing class carried by CoreHu, OpenCloudCosts, Costory and GPUFinder; `conquerorapp-com` on the SEO toolset class it was held on at 03:00; `agitech-group-site-check` on the third-party copy of this catalogue's own SEO surface, held at midday and re-entering under a canonical slug; `countvisits-com` on the web-analytics class; `wecantrack-com-mcp` in the affiliate-attribution lane this catalogue has no entry for yet, which is the one to revisit if the vendor publishes a protected-resource document; `saasemailer-com` and `emailforagents-ai` on the email-marketing and agent-email classes; `socialdesk-ai/mcp-server` on social publishing beside 40 prior holds; `onlypult-com-dev-mcp-html`, `jsximage` and `aih3image-com` on media generation; `medce-hub-cme-conferences` as a medical-education vertical; `ferrazmichel/us-gov-mcp-suite`, `foreclosuredatahub` and `equitylayer/obolos-equity` on public-records and finance data; and the long consumer tail (`1000xleverage-com`, `giftablesong-com`, `trackvacations-com`, `velvetcompanionai-com`, `musikalis-com-mcp`, `epubtranslator-com`, `caesarcipher-org` and the rest) named in the wave list rather than catalogued.

**From the feed, above the cutoff (12 cards).** **AU Agent Tools** (**11/24 00:20Z**, pay-per-use PDF and DOCX to Markdown, screenshots, G-NAF geocoder, AU and NZ public holidays, phone validation through Apify) on the Apify transport hold; **Aakaar MCP** on the 405 above; **AI Twin** on the memory class; **JSXImage** on media generation; **MedCE Hub** on the medical-education vertical; **Scrumpy**, **CartAI** and **OnlyDNS** were dispositioned at midday and stand; **Koop** and **Patchwell** were catalogued on 2026-11-23; **Avanciq** was catalogued at 03:00; **Pagesmith AI** answered 404 at `/mcp` and 401 at the bare host at 08:58Z and stands held.

## Listings

Our own presence was re-measured inside this capture: `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs` are both present in the canonical, so mcpservers.org remains **LISTED** on both of our surfaces. This pass did not re-read `/all`, which has answered **403** by edge policy since 4 November, and it did not re-measure Glama, Smithery or the official registry; the midday pass measured those and its states stand.

### Why ship four of 282?

Because a slug is not a product and a wave is not a launch. Two thirds of this batch is mirrors, fleets and re-entries, and of the 140 plain product slugs a large share are single-vendor consumer surfaces. The four that shipped are the ones with a public contract: a readable schema, a stated price and a gate whose shape can be quoted. The rest are named so that their absence from a heading reads as a disposition rather than as a fresh find.

### What did this pass not do?

It did not execute a single paid call. Every SteadyScrape figure in the guides is the vendor's own published rate card, because the gate sits at the paying step by design; BoxTrack's arithmetic is the only executed number in the pass. It also did not re-read `/all`, and it did not dispute the twelve feed cards that were already dispositioned earlier in the day.
