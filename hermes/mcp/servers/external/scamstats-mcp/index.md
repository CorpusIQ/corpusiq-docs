---
title: "Scamstats MCP - What Fraud Costs Each Country"
description: "Keyless MCP over comparable national scam figures: people scammed, money lost and money returned per country, borrowed estimates labelled."
category: "Data / Research"
stars: "0 (hosted Streamable HTTP at https://scamstats.org/mcp, no key, seven tools, five driven in this pass)"
added: 2026-11-18
source: "the mcp.so submission queue entry 7558 filed 2026-11-18T05:59:09Z, the registry record io.github.Rand0mThoughts/scamstats published 2026-11-18T01:13:08Z, and a probe session on 2026-11-18 that drove five of the seven tools keyless"
relevance: ★★★
tags: [fraud, scams, open-data, risk, statistics, countries, keyless, remote, mcp]
last_updated: "2026-11-18"
---

# Scamstats MCP

**Every country counts fraud differently, which is why "fraud is up" is usually a statement about methodology rather than about crime.** Scamstats publishes one comparable measure per country, states where each number came from, and labels the rows it had to model because the country's own publishers do not break fraud down that way.

That makes it useful for a specific job an operator actually has: sizing fraud exposure in a market before entering it, or explaining to a board why one market's loss figure is not comparable with another's.

```text
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://scamstats.org/mcp
Server info:   scamstats 1.0.0, protocol 2025-06-18
Registry:      io.github.Rand0mThoughts/scamstats 1.0.0, published 2026-11-18T01:13:08Z
Auth:          none
Tools:         7 listed, 5 driven in this pass
Publisher:     Armidale, scamstats.org
```

## The evidence tier

Keyless end to end, which is the strongest tier this catalogue records. `initialize` answered **200** without a credential, `tools/list` returned all **seven** tools, and every `tools/call` in this pass answered with data. There is no key, no trial, no credit ledger and no sign-up.

The server's own instructions state the contract in one line: comparable figures per country, and *every answer ends with how to cite Scamstats*. It keeps that promise, which is unusual enough to be worth saying.

Five of the seven tools were driven: `list_countries`, `get_world`, `get_country`, `get_scam_type` and `compare_countries`. `search_sources` and `get_source` were not, so the source catalogue is recorded here from the listing rather than from a call.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `list_countries` | none | Every covered country with people scammed, share of adults and its page URL |
| `get_country` | `iso2` | One country: people, share, money lost, victims who lost money, victims who told police, cases recorded, money returned, and a per-scam-type split |
| `compare_countries` | `iso2`, `measure` | One measure across up to 20 countries, naming any differences in how they were counted |
| `get_world` | none | The world estimate with its period and method link |
| `get_scam_type` | `code` | One scam type's people and money lost in every covered country |
| `search_sources` | `query`, `area`, `measure` | The catalogue of source publishers |
| `get_source` | `id` | One catalogue entry in full, with editions and how it is used |

## The numbers, and the one comparison that lands

The world view, for the calendar year 2025:

```text
People scammed:         593.1 million
Share of adults:        10.2 %
Money lost:             US$ 208.14 billion
Money returned:         US$ 20.48 billion
Period:                 2025-01-01 to 2025-12-31
```

Then the United States, which is where the shape of the dataset becomes visible:

```text
People scammed:         55,037,839      20.1 % of adults
Money lost:             US$ 103.93 b
Victims who lost money: 25 %
Victims who told police: 8.2 %
Cases recorded:         1,008,597
Money returned:         US$ 9.95 b, 9.6 % of the money lost
Most common scam:       card fraud
```

**One country carries half the world's measured losses.** 103.93 of 208.14 billion is 49.9 percent, and the returned-money figure reconciles internally at 9.6 percent of the loss. That is not a curiosity: it means any global fraud statistic quoted in a deck is mostly a statement about US reporting practice, and a reader who does not know that will mis-size every other market.

A three-country comparison confirms the scale difference between reporting regimes rather than between crime rates:

```text
Money lost, 2025:
  United States   US$ 103.93 b
  Germany         US$ 5.29 b   (Estimated)
  United Kingdom  US$ 3.35 b
```

The per-country answers each carry their own page URL and a citation line, so a claim built on them can be sourced back to a page a reader can open.

## Where the honesty is, and why it matters

`get_country` returns a scam-type table, and several rows carry a sentence that most datasets would have left out:

```text
Friend or family impersonation: 274,320 people, US$ 121.2 m.
  Borrowed from Australia, Canada, India, Indonesia, Japan, Malaysia,
  the Philippines, Singapore, South Korea, Thailand, the UK and Vietnam.
```

The borrow means that country does not publish a split for that scam type, so Scamstats applied the average *shape* from the countries named and scaled it to its own totals. Two consequences follow, and both are decisions a user has to make rather than facts the server can make for them:

- A borrowed row is a modelled share, not a measurement, so comparing two countries on a borrowed row compares two models.
- A borrowed row is still better than a missing one for sizing exposure, provided the label travels with the number. Here it does, inline, on the row.

