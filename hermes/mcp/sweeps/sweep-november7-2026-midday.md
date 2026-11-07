---
title: "MCP Server Discovery - November 7, 2026 (Midday)"
description: "Forty sitemap additions six hours after a flat night pass, five fresh mcp.so cards and six queue arrivals, with one commercial property prospecting surface catalogued."
last_updated: 2026-11-07
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november7-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 7, 2026 (Midday)

## Summary

This pass fired on the **10:00 MST** tick, six hours after the night sweep that proved the canonical flat by arithmetic. The same surface moved this time: the twelve-sitemap universe went from **19,859** to **19,898** distinct server URLs, **40 additions and 1 removal**. The mcp.so homepage carried **5** cards strictly above the night stamp, and the submission queue added **6** numbers from `#6893` to `#6898`, every one an arrival.

**One server was catalogued.** It is the first entry here built around the commercial prospecting loop rather than the property record: find a commercial parcel, name the person behind the LLC, deliver a phone number and an email, then keep the deal in the same workspace.

## Sources Swept

| Surface | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 12 server maps (`servers/1` to `servers/10`, `priority-servers`, `remote-mcp-servers`) fetched fresh with plain urllib, inline locale prefixes stripped, `/servers/` subset only | **63,231** raw `<loc>` entries, **19,898** distinct server URLs against **19,859** at the 03:00 capture: **40 additions, 1 removal** |
| mcpservers.org `/all` and detail pages | direct fetch with a browser user agent, then the r.jina.ai reader proxy | **403** direct and **401 03** bad IP reputation through the proxy, the standing condition since November 4, so no detail page could be read |
| mcp.so homepage | direct fetch with a browser user agent, gzip decoded, TanStack payload parsed on `slug` / `tagline` / `authType` / `createdAt` | **188** `createdAt` occurrences in the document, **148** cards parsed, newest `2026-11-07T16:50:15.825Z` (Fulfy Plus); **5** cards strictly above the night stamp and **1** at it |
| chatmcp/mcpso submission queue | authenticated `gh api`, bodies included in one call | **6** arrivals from `#6893` MakeMidas to `#6898` GhosterMail, none a listing update |
| official MCP registry | `registry.modelcontextprotocol.io/v0/servers?search=` per candidate | **37** survivors searched, **22** returned a name-and-description match, and **6** of those matches were wrong-product matches caught by reading the description rather than the name |

## Catalogued

- [West Kite MCP - Owner Tracing for Commercial Property](/hermes/mcp/servers/external/west-kite-mcp/) - remote Streamable HTTP at `https://app.westkite.com/mcp`, OAuth with no API key, and the tier is documented from the server's own contract because the surface is account gated. A keyless `initialize` returns **401** `{"error":"Connect your West Kite account.","code":"SIGN_IN_REQUIRED"}` with `WWW-Authenticate` naming `https://app.westkite.com/.well-known/oauth-protected-resource/mcp` and a ten-scope list that separates reads from writes (`wk:data:read`, `wk:research:read`, `wk:documents:read`, `wk:assets:read`, `wk:conversations:read`, `wk:saved:read`, then `wk:saved:write`, `wk:research:write`, `wk:documents:write`, `wk:actions:write`). That protected-resource document answers **200** naming the resource, the authorization server on the same host, the bearer-in-header method, **15** declared scopes including `profile` and `email`, and its own setup documentation URL. **The data claim is the entry:** **107 million** US parcels across **1,787** counties in **27** states and Washington DC, stated by the vendor to include all of California, Florida and Nevada, with owner tracing from the LLC to the people behind it, then a phone number and an email. The filters are the ones that decide a commercial deal (type, size, sale date, value, owner, permits, zoning, flood risk), the off-market angles are the ones that produce a conversation (long-held buildings, underbuilt lots, recent permits), and the export returns a full result set as one file with an exact total and its sources. **The session model is why it earns the guide rather than a hold:** the agent drafts, the person sends outreach from West Kite, and every change waits on a review link the person approves, valid **15 minutes**, so nothing leaves the building on the agent's authority. No published tool inventory, which is recorded as a limit rather than guessed at, and **60 requests per minute** per account. **$149** a month, one plan, **7-day** trial with **150** tokens and no card, **1,500** tokens a month for new contact details and mail (email **5**, phone **10**, postcard **50**, handwritten letter **75**, a lookup that finds nothing costs **0**), extra tokens **$0.10**, no rollover, nothing charged when the trial ends.

