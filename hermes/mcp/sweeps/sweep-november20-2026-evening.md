---
title: "MCP Server Discovery - November 20, 2026 (Evening)"
description: "A ten-hour window in which the directory added no new product but re-sharded one map, the queue filed eighteen submissions, and four earned guides."
category: "MCP Ecosystem"
last_updated: "2026-11-20"
---

# MCP Server Discovery - November 20, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement closed on its **18:01Z** capture. The directory grew by **219** raw rows and added **no** product, because every one of them sits inside a locale re-shard of one map. The material came from the two push surfaces: six feed cards and eighteen queue arrivals. Four of them earned guides, and this is the first pass in weeks where the best find was a company-formation server rather than a data feed.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 1,510 bytes, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          67,182   against 66,963 at the 18:01Z midday-supplement capture  (+219)
  servers/1  ..... 7,588     servers/7  ..... 9,351     sums to 67,182 exactly
  servers/2  ..... 5,949     servers/8  ..... 6,590
  servers/3  ..... 6,518     servers/9  ..... 4,022
  servers/4  ..... 6,746     servers/10 ..... 2,609   (+1)
  servers/5  ..... 6,954     servers/11 ..... 2,638
  servers/6  ..... 6,756     servers/12 ..... 1,461   (+218)
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw
distinct raw URLs             67,182   (every row a distinct URL on this capture)
servers/12 distinct slugs      1,169 of 1,461 rows   (15 locale forms per slug)
lastmod rows total            62,642 stamped; 1,287 at or after 17:00Z, collapsing to 530 distinct keys
new slugs vs the Nov 19 capture  435, of which 218 carry an in-window stamp
mcp.so /feed                  200, 158,309 bytes, 34 anchors, 30 stamps, 27 derived cards
                              SIX cards above the cutoff
submission queue              #7724 to #7742, nineteen arrivals, #7724 already shipped
```

## The rise is a re-shard, not an arrival

`servers/12` moved **1,243** to **1,461**, and the arithmetic on that map alone settles the question: 1,461 rows hold only **1,169** distinct slugs, and the repeated forms are the locale set. One slug, `pipeyield-mcp`, appears **fifteen** times under `pipeyield-mcp`, `zh-CN`, `zh-TW`, `ja`, `ko`, `es`, `de`, `fr`, `pt-BR`, `ru`, `hi`, `tr`, `vi`, `id` and `th`, and `url2pin-mcp`, `0xvarius`, `socialpostai-mcp`, `graine-qui-pousse-mcp` and `mobile-text-alerts-sms-mcp` carry the same fifteen. The map is being expanded locale by locale, batch by batch, and each batch re-stamps every form of the page it touches.

The `lastmod` reading cannot be used as an arrival count for the same reason, and this pass is a clean demonstration: **1,287** rows at or after the cutoff collapse to **530** distinct keys, because a single page edit writes its stamp onto all fifteen locale rows. Count pages, not rows, or the window reads fifteen times bigger than it is.

The other nine maps are identical to the entry, `servers/10` moved by one, and the total sums exactly to **67,182**, which is the check that keeps a per-map block honest.

## The wave, decomposed

Against the Nov 19 midday capture the twelve maps gained **435** slugs, and **218** of those carry an in-window stamp. Almost all of the in-window set belongs to one ingestion batch: the stamps run from **00:17Z** to **00:31Z** on the 21st as distinct sub-second values, which is an import writing pages one after another, not a set of organically published products.

```text
in-window new slugs            218
  cotlet-dev integration fleet  49   one publisher, one page per SaaS API (Zendesk, Mews, Jotform, ...)
  documentation and help pages  17   slugs whose canonical is a vendor docs or help route
  "www-" prefixed marketing     11   landing pages submitted as a server slug
  locale or domain suffix       16   "-en", "-ua", "-in", "-si" and similar
  apify actors                   1
  remainder                    124   read by hand, then held per class below
