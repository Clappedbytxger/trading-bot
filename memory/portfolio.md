---
last_updated: 2026-05-20T16:39:13Z
broker: alpaca
account_type: paper
total_value_usd: 100376.39
cash_usd: 38000.00
day_pnl_pct_vs_tue_close: +0.2495
day_spy_pct_vs_tue_close: +0.6978
day_alpha_bp_vs_spy: -44.8
two_day_pnl_pct_vs_mon_close: -0.3079
two_day_spy_pct_vs_mon_close: +0.0284
two_day_alpha_bp_vs_spy: -33.6
ytd_pnl_pct: 0.3764
benchmark_spx_ytd: 8.4483
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 738.86
alpha_vs_spx: -8.0719
ytd_alpha_widening_vs_02open_bp: -37.2
position_count: 8
leverage_x: 0.62
phase: live-phase-legacy
phase_flip_next: 2026-05-21T00:00:00Z (learning-month begins)
---

# Portfolio — 03-midday 2026-05-20 (intraday, 16:39Z / 12:39 ET)

> **Phase note**: This is the **last 03-midday under Live Phase**. Tomorrow's routines
> run under Learning-Month multi-sleeve rules; this portfolio file flips to per-sleeve
> tables at the first 5/21 routine. Until then, all 8 positions are tracked as a single
> Core-equivalent book under Variant C "AI-Capex Barbell".

## Intraday snapshot — Wed 5/20 (~3h into session, 16:39Z)

| Metric                  |  Mon close (5/18) | Tue close (5/19) | Wed 02-open (13:41Z) | Wed 03-midday (16:39Z) | Δ vs 02-open      |
|-------------------------|------------------:|-----------------:|---------------------:|-----------------------:|------------------:|
| Equity                  |       $100,686.35 |      $100,126.61 |          $100,259.51 |            $100,376.39 |  +$116.88 (+0.117%) |
| SPY                     |           $738.65 |          $733.73 |              $735.54 |                $738.86 |  +$3.32   (+0.451%) |
| Cash %                  |            37.74% |           37.95% |               37.90% |                 37.86% |  -0.04 pp           |
| Position count          |                8  |               8  |                   8  |                     8  |       0             |

- **Day P&L vs Tue close: +$249.78 (+0.249%) vs SPY +0.698%** → **day-alpha -44.8 bp**
  (widened from -11.3 bp at 02-open). Mid-session tape ran on broad-market breadth Bull
  doesn't own (more Mag-7-ex-AI, small/mid-cap rotation per intraday breadth). AI block
  mixed: MSFT recovered (+2.02% → +3.02%), AVGO recovered (-0.03% → +1.02%, **cushion
  back to 4.86% from 3.86%**), GOOGL slipped (+0.43% → -0.76%, **now tightest cushion
  at 4.32%**). Defensive: V flat (+1.40% → +1.15%), BRK.B flat (-0.85% → -0.99%). LLY
  **round-tripped its HWM**: touched fresh $1037.88 intraday then pulled back to
  $1006.07 (+3.31% → +0.82% UPL, **-2.40 pp intraday give-back**). Broker trail-stop
  auto-advanced $927.81 → $934.092 on the new HWM.
- **2-day P&L vs Mon close: -0.308% vs SPY +0.028% → 2-day-alpha -33.6 bp**. The
  Tue+Wed-open flat 2-day-alpha (-0.2 bp at 02-open) has been re-opened to -33.6 bp by
  the mid-session GOOGL/LLY/BRK.B sequence. Inside daily noise, no spec action.
- **YTD: Bull +0.376% vs SPX +8.448% → Alpha -8.072%.** vs 02-open alpha (-7.700%):
  **-37.2 bp widening** through midday. Within daily noise; mid-session SPY breadth
  rally is not a strategy-spec event.

