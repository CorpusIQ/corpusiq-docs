---
title: "Yellow Stake Agent Desk MCP - Can This Lead Be Called"
description: "Keyless calling-window, Do Not Call and lead-data checks for US insurance agents, with a statute citation on every answer."
category: "Compliance & Sales Ops"
stars: "n/a (vendor-hosted; registry record com.yellowstake/agent-desk 2.0.0 published 2026-11-28T09:50:45Z, no public repository measured this pass)"
added: 2026-11-28
source: "mcpservers.org slug yellowstake/agent-desk in the 2026-11-28 window, resolved through the official registry to com.yellowstake/agent-desk 2.0.0; keyless initialize 200 as agent-desk 2.0.0 on protocol 2025-06-18, a 7-tool tools/list with full schemas, and fifteen tools/call attempts driven keylessly across calling windows, state rules, lead scrubbing, message checks, lead economics and NANPA lookups"
relevance: "★★★"
tags: [tcpa, insurance, leads, compliance, calling-hours, do-not-call, nanpa, remote-mcp, keyless]
last_updated: "2026-11-28"
---

# Yellow Stake Agent Desk MCP

**A purchased lead has a short life and a long list of ways to waste it: the number is fake, the state has a different calling window than the one you remember, the Sunday rule starts at noon in Texas and at eight in Florida, and the text you are about to send is missing the two lines a carrier's compliance desk will ask about. Agent Desk answers those questions one at a time, keylessly, with a statute citation attached to every answer, and it is the first surface in this catalog that answers *"may I call this person right now"* rather than *"who is this person".***

```
Server type:  Remote (Streamable HTTP, stateless - no Mcp-Session-Id issued)
Endpoint:     https://yellowstake.com/mcp
Registry:     com.yellowstake/agent-desk 2.0.0, published 2026-11-28T09:50:45Z
Auth:         none - initialize, tools/list and every call answered keyless
Tools:        7 (check_lead_contact, check_lead_data, check_outreach_message,
              state_telemarketing_rules, check_calling_window, insurance_lead_cost,
              lookup_phone)
Vertical:     US insurance agents buying leads; the rules cited are federal and state
```

`initialize` answered **200** as `agent-desk` **2.0.0** and shipped an `instructions` block that states its own scope better than most landing pages: *"can I contact this lead (by call, autodialer or text, and when), is this lead bad and returnable, is this message compliant, state telemarketing rules, calling hours, and lead cost. Answers cite their rules and are planning aids, not legal advice. Write any drafts yourself from these facts."*

## What was driven

| Call | Answer |
|---|---|
| `state_telemarketing_rules FL` | Weekdays, Saturday and Sunday **8 a.m. to 8 p.m.**, two time zones, call cap **3 sales calls per person per subject in 24 hours across all your numbers**, state Do Not Call list fed from the national registry, exemptions for an existing business relationship and an express request |
| `state_telemarketing_rules TX` | Weekdays and Saturday **9 a.m. to 9 p.m.**, Sunday **noon to 9 p.m.**, no numeric state cap, automated calls restricted (a sales call needs consent when the mobile user pays), **one-party** recording consent, registered-agent requirement |
| `check_calling_window CA` | Outside hours at 02:04 local; opens **8:00 AM PST**; *"Only the federal window applies"* with 47 CFR 64.1200 and 16 CFR 310.4 cited |
| `check_calling_window TX` Sunday 11:00 CST | Outside; opens **1:00 PM CST** - the noon rule enforced at the boundary, not summarised |
| `check_lead_data` | Verdict **"Likely returnable"** with three flags: no name on the lead, `555-01xx` reserved for fiction, placeholder email - plus a ready return-request message |
| `lookup_phone` | `+130****0142: FL, special` - NANPA data explaining that 555 numbers are kept for directory assistance, fiction and special services, with the middle digits masked |
| `insurance_lead_cost` | 100 leads at 45, 35 percent contact, 8 percent close, 600 first-year commission: **2.8 policies per 100 leads**, **35.71 leads per policy**, **cost per policy 1607.14**, **break-even 16.8 per lead**, **profit per lead -28.2** - the arithmetic reproduced exactly |
| `check_outreach_message` SMS | Verdict **"2 things to fix"**: name yourself and your agency at the start, and never guarantee a rate, savings or approval; the message that omitted an opt-out was told to add one, with FCC 26-67 cited *"from November 25, 2026"* |
| `check_lead_contact FL` | **"Stop: do not contact this lead on any channel"**, then per-channel detail: manual call blocked on the fake number with *"ask the vendor for a credit"*, plus the Do Not Call scrub, the state list and the calling-hour wait, each with its own citation |