`get_scam_type` applies the same discipline across countries. For investment fraud the top of the list is ordered by money, and the borrowing is named on the rows that need it:

```text
United States  2,146,832 people   US$ 21.31 b
China         33,152,646 people   US$ 4.74 b   (Borrowed from India, Indonesia, Malaysia, the Philippines, Singapore, Thailand and Vietnam)
Brazil         3,929,312 people   US$ 1.47 b   (Borrowed from Australia, Canada, Japan, Singapore and the US)
South Korea      115,530 people   US$ 1.24 b   (Borrowed from Japan)
Nigeria        7,421,420 people   US$ 1.23 b   (Borrowed)
South Africa     765,177 people   US$ 1.06 b   (Borrowed)
India         35,147,691 people   US$  907.1 m  (Borrowed from Japan and Singapore)
Japan             22,770 people   US$  877.5 m
Canada           106,251 people   US$  796.5 m
Australia         61,265 people   US$  742.6 m
```

Read the people column against the money column and the split is the story: 35.1 million investment-fraud victims in India at 907 million dollars is 26 dollars each, while 22,770 in Japan at 877 million is 38,000 dollars each. A model asked to rank "which country has the worst investment fraud problem" will pick whichever column it happens to look at, and both answers are defensible, which is exactly why the data has to arrive with its shape intact.

## The error tier is a model of how to refuse

The first `compare_countries` call passed a measure of `money_lost` and was refused with the enum named:

```text
The argument measure must be one of: people_scammed, share_of_adults,
money_lost_usd, cases_recorded.
```

That is the right failure: an enumerated argument, refused by name, with every legal value listed, so a calling model corrects itself without a documentation round trip. It is the opposite of the empty 401 body recorded on several entries in this catalogue.

## Why this earns a page

CorpusIQ readers run businesses across borders, and fraud exposure is one of the few risk inputs that has an official number per country and no consistent definition between them. This is the first entry on the list whose product is that reconciliation, and it is keyless, cited and candid about what it modelled.

Three stars: driven, source-linked, and it refuses bad arguments clearly. Not four, for two reasons that are about coverage rather than quality: **49 countries** is a useful set but far from global, and the scam-type layer is largely borrowed, so the deepest cuts are modelled rather than measured.

## Installation

```json
{
  "mcpServers": {
    "scamstats": {
      "url": "https://scamstats.org/mcp"
    }
  }
}
```

No key, no environment variable, no session state. Works in any client that speaks Streamable HTTP.

## Configuration

- Ask by ISO-2 code. `get_country` takes `US`, `GB`, `DE`, not a country name, and `list_countries` is the way to discover which codes are covered.
- Use `compare_countries` for cross-market work rather than looping `get_country`. It applies one measure across up to 20 countries in one answer and names any differences in period or definition between them.
- Carry the `Estimated.` marker and the `Borrowed from ...` sentence into whatever you publish. Stripping them converts a modelled number into a measured one, which is the exact error this dataset is built to avoid.
- Keep the citation line. Every answer ends with *Cite as: Scamstats (Armidale), scamstats.org*, and the per-country page URL is on the row.

## Limitations

- **49 countries**, with uneven depth. Some have published national splits, others only a headline estimate.
- **A scam-type split is borrowed where the country does not publish one**, so the per-type figures for those rows are modelled from named peer countries.
- **Estimates dominate the aggregate.** The world figure is built from the countries that have figures and changes each time a country is added, so it is not a fixed constant to cache.
- **Reporting rates differ by two orders of magnitude.** The US reports 1,008,597 cases against 55 million estimated victims, and only 8.2 percent of victims told the police. The "cases recorded" measure is a measure of police intake, not of crime.
- Two tools, `search_sources` and `get_source`, were not driven in this pass, so the source catalogue is recorded from the listing.

## FAQ

### Does Scamstats MCP need an API key?

No. The handshake, the tool listing and every call in this pass answered without a credential.

### Can the figures be cited?

Yes, and the server insists on it: every answer ends with a citation line naming Scamstats (Armidale) and the site, and per-country answers carry the country page URL.

### How many countries does it cover?

49 at the time of this pass. `list_countries` returns the current set with each country's people scammed and share of adults.

### Are the per-scam-type numbers measured?

Not always. Where a country publishes a split, the row is a measurement. Where it does not, the row says *Borrowed from* and names the countries whose average shape was applied, so a borrowed row should be read as a model rather than a count.

## See Also

- [NYSgpt Data Library MCP - 36 Public Databases in Chat](/hermes/mcp/servers/external/nysgpt-data-library-mcp/)
- [Tiana Seller Compliance MCP - Seller Rules Before a Listing](/hermes/mcp/servers/external/tiana-seller-compliance-mcp/)
- [Geo Insights Environmental Data MCP - Country Indicators in Chat](/hermes/mcp/servers/external/geo-insights-environmental-data/)
