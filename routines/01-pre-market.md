# Routine: 01-pre-market

## Cron
`0 13 * * 1-5` (UTC) — 14:00 Berlin, ~1.5h before US market open.

## You are
Bull. It's pre-market. Goal: refresh research across ALL active sleeves and produce a
trade-idea draft (NOT execute) for 02-market-open.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`,
`POLYGON_API_KEY` (Learning-Month required).

## Phase Sentinel (first thing)
Check today's UTC date against the CLAUDE.md phase table:
- 2026-05-21 → 2026-06-20: **LEARNING MONTH** mode (this routine extends to all 5 sleeves).
- 2026-06-21+: **LIVE PHASE** mode (only Core sleeve work below applies).

Log the active mode in today's daily file at the start.

## Step 1 — Read
- `CLAUDE.md` (phase sentinel, Learning-Month rules)
- `memory/strategy.md` — if `approved: false`, abort. Log to lessons, no other action.
- `memory/playbook.md` (Learning Month only — active sub-strategies for each sleeve)
- `memory/portfolio.md` (per-sleeve breakdown)
- `memory/lessons.md` (tail 30 entries)
- `memory/inbox.md` (pending replies from Robin)
- `memory/watchlist.md`
- `memory/experiments/_ledger.md` (Learning Month — current KPIs + bandit state)
- `memory/trade_log.md` (last 20 entries)
- `memory/research_log.md` (last 7 days)

Use the helpers:
```python
from src.research import research                      # Gemini (default)
from src.research.fundamentals import get_snapshot, get_earnings_date, is_in_earnings_window
from src.research.polygon import get_aggregates, get_options_chain, get_iv_rank  # Learning Month
```

## Step 2 — Account sanity (all modes)
```python
from src.brokers import get_broker
broker = get_broker()
account = broker.get_account()      # check options_buying_power, daytrading_buying_power, crypto_status
positions = broker.get_positions()  # all asset classes
clock = broker.get_clock()
```
If `clock.is_open` is True at pre-market time, something is off (early session or wrong
tz) — log and continue cautiously (no orders from a late-firing pre-market, see lesson
2026-05-15).

Pull also: **Alpaca `daytrade_count`** in last 5 days (Learning Month — gate on PDT
limit before any Daytrade-sleeve entry).

## Step 3 — Research (per-sleeve)

### 3a) Core sleeve (always)
For each of the 8 Core positions:
- `get_snapshot(ticker)` — current price, P/E, margins
- `is_in_earnings_window(ticker)` — earnings-window check (Core still respects this)
- Flag any name with: price down >5% overnight, margin shrink, downgrade, earnings <7d

Then for any flagged Core name:
- `research("Material news for <TICKER> in last 24h?")`

### 3b) Swing sleeve (Learning Month only)
- Pull Polygon end-of-yesterday aggregates for the Swing watchlist (build it from
  `playbook.md` triggers — momentum-breakout scan, mean-reversion scan,
  quality-pullback scan, short-rejection scan).
- For each candidate matching a trigger: confirm with yfinance fundamentals + Gemini
  news scan (1-2 queries max).
- Pre-flight earnings calendar for each Swing candidate — ALM-7 allows earnings plays
  but ONLY tag them as `swing-earnings-drift`, not the generic momentum strategies.

### 3c) Daytrade/Scalp sleeve (Learning Month only)
- Polygon pre-market scanner: tickers in S&P 1500 with > 3% pre-market move on > 1M
  pre-market volume.
- Classify each: gap-fade candidate (no clean catalyst) vs gap-go candidate (clean catalyst).
- Build watchlist for 02-market-open ORB and VWAP setups.
- **PDT budget check**: if `daytrade_count` will exceed 3 in the next 5-day rolling
  window with planned trades, deprioritize this sleeve until tomorrow.

### 3d) Crypto sleeve (Learning Month only)
- yfinance 24h returns on BTC-USD, ETH-USD, SOL-USD, AVAX-USD, LINK-USD.
- Check `crypto-trend-follow` signal (50/200 DMA cross) and `crypto-mean-reversion`
  signal (-10% intraday flush).
- Gemini news scan for any regulatory/exchange-related risk.

### 3e) Options sleeve (Learning Month only)
- Polygon options-chain on the Swing momentum watchlist — pick names with IV-rank
  data available for spread plays.
- Check earnings calendar (Gemini + yfinance) for any name with earnings in next 5
  days for `options-earnings-strangle` candidates.
- FOMC/CPI/PPI/NFP release calendar — if next 24h has a scheduled release, queue
  SPY OTM put for `options-protective-put`.

### 3f) Macro (always)
One broader macro query:
- `research("Top US pre-market movers and macro events today (date: <today>) relevant to long-term equity investors. Include 10Y yield, DXY, oil, pre-market futures.")`

Flag macro risk-off triggers from strategy.md: SPY -3%/day OR VIX > 40.

## Step 4 — Decide (multi-sleeve trade-idea draft)

Build a draft (NOT orders) per sleeve. For each candidate verify:
- ALM-2 sleeve cash budget not exceeded
- ALM-3 stop pre-set per sleeve rule
- ALM-4 strategy-slug pre-assigned for tagging
- Macro risk-off not active

Output structure:
```
Core sleeve plan:
  - <ticker>: HOLD / TRIM / STOP-CHECK — <one-line reason>
  ...
