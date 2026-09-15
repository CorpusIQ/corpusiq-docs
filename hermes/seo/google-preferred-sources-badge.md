---
title: Google Preferred Sources Badge - Get Cited in AI Overviews
description: "How the Google Preferred Sources badge works and how to add it to your site in two lines of code. Get a preferred badge in AI Overviews, AI Mode, and Top Stories."
last_updated: 2026-08-25
canonical: "https://www.corpusiq.io/docs/hermes/seo/google-preferred-sources-badge/"
robots: "index,follow"
tags: ["geo", "aeo", "seo", "ai overviews", "google search"]

---

# Google Preferred Sources Badge

Google lets readers mark a site as a preferred source. Once a reader picks your site, your content can show a "preferred" badge in AI Overviews, AI Mode, Top Stories, and Google Discover.

This page explains what the feature is, why it matters for AI-era search, and how to add it to any site in two lines of code.

## What is a preferred source?

Preferred sources is a Google Search feature. Users select the sites they trust in Google's source preferences tool. After that, content from those sites is more likely to appear in:

- AI Overviews and AI Mode, highlighted with a preferred badge
- Top Stories, with a preferred badge
- Google Discover

It is a reader-driven signal. The reader chooses, and Google surfaces more of your content for that reader.

## Why it matters for AEO and GEO

Answer engines and generative engines cite sources they can trust. A preferred badge does two things:

1. It puts your site in front of readers who already trust you, in the exact surfaces where AI answers appear.
2. It signals to Google that real users actively select your content.

For business tools sites, this targets the same surfaces as AEO and GEO work: AI Overviews, AI Mode, and conversational search.

## Eligibility

Only domain-level and subdomain-level sites are eligible. Subdirectory paths are not.

- Eligible: `https://example.com`, `https://code.example.com`
- Not eligible: `https://example.com/blog`

## Implementation (standard, recommended)

Two lines. Add the library script to the head:

```html
<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
```

Add the button where you want it in the body:

```html
<div google-add-preferred-source-btn></div>
```

That is it. The button is auto-localized and Google-styled.

### Dark theme

```html
<div google-add-preferred-source-btn data-theme="dark"></div>
```

### Language override

```html
<div google-add-preferred-source-btn data-lang="en"></div>
```

## Deeplink (no code)

For social posts, newsletters, and emails, use the deeplink format:

```
https://www.google.com/preferences/source?q=https://yourdomain.com
```

Readers click, add your site, and get returned to your page.

## Advanced usage

For custom UI, the library also ships as an ES module with a programmatic API:

```javascript
import { preferredSource } from "https://news.google.com/swg/js/v1/publisher.mjs";

preferredSource.init({ theme: "dark", lang: "en" });
```

Or bind to any click handler:

```javascript
button.onclick = () => { preferredSource.addPreferredSource(); };
```

## Official docs

- Google Search Central guide: https://developers.google.com/search/docs/appearance/preferred-sources
- Source preferences tool: https://www.google.com/preferences/source

*← [SEO Pages](/docs/hermes/seo) | [Hermes Home](/docs/hermes)*
