---
last_updated: 2026-05-13T20:30:00Z
broker: alpaca
account_type: paper
total_value_usd: 100772.72
cash_usd: 38000.00
day_pnl_pct: 0.682
ytd_pnl_pct: 0.773
benchmark_spx_ytd: 9.116
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_close: 743.42
alpha_vs_spx: -8.343
position_count: 8
---

# Portfolio — post-04-pre-close 2026-05-13

T-30 min to close. No actions taken this routine — closing-decision spec triggers
unmet (no +5% intraday move, no thesis break, no red-day close). Account equity
**$100,772.72** (+$682.27 / +0.682% on the day vs yesterday's $100,090.45 close).
Total unrealized **+$772.72** across 8 positions, with VOO leading dollar contribution
(+$382) and GOOGL leading by % (+4.02%). V is the only red name (-0.96%, well inside
guardrail #3 band). All 8 trailing stops `status=new`, GTC, 10% — HWMs ratcheted
higher on 6 of 8 names since 03-midday.

Alpha clock: **-8.343%** vs SPX YTD (vs -8.131% at 02-market-open) — modestly widened
~21 bps over the session because SPY +0.71% beat Bull +0.68% on a day where we're
still 62% deployed pre-tranche-3. Mechanical fix is tomorrow's final DCA leg.

## Open Positions

| Symbol | Qty | Avg Entry | Now | Market Value | Unrealized P&L | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|----:|-------------:|---------------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $683.45 | $33,716.24 | +$382.24 (~+1.15%) | 33.46% | 50% (Core ETF) | 10% trail on 49 sh GTC — HWM 683.90, stop 615.51 |
| GOOGL  | 12.047273 | $387.308 | $402.88 |  $4,853.61 | +$187.61 (~+4.02%) |  4.82% |  7%            | 10% trail on 12 sh GTC — HWM 403.70, stop 363.33 |
| META   |  7.767476 | $600.710 | $616.73 |  $4,790.44 | +$124.44 (~+2.67%) |  4.75% |  7%            | 10% trail on 7 sh GTC — HWM 619.89, stop 557.90 |
| AVGO   | 11.264102 | $414.236 | $417.73 |  $4,705.35 |  +$39.35 (~+0.84%) |  4.67% |  7%            | 10% trail on 11 sh GTC — HWM 418.63, stop 376.77 |
| MSFT   | 11.521758 | $404.973 | $405.32 |  $4,670.00 |   +$4.00 (~+0.09%) |  4.63% |  7%            | 10% trail on 11 sh GTC — HWM 406.31, stop 365.68 |
| LLY    |  3.341161 | $997.857 |$1015.37 |  $3,392.51 |  +$58.51 (~+1.76%) |  3.37% |  5%            | 10% trail on 3 sh GTC — HWM 1022.82, stop 920.54 |
| BRK.B  |  6.883950 | $484.315 | $485.54 |  $3,342.40 |   +$8.40 (~+0.25%) |  3.32% |  5%            | 10% trail on 6 sh GTC — HWM 487.14, stop 438.43 |
| V      | 10.256781 | $325.053 | $321.95 |  $3,302.17 |  -$31.83 (~-0.96%) |  3.28% |  5%            | 10% trail on 10 sh GTC — HWM 325.42, stop 292.88 |

Total committed: $62,772.72 (62.29% of equity)
Cash retained: $38,000.00 (37.71%)
Open positions: 8 / 10 (NVDA still deferred; reserve slot held)
Leverage: 0.62x (cap 2x)
Day P&L: +$682.27 (+0.682%) — 7 green / 1 red (V); broad strength led by GOOGL +4.02%, META +2.67%, LLY +1.76%, VOO +1.15%.
Fractional uncovered: ~3.40 sh aggregate ≈ $1,900 notional (~1.89% of equity). Mitigation still deferred to post-tranche-3 consolidation per lessons.md 2026-05-12.

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
