---
title: "LogPulse MCP - Changelogs an Agent Can Upgrade"
description: "Driven keyless: any public CHANGELOG becomes versions, breaking changes and migration steps, and a Keep a Changelog 2.0.0 check with line numbers"
category: "Developer Tooling / Release Management"
stars: "n/a (hosted service, registry app.lovable.release-ripple-roadmap/logpulse 1.0.0 against 1.1.0 served)"
added: 2026-11-13
source: "the submission queue entry #7292, the official registry record naming the remote https://release-ripple-roadmap.lovable.app/mcp, and a keyless session on this host: initialize, tools/list and seventeen tools/call requests against the live endpoint"
relevance: ★★★
tags: [changelog, release-notes, breaking-changes, migration, keepachangelog, semver, keyless, mcp]
last_updated: "2026-11-13"
---

# LogPulse MCP

**A coding agent writes against the version of a library it saw in training. When the library ships a breaking change, the agent finds out from a stack trace.**

Release notes are prose. They live in a README, a GitHub release, a blog post, or nowhere, and the one thing an agent needs - that `acme.track()` no longer takes a callback, and here is the one line to replace - is buried in paragraph four. LogPulse's premise is that a changelog should be a feed an agent can read, with the breaking change and the migration step as separate fields rather than as sentences.

It also does the unglamorous half: it will take a `CHANGELOG.md` and check it against Keep a Changelog 2.0.0, line by line, and hand back a corrected copy.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://release-ripple-roadmap.lovable.app/mcp
Transport:   JSON-RPC 2.0 over POST, SSE responses, no session id issued
Auth:        none for nine tools; publish_release and post_roadmap_update need a Bearer API key
Server name: logpulse 1.1.0 (title LogPulse), protocol 2025-06-18, capabilities tools only
Tools:       11, read from a live tools/list
Built by:    Kalmwerk (release-ripple-roadmap.lovable.app)
Registry:    app.lovable.release-ripple-roadmap/logpulse 1.0.0, published 2026-10-30T16:09:19Z
Pricing:     every tool except publishing is free; Free plan publishes 10 releases, Pro EUR 99 a year
Discovery:   /mcp/server-card, /.well-known/mcp.json, /.well-known/agent-card.json
```

## The evidence tier

Everything below was measured on 2026-11-13 between 17:55Z and 18:10Z against the live endpoint, with no key and no account: `initialize` returned HTTP 200 as `logpulse` **1.1.0** on protocol `2025-06-18` with tools as its only capability, `tools/list` returned **11** tools, and **seventeen** `tools/call` requests were driven, sixteen of which answered with a result and one of which was refused on an argument name. Nothing below is quoted from the vendor's submission text.

## Why This Matters for Operators

The question "what changed, and what do I have to do about it?" is the cheapest question a business can ask and the most expensive one to get wrong. An agent that answers it from memory answers about a version that may not exist any more. An agent that answers it from a release feed answers about the version actually installed.

Two surfaces here are worth the operator's attention, and neither needs an account: `convert_changelog` turns any public GitHub repository's releases into the structured shape, and `validate_changelog` measures a changelog file against the specification its own project claims to follow. The second one is where the tool is unusually honest, and also where it stops short.

## What It Actually Does

| Tool | What it answers |
|---|---|
| `search_changelogs` | Finds a hosted changelog by package, repository, product name or slug |
| `get_changelog` | One changelog's name, repository, packages, latest version and feed links |
| `list_releases` | Published releases newest first, with breaking changes, migration steps and deprecations |
| `get_release` | One release by version or URL slug, with full notes |
| `compare_versions` | What changed between two versions and every migration step on the way |
| `get_roadmap` | Items under review, planned, in progress and shipped, with vote counts |
| `generate_release_notes` | Release notes from a public repository's commits and merged pull requests |
| `validate_changelog` | A Keep a Changelog 2.0.0 check with line numbers, fixes and a corrected copy |
| `convert_changelog` | Any changelog text or GitHub URL into a machine-readable changelog |
| `publish_release` | Writes a release to the caller's own changelog (needs an API key) |
| `post_roadmap_update` | Adds or moves a roadmap item (needs an API key) |

Nine of the eleven carry `readOnlyHint: true` and `openWorldHint` only where they reach GitHub. The two write tools carry `readOnlyHint: false` with `destructiveHint: false`, and both refuse without a key rather than silently doing nothing.

## The check that reports its own line numbers

Given a deliberately non-conforming changelog - a US-format date, `### Fixes` and `### Improvements`, versions out of order, no Unreleased section - `validate_changelog` returned `valid: false` with **1 error, 6 warnings and 1 tip** over **3 versions**, each with a rule name and a line number:

| Severity | Rule | Line | What it said |
|---|---|---|---|
| error | `date-format` | 5 | `12/03/2026` is not `YYYY-MM-DD`, and could be read as day/month or month/day |
| warning | `unreleased-missing` | 5 | no Unreleased section, fixed in the corrected copy |
| warning | `change-type-unknown` | 10 | `Fixes` is not one of the six types, renamed to `Fixed` |
| warning | `change-type-unknown` | 24 | `Improvements` is not one of the six types, renamed to `Changed` |
| warning | `change-type-duplicate` | 24 | version 1.1.0 carried two Changed sections, merged |
| warning | `version-order` | 18 | 1.1.0 is listed below 1.0.0 |
| warning | `link-missing` | - | no version links to its changes |
| info | `format-link` | - | the file does not say it follows Keep a Changelog |

