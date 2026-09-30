---
title: "Povver MCP - Strength Training Data for Your Assistant"
description: "Povver exposes 38 tools over MCP: read set-level workout history, strength trends and plateau detection, then write routines and periodization plans."
category: Productivity
stars: n/a (no public repo)
added: 2026-09-30
source: "mcp.so feed (Povver - Strength Training)"
relevance: ★★
tags: [fitness, personal-data, read-write, oauth, api-key, remote-mcp, productivity]
---

# Povver MCP

**Your training history, readable and writable from any assistant.** Povver is an iOS strength-training app that logs every set you lift and works out what your training is doing to each muscle group, whether each lift is still climbing, and what should change next. Its MCP server exposes that analysis to Claude, Cursor or any MCP client, and lets the assistant write the change back: build next week's routine and set it active, edit templates, write a finished session, adjust the periodization plan.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in (browser clients) or Bearer API key (Cursor, Windsurf, Claude Code, scripts)
Endpoint: https://mcp.povver.ai/mcp
Tools: 38 (25 read, 13 write, 3 destructive)
Pricing: 14-day free trial, then EUR 9.99/month or EUR 79.99/year
Category: Productivity
Built by: povver.ai
```

## What it exposes

Reads cover your whole history plus everything the analysis derived from it: `check_connection`, `get_user_profile`, `get_training_snapshot`, `explain_rule`, `list_routines`, `get_routine`, `list_templates`, `get_template`, `list_workouts`, `get_workout`, `search_exercises`, `get_strength_climb`, `get_training_insights`, `get_muscle_state`, `get_recommendations`, `get_muscle_group_progress`, `get_exercise_progress`, `query_sets`, `list_trained_exercises`, `get_training_status`, `list_memories`, `get_memory`, `get_recent_suppressions`, `get_periodization_plan` and `preview_periodization_plan`.

Writes cover routines, templates, finished workouts, coach memories, and accepting or dismissing a recommendation: `review_recommendation`, `create_routine`, `update_routine`, `set_active_routine`, `create_template`, `update_template`, `create_workout`, `update_workout`, `update_memory_status`, `save_injury_memory`, `set_periodization_plan`, `pause_periodization_plan` and `resume_periodization_plan`. Three more are marked destructive so the client asks before running them: `delete_workout`, `delete_routine`, `delete_template`.

Clients that support resources and prompts get your training status, active routine, last ten workouts and latest analysis as attachable context, plus four ready-made prompts: a weekly review, what to train today, a single lift's progress, and a program critique. Live set-by-set logging is deliberately not exposed; that stays in the app next to the set grid. A finished session can be written in one call, up to 25 sessions at a time.

## Connecting

For Claude Desktop or claude.ai, add a custom connector named Povver with the server URL `https://mcp.povver.ai/mcp` and no API key, then sign in with your Povver account when prompted. The app's Profile, Integrations, Claude screen walks through the same steps, shows this month's reads and writes with a fourteen-day activity strip and which tools were used, and can disconnect the server.

For clients that cannot sign in through a browser (Cursor, Windsurf, Claude Code, your own scripts), generate an API key under Profile, Integrations, Developer access and send it as a `Bearer` token in the `Authorization` header. Keys are listed with the name you gave them and when they were last used, and any of them can be revoked. The connection works during the 14-day trial and on a subscription, checked on every request.

## Notes

MCP access hangs off your Povver account, so there is nothing to configure beyond the endpoint plus either the OAuth sign-in or a key. Workouts written over MCP are keyed, so resending the same batch after a dropped connection does not double your history, and each tool states whether it is safe to retry. Reads and writes never touch your subscription or account settings. Analysis only starts meaning something after a few sessions of baseline, so weight changes in the first two weeks are mostly calibration.

## See Also

- [Fitness and health MCP servers](/hermes/mcp/servers/external/)
- [Productivity MCP servers](/hermes/mcp/servers/external/)
