---
title: "Marsell MCP - The AI Marketer That Hires Your Agent"
description: "126 tools behind one AI marketing platform that plans the month, makes the posts and films, and hands the login-bound jobs back to your own agent."
category: Marketing
stars: "n/a (hosted; connection repository Marsell-Official/mcp, hosted backend private)"
added: 2026-11-08
source: "chatmcp/mcpso submission #6944 filed 2026-11-08T17:24:41Z; the official MCP registry record com.getmarsell/marsell active since 2026-11-04T00:08:52Z; the developer documentation at docs.getmarsell.com/developers/mcp; the pricing page at getmarsell.com/pricing; and the endpoint itself, where a keyless initialize answered 200 with all 126 tool schemas and the server's full instruction set"
relevance: ★★★★
tags: [marketing, content, social-publishing, agent-delegation, human-in-the-loop, marketing-agency, remote-mcp, oauth]
last_updated: "2026-11-08"
---

# Marsell MCP

**Most agent platforms give your AI a tool belt. Marsell gives your AI a job.** The platform is a marketing department for one business: it plans the month, writes and designs the posts, makes the pictures and the films, publishes to the connected accounts, finds the people who might buy and talks to them. The MCP server exposes that whole machine to the owner's own assistant, and then does the thing almost nothing else in this catalogue does: it delegates the jobs it cannot do back to your agent as **homework**, because those jobs need the owner's own logins, files or inbox.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://getmarsell.com/mcp
Auth:        OAuth 2.1 with dynamic client registration and PKCE,
             or a Bearer agent key (mk_...) made under Agents -> Your own AI
