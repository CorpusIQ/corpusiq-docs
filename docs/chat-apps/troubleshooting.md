---
description: >-
  Fixes for the common things that stop CorpusIQ answering in Slack or Teams:
  not linked, no AI key, a tool that isn't connected, or the wrong account.
---

# Troubleshooting

Almost every "it's not answering" comes down to one of four things. Work down
the list — they're in the order you'll hit them.

## "It's asking me to sign in"

The app isn't linked to your CorpusIQ account yet, or your link expired.

- **Slack:** run `/corpusiq-login` and follow the direct message it sends you.
- **Teams:** send the app a message and tap the **Sign in** prompt.

If you linked a while ago and it's asking again, the link timed out — sign in
again and it'll stick.

See [getting-started-slack.md](getting-started-slack.md) or
[getting-started-teams.md](getting-started-teams.md) for the full flow.

## "It says it needs an AI key"

The chat app uses your own AI key to do the thinking, and one hasn't been set.

Add it in the CorpusIQ dashboard, not in chat:

1. Sign in at [the dashboard](https://www.corpusiq.io).
2. Open your AI key settings.
3. Add a key from OpenAI, Anthropic, or Azure OpenAI and save.

Ask again and it'll answer. If you believe your workspace provides a shared key,
check with whoever set the app up — the message means the app read no key for
you.

## "It says a tool isn't connected"

You asked something that needs a business tool you haven't linked to CorpusIQ
yet — for example, asking about orders before connecting your store.

The reply points you to connect it. Do that once in the dashboard, then ask the
same question again. The app doesn't guess at data it can't reach, which is why
it asks rather than making something up.

## "The answer is for the wrong account"

If answers look like someone else's data, or you're on a shared computer, the
app may be linked as a different person.

- Sign out: `/corpusiq-logout` in Slack, or the logout action in Teams.
- Sign back in as yourself.

One person is linked at a time, so signing out and back in puts it right.

## The sign-in prompt won't complete (Teams)

If tapping **Sign in** in Teams doesn't finish:

- Make sure you're signed in to Teams with the Microsoft account you expect.
- Try the message again — send a fresh message to bring the prompt back.
- If it still won't complete, your workspace's sign-in setup may need an
  admin's attention. Tell whoever installed the app, or email
  [support@corpusiq.io](mailto:support@corpusiq.io).

## Still stuck

If none of the above fixes it, email
[support@corpusiq.io](mailto:support@corpusiq.io) with your platform (Slack or
Teams), what you asked, and what came back. The more specific, the faster the
fix.