**Why it is not a duplicate.** The real estate shelf has an owner for management ([Hercules Property](/hermes/mcp/servers/external/hercules-property-mcp/), Dutch Property Context, AskRent, LucidRents) and an owner for parcel research ([DFX Intelligence](/hermes/mcp/servers/external/dfx-intelligence-mcp/), [dfx-real-estate](/hermes/mcp/servers/external/dfx-real-estate-mcp/), Homedex UK), and BatchData was held earlier on the same shelf as a property and skip-tracing entry. None of them trace an owner to a person, deliver a contact, and keep the deal in the same record. West Kite is the prospecting loop, not the record.

## Held, with the class owner named

**From the 40 sitemap additions.** Three were prior dispositions found on a compact token and confirmed by context, not by substring: `itulo/eu-nordic-open-data-mcp` on the Apify actor distribution hold recorded against `#6236` in the October 27 sweep; `tankucukhas/spacepal-mcp` on the macOS Spaces consumer hold recorded in the November 6 night pass; `patentref-mcp` on the patent and IP class carried by Patsnap and LegalCode, held in the November 6 midday pass, re-confirmed here on the sitemap rather than the card. The remaining **36** were read against the catalogue and the ledgers:

- `quotedpart-com-capabilities-mcp-server` on the manufacturing quoting class (CNC Compass, MechanoFab, Cutting Tools AI), already held as `#6828`.
- `jobpostingsapi-com-mcp` on the jobs-data class: OpenHire, Jobyap, Magnificent Jobs, Headcount Labs and the Hilead hiring-signal entry.
- `checkdomainrating-com-en-domain-rating-mcp-server` on the SEO class, which carries twenty guides and already held GoAnyAPI on the same job.
- `fanduelapi-com-docs` on the consumer gambling class (BetBank, Fast Props API, robopunter).
- `esimx-com/esimx-mcp` on the travel eSIM class (PuraSIM, SecondSim, shibaSIM).
- `agentscpa-com-docs` on the affiliate program operations class (Cello, GrowSurf, Ambassly, LinkJolt).
- `theopenapps-com` on the app store analytics class (Sonar ASO, AppSigma, PastCharts, StorePilot).
- `thenetworkery-com-docs-mcp` on the DNS and email-auth diagnostics class (TamingDNS, Highwire).
- `cgbb-org-ai-trust` on the trust and verification class (TrustScan, AgentTrust, the Agent Verification API): the vendor is a standards council rating corporate trust, which is the same surface with a different output.
- `mail-cuck-com-en` on the email class beside the MailTester trio and InboxSim.
- `glpcompare-co-partners` on the healthcare vertical, recording its evidence so a later pass can promote it without re-probing: **`https://glpcompare.co/api/mcp` answered a keyless `initialize` 200** as `glpcompare` **1.0.0** with **3** tools (`find_glp1_prices`, `find_seller_glp1_prices`, `list_glp1_medications`), instructions that demand the check date and the page link on every price, and US self-pay GLP-1 prices sourced from sellers plus CMS NADAC.
- `augur-trade-com-foresight` on the trading signals class inside the saturated stock-research group (fAlpha, BDE, Altair, ValuEdge holds).
- `pandadad0214/panda-leads-tools`, `panda-public-funding-tools`, `panda-research-tools` and `panda-web-security-tools` as one single-author fleet of four packs on carried classes (leads and enrichment, government funding, research, OSINT), none of them holding an official registry entry under any Panda name, and the registry hits returned for them were other vendors matched on a shared token.
- `greatpyrenesedad/bullpen-mcp` as an AI phone sales service that signs agents up by paying (MPP), on the sales-outreach class.
- `cigo240920/cigo-aircare-connector` as a single-vendor Korean B2B cabin-filter catalogue, industrial supply rather than a data surface.
- `heystacks-com-for-agents` on the document and table class (DocsAutomator and neighbours).
- `runlater-app-docs-mcp` and `radishsoftware/mobster` as agent infrastructure rather than business data: scheduled HTTP calls with retries, and iOS device control that needs macOS and `uv`.
- `docs-strg-com` as S3-compatible object storage management, infrastructure.
- `www-threadcamp-com` as an email API for agents (programmatic inboxes, Resend-compatible sending), the email class again.
- `www-arca-inc-research` as a Tokyo web design agency, outside operator scope and evidently not the research surface its slug implies.
- `stayotter-com-connect` on the travel vertical, `readlink-app-connectors` on a consumer book library, `yourmelody-ai-mcp` as song gifts, `pikah3-com` and `photoanimate-org` on media generation, `postersize-org` and `www-scidrawer-com` as consumer print and drawing utilities, `fireflywedding-org` as a wedding vertical, `www-azyun-com` as an API gateway page with the title `New API` and nothing to read, and `sohan-bhat/openhal` plus `agentjournal-dev-discli` left unjudged because neither slug resolved in the registry and no detail page could be read.