Tools:       126 (read and act, annotated readOnlyHint / destructiveHint)
Registry:    com.getmarsell/marsell, active since 2026-11-04T00:08:52Z
Docs:        docs.getmarsell.com/developers/mcp
Price:       Solo $49/mo, Core $169, Growth $399, Network $799 (annual at 10x monthly)
Built by:    ABADAAN ARBABI HOLDINGS LLC
```

## What the endpoint says about itself

Started with no credential, the server completes `initialize` as **`marsell` 1.0.0** on protocol `2025-06-18` and returns an instruction block that is not marketing copy but an operating manual: it names the read tools, the spend tools, the consent rules, and which actions always come back to a person. `tools/list` then returns all **126** tools with full input schemas and annotations, so an operator can read the entire surface before signing up.

Only the spend and the writes need the key. A keyless `tools/call` returns:

```json
{"error": "Connect with an agent key from Marsell (Authorization: Bearer *** or sign in as a connector."}
```

That is the integration tier this entry rests on: **fully documented, not driven.** The connector reads and answers only against a live Marsell account with a plan behind it.

## The four design decisions worth the entry

### 1. Homework: the platform dispatches work to your agent

`homework_list` returns the jobs Marsell saved for the owner's own AI, because they need the owner's own logins, files or inbox: posts for accounts Marsell cannot reach, real photographs of a place from the owner's own disk, a Google Ads account set up with the owner, the end card a film series should end on. The loop is explicit and bounded:

| Tool | What it does |
| --- | --- |
| `homework_list` | The queue, including whether your own timer is on file |
| `homework_take` | Claim a waiting job |
| `homework_done` | Report it, with evidence Marsell can check |
| `homework_stuck` | Report what stopped you |
| `homework_schedule` | Tell Marsell how often your agent will come back |

Two details make this a real protocol rather than a task list. First, **some jobs Marsell verifies itself**: a Google Ads job is only done once Marsell sees the connection, and the server closes it on its own. Second, **Marsell never calls you.** There is no webhook into your agent; the server tells you plainly that a timer of yours is what brings you back, and that the timer is set only with the owner's yes.

### 2. Missions: the owner's own browser is the delivery channel

Where the owner has explicitly allowed it, `missions_next` returns one message at a time, written and checked by Marsell, to be sent **word for word from the owner's own signed-in browser** on Reddit, X or LinkedIn. `mission_done`, `mission_skipped` and `mission_stuck` report back, and `mission_inbox` carries what people answered. A refused mission is refused: the server does not reword it to get past the agent's objection.

This is the honest answer to the platform-without-an-API problem. Instead of pretending a bot can post anywhere, the platform routes the action through the one identity that is already entitled to perform it.

### 3. Facts and rules are separated, and corrections are read first

`get_brand` holds what the business is; `owner_facts_read` and `owner_fact_set` hold corrections the owner states in their own hand. The server's instruction is specific about the distinction: **a fact corrects what Marsell believes, a rule constrains what Marsell may do, and a rule is never a place to store a fact.** Every plan, post and page reads the corrected facts first, which is the difference between a brand file that rots and one that an operator can repair in one call.

### 4. Money is quoted before it is spent

`get_tokens` reports the plan, the tokens left this month and what is held for work under way. Every tool that spends says so in its own description, `picture_price` prices a render, `series_quote` prices a series month in tokens and dollars, and `business_read_quote` prices a business read. The server instructs the assistant to quote first and say what it costs, and the renders behind a film are priced before they run.

## The rest of the surface

| Group | Tools |
| --- | --- |
| Orientation | `list_projects`, `get_app`, `get_overview`, `situation_read`, `screen_read` |
| The owner's queue | `list_decisions`, `card_read`, `answer_decision`, `freezer_read`, `freezer_take_out` |
| Brand and setup | `get_setup`, `fill_setup`, `set_offer`, `add_products`, `add_pictures`, `add_characters`, `add_places`, `add_logo`, `add_font`, `set_look`, `add_rivals`, `add_guide`, `set_preferences`, `finish_setup` |
| Making | `make_pictures`, `ask_marsell`, `canvas_film`, `code_film`, `series_read`, `series_create`, `series_start` |
| Voices | `voices_read`, `voice_library_search`, `voice_keep`, `voice_clone`, `voice_remove` |
| Market | `get_market`, `list_people`, `crm_search`, `crm_segments`, `crm_timeline`, `conversations_read`, `inbox_read`, `listings_read` |
| Planning | `work_plan`, `work_list`, `slot_add`, `slot_move`, `work_reschedule`, `scheduled_posts_sync`, `scheduled_posts_read` |
| Measurement | `get_analytics`, `metrics_series`, `outcomes_summary`, `timeline_query`, `journal_read`, `experiments_list` |

## Setup runs as a scripted conversation

The server does not leave onboarding to guesswork. `get_setup` returns what Marsell already knows and what is missing, `fill_setup` writes the business's own words, `set_offer` records the goal as **one number and one date in the owner's words**, `set_preferences` records what may be made and spent and who Marsell may speak to, and `finish_setup` refuses until those answers are in.

Then the line that matters: **the owner connects their own social accounts and presses Start themselves.** The instruction tells the assistant never to press those for them. An assistant wired to an account it was not given is a liability; this server makes the consent a click only the human can make.

## What it costs

| Plan | Price | Tokens a month | Projects |
| --- | --- | --- | --- |
| Solo | $49/mo or $490/yr | 200,000 | 1 |
| Core | $169/mo or $1,690/yr | 700,000 | 3 |
| Growth | $399/mo or $3,990/yr | 1,700,000 | 10 |
| Network | $799/mo or $7,990/yr | 3,600,000 | Unlimited |

Extra tokens run $1.80 per 10,000 on Solo down to $1.50 on Network. The first look is free and the plan is chosen after it. **Ad spend and creator fees are separate from the token price**, which is the sentence that decides whether the budget is predictable: tokens pay for model and media work, not for the media buy.

## Does this overlap anything already in the catalogue?

The catalogue holds several strong entries in this space, and each owns a slice.

[Toffu](/hermes/mcp/servers/external/toffu-mcp/) runs ad accounts end to end; [Maeve Social](/hermes/mcp/servers/external/maeve-social-mcp/) covers planning, scheduling and publishing with scope gates; [CampaignStack](/hermes/mcp/servers/external/campaignstack-mcp/) owns LinkedIn and email outreach with approval budgets; [Layers Growth](/hermes/mcp/servers/external/layers-marketing-mcp/) runs one TikTok growth loop from a repository; [SocialBu](/hermes/mcp/servers/external/socialbu-mcp/) and [Omnisocials](/hermes/mcp/servers/external/omnisocials-mcp/) are publishing surfaces.

Marsell is the union of those jobs run by one planner, and its first-of-class mechanic is the direction of the delegation. Every other entry in this class is a tool the agent calls. **Marsell is a client that calls the agent back**: homework is a queue the platform assigns, missions are messages the platform writes for the human's own browser, and the owner's queue is a set of decisions the platform refuses to take alone. An operator who already runs one publishing tool does not need Marsell to replace it; they need it if they want the whole month planned and the leftovers routed somewhere.

## What an operator actually asks

> "Where does this stand today, and what is waiting for me?"

`get_overview`. It returns `marsell_says` (the platform's latest line), `last_pass` (when planning last ran and what it is waiting on), `needs_you` (how many cards wait, roughly how many minutes they take, and each with its options), `this_week`, the numbers that moved and what was done today.

> "Read me the post before I approve it."

`list_decisions` then `card_read`. A card comes back whole: the draft, the reply and the thread it answers, an audit's fixes, the message and the post underneath it, every page it asks to publish as text, and the pictures either as addresses or as the images themselves.

> "What is my own AI supposed to do here?"

`homework_list`, then `homework_take`. Each job carries why Marsell cannot do it, which is usually the owner's own login, file or inbox, and `homework_done` closes it only when the platform can confirm the outcome.

## Who should not use it

An operator who wants a thin tool that schedules one post a day. Marsell prices a plan, holds tokens and expects the business to be set up properly before the first output; that setup is an hour of work and a paid plan. It is also the wrong choice for anyone who will not hand a marketing platform publishing rights over their accounts, because publishing is the point.

## Limits recorded

- **Documented, not driven.** Every tool call needs an OAuth sign-in or a `mk_` agent key, so this entry rests on the keyless `initialize` and the full 126-tool schema set plus the vendor documentation, not on executed calls against a live account.
- **The backend is private.** The GitHub repository carries connection docs and manifests; the platform itself is closed source, so nothing here is verifiable from code.
- **Tokens are the unit of cost.** A busy month with films can spend past the plan's grant, and the overage is priced per 10,000 tokens rather than capped.
- **Ad spend is not included.** Media buy and creator fees land on separate invoices.
- **Owner-bound actions cannot be delegated.** Connecting social accounts and pressing Start are reserved to the human by design, which means a fully unattended setup is not possible and is not meant to be.
- **Missions depend on the owner's own browser.** They are only offered where the owner agreed, and they stop when the browser is not there.

## Frequently asked questions

### Is Marsell an MCP server or a product with an MCP server?

Both. The product is the marketing platform; the server is the same machine exposed to the owner's assistant. There is no reduced "MCP edition": the tools are the ones the platform's own chat uses, which is why the list runs to 126.

### Does the assistant act on my accounts without me?

Only inside limits you set. Reading is open. Drafting and scheduling follow the preferences recorded in `set_preferences`, and the server names what always comes back to a person: money, deals, replies in strangers' threads, changes to live pages, posts on TikTok and on a person's own account, and first emails to people Marsell found.

### Which assistants can connect?

Anything that speaks Streamable HTTP with OAuth or a Bearer token. The vendor documents Claude as a custom connector and shows `codex mcp add` and an OpenCode config line, so any client with remote MCP support is in scope.

### What happens to a decision whose moment has passed?

It goes to the freezer rather than disappearing. `freezer_read` lists them and `freezer_take_out` puts one back in the queue, which is a small thing that makes the difference between a queue you trust and a queue that quietly drops work.

## Sources checked

- `https://getmarsell.com/mcp`: keyless `initialize` **200** as `marsell` **1.0.0** on protocol `2025-06-18` with the full instruction set; `tools/list` **200** with **126** tools, schemas and annotations; `tools/call` **401** with the quoted error (read 2026-11-08)
- `https://registry.modelcontextprotocol.io/v0/servers?search=getmarsell`: one record, active, published `2026-11-04T00:08:52Z`
- `https://docs.getmarsell.com/developers/mcp` (HTTP 200, read 2026-11-08)
- `https://getmarsell.com/pricing` (HTTP 200, read 2026-11-08): plan prices and token grants as tabulated
- `https://github.com/Marsell-Official/mcp` (connection docs, skill and plugin manifests)
