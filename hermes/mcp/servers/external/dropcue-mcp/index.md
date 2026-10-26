---
title: "DropCue MCP - Music Catalog, Pitches and Royalties"
description: "A local MCP server for music catalog and rights work: tracked share links, a pitch pipeline, licenses, PRO royalty imports and per-track earnings."
category: Media
stars: n/a (local kit, paid Studio plan)
added: 2026-10-24
source: "chatmcp/mcpso issue #6036 (October 24, 2026 midday sweep) + public install kit built and driven locally"
relevance: ★★★
tags: [music, royalties, licensing, publishing, sync, rights, pitch-pipeline, local-mcp, stdio, business-records]
last_updated: "2026-10-24"
---

# DropCue MCP

**A music catalog server for the people who license music for a living.** Composers, producers, publishers and sync agencies keep their catalog in DropCue, and this server lets an agent work the business side of it: who was pitched, what was licensed, what a PRO statement paid, and which deliverables are still owed.

```
Server type: Local (stdio, node >= 20), talks to https://dropcue.app/api/v1
Auth: personal API key from DropCue Settings, read from DROPCUE_API_TOKEN or the macOS Keychain item "dropcue-api-token"
Protocol: 2025-06-18 (observed at initialize on the published kit)
Server: dropcue 0.19.1, tools capability with listChanged
Tools: 105 (tools/list on the kit build; version.json declares the same count)
Install: curl -fsSL https://dropcue.app/kit/install.sh | bash
Required plan: paid DropCue Studio, from $29/mo billed annually. Trials do not include it
Built by: DropCue (dropcue.app)
```

## Why This Matters for Operators

Rights work is the part of a music business that agents have never been able to touch. A catalog lives in one app, the pitch history in a spreadsheet, the license record in a folder of PDFs, and the PRO statements in whatever CSV each society happened to export this quarter. Answering "who am I waiting on" means opening all four.

DropCue is the first entry in this catalog where the catalog, the pitch, the license and the royalty statement are one record set behind one server. `whats_next` is the tool that shows it: overdue and upcoming project and cue deadlines, cues sent and waiting for notes, pitch follow-ups, open to-dos, exclusives and holds ending soon, registrations to finish and unsigned agreements, grouped overdue, soon, waiting, no date and later. The vendor states plainly that plays and downloads never appear there, which is the discipline a business answer needs: attention items only.

The royalty side is the second reason. `import_royalty_statement` takes a PRO or publisher statement CSV up to 4 MB and 50,000 lines, reads it the way DropCue's own importer reads it, and returns the source, period, line count and total on a dry run first. A layout it does not recognise comes back with its column headers so the user can name the title and amount columns instead of guessing. `royalty_summary` then answers by source, network, show, usage, society and territory, with top and bottom earning tracks.

## What It Actually Does

All 105 tools were read from `tools/list` on the published kit, and the API routes behind them are documented in the kit's own `openapi.yaml`.

| Area | Representative tools | What it answers |
|---|---|---|
| Catalog | `search_tracks`, `update_track_metadata`, `nest_versions`, `list_albums`, `get_playlist` | what we have, and where each version sits |
| Intake | `preview_upload`, `upload_tracks`, `upload_status`, `preview_replace_audio`, `replace_audio` | bring a folder in, or swap a master in place, after a confirmed preview |
| Pitching | `list_pitches`, `get_pitch`, `update_pitch`, `log_follow_up`, `create_pitch` | which supervisor has which cue, and what is due next |
| Sharing | `create_share_link`, `add_share_recipient`, `list_shares`, `get_share` | a tracked link per person, with views, plays and downloads |
| Rights | `list_licenses`, `add_license`, `update_license`, `attach_license_file`, `license_statuses` | what was licensed, to whom, at what fee, for what term, and what is unpaid |
| Royalties | `import_royalty_statement`, `royalty_summary`, `track_royalties`, `list_royalty_statements` | what a statement paid, per track and per network |
| Relationships | `list_contacts`, `list_organizations`, `add_agreement`, `attach_agreement_file` | who the company contact is, and what is signed |
| Delivery | `create_project`, `add_cues`, `update_deliverables`, `list_deliveries` | which cue of which job has which deliverable outstanding |
| Reporting | `report_summary`, `report_top`, `report_tracks` | opens, plays, listeners, downloads and link sends against the period before |
| Work queue | `whats_next`, `list_todos`, `update_todo` | what needs a person today |

## Installation

One line in Terminal on a Mac installs the kit, asks for the key and connects Claude Code, the Claude app and Codex:

