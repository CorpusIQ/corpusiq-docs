---
title: "djbnb MCP - Who Is Playing Tonight From a Live Calendar"
description: "Two keyless tools over 17 US cities: every announced DJ night tonight or this weekend, with venue, start time, door price and the DJs on the bill."
category: "Data & Research"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7771 filed 2026-11-21T14:50:01Z; the official MCP registry record com.djbnb/djbnb 1.0.0; keyless initialize and tools/list, then four tools/call and one resources/read on 2026-11-21"
relevance: ★★★
tags: [events, nightlife, music, local-data, calendar, remote-mcp, keyless, mcp-apps]
last_updated: "2026-11-21"
---

# djbnb MCP

**Remote MCP server (Streamable HTTP, no authentication)** - a live calendar of DJ nights in seventeen US cities, exposed as two tools and one UI card. An agent asks "who is playing in Detroit tonight" and gets back each night's start time, venue, door price when known, the DJs on the bill and a link per event, read from the listings on djbnb.com.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://djbnb.com/mcp
Tools:       2 (list_cities, whos_playing)
Resources:   1 (ui://djbnb/night-card-v1.html, MCP Apps card)
Registry:    com.djbnb/djbnb 1.0.0
Instructions: "Read only. Answers who is playing in a djbnb city tonight
              or this weekend, from the nights listed on djbnb.com."
Machine-readable: https://djbnb.com/llms.txt
```

## Why This Matters for Operators

Local event data is the kind of structured answer that a general model invents. This server does not: every line is an event page on the vendor's own site, and the two things that make a listing verifiable - a start time local to the city and a door price - are in the payload when the venue published them.

For an operator it is also a small, honest test of what a niche directory looks like when it is exposed properly: two tools, an enum on the only free-form argument, and a refusal that names the covered cities instead of returning nothing.

## Measured Behaviour

Four `tools/call` requests and one `resources/read` were driven keyless on 2026-11-21.

| Call | Arguments | Result |
|---|---|---|
| `list_cities` | none | **17** cities, each with a slug and links to its tonight and this-weekend pages |
| `whos_playing` | `detroit` | **11** nights tonight, Saturday, November 21 |
| `whos_playing` | `new-york-ny`, `this_weekend` | **40** nights across Saturday and Sunday |
| `whos_playing` | `atlantis` | refused: *"djbnb does not cover atlantis yet"* plus the seventeen-city list |
| `whos_playing` | `when: "weekend"` | refused: *"when must be tonight or this_weekend, not weekend."* |
| `resources/read` | `ui://djbnb/night-card-v1.html` | **200**, `text/html;profile=mcp-app`, **10,456** bytes |

Detroit, tonight, as returned:

```text
9:00 PM   Fadi Mohem by Urban Pulse
          Tangent Gallery / Hastings Street Ballroom, Detroit, MI. $20 cover.
          DJs: Echoføn, Hudson
9:00 PM   Eli Escobar - Extended Set            TV Lounge, Detroit, MI
9:00 PM   12 Hour Party feat. John Acquaviva    Marble Bar, Detroit, MI
          DJs: saylem celeste, Terrence Dixon, Pablo R. Ruiz
10:00 PM  HIPHOP NIGHT: DJ MOBEATZ + MORE       Big Pink, Detroit, MI. $20 cover.
10:00 PM  Deep Dive                             SPKRBOX, Detroit, MI
10:00 PM  Miami Nights Presents: Miami Vice     The Annex, Detroit, MI. Free.
2:00 PM   ABOVE THE STATUS: Dunk Contest        Social Status Detroit. Free.
```

New York, this weekend, returned **40** nights in the same shape, including three separate Saturday 5:00 PM reggaeton rooms at San Antonios and a free 7:00 PM happy hour at Bossa Nova Civic Club in Brooklyn. The asymmetry is the interesting part: the same question returns eleven nights in Detroit and forty in New York, and a model that guesses from city size would get the ratio wrong.

### The card is a real UI resource

The server advertises a `night-card` resource at `ui://djbnb/night-card-v1.html`, and reading it returns **10,456** bytes of self-contained HTML with `mimeType: text/html;profile=mcp-app` - a dark card that lays out the time, the night, the venue, the door price and the linked DJs. That is a client-rendered view of the same answer rather than a separate API, and it is the shape MCP Apps expects: the server owns the presentation.

## Where It Stops

- **Seventeen US cities.** Detroit, Royal Oak, Salt Lake City, Chicago, Austin, Denver, Seattle, Philadelphia, Miami, Los Angeles, New York, San Francisco, Washington DC, Boston, San Diego, Portland and Houston. Anything else is refused with that list.
- **Two time windows.** `tonight` is the default; `this_weekend` widens it. There is no date argument, so a "next month" plan is not answerable.
- **Nightlife only.** DJ nights and the venues that host them. No concerts, no ticketing, no ticket purchase.
- **No artist lookup.** A DJ appears as a line inside an event with a profile link; there is no tool that takes a DJ name and returns their dates.
- **Door price only when known.** Some lines carry a cover, some carry "Free", and the rest carry nothing.
- **Local time, no timezone field.** Start times are local to the city and the response says so, but no offset is returned.

### Does it need an account or a key?

No. `initialize`, `tools/list`, all four calls above and the resource read answered without a token, a cookie or an API key. The registry record names the remote and nothing else.

### How should an agent present a night?

Give the start time with its city-local caveat, the night name, the venue, the door price if one was returned, and the DJs. Link the event. Do not add a recommendation the payload does not make, and do not merge two nights into one answer - each event has its own link.

### Can an agent ask for a city it cannot spell?

Yes, and it gets a useful refusal. `atlantis` returned the "does not cover" message with the full city list, which is enough for a retry without a second call. The one enum argument is equally explicit: `weekend` is refused by name, `this_weekend` is accepted.

## Catalogue Position

Event and venue data had no owner in this catalogue. The nearest surfaces are ticketing and local search, and neither returns a night-by-night listing with door prices. djbnb is the first entry here whose payload is a city's calendar rather than a catalogue of businesses, and it is also a small clean example of a server shipping an MCP Apps card beside its tools.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery - November 21, 2026 (Midday)](/hermes/mcp/sweeps/sweep-november21-2026-midday)
