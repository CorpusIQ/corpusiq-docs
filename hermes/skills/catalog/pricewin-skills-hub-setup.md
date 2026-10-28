---
title: "PriceWin Skills - Hotel Deal and Flight Search Setup"
description: "PriceWin's travel suite: 68.4K combined installs. Live OTA price comparison across Booking, Agoda, Google Hotels, plus flight search and booking."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pricewin-skills-hub-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "travel", "price comparison", "hotel booking"]
---

# PriceWin Skills - Setup Guide

**Source:** [price-win/pricewin-skills-hub](https://www.skills.sh/price-win/pricewin-skills-hub) via skills.sh - 68.4K combined installs across 6 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [price-win/pricewin-skills-hub](https://github.com/price-win/pricewin-skills-hub) - 2 stars, MIT No Attribution (the pack records MIT; the LICENSE text is MIT-0), branch main, last commit 2026-08-09, 5 skill directories under `skills/`; four hold a `SKILL.md` with `reference.md`, `skill-card.md` and `SECURITY.md` beside it, and the standalone deal finder replaces the docs with `bin/`, `lib/`, a `package.json` and its own `install.sh`

**Category:** Travel price comparison, flight search and hotel booking for agents

**Quality Tier:** 🟡 Beta - very small vendor repo, 2 GitHub stars, 5 skill directories against 6 indexed listings, maintained by the PriceWin team alone, two of six listings carry a Snyk Fail verdict

PriceWin (price.win) is a Vietnamese travel price comparison product that markets itself as finding the best price across 50+ travel platforms. This repository is its agent surface, published to skills.sh, ClawHub, Hermes and OpenClaw, and it splits the problem in two. One skill, `pricewin-hotel-deal-finder`, is standalone: it ships its own code, drives a local stealth browser over Booking.com, Agoda and Google Hotels, adds one HTTPS call to the OpenTravel public API, and needs no MCP server, no account and no API keys. The other four are documentation-only skills that drive a hosted `pricewin` MCP server which the user has already installed and approved.

That split is the interesting design decision. Search and comparison are cheap to run locally and safe to hand to an agent, so the deal finder runs on the machine. Booking is neither, so it lives behind a server the user registers deliberately, in a skill of its own, so that installing hotel search never grants booking authority. The repository is also candid about its own history: `CLAUDE.md` records that the standalone skill was renamed from `pricewin-deal-finder` to `pricewin-hotel-deal-finder`, accepting a full install-count reset, which is why the index still carries both names.

## Installation

The README leads with a single-skill install through the skills.sh CLI:

```bash
npx skills add https://github.com/Price-Win/pricewin-skills-hub --skill pricewin-hotel-deal-finder
```

The README also documents a direct Hermes install that pulls the whole directory from the repository:

```bash
hermes skills install github:Price-Win/pricewin-skills-hub/skills/pricewin-hotel-deal-finder
```

The standalone skill needs its own first-run setup, because `skills add` only copies files. The install hook fetches Node dependencies and a Chromium build for Patchright, roughly 200MB, once:

```bash
git clone git@github.com:Price-Win/pricewin-skills-hub.git
cd pricewin-skills-hub/skills/pricewin-hotel-deal-finder && ./install.sh
```

The four MCP skills are inert until the `pricewin` server is registered, and again `skills add` cannot do that for you, since the CLI has no install hook. `pricewin-flight-search` ships a registrar that writes the hosted endpoint into whichever agent configs it finds. Preview it first, then run it, then restart the agent:

```bash
cd skills/pricewin-flight-search
bash install.sh --dry-run
bash install.sh
```

The hosted server is `https://mcp.price.win/mcp` over Streamable HTTP, stateless, with no credentials and no account. If you run the server yourself over stdio instead, the README's `mcpServers` block points `node` at `pricewin-mcp/dist/index.js`. For OpenClaw and ClawHub users, the README shows `openclaw skills install pricewin-hotel-deal-finder` as the consumer side of the same listing.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pricewin-hotel-deal-finder | 19,455 | The standalone one-command comparison: a local Patchright daemon reads Booking.com, Agoda and Google Hotels while one API call hits OpenTravel, then the output ranks best value, cheapest and quality picks in USD with a direct link to the cheapest OTA. No server, no keys, about 200MB of Chromium on first install. |
| pricewin-flight-search | 10,576 | Live flight fares for a route and date across Agoda, Trip.com and Traveloka, one-way or round-trip, any cabin, returning airline, times, stops, duration and a provider booking link. Added 2026-08-01 and the only skill here with its own MCP registrar. |
| pricewin-price-comparison | 10,515 | Comparing live room rates across Booking.com, Agoda, Traveloka and OpenTravel for specific dates, including which OTA is cheapest for a named property, per-room prices and free-cancellation terms. |
| pricewin-hotel-search | 10,498 | Live hotel search for travel dates through `search_hotels_live` and `poll_search_results`, covering Agoda, Booking.com and Traveloka plus OpenTravel direct listings. Documentation only, no code of its own. |
| pricewin-booking-assistant | 10,482 | Recommending a room and completing a real booking on OpenTravel direct inventory: a payment link over a chosen rail, payment status checks, link reissue, and cancellation through a cancel token. Handles guest PII and real money. |
| pricewin-deal-finder | 6,874 | The earlier slug for the standalone deal finder, retired when the skill was republished as `pricewin-hotel-deal-finder` with a deliberate install-count reset. It has no separate directory in the current tree. |

All 6 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Travel pricing is a domain where an agent can produce a confident wrong answer cheaply. Two OTAs quote different totals for the same room, one of them is per night and the other per stay, and a third is in a currency the model silently converts. These skills exist because those mistakes are systematic, and they answer them with procedure rather than prose.

The clearest example is units. `pricewin-hotel-deal-finder` normalizes every source to USD, and the skills state which sources geo-lock to VND and get converted at a live FX rate. `pricewin-flight-search` goes further and tells the agent that a flight `price` is the party total for the leg while hotel prices are per night, that its `bookingUrl` already carries the dates so appending parameters corrupts it, and that the `currency` field must be read rather than assumed. An agent working from memory gets all three wrong.

The polling contract is the second useful piece. `search_hotels_live` returns immediately with a session id and results only arrive through `poll_search_results`, while `poll_flight_results` blocks internally for about 30 seconds, so the hotel sleep-then-poll loop must not be copied onto flights. Getting that wrong produces empty result sets that look like a broken backend.

The third is scope discipline. Only OpenTravel direct results, the ones carrying a `propertyId`, can be booked; OTA results are comparison-only and the skill says so explicitly, in a table, at the top. The booking skill returns a payment link rather than taking card details, so the agent never sees payment credentials, and it treats guest name, phone and email as data that must come from the user in the current conversation rather than from a profile. For an unattended Hermes run that separation is the difference between a helpful booking and an agent guessing whose name to reserve under.

## Usage

| You say | What happens |
|---|---|
| "Find me a hotel in Da Nang for 3 nights, 2 guests" | pricewin-hotel-deal-finder runs one command, reads three sites plus OpenTravel, and returns ranked best-value, cheapest and quality picks with USD nightly prices and links to the cheapest source. A new city pays a one-time discovery cost of 2 to 4 minutes, then joins the selector cache. |
| "Is Agoda or Booking cheaper for this hotel?" | pricewin-price-comparison calls `get_ota_hotel_detail` for the named property and lays out per-room rates per OTA side by side, so the answer is a comparison rather than a single quote. |
| "Search hotels in Bangkok for 12 to 15 November" | pricewin-hotel-search calls `search_hotels_live`, then polls `poll_search_results` until the crawl returns, and reports each property with its source and nightly rate. |
| "Cheapest flight from Hanoi to Bangkok next Friday" | pricewin-flight-search calls `search_flights_live` and `poll_flight_results`, which blocks internally, then returns fares by airline with times, stops and a provider deep link that already carries the dates. |
| "Which rate has free cancellation" | pricewin-price-comparison calls `get_cancellation_policy` and reports the cancellation terms next to the rate, so the cheaper room is not chosen on price alone. |
| "Book that room and send me the payment link" | pricewin-booking-assistant confirms the property is OpenTravel direct, calls `create_booking` with guest details the user typed, and returns a payment link for the chosen rail. The agent never sees card, bank or PayPal credentials, and OTA-only hotels get a handoff link instead. |
| "Cancel booking PW12345" | pricewin-booking-assistant calls `request_cancel_token` with the guest email, then `cancel_booking`, and reports the resulting status instead of assuming the cancellation succeeded. |

## Verification

Probe the paths before you install from them. All five URLs below returned 200 when this guide was written on 2026-10-28, on branch main:

```bash
for p in pricewin-hotel-deal-finder pricewin-flight-search pricewin-price-comparison \
         pricewin-hotel-search pricewin-booking-assistant; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/Price-Win/pricewin-skills-hub/main/skills/$p/SKILL.md"
done
```

Read the two that touch money and guest data before installing them:

- https://raw.githubusercontent.com/Price-Win/pricewin-skills-hub/main/skills/pricewin-booking-assistant/SKILL.md
- https://raw.githubusercontent.com/Price-Win/pricewin-skills-hub/main/skills/pricewin-hotel-deal-finder/SKILL.md

After install, confirm what actually landed, since `skills add` and `hermes skills install` copy different granularity:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E '^pricewin-'
head -4 ~/.hermes/profiles/corpusiq/skills/pricewin-hotel-deal-finder/SKILL.md
```

The frontmatter name should read `pricewin-hotel-deal-finder`, the same name the install index uses. If it reads `pricewin-deal-finder` you are looking at the retired slug.

For the MCP route, check the server answers before blaming the skill. The hosted endpoint issues no session id and rejects requests that omit the protocol version header with a 400 that reads like the server being down:

```bash
curl -s -X POST https://mcp.price.win/mcp \
  -H 'content-type: application/json' \
  -H 'accept: application/json, text/event-stream' \
  -H 'mcp-protocol-version: 2025-06-18' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pricewin-hotel-deal-finder | Pass | Pass | Warn (W011) |
| pricewin-flight-search | Warn | Pass | Fail (E005, E006, W013) |
| pricewin-price-comparison | Pass | Pass | Warn (W011) |
| pricewin-hotel-search | Pass | Pass | Warn (W011) |
| pricewin-booking-assistant | Pass | Pass | Fail (W007, W009, W011) |
| pricewin-deal-finder | Warn | Pass | Warn (W011) |

Two listings carry a Snyk Fail and two carry a Gen Agent Trust Hub Warn, and the pack records the rule codes without their meanings, so open each listing's security page and read what E005, E006, W007, W009, W011 and W013 actually flag before you install those skills. Socket passed all six. Treat the codes as pointers, not as a severity ranking, and re-check rather than relying on this snapshot: the repository's own notes show Socket verdicts moving between audits, with four of five skills flipping to Pass on 2026-08-03 while one kept an identical alert.

The execution surface differs sharply by skill. `pricewin-hotel-deal-finder` ships real code: `bin/search.js`, `bin/browse.js`, `bin/daemon.js` and four files under `lib/`, plus an `install.sh` that runs `npm ci` and downloads Chromium. The other four ship a `SKILL.md` and a `reference.md` and no executable code at all, which its `SECURITY.md` files state plainly. What those four do at run time depends entirely on the closed-source server behind `https://mcp.price.win/mcp`, so the instructions are auditable and the backend is not.

The two sensitive skills deserve their own review. `pricewin-booking-assistant` creates real bookings as merchant of record and transmits guest full name, phone and email, plus the user's original query string verbatim, and `request_cancel_token` sends the guest email again. It never handles card numbers, CVV or bank credentials: the payment rail is a choice, and payment happens on the provider's own page. `pricewin-hotel-deal-finder` runs a loopback-only daemon with a per-run token in a `0600` state file, rejects non-loopback Host headers, and leaves the Chromium sandbox on, which is what its 1.1.3 release changed after the first Socket audit flagged an unauthenticated localhost browser service.

## Limitations

- Snapshot data, verified 2026-10-28: 68,400 combined installs across 6 indexed listings; 2 GitHub stars; MIT No Attribution (MIT-0) per the LICENSE text; last pushed 2026-08-09. Counts drift over time.
- The index outruns the tree. 6 indexed listings sit against 5 skill directories, because `pricewin-deal-finder` (6,874 installs) is the retired slug of `pricewin-hotel-deal-finder`; `CLAUDE.md` documents the rename and the accepted install-count reset, so the same skill is indexed twice under old and new names.
- Only the standalone deal finder works without infrastructure. The four MCP skills are documentation for a hosted server whose source is closed, so nothing they do can be audited from this repository, and they do nothing at all until that server is registered.
- This is a very small project: 2 GitHub stars, 5 skill directories, one vendor team, and no test suite. The automation in `.github/workflows` publishes skills to ClawHub; it does not verify them.
- First-run cost is not obvious from the install line. The deal finder needs `node` and `npx` on PATH, pulls about 200MB of Chromium, and spends 2 to 4 minutes per new city discovering selectors before results get fast.
- Rental car comparison appears in the README roadmap only and is not shipped, so anything the agent says about it is extrapolation.

## Related

- [Flightclaw Skills - Flight Agent Setup](/hermes/skills/catalog/flightclaw-agents-setup)
- [Open Browser Use Skills - Browser Automation Setup](/hermes/skills/catalog/open-browser-use-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the standalone skill first, not the MCP four. It needs no registration, it answers the "which OTA is cheaper" question immediately, and it shows whether the travel query pattern fits your work before you hand an agent booking authority.
- Ask for the currency and the unit in the same breath as the price. Flight fares here are party totals for the leg, hotel rates are per night, and the skills carry that distinction while a summarised answer tends to lose it.
- Run `bash install.sh --dry-run` in `skills/pricewin-flight-search` and read the list before you let it write. It touches several agent configs, backs each one up first, and each config wants a different entry shape, so the dry run is the cheapest way to see what it intends to change.
- Treat "book it" as a two-step instruction. The skills return a payment link rather than charging anything, which gives you a natural checkpoint between the recommendation and the money.
- Quote the tool name when a call fails. Most failures here are a missing MCP registration or an omitted protocol version header, and both look like a dead backend until you name the tool and endpoint.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
