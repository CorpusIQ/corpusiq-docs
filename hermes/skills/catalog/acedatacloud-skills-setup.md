---
title: "AceDataCloud Skills - Hosted AI API Suite"
description: "acedatacloud/skills on skills.sh: 19.4K combined installs across 124 listings; hosted AI music, image, video, chat and cloud-ops skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/acedatacloud-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "ai video", "image generation", "api integrations"]
---

# AceDataCloud Skills - Setup Guide

**Source:** [acedatacloud/skills](https://www.skills.sh/acedatacloud/skills) via skills.sh - 19.4K combined installs across 124 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 17 stars, licence NOASSERTION, last pushed 2026-11-03, 122 SKILL.md directories spread across skills/, claude-plugins/ and platforms/amp/skills/
**Category:** Hosted AI APIs for agents: music, image and video generation, chat, web search, mail, social publishing and Tencent Cloud operations through one AceDataCloud account
**Quality Tier:** 🟡 Beta - Snyk Warns on the fish-audio and microsoft-outlook samples; GitHub licence NOASSERTION.

AceDataCloud publishes one agent skill per API surface rather than one skill per vendor. The catalogue covers generative media (Suno, Producer, Veo, Kling, Wan, Hailuo, Seedance, Luma, Flux, Seedream, Nano Banana, gpt-image-2), productivity connectors (Gmail, Outlook, Calendar, Drive, OneDrive, Notion, Slack, GitHub, GitLab), publishing targets (Substack, dev.to, Blogger, LinkedIn, Reddit, Zhihu, WeChat) and Tencent Cloud operations (CLS, DNSPod, TKE, EdgeOne, COS).

Every skill calls the same platform, so a single AceDataCloud account and key pair covers the set. The README's first-run table sends you to one service at a time, which is the intended install shape: the skills are small individually and broad in aggregate.

## Installation

The README's recommended path installs a single skill into a coding agent through the skills CLI:

```bash
npx --yes skills@1.7.2 add acedatacloud/skills --skill suno-music -a codex --yes
npx --yes skills@1.7.2 list
```

Replace `codex` with another supported agent such as `claude-code` or `cursor`. For Codex the files land in `.agents/skills/suno-music/`, and a fresh assistant session is needed to pick them up. No ClawHub account, OpenClaw install or paired MCP server is required on this path, and installation by itself generates no media.

The ClawHub route uses shorter package names than the repo folder names:

```bash
npm install -g clawhub
clawhub install @acedatacloud/suno
clawhub list
```

`@acedatacloud/suno` maps to `skills/suno-music`, and `@acedatacloud/nano-banana` maps to `skills/nano-banana-image`.

Credentials are the part that trips people up. Generation calls read `ACEDATACLOUD_API_TOKEN`; account resources such as balance read the separate `ACEDATACLOUD_PLATFORM_TOKEN`; the optional `acedatacloud` account skill reads the public catalog and pricing with no key at all. A skill cannot create an environment variable or load a `.env` file itself, so set the token in your agent's environment or secret store before the first call, and never paste a key into a prompt.

## What It Provides

45 listings clear the 200-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| fish-audio | 4,136 | Text-to-speech, saved voice lookup, persistent public voice models and one-shot cloning from an HTTPS audio URL plus its transcript |
| suno-music | 277 | Suno song and instrumental generation, lyrics, availability checks, track extension, covers and multitrack Studio project edits |
| microsoft-outlook | 262 | Outlook and Microsoft 365 mail and calendar through Microsoft Graph: reading, searching, drafting, sending, replying and scheduling |
| wechat-official-account | 249 | Official Account articles, drafts, publishing, customer-service messages, menus and stats through the WeChat MP server-side API |
| luma-video | 245 | Luma Dream Machine text-to-video, image-to-video and video extension |
| veo-video | 235 | Google Veo 3 and 3.1 text-to-video, still-image animation, reference blending and 1080p upscaling |
| seedance-video | 234 | Seedance 2.0 and 2.5 text-to-video, image-to-video, multimodal references, editing and extension |
| kling-video | 234 | Kling generation plus Turbo, storyboards, motion control, talking photos, lip sync, product studio and commercial voiceovers |
| wan-video | 232 | Wan text-to-video, image-to-video, reference transfer, 480P to 1080P output and optional audio |
| flux-image | 232 | Flux image generation and text-instruction editing, plus FLUX 3 video |
| seedream-image | 229 | Seedream 5.0 text-to-image, reference-image editing, related image sets, transparent-background edits and editable layer extraction |
| hailuo-video | 229 | Hailuo (MiniMax) text-to-video and image-to-video with director mode |
| producer-music | 228 | Producer song and lyric generation, track extension, covers, vocal and instrumental swaps, section replacement and reference audio upload |
| sora-video | 227 | Explains the retired Sora integration and helps migrate existing workflows; the service is not in the public API catalog |
| google-search | 226 | Google web, image, news, maps, local place and video search with localization, time filtering and pagination |
| tencentcloud-cos | 225 | COS bucket and object work: list buckets and objects, upload, download, delete, pre-signed URLs and bucket size |
| nano-banana-image | 224 | Nano Banana, Nano Banana 2.1 and Pro generation and reference-image editing at 1K, 2K and 4K |
| ai-chat | 224 | 50+ models through unified chat APIs, including native Claude Messages, Gemini audio analysis, OpenAI-compatible calls, embeddings and stateful conversations |
| google-gmail | 223 | Gmail threads and labels: search, triage, archive, attachments and sending over the Gmail v1 REST API |
| face-transform | 222 | Face keypoints, portrait beautification, aging and de-aging, gender swap, face replacement, cartoon avatars and liveness detection |
| zhihu | 221 | Zhihu and web search, trending topics, and reading or publishing Zhihu articles and answers |
| short-url | 221 | Single and batch short-link creation with custom slugs and expiry |
| template-skill | 216 | Name-level only: a scaffold for authoring a new skill; the skill ships no description, so its behaviour is unverified |
| google-calendar | 216 | Calendar agenda, free-busy, invitations, conflict checks and event management over the Calendar v3 REST API |
| youtube | 215 | YouTube search, own-channel and video stats, comments and uploads over the Data API v3 |
| tencentcloud-cls | 215 | CLS log search, trace-ID lookups, 5xx hunting and CQL or SQL analytics over log topics |
| blogger | 214 | Blogger post publishing, blog listing and post updates over the Blogger API v3 |
| microsoft-onedrive | 213 | OneDrive and SharePoint folders and files, uploads, downloads and sharing links through Microsoft Graph |
| gpt-image-2 | 213 | OpenAI gpt-image-2 generation and editing, including compositing a real logo, QR code or screenshot into a scene |
| google-drive | 213 | Drive read, export, upload, rename, move and delete on files explicitly selected or shared with the app |
| github | 212 | GitHub issues, pull requests, repos, code search, releases, gists, stars and Actions through the gh CLI |
| tencentcloud-tke | 211 | Kubernetes Engine clusters and workloads: cluster and node health, pods, scaling, rolling restarts, kubeconfig and events |
| tencentcloud-edgeone | 211 | EdgeOne zones, CDN cache purge and prefetch, task status and acceleration domain management |
| tencentcloud-dns | 211 | DNSPod records for A, AAAA, CNAME, MX, TXT, NS, SRV and CAA, plus ACME challenge, SPF and DKIM records |
| tencentcloud-cls-alarm | 210 | CLS alarm policies, notice groups, shields and alarm execution logs, including mute windows |
| google-tasks | 210 | Tasks lists and items: weekly recaps, grouping, adding, completing, moving and deleting |
| slack | 209 | Slack public-channel search, reading joined conversations and user-confirmed bot messages |
| notion | 209 | Notion page and database search, reading, appending and creation |
| gitlab | 209 | GitLab issues, merge requests, repositories, CI pipelines and code search through the glab CLI |
| onepage-pdf | 208 | HTML to a single continuous-page PDF that keeps desktop layout, backgrounds and selectable text |
| linkedin | 208 | LinkedIn personal-feed text and link posts, including cross-posting an article |
| devto | 207 | dev.to publishing, updates, article listing and stats over the Forem API v1 |
| reddit | 206 | Subreddit search, rule reading, thread replies and link or text submissions via OAuth or login cookies |
| cos-upload | 205 | Uploads a local image, audio, video or document to AceData Cloud CDN and returns a public URL |
| substack | 201 | Substack identity, publication listing, post stats and new post publishing with the user's own cookies |

The remaining 79 indexed listings range from 1 to 181 installs.

## Why This Matters for Hermes Agents

Most agent skill collections are broad and shallow: one skill per vendor with the model names buried in the prompt. AceDataCloud goes the other way, one skill per API surface, so an agent loads a few thousand tokens about Suno instead of a whole platform description.

That granularity is what makes the README's install prompt work. You name the service, install that skill only, and the context cost stays proportional to the task in front of you rather than to the size of the vendor catalogue.

The credential split is worth copying in your own skills. Generation uses `ACEDATACLOUD_API_TOKEN`, account reads use `ACEDATACLOUD_PLATFORM_TOKEN`, and public pricing needs nothing. A service-scoped key narrows the blast radius of a leak in a way a single shared key never does.

Coverage is the practical argument. Suno, Veo, Kling, Wan, Hailuo, Seedance, Flux, Seedream and Nano Banana share one request shape, so a pipeline that needs a track plus a cover image does not pull in two vendor SDKs and two auth flows.

The operations skills reach past media: CLS log search, DNSPod records, TKE workloads and EdgeOne cache purges are the chores that usually interrupt a deploy, and having them as agent-readable procedures shortens the loop between noticing a problem and running the fix.

Read the popularity signal honestly. Install counts here measure a distribution list, not review depth: one table row ships no description at all, and the only two Snyk warns in the sample land on the mail and voice skills. Check those two before wiring them into anything that sends.

## Usage

| You say | What happens |
|---|---|
| "Generate a 30-second synthwave track with vocals" | suno-music submits the song, checks audio availability and can extend, cover or edit the result |
| "Animate this product photo into a video" | luma-video or veo-video takes the image, submits a job and returns a task ID to poll |
| "Find competitor pricing pages on the web" | google-search returns structured results with titles, snippets and URLs, with localization and time filters |
| "Triage my Outlook inbox and draft two replies" | microsoft-outlook searches and reads the mailbox, drafts the replies and leaves sending to you |
| "Trace this failing request in our logs" | tencentcloud-cls searches the log topic by trace ID and runs a CQL query over the window |
| "Shorten this link with a custom slug" | short-url creates the short link with the slug and expiry you specify |
| "Publish this post to my Substack" | substack shows the logged-in publication and publishes the post using your own cookies |

## Verification

Fetch one skill file and confirm the frontmatter is intact:

```bash
curl -fsSL https://raw.githubusercontent.com/acedatacloud/skills/main/skills/ai-chat/SKILL.md | head -12
```

That URL returned 200 with the `ai-chat` frontmatter on 2026-11-04. The account skill resolves the same way at `skills/acedatacloud/SKILL.md`.

Then confirm the skill landed where your agent reads skills from. On the Codex path the README says the directory is `.agents/skills/<skill-name>/`, so check for the folder and the file inside it:

```bash
npx --yes skills@1.7.2 list
ls .agents/skills/suno-music/
```

`skills@1.7.2 list` is the CLI's own inventory. If the skill is missing there, the install ran against the wrong agent flag or the session started before the copy finished.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fish-audio | Pass | Pass | Warn |
| suno-music | Pass | Pass | Pass |
| microsoft-outlook | Pass | Pass | Warn |
| figma | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 19,364 combined installs across 124 indexed listings; 17 GitHub stars; NOASSERTION licence; last pushed 2026-11-03. Counts drift over time.
- The index and the tree disagree by two: 124 indexed listings against 122 SKILL.md directories in the repo, 111 of those under `skills/` and the rest under `claude-plugins/` and `platforms/amp/skills/`.
- GitHub reports NOASSERTION for the licence while the README badge says Apache-2.0. The LICENSE file is the tiebreaker, so do not assume Apache terms until it is read.
- The four sampled verifications cover 4 of 45 table rows. figma appears in the security sample but sits below the install threshold, so it is not in the table above.
- Installation produces nothing. Every media and connector skill needs a funded AceDataCloud application and its own API key, and a skill cannot set an environment variable or load a `.env` file for you.
- sora-video documents a retired integration. The Sora service is not published in the public API catalog, so treat that skill as migration guidance rather than a working generator.

## Related

- [Songwriting & AI Music - Creative Music Generation Setup](/hermes/skills/catalog/songwriting-and-ai-music-setup)
- [HeartMuLa - Open-Source AI Music Generation Setup](/hermes/skills/catalog/heartmula-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one service at a time. The README's first-run table exists because loading 45 unrelated API procedures costs context on every single turn.
- Start with the general application key, then mint a service-scoped key once a workflow reaches production. Revoking one narrow key is cheaper than rotating a shared one.
- Submit once and poll the same task ID. Re-submitting on a timeout double-bills a video job, and every generation skill returns an ID for exactly this reason.
- Use cos-upload as the bridge. Image-to-video and audio-input APIs want a public URL, and a local path will not survive the hop.
- Check balance before a batch. Credits are consumed per call, and the account skill reads catalog and pricing without spending anything.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
