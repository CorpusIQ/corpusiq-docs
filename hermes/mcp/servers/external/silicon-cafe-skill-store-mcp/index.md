---
title: "Silicon Café Skill Store MCP - Audit Before You Install"
description: "A keyless store of 43,000 agent skills with a pre-install audit tier, per-skill findings by category, and a feed of tier changes and recalls."
category: "Agent Tooling"
stars: "n/a (hosted store; 1vr.com)"
added: 2026-11-27
source: "mcp.so /feed card `/servers/silicon-caf-skill-store` stamped 11/27/2026 08:42 AM UTC; keyless initialize 200 as 1vr-skill-store 1.0.0 on protocol 2025-06-18 at https://1vr.com/mcp/skill-store, a 6-tool tools/list, and ten tools/call requests driven on 2026-11-27 (search_skills on invoice and on quickbooks, get_skill 42077, check_skill 42077 and a name-based miss, get_install_info 42077, skill_status_feed, top_skills twice)"
relevance: "★★"
tags: [agent-tooling, skills, audit, supply-chain, security, registry, keyless, remote-mcp]
last_updated: "2026-11-27"
---

# Silicon Café Skill Store MCP

**An agent that installs whatever a search result names is the largest unmanaged supply chain in a small business's stack.** A skill is a folder of instructions and scripts that runs with whatever access the agent has, and until recently the only vetting was a README and a star count. Silicon Café (operated as the 1VR Skill Store) collects agent skills from several sources, runs a static pre-install audit on each, and exposes the record over MCP: search the store, read a skill's audit findings by category, and subscribe to the tier changes and recalls the store publishes.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://1vr.com/mcp/skill-store     keyless, no account
Auth:         none for search and audit; an optional 1VR agent key is recorded
Server:       1vr-skill-store 1.0.0, protocol 2025-06-18
Tools:        6, from a keyless tools/list
Store size:   43,000+ skills (the tool's own description; the mcp.so filing says 30,000+)
```

This is one of the few surfaces this catalog carries where every tool answers **without a credential**: `initialize` and `tools/list` return **200**, and `tools/call` returns real payloads on the same unauthenticated connection.

## The six tools, read from the live list

| Tool | What it returns |
|---|---|
| `search_skills` | Matching skills with id, name, tagline, category, language, author, source, install text and the recorded audit tier |
| `get_install_info` | One skill's ready-to-run install string and source link, with the anonymous request flagged as not recorded |
| `check_skill` | The audit record for one skill id: tier, when it was checked, and findings by category |
| `get_skill` | The full store record for one skill id, including the complete description |
| `skill_status_feed` | Recorded tier changes from the store audit log, newest first, including recalls |
| `top_skills` | The most-looked-up skills by recorded store lookups |

## What a driven record looks like

`get_skill` on id **42077** returned `mcf-accounting-tool`, sourced from ClawHub, category `其他`, language `en`, install text `openclaw skills install @cameron48/mcf-accounting-tool`, and the tier **notice** recorded at `2026-11-27T10:01:27+00:00`. The findings block behind that tier:

```
permissions: 0    network: 0    credentials: 0
suspicious: 0     dependencies: 1  (install_metadata)
meta: source_kind=basic, source_chars=0, reason=source_unavailable, rules=v1
```

**Read that carefully, because it is the whole limitation of a static tier.** The scan found no permission, network or credential claims, because it never saw the source: `source_chars` is **0** and the reason is `source_unavailable`. The single dependency signal is the install string itself. The vendor states the caveat in the tool's own output: *"tier summarises static audit signals only; a tier is not a safety endorsement and is not a security guarantee."* A `notice` here means "the store could only read metadata", not "something is wrong".

## The status feed is the part worth subscribing to

`skill_status_feed` returned four entries, and the shape is a real change log rather than a static badge:

| When (UTC) | Skill | Change | Reason |
|---|---|---|---|
| 2026-11-27T07:40:24 | 1876 `e2etest` | notice to notice, type **recall** | `new_high_risk_signal` |
| 2026-11-25T10:20:52 | 392 `i18n-helper` | clear to notice | `source_changed_recheck` |
| 2026-11-25T10:20:52 | 182 `error-translator` | clear to notice | `source_changed_recheck` |
| 2026-11-25T10:20:52 | 127 `zh-readme` | notice to clear | `source_changed_recheck` |

The first row is the one an agent should act on: a skill recalled for a **new high-risk signal** while its tier label stayed the same, so a reader watching the tier alone would never see it. The other three are re-checks after a source change, which is the correct behaviour for a moving target: a skill that was clear in October is not clear in November just because the file did not move.

## How the ranking is actually computed

`top_skills` lists twenty rows by `heat` and, read field by field, the label means audits rather than installs:

```
1.  nano-banana (#66)         tier=risk     heat=417   install_hits=0  audit_hits=417
2.  skill-community-ops (#900) tier=clear   heat=126   install_hits=0  audit_hits=126
3.  payments-ar (#1000)        tier=notice  heat=116   install_hits=0  audit_hits=116
6.  feishu-lark (#800)         tier=risk    heat=84    install_hits=0  audit_hits=84
```

Every one of the twenty rows carries `install_hits: 0`, so "most looked up" in this pass is **most audited**. That is a defensible measurement, but the tool description sells it as install fetches plus audit checks, and on an anonymous connection only one of those two counters moves. The top of the list is also the least comfortable row in the store: `nano-banana` is ranked first at **417** audits and its recorded tier is **risk**.

## What it is not

- **It is not a security review.** Static signals over metadata, with a tier that downgrades to `notice` when the source could not be read at all.
- **It does not install anything.** Every tool returns an install string owned by another source; the agent still decides what to run.
- **It is English-facing and Chinese-labelled.** Categories come back as `其他`, `效率办公`, `生活服务`, `内容创作` and `社交社区`, and the share snippet rendered for a skill is Chinese-only, while `lang` reads `en`.
- **Its counts disagree with its own listing.** The live tool description says **43,000+** skills; the submission filed to mcp.so says **30,000+**. Both are recorded rather than one.

## Three defects recorded

1. **`check_skill` and `get_skill` take an integer `skill_id`, not a name.** Passing a slug answers HTTP 200 with `isError: true` and *"argument 'skill_id' is required and must be an integer"*, which is honest but means an agent must resolve a name through `search_skills` first.
2. **Taglines are truncated mid-word** in search results and in `get_install_info` (`... and…`), while the same record's `detail_excerpt` carries the full sentence. A client that renders only the tagline shows a broken description.
3. **The text header states the total, not the page.** `search_skills` with `limit: 1` returned exactly one row and still opened with *"160 skills matched."* The `limit` argument is honoured on both `search_skills` and `top_skills` (1 and 3 returned 1 and 3), so the count is not a page size, and a reader that parses the text line rather than the structured `results` array over-reports what it received.

## Frequently asked questions

### Do I need an API key to use the store?

No. Search, audit and ranking all answer on an unauthenticated connection. A 1VR agent key, when present, is written into the store's install log, so the difference is whether your lookups are recorded, not whether they work.

### Is a "clear" tier a green light to install a skill?

No, and the vendor says so in the payload. The tier summarises static signals and is explicitly not a security endorsement. Treat `clear` as "nothing was flagged in what the store could read", and treat `notice` on a skill with `source_chars: 0` as "nothing was read at all".

### Why watch the status feed instead of the tier?

Because a recall can arrive without a tier change. Skill **1876** was recalled for a new high-risk signal while its tier stayed at `notice`, so the feed is the only surface that reports it.

### Is this a store for one agent framework?

No. Install strings in one search cover OpenClaw, plain `git clone` from a GitHub repository, `npx skills add` and framework-specific plugins, because the store indexes several sources rather than one marketplace.

## Business relevance

- **Operators enabling agent skills** get one place to check what a skill claims before it runs with the agent's access.
- **Security-minded teams** get a change log of tier flips and recalls, which is the shape an internal review process needs.
- **Anyone comparing skill sources** sees ClawHub, GitHub and framework marketplaces side by side with the same audit fields.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
