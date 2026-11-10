---
title: "Agent Help Network MCP - Next Action for a Blocked Step"
description: "Keyless lookup that reads a host's robots.txt agent tokens, official API path and status page, then returns one next action when a web step is blocked"
category: Productivity
stars: "n/a (hosted; keyless, stateless, three read-only tools, answered live)"
added: 2026-11-09
source: "chatmcp/mcpso submission #7053 (2026-11-10T03:49:36Z); the endpoint at agenthelpnetwork.com/mcp, driven keyless through initialize, tools/list and four check_incident calls"
relevance: ★★★
tags: [mcp-server, agents, robots-txt, web-automation, blocked-steps, captcha, status-page, keyless, remote-mcp]
last_updated: "2026-11-09"
---

# Agent Help Network MCP

**The hardest failure in an agent's day is the one with no explanation: a 403 that was a 200 yesterday, a login wall after the credentials were accepted, a "verify you are human" page with no code behind it. Agent Help Network answers the question the agent should have asked before retrying, which is what this host has declared for agents, and it ends every answer with one next action.**

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://agenthelpnetwork.com/mcp
Auth:        none; keyless initialize, tools/list and tools/call all answered
Protocol:    2025-06-18, server "Agent Help Network" 0.1.0
Session:     none returned, the server is stateless
Tools:       3, all read-only, all annotated
Publisher:   Agent Help Network (listing filed by the vendor)
```

## What the endpoint actually returns

This is a keyless surface, so the measurement is the whole answer rather than a permission document. A `POST initialize` returns **200** with the standard capabilities plus a `prompts` block and an `instructions` string that is worth reading as the product brief: answers are advisory, the platform's own rules and the user's instructions come first, and thin evidence is a reason to tell the user what was found rather than to guess. `tools/list` returns **three** tools, each carrying MCP annotations that mark them read-only, idempotent and open-world:

```text
check_incident      Check host access profile     site_host, error_class, task_step, failure_stage,
                                                  http_status, challenge, retry_after, via,
                                                  agent_vendor, failed_at, test
rate_last_lookup    Rate the last lookup          token, outcome, path
report_observation  Report an authorized observation   observation
```

A `check_incident` call returns two content blocks: a one-line summary that is meant to be read by the model, and a JSON body with **27** top-level keys for the client. The interesting keys are `next_action`, `recommendation`, `access_profile`, `official_paths`, `current_site_status`, `evidence_level` and `ahn_check`, the last being the server's own probe of the host, which declares its vantage (a data-centre address, the `AgentHelpNetwork` user agent, no cookies or scripts) instead of presenting itself as your browser.

## Four branches, measured on four hosts

The value of the surface is that it does not return one score, it returns one branch. Four calls made in this pass landed on four different ones.

**A robots rule that stops specific agents.** `www.linkedin.com` with `error_class=site_access` answered `next_action.do: use_official_path` with `https://learn.microsoft.com/en-us/linkedin/` and a `stop_if_you_are` list of **six** agent tokens: `ChatGPT-User`, `Claude-User`, `Perplexity-User`, `Meta-ExternalFetcher`, `DuckAssistBot` and `Diffbot-User`. The summary said the restriction applies to requests that send those tokens, which is the correct scoping: a browser-automation client sending a normal browser user agent is not the same request as a retrieval bot declaring itself, and the answer distinguishes them.

**A subdomain with no policy of its own.** `api.github.com` answered `next_action.do: lookup_apex_host` with `lookup_host: github.com` and the line "Policy is read only for a site's main domain, not this subdomain." Look up the apex once, with the same fields, and the site-wide declaration comes back. This is a real design decision made visible: the unit of policy is the host, so a subdomain question is answered by the domain.

**A 5xx with nothing to blame.** `github.com` with `error_class=service_error` answered `next_action.do: proceed` with `https://www.githubstatus.com/` attached, **33** parsed robots rule groups, a full `official_paths` record naming the REST docs and the PAT and OAuth2 authentication routes, and a feedback token for `rate_last_lookup`. In other words: no agent vendor is blocked at the root, this looks like an ordinary failure, retry once and check the status page.

**A check that a person must clear.** `www.nytimes.com` with `error_class=human_verification` answered `next_action.do: hand_off_to_human`: "do not try to solve or bypass the check." The same response listed the NYTimes Developer Network as the official API path, which is the second half of the instruction: hand the human step to the human, and if the data is genuinely needed, take the sanctioned route instead.

