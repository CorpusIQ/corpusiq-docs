---
title: "Media List MCP - Journalist and Podcast Contacts"
description: "Find journalists, editors and podcast hosts to pitch by beat, outlet and location, and work with saved lists and campaigns from your assistant."
category: Marketing
stars: n/a (new listing)
added: 2026-10-12
source: "chatmcp/mcpso issue #5211 (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [pr, public-relations, journalists, media-contacts, podcasts, outreach, marketing, remote-mcp]
last_updated: "2026-10-19"
---

# Media List MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or API key)** - find the right journalists, editors, podcast hosts and creators to pitch, straight from your AI assistant. Search Media List by beat, outlet, location and role, open a contact, and work with your saved lists and campaigns. Built for PR agencies, publicists and founders who pitch their own story; read only.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (sign in with Media List, dynamic client registration) or an API key as a Bearer header
Endpoint: https://medialist.com/mcp
Tools: 9 (search_contacts, search_outlets, get_contact, get_filter_values, list_lists, get_list, list_campaigns, get_campaign, get_account)
Pricing: paid Media List plan (see medialist.com/pricing); no free tier for API access
Category: Marketing / PR
Built by: Media List (medialist.com, hosted service)
Website: medialist.com
Listing: chatmcp/mcpso issue #5211 (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Media outreach is a research problem wearing a writing problem's clothes. The pitch is easy; knowing which 40 journalists across 12 outlets actually cover your category, and which podcast hosts take founder guests, is the work. That research normally means a subscriptions spreadsheet, a browser and an hour per campaign.

Media List moves it into the assistant. Ask who covers your sector at the outlets that matter, filter by beat and location, open a contact to check the fit, and pull the campaign and list context you already maintain. The catalog's Comunicate entry handles press-release distribution once the story goes out; Media List is the targeting layer before that, for the founders and agencies choosing who to approach.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Search | search_contacts, search_outlets, get_filter_values: find journalists, hosts and outlets by beat, role, location and other filters |
| Contacts | get_contact: one contact record with their details and outlets |
| Lists and campaigns | list_lists, get_list, list_campaigns, get_campaign: work with the lists and campaigns you maintain in Media List |
| Account | get_account: the account behind the connection |

## Installation

```bash
claude mcp add --transport http --scope user media-list https://medialist.com/mcp
```

Then sign in with Media List when the client opens the OAuth flow, or send an API key as a Bearer header.

## Configuration

```json
{
  "mcpServers": {
    "media-list": {
      "type": "http",
      "url": "https://medialist.com/mcp",
      "headers": {
        "Authorization": "Bearer ${MEDIA_LIST_API_KEY}"
      }
    }
  }
}
```

## Business Relevance

- **Founders pitching their own story** can build a targeted journalist and podcast list in one conversation instead of hiring an agency for the first pass.
- **PR agencies and publicists** can research beats and outlets for a new client fast, then work from their existing lists and campaigns.
- **In-house marketing teams** covering launches can find the right reporters per announcement without keeping a media database current by hand.
- **Content and SEO teams** doing digital PR can match link-building targets to actual journalists covering the beat.

## Integration with CorpusIQ

CorpusIQ answers from the business systems; Media List answers who to pitch. Pull the story material from your connected sources - Stripe for growth numbers you can disclose, the frontend or content source for what shipped - then have the assistant match the story angle to the journalists who cover that beat and open the contact. The pair turns "we should get coverage" into a named list with the story facts behind it.

## Limitations

- Requires a paid Media List plan; the MCP endpoint itself answers initialize keyless but tool calls need the plan's credentials.
- Read only: it does not send pitches or manage replies; combine it with your outreach tool for sending.
- Coverage is only as good as Media List's database; spot-check a contact before a critical pitch.

## FAQ

### What do I need to get started?

A Media List plan and an account. Connect the server with OAuth or an API key, and the assistant can work with contacts, lists and campaigns on your plan.

### Is it read only?

Yes. The nine tools search and read contacts, outlets, lists and campaigns; nothing in the API surface writes to your account.

### How is this different from the catalog's Comunicate entry?

Comunicate distributes a release once it is written; Media List is where you decide who to pitch in the first place. Use them as a pair: target with Media List, distribute with Comunicate.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
