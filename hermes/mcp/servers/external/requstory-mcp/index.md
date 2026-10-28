---
title: "Requstory MCP - Map How a Company Works From Its Website"
description: "Maps a company from its public website: journey stages, teams, owners and handoffs, then scores AI readiness and answers questions."
category: Business Intelligence / Process Mapping
stars: ★★★ (keyless public tools, 10 tools live-probed)
added: 2026-10-28
source: "live probe of https://requstory.com/mcp returning HTTP 200 keyless on initialize 200 with serverInfo requstory 1.0.0 and a full tools/list of 10 tools, plus submission issue chatmcp/mcpso #6287 and the vendor docs at requstory.com/developers/api"
relevance: ★★★
tags: [process-mapping, company-research, ai-readiness, customer-journey, org-chart, keyless, streamable-http]
last_updated: "2026-10-28"
---

# Requstory MCP

**Every business has a process nobody wrote down, and the person who knows it left the documentation to whoever answers the next question.**

```
Server type:  Remote (Streamable HTTP), keyless public tools
Endpoint:     https://requstory.com/mcp
Auth:         none for public tools, API key for account tools
Tools:        10 at tools/list
Registry:     com.requstory/mcp
Docs:         requstory.com/developers/api
Repository:   github.com/3d7tech/requstory-cli (MIT, CLI)
```

## Why This Matters for Operators

A company's own website is the only description of its business that it publishes in public. It says which teams exist, what the customer is supposed to do first, where a handoff happens and how many steps it takes before a stranger can buy something. Read carefully, it is an org chart and a process map written by accident.

This server reads it deliberately. `map_website` takes up to six pages of a public site and returns the customer journey, the teams with their owners, the processes and the handoffs between them. Then it does the part that matters: it names the teams with **no owner**, and the checks that competitors pass that this company fails. That is the difference between a research summary and a finding.

## What It Returns, Verified

The endpoint is live and open: a bare `POST initialize` on `https://requstory.com/mcp` returned **HTTP 200** with `serverInfo` name `requstory`, version `1.0.0`, on protocol `2025-06-18`, and a full `tools/list` of **10 tools**. Three are public and need no key at all: `search_companies`, `get_company_score` and `check_ai_readiness`.

The published flow, from the server instructions:

- `search_companies` finds companies Requstory has already mapped and scored, by name or website
- `get_company_score` returns an ease-of-doing-business score out of 100 across four parts: find and understand, get started online, get help, and AI-agent readiness
- `check_ai_readiness` tests whether agents can read, understand and act on any website: bots allowed, readable pages, product data, checkout, help
- `map_website` maps the journey, teams, processes and handoffs from up to six pages, and the map is saved
- `get_map`, `list_maps` and `ask_map` read a saved map and answer questions about it with citations, free from the map's pages and entries by default
- `get_ai_company` builds a made-up company run end to end by agents from real public company maps, teams as agent lanes

## Limits Worth Recording

Account tools (`map_website` job results, `list_maps`, `get_map`, `ask_map`, `get_account`) need an API key from the Requstory profile sent as a bearer token, and the free plan carries credits and a daily map allowance that `get_account` reports. `ask_map` answers from the map's own pages unless `ai=true` is set, which is the honest default and also the one to check before quoting an answer. The scores are computed from public pages only, so a company whose process lives behind a login is scored on what it shows a stranger, which is exactly what the score claims to measure.

## FAQ

### Does Requstory need an API key to be useful?
No. The three public tools, `search_companies`, `get_company_score` and `check_ai_readiness`, answer keyless, so an agent can score a prospect or audit a site's agent-readiness before anyone signs up.

### What does the ease-of-doing-business score actually measure?
Four parts, all from public pages: whether a buyer can find and understand the company, whether they can start online, whether they can get help, and whether an AI agent can read and act on the site.

### Can it map a company that is not in its index?
Yes. `map_website` works on any public website from up to six pages, and the result is saved to the account for `get_map` and `ask_map`.

### Where does the data come from?
Public website pages only. The map is built from what the site publishes, and `ask_map` cites the map's own pages and entries rather than a model's memory.
