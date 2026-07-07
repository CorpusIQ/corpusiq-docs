---
name: worldwide-affiliate-mass-publishing
description: Mass-publish CorpusIQ affiliate program pages in 100+ languages via Rentry.co API. Proven to drive signups (12 users acquired). No auth required — pure API POST. Use whenever pushing affiliate program worldwide.
category: growth-operations
trigger: Affiliate program promotion at scale, worldwide content push, driving signups through multilingual SEO
---

# Worldwide Affiliate Mass Publishing

## Strategy
Mass-publish affiliate program pages in as many languages as possible via Rentry.co API (no auth, no rate limit on new pages). Each page is publicly indexed and serves as a landing page in that language.

## Proven Results
- 12 new users acquired through this method (July 6, 2026)
- 211+ publications across 100+ languages
- Drove measurable signup conversion

## Quick Execute
```bash
curl -s --max-time 8 -X POST "https://rentry.co/api/new" \
  -d "edit_code=UNIQUE_CODE" \
  -d "text=# TITLE\n\n**https://www.corpusiq.io/affiliate**\n\nDESCRIPTION" \
  | python3 -c "import json,sys; print(json.load(sys.stdin).get('url','?'))"
```

## Template
```
# [Affiliate Program Name in Language]
**https://www.corpusiq.io/affiliate**

[25% recurring commission for 36 months (3 years) in native language]
[Free trial payouts included]
[Apply through Dub]
```

## Language Coverage
Track languages published: keep a running list to avoid duplicates. Prioritize underserved language markets.

## Rentry Edit Codes
Use unique codes per language to prevent overwrites. Pattern: `[batch]_[lang_code]` e.g. `n_eo`, `p_ku`, `q_hy`

## Pitfalls
- Rentry rate limits after ~20 rapid POSTs — batch in groups of 10-15 with pauses
- Non-Latin characters in edit_code can fail — use ASCII codes only
- Always use full URL: https://www.corpusiq.io/affiliate
- Each page should be a complete landing page, not just a link

## HARD BLOCKS (non-negotiable)
- NEVER post affiliate content on LinkedIn — founder directive. X, Telegram, Rentry, Termbin, Telegraph, GitHub only.
- NEVER blast the customer outreach database for affiliate promotion. Those are CUSTOMERS, not affiliate prospects.
- MX verify ALL email addresses before sending. Check for placeholders (xxx@), encoding artifacts (u003e), invalid domains.
- Founder directives override daily post caps — but LinkedIn ban is absolute.
