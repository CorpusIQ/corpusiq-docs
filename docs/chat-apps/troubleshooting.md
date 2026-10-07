---
description: >-
  Fixes for the common things that stop CorpusIQ answering in Slack or Teams:
  not linked, no AI key, a tool that isn't connected, or the wrong account.
canonical: "https://www.corpusiq.io/docs/chat-apps/troubleshooting/"
robots: "index,follow"
last_updated: "2026-10-07"
title: "Troubleshooting - CorpusIQ Docs"
tags: ["hermes agent", "ai agent", "documentation"]

---

# Troubleshooting

Almost every "it's not answering" comes down to one of four things. Work down
the list - they're in the order you'll hit them.

## "It's asking me to sign in"

The app isn't linked to your CorpusIQ account yet, or your link expired.

- **Slack:** run `/corpusiq-login` and follow the direct message it sends you.
- **Teams:** open the app's personal chat and send `corpusiq-login`. Complete
  Microsoft sign-in and, on first use, explicitly approve the CorpusIQ account
  link. Then send a fresh `corpusiq-login` to finish. The Microsoft and CorpusIQ
  email addresses do not need to match. Never post a code or credential in a
  group chat or channel.

If you linked a while ago and it asks again, complete sign-in again. In Teams,
the command resumes an unexpired account-link attempt; an expired attempt
requires a new sign-in. Resend your question after connecting; the bot does not
automatically replay questions from before sign-in.

See [getting-started-slack.md](getting-started-slack.md) or
[getting-started-teams.md](getting-started-teams.md) for the full flow.

## "It says it needs an AI key"

The chat app uses your own AI key to do the thinking, and one hasn't been set.

Add it in the CorpusIQ dashboard, not in chat:

1. Sign in at [the dashboard](https://www.corpusiq.io).
2. Open your AI key settings.
3. Add a key from OpenAI, Anthropic, or Azure OpenAI and save.

Ask again after saving your provider configuration. CorpusIQ uses your own
configuration and does not fall back to a CorpusIQ-owned provider key when it
is missing. Provider usage charges are separate from your CorpusIQ subscription.

## "It says a tool isn't connected"

You asked something that needs a business tool you haven't linked to CorpusIQ
yet - for example, asking about orders before connecting your store.

The reply points you to connect it. Do that once in the dashboard, then ask the
same question again. The app doesn't guess at data it can't reach, which is why
it asks rather than making something up.

## "The answer is for the wrong account"

If answers look like someone else's data, or you're on a shared computer, the
app may be linked as a different person.

- Sign out: `/corpusiq-logout` in Slack, or `corpusiq-logout` in Teams personal chat.
- Sign back in as yourself.

Each Teams request uses the requesting user's linked CorpusIQ identity. Signing
out and explicitly linking your intended account does not grant other group or
channel participants access to that account.

## The sign-in prompt won't complete (Teams)

If tapping **Sign in** in Teams doesn't finish:

- Make sure you're signed in to Teams with the Microsoft account you expect.
- Send a fresh `corpusiq-login` in the app's personal chat to resume or confirm
  the attempt. After browser approval, return to Teams and send the command
  again. If the attempt has expired, start a new sign-in.
- If it still won't complete, your workspace's sign-in setup may need an
  admin's attention. Tell whoever installed the app, or email
  [support@corpusiq.io](mailto:support@corpusiq.io).

## Still stuck

If none of the above fixes it, email
[support@corpusiq.io](mailto:support@corpusiq.io) with your platform (Slack or
Teams), what you asked, and what came back. The more specific, the faster the
fix.
