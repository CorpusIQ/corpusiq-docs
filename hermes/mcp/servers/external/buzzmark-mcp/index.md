---
title: "Buzzmark MCP - Brand-Voice Social Drafts With a Voice Score"
description: "A ghostwriter server that reads the operator's own website first, writes posts in that voice per network, scores how much each draft sounds like the brand and refuses to publish without a calendar step."
category: Marketing / Content Operations
stars: n/a (commercial, free trial, hosted)
added: 2026-10-25
source: "mcp.so /feed card (submitted 2026-10-25) + mcpservers.org listing + live 401 probe on the endpoint + vendor pricing page"
relevance: ★★
tags: [social-media, content, brand-voice, ghostwriting, scheduling, linkedin, x, instagram, drafts]
---

# Buzzmark MCP

**Drafts that sound like the business, not like an AI.** Point it at a website and it writes in that voice, gives every post a version for each network, scores how much the draft sounds like the brand, then puts it on a calendar instead of on the internet.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://buzzmark.ai/mcp
Auth:        OAuth, no key pasted by hand (unauthenticated initialize returns 401 invalid_token)
Tools:       21
Registry:    ai.buzzmark/mcp 1.0.0
Built by:    Buzzmark, Piik Labs AB (buzzmark.ai)
```

## Why This Matters for Operators

The content problem for a small business is not publishing. Publishing has been solved a dozen times over, and this catalog already carries UniPost, ViewsBase, Chirpie, PendPost, Postkey, FeedSquad and Sendcove for it.

The unsolved part is that a machine-written post reads like a machine wrote it, and the operator can feel it even when they cannot name it. So they rewrite, which costs more time than writing it themselves would have, and the tool gets abandoned.

Buzzmark attacks that specific failure. It reads the website before it writes, keeps a separate profile for the founder's voice and the company's voice, and returns a score for how close the draft sits to the brand. That score is the difference between a text generation feature and a feedback loop: the operator can reject a 62 and accept a 91 without rewriting either.

## What It Actually Does

Probed live in this sweep: unauthenticated `POST initialize` to `https://buzzmark.ai/mcp` returned HTTP 401 `{"error":"invalid_token","error_description":"No authorization provided"}`, so the endpoint is real, hosted and OAuth-gated. No account was created, so no tool call was executed; the surface below is read from the vendor's published listing and registry entry rather than a handshake.

The twenty-one tools group into four jobs.

| Group | Tools seen | What they do |
|---|---|---|
| Structure | `list_social_sets` and the brand-profile readers | A social set is a group of connected accounts with its own brand profile, time zone and weekly posting slots; most other tools take a `social_set_id` from here |
| Writing | the Buzz writer, `save_draft`, `save_as_drafts` | One to five posts from an idea, in a brand profile's voice, checked against the platform's own limits (length, missing picture) and against Buzzmark's writing rules before the operator sees it |
| Assets and planning | `create_image`, `create_weekly_content_plan` | A picture per post, and a week planned around the account's best posting times |
| Scheduling | `schedule_post`, `schedule_posts`, `get_post` | Schedule onto the Buzzmark calendar, and read one post in full with its thread parts, images, target accounts, status and time |

The behaviour that matters is the one the vendor states plainly: nothing goes out on the spot. A scheduled post lands on the calendar where it can be changed or removed first, which makes the agent a drafting colleague rather than a publishing credential.

## Installation

```
claude mcp add buzzmark --transport http https://buzzmark.ai/mcp
```

Any other MCP client adds `https://buzzmark.ai/mcp` as a remote Streamable HTTP server and completes the OAuth flow when prompted. No key is copied by hand.

## Business Relevance

Six networks from one idea, each in the right shape rather than the same paragraph cross-posted. For a founder who posts in their own name and a marketing lead who posts for the company, the two profiles are the useful part: the founder's voice is not the brand's voice, and mixing them is why founder accounts read like press releases.

The voice score is a measurable acceptance test, and that is rarer than it should be in this category. Most writing tools ask the operator to judge. This one proposes a number first.

## Integration with CorpusIQ

The pairing is ask, then draft. A question answered against the operator's connected data becomes the raw material for a post, and the operator keeps the judgement about whether the sentence is theirs. It is also the shortest route this catalog carries from a business fact to a scheduled post that still sounds like the business.

## Limitations

- No tool call was possible without an account, named here as the gap. `initialize` was refused with 401 before any handshake, so the twenty-one tools are documented, not driven.
- The class is dense on the publishing side. UniPost, ViewsBase, Chirpie, PendPost, Postkey, FeedSquad and Sendcove already carry multi-network posting, several with approval gates. Buzzmark is catalogued for the generation side, voice matching and the score, not for publishing breadth; if the question is "can I post to fourteen networks", the carried tools answer it better.
- The listing's setup command points at `https://buzzmark.ai/mcp` while `buzzmark.ai/docs/mcp` returns 404, so the tool reference lives in the mcpservers.org and mcp.so listing rather than in a stable vendor document. A tool reference that moves is a tool reference that will drift.
- Pricing is per brand, per channel and per volume of writing, not per seat: $29 a month (50 Buzz, 20 images, 3 Scout runs), $49 a month or $36.75 for the first 12 months (200 Buzz, 300 images, 15 Scout), $99 a month or $74.25 for the first 12 months (500 Buzz, 500 images, 60 Scout), each with a trial that charges nothing today. The listing does not state which tier includes MCP access.
- Text returned in post listings is cut at 400 characters; the full thread only comes back from the single-post tool, which is a trap for anything that lists before it reads.
- Nothing in the surface proves the voice score is stable between runs, and no call was made to test it.

## FAQ

### Does it publish on its own?

Not on the spot. Scheduled posts land on the Buzzmark calendar first, where the operator can change or remove them.

### How does it learn the voice?

It reads the operator's website first, then keeps learning from published posts and from the way the operator edits its drafts.

### What are "Buzz" and "Scout"?

Buzz is the unit of written posts per month; Scout runs are the research passes over the operator's sector news that feed the ideas.

### Which networks does it cover?

Instagram, LinkedIn, Facebook, X, Threads and TikTok, one version per network rather than one paragraph repeated.

## See Also

- [UniPost MCP - LinkedIn and X Publishing With Approval](/hermes/mcp/servers/external/unipost-mcp/)
- [PendPost MCP - Local-First Social Publishing with Approval](/hermes/mcp/servers/external/pendpost-mcp/)
- [Chirpie MCP - Unified Social Posting Across 14 Platforms](/hermes/mcp/servers/external/chirpie-mcp/)