`www.amazon.com` returned the same shape as LinkedIn with a different official path, `https://developer-docs.amazon/sp-api/` and seven blocked tokens. One practical note for anyone wiring it up: the prose in the tool description says `host` while the schema field is `site_host`, and a call using the shorter name returns a Pydantic validation error naming `site_host`. Send the schema name.

## The class it enters, with the owners named

Everything catalogued beside this one faces the publisher, not the agent. [AI Crawler Index](/hermes/mcp/servers/external/pathwren-ai-crawler-index/) identifies AI crawlers and generates the robots.txt that expresses a site owner's stance, and [NMOS crawl analytics](/hermes/mcp/servers/external/nmos-crawl-analytics-mcp/) reports what bots actually read on your site. Both are the site's side of the conversation. The reader class, from Avo Cado Read,
a robots-respecting web-to-markdown reader, to Litescrape, respects robots and returns 
the fact that it was blocked, which is honest and leaves the decision to the caller.

Agent Help Network is that decision, made once and handed back as an action: continue, wait, use the official path, hand off to the person, stop retrying, or look up the apex. No catalogued server gives an agent a stop-or-go verdict for a blocked step, and none assembles the robots rules, the developer portal and the status page into one answer. It is first of class for a narrow reason, and the narrowness is the point.

## Why a business operator would want this

An operator does not usually buy an agent to browse; they buy it to finish a task. When the task stalls on a 403, the failure mode that costs money is not the error, it is the loop: retry, change the user agent, retry, hit the wall harder, then report nothing useful. A lookup that returns "this host disallows `Claude-User` at the root and publishes an official API here" converts a dead end into a decision in one call.

There is a second use that matters more for a business: knowing whether a failure is yours or theirs. `current_site_status`, `provider_status`, `failures` and `successes` over a seven-day horizon are the difference between debugging your own integration and waiting for somebody else's incident, and the server is explicit about which of those it can measure.

The privacy design is also worth naming, because it is the part that usually goes wrong. Only the public hostname is sent, never a path, query string or credential; observations are de-identified and enter private review rather than becoming status claims; and the `report_observation` tool refuses names, account details, URLs, cookies and tokens by instruction. An operator can let this run without handing a third party a map of what their agent is doing.

## Limits, stated as limits

It is advisory and host-level. It cannot tell you why a specific page refused you, and it says so: on `api.github.com` the cause came back `undetermined` with `confidence: low` and `basis: [site_probe]`, and on LinkedIn it recorded that it does not measure the site at all because that site's robots.txt disallows its own checker. `evidence_level: no_reports` appeared on every host measured here, which means the community-report half of the product is still thin and the answer rests on the host's public declarations. Its own probe runs from a data-centre address with a declared user agent, so a 200 from its vantage is not a promise of a 200 from your browser. And it never changes the target site or your data, which is a comfort for read-only use and no help at all if what you wanted was a workaround. It will not give you one, by design.

## Frequently asked questions

### What does Agent Help Network do when a page returns a 403?

It looks up the host once, reads the public robots.txt rules for the named agent tokens, finds the official developer or API path, checks the provider's status page, and returns one next action. For LinkedIn and Amazon that action was `use_official_path` with the developer docs URL attached, rather than advice about retrying.

### Does it need an API key?

No. `initialize`, `tools/list` and `tools/call` all answered without credentials in this pass, and no session ID was issued. The server is stateless, so each call stands alone.

### What does "no_reports" mean on the answer?

It means the seven-day community horizon holds no firsthand reports for that host, so the answer rests on the host's own declarations and the server's probe. It is not a healthy-site signal and it is not a fault: four different hosts all returned `no_reports` in this pass because the reporting pool is still small.

### Can it tell me whether a site is down right now?

Partly, and it separates the parts. `current_site_status`, `provider_status` and the `official_status_page` record come from the provider's own status surface, while `ahn_check` is the server's single probe from its own vantage. A single probe is not an uptime measurement and the tool says as much.

### Why does it answer about the whole host instead of the page I called?

Policy is published per host, and the server says so directly: the unit is the host, so a subdomain with no policy of its own gets a `lookup_apex_host` instruction and the domain's declaration. Path-level refusal is outside what it claims to measure.

### Does this replace robots.txt handling inside my own agent?

No. It is a lookup an agent makes when a step is already blocked or when a user asks whether a site allows agents. Your client's own rules and your user's instructions still come first, which the server's `instructions` string states before it states anything else.
