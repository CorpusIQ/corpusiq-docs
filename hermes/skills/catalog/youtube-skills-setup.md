---
title: "YouTube Skills - Transcript API Suite for Agents"
description: "zeropointrepo/youtube-skills: 11.2K combined installs. Twelve MIT skills for YouTube transcripts, search, channels and playlists via TranscriptAPI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/youtube-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "youtube", "transcripts", "video search", "media"]
---

# YouTube Skills - Setup Guide

**Source:** [zeropointrepo/youtube-skills](https://www.skills.sh/zeropointrepo/youtube-skills) via skills.sh - 11.2K combined installs across 12 indexed listings; first documented 2026-11-02 (evening sweep)

**GitHub:** [zeropointrepo/youtube-skills](https://github.com/zeropointrepo/youtube-skills) - 1,159 stars, MIT, branch main, last pushed 2026-10-27; 12 skill directories under `skills/` and the same 12 names mirrored under `clawhub/`, each skill carrying a `SKILL.md` plus `references/auth-setup.md` and `references/curl-examples.md`

**Category:** YouTube transcripts, search, channel and playlist data for agents, delivered as HTTP calls to a hosted API

**Quality Tier:** 🟡 Yellow - Socket fails two of the three sampled listings and Snyk warns on all three, although the repository ships Markdown only and every skill is a thin wrapper over one documented HTTP API

YouTube Skills is published by Zero Point Studio, the team behind TranscriptAPI, and it exists to remove the usual transcript plumbing from an agent's path. The README is direct about the problem it solves: no yt-dlp, no headless browser, no binaries, because YouTube blocks most cloud IP addresses and the scraping routes break in exactly the environments agents run in. Instead the skills document a small set of endpoints on transcriptapi.com, and the agent calls them with an API key.

The repository carries twelve skills, but they are deliberately redundant. The README says so in its own words: many are narrower variants or aliases of the core five, so the agent can find a matching skill regardless of how a request is phrased. `youtube-full` is the one the README recommends, covering transcripts, search, channels, playlists and within-channel search in a single file of 293 lines, with `yt`, `transcript`, `captions`, `subtitles`, `youtube-search`, `youtube-channels`, `youtube-playlist`, `youtube-data`, `youtube-api`, `transcriptapi` and `video-transcript` as the narrower entries around it.

## Installation

The README documents four install routes. For Hermes Agent it gives an explicit command rather than the generic CLI path:

```bash
hermes skills install skills-sh/ZeroPointRepo/youtube-skills/skills/youtube-full
```

The skills.sh CLI route works per skill or across all twelve:

```bash
npx skills add ZeroPointRepo/youtube-skills --skill youtube-full
npx skills add ZeroPointRepo/youtube-skills
```

OpenClaw users get a separate registry command, and the manual route is a clone plus a copy:

```bash
npx clawhub@latest install youtube-full

git clone https://github.com/ZeroPointRepo/youtube-skills.git
cp -r youtube-skills/skills/youtube-full ~/.claude/skills/
```

Copy the whole skill directory, not only `SKILL.md`. Every one of the twelve points at `references/auth-setup.md` for credential setup and at `references/curl-examples.md` for ready-to-run requests, and the skill text opens with an instruction to read the auth page when `$TRANSCRIPT_API_KEY` is unset.

The key itself is the one external dependency. The README says the first run sets it up interactively: the agent asks for an email address, registers it with TranscriptAPI, the user enters the OTP that arrives by mail, and the key is then saved to the shell and agent config. The manual alternative is signing up at transcriptapi.com and copying a key that starts with `sk_`. The free tier is 100 credits with no card, and most endpoints cost one credit, with `channel/resolve`, `channel/latest` and the transcript `info` endpoint listed as free.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| youtube-full | 2,249 | Everything in one skill: transcripts, video and channel search, channel browsing, playlists, within-channel search, triggered by pasted links, video IDs, @handles or topic research. |
| youtube-search | 1,008 | Finding videos or channels on a topic, discovering creators, tutorials and talks, and looking up a channel by name or handle. |
| video-transcript | 913 | Turning a pasted video link or ID into text: transcribe, summarize, quote, translate, extract. |
| transcriptapi | 852 | The widest endpoint surface in the set, for transcripts plus video and channel work. |
| transcript | 837 | The spoken content of one video: summarize, quote, transcribe, translate, fact-check. |
| subtitles | 829 | Timestamped subtitles for translation, read-along, language learning and accessibility work. |
| youtube-api | 798 | YouTube data without Google quotas or OAuth: transcripts, metadata, channel info, search results, playlists. |
| youtube-channels | 766 | Channel-first work: browse uploads, see recent posts, search inside a channel, resolve a handle to a channel ID. |
| captions | 745 | Timestamped caption data for quoting, translation and deaf or hard-of-hearing use cases. |
| youtube-data | 734 | Structured data for analysis: metadata, upload history, search results and playlist contents with no OAuth. |
| youtube-playlist | 732 | Listing and working through a playlist for transcripts or research, including course and series collections. |
| yt | 713 | Quick lookups: latest uploads, a fast summary, a topic search. |

All 12 indexed listings clear the threshold and appear in the table above.

The substance sits in `youtube-full`. It documents a transcript endpoint that takes a URL or an 11-character ID and returns either JSON with per-line `text`, `start` and `duration` or a flat text body with timestamps; a search endpoint with `type` of `video`, `channel`, `playlist` or `movie`, plus first-page filters for `sort`, `upload_date`, `duration` and `features`; channel endpoints for handle resolution, latest uploads, the videos, shorts and streams tabs with `sort` and continuation paging, channel search, profile, playlists, community posts and curated sections; and playlist pagination over `PL`, `UU`, `LL`, `FL` and `OL` prefixes. It closes with a credit table per endpoint, a validation table, an error table mapping 401, 402, 403/1010, 404, 408, 422 and 429 to an action, and two worked workflows.

One header detail is worth repeating because it fails loudly: every request needs both an `Authorization: Bearer` header and a `User-Agent` naming the agent. The skill states that omitting the user agent or sending a bare default gets a Cloudflare 403 with error code 1010. The example values in the files are written as `HermesAgent/0.11.0` and `YourAgent/1.0`, which is the shape the API expects.

## Why This Matters for Hermes Agents

Transcript access is the difference between an agent that can talk about a video and one that can only guess from a title. The usual alternatives are a Python dependency on yt-dlp or a browser automation pass, and both fail from cloud IP ranges in ways that look like the video does not exist. This suite replaces that with an HTTP call and an API key, which is the only class of dependency an agent can install, debug and cost-account on its own.

The cost model is unusually legible for a media tool. Credits are per endpoint and printed in the skill: one credit for a transcript, one per page of search or channel videos, one per page of playlist contents, and free for handle resolution, the latest-uploads feed and the transcript info call. An agent that checks a channel's newest uploads before deciding what to transcribe spends nothing on the discovery step, and the skill documents that sequence as its channel-monitoring workflow.

The failure modes are documented rather than left to be discovered. A 402 means the account is out of credits, not that the video is private. A 403 with code 1010 means the user agent header, not the key. A 404 means no captions exist for that video. Teaching an agent those three distinctions is worth more than any amount of retry logic, because each one resolves to a different action: top up, fix a header, or move on.

For builders, the twelve-skill design is a deliberate hedge against trigger phrasing. An agent that only knows `youtube-full` may still decline a request phrased as "read the captions in Spanish", while one that also holds `captions` and `subtitles` will match. The README states this plainly, and it is a pattern worth copying when the skill router, rather than the model, is doing the matching.

## Usage

| You say | What happens |
|---|---|
| "Summarize this video: https://youtube.com/watch?v=..." | Calls the transcript endpoint with `format=json&include_timestamp=true&send_metadata=true`, then summarizes from the timestamped lines. |
| "Find the five most viewed talks on this topic from the past month" | Calls search with `type=video`, `sort=views`, `upload_date=month` and `limit=5`, then reads the transcripts of the picks. |
| "What has TED posted this week?" | Uses the free `channel/latest` call with `channel=@TED`, which returns the 15 newest items with exact view counts and ISO timestamps. |
| "Search the TED channel for artificial intelligence" | Calls `channel/search` with the handle and query, at one credit per call. |
| "List every video in this playlist" | Calls `playlist/videos` with the playlist URL or ID and follows `continuation_token` while `has_more` is true, one credit per page. |
| "Give me the clean text of this video for language practice" | Uses the captions or subtitles skill, which documents fetching clean text without timestamps and reads the response `language` field. |
| "Transcribe this channel's whole back catalogue" | Walks `channel/videos` page by page at one credit per page, then transcribes each ID, and the credit table lets it price the job before starting. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/ZeroPointRepo/youtube-skills/main/skills/youtube-full/SKILL.md
```

After a clone, confirm the references came with the skill and that the two trees really do hold twelve skills each:

```bash
git clone --depth 1 https://github.com/ZeroPointRepo/youtube-skills.git /tmp/yt-skills
ls -d /tmp/yt-skills/skills/*/ | wc -l
ls -d /tmp/yt-skills/clawhub/*/ | wc -l
head -3 /tmp/yt-skills/skills/youtube-full/SKILL.md
```

Both counts should print 12, and `head` should show `name: youtube-full` followed by the description the runtime routes on. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/youtube-full/references
grep -n 'TRANSCRIPT_API_KEY' ~/.hermes/profiles/corpusiq/skills/youtube-full/SKILL.md | head -3
```

The reference listing should show `auth-setup.md` and `curl-examples.md`, and the grep should show the required environment variable block. If the references are missing, the skill will still load and then fail at the first request.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| youtube-full | Pass | Pass | Warn |
| youtube-search | Warn | Fail | Warn |
| video-transcript | Warn | Fail | Warn |

The sampled verdicts are the reason this guide is yellow rather than green. Two of the three listings carry a Socket fail and a Gen Agent Trust Hub warn, and all three carry a Snyk warn. The repository itself contains no executable code: 24 `SKILL.md` files across the two trees, 24 reference files, a `plugin.json`, a `SECURITY.md`, a `CONTRIBUTING.md` and an assets folder. There is no install script, no hook and no dependency, so nothing runs when a skill loads beyond reading Markdown.

What the skills do carry is an instruction to send data to a third party. Every endpoint is on transcriptapi.com, every request needs a bearer key, and the returned text is video content plus metadata. Treat the API key as a secret in the ordinary way, keep it in the shell environment rather than in a skill file, and read the `SECURITY.md`, which asks that reports go to hello@transcriptapi.com rather than a public issue and states that the repository's scope covers the skill definitions and the interaction patterns they instruct.

The publisher is explicit that TranscriptAPI is an independent service, not affiliated with, endorsed by or sponsored by YouTube or Google. That is a compliance statement as much as a legal one: this suite reads public YouTube data through a third-party proxy, so check that the use you have in mind is one you are comfortable with before wiring it into a production agent.

## Limitations

- Snapshot data, verified 2026-11-02: 11,176 combined installs across 12 indexed listings; 1,159 GitHub stars; MIT; last pushed 2026-10-27. Counts drift over time.
- The repository holds the same 12 skills twice, once under `skills/` and once under `clawhub/`. The two copies are not byte-identical: the clawhub variants use a different metadata line and a different example format, with `curl` one-liners in place of the `http` blocks. Install from `skills/`, which is the tree the README and the Hermes command both point at.
- Every skill needs a `TRANSCRIPT_API_KEY` and a paid-credit account to do real work. The free tier is 100 credits; sustained transcript work consumes them at one credit per transcript and one per page of any listing.
- The twelve skills overlap heavily by design. Two of them, `youtube-full` and `transcriptapi`, describe nearly the same surface, and an agent holding several may pick a narrower one than the task needs.
- Two of the three sampled listings fail the Socket audit. The fail reasons are not visible in the pack, so check the security pages on skills.sh before installing into a production profile.
- All data comes from a third-party service that is not affiliated with YouTube or Google, and the README's no-yt-dlp claim describes the agent-side dependency, not the upstream reliability.

## Related

- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Youtube Content Setup](/hermes/skills/catalog/youtube-content-setup)
- [Skills Collective AI Media - Image & Video Gen Setup](/hermes/skills/catalog/skills-collective-ai-media-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `youtube-full` first and add the narrower skills only when a phrasing keeps missing. The README recommends exactly that, and one 293-line skill is easier to keep in context than twelve overlapping ones.
- Send the `User-Agent` header every time. The 403 with code 1010 is the single most likely failure and the fix is a header, not a key.
- Spend the free calls first. Resolve a handle, read `channel/latest` and call `info` before spending credits, then transcribe only the items you have chosen.
- Price the job before you run it. The credit table lets an agent say "this back catalogue is 40 pages, so 40 credits plus one per transcript" instead of discovering the limit halfway through.
- Paging requires repeating the filters. On `channel/videos`, send the same `sort` on every follow-up request, because the continuation token is tied to the tab and ordering you started with.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
