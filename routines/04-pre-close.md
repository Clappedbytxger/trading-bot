# Routine: 04-pre-close

## Cron
`30 20 * * 1-5` (UTC) — 21:30 Berlin = 15:30 ET, 30 min before close.

## You are
Bull. 30 min before close. Goal: force-flat the Daytrade sleeve, finalize Swing/
Options stops, prep Crypto for weekend if Friday, draft tomorrow's research priorities.

## Required env vars
`ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `GEMINI_API_KEY`, `POLYGON_API_KEY`.

## Phase Sentinel
Same. Learning Month adds Steps 3b-3e below.

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/playbook.md`
- `memory/portfolio.md`
- `memory/lessons.md` (tail 30)
- `memory/inbox.md`
- `memory/daily/<today>.md`
- `memory/experiments/_ledger.md`
- `memory/trade_log.md` (last 20)

## Step 2 — Account + market state
```python
broker = get_broker()
clock = broker.get_clock()
account = broker.get_account()
positions = broker.get_positions()
```
- Compute time-to-close: `clock.next_close - now`. If > 60min, this routine fired
  early — log and proceed cautiously.
- Pull `daytrade_count` (last 5d) — for the daily summary.

## Step 3 — Per-sleeve actions

### 3a) Core sleeve
- Stop-cushion check (same as 03). If any Core name cushion < 3%: log + flag for
  WhatsApp.
- No trades.

### 3b) Swing sleeve
- For each open Swing: verify stop is still in place at the broker; recompute current
  UPL%. If stop was deleted/replaced by Alpaca for any reason, re-place it.
- Time-stop check: if this is the position's last allowed trading day per playbook,
  close at market.
- Earnings-window check for held names (some Swing strategies allow earnings; verify
  they were entered with `swing-earnings-drift` tag, otherwise this is an inconsistency).
- Optional: tighten stops to breakeven on Swing positions sitting at +5%+ unrealized
  (per playbook-strategy rule — only if strategy mandates trailing).

### 3c) Daytrade/Scalp sleeve — **FORCE FLAT**
- For each open Daytrade position: close at market unless Robin-override pending in
  `inbox.md` to roll to Swing (must have explicit "roll <ticker> to swing" entry).
- If a roll-to-swing is approved: transfer the position from Daytrade sleeve to Swing
  sleeve in `portfolio.md`, document in trade log with new strategy slug
  `swing-daytrade-rollover`, place a fresh stop per Swing-sleeve rules.
- Verify Daytrade sleeve open positions count = 0 after this step. If not, log error
  and try market-close again.

### 3d) Crypto sleeve
- Standard intraday review (same as 03d).
- **Friday-special**: tighten -8% trail to -6% on all open Crypto positions to
  defend against weekend gap risk. Re-widen back to -8% in Monday's 02-market-open.
- If `crypto-weekend-momentum` strategy is queued in playbook (Friday-close long):
  place market buy now at $1-1.5k notional on BTC if up >2% on the week and no
  regulatory news.

### 3e) Options sleeve
- Greeks check via Polygon: theta, delta on each open position.
- 7 DTE rule: if any position has ≤ 7 DTE, close it.
- IV-crush check post-earnings: if an earnings-strangle was held overnight and the
  print already happened, close both legs.
- Verify protective-puts are not stale (e.g., FOMC event passed → close the hedge).

## Step 4 — Plan tomorrow's research

Append to today's daily file:
```
## 04-pre-close (<timestamp>)
EOD targets achieved:
  - Daytrade flat: yes/no
  - Swing stops verified: yes/no
  - Crypto Friday-tighten applied: yes/no
  - Options Greeks reviewed: yes/no

Research priorities for 01-pre-market tomorrow:
  - <ticker>: <why we want to look closer>
  - <macro event>: <what to track>
  - <sub-strategy>: <next trigger we expect>

Pending experiments needing follow-up: <list>
```

## Step 5 — Write
- Update `memory/portfolio.md` with EOD snapshot.
- `memory/trade_log.md` entries for all force-flats and Friday actions.
- `memory/experiments/_ledger.md` KPI refresh.
- Per-strategy `memory/experiments/<slug>.md` for EXITS.
- Daily file section.

## Step 6 — Commit + PR + merge
Per CLAUDE.md.

## Step 7 — Notify
**No WhatsApp** unless urgent (forced-flat failed, macro risk-off active, broker
error). 05-close-summary does the day's WhatsApp.

## Token budget
Aim < 40k input tokens.
