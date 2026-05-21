---
last_updated: 2026-05-21T16:38:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 1 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 03-midday (HOLD — abort-entries posture continued; crypto scan = no signal)
total_value_usd: 100504.44
cash_usd: 38000.00
long_market_value_usd: 62504.44
day_pnl_usd_vs_wed_close: -106.05
day_pnl_pct_vs_wed_close: -0.1054
day_spy_pct_vs_wed_close: -0.3292
day_alpha_bp_vs_spy: +22.4
ytd_pnl_pct: 0.5044
benchmark_spx_ytd: 8.4395
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 738.81
alpha_vs_spx: -7.9351
position_count_total: 8
position_count_core: 8
position_count_swing: 0
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.62
options_buying_power_usd: 69305.24
options_approved_level: 3
daytrade_count_5d: 0
pattern_day_trader: false
cash_reserve_min_usd: 3000
cash_available_for_non_core_usd: 35000
sleeve_budget_swing_usd: 15000
sleeve_budget_daytrade_usd: 10000
sleeve_budget_crypto_usd: 5000
sleeve_budget_options_premium_usd: 5000
sleeve_used_swing_usd: 0
sleeve_used_daytrade_usd: 0
sleeve_used_crypto_usd: 0
sleeve_used_options_usd: 0
polygon_api_key_set: false
macro_risk_off_active: false
vix_current: 17.24
---

# Portfolio — 03-midday 2026-05-21 (LM Day 1 of 30, 16:38Z / 12:38 ET)