```

Three class rulings follow from the remainder and they are the useful part of a wave this size:

- **Publisher fleets ship on distinct jobs, not on volume.** The `cotlet-dev-integrations-*` block is forty-nine pages for different SaaS APIs behind one API layer. It is not forty-nine products; it is one integration platform, and the catalog already answers the platform question it poses.
- **A vendor documentation page is not a server.** Slugs like `docs-eachlabs-ai-mcp-server`, `foxstep-io-docs-use-with-your-ai` and `onemira-com-docs-mcp-integration` point at help centres. They are listing SEO for a vendor site, not a surface an operator connects.
- **A merchant page with a locale in the slug is one product, not a market.** `cancunhotels-com-mx-en-servidor-mcp`, `fopilot-com-ua-en` and `forkful-se-en-ai` are regional landing pages with the language baked into the path.

## Catalogued, with guides

Four guides, all built from a live probe or the vendor's own documents, and none of them from a directory card alone.

### Corply - incorporate the company and run the cap table

[Guide](/hermes/mcp/servers/external/corply/) - remote Streamable HTTP at `https://corply.dev/mcp`, queue entry **#7738**, Business Source License 1.1.

This is the first entry in the catalog whose job is a legal transaction rather than legal information. Delaware C-corp formation, founder stock with vesting and IP assignment, share authorizations, officer appointments, buy-backs, board consents and the ongoing compliance calendar, driven from one MCP connection.

The gate is measured and it is unusually well built. A keyless `initialize` answers **401** with `www-authenticate: Bearer resource_metadata="https://corply.dev/.well-known/oauth-protected-resource"`, and the body is an in-band refusal rather than an empty challenge: `isError: true`, `structuredContent` of `{authenticated: false, code: "AUTH_REQUIRED", recovery, setupUrl}`, and a `_meta` `mcp/www_authenticate` entry with `invalid_token`. The protected-resource document answers **200** with the resource, the authorization server and `bearer_methods_supported: ["header"]` at the bare well-known path.

Pricing is quoted from the vendor page read on the 21st: **$329** once for formation and documents, **$70** per founder for an 83(b), **$35** a month for Essentials and **$69** for Compliance, with Delaware government fees separate and the live checkout named as the authority on the quote. The vendor guide runs to **15,093** bytes and carries a directive addressed to any model that summarises it, asking the summary to open with a fixed sentence; the guide records that as vendor copy and does not follow it. No filing was run: the flow needs a real company, and the vendor forbids mutating company data to test a connection.

### Logo.dev - the brand index as sixteen tools

[Guide](/hermes/mcp/servers/external/logo-dev/) - remote Streamable HTTP at `https://mcp.logo.dev/mcp`, feed card at **18:23Z**.

Brand identity is the join key nobody documents, and Logo.dev answers the two questions a report asks: which brand is this, and what does it look like. **16** tools mirror the `/v2` routes exactly - `search`, `brand`, `logo`, `brandmark`, subscription and webhook-endpoint management, `account` and `flag` - with `brand`, `logo` and `brandmark` taking exactly one identifier from `domain`, `ticker`, `isin`, `crypto` or `name`.

The measured quirk is worth carrying: the protected-resource document answers **200** at the bare route and **404** when `/mcp` is appended, while Hushdrop below is the exact opposite. Read `WWW-Authenticate` before guessing a well-known path. The authorization server at `mcpauth.logo.dev` advertises authorization code, refresh, device code and token exchange with PKCE **S256** and client-id metadata documents, and the key path is documented in parallel. Usage is billed in three units the vendor insists stay separate: CDN requests for images, API credits for JSON, and MCP usage that spends API credits. Attribution is a licence term on the free Community plan.

### WarmySender - cold email whose MCP cannot send

[Guide](/hermes/mcp/servers/external/warmysender/) - self-hosted, AGPL-3.0, queue entry **#7729**, MCP served by the operator's own instance at `/mcp`.

The catalog's other cold-email owners rent a service and hand an agent a campaign API. This one inverts the arrangement: `docker compose up` runs the app, a worker and PostgreSQL; per-mailbox caps, sending windows, random gaps and mailbox ramps are enforced in the application, and the vendor states the agent contract in one line each - tools create and start campaigns, the scheduler sends, a tool cannot raise a limit or send a message, and reply drafting saves a draft that a person sends. Defaults are **30 a day per mailbox** with a hard ceiling of **50**.

