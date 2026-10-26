---
title: "Recoup Skills - Music Label Agent Suite Setup"
description: "recoupable/skills: 32.0K combined installs across 141 listings. A record label in a box: roster, catalog, release, research and content skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/recoupable-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "music industry", "catalog", "mcp"]
---

# Recoup Skills - Setup Guide

**Source:** [recoupable/skills](https://www.skills.sh/recoupable/skills) via skills.sh - 32.0K combined installs across 141 indexed listings; snapshot taken Oct 26, 2026
**GitHub:** [recoupable/skills](https://github.com/recoupable/skills) (9 stars; GitHub reports NOASSERTION, and the LICENSE file is AGPL-3.0 for non-commercial use with a separate commercial licence on request; pushed 2026-10-26; branch `main`; 125 directories under `skills/`, each holding a `SKILL.md`; GitHub reports a 19,665 KB repo)
**Category:** Music / Label Operations
**Quality Tier:** 🟡 Beta (very active publisher with 141 indexed listings and a working plugin, but a non-commercial AGPL licence with a paid commercial option, Snyk Warn on the sampled platform skills, and 65 of the 125 in-repo skills being internal agency-consulting workflows)

Recoup is an AI music platform whose agent layer ships as one plugin: a Claude Code, Codex and Cursor plugin, a remote MCP server at `https://api.recoupable.dev/mcp`, and 125 skills in the repository. The README calls it "a record label in a box", and the coverage matches - roster onboarding, catalog and contract diligence, release planning, playlist and press research, song analysis, cover art, lyric video and full narrative music videos. Installation is a two-line plugin flow, and every skill then rides the same authenticated MCP connection.

Two things need stating up front because the catalog entry alone would mislead. First, the install counts on the top six skills (4,707 to 4,957, within 250 installs of each other) look like suite-wide adoption of one plugin rather than six independent decisions. Second, 65 of the 125 skills are `recoup-internal-consulting-*` workflows for Recoup's own agency practice - PMF discovery, proposals, invoicing, LinkedIn funnels, client reporting. They are published in the clear, but they are staff operating procedures, not customer features, and the README says so directly: the name does not make their contents private.

## Installation

The skills-only path, which is what skills.sh indexes:

```bash
npx skills add recoupable/skills
```

That installs instructions only. The MCP tools need the plugin path, or a manual server entry:

```bash
# Claude Code, plugin marketplace
/plugin marketplace add recoupable/skills
/plugin install recoup-plugin@recoup

# confirm the installed package and the MCP connection
claude plugin list
claude mcp get plugin:recoup-plugin:recoup
```

For Codex and Cursor the README points at each host's local-plugin flow: the Codex manifest references `.mcp.json`, the Cursor manifest references `mcp.json`, and both configure the same remote server. No API key is bundled.

After installing, authorize the server in the host's connection UI (`/mcp` in Claude Code), review the `mcp:tools` permission, and confirm with a read-only call such as `list_artists`. The host stores and refreshes the OAuth credentials. REST-only endpoints and the bundled scripts still need separate REST credentials, so installing the skills does not make every endpoint an MCP tool.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| recoup-platform-api-access | 4,957 | Call the Recoup REST API and external connectors directly: platform resources plus Google Docs, Sheets, Drive, Gmail, TikTok and Instagram actions |
| recoup-platform-email-helper | 4,871 | Send task email through a bundled Node script that serializes the body correctly instead of hand-built curl |
| recoup-platform-build-os | 4,715 | Scaffold a music company workspace in its own repo, with health checks, reusable knowledge and portable skills |
| recoup-roster-manage-artist | 4,709 | Work inside one artist folder: read and update context, brand, songs and releases |
| recoup-roster-add-artist | 4,709 | Add or attach an artist: verify Spotify identity, resolve the workspace, then research, catalog and socials |
| recoup-roster-list-artists | 4,707 | Inventory the roster, falling back to the live account when the local filesystem is empty |
| recoup-music-video | 1,202 | Narrative music video through the Small Room workflow: bible, audition, plates, shot list, motion, verified edit |
| recoup-api | 550 | Listed on skills.sh but has no `SKILL.md` in the current `skills/` tree, so its instructions could not be reviewed at this snapshot |
| artist-workspace | 452 | Listed on skills.sh but has no `SKILL.md` in the current `skills/` tree, so its instructions could not be reviewed at this snapshot |

The remaining 132 indexed listings range from 1 to 31 installs. They are the long tail of the same suite: song and release helpers (`recoup-song-analyze-audio` 31, `recoup-release-plan-rollout` 30, `recoup-content-write-caption` 29), catalog diligence (`recoup-catalog-review-deal` 29, `recoup-catalog-estimate-value` 29), platform plumbing (`recoup-platform-connect-account` 29, `recoup-platform-capture-lesson` 27), and most of the 80 `recoup-internal-*` staff skills, which sit at 1 to 3 installs and read as internal procedures rather than customer features.

## Why This Matters for Hermes Agents

Most skill repositories hand an agent prose. This one hands it a workspace convention plus a connection. Artist directories live at `artists/{artist-slug}/` with a `RECOUP.md` identity file carrying `artistName`, `artistSlug` and `artistId`, and the roster skills read and write that layout. An agent that can list a roster, resolve one artist, and then work inside their folder has a durable operating model rather than a chat transcript.

The second useful pattern is the split between read and mutation. `recoup-roster-add-artist` verifies Spotify identity and asks for confirmation before a live mutation, and it explicitly rejects a name or a local folder as proof of identity. `recoup-platform-api-access` tells the agent to prefer authenticated MCP tools over raw curl. Those are the two failure modes that make agent-driven CRM work dangerous, and both are addressed in the instructions rather than left to the operator.

Third, the email helper is a small but instructive artifact: it exists because hand-built `curl` with inline `jq` produced malformed bodies and the API used to return `success:true` on an empty footer-only email. A skill that encodes "do not serialize JSON in the shell" is worth more than a page of style guidance, and the same lesson transfers to any Hermes job that posts JSON to an API.

Finally, the suite shows what a mature skill pack looks like operationally: a `RESOLVER.md` routing table, `resolver-eval.jsonl` fixtures, CI that fails on unreachable skills, and two build artifacts (customer and full) generated on every merge. If you maintain a private skill library, that structure is the part to copy.

## Usage

| You say | What happens |
|---|---|
| "Add this new signing to the roster" | `recoup-roster-add-artist` verifies the Spotify identity, resolves the artist in the workspace, then runs research, catalog and socials enrichment |
| "What is in this artist's workspace?" | `recoup-roster-manage-artist` reads `artists/{slug}/RECOUP.md` context plus brand, songs and releases, then summarises or updates |
| "Should we buy this catalog?" | `recoup-catalog-review-deal` runs the underwriting flow from data room to IC memo, with `recoup-catalog-estimate-value` for a public-data valuation |
| "Find playlist targets across the whole catalog" | `recoup-research-playlist-targets` maps placement gaps, and `recoup-research-find-contacts` drafts outreach to the right curators |
| "Make a music video for the new single" | `recoup-music-video` runs the Small Room sequence and stops at the finished asset unless publishing is requested |
| "Email the owner the weekly report" | `recoup-platform-email-helper` sends through the bundled Node script so the body is serialized correctly |
| "recoup-internal: run the daily sales sweep" | Only fires with the literal `recoup-internal` keyword, then ranks the Stripe, Attio and valuation follow-ups into one list |

## Verification

Confirm the skill install and the plugin state:

```bash
npx skills list | grep -i recoup
claude plugin list
claude mcp get plugin:recoup-plugin:recoup
```

Read the instruction files before granting the MCP permission. All five URLs below returned HTTP 200 when checked with `curl` on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/recoupable/skills/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/recoupable/skills/main/skills/recoup-platform-api-access/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/recoupable/skills/main/skills/recoup-roster-add-artist/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/recoupable/skills/main/skills/recoup-music-video/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/recoupable/skills/main/.claude-plugin/plugin.json
```

The routing table is the fastest way to see whether a skill you want exists, and it is served from the same branch:

```bash
curl -sL https://raw.githubusercontent.com/recoupable/skills/main/RESOLVER.md | grep -i 'catalog'
```

Then prove the connection does real work with a read-only call. The README's own check is `list_artists`: ask the host for "list my artists" after OAuth consent and confirm real rows come back rather than a permission error. A connected server only proves transport and authentication, not that your workspace is authorized for the business tools.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| recoup-platform-api-access | Pass | Warn | Warn |
| recoup-platform-email-helper | Pass | Pass | Pass |
| recoup-roster-add-artist | Pass | Pass | Warn |
| recoup-music-video | Pass | Pass | Warn |

Every sampled page served a verdict; nothing had to be recorded as not reported. Socket warns on one of the four (the API access layer), and Snyk warns on three of four (api-access, roster-add-artist, music-video), while Gen Agent Trust Hub clears all four.

Read the permission surface before consenting, because this suite is built to act. The README directs you to review the full `mcp:tools` permission on a remote server at `api.recoupable.dev`, which means the host holds an OAuth token tied to a Recoup account and can call whatever business tools that account authorizes. `recoup-roster-add-artist` performs a live mutation and is instructed to confirm identity first. `recoup-platform-email-helper` sends real email to real recipients. `recoup-platform-api-access` can run connector actions that edit Google Docs, Sheets and Drive and act through Gmail, TikTok and Instagram. `recoup-platform-connect-account` falls back to REST credentials when OAuth is unavailable, so a second credential path exists. There is no local credential file in the repo and no bundled API key; the README states that credential export is excluded. The `recoup-internal` keyword is a routing gate in the instructions, not a permission boundary on the server side, so treat staff skills as available to any agent that can reach the MCP tools.

## Limitations

- The install index and the repository tree disagree. 27 of the 141 indexed listings have no directory under the current `skills/` tree, including two that sit in the top nine by installs (`recoup-api` at 550 and `artist-workspace` at 452). In the other direction, 11 tree directories are not indexed at all, among them `recoup-catalog-audit-catalog`, `recoup-release-manage-delivery`, `recoup-internal-podcast` and `recoup-research-artist-overview`.
- The licence as published is not plain open source. GitHub reports NOASSERTION, the LICENSE file states AGPL-3.0 for non-commercial use with a commercial licence available from support@recoupable.com, and `.claude-plugin/plugin.json` declares `AGPL-3.0-only`. The non-commercial rider means a commercial deployment needs the paid licence, so read all three before shipping anything built on this code.
- Much of the suite is internal agency-consulting procedure. 65 skills carry the `recoup-internal-consulting-` prefix and 80 carry `recoup-internal-` overall, covering PMF discovery, proposals, invoicing, LinkedIn publishing and client reporting. They only fire on the literal `recoup-internal` keyword, and the README notes that the name does not make their contents private.
- The skills are instructions, not the platform. Hosted operations such as saving a catalog import need the corresponding API and database release; a local worksheet is not a hosted import, and REST-only endpoints need separate credentials.
- The skill surface moves fast, and the README carries migration notes for a package rename (`recoup-skills` to `recoup-plugin`) and for dropped lifecycle hooks in 2.1.1 and 2.2.0. Re-read the README after any update instead of assuming the skills you installed last month behave the same.
- Snapshot data, verified Oct 26, 2026: 31,987 combined installs across 141 indexed listings; 9 GitHub stars; NOASSERTION on GitHub with an AGPL-3.0 non-commercial LICENSE file; last pushed 2026-10-26. Counts drift over time.

## Related

- [Songwriting & AI Music - Creative Music Generation Setup](/hermes/skills/catalog/songwriting-and-ai-music-setup) - song generation without the label operations layer.
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup) - the video generation side that pairs with the music video workflow here.
- [Social Content - Multi-Platform Social Media Creation Setup](/hermes/skills/catalog/social-setup) - posting and repurposing outside a music-specific suite.
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - planning discipline for the content skills that ship here.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the plugin, not just the skills, if you want the tools. `npx skills add` writes instructions and nothing else; the MCP connection is what makes `list_artists` and the catalog operations real.
- Verify with a read after OAuth. `claude mcp get plugin:recoup-plugin:recoup` only confirms transport and auth; a read-only `list_artists` confirms the tools your account actually authorized.
- Grep `RESOLVER.md` before asking for a skill. It is the routing table the agent itself uses, and it is faster than listing 125 directories.
- Never hand-build the email payload. Use `recoup-platform-email-helper`; the README documents that the shell-serialized version used to deliver empty emails and report success.
- Keep private artist evidence in the workspace the skill writes to, not in chat. These skills treat `artists/{slug}/` as the record of truth, and a summary pasted into a session is not durable.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
