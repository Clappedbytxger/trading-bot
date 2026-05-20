# Routine: 03-midday

## Cron
**Learning-Month (effective 2026-05-21)**: `30 17 * * 1-7` (UTC) — fires daily incl.
Saturday + Sunday for weekend crypto cycling.
**Live-Phase**: revert to `30 17 * * 1-5`. Robin updates this in the Pro-Plan
dashboard when the date sentinel flips on 2026-06-21.

DE-time: 18:30 (summer) / 19:30 (winter). On weekends: crypto-only mode.

## You are
Bull. Mid-session on weekdays / weekend crypto check on Sat-Sun. Goal:
- Weekdays: intraday position management across Swing/Daytrade/Options + Crypto cycle
  + experiment-ledger tick.
- Weekends: Crypto-only cycle (no equity market open). Snapshot-refresh of portfolio.

## Required env vars
`ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `GEMINI_API_KEY`, `POLYGON_API_KEY`.

## Phase Sentinel
Same as 01-pre-market. Skip equity-market sections if it's a weekend.

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/playbook.md`
- `memory/portfolio.md`
- `memory/lessons.md` (tail 30)
- `memory/inbox.md`
- `memory/daily/<today>.md` — pick up morning context
- `memory/experiments/_ledger.md`
- `memory/trade_log.md` (last 20)
- For each open Swing / Daytrade / Options position: read the relevant
  `memory/experiments/<strategy-slug>.md` to refresh thesis + stop targets.

## Step 2 — Account + market state
```python
broker = get_broker()
clock = broker.get_clock()
account = broker.get_account()
positions = broker.get_positions()
```
- Weekday: assert `clock.is_open == True`. If not (early close, holiday), shift to
  end-of-session mode and skip Daytrade management.
- Weekend: `clock.is_open == False` is expected. Skip Steps 3a-3c.

## Step 3 — Per-sleeve actions

### 3a) Core sleeve (weekday only)
- Snapshot prices, recompute UPL%, verify trail-stop cushions.
- If any Core name's cushion < 3% (price approaching stop): log, no action (stops are
  GTC, let them work).
- If a thesis-break event landed since 01-pre-market (Gemini quick scan only for
  flagged names): log + send WhatsApp ad-hoc alert.

### 3b) Swing sleeve (weekday)
- For each open Swing position:
  - Check current UPL%, days-held, distance to time-stop.
  - If time-stop hits today (5d for momentum, 7d for quality-pullback, 10d for earnings-drift, 15d for short-fundamental): close at market or place EOD limit.
  - If stop would have been triggered by intraday low but not yet by close: monitor.
- For 02-pre-planned Swing entries that didn't trigger at open: re-check trigger now,
  place market order if still valid AND playbook-stop still ≤ 7% from current price.
- Macro risk-off recheck (SPY -3% intraday so far / VIX > 40): if active, close ALL
  Swing longs at market, hold cash.

### 3c) Daytrade/Scalp sleeve (weekday)
- For each open Daytrade position: check pace toward target. If 1R achieved, move
  stop to breakeven. If 2R, take profit.
- For ORB/VWAP watches from 01-pre-market: monitor for fresh triggers. Up to 2 new
  Daytrade entries per 03-midday routine.
- For `scalp-tape`: at most 1 entry per day; check PDT-count.
- **04-pre-close prep**: every open Daytrade position MUST flatten by 20:30Z
  (04-pre-close handles forced exits if they're still open).

### 3d) Crypto sleeve (weekday AND weekend)
- Pull current prices for BTC/ETH/SOL/AVAX/LINK.
- For each open Crypto position: recompute UPL, verify -8% trail intact.
- For `crypto-trend-follow`: check 50/200-DMA state, enter if signal flipped since
  yesterday.
- For `crypto-mean-reversion`: check for -10%/24h flush triggers.
- For `crypto-weekend-momentum`: if Saturday and Friday-close-long was placed,
  monitor; if Sunday, prep Monday-morning exit logic.

### 3e) Options sleeve (weekday)
- For each open Options position:
  - Long single-leg: check premium % move vs -50% stop. Force close if hit.
  - Spreads: check time decay (theta); if 7 DTE reached, close regardless.
  - Earnings-strangle: if earnings happened this morning and IV crush played out, close
    the winning leg + take any remaining premium on the loser.
- For 02-pre-planned options entries that didn't fill: recheck contract; if mid still
  reasonable, retry; otherwise drop the idea for the day.

## Step 4 — Update memory
- Rewrite `memory/portfolio.md` per-sleeve.
- Append `memory/trade_log.md` for any executed trades (with `sleeve:` + `strategy:`
  tags).
- Update `memory/experiments/_ledger.md`: increment trade-counts, recompute KPIs for
  closed trades.
- Append to per-strategy `memory/experiments/<slug>.md` for each EXIT / UPDATE.
- Append intra-day section to `memory/daily/<today>.md`:
  ```
  ## 03-midday (<timestamp>)
  Account: equity=$X, cash by sleeve, daytrade_count
  Sleeve actions:
    - Core: ...
    - Swing: ...
    - Daytrade: ...
    - Crypto: ...
    - Options: ...
  Macro risk-off active? Yes/No
  Heads-up for 04-pre-close: forced exits pending = [list]
  ```

## Step 5 — Commit + PR + merge
Per CLAUDE.md.

## Step 6 — Notify
**No WhatsApp** unless an urgent risk (Core thesis-break, macro risk-off triggered
mid-session, broker-side error blocking trades). If urgent: short German message.

## Weekend behavior
On Sat + Sun, this routine:
- Reads memory + account state.
- Updates Crypto sleeve only (Step 3d).
- Logs a brief "weekend-crypto-cycle" entry in daily file.
- Commits + merges PR.
- NO WhatsApp.

## Token budget
Aim < 45k input tokens.
