# Robin's Inbox — bidirectional reply channel for Bull

CallMeBot WhatsApp is **outbound-only** (Bull → Robin). When Bull asks Robin a
question via WhatsApp, Robin's reply has nowhere to land that scheduled routines
can read on the next clone. This file fixes that gap.

## How to use (Robin)

When Bull asks you a question in a WhatsApp message, reply by **editing this file
on GitHub** (web UI is fine — `https://github.com/Clappedbytxger/trading-bot/edit/main/memory/inbox.md`)
and committing directly to `main`. Bull's next routine will start with a `git
merge origin/main` into its working branch and read this file at Step 1 (READ).

**Format**: append a new entry to the top of the "Pending replies" section
below. Use the routine-name + question-shorthand Bull used in the WhatsApp.

```
## <YYYY-MM-DD HH:MM Berlin> — re: <routine-name> <short question label>
<your one-line reply, freeform — Bull will parse it>
```

Bull moves entries from "Pending replies" → "Processed" once acted upon, and
never deletes anything (this is an append-only audit trail).

Replying via WhatsApp text does **not** work today (no inbound listener). Until
a real bidirectional channel is built (Telegram bot / Twilio webhook / GitHub
issues), this file IS the reply channel.

---

## Pending replies

(none — Bull processes from here on each routine's READ step)

## Operational notes (read every routine)

### 2026-05-20 — Learning Month begins 2026-05-21
- CLAUDE.md Phase Sentinel: 5/21 → 6/20 = LEARNING MONTH (all hard guardrails
  paused, sleeve-specific ALM rules active). On 6/21 Live Phase reactivates
  automatically.
- New helpers/data: Polygon.io (POLYGON_API_KEY), Alpaca Options Level 3,
  Alpaca crypto, Alpaca shorting. No Forex (skipped), no Futures (skipped).
- Robin **must update Pro-Plan cron**: `03-midday` extends from `* * 1-5` to
  `* * 1-7` (fires Sat+Sun for weekend crypto). All other routines unchanged.
- Bull may modify `strategy.md`, `playbook.md`, `experiments/*` autonomously
  during Learning Month. PR-diff is Robin's review channel; no pre-approval
  needed for sleeve refinements / strategy-bandit decisions.

---

## Processed

### 2026-05-16 — re: 06-weekly-review tranche-3 A/B (Robin reply via chat session)
- Robin reply: **"B"** (defer T3 ~1 week into post-NVDA + post-Warsh window).
- Channel: Claude Code chat session (the WhatsApp WhatsApp "B" Robin sent never
  reached Bull — CallMeBot is outbound-only; see lesson 2026-05-16).
- Bull action: recorded in `portfolio.md` Pending section + `trade_log.md` as
  deferred decision. Next T3 evaluation window: Thu 2026-05-21 (post-NVDA print
  Wed 5/20 post-close), conditional on the strategy caveat (≥1 -3% red day for
  NVDA specifically) and on macro tape post-Warsh first remarks (Mon 5/18).

### 2026-05-16 — re: strategy_proposals.md DCA-vs-guardrail-#5 (Robin reply via chat session)
- Robin reply: **"akzeptiert, setze um"**.
- Channel: Claude Code chat session.
- Bull action: encoded in `strategy.md` v2 2026-05-16; proposal entry marked
  APPROVED in `strategy_proposals.md`.
