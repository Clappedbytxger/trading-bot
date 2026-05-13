---
last_updated: 2026-05-13T13:42:00Z
broker: alpaca
account_type: paper
total_value_usd: 100056.93
cash_usd: 38000.00
day_pnl_pct: -0.0335
ytd_pnl_pct: 0.0569
benchmark_spx_ytd: 8.189
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_close: 737.10
alpha_vs_spx: -8.132
position_count: 8
---

# Portfolio — post-02-market-open 2026-05-13

DCA tranche 2 of 3 executed cleanly at the open — all 8 BUYs filled in <5s, same
nominal sizes as tranche 1 ($30,999.62 total). Account equity **$100,056.93** (modest
-$33.52 / -0.034% intraday on a SPY -0.10% day at the open). Position sizes roughly
doubled across all 8 names; VOO weight now **33.4%** (still inside ETF-Core band of
45–55%, well under the 60% guardrail cap). AI/Quality block ~18.6% (4 names × ~4.65%);
defensive ballast ~10.0% (3 names × ~3.33%). Cash now $38k (down from $69k pre-trade)
— tranche 3 (2026-05-14) will commit another ~$31k, landing us near strategy weights.

All 8 trailing stops cancelled and re-issued at the new floor(qty) per lesson 2026-05-12
on Alpaca fractional-stop limitation. **Alpha clock starts now:** -8.13% vs SPX YTD
(improved from -8.26% yesterday's close; the ~13 bps tightening = first day of real
tracking).

## Open Positions

| Symbol | Qty | Avg Entry | Now | Market Value | Unrealized P&L | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|----:|-------------:|---------------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $677.70 | $33,432.53 | +$98.53 (~+0.30%) | 33.41% | 50% (Core ETF) | 10% trail on 49 sh GTC — 0.332 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $402.17 |  $4,633.71 | -$32.29 (~-0.69%) |  4.63% |  7%            | 10% trail on 11 sh GTC — 0.522 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $388.22 |  $4,677.02 | +$11.02 (~+0.24%) |  4.67% |  7%            | 10% trail on 12 sh GTC — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $601.49 |  $4,672.06 | +$6.06 (~+0.13%)  |  4.67% |  7%            | 10% trail on 7 sh GTC — 0.767 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $411.15 |  $4,631.24 | -$34.76 (~-0.75%) |  4.63% |  7%            | 10% trail on 11 sh GTC — 0.264 sh unprotected |
| V      | 10.256781 | $325.053 | $324.22 |  $3,325.45 | -$8.55 (~-0.26%)  |  3.32% |  5%            | 10% trail on 10 sh GTC — 0.257 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $484.28 |  $3,333.74 | -$0.26 (~-0.01%)  |  3.33% |  5%            | 10% trail on 6 sh GTC — 0.884 sh unprotected |
| LLY    |  3.341161 | $997.857 | $1003.00|  $3,351.18 | +$17.18 (~+0.52%) |  3.35% |  5%            | 10% trail on 3 sh GTC — 0.341 sh unprotected |

Total committed: $62,056.93 (62.02% of equity)
Cash retained: $38,000.00 (37.98%)
Open positions: 8 / 10 (NVDA deferred; second slot held in reserve)
Leverage: 0.62x (cap 2x)
Day P&L: -$33.52 (-0.034%) — modest red open, drag from MSFT/AVGO; GOOGL/META/LLY/VOO/BRK.B green.
Fractional uncovered: ~3.40 sh aggregate ≈ $1,876 notional (~1.87% of equity). Mitigation deferred to 03-midday or post-tranche-3 consolidation.

## Pending (not yet opened)

- **NVDA** — target 7%. Still deferred. Today (5/13) at 98.7% of 52w-Hi; earnings
  2026-05-20 (Wed) post-close. Earnings-window guardrail #8 opens 2026-05-15 (Fri).
  Strategy caveat: wait for at least one -3% red day before initiating, and likely
  re-evaluate post-print. **No tranche-3 action for NVDA either.**

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional). ✅
- Tranche 3 of 3: planned **2026-05-14** (same 8 names, same nominal sizes). Post-tranche-3
  weights will approach: VOO ≈ 50%, AI/Quality ≈ 7% each, defensive ≈ 5% each.

## Recent Closed Positions (last 5)

(none)
