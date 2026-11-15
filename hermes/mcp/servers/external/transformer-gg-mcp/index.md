---
title: "Transformer.gg MCP - Sponsored X Post Value"
description: "A one-tool keyless MCP server that prices a sponsored X post from a published follower curve, and says plainly it is an estimate, not an offer."
category: "Marketing / Influencer Pricing"
stars: "0 (one tool, hosted, keyless public tier)"
added: 2026-11-14
source: "the mcpservers.org canonical, which listed transformer-gg as a new key on 2026-11-14, the mcp.so submission queue entry #7363 filed 2026-11-14T22:50Z, and a driven session against https://transformer.gg/mcp/public on 2026-11-14 in which initialize answered 200 as transformer-public and the tool was called eleven times"
relevance: ★★★
tags: [influencer-marketing, creator-economy, x-twitter, rate-card, budgeting, keyless, remote-mcp]
last_updated: "2026-11-14"
---

# Transformer.gg MCP

**The first number in every sponsored post negotiation is invented by whoever speaks first.** A brand asks what a post costs and the creator quotes a figure from memory, or from a rate card they set two years ago; the brand counters with a figure from a spreadsheet a previous colleague built. Neither number has a source, and both sides know it, which is why the negotiation takes three weeks and lands somewhere unrelated to either opening figure.

Transformer's MCP server answers with a number and then explains, in the same response, that it is an estimate from a published curve and not what any brand has paid. That honesty is unusual enough to be the reason this server is catalogued despite carrying exactly one tool: an estimate that names its own method is usable in a budget, and an estimate that does not is a rumour.

```
Server type:   remote Streamable HTTP, JSON-RPC 2.0
Endpoint:      https://transformer.gg/mcp/public   (keyless public tier)
               https://transformer.gg/mcp          (authenticated tier)
Server:        transformer-public, version 882fd0e
Website:       https://transformer.gg/
Source:        https://github.com/NBV-AppFactory/transformer-mcp
Registry:      gg.transformer/transformer
Auth:          none on the /public path
Tools:         1 (get_influencer_value)
Listed on:     mcpservers.org as transformer-gg, mcp.so queue #7363
```

## The evidence tier

Driven. The public endpoint answered `initialize` **200** with server name `transformer-public` and a single tool, and that tool was called eleven times across five handles, one malformed argument and one account that does not exist. Every figure below is a live response.

## What the tool returns

`get_influencer_value` takes one argument, `handle`, a string of 1 to 40 characters in the shape `jane_doe` or `@jane_doe`, and returns a structured object rather than prose:

```
{
  "handle": "levelsio",
  "value": { "lowUsd": 9050, "highUsd": 13600, "usualUsd": 11325,
             "currency": "USD", "per": "one sponsored X post",
             "source": "Transformer's estimate" },
  "followerBand": "500k-1M",
  "method": "Our estimate from the account's follower count on Transformer's
             published curve ($50 a post at 1k followers, $1,200 at 100k,
             $10,000 at 1M, $25,000 at 5M+), adjusted gently (0.75x to 1.35x)
             for its views and engagement where we have them, shown as a range.",
  "url": "https://transformer.gg/value/levelsio",
  "note": "An estimate shown as a range; not an offer and not what brands have paid."
}
```

Four handles, four answers:

| Handle | Band | Low | Usual | High |
|---|---|---|---|---|
| `levelsio` | 500k-1M | $9,050 | $11,325 | $13,600 |
| `a16z` | 1M-5M | $9,750 | $12,175 | $14,600 |
| `naval` | 1M-5M | $20,650 | $25,825 | $31,000 |
| `elonmusk` | 5M+ | $19,950 | $24,925 | $29,900 |

The published curve is the useful part of the response, because it lets a buyer sanity-check any number the tool produces: **$50 a post at 1,000 followers, $1,200 at 100,000, $10,000 at 1,000,000 and $25,000 at 5,000,000 or more**, with a 0.75 to 1.35 multiplier for views and engagement where it has them.

## The arithmetic controls

Two properties of the response were reproduced by hand, and one of them exposed something worth knowing before quoting the figures.

**The "usual" value is the exact midpoint of the range.** In all four rows, low plus high divided by two gives the usual figure to the dollar: 9,050 and 13,600 average to **11,325**; 19,950 and 29,900 to **24,925**; 9,750 and 14,600 to **12,175**; 20,650 and 31,000 to **25,825**. So the three numbers are one number and a width, not three independent measurements, and a buyer who treats "usual" as a modal price is reading a midpoint.