The engineering decision that earns the guide is that **the citation travels with the answer**. `"Fla. Stat. § 501.616(6)"`, `"Tex. Bus. & Com. Code § 301.051(b)(2)"`, `"47 CFR § 64.1200(c)(1)"` - a compliance reviewer does not have to take the tool's word for it, and an agent can quote the rule rather than paraphrase the tool. Every rules answer also carries the date it was checked (**2026-11-27** on this read) and the sentence *"This is a guide, not legal advice."*

## The defect: Florida opens at 9, and the same answer says 8

The window gate and the printed rule disagree, and it reproduces on every day of the week:

```
FL Mon 2026-11-30T13:00:00Z  (8:00 AM EST) -> outside, opens 9:00 AM EST
FL Mon 2026-11-30T14:00:00Z  (9:00 AM EST) -> inside
FL Mon 2026-12-01T00:59:00Z  (7:59 PM EST) -> inside
FL Mon 2026-12-01T01:00:00Z  (8:00 PM EST) -> outside
```

So the enforced Florida window is **9:00 a.m. to 8:00 p.m.**, while both `check_calling_window` and `state_telemarketing_rules` print **"weekdays 8 a.m. to 8 p.m.; Saturday 8 a.m. to 8 p.m.; Sunday 8 a.m. to 8 p.m."** for the same state. One of the two is wrong, and an agent reading the text and trusting the text will believe it may call at 8 a.m. and be refused by the tool. The failure is safe in the legal direction - it blocks an hour it might have allowed - but it costs an hour of a purchased lead's contactable life every day, and it means the tool's own text is not evidence of what the tool does.

Two smaller things in the same answer: on a panhandle ZIP (**32501**, Central time) the response prints a single local time (`Mon 08:30`) while an Eastern-time ZIP prints both (`Mon 08:00 / Mon 07:00`), so the two-timezone display is inconsistent; and `check_outreach_message` accepts only `text` - passing `message` returns *"Paste the message, email or script to check"* with `isError: true`, which reads as a validation complaint rather than a key mismatch.

## What it is not

It is not a Do Not Call scrub. `check_lead_contact` tells you to scrub the number against the national registry and the state list; it does not scrub for you, and the same disclaimer repeats it: *"It cannot see your consent records, your Do Not Call scrub or how you send the message."* Nor is it a dialer, a CRM or a consent ledger. It is a **rules oracle and a sanity check** that sits in front of those systems, and the honest use is to call it immediately before a dial or a send, then write the actual outreach yourself from the facts it returns.

## Why an operator who is not an insurance agent should still read it

Because the shape is the one every outbound function is missing. Replace *insurance lead* with *recruiting candidate*, *SaaS trial signup* or *past customer*, and the questions stay the same: what hours may I contact this person in their state, what does this state require me to say at the start of the message, is this number real, and is this list worth what I paid per lead. This server answers those questions for one vertical and cites the statutes; the pattern - compliance as a callable, keyless, cited check before the outbound action - is the part to copy into your own workflow.

## Also worth knowing

Every answer masks phone numbers in its output (`+130****0142`, `+121****0199`), so a log of calls to this server is not a list of numbers. The lead-economics tool takes only the first-year commission, states that renewals make each lead worth more, and asks for your own last-90-days rates rather than vendor benchmarks - the difference between a calculator and a forecast. The `lookup_phone` tool accepts up to **1,000** numbers per call and reads NANPA data refreshed daily, which is the same source that lets `check_lead_data` call a `555-01xx` number fake with a citation instead of a shrug.
