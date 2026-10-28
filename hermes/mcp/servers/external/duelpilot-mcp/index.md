---
title: "Duelpilot MCP - A/B Tests Your Agent Runs, You Approve"
description: "Agent-run A/B testing on your own site: proposals, a brand kit measured from the live page, GA4 goals, and a launch that only a person can approve."
category: Marketing / Growth Operations
stars: ★★★ (401 gated endpoint, no-auth docs endpoint driven live)
added: 2026-10-28
source: "live probe of the account endpoint https://duelpilot.com/api/mcp returning HTTP 401 naming the Bearer token, the no-auth documentation endpoint https://duelpilot.com/agent/mcp driven to HTTP 200 with serverInfo duelpilot.com-site-search 1.0.0 and three tools, and the vendor's agent instruction page at mcpservers.org/servers/duelpilot-com-agents-md"
relevance: ★★★
tags: [ab-testing, experimentation, conversion, ga4, landing-pages, agent-runs, human-approval, mcp]
last_updated: "2026-10-28"
---

# Duelpilot MCP

**A test nobody launches is an opinion with a spreadsheet. The agent does the work here, and a person still presses the button.**

```
Server type: Remote (Streamable HTTP), account-gated
Endpoint:    https://duelpilot.com/api/mcp
Auth:        Bearer token dpl_... scoped to one site, or OAuth in the browser
Docs server: https://duelpilot.com/agent/mcp (no auth, 3 tools)
Guard:       approve_and_launch, ship_winner, resume_experiment need a person's yes
Site:        duelpilot.com
```

## Why This Matters for Operators

Most A/B testing tools assume a growth team with a front-end developer and a quarter to spare. The person running a store or a services site has the traffic and the hypothesis and neither of the other two. What usually happens is that the audit happens, the recommendations get written, and the site does not change.

This server is built the other way round. The agent is the operator: it reads the site, drafts the ideas with evidence, designs the variations, runs the check on phone and desktop, and monitors. The human keeps exactly the decisions that require a person, which the server enforces rather than asks for in a prompt.

That division is the reason to catalogue it. Hypotize in this catalogue plans experiments and does not run them; Duelpilot is the first surface tracked here where the test actually launches, receives traffic and concludes.

## What It Returns, Verified

The account endpoint is gated in the shape its documentation describes. A bare `initialize` on `https://duelpilot.com/api/mcp` returned **HTTP 401** with:

```
{"jsonrpc":"2.0","error":{"code":-32001,
 "message":"Missing or invalid Duelpilot token (Authorization: Bearer ..."}}
```

The separate documentation server is open: `https://duelpilot.com/agent/mcp` answered `initialize` with **HTTP 200**, `serverInfo` name `duelpilot.com-site-search`, version `1.0.0`, and `tools/list` returned three tools, `search_site`, `get_page` and `report_missing`, so the vendor's own guidance can be read by an agent before it holds a token.

The working surface, taken from the vendor's agent instructions:

- **Install and prove control.** `get_install` returns the script tag, `verify_install` checks the live page in real desktop and mobile browsers, and only after that check passes do the tools that fetch pages (`inspect_page`, `run_site_check`, `submit_proposals`) work at all. A passing check is also the proof that the user controls the site.
- **Measure the site instead of guessing.** Right after a passing check the server measures the live site in two browsers and returns colours by role, fonts, radius, button styles and CSS design tokens from `get_brand_kit`.
- **Set the target.** `propose_goal` takes the primary conversion plus one or two guardrails and checks the selector, URL rule or event before accepting it; a goal it cannot check needs the person's words instead.
- **Draft with evidence.** `start_agent_run` with `agent: "analyst"` returns the Analyst instructions, and `propose_ideas` requires **two pieces of evidence per idea** plus `url_rules` and an ICE score, so an idea without a reason is not submittable.
- **Design and check.** `start_agent_run` with `agent: "designer"` designs two to four proposals, `submit_proposals` dry-runs them, and each proposal gets a preview link and a site check on phone, tablet and desktop.
- **Launch only with consent.** `approve_and_launch` returns the exact summary (versions, goal, traffic, price if it starts a plan) and only accepts an explicit yes echoed back with its `summary_hash`. `ship_winner` and `resume_experiment` follow the same rule.
- **Code tests.** A test can be a code variation rather than a visual one: the flag key is the experiment key (`e12`), arms are `c` for control and `v1` to `v3`, and `null` always means control.

## The Gate That Earns the Entry

The server refuses in the direction that matters. Switching autopilot on, changing the consent mode, signing in to Google on the user's behalf and starting billing are not tools at all; they are described as the user's own clicks, and `get_owner_actions` returns each one with its exact URL instead of a menu path.

Every failure answers `{ok:false, code, message, fix}` and the codes are honest about whose problem it is: `HUMAN_ONLY` means a person decides, `PLAN_REQUIRED` and `BILLING_REQUIRED` carry the link the person needs, `NOT_INSTALLED` and `NOT_CLAIMED` say the setup is incomplete, and `CONFIRMATION_MISMATCH` fires when what the user agreed to is no longer what is waiting, so the agent has to show the new version rather than reuse the old yes. That is a better containment shape than a permission flag, because it cannot be talked around.

## Limits Worth Recording

The token is scoped to **one site**, so an agency running several sites holds several connections. Nothing runs before the workspace is claimed and a plan chosen, and the claim link is a person's click. Measurement rides on the installed script tag plus a GA4 property the user selects, so a site without analytics access gets weaker evidence. Tests need traffic to conclude, and the server does not supply it. Autopilot exists but is the owner's setting, which means an agent cannot make the system decide on its own.

## FAQ

### Can my agent launch a test without me?
No. `approve_and_launch`, `ship_winner` and `resume_experiment` all require an explicit yes plus the matching `summary_hash`. The agent can draft, design and check, and then it hands over the summary and the links.

### Do I need an MCP client?
No. The API is stateless JSON-RPC, so a plain `curl` POST with a `tools/call` body works, and the vendor documents `tools/list` and a `setup` prompt for guided setup.

### What stops the agent from designing junk?
`propose_ideas` requires two pieces of evidence per idea and an ICE score, and every proposal is checked in a real browser on phone, tablet and desktop before the person sees it.

### Does it work for shops that are not on Shopify?
Yes, the install is one script tag on any site the user controls. `verify_install` is the gate, so a site that cannot be fetched cannot be tested.

### Where does the brand come from?
From the live page. The server measures colours by role, fonts, radius and design tokens in desktop and mobile browsers, and any brand guidelines the user uploads are read into structured rules that block a version carrying a banned phrase.
