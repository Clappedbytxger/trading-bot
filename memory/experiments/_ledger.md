# Experiments Ledger — Learning Month KPIs

Updated by `05-close-summary` daily and `06-weekly-review` weekly. The week-end
strategy-bandit (kill worst, double best) consumes this table.

Window: 2026-05-21 → 2026-06-20.

## How KPIs are computed
- **Trades**: count of closed trades attributable to this strategy.
- **Win-rate**: closed trades with P&L > 0 / closed trades.
- **Avg R**: mean of (P&L / initial-risk) across closed trades. Positive = net gain on R basis.
- **Max DD**: largest peak-to-trough equity drawdown attributable to this strategy.
- **Net P&L**: cumulative $ realized + unrealized.
- **Alpha vs SPY**: strategy daily-return mean - SPY daily-return mean over same window.
- **Cost basis**: budget allocated by sleeve.
- **Risk-adj return (RAR)**: Net P&L / |Max DD|. Used for weekly bandit ranking.

## Ledger

| Strategy slug | Sleeve | Status | Trades | Win-rate | Avg R | Net P&L | Max DD | RAR | Alpha vs SPY | Last update |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| core-buy-and-hold          | Core      | active | 16 fills (T1+T2, no closes) | — | — | +$468.18 (UPL) | $0 (no closes) | — | -7.90% (Live-Phase carryover + LM Day 1) | 2026-05-21 02-open |
| swing-momentum-breakout    | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-mean-reversion       | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-quality-pullback     | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-earnings-drift       | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-insider-buys         | Swing     | paused | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-short-rejection      | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-short-fundamental    | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-orb               | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-vwap-pullback     | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-gap-fade          | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-gap-go            | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| scalp-tape                 | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-news-catalyst     | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| crypto-trend-follow        | Crypto    | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| crypto-weekend-momentum    | Crypto    | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| crypto-mean-reversion      | Crypto    | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-long-call-momentum | Options   | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-protective-put     | Options   | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-vertical-bull-call-spread | Options | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-earnings-strangle  | Options   | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-cash-secured-put   | Options   | paused | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |

## Sleeve roll-ups

| Sleeve | Cash Budget | Used | Open positions | Cumulative P&L | Cumulative Alpha vs SPY |
|---|---:|---:|---:|---:|---:|
| Core     | $62,000 | $62,468.18 (mark, +$468.18 UPL) | 8 | +$492.26 / +0.493% (9-day Live-Phase + LM Day 1 carryover) | -7.90% Live-Phase + LM Day 1 carryover |
| Swing    | $15,000 | $0      | 0 | $0 | — |
| Daytrade | $10,000 | $0      | 0 | $0 | — |
| Crypto   | $5,000  | $0      | 0 | $0 | — |
| Options  | $5,000  | $0      | 0 | $0 | — |
| Cash reserve | $3,000 | — (of $38,000 cash total, ≥$3k reserved per ALM-2) | — | — | — |

## Weekly bandit log (06-weekly-review writes here)

(none yet — first bandit review will fire Fri 2026-05-29 in 06-weekly-review)

## Daily refresh log

- **2026-05-20 EOD (05-close-summary)** — Final Live-Phase EOD pre-LM-start. 0 trades
  across all 22 seeded strategies (Core in HOLD; Swing/Daytrade/Crypto/Options not
  yet active). Per-strategy KPIs unchanged from initialization; `core-buy-and-hold`
  row updated with carryover Live-Phase mark (+$610.31 UPL on $62,610.49 cost-basis,
  -8.24% alpha vs SPY over the 9-day Live-Phase paper run 5/12 → 5/20). All sleeve
  budgets ready for LM Day 1 activation tomorrow 13:00Z.

- **2026-05-21 14:30Z (02-market-open, LM Day 1)** — **ABORT-ENTRIES routine** because
  the 13:00Z 01-pre-market did not fire (4th miss in 9 trading days). 0 trades on any
  sleeve. Only KPI delta: `core-buy-and-hold` UPL drifts $610.31 → $468.18 (-$142.13
  intraday) on broker mid-morning marks. BRK.B leading the drawdown -1.59% UPL, MSFT
  leading gains +4.33%. SPY -0.430% intraday → Core day-alpha so far +28.9 bp (Core
  -0.141% intraday vs SPY -0.430%, alpha from individual-name dispersion). Swing /
  Daytrade / Crypto / Options sleeves remain at 0 trades — no plan = no entries per
  ALM-1. Robin notified via WhatsApp + inbox.md options A/B for unblocking Day 1.
