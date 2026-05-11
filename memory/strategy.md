---
version: 0
approved: false
created: 2026-05-11
last_modified: 2026-05-11
note: "Placeholder. No trades may be placed until version >= 1 AND approved: true."
---

# Active Strategy — NOT YET DEFINED

This file is a placeholder. The active strategy has not yet been approved.

## How to populate this file

1. Run the one-time routine `00-strategy-init` in Claude Desktop.
2. The bot will research the macro context and write 3 candidates to `memory/strategy_candidates.md`.
3. Robin reviews the candidates on GitHub.
4. Robin **manually edits this file** (`memory/strategy.md`) — replaces the contents with
   the chosen variant, bumps `version` to `1`, sets `approved: true`.
5. After commit, the bot's regular cron routines can begin placing trades.

Until then, the bot must operate in **research-only mode** (no trades).