The response carries `fixed_markdown`: the same file with the Unreleased section added, the two unknown types renamed and the duplicate sections merged, **four findings auto-fixed**. Records the vendor served alongside the check would let a team wire this into CI and read a rule name rather than a diff.

## The defect: the corrected copy still fails

The corrected copy still contains the one **error**. The date stays `12/03/2026` and the versions stay misordered, so a pipeline that trusts `fixed_markdown` ships a file the same tool just called invalid. Only warnings are auto-fixed, and the response says so only by omission - there is no field marking which severities the fixer touches. Treat the corrected copy as a starting point for a human, never as a passing file.

Two related behaviours worth knowing:

- The structured field is `fixed_markdown`. A caller that looks for `corrected_markdown` gets nothing and may conclude no fix was offered.
- A file this tool cannot find at the repository root is reported plainly: `We couldn't find a changelog file (CHANGELOG.md, CHANGES.md, HISTORY.md…) in sindresorhus/got. Is the repository public? Link the file directly or paste it.` Pointing it at `conventional-changelog/standard-version` found the file and returned **28 errors, 124 warnings and 1 tip** over **37 versions** with **148** findings auto-fixed, which is a fair verdict on a conventional-changelog file measured against Keep a Changelog.

## The conversion, measured on a real repository

`convert_changelog` on `https://github.com/sindresorhus/got` returned the shape `logpulse.changelog.v1`: **100 releases**, latest **16.2.0** dated `2026-10-30`, **40** breaking changes, **0** deprecations, generated at `2026-11-13T18:02:00.114Z`. Each release carries version, title, date, URL, prerelease and yanked flags, a per-type change map (added, changed, deprecated, removed, fixed, security, other), its own breaking-change list and a `migration_guide` field.

`generate_release_notes` on the same repository returned the range `v16.1.0...v16.2.0` with **1 entry from 2 commits and 1 pull request**, plus a warning that earns trust: `Nothing has been merged into main since v16.2.0, so these are the notes for v16.2.0 itself.` It reports the range it actually used instead of an empty changelog.

The conversion has a normalization defect: entry text keeps GitHub's horizontal rule as a list item (`"---"` appears inside the `other` array) and the compare URL is treated as a change of its own. A consumer that counts changes per release will over-count by two on every release that carries a compare link.

## The hosted layer today is seed data

`search_changelogs` answered for `acme` and `logpulse` and for nothing else tried: `next`, `zod`, `vite`, `supabase`, `github` and `lovable` all returned zero results. The two records that do resolve are demonstration fixtures - the `acme` record points at `https://acme.example.com` and describes a product analytics suite with **8** releases, and the `logpulse` record describes "the lightweight changelog widget" rather than this product.

`compare_versions` against that fixture is still a clean read of the intended shape: **8** releases, **3** breaking changes, **3** deprecations, and migration steps that name the version, the summary, what it `affects` and the replacement text - `acme.track()` losing its callback, page-number pagination replaced by `next_cursor`, funnel step ids becoming strings.

So the honest reading is: the hosted aggregation layer is not populated yet, and the value today is in the four free tools that read other people's repositories.

## The write path, to its gate

`publish_release` without a credential returns `isError: true` and: `This tool needs a LogPulse API key. Create one in LogPulse → Developers, then add the HTTP header 'Authorization: Bearer ***' to this MCP server in your client's settings.` The instructions string also warns the assistant never to ask the user to paste a key into the chat, which is the correct instruction for a surface that takes a bearer token.

## Setting it up in Hermes

```bash
hermes mcp add logpulse --url https://release-ripple-roadmap.lovable.app/mcp
hermes mcp test logpulse
```

No key is needed for reading, converting and validating. Add `Authorization: Bearer <key>` in the client's MCP server settings only if the assistant will publish releases or move roadmap items.

## Where this sits in the catalog

The nearest neighbour is [End of Life MCP](/hermes/mcp/servers/external/endoflife-mcp/), which owns the lifecycle question: is this dependency maintained, and when does it stop receiving fixes. LogPulse answers the other half of the same operator question, which is what the upgrade costs - the change itself, the breaking change inside it and the migration line that follows from it. It is not a duplicate of the EOL surface, and it is not a business-data connector: it is release hygiene, and the check is the part a team can act on today.

## Limitations recorded

- Hosted changelog inventory is seed data; search is only useful for products already publishing here.
- `fixed_markdown` never repairs an `error`-severity finding, including the date format, and does not reorder versions.
- Conversion keeps GitHub's `---` separators and the compare URL as entries in the change list.
- The registry record names **1.0.0** while the server serves **1.1.0**; read `initialize` for the version actually running.
- The hosted-plan figures come from the vendor's pricing page as read on 2026-11-13: Free publishes up to 10 releases, Pro at EUR 99 a year is listed as opening soon, open-source projects are unlimited.

### Is LogPulse an MCP server or a changelog host?

Both, and the two halves are at different stages. The MCP server is live, keyless and does real work on any public GitHub repository today. The changelog host is the business model behind it and currently carries demonstration records.

### Does it need an account to read a changelog?

No. `initialize`, `tools/list` and the nine read tools answered with no credential on 2026-11-13, and the vendor documents publishing as the only authenticated path.

### Can it be wrong about what changed?

It can be incomplete, and it says where it stops: a conversion reads release notes rather than code, so a breaking change that was never written down cannot appear in the feed. That is the same limit as reading the release page, with the advantage that the migration field is asked for explicitly.
