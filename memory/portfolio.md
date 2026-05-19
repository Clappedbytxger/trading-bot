---
last_updated: 2026-05-19T13:33:00Z
broker: alpaca
account_type: paper
total_value_usd: 100365.22
cash_usd: 38000.00
day_pnl_pct_vs_mon_close: -0.3190
day_spy_pct_vs_mon_close: -0.5889
day_alpha_bp_vs_spy: +27.0
ytd_pnl_pct: 0.3652
benchmark_spx_ytd: 7.7777
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 734.30
alpha_vs_spx: -7.4125
ytd_alpha_narrowing_vs_mon_close_bp: +31.7
position_count: 8
leverage_x: 0.62
---

# Portfolio — 02-market-open 2026-05-19 (open snapshot, 13:33Z / 09:33 ET)

## Open snapshot vs Mon (5/18) close

| Metric                  |  Mon close (20:15Z) | Tue open (13:33Z) |  Δ                |
|-------------------------|--------------------:|------------------:|------------------:|
| Equity                  |         $100,686.35 |       $100,365.22 |  -$321.13 (-0.32%) |
| SPY                     |             $738.65 |           $734.30 |  -$4.35 (-0.589%) |
| Cash %                  |              37.74% |            37.86% |  +0.12 pp         |
| Position count          |                  8  |                8  |       0           |

- **Day P&L: -$321.13 (-0.319%) vs SPY -0.589%** → **day alpha +27.0 bp** at open.
  Defensive ballast + cash sleeve doing the relative-performance work on a weak-tape
  open (futures led red overnight on hawkish-Warsh tape + Iran-strike-cancellation
  oil-down + 10Y at 4.61%).
- **YTD: Bull +0.365% vs SPX +7.778% → Alpha -7.413%.** Vs Mon close alpha (-7.730%):
  **+31.7 bp narrowing** into the open. First reading of "AI-Capex Barbell" working
  on a real weak-tape day.

## Open positions (broker mark @ 13:33Z)

| Symbol | Qty       | Avg Entry | Open Mark  | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Fri | Trail Stop                                                |
|--------|----------:|----------:|-----------:|-------------:|---------------:|---------:|--------:|-------:|-------------:|-----------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |   $675.085 |   $33,303.52 |        -$30.48 |  -0.091% |  33.18% | 50% (Core) | -0.526%   | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.13% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |   $426.850 |    $4,918.06 |       +$252.06 |  +5.402% (best UPL) |   4.90% |  7% | +0.731%   | 10% trail / 11 sh GTC / **HWM $432.70** (auto-advanced from $428.17) / **stop $389.43** / cushion 8.77% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |   $392.840 |    $4,732.65 |        +$66.65 |  +1.428% |   4.72% |  7% | -1.015%   | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.75 / cushion 6.39% — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |   $606.800 |    $4,713.30 |        +$47.30 |  +1.014% |   4.70% |  7% | -0.622%   | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.36 / cushion 7.49% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |   $414.810 |    $4,672.46 |         +$6.46 |  +0.138% |   4.66% |  7% | -1.236%   | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.12 / **cushion 4.02% (tightest)** — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |   $331.010 |    $3,395.10 |        +$61.10 |  +1.833% |   3.38% |  5% | -0.414%   | 10% trail / 10 sh GTC / **HWM $334.59** (auto-advanced from $333.43) / **stop $301.13** / cushion 9.03% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |   $485.000 |    $3,338.72 |         +$4.72 |  +0.141% |   3.33% |  5% | -0.412%   | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.42 / cushion 9.19% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 |   $985.108 |    $3,291.41 |        -$42.59 |  -1.278% (worst) |   3.28% |  5% | -0.486%   | 10% trail / 3 sh GTC / HWM $1022.82 / stop $920.54 / cushion 6.55% — 0.341 sh unprotected |

Total committed: $62,365.22 (62.14% of equity)
Cash retained: $38,000.00 (37.86%)
Open positions: 8 / 10 (NVDA deferred — earnings 5/20 PM; 9th slot reserved)
Leverage: 0.62x (cap 2x)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at open.** MSFT and V HWMs auto-advanced
overnight via IEX marks (MSFT +$4.53 to $432.70 / stop +$4.08 to $389.43; V +$1.16 to $334.59 /
stop +$1.04 to $301.13). **Tightest cushion: AVGO 4.02%** (was 5.21% at Mon close — third
consecutive down-day for AVGO, no thesis-break but on the watchlist). Second-tightest: GOOGL
6.39% (newly tighter; pulled back -1.0% intraday from Mon close mostly on the tech-sell-off
tape). Third: LLY 6.55%. All still inside the strategy's 10%-trail design band.

Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,890 notional (~1.88% of equity). Unchanged.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings **2026-05-20 (Wed) post-close** — T-1 day. Guardrail-#8
  earnings window open since 2026-05-15. Entry blocked. Re-evaluate post-print Thu 5/21
  per strategy caveat (still needs ≥1 -3% red day before completing tranches 2+3; today
  pre-mkt -1% only).
- **DCA tranche 3 of 3** — **DEFERRED PER ROBIN DECISION 2026-05-16: Option B**
  (processed in `memory/inbox.md`). Earliest re-evaluation window: Thu 2026-05-21 in
  01-pre-market (post-NVDA print + 3 trading days of Warsh-era tape). Most likely actual
  execution: Mon 2026-05-25 or Tue 2026-05-26 if tape settles cleanly. T3 sizing per
  `strategy.md` v2 DCA rule: VOO capped at `min($16,667, 0.30 × cash_at_open)`, residual
  rolls forward to T4/T5.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **DEFERRED** to earliest Thu 2026-05-21 evaluation; most-likely-execution
  Mon 2026-05-25 / Tue 2026-05-26.

## Today's trades

**Zero trades placed at 02-market-open.** Plan from this morning's 01-pre-market
(`memory/daily/2026-05-19.md`) was unanimous HOLD across all 8 names; no spec triggers
fired (no thesis-break, no stop breach, no earnings-window resolution, no Robin inbox
reply, no fresh -3% red day on NVDA, no T3 unlock). Bias = inaction unless a spec
trigger fires (lesson 2026-05-16). 6th consecutive routine with no trades.

## Recent Closed Positions (last 5)

(none)
