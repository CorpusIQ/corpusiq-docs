# Affiliate Link Attribution with Dub.co

## Why affiliate link tracking matters

CorpusIQ pays 25 percent recurring commission for 3 years. One referral at 99 dollars per month earns 891 dollars lifetime. The question is: which channels drive those referrals.

Generic links like `corpusiq.io/affiliate` give you zero attribution data. You do not know whether the click came from X, LinkedIn, Reddit, or a newsletter mention. That means you cannot double down on what works.

## What Dub.co solves

Dub is an open-source link attribution platform. It replaces your long affiliate URLs with branded short links and tracks every click through to conversion.

For CorpusIQ specifically, Dub enables:

- **Channel-level attribution**: create separate short links for X, LinkedIn, email, Reddit, Discord, and your newsletter. Every click is tagged with its source.
- **Geographic analytics**: see which countries and cities your affiliate traffic comes from.
- **Device breakdown**: know whether your audience clicks on mobile, desktop, or tablet.
- **Conversion tracking**: when paired with a conversion pixel, Dub tracks the full click-to-signup funnel.
- **QR codes**: generate QR codes for physical events, conference booths, or business cards.
- **Branded domains**: use your own domain instead of a generic shortener.

## Setting up Dub for CorpusIQ affiliate links

Create a Dub workspace at dub.co. Add your domain or use the default dub.sh domain.

For each promotion channel, create a unique link:

| Channel | Link | Target |
|---------|------|--------|
| X/Twitter | dub.sh/corpusiq-x | whop.com/joined/corpusiq?utm_source=x |
| LinkedIn | dub.sh/corpusiq-li | whop.com/joined/corpusiq?utm_source=linkedin |
| Reddit | dub.sh/corpusiq-reddit | whop.com/joined/corpusiq?utm_source=reddit |
| Email outreach | dub.sh/corpusiq-email | whop.com/joined/corpusiq?utm_source=email |
| GitHub | dub.sh/corpusiq-gh | whop.com/joined/corpusiq?utm_source=github |

Every click is then tracked independently. At the end of the month, you know exactly which channel delivered.

## API-first approach

Dub provides a full REST API for programmatic link creation:

```
POST https://api.dub.co/links
{
  "url": "https://whop.com/joined/corpusiq",
  "key": "corpusiq-x",
  "utm_source": "x",
  "utm_medium": "social",
  "utm_campaign": "affiliate-aug2026"
}
```

This means Hermes can create attribution links automatically for every new promotion channel without manual dashboard work.

## Dub's own affiliate program

Dub also runs an affiliate program at dub.co/affiliates. Promoting Dub alongside CorpusIQ creates a natural pairing: Dub tracks the links, CorpusIQ provides the business intelligence layer behind them.

The overlap is not competitive. It is complementary. Dub handles attribution. CorpusIQ handles business answers across 40-plus data sources.
