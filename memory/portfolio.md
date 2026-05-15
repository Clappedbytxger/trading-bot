---
last_updated: 2026-05-14T20:20:00Z
broker: alpaca
account_type: paper
total_value_usd: 101196.48
cash_usd: 38000.00
day_pnl_pct: 0.5031
ytd_pnl_pct: 1.1965
benchmark_spx_ytd: 9.813
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 748.17
alpha_vs_spx: -8.617
position_count: 8
---

# Portfolio — post-close 2026-05-14

**No trades today.** DCA tranche 3 of 3 remains **blocked** pending Robin's decision
(see `04-pre-close` open question in `memory/daily/2026-05-14.md`). 05-close-summary
is a no-action routine by design; close-out reconciliation only.

Equity printed the session out at **$101,196.48** vs Alpaca `last_equity` $100,689.94
→ **Day P&L +$506.54 / +0.503%**. The 04-pre-close intraday peak ($101,257.52) gave
back ~$61 into the final 20 minutes (AVGO and GOOGL ticked down a few cents off their
HWMs, LLY rotated harder than expected at the close). AI/Quality block did the heavy
lifting on the day: **AVGO +5.61% day** (best), VOO core +0.73%, V +0.69%, MSFT
+0.69%, META +0.07%. Defensive ballast wobbled into the close: **LLY -0.89% day**
(worst), GOOGL -0.48% (gave back morning gains), BRK.B -0.15%. Note: today's worst
*day-mover* is LLY, NOT V — V's UPL is still the most negative position cumulatively
(-0.78%) but its day move was +0.69%. The 04-pre-close report that flagged "Worst: V
-0.90%" was UPL-based; today's close summary uses *day move* per spec.

SPY closed **$748.17** → SPY YTD **+9.81%** (vs 2026-01-02 ref $681.31). Bull YTD
**+1.20%** → Alpha vs SPX **-8.62%** (vs -8.44% at AM / -8.61% at 04-pre-close —
~18 bp widening across the day, entirely cash-drag artifact on a +0.5% SPY day with
37.5% of book in cash). No structural change.

All 8 trailing stops verified GTC and active 8/8 status=new (no fills, no
modifications). HWMs effectively unchanged vs 04-pre-close levels (peaks held but
positions ticked off slightly into close — VOO 687.37 < HWM 689.10; AVGO 440.25 < HWM
441.35; MSFT 407.90 < HWM 411.84; META 617.06 < HWM 623.73). No position is within
9 percentage points of its -10% stop. No stop-tightening trigger fired (strategy
threshold is +15% UPL per name; best UPL AVGO +6.28%, well below).

## Open Positions

| Symbol | Qty | Avg Entry | Now | Market Value | Unrealized P&L | Day Δ | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|----:|-------------:|---------------:|------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $687.370 | $33,909.57 | +$575.57 (+1.73%) | +0.73% | 33.51% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $440.250 |  $4,959.02 | +$293.02 (+6.28%) | **+5.61%** (best) |  4.90% |  7%            | 10% trail on 11 sh GTC, HWM $441.35, stop $397.22 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $400.610 |  $4,826.26 | +$160.26 (+3.44%) | -0.48% |  4.77% |  7%            | 10% trail on 12 sh GTC, HWM $403.70, stop $363.33 — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $617.060 |  $4,793.00 | +$127.00 (+2.72%) | +0.07% |  4.74% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $407.900 |  $4,699.73 |  +$33.73 (+0.72%) | +0.69% |  4.64% |  7%            | 10% trail on 11 sh GTC, HWM $411.84, stop $370.66 — 0.522 sh unprotected |
| LLY    |  3.341161 | $997.857 |$1006.700 |  $3,363.55 |  +$29.55 (+0.89%) | **-0.89%** (worst) |  3.32% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $484.800 |  $3,337.34 |   +$3.34 (+0.10%) | -0.15% |  3.30% |  5%            | 10% trail on 6 sh GTC, HWM $487.14, stop $438.43 — 0.884 sh unprotected |
| V      | 10.256781 | $325.053 | $322.520 |  $3,308.02 |  -$25.98 (-0.78%) | +0.69% |  3.27% |  5%            | 10% trail on 10 sh GTC, HWM $325.42, stop $292.88 — 0.257 sh unprotected |

Total committed: $63,196.49 (62.45% of equity)
Cash retained: $38,000.00 (37.55%)
Open positions: 8 / 10 (NVDA deferred; second slot held in reserve)
Leverage: 0.62x (cap 2x)
Day P&L: +$506.54 (+0.503%) — Bull tracked SPY day (~+0.52%) within 2 bp on the
committed sleeve; the rest of the residual gap is the 37.5% cash sitting out a +0.5%
broad-tape session.
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,945 notional (~1.92% of equity).
Mitigation still deferred until after tranche 3 consolidates remainders to ≥1 whole share.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings 2026-05-20 (Wed) post-close. Guardrail-#8 earnings
  window **opens tomorrow 2026-05-15** → entry blocked regardless. Hard pass through
  next week's print, then re-evaluate per strategy caveat (needs at least one -3% red
  day before completing tranches 2+3; currently still near 52w-Hi).
- **DCA tranche 3 of 3** — **STILL BLOCKED.** Today: 01-pre-market did not run;
  02-market-open held by spec; 04-pre-close held the line; no-trade close.
  Awaiting Robin decision: (A) explicit memory-edit go-ahead before tomorrow's
  02-market-open, or (B) defer until tomorrow if 01-pre-market on 2026-05-15 runs
  successfully and re-validates the plan, or (C) defer a full week into the
  post-NVDA / post-Fed-transition window. 2026-05-15 is Powell→Warsh Fed transition
  day, NVDA earnings-window opens (irrelevant for the 8-name tranche since NVDA is
  excluded), and `06-weekly-review` fires post-close.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **NOT EXECUTED 2026-05-14** — blocked by missing pre-market draft.
  Pending Robin decision. Post-tranche-3 weights would land near: VOO ≈ 50%,
  AI/Quality ≈ 7% each, defensive ≈ 5% each.

## Recent Closed Positions (last 5)

(none)
