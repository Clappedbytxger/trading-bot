---
last_updated: 2026-05-14T19:40:00Z
broker: alpaca
account_type: paper
total_value_usd: 101257.52
cash_usd: 38000.00
day_pnl_pct: 0.5637
ytd_pnl_pct: 1.2575
benchmark_spx_ytd: 9.871
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 748.56
alpha_vs_spx: -8.614
position_count: 8
---

# Portfolio — post-04-pre-close 2026-05-14

**No trades today.** Tranche 3 of 3 remains blocked pending Robin's decision (see
`02-market-open` section in `memory/daily/2026-05-14.md`). 04-pre-close was a
no-action routine by design — bias toward do-nothing into the close, no thesis-break
exits required, no stop-tightening triggered (best UPL is AVGO +6.44%, well below the
+15% stop-tighten threshold). All 8 trailing stops verified GTC and active.

Equity closed the session at **$101,257.52** (+$567.58 / +0.564% day vs Alpaca
`last_equity` $100,689.94). AI/Quality block did the heavy lifting: AVGO +6.44%
(best, HWM ratcheted 429.76 → 441.35), GOOGL +3.47%, META +2.82%, MSFT turned green
(+1.06%). VOO core +1.84%. Defensive ballast flat (BRK.B +0.02%, V -0.90%, LLY +0.92%).
SPY closed at $748.56 → SPY YTD **+9.87%**. Bull YTD **+1.26%**. Alpha widened from
-8.44% (this morning) to **-8.61%** — still entirely structural, the 37.5% cash sleeve
is the drag.

Trailing-stop HWMs advanced today on 4 of 8 names since morning: VOO 684.80 → 689.10,
AVGO 429.76 → 441.35, MSFT 406.31 → 411.84, META 619.89 → 623.73. GOOGL/LLY/BRK.B/V
HWMs unchanged. No position is within 9 percentage points of its -10% stop.

## Open Positions

| Symbol | Qty | Avg Entry | Now | Market Value | Unrealized P&L | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|----:|-------------:|---------------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $688.110 | $33,946.08 | +$612.08 (~+1.84%) | 33.52% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $440.920 |  $4,966.57 | +$300.57 (~+6.44%) |  4.90% |  7%            | 10% trail on 11 sh GTC, HWM $441.35, stop $397.22 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $400.760 |  $4,828.07 | +$162.07 (~+3.47%) |  4.77% |  7%            | 10% trail on 12 sh GTC, HWM $403.70, stop $363.33 — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $617.680 |  $4,797.81 | +$131.81 (~+2.82%) |  4.74% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $409.270 |  $4,715.51 |  +$49.51 (~+1.06%) |  4.66% |  7%            | 10% trail on 11 sh GTC, HWM $411.84, stop $370.66 — 0.522 sh unprotected |
| LLY    |  3.341161 | $997.857 |$1007.048 |  $3,364.71 |  +$30.71 (~+0.92%) |  3.32% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $484.433 |  $3,334.81 |   +$0.81 (~+0.02%) |  3.29% |  5%            | 10% trail on 6 sh GTC, HWM $487.14, stop $438.43 — 0.884 sh unprotected |
| V      | 10.256781 | $325.053 | $322.125 |  $3,303.97 |  -$30.03 (~-0.90%) |  3.26% |  5%            | 10% trail on 10 sh GTC, HWM $325.42, stop $292.88 — 0.257 sh unprotected |

Total committed: $63,257.53 (62.47% of equity)
Cash retained: $38,000.00 (37.53%)
Open positions: 8 / 10 (NVDA deferred; second slot held in reserve)
Leverage: 0.62x (cap 2x)
Day P&L: +$567.58 (+0.564%) — AI block led; SPY +0.53% day → slight day outperformance.
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,950 notional (~1.93% of equity).
Mitigation still deferred until after tranche 3 consolidates remainders to ≥1 whole share.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings 2026-05-20 (Wed) post-close. Guardrail-#8 earnings
  window opens **tomorrow 2026-05-15** → entry blocked regardless. Hard pass through
  next week's print, then re-evaluate per strategy caveat (needs at least one −3% red
  day before completing tranches 2+3; currently still near 52w-Hi).
- **DCA tranche 3 of 3** — **STILL BLOCKED.** Today's 01-pre-market did not run;
  02-market-open could not execute without that draft; 04-pre-close held the line.
  Awaiting Robin decision: (a) explicit memory-edit go-ahead before tomorrow's
  02-market-open, or (b) defer until tomorrow if 01-pre-market on 2026-05-15 runs
  successfully and re-validates the plan. Note: 2026-05-15 is Powell→Warsh Fed-
  leadership transition day and NVDA earnings-window opens (irrelevant for the
  8-name tranche since NVDA is excluded), and the weekly review fires post-close.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **NOT EXECUTED 2026-05-14** — blocked by missing pre-market draft.
  Pending Robin decision. Post-tranche-3 weights would land near: VOO ≈ 50%,
  AI/Quality ≈ 7% each, defensive ≈ 5% each.

## Recent Closed Positions (last 5)

(none)
