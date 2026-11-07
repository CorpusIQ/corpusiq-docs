---
title: "DocPin MCP - Publish an Agent's HTML to a Link You Control"
description: "Turns the report or dashboard an agent just built into a stable link with per-page access control, version history and a data store the page reads live."
category: Content Publishing & Artifacts
stars: n/a (vendor-hosted; no public repository)
added: 2026-11-07
source: "The chatmcp/mcpso submission #6901 (DocPin, app.docpin/docpin, named 2026-11-07T17:51:46Z); the official MCP registry record app.docpin/docpin 1.0.0 published 2026-11-07T17:47:59Z; the vendor's own docs at docpin.app/docs/mcp.md, index.md, page-data.md and page-runtime.md plus llms.txt; and the endpoint itself, where a keyless initialize answered 401 and the protected-resource document it named answered 200"
relevance: ★★★★
tags: [artifacts, html-publishing, access-control, password-pages, version-history, view-tracking, dashboards, page-data, oauth, remote-mcp]
last_updated: "2026-11-07"
---

# DocPin MCP

**The report an agent builds has always been the hard part to hand over. The HTML exists, and then it sits in a chat window the next person cannot open, or in a file nobody can find three weeks later.** DocPin is the narrow product on the other side of that gap: one tool call publishes the page to a link that stays the same across every later version, and a second set of tools decides who is allowed to open it.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.docpin.app/mcp
Auth:        OAuth 2.0, dynamic client registration, PKCE
Scopes:      publish, settings
Registry:    app.docpin/docpin 1.0.0 (active, published 2026-11-07T17:47:59Z)
REST:        https://api.docpin.app with an API key
Link forms:  acme.docpin.it/{slug} · docs.acme.com/{slug} (Pro) · docpin.it/Ab3dE7
Plans:       Free (3 pages) · Pro $8 a month
```

## What the endpoint says about itself

A keyless `initialize` on `https://mcp.docpin.app/mcp` answers **401** with

```
WWW-Authenticate: Bearer realm="OAuth",
  resource_metadata="https://mcp.docpin.app/.well-known/oauth-protected-resource/mcp",
  scope="publish settings"
```

and the document it names answers **200** with `resource` set to the MCP URL, the authorization server on the same host, `scopes_supported` of `publish` and `settings`, `bearer_methods_supported` of `header`, and `resource_name` of `DocPin`. That is the whole auth model in two reads: there is no API key to paste into a chat client, and the two scopes are the split that matters operationally. A connection approved without the settings tick can publish pages and cannot touch branding, domains, members or billing.

The registry record is a single active version, `1.0.0`, published four minutes before the submission was filed, with one `streamable-http` remote and the website `docpin.app`.

## The tools, by the job they do

**Publishing.** `publish_page` takes `html`, or `files` as `[{path, content}]` with an `index.html` inside, and returns the links. Republishing the same `slug` publishes a new version **behind the same link**, which is the single behaviour that makes this usable for a recurring report: the URL in a partner's bookmarks does not rot. A draft returns `url: null` and a `previewUrl` that works for about an hour and is not for sharing. For large pages there is `create_upload_link`, a one-time link valid **15 minutes** that takes a file up to **25 MB** (a `.zip` with an `index.html` works) and prints the links as JSON as soon as the upload lands, which is the route for anything an agent can write to disk faster than it can inflate a JSON string.

**Who can open it.** `set_access` takes `team`, `public`, `password`, `people` (emails and `@domains`) or `inherit`. Password pages and people-only pages need Pro, and the `inherit` value is what makes boards coherent: pages in a board follow the board. `set_draft` with `draft: false` is the share step and it *requires* an `access` value, so the agent has to ask the person who should be allowed in rather than defaulting to public. `rename_page` keeps the short link and redirects the old addresses, and `move_page` puts a page in or out of a board.

**What happened after.** `list_versions` and `restore_version` give history and a rollback. `get_page_views` reports how often a page was opened and, on a people-only page, by whom. That last pair is the difference between publishing and sending: a report nobody opened is a fact you can see.