## Open positions (broker mark @ 16:39Z)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Tue close | Trail Stop                                                                              |
|--------|----------:|----------:|----------:|-------------:|---------------:|---------:|--------:|-------:|-------------------:|-----------------------------------------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |  $679.12  |   $33,502.58 |       +$168.58 |  +0.506% |  33.38% | 50% (Core) | +0.710%            | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.68% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |  $417.22  |    $4,807.11 |       +$141.11 |  +3.024% (best UPL) |   4.79% |  7% | +0.207%            | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.66% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |  $384.35  |    $4,630.37 |        -$35.63 |  -0.764% |   4.61% |  7% | -0.890%            | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 4.32% (tightest)** — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |  $603.52  |    $4,687.83 |        +$21.83 |  +0.468% |   4.67% |  7% | +0.181%            | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 6.99% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |  $418.46  |    $4,713.58 |        +$47.58 |  +1.020% |   4.70% |  7% | +1.057% / **+1.05% intraday recovery** | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 4.86%** (loosened from 3.86% at 02-open) — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |  $328.80  |    $3,372.43 |        +$38.43 |  +1.153% |   3.36% |  5% | -0.337%            | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.26% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |  $479.53  |    $3,301.06 |        -$32.94 |  -0.988% (worst UPL) |   3.29% |  5% | -0.358%            | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.16% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 | $1,006.07 |    $3,361.44 |        +$27.44 |  +0.823% |   3.35% |  5% | -1.103% **(round-trip from intraday HWM)** | 10% trail / 3 sh GTC / **HWM $1,037.88 (new auto-advance, +$6.98 vs 02-open)** / stop $934.092 (auto-trail from $927.81) / cushion 7.15% — 0.341 sh unprotected |

Total committed: $62,376.39 (62.14% of equity)
Cash retained: $38,000.00 (37.86%)
Open positions: 8 / 10 (NVDA 9th slot reserved — earnings tonight PM)
Leverage: 0.62× (cap 2×)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at 16:39Z (re-pulled live from broker).**
No fills today → no order-state changes. **LLY HWM auto-advanced** from $1030.90 (02-open) to
$1037.88 (intraday high) → broker trail-stop auto-advances $927.81 → $934.092 (10% trail).
**Tightest cushion now GOOGL 4.32%** (was 5.46% at 02-open; slipped 114 bp on intraday weakness;
still inside 10% trail design band, still >3% so no log-flag per routine spec). Second-tightest:
AVGO 4.86% (loosened from 3.86% on intraday recovery; cushion-bleed broken on this name).

Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,894 notional (~1.89% of equity). Unchanged.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings **2026-05-20 (Wed) post-close — TONIGHT, T-0 day**.
  Guardrail-#8 earnings window remains open since 2026-05-15. Entry blocked through 2026-05-23.
  **Re-evaluate Thu 2026-05-21 01-pre-market post-print** — that will be the **first
  Learning-Month routine**; NVDA candidacy moves to the **Swing sleeve** framework per
  `strategy.md` v3 (not a Core add).
- **DCA tranche 3 of 3** — **DEFERRED PER ROBIN DECISION 2026-05-16: Option B**. Earliest
  re-evaluation Thu 2026-05-21. **However**, per `strategy.md` v3, **Tranche-3 DCA is
  suspended for Learning Month**. Effective implication: **T3 is now deferred to 6/21+** unless
  Robin overrides via `inbox.md` before tomorrow's open.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **DEFERRED** to 2026-06-21+ (Learning-Month freeze).

## Today's trades

**Zero trades at 03-midday.** 12th consecutive no-action routine (Mon 5/18 four + Tue
5/19 five + Wed 5/20 three so far). All 8 trailing stops intact GTC. LLY HWM
auto-advanced broker-side (no manual order action). GOOGL cushion tightened to 4.32%
(tightest in book) on intraday weakness but remains inside 10% trail design band and
>3% spec-threshold — monitoring through 04-pre-close.

## Recent Closed Positions (last 5)

(none)
