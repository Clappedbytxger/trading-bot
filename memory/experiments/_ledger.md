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
| core-buy-and-hold          | Core      | active | — | — | — | $+0.00 | $0 | — | — | 2026-05-20 |
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
| Core     | $62,000 | $62,000 | 8 | inherited | — |
| Swing    | $15,000 | $0      | 0 | $0 | — |
| Daytrade | $10,000 | $0      | 0 | $0 | — |
| Crypto   | $5,000  | $0      | 0 | $0 | — |
| Options  | $5,000  | $0      | 0 | $0 | — |
| Cash reserve | $3,000 | — | — | — | — |

## Weekly bandit log (06-weekly-review writes here)

(none yet — first bandit review will fire Fri 2026-05-29 in 06-weekly-review)
