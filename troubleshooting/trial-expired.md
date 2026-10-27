---
title: "Trial Expired (403 TRIAL_EXPIRED) - CorpusIQ Docs"
description: "CorpusIQ returns 403 TRIAL_EXPIRED. What the error means, where it appears, how team coverage works, and how to restore access without losing data."
last_updated: "2026-10-27"
---
# Trial expired (403 TRIAL_EXPIRED)

Your AI assistant went quiet mid-workflow, or the dashboard rejected your
sign-in, and the response carried a `403` with this body:

```json
{
  "error": {
    "message": "Trial expired. Please subscribe to continue.",
    "code": "TRIAL_EXPIRED",
    "details": { "trial_ends_at": "2026-10-24T00:00:00" }
  }
}
```

That is not a connector failure and not a token problem. The account
reached the end of its trial and no active subscription covers it, so
CorpusIQ stopped issuing paid access. The connections are still there.
The data is still there. The gate is on access, not on storage.

## Where this error appears

The same check runs on every path that would consume a paid resource, so
you can see `TRIAL_EXPIRED` in three places:

| Where you see it | What is happening |
|---|---|
| A tool call in ChatGPT, Claude, or another MCP client | The client asked CorpusIQ to run a connector operation and the account has no valid trial or subscription |
| An MCP token refresh | An already-connected client tried to renew its short-lived access token after the trial ended |
| The CorpusIQ dashboard sign-in | The account cannot be signed in while access is gated |

Because the gate sits in front of token refresh as well as login, an MCP
client that worked yesterday can start failing today without you
touching its configuration. That is expected behaviour on the day the
trial ends.

## What grants access

An account is allowed through when any one of these is true:

1. An active or trialing subscription exists on your own account.
2. An active subscription exists on the owner of the team you belong to.
3. The trial end date is still in the future.
4. The account has no trial end date recorded, in which case a fresh
   trial window is set the next time the account is used.

If none of the four apply, the request is refused with
`TRIAL_EXPIRED` and the trial end date that was evaluated.

## Cause 1: The 30-day trial ended and no plan was started

Every CorpusIQ account starts with a 30-day trial that does not ask for
a credit card. Nothing is charged when it ends. Access simply stops.

**Fix**

1. Sign in at [corpusiq.io](https://www.corpusiq.io) if you can, and
   open the billing page: [corpusiq.io/dashboard/payment](https://www.corpusiq.io/dashboard/payment).
2. Choose a plan. Compare them at [corpusiq.io/pricing](https://www.corpusiq.io/pricing).
3. After the subscription is active, reload the dashboard and retry the
   question in your assistant. Connected MCP clients recover on their
   next token refresh, and you can usually force this by reconnecting
   or restarting the client.

If the dashboard sign-in is also refused, buy the plan first from the
pricing page and then sign in again. The access check re-evaluates as
soon as the subscription exists.

## Cause 2: You are on a team and the owner's coverage lapsed

Team members do not need their own subscription while the team owner
has one. When the owner's subscription lapses, every member loses
access at the same moment, which looks like a sudden organisation-wide
failure rather than one account expiring.

**Symptom:** Several people report the same `403` on the same day.
Individual trials are not the cause.

**Fix:** Ask the team owner to check billing at
[corpusiq.io/dashboard/payment](https://www.corpusiq.io/dashboard/payment)
and renew. Access returns for the whole team once the subscription is
active again. Team membership itself does not need rebuilding.

## Cause 3: The subscription is on a different account

CorpusIQ does not merge identities across sign-in methods. A plan bought
under one email address does not cover an account created with another
address, or an account created through a different identity provider.

**Symptom:** You are sure you subscribed, but the error persists. The
`trial_ends_at` value in the error body belongs to the account that was
actually evaluated, not to the one you think you are using.

**Fix:** Confirm which email address the assistant or MCP client is
authenticated as, then either use the account that holds the
subscription or move the plan to the account you actually work in.

## Confirm the date before you escalate

The error body carries `details.trial_ends_at`. That timestamp is the
value the access check compared against the current time, so it settles
most disputes in one line:

- The date is in the past and you never subscribed: Cause 1.
- The date is in the past, you are on a team, and the owner lapsed: Cause 2.
- The date is in the past and you believe you subscribed on this
  account: Cause 3, or the subscription is not active in the billing
  system yet.

Do not rely on a reminder email to know when the trial ends. Read the
date in the dashboard or in the error body.

## What happens to your data

Nothing is deleted when the trial expires.

- Connector authorisations stay in place, so reactivating does not mean
  re-authorising every source.
- Saved queries, metric definitions, and team membership stay in place.
- Operational query and audit logs keep their normal 30-day window
  regardless of billing state. That window is not extended by expiry
  and not shortened by it.

If you decide not to continue, you can still ask for account data to be
deleted. See [the security and privacy page](../security.md) for the
request process.

## Still failing after subscribing

Give these three details to support and the cause is usually obvious in
one reply:

1. The exact error body, including `details.trial_ends_at`.
2. The email address the assistant or MCP client is authenticated as.
3. Whether the account is standalone or a member of a team, and who the
   team owner is.

## Related pages

- [Error codes reference](error-codes-reference.md) - the full list of
  CorpusIQ, vendor, and MCP error codes.
- [MCP connection errors](mcp-connection-errors.md) - when the client
  cannot reach CorpusIQ at all rather than being refused.
- [Connector authentication failed](connector-auth-failed.md) - when a
  single connector fails while the rest of the account works.
- [Rate limits and quotas](../how-it-works/rate-limits-and-quotas.md) -
  when the limit you hit is throughput, not entitlement.