**From the 5 fresh mcp.so cards.** `quickbooks-bridge` on the accounting connector class (Caribooks, the QuickBooks and datagrout entries, Superbooks, Fortnox, Xero), `anymail-finder` on the B2B email find and verify class (Hilead, MailTester trio), `hunter-killer` as crypto liquidation data, `ohmybug` as developer tooling outside operator scope, `smoover-moving-cost-calculator` as a regional moving quote, and `fulfy-plus` as Venezuelan carrier rate comparison, a regional logistics source.

**From the 6 queue arrivals.** `#6893` **MakeMidas** on the media generation aggregator class (Varosity, Superpowers, Wiro AI); `#6894` **PuntersEdge** on the same consumer gambling class as the FanDuel API card, Australian and New Zealand racing odds; `#6895` **juris-licita-mcp** as a regional legal and procurement vertical, its BR specific court-calendar arithmetic sitting beside the tender class already carried by Otnox, Qlows, the TED monitor, UK Tenders and Texas ESBD, and beside the regional legal trio held in October; `#6896` **Agentic Kingdoms** as a consumer strategy game; `#6897` **Fezola** on the email class as a multi-provider inbox reader that never sends; `#6898` **GhosterMail** on agent email, saturated since the Voidmail precedent.

## Probes

| Endpoint | Result |
| --- | --- |
| `https://app.westkite.com/mcp` | **401** `SIGN_IN_REQUIRED` with `WWW-Authenticate` naming its protected-resource document and a ten-scope list |
| `https://app.westkite.com/.well-known/oauth-protected-resource/mcp` | **200**, resource, authorization server, **15** scopes, bearer method, documentation URL |
| `https://glpcompare.co/api/mcp` | keyless `initialize` **200** as `glpcompare` **1.0.0**, `tools/list` **3** tools |
| `https://makemidas.com/api/mcp` | **401** |
| `https://api.ghostermail.com/mcp` | **401** |
| `https://glpcompare.co/mcp` | **404**, the detail route differs from the API route |

## Core listing check, measured rather than inherited

The fresh canonical carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. The mcpservers.org detail page answers **403** to an anonymous fetch, which is their edge policy and not a delisting. Glama answers **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`, and a connectors search for the name returns the same handle plus its tool fragment. All four direct mcp.so slugs still answer **404**, so the listing there remains absent. The smithery registry API answered an error payload twice rather than a result set, so this pass records no smithery state rather than an inferred one.

## Count

The guide tree held **1,112** directories before this pass and holds **1,113** after it, **1,255** entries counting single-file guides before and **1,256** after. One server catalogued, one guide written, no resubmissions, and no corrections to prior entries.
