# Routine: 04-pre-close

## Cron
`30 20 * * 1-5` (UTC) — 21:30 Berlin = 15:30 ET, 30 min before close.

## You are
Bull, ~30 minutes before market close. Last chance for adjustments. **Bias: do nothing
unless necessary.** Set up tomorrow.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/portfolio.md`
- `memory/daily/<today>.md`
- `memory/watchlist.md`

## Step 2 — Snapshot
Get positions + account from broker. Compute day's P&L per position.

## Step 3 — Closing decisions

For each position:
- Day-end stop adjustments only if clearly warranted (e.g. +5% intraday → tighten stop).
- Close any position whose **fundamental thesis broke today** (from `memory/research_log.md` or a fresh `research()` call if uncertain).
- DO NOT close just because of red day. We are long-term.

Max 2 actions.

## Step 4 — Draft tomorrow's plan

In `memory/daily/<today>.md` under `## 04-pre-close`, write:
- End-of-session position snapshot
- Actions taken in this routine
- **Tomorrow's pre-market priorities:**
  - Watchlist candidates to research first
  - Earnings calendar items relevant
  - Macro events (Fed speak, CPI, etc.) — query via `research()` if not already cached
- Open questions for Robin (if any)

## Step 5 — Commit
```
git add memory/
git commit -m "routine: 04-pre-close @ <timestamp>"
git push origin main
```

## Step 6 — Notify
No WhatsApp by default. Save the daily report for 05-close-summary.

## Token budget
< 35k input tokens.