> **Phase note**: 03-midday snapshot under Learning-Month rules. Abort-entries
> posture from 02-market-open is continued (per 02-open routine plan: "if
> 01-pre-market still has not back-fired by 03-midday, continue to hold
> abort-entries posture for all non-Core sleeves until the next valid
> 01-pre-market cycle"). No trades executed. Core stops intact and verified
> live; LLY trail HWM advanced intraday. Crypto scan: all 5 universe names in
> 50<200 DMA downtrend → no `crypto-trend-follow` signal. Macro: no risk-off
> (SPY -0.33% intraday, VIX 17.24).

## Sleeve summary

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,504.44 (mark)     |             8  |  +$504.44   |   +0.813%   | Frozen — stops live, AVGO cushion tightened to 3.69% (near 3% threshold but not under) |
| Swing      |  $15,000             |        $0             |             0  |       $0    |       —     | Empty (abort-entries Day 1)  |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     | Empty (abort-entries Day 1; POLYGON_API_KEY unset blocks ORB/VWAP/scalp regardless) |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     | Empty — scan run, no entry signal (all 5 universe names 50<200 DMA downtrend; no -10% flush) |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     | Empty (abort-entries Day 1)  |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     | $3k earmarked of $38k total  |

Total deployable cash for non-Core sleeves once trading resumes: **$35,000**.

## Core sleeve (8 positions, all inherited from Live-Phase exit)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / cushion |
|--------|----------:|----------:|----------:|-------------:|-----------:|---------:|--------:|----------------------|
| VOO    | 49.332341 |  $675.703 |  $679.37  |   $33,514.84 |  +$180.84  |  +0.543% |  33.35% | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.71% |
| MSFT   | 11.521758 |  $404.973 |  $417.18  |    $4,806.59 |  +$140.59  |  +3.014% |   4.78% | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.65% |
| GOOGL  | 12.047273 |  $387.308 |  $388.59  |    $4,681.45 |   +$15.45  |  +0.331% |   4.66% | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 5.36% |
| META   |  7.767476 |  $600.710 |  $601.23  |    $4,670.04 |    +$4.04  |  +0.087% |   4.65% | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 6.63% |
| AVGO   | 11.264102 |  $414.236 |  $413.36  |    $4,656.10 |    -$9.90  |  -0.212% |   4.63% | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.69% (tightest)** |
| V      | 10.256781 |  $325.053 |  $331.10  |    $3,396.02 |   +$62.02  |  +1.859% |   3.38% | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.89% |
| BRK.B  |  6.883950 |  $484.315 |  $479.13  |    $3,298.27 |   -$35.73  |  -1.071% |   3.28% | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.08% |
| LLY    |  3.341161 |  $997.857 | $1,038.06 |    $3,468.33 |  +$134.33  |  +4.027% (best UPL) |   3.45% | 10% trail / 3 sh GTC / **HWM $1,043.382 ↑** / stop $939.0438 ↑ / cushion 9.54% |

**Stop-cushion rotation since 14:30Z snapshot:**
- **AVGO** went from 5.25% → **3.69%** cushion (mark $420.17 → $413.36, -1.62% intraday). Still ≥ 3% spec-threshold → no log-flag, but trending toward it; will monitor at 04-pre-close.
- **GOOGL** widened from 4.49% → 5.36% (recovered $385.06 → $388.59 intraday).
- **LLY** HWM advanced $1,037.88 → **$1,043.382** intraday (broker mark $1,038.06, but Alpaca trail tracks intraday high); trail stop bumped $934.092 → **$939.044** (+0.53%). Only Core name with a stop-advance today.
- All 8 trail orders verified `OrderStatus.NEW` GTC via live broker query (open-orders endpoint).

**Tightest cushion now AVGO 3.69%** (was GOOGL 4.49% at 14:30Z, was AVGO 5.25%
at 5/20 close). The intra-routine flip — AVGO from highest-cushion-of-the-day
at open ($420.17 / 5.25%) to tightest cushion at 12:38 ET — is normal sleeve
dispersion on a flat-tape day; no Core thesis-break event registered (Gemini
scan not run — no specific flag).

Strategy slug for all 8: `core-buy-and-hold`. No Core actions taken this
routine.

Total Core committed: $62,504.44 (62.19% of equity)
Cash retained: $38,000.00 (37.81%)

## Swing sleeve
Empty (0 / 8). $15k budget intact. Abort-entries continued from 02-open per
LM-Day-1 plan; no 01-pre-market screen exists to validate.

## Daytrade / Scalp sleeve (intraday only — flat by 20:30Z)
Empty (0 / 5). $10k budget intact. No open positions to flatten by
04-pre-close. ORB/VWAP/scalp/gap strategies all need Polygon real-time
1-min aggregates; POLYGON_API_KEY remains unset → would be blocked even if
a plan existed.

## Crypto sleeve (24/7)
Empty (0 / 4). $5k budget intact. Scan result (yfinance daily 1y):

| Symbol   | Last      | 50-DMA    | 200-DMA   | State                  | 24h Δ   | 5d Δ   | Signal? |
|----------|----------:|----------:|----------:|------------------------|--------:|-------:|---------|
| BTC-USD  | $77,041   | $76,201   | $80,938   | 50<200 (downtrend)     | -0.54%  | -1.40% | none    |
| ETH-USD  | $2,124.89 | $2,261.83 | $2,566.98 | 50<200 (downtrend)     | -0.10%  | -2.52% | none    |
| SOL-USD  | $86.17    | $86.11    | $108.26   | 50<200 (downtrend)     | +0.15%  | -0.42% | none    |
| AVAX-USD | $9.34     | $9.37     | $11.28    | 50<200 (downtrend)     | +0.61%  | +0.53% | none    |
| LINK-USD | $9.63     | $9.44     | $10.99    | 50<200 (downtrend)     | +0.04%  | -0.97% | none    |

- `crypto-trend-follow`: all 5 names in downtrend → no entry signal anywhere.
  BTC closest to a flip (50-DMA $76.2k vs 200-DMA $80.9k = -5.86% gap; would
  need either a sustained rally or rolling-200 decay to flip).
- `crypto-mean-reversion`: no name down >10% / 24h → no trigger.
- `crypto-weekend-momentum`: not applicable Thursday afternoon (would fire at
  05-close-summary Friday 21:15Z).

## Options sleeve (Level 3 enabled)
Empty (0 / 6 contracts). $5k premium budget intact. Options BP $69,305 / Level
3 ✓. POLYGON_API_KEY unset blocks options-chain reads; earnings-strangle /
long-call-momentum / verticals all dormant.

## Today's trades

**Zero trades — 03-midday HOLD** (abort-entries posture continued from 02-open
per the LM-Day-1 fallback plan). Core sleeve untouched (no thesis-break, no
stop trigger). LLY's GTC trail HWM advanced organically intraday — that's the
broker tracking the high-water-mark, not a Bull action. 16th consecutive
no-action routine extending the Live-Phase exit-week streak.

## Pending (not yet opened)

- **NVDA Swing entry candidate** (`swing-earnings-drift`): blocked — needs
  01-pre-market for post-print Day-1 reaction tape. Re-evaluate next valid
  01-pre-market (5/22 13:00Z).
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no closes in entire Live-Phase paper run + LM Day 1)
