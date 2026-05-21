---
last_updated: 2026-05-21T14:30:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 1 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 02-market-open (ABORT-ENTRIES — no 01-pre-market plan today)
total_value_usd: 100468.18
cash_usd: 38000.00
long_market_value_usd: 62468.18
day_pnl_usd_vs_wed_close: -142.31
day_pnl_pct_vs_wed_close: -0.1414
day_spy_pct_vs_wed_close: -0.4304
day_alpha_bp_vs_spy: +28.9
ytd_pnl_pct: 0.4682
benchmark_spx_ytd: 8.3679
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 738.07
alpha_vs_spx: -7.8997
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
---

# Portfolio — 02-market-open 2026-05-21 (LM Day 1 of 30, 14:30Z / 09:30 ET)

> **Phase note**: This is the **first per-sleeve portfolio snapshot under
> Learning-Month rules**. 02-market-open ran in **ABORT-ENTRIES** mode because
> the 13:00Z 01-pre-market did not fire and no validated trade plan exists for
> today. The 8 inherited Core positions are untouched. Swing/Daytrade/Crypto/
> Options sleeves are all empty as expected on Day 1. See
> `memory/daily/2026-05-21.md` for the full routine log.

## Sleeve summary

| Sleeve     | Cash budget | Used         | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|------------:|-------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis) | $62,468.18 (mark) | 8           | +$468.18    |   +0.755%   | Frozen — no new entries     |
| Swing      |  $15,000    |        $0    |             0  |       $0    |       —     | Empty (no LM plan today)    |
| Daytrade   |  $10,000    |        $0    |             0  |       $0    |       —     | Empty (no LM plan today)    |
| Crypto     |   $5,000    |        $0    |             0  |       $0    |       —     | Empty (no LM plan today)    |
| Options    |   $5,000 (premium) | $0    |             0  |       $0    |       —     | Empty (no LM plan today)    |
| Cash reserve | ≥$3,000   |       —      |             —  |       —     |       —     | $3k earmarked of $38k total |

Total deployable cash for non-Core sleeves once trading resumes: **$35,000**.

## Core sleeve (8 positions, all inherited from Live-Phase exit)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / cushion |
|--------|----------:|----------:|----------:|-------------:|-----------:|---------:|--------:|----------------------|
| VOO    | 49.332341 |  $675.703 |  $678.64  |   $33,478.90 |  +$144.90  |  +0.435% |  33.32% | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.62% |
| MSFT   | 11.521758 |  $404.973 |  $422.52  |    $4,868.17 |  +$202.17  |  +4.333% (best UPL)  |   4.85% | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.83% |
| GOOGL  | 12.047273 |  $387.308 |  $385.06  |    $4,638.92 |   -$27.08  |  -0.580% |   4.62% | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 4.49% (tightest) |
| META   |  7.767476 |  $600.710 |  $601.37  |    $4,671.13 |    +$5.13  |  +0.110% |   4.65% | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 6.65% |
| AVGO   | 11.264102 |  $414.236 |  $420.17  |    $4,732.84 |   +$66.84  |  +1.432% |   4.71% | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / cushion 5.25% |
| V      | 10.256781 |  $325.053 |  $328.22  |    $3,366.48 |   +$32.48  |  +0.974% |   3.35% | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.09% |
| BRK.B  |  6.883950 |  $484.315 |  $476.63  |    $3,281.10 |   -$52.90  |  -1.587% (worst UPL) |   3.27% | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 7.59% |
| LLY    |  3.341161 |  $997.857 | $1,026.78 |    $3,430.64 |   +$96.64  |  +2.899% |   3.42% | 10% trail / 3 sh GTC / HWM $1,037.88 / stop $934.092 / cushion 9.03% |

**Tightest cushion now GOOGL 4.49%** (was AVGO 4.70% at 5/20 close; rotation
on green-tape morning with GOOGL pulling back -1.01% intraday while AVGO
recovered +0.58%). All cushions still > 3% spec-threshold; no log-flag.
Strategy slug for all 8: `core-buy-and-hold`. Trail stops untouched this
routine (no thesis-break, no -10% trigger) — verification re-runs at 03-midday.

Total Core committed: $62,468.18 (62.18% of equity)
Cash retained: $38,000.00 (37.82%)

## Swing sleeve
Empty (0 / 8). $15k budget intact. No entries — no 01-pre-market plan today.

## Daytrade / Scalp sleeve (intraday only — flat by 20:30Z)
Empty (0 / 5). $10k budget intact. ORB / VWAP / gap-fade setups not actionable
without 01-pre-market gap-scan and without POLYGON_API_KEY (not set).

## Crypto sleeve (24/7)
Empty (0 / 4). $5k budget intact. Crypto-trend-follow / weekend-momentum /
mean-reversion all dormant until 01-pre-market produces a screen.

## Options sleeve (Level 3 enabled)
Empty (0 / 6 contracts). $5k premium budget intact. Options BP $69,305 / Level
3 ✓ confirmed operational. Earnings-strangle / long-call-momentum / verticals
all dormant until 01-pre-market identifies candidates.

## Today's trades

**Zero trades — 02-market-open ABORTED entries** because the 13:00Z 01-pre-market
did not fire. Per `routines/02-market-open.md` Step 1 spec, no new positions on
ANY sleeve without a validated pre-market plan. Core sleeve untouched (no
thesis-break, no stop trigger). 15th consecutive no-action routine extending the
Live-Phase exit-week streak (Mon 5/18 → Thu 5/21 02-market-open).

## Pending (not yet opened)

- **NVDA** — Live-Phase Variant-C reservation expired; NVDA candidacy is now
  routed through Swing sleeve `swing-earnings-drift` per `strategy.md` v3.
  **Cannot evaluate today** — needs 01-pre-market to read post-print AH price
  + Day-1 reaction tape. Re-evaluate next valid 01-pre-market (likely 5/22 13:00Z).
- **DCA tranche 3 of 3 (legacy Live-Phase)**: still DEFERRED to 2026-06-21+
  per strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no positions closed in the entire Live-Phase paper run, none in LM)