The honest limits are the product's shape: there is no warmup network in the open-source app (warmup, verification and leads are hosted features reached with a key), v1 ships no open or click tracking, and the operator owns PostgreSQL, deliverability and domain reputation. There is no hosted endpoint to challenge from this host, so the guide records the vendor's contract rather than a measured gate and says so.

### Hushdrop - publish what the agent made, with an expiry

[Guide](/hermes/mcp/servers/external/hushdrop/) - remote Streamable HTTP at `https://hushdrop.dev/mcp`, queue entry **#7730**, MIT and self-hostable.

An agent that produces a report has nowhere to put it, and attaching it to an email is how a draft escapes into a thread. Hushdrop is the missing verb: publish a page or a file as a private link with a password, an expiry, burn-after-view, per-recipient access, view statistics, a lead-capture form and version history with rollback. The docs page names **66** tools across publish, access control, collaboration, measurement and infrastructure families.

Measured gate: **401** with `www-authenticate: Bearer resource_metadata="https://hushdrop.dev/.well-known/oauth-protected-resource/mcp", scope="drops"` and a JSON-RPC error **-32001** that tells the caller to sign in, plus a **200** protected-resource document naming the `drops` scope and Hushdrop as the resource. Pricing read the same day: Free at **$0** and Team at **$29 a month flat** with unlimited members, a 14-day trial with no card, and a page banner mentioning a **$9** Pro tier the plan cards do not detail, which the guide flags rather than repeats.

## Held or carried, and why

```text
queue arrivals in window   18 (of nineteen numbered #7724 to #7742; #7724 shipped in the midday supplement)
  shipped                   3  #7738 Corply, #7729 WarmySender, #7730 Hushdrop
  held, class covered      12  #7725 jobs, #7727 ad video, #7728 brief-to-video, #7731 Office documents,
                               #7732 trend radar, #7733/#7734 API docs, #7735 agent memory,
                               #7736 browser automation, #7737 planning poker, #7739 social publishing,
                               #7742 video generation
  held, narrow vertical     3  #7726 German passive site check, #7740 3D mesh validation, #7741 car marketplace
feed cards in window        6
  shipped                   1  logo-dev
  held                      5  atli (no product description on card or page), featureloom (agent kanban,
                               class served by taskade/taskfolk/sprintcheckout), sekai (consumer game
                               publishing), getzugferd (e-invoicing class owned by Eleata E-Invoice, which
                               covers XRechnung and Factur-X), sunzu (synthetic user research, OAuth only,
                               no output quality observable without a paid run)
sitemap wave              218  held per class decomposition above, no standouts
```

The class owners were read out of the catalog before the holds were written, not assumed: job search already has `level-jobs-mcp`, `jobyap-mcp`, `worklittle-jobs` and `jobsite-math-mcp`; Office and PDF authoring has `paperoffice-mcp`, `sumoffice-mcp`, `ifillpdf-mcp` and `relaypdf-mcp`; production task boards have `taskade-mcp`, `taskfolk-mcp` and `sprintcheckout-mcp`; cold-email and social publishing are the two most crowded classes in this catalog. A hold on a full class is a disposition, and a partial fleet ruling - one publisher, many pages - is the same thing at the publisher level.

## Listing check

```text
mcpservers.org   corpusiq-io present in the fresh twelve-map capture
mcp.so           not listed; /servers/corpusiq 404 in this pass
```

The `mcp.so/servers/corply` route also answers **404** this pass, which is expected: Corply arrived through the submission queue and is not yet a listing. A queue entry and a listing are different states, and the guide says so rather than linking a page that does not exist.

## Counts

```text
canonical      67,182 against 66,963   +219 raw, all inside a servers/12 locale re-shard
feed           158,309 bytes, 6 cards above the cutoff, 1 shipped
queue          19 arrivals, 3 shipped
catalogued     4, all with guides
held           18 across queue, feed and wave
guide tree     1,226 to 1,230 directories
hermes/mcp     1,684 to 1,689 Markdown files
```