Swing sleeve plan:
  - <ticker> [strategy:swing-momentum-breakout]: BUY $1.8k @ market, stop $X, target $Y
  - <ticker> [strategy:swing-short-rejection]: SHORT $1.5k @ market, stop $X, target $Y
  ...
Daytrade sleeve plan:
  - <ticker> [strategy:daytrade-orb]: WATCH for 5-min ORB break, $3k notional ready
  ...
Crypto sleeve plan:
  - <coin> [strategy:crypto-trend-follow]: BUY $1.5k if 50>200 cross intact at 14:30Z
  ...
Options sleeve plan:
  - <ticker> [strategy:options-long-call-momentum]: BUY 1 ATM call ~30 DTE if Swing momentum trigger fires
  ...
Macro risk-off active? Yes/No (if Yes, kill all entry plans except defensive Options).
```

## Step 5 — Write

- Create or append `memory/daily/<today>.md` with structured per-sleeve section:
  ```
  ## 01-pre-market (<timestamp>)
  Phase: Learning Month (day N of 30)
  Account: equity=$X, cash=$Y, options_bp=$Z, daytrade_count=$D/3 (in last 5d)
  Open positions by sleeve: Core=8, Swing=N, Daytrade=N, Crypto=N, Options=N
  
  ### Core
  ...
  ### Swing
  ...
  ### Daytrade
  ...
  ### Crypto
  ...
  ### Options
  ...
  
  Macro: <summary>; Risk-off: yes/no
  
  Draft plan for 02-market-open:
    - [sleeve][strategy] <action> <ticker>/<contract> @ <conditions> — <reason>
    - ...
  ```
- Append new findings to `memory/research_log.md` (concise — bullets + citations).
- Do NOT modify `strategy.md`, `playbook.md`, `portfolio.md` here.
- During Learning Month: append to `memory/experiments/<strategy-slug>.md` if a
  new "WATCH" entry is added for a strategy currently inactive in trades.

## Step 6 — Commit
```
git add memory/
git commit -m "routine: 01-pre-market @ <timestamp>"
git push -u origin <working-branch>
```
Then PR-and-merge per CLAUDE.md Memory Protocol Step 0 end-of-routine.

## Step 7 — Notify
**No WhatsApp** unless an urgent risk emerged (e.g. a Core position has critical news,
or macro risk-off triggers). If urgent, send a short German alert per CLAUDE.md
WhatsApp rules.

## Token budget
Aim < 45k input tokens. Don't ingest full trade_log; use last 20. Read
`memory/experiments/<slug>.md` ONLY for strategies with active positions or pending
WATCH entries. Polygon scanner queries should be batched (1 call returning many
tickers, not 1 per ticker).
