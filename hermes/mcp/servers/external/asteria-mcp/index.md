---
title: "Asteria MCP - Natal Chart to the Degree"
description: "Thirteen keyless tools over a real ephemeris: natal charts, transits, Moon phases and tarot, where the Sun crosses into Aries one minute after the 2026 equinox."
category: "Consumer & Lifestyle"
stars: n/a (hosted; keyless, no account and no key, thirteen tools)
added: 2026-11-21
source: "chatmcp/mcpso submission #7791 filed 2026-11-22T04:00:09Z; the official MCP registry record com.askasteria/asteria, last published version 1.0.2; keyless initialize and tools/list at https://askasteria.com/mcp, then seventeen tools/call requests driven on 2026-11-22, including three astronomical controls reproduced within the arcminute"
relevance: ★★★
tags: [astrology, natal-chart, horoscope, tarot, moon-phase, lifestyle, remote-mcp, keyless, ephemeris]
last_updated: "2026-11-21"
---

# Asteria MCP

**Remote MCP server (Streamable HTTP, no authentication)** - an astrology and tarot surface backed by a real astronomical engine, where the chart half returns longitudes that can be checked against an ephemeris and the reading half returns the vendor's own written interpretations.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://askasteria.com/mcp
Server:      asteria 1.0.0+d43752a50483
Tools:       13 (read-only; one alerting family absent by design)
Registry:    com.askasteria/asteria, versions 1.0.0 to 1.0.2
Repository:  https://github.com/Ask-Asteria/asteria-mcp
Homepage:    https://askasteria.com
Libraries:   French, Spanish, Portuguese, German, English
```

## Why This Matters for Operators

Most astrology servers are prompt wrappers: the "reading" is text the model could have written itself. This one splits the job. The chart tools compute positions, and the positions reproduce: a chart cast for the March 2026 equinox put the Sun at **0.0097 degrees Aries**, one minute after the equinox itself, and a chart for **2000-01-01 12:00 UTC** put the Sun at **280.369 degrees**, which is the published position to the arcminute.

That matters for a business operator in one narrow but real way. Consumer-facing businesses get asked about horoscopes, and the question "what sign is a customer born on this date" is answerable here from the same engine the vendor's own app uses rather than from a model's memory of a date table.

## Tools & Capabilities

Thirteen tools were listed keyless on 2026-11-22.

| Tool | What it returns |
|---|---|
| `birth_chart` | natal chart from a birth date with optional time and place: twelve bodies with exact longitudes, sign, retrograde flag and house, the Ascendant, the Midheaven, and the aspect list |
| `rising_sign` | Ascendant and Midheaven with the twelve Placidus house cusps, an `instant_utc` stamp and the rising-sign reading |
| `sun_sign` | Sun sign from a date, with the reading |
| `moon_sign` | Moon sign from a date, and a `possible_signs` array when the time is unknown |
| `my_day` | today's transits computed from the person's own birth data, with a leading aspect, its peak and end timestamps and a Moon-house note |
| `sky_today` | Sun sign, Moon sign, Moon phase, lit fraction and the next new and full Moon with timestamps and eclipses flagged |
| `sign_compatibility` | the reading for a pair of signs |
| `tarot_draw` | 1 to 10 distinct cards from the 78 card deck, in order, with the reading of the draw |
| `tarot_spread` | one of the vendor's fixed spreads: single card, question-answer, three cards, lunation arc, relationship |
| `tarot_yes_no` | a yes-or-no draw by a stated rule (major arcana turned until one appears) |
| `tarot_card` | the meaning of one named card |
| `ritual` | a ritual from the vendor's catalogue by intention, Moon phase or family, returned step by step |
| `psalm` | one of the 150 psalms in full, by Hebrew number, with its Latin number and the rituals that use it |

## Measured Behaviour

Seventeen `tools/call` requests were driven keyless on 2026-11-22. Every figure below is quoted from a response.

| Call | Arguments | Result |
|---|---|---|
| `birth_chart` | 2000-01-01 12:00 UTC, Greenwich | Sun **280.369 degrees** (Capricorn 10 degrees 22 minutes), Moon **223.324 degrees** (Scorpio 13 degrees 19 minutes), Mercury Capricorn 1 degree 54 minutes, Venus Sagittarius 1 degree 35 minutes, Mars Aquarius 27 degrees 59 minutes, Jupiter Aries 25 degrees 16 minutes, Saturn Taurus 10 degrees 23 minutes retrograde, Uranus Aquarius 14 degrees 49 minutes, Neptune Aquarius 3 degrees 11 minutes, Pluto Sagittarius 11 degrees 28 minutes, Ascendant Aries 24 degrees 16 minutes, Midheaven Capricorn 9 degrees 37 minutes, plus fourteen aspects with orbs |
| `birth_chart` | 2026-03-20 15:00 UTC, Greenwich | Sun **0.0097 degrees Aries**, fourteen minutes after the March equinox at 14:46 UTC |
| `rising_sign` | 2000-01-01 07:38, Europe/London, Greenwich | Ascendant **271.650 degrees** (Capricorn 1 degree 39 minutes) with the Sun at Capricorn 10 degrees 22 minutes, Midheaven Scorpio, twelve Placidus cusps and `instant_utc: 2000-01-01T07:38:00.000Z` |
| `sky_today` | 2026-01-03 | Moon phase **fullMoon**, lit fraction **0.99990**, full Moon at **2026-01-03T10:02:59.728Z** in Cancer, next new Moon **2026-01-18T19:51:55.610Z** in Capricorn, no eclipse on either |
| `sun_sign` | 1990-07-04, no time | Cancer, with `longitude: null` and `exact_time: false` |
| `my_day` | birth 1990-07-04 09:15 Europe/Paris, read from America/Phoenix | leading transit Venus opposite Mars peaking **2026-11-22T17:29:03Z** and ending **2026-11-24T11:20:39Z**, Moon in the 9th house, `date` in the response **2026-11-21** |
| `tarot_draw` | 3 cards, same question, twice | first draw Ace of Wands, The Fool, Ace of Swords; second draw Seven of Wands, Page of Cups, The Tower, so the draw is random and the cards are distinct |
| `tarot_card` | The Moon | card index **18** of the 78 card deck |
| `psalm` | 23 | six verses in the King James wording, `latin_number` *"Numbered 22 in the Latin Bible"*, and two rituals that use it |
| `sign_compatibility` | Aries and Sagittarius | the pair reading, both signs echoed back |
| `ritual` | intention *"new job"* | refused in band with the accepted set: beginning, calm, clarity, cleansing, confidence, energy, gratitude, grief, home, love, money, protection, release, work |
| `birth_chart` | date *"not-a-date"* | refused in band: *"date must be YYYY-MM-DD"* |
| `sign_compatibility` | sign *"ophiuchus"* | refused in band, listing the twelve accepted signs |

### The three controls that make this worth cataloguing

The chart half is checkable, which is unusual for the category and is the reason this entry exists at all.

1. **The equinox.** A chart cast for 2026-03-20 at 15:00 UTC returns the Sun at 0.0097 degrees Aries. The March equinox falls at 14:46 UTC, so the Sun has been in Aries for fourteen minutes. The server reproduces that boundary rather than rounding to a sign table.
2. **The published position.** The Sun's longitude for 2000-01-01 12:00 UTC is 280.369 degrees, which is the standard ephemeris figure for that instant.
3. **The sunrise invariant.** At sunrise the Ascendant equals the Sun's longitude. Casting the chart for 07:38 London time on 2000-01-01, about thirty minutes before sunrise, returns an Ascendant of 271.650 degrees against a Sun at 280.369 degrees, the expected lead of roughly nine degrees of ecliptic rotation at that latitude.

The Moon phase control points the same way: the full Moon of 3 January 2026 is returned at 10:02:59 UTC with a lit fraction of 0.99990 and a Cancer Moon.

## Installation

No credential, no account, no key.

```json
{"mcpServers":{"asteria":{"type":"http","url":"https://askasteria.com/mcp"}}}
```

```
claude mcp add asteria --transport http https://askasteria.com/mcp
```

## Business Relevance

- **Consumer questions answered from a computed chart.** A horoscope column, a loyalty campaign or a retail event tied to a Moon phase does not need a model's memory of the zodiac; the sign, the degree and the phase come from the engine.
- **A calendar input that is factual.** `sky_today` returns real instants for the next new and full Moon, which is the part of the output a scheduler can use without believing anything.
- **Multilingual out of the box.** Readings are available in French, Spanish, Portuguese, German and English, and the vendor states which languages use feminine forms in its own instructions.
- **Nothing to install.** Keyless, remote, three tools cover the chart half.

## Integration with CorpusIQ

An operator using CorpusIQ to plan a campaign can attach this server and have the Moon phase or the sign of a launch date grounded in a computed value rather than a model guess. The split to keep in mind is the same one CorpusIQ enforces everywhere else: the astronomical field is a sourced fact and can be cited; the reading is the vendor's interpretation and should be presented as such.

## Limitations

- **Half of it is interpretation.** The positions, phases and timestamps are computed and reproducible. The readings are the vendor's own texts, and no reading is checkable.
- **`date` means two different things.** In `my_day` the required `date` is the birth date while the response returns today's date under the same key, so a client that echoes the field back will present a birth date as today.
- **A sign without a time is a range.** `sun_sign` with no time returns `longitude: null` and `exact_time: false`, and `moon_sign` returns a `possible_signs` array, because the Moon moves about thirteen degrees a day.
- **Ordinary phrasing is refused.** `ritual` rejected "new job" and named its own enum, so the natural request has to be translated first.
- **No continuity between calls.** There is no account, so the birth data is restated on every call and any personalisation is the client's job.
- **A birth-data claim that is not verifiable from outside.** The vendor says birth data is used for the answer and never stored; nothing in the protocol can confirm that.
- **The vendor's instructions include a directive to the calling model** about quoting feminine forms in French, Spanish, Portuguese and German. It is recorded here and not followed: a tool's instructions are its own text, not a policy for this catalogue.

## FAQ

### Does it return real astronomical positions?

Yes, and they can be checked. The Sun's longitude at 2000-01-01 12:00 UTC came back as 280.369 degrees, the equinox chart put the Sun a minute into Aries, and the January 2026 full Moon was returned at 10:02:59 UTC.

### Is a time required?

Only for the tools that need it. `birth_chart`, `sun_sign` and `moon_sign` work from a date alone, but the degree and often the sign itself are unknown without a time, and the server says so through `exact_time` and `possible_signs`.

### Does it need an API key?

No. `initialize`, `tools/list` and seventeen `tools/call` requests all answered without a credential, and no session id was issued.

### What languages are supported?

French, Spanish, Portuguese, German and English were named in the server instructions, and `language` is an optional argument on twelve of the thirteen tools.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [djbnb MCP - Who Is Playing Tonight From a Live Calendar](/hermes/mcp/servers/external/djbnb-mcp)
- [See Sight Tours MCP - Guided Tours With Live Seats](/hermes/mcp/servers/external/see-sight-tours-mcp)