**Kept current without republishing.** Every page carries a JSON store, up to **1 MB**, read in the browser with `docpin.data()` or `docpin.onData(cb, { every })`. `set_page_data` merges by default (a `null` removes a key), `replace: true` replaces the object, and `get_page_data` first is the documented way to avoid losing keys. This is what a dashboard actually needs: the layout and the numbers are separate artifacts, so a nightly job updates the figures and the page keeps its link, its version history and its access rules untouched. Writes are capped at about **30 a minute per workspace** (`429` over that) and the store is `413` past 1 MB.

**Workspace settings.** `get_workspace_settings` returns the plan, the new-page defaults, branding, custom domains with DNS status, members and invites, and billing in one call. `add_custom_domain` returns the CNAME to set plus a one-click link where the DNS provider supports it, `check_custom_domain` is open to any member, and `set_branding_image` takes a URL or base64. `get_billing_link` returns a Stripe link with `interval` of `month` or `year`: the person pays on Stripe themselves. Deleting a workspace, creating API keys and `delete_page` stay behind an explicit human request, which is the right side of the line for an agent to be on.

## The published page, and what it cannot do

The page runs in a sandboxed frame on its own address under `docpinusercontent.com`, one address per published version, with the surrounding DocPin page carrying the link, the badge and the password or sign-in screen. `localStorage` and `sessionStorage` work, kept per page and per visitor, and survive both reloads and new versions. **Cookies and IndexedDB are blocked**, service workers with them, and the `?query` and `#hash` sync with the address bar so state written with `history.replaceState` is shareable. The vendor's own checklist for AI-generated pages is the practical version of all of this: one self-contained HTML document, handle empty data, wrap `localStorage` in `try/catch`, and avoid anything needing the camera or location.

That means a DocPin page is a place to read a report, filter a table and keep a view in the URL. It is not a host for an authenticated web app, and it is not a file store. Page data is as visible as the page it feeds, which the vendor states plainly: never put secrets in it.

## Why it earns a guide rather than a hold

The artifact shelf already has owners for two adjacent jobs. [HTML Pub](/hermes/mcp/servers/external/htmlpub-mcp/) publishes AI-generated HTML to a domain through the Leadpages ecosystem, and [Shareglow](/hermes/mcp/servers/external/shareglow-mcp/) fixes how a link renders when it is pasted somewhere. Neither of them answers the question an operator asks the second time: *who is allowed to open this, and did they.* DocPin's access modes, version history with restore, view log and the data store that updates a dashboard without a republish are four capabilities in one product, and the stable link across republishes is the mechanical part that makes the other three usable for anything recurring.

For any team whose deliverable to a client is a report, the pattern is: the agent builds the page, `publish_page` on a named slug, `set_access` to the client's domain, `get_page_views` as the follow-up signal, and `set_page_data` from whatever job recomputes the numbers. That is a delivery loop, not a hosting account.

## Limits Recorded

- **Free** is 3 pages with workspace links, public pages, secret links and page data. **Pro at $8 a month** adds unlimited pages, custom domains, password and people-only pages, and a smaller badge.
- Page data is **1 MB per page** and about **30 writes a minute** per workspace; both limits return their own status rather than failing quietly.
- Upload links expire in **15 minutes**; draft preview links last about an hour and are explicitly not for sharing.
- The MCP endpoint is OAuth-only. An agent that cannot complete a browser sign-in cannot use it, whatever its key situation.
- Page data, view counts, version links and access lists all live with the vendor. This is a hosting product, not a connector to data you already own.
- Hosted and priced as a service with no public repository, so the sandbox behaviour is documented rather than auditable. Recorded as a limit, not a criticism.
- Read on **2026-11-07**. Re-read `https://docpin.app/docs/index.md` before quoting the plans, which changed once already.

## See Also

- [HTML Pub MCP](/hermes/mcp/servers/external/htmlpub-mcp/) - publish an agent's HTML to your own domain through Leadpages
- [Shareglow MCP](/hermes/mcp/servers/external/shareglow-mcp/) - Open Graph previews, branded images and click stats for the links you publish
- [SumOffice MCP](/hermes/mcp/servers/external/sumoffice-mcp/) - the other half of the artifact loop: edit a workbook and return it as a download
- [ReportGem MCP](/hermes/mcp/servers/external/reportgem-mcp/) - the report itself rather than the link it lives on