**The range width is a fixed 1.5x, whatever the account.** 13,600 / 9,050 is 1.503, 29,900 / 19,950 is 1.499, 14,600 / 9,750 is 1.497, 31,000 / 20,650 is 1.501. Every range is within a rounding of 1.5 times its own floor, which is narrower than the 0.75 to 1.35 multiplier window the method paragraph describes (that window spans 1.8x). The published method is a shape, not a formula you can run, because the inputs it claims to use (views, engagement) are not returned in the response.

**The band is not the price.** The most consequential observation of the pass sits in the table above: `a16z` and `naval` are in the same 1M-5M band and price at **$12,175** and **$25,825**, a factor of 2.1 apart, while `levelsio` in the smaller 500k-1M band prices at **$11,325**, only 7% below the larger band's cheaper account. Whatever the multiplier is reading, it is doing more work than the follower band, and it is not visible to the caller. That is not a defect in the answer; it is the reason to use the range as a negotiation bracket rather than the midpoint as a rate.

## The defect this pass is recording

**A handle that does not exist is reported as a malformed handle.** Two calls returned `isError` true with the same sentence: *That isn't an X handle like @jane. [bad_handle]*. One of them was genuinely malformed (`@nostr:invalid handle!!`), and the other was `thisuserdoesnotexist_zzq9921`, a syntactically valid 24 character handle for an account that does not exist. The tool cannot tell the two apart, or does not distinguish them in the message, so an assistant asked about a mistyped or deleted account will tell the user their handle is malformed. When that message appears, check the spelling before rewriting the handle.

## Where this fits, and where it does not

- **It prices one format on one platform.** One sponsored X post. A thread, a video, a LinkedIn post or an Instagram reel is outside the surface, and a creator whose audience lives elsewhere is not represented.
- **It is an estimate from a curve, and the vendor says so in the payload as well as on the page.** No response here should be quoted to a creator as an offer.
- **Following counts move and the tool has no as-of date.** The `url` field is a live page rather than a snapshot, and no timestamp appears in the response, so two calls a month apart cannot be proven comparable. Record the date yourself when a figure goes into a budget.
- **The authenticated tier was not measured.** `https://transformer.gg/mcp` is the documented path for a key or account; only the `/public` tier was driven here, and this guide describes nothing beyond it.
- **One tool is a small surface.** What earns the entry is the data behind it and the method note, not breadth. A team that needs discovery or analytics should look at the creator-discovery and influencer-analytics entries in this catalog instead.

## Frequently asked

### What does one sponsored X post on a large account cost, per this tool?

At the 1M to 5M band it returns between roughly $9,750 and $31,000 depending on the account, with the two accounts sampled there landing at $12,175 and $25,825. At 500k to 1M, `levelsio` came back at $11,325 as the midpoint of a $9,050 to $13,600 range.

### Is this what creators actually get paid?

No, and the response says so in its own `note` field: *An estimate shown as a range; not an offer and not what brands have paid.* It is a starting bracket for a negotiation, derived from follower count and adjusted for engagement.

### How does it decide the number?

From a published curve anchored at $50 a post for 1,000 followers, $1,200 at 100,000, $10,000 at 1,000,000 and $25,000 at 5,000,000 or more, adjusted by 0.75x to 1.35x for views and engagement where it has them. The adjustments themselves are not returned, which is why two accounts in one band can differ by a factor of two.

### Does it need an API key or an account?

Not on the public path. `initialize` and every call in this pass answered 200 on `https://transformer.gg/mcp/public` with no credential. The `/mcp` path is the authenticated tier and was not measured here.

### What should I do with a malformed handle error?

Check the spelling before changing the handle. A valid handle for an account that does not exist returns the same message as a syntactically broken one, so the error is a weak signal about which problem you have.

## What to check before you quote it

1. Record the date of the call. No as-of timestamp comes back, so the figure is only defensible with the date you captured it.
2. Use the range as a bracket and the midpoint as a starting position, not as a rate.
3. Compare two accounts inside the same band before assuming the band sets the price. It does not.
4. Treat a handle that returns `bad_handle` as possibly a typo, not necessarily a syntax error.
5. Keep the vendor's own sentence in whatever goes to a creator: an estimate, not an offer.
