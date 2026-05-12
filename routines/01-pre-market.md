# Routine: 01-pre-market

## Cron
`0 13 * * 1-5` (UTC) — 14:00 Berlin, ~1.5h before US market open.

## You are
Bull. It's pre-market. Goal: refresh research, identify catalysts, draft (not execute) trade ideas for the open.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`

## Step 0 — Sync with main
See `CLAUDE.md` → Memory Protocol → Step 0. `git fetch && git merge origin/main` into the
working branch BEFORE reading. End-of-routine: merge working branch back into `main`.

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md` — if `approved: false` or missing, abort. Log to lessons, no other action.
- `memory/portfolio.md`
- `memory/lessons.md` (tail)
- `memory/watchlist.md`
- `memory/trade_log.md` (last 20 entries)
- `memory/research_log.md` (last 7 days)

Use the helpers:
```python
from src.research import research                      # Gemini (default)
from src.research.fundamentals import get_snapshot, get_earnings_date, is_in_earnings_window
```


## Step 2 — Quick account sanity
```python
from src.brokers import get_broker
broker = get_broker()
account = broker.get_account()
positions = broker.get_positions()
clock = broker.get_clock()
```
If `clock.is_open` is True at pre-market time, something is off (early session or wrong tz) — log and continue cautiously.

## Step 3 — Research

**Quantitative side (yfinance, free):**
For each current open position AND top 3 watchlist candidates:
- `get_snapshot(ticker)` — for current price, P/E, margins
- `is_in_earnings_window(ticker)` — flag for guardrail check before any new buy

**Qualitative side (Gemini, free with grounded synthesis):**
For each ticker that yfinance flagged something off (price down >5%, margin shrink) OR has earnings within 7 days:
- `research("Any material news, earnings, downgrades, regulatory action for <TICKER> in the last 24 hours?")`

Then one broader macro query:
- `research("Top US pre-market movers and macro events today (date: <today>) relevant to long-term equity investors.")`

## Step 4 — Decide

Build a **trade-idea draft** (not orders):
- For each open position: hold / trim / close / stop-adjust — with one-line reason.
- For each watchlist candidate: buy / skip / wait — with criteria for entry trigger.
- Respect ALL hard guardrails in `CLAUDE.md`. If a candidate would violate a guardrail, drop it and log to lessons.

## Step 5 — Write

- Append to `memory/daily/<today>.md`:
  ```
  ## 01-pre-market (<timestamp>)
  Account: equity=$X, cash=$Y, buying_power=$Z
  Open positions: <count>, day_pnl: <pct>
  Watchlist focus today: TICKER1, TICKER2, TICKER3
  Catalysts: <bullet summary>
  Draft plan for open:
    - <action> <ticker> @ <conditions> — <reason>
    - ...
  ```
- Append new findings to `memory/research_log.md` (keep it concise — bullet points + citations).
- Do NOT modify `strategy.md` or `portfolio.md` here.

## Step 6 — Commit + open/refresh PR with auto-merge
`main` is branch-protected. Do NOT push to it directly. Use the GitHub MCP PR flow:
```
git add memory/
git commit -m "routine: 01-pre-market @ <timestamp>"
git push -u origin <working-branch>
```
Then in MCP:
1. `mcp__github__list_pull_requests` with `head=clappedbytxger:<working-branch>`, `state=open`
2. If none exists: `mcp__github__create_pull_request` (base=`main`, head=`<working-branch>`,
   title=`routine: 01-pre-market @ <timestamp>`, body links to today's daily file).
3. `mcp__github__enable_pr_auto_merge` (mergeMethod: `MERGE`).
4. End the routine. Do not poll for merge completion.

## Step 7 — Notify
**No WhatsApp** unless an urgent risk emerged (e.g. a current position has critical news). If urgent, send a short German alert.

## Token budget
Aim for < 40k input tokens. Don't ingest full trade_log; use last 20 entries only.
