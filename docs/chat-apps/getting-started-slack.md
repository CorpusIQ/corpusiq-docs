---
description: >-
  Start using CorpusIQ in Slack in three steps: link your account with
  /corpusiq-login, add your AI key in the dashboard, and ask your first
  question.
---

# Getting started in Slack

Three steps, once. After that, asking a question is all that's left.

## Step 1 — Link your CorpusIQ account

The app won't read any data until it knows who you are. Linking connects your
Slack identity to your CorpusIQ account.

1. In Slack, type `/corpusiq-login` and send it. You can do this in a direct
   message to the app or in any channel — the reply comes to you privately.
2. The app sends you a direct message with a link and a short code.
3. Open the link, confirm the code matches, and sign in to CorpusIQ.
4. The app messages you the moment you're connected. The code is good for about
   15 minutes; if it expires, just run `/corpusiq-login` again.

<!-- screenshot: the /corpusiq-login DM showing the link and the confirmation code -->

You only do this once. The app remembers you until you sign out.

If you're already linked and run `/corpusiq-login` again, the app tells you so
— it won't create a second login.

## Step 2 — Set your AI key

CorpusIQ does the thinking with an AI model, and in Slack and Teams you bring
your own key for it. This keeps the AI spend and the data on the model side
inside your own account.

You add the key once, in the CorpusIQ dashboard (not in Slack):

1. Sign in at [the CorpusIQ dashboard](https://www.corpusiq.io).
2. Go to your AI key settings.
3. Paste in a key from OpenAI, Anthropic, or Azure OpenAI and save.

<!-- screenshot: the dashboard AI key setting with a provider selected -->

Until a key is set, the app will tell you it needs one rather than answering
with someone else's — so if your first question comes back asking for a key,
this is the step you're missing.

Your workspace may be set up so the key is already provided for everyone. If so,
you can skip this step — ask a question, and if it answers, you're set.

## Step 3 — Ask your first question

Now the part you're here for. Two ways to ask:

- **Direct message** the app for a private answer.
- **@-mention** the app in a channel (for example, `@CorpusIQ how did sales do
  last week?`) when the answer is useful to the whole channel.

Ask in plain English. A good first question is one you already know the rough
answer to, so you can see the shape of a reply:

> How much revenue did we bring in last month?

> Which ad campaigns spent the most last week?

> How many orders are waiting to ship?

The answer comes back in the thread, formatted — key numbers as tiles, not a
paragraph you have to read twice.

<!-- screenshot: a CorpusIQ answer in a Slack thread showing KPI tiles -->

If the answer needs a tool you haven't connected, the app says so and gives you
a button or link to connect it. Connect it once in the dashboard, ask again,
and the answer is there.

## That's it

You've done the two one-time steps. From here on it's just step three — ask,
read, ask again. For questions worth trying next, see
[asking-questions.md](asking-questions.md).