```
curl -fsSL https://dropcue.app/kit/install.sh | bash
```

The kit is a self-contained Node program with two dependencies (`@modelcontextprotocol/server` 2.0.0 and `zod` 4). It was downloaded and built in this sweep from `https://dropcue.app/kit/dropcue-kit.tar.gz`; `initialize` returned `serverInfo` `dropcue` 0.19.1 on protocol 2025-06-18 with the tools capability, and `tools/list` returned 105 tools. Any MCP client that speaks stdio can run it with `DROPCUE_API_TOKEN` set.

## Configuration and Safety

The token is a personal API key created in DropCue under Settings, API and AI assistants, stored in the macOS Keychain and never written into a tool result, an error message or a log line. It can be switched off and stops working on the next request.

The server is explicit about what it will not do, and the restrictions are enforced in the tool surface rather than promised in prose:

- it cannot delete tracks, playlists, contacts or companies; removing something archives it and it can be restored
- it never sends email, and there is no send tool in the 105
- writers, publishers and ISRCs are never changed; `fill_track_credits` fills only empty fields
- the only public actions are `create_share_link` and `publish_portfolio`, and both require the user to agree first
- the only delete is `discard_portfolio`, and only for an unpublished draft
- uploads, audio replacements and stem runs show a plan and wait for confirmation, and a replaced file is kept on the server for 30 days

One distinction the README makes that matters for client confidentiality: discovery is separate from sharing. With Discovery on, a new main track is discoverable to music supervisors even with no share link, so "unshared" means no link rather than not visible, and `preview_upload` says which applies before anything uploads.

## What It Costs

The API and the MCP connection come with paid DropCue Studio at $29 a month billed annually, together with the Business Suite and team seats. Trials do not include it. Video intake needs Pro or higher, `build_portfolio` is Studio at 30 builds a month, and `make_stems` costs one stem credit per run and is not available on Starter or Artist.

The vendor's own comparison, dated September 28, 2026, puts DISCO's API on its Enterprise plan only with custom pricing and says ReelCrafter lists no API at all. That is a vendor claim recorded as such.

## Integration with CorpusIQ

Music rights is a vertical business system of record, which is where CorpusIQ connectors stop. CorpusIQ reads the operator's own Google Workspace, accounting, commerce and analytics sources with read-only retrieval; DropCue holds the catalog, pitch, license and royalty records that no general connector covers. The shape is the same one this catalog applies elsewhere: ask the cross-source question in the assistant, and let the domain system answer for its own records.

## Limitations

- **No live API call was made.** The kit was built and spoken to locally, and `tools/list` is real, but every tool that reaches the API needs a paid Studio account with a personal key, which this sweep does not create. That is the gap, named rather than papered over.
- **Mac only, as the vendor states.** The install script and the Keychain token are macOS paths.
- **No OAuth and no hosted endpoint.** There is nothing to probe remotely, so the 401-plus-metadata evidence tier used for hosted servers does not apply here.
- **No official MCP registry entry.** A search of `registry.modelcontextprotocol.io` for dropcue returned zero servers on October 24, 2026.
- **Discovery is on by default for new uploads on accounts that enable it**, so an agent uploading a client's unreleased cues should be told which state applies.
- **The kit is a pilot**, described as such in its own package and README.
- Single vertical: this catalogues a music business, not a general media library.

## FAQ

### Can an agent delete a client's tracks or send music out?
No. Nothing in the 105 tools deletes a track, playlist, contact or company, and there is no send tool at all. Removing archives, and the two public actions, a share link and a portfolio publish, stop for the user's confirmation.

### Does it replace the sync licensing database I already use?
It replaces the record keeping around it for DropCue accounts. Licenses, agreements, deliveries, pitches and PRO statements live in one record set, which is the difference between answering "what did this cue earn across networks" and reconciling four exports by hand.

### How does it differ from the music-generation servers already in this catalog?
Those produce audio. This one operates a catalog that already exists: metadata in bulk, versions nested, licenses recorded, statements imported, deliverables tracked. Generation and rights are different jobs and the catalog now holds both.

### Can my assistant change a writer, publisher or ISRC?
No. Those fields are protected; `fill_track_credits` fills empty credits only. Anything already recorded stays as it is.

### What do I need before it works?
A paid DropCue Studio plan, the key from Settings, API and AI assistants, and a Mac. The one-line installer does the rest, and `check_version` reports whether the installed kit is current.

## See Also

- [GumroadDNA MCP - Gumroad Store Operations](/hermes/mcp/servers/external/gumroad-dna-mcp/) - another local stdio server over one business system's own API
- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full curated list
