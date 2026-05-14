---
last_updated: 2026-05-14T17:35:00Z
broker: alpaca
account_type: paper
total_value_usd: 101072.85
cash_usd: 38000.00
day_pnl_pct: 0.3802
ytd_pnl_pct: 1.0728
benchmark_spx_ytd: 9.738
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 747.66
alpha_vs_spx: -8.665
position_count: 8
---

# Portfolio — post-03-midday 2026-05-14

**No trades executed mid-day.** All 8 positions are well inside the band: worst is V
at **-1.03%** (far from the -7% investigation trigger), best is AVGO at **+4.47%**
(far from the +15% stop-tighten trigger). No thesis-break signals. The DCA tranche 3
remains blocked pending Robin's decision (carried over from 02-market-open).

Equity now **$101,072.85** (+$382.91 / +0.38% day on Alpaca `last_equity` $100,689.94).
The AI/Quality block keeps leading (AVGO +4.47%, META +3.13%, GOOGL +3.01%); MSFT
turned green (+0.67% from -0.23% this morning). Defensive ballast still mixed — LLY
modestly green (+0.72%), BRK.B flipped slightly red (-0.54%), V worsened to -1.03%.
SPY at **$747.66** is +0.41% since 02-market-open and +1.25% on the day → YTD
**+9.738%**, vs Bull YTD **+1.073%**, so alpha widens further to **-8.665%** (from
-8.438% at 02-market-open). Still entirely explained by 37.6% cash drag while broad
tape rallies. Structural fix = tranche 3, which is the blocked item.

All 8 trailing stops still active GTC, 10%, `status=new`. HWMs ratcheted up on 4 of
8 names since this morning: VOO 684.80 → 689.10, MSFT 406.31 → 411.84, META 619.89
→ 623.73, AVGO 429.76 → 439.75. GOOGL/LLY/BRK.B/V HWMs unchanged. No stop within 9
percentage points of the current price; the closest (V, current $321.70 vs stop
$292.88) is still 9.0% above stop.

## Open Positions

| Symbol | Qty | Avg Entry | Now | Market Value | Unrealized P&L | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|----:|-------------:|---------------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $687.360 | $33,909.08 | +$575.08 (~+1.73%) | 33.55% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $432.735 |  $4,874.37 | +$208.37 (~+4.47%) |  4.82% |  7%            | 10% trail on 11 sh GTC, HWM $439.75, stop $395.78 — 0.264 sh unprotected |
| META   |  7.767476 | $600.710 | $619.500 |  $4,811.95 | +$145.95 (~+3.13%) |  4.76% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $398.950 |  $4,806.26 | +$140.26 (~+3.01%) |  4.76% |  7%            | 10% trail on 12 sh GTC, HWM $403.70, stop $363.33 — 0.047 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $407.701 |  $4,697.43 |  +$31.43 (~+0.67%) |  4.65% |  7%            | 10% trail on 11 sh GTC, HWM $411.84, stop $370.66 — 0.522 sh unprotected |
| LLY    |  3.341161 | $997.857 |$1005.060 |  $3,358.07 |  +$24.07 (~+0.72%) |  3.32% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $481.720 |  $3,316.14 |  -$17.86 (~-0.54%) |  3.28% |  5%            | 10% trail on 6 sh GTC, HWM $487.14, stop $438.43 — 0.884 sh unprotected |
| V      | 10.256781 | $325.053 | $321.695 |  $3,299.56 |  -$34.44 (~-1.03%) |  3.26% |  5%            | 10% trail on 10 sh GTC, HWM $325.42, stop $292.88 — 0.257 sh unprotected |

Total committed: $63,072.86 (62.40% of equity)
Cash retained: $38,000.00 (37.60%)
Open positions: 8 / 10 (NVDA deferred; second slot held in reserve)
Leverage: 0.62x (cap 2x)
Day P&L: +$382.91 (+0.38%) — AI block driving; SPY +1.25% day.
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,930 notional (~1.91% of equity).
Mitigation still deferred — tranche 3 was supposed to consolidate today, but is
blocked pending Robin's decision.

## Pending (not yet opened)

- **NVDA** — target 7%. Still deferred. Earnings 2026-05-20 (Wed) post-close.
  Guardrail-#8 earnings-window opens **tomorrow 2026-05-15**, which would block
  entry anyway. Hard pass through next week's print.
- **DCA tranche 3 of 3** — **STILL BLOCKED.** Planned for today (5/14, $30,999.62
  across the same 8 names), but 01-pre-market did not produce a draft plan. Per
  routine spec, neither 02-market-open nor 03-midday executes without an approved
  same-day draft. Awaiting Robin decision: (a) manual go-ahead via reply, or
  (b) defer to tomorrow 5/15 if 01-pre-market runs successfully.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **NOT EXECUTED 2026-05-14** — blocked by missing pre-market draft.
  Pending Robin decision. Post-tranche-3 weights would land near: VOO ≈ 50%,
  AI/Quality ≈ 7% each, defensive ≈ 5% each.

## Recent Closed Positions (last 5)

(none)
