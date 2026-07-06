---
description: >-
  The CorpusIQ chat commands for signing in, signing out, and switching which
  account you're using in Slack and Teams.
---

# Commands and your account

There are only a couple of commands to know. Most of the time you won't touch
them — you link once and ask questions from then on. They matter when you're
setting up, stepping away from a shared machine, or switching accounts.

## Signing in

**Slack:** `/corpusiq-login`

Starts the link between your Slack identity and your CorpusIQ account. The app
sends you a direct message with a link and a code; open it, confirm, and sign
in. Full walkthrough in [getting-started-slack.md](getting-started-slack.md).

**Teams:** send the app a message.

If you're not linked, Teams shows a **Sign in** prompt that uses your Microsoft
account. Walkthrough in [getting-started-teams.md](getting-started-teams.md).

You stay linked until you sign out — you don't re-run this before every
question.

## Signing out

**Slack:** `/corpusiq-logout`

Drops the app's link to your CorpusIQ account. After this, the app won't act as
you again until you sign back in. Use it when:

- you're on a shared computer and want to be sure the app isn't still you, or
- you want to switch to a different CorpusIQ account (sign out, then sign back
  in as the other one).

The app confirms when you're signed out. If you weren't linked to begin with, it
tells you that plainly instead of pretending it did something. If the sign-out
doesn't take for any reason, it says so and asks you to try again — it won't
claim you're signed out when you aren't.

**Teams:** the same **corpusiq-logout** action is available from the app's
command menu.

## Switching accounts

If you need the app to act as a different CorpusIQ account — say you have a
personal one and a shared team one — sign out and back in:

1. Sign out (`/corpusiq-logout` in Slack, or the logout action in Teams).
2. Sign in again and choose the account you want.

There's one active account per person at a time in a workspace. Switching is
just sign-out, sign-in.

## A note on privacy

The app always acts as the linked person, using their permissions. Signing in
doesn't give the app more access than you already have — it reads the same
tools you connected, nothing more. Signing out removes the app's ability to act
as you until you choose to link again.
