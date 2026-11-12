---
title: "How to Rewind a Hermes Conversation Without Losing Context"
description: "Rewind a Hermes conversation in the TUI or CLI: edit an earlier prompt, resend it, or fork from before it, and leave the original transcript intact."
category: guides
tags: ["hermes agent", "sessions", "cli", "tui", "prompt recovery"]
last_updated: "2026-11-12"
canonical: "https://www.corpusiq.io/docs/hermes/guides/conversation-rewind/"
robots: "index,follow"
---

# How to Rewind a Hermes Conversation Without Losing Context

A long agent session usually fails at the prompt, not at the tool. You phrase the request loosely at turn three, the agent spends the next forty turns working from that loose framing, and by the time you notice, the transcript is expensive to throw away and embarrassing to keep.

The old recovery options were both bad. Continue the session and every later turn inherits the wrong premise. Start a new session and you lose the context that made the session worth having: the files it read, the decisions it recorded, the corrections you already made.

Hermes Agent v0.23.0 added a third option. `/rewind` moves the conversation back to an earlier message, so the context after the mistake disappears while the work before it survives.

## What `/rewind` does

In the TUI and the classic CLI, type `/rewind`, or press Esc twice on an empty prompt. Hermes lists your earlier messages in the session. Pick one, then choose what happens next:

- **Edit and resend.** The message you selected becomes the live prompt again, with your correction applied. Everything after it is gone from the working conversation.
- **Fork a new session from before it.** Hermes starts a new session at that point in the history. The original session stays exactly as it was, so you can return to it, compare the two branches, or discard the fork.

The release notes are explicit about the second guarantee: the original session is not mutated by a rewind. Rewinding is a view of history you can walk away from, not an edit that rewrites the record.

This shipped in v0.23.0 ([#144937](https://github.com/NousResearch/hermes-agent/pull/144937), [#148880](https://github.com/NousResearch/hermes-agent/pull/148880); full notes: [v0.23.0 release](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0)). On an earlier version the command does not exist, and the two options below are what you have.

The same release added a smaller habit that prevents some of these rewinds. When an agent asks for approval and you want to reject the action but keep the intent, the approval prompt accepts "No, and tell Hermes what to do instead" - a rejection that carries the correction in the same turn, rather than a rejection followed by a separate message the agent may not connect to it.

## Rewind is not rollback: two different layers

The most common confusion is treating rewind as a file-safety feature. It is not, and the distinction matters when a turn went wrong in both ways at once.

| Layer | Feature | What it moves | Use it when |
|---|---|---|---|
| Conversation | `/rewind` | Messages, and the context the model sees | The prompt was wrong, or the plan was wrong |
| Filesystem | Checkpoints and rollback (shadow git snapshots) | Files the tools changed on disk | A tool edited, moved or deleted something it should not have |

Rewind repairs the reasoning. Checkpoints repair the disk. If an agent misread the task and then wrote forty files, rewinding the conversation leaves the forty files in place, and rolling the files back leaves the bad reasoning in the transcript. Do both, conversation first: once the premise is fixed, a re-run against the restored files is usually clean.

Checkpoints and rollback are documented separately by Nous Research: [Checkpoints & Rollback](https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback).

## When to rewind, when to fork, when to start over

The three moves are not interchangeable, and choosing badly costs a session.

**Edit and resend** when you want the same session to continue and you know exactly what was wrong. The correction is one sentence: a scope you left out, a file you named wrongly, an assumption the agent made that you can now state as a constraint. This is the cheapest move and the one you should reach for first.

**Fork** when you want to keep both outcomes. Two designs, two debugging theories, or a change you are not sure about: fork before the branch point, run the alternative, then read both transcripts side by side. Forking is also the honest move when the session contains work you do not want to disturb, such as a delegated run that is still writing results.

**Start over** when the session is contaminated rather than misdirected: the agent has absorbed a wrong fact, a stale file, or a bad tool result, and every later turn quotes it back to you. A rewind to before the contamination works here, but only if you can name the turn where the bad fact entered. If you cannot, `/new` with a shorter, better-scoped prompt is faster than archaeology.

## What rewind does not fix

Rewind cannot undo what already left the session. Files changed on disk stay changed (use checkpoints). Messages already sent to a channel stay sent. Commits pushed, emails sent, cron jobs created and API calls made are outside the transcript entirely, which is why the approval prompt exists in the first place.

It also does not repair a prompt that was vague in a way you still cannot articulate. If the rewrite is another paraphrase of the same request, the agent will produce the same shape of answer and you will rewind twice. Before resending, convert the correction into something checkable: a file path, a number, a constraint, a definition of done.

One more boundary worth knowing: rewind is described for the TUI and the classic CLI. Desktop and the messaging gateways each keep their own conversation affordances, so do not assume the keystroke travels with you between surfaces.

## FAQ

### How do I rewind a conversation in Hermes?

Type `/rewind` in the TUI or the classic CLI, or press Esc twice on an empty prompt. Hermes lists the earlier messages in the session. Select one and either edit and resend it, which drops everything after it from the working conversation, or fork a new session from just before it. Both options require v0.23.0 or later.

### Does rewinding delete the original session?

No. Forking starts a new session at the chosen point and leaves the original exactly as it was. You can go back to it, compare the two, or discard the fork. The original transcript is the record; the rewind is a branch off it.

### Is `/rewind` the same as rolling back files?

No. `/rewind` moves the conversation and the context the model sees. It does not restore files that tools changed on disk. For that, use the separate checkpoints and rollback feature, which snapshots files in a shadow git repository before destructive operations.

### Can I rewind a session that is still running a turn?

The release notes describe starting `/new` while a turn is still running in the TUI, with the old turn continuing in the background. For `/rewind`, treat the running turn as unfinished work: let it land, then rewind, so you are choosing from complete messages rather than a half-written one.

### What should I do instead of rewinding repeatedly?

Convert the correction into a checkable constraint before you resend: a path, a number, a named file, or a one-line definition of done. Repeated rewinds usually mean the prompt still describes the goal in words the agent cannot verify, not that the agent needs another attempt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I rewind a conversation in Hermes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Type /rewind in the TUI or the classic CLI, or press Esc twice on an empty prompt. Hermes lists the earlier messages in the session. Select one and either edit and resend it, which drops everything after it from the working conversation, or fork a new session from just before it. Both options require v0.23.0 or later."
      }
    },
    {
      "@type": "Question",
      "name": "Does rewinding delete the original session?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Forking starts a new session at the chosen point and leaves the original exactly as it was. You can return to it, compare the two branches, or discard the fork. The original transcript is the record; the rewind is a branch off it."
      }
    },
    {
      "@type": "Question",
      "name": "Is /rewind the same as rolling back files?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "/rewind moves the conversation and the context the model sees. It does not restore files that tools changed on disk. For files, use the separate checkpoints and rollback feature, which snapshots files in a shadow git repository before destructive operations."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do instead of rewinding repeatedly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Convert the correction into a checkable constraint before you resend: a file path, a number, a named file, or a one-line definition of done. Repeated rewinds usually mean the prompt still describes the goal in terms the agent cannot verify."
      }
    }
  ]
}
</script>

*← [All guides](index.md) | [Check an AI answer against your books](check-ai-answer-against-your-books.md) | [Sessions and storage](/hermes/setup/session-cleanup)*

*↑ [Section Home](/hermes/guides)*
