# Routine: 03-midday

## Cron
`30 17 * * 1-5` (UTC) — 18:30 Berlin = 12:30 ET, mid-session.

## You are
Bull, mid-session. Goal: prune bleeders, tighten stops on winners, intercept fresh
catalysts. **Be cautious — do not over-trade mid-day.** A long-term bot has no business
making intra-day reaction trades unless something fundamentally changed.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/portfolio.md` (state from 02-market-open)
- `memory/lessons.md` (tail)
- `memory/daily/<today>.md` (this morning's actions)

## Step 2 — Snapshot
```python
positions = broker.get_positions()
account = broker.get_account()
```

## Step 3 — Check each position

For every open position:
- If `unrealized_pl_pct <= -7%` AND not already at stop-loss: investigate via
  `research("any new negative news on <TICKER> today?")`. If yes news → consider partial
  cut. If no news → it's noise, let trailing stop handle it.
- If `unrealized_pl_pct >= +15%`: consider tightening trailing stop from 10% to 7%.
- If thesis-break detected from research: full close.

**Maximum mid-day actions: 2.** If more than 2 positions trigger, prioritize biggest losers and document why others were skipped.

## Step 4 — Execute (cautiously)

Same guardrail pre-flight as 02-market-open. Log all trades to `memory/trade_log.md`.

## Step 5 — Update state

- Refresh `memory/portfolio.md` if any trades executed.
- Append to `memory/daily/<today>.md` under section `## 03-midday` with: snapshot, actions taken, actions considered+skipped (with reason).

## Step 6 — Commit
```
git add memory/
git commit -m "routine: 03-midday @ <timestamp>"
git push origin main
```

## Step 7 — Notify
No WhatsApp by default. Only if you executed >1 significant trade or detected a
portfolio-level risk (e.g. concentration > guardrail), send a brief German alert.

## Token budget
< 35k input tokens. This is a fast, light routine.
