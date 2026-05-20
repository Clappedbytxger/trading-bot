---
last_updated: 2026-05-20T13:41:38Z
broker: alpaca
account_type: paper
total_value_usd: 100259.51
cash_usd: 38000.00
day_pnl_pct_vs_tue_close: +0.1327
day_spy_pct_vs_tue_close: +0.2460
day_alpha_bp_vs_spy: -11.3
two_day_pnl_pct_vs_mon_close: -0.4239
two_day_spy_pct_vs_mon_close: -0.4224
two_day_alpha_bp_vs_spy: -0.2
ytd_pnl_pct: 0.2596
benchmark_spx_ytd: 7.9592
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 735.535
alpha_vs_spx: -7.6996
ytd_alpha_widening_vs_tue_close_bp: -13.2
position_count: 8
leverage_x: 0.62
phase: live-phase-legacy
phase_flip_next: 2026-05-21T00:00:00Z (learning-month begins)
---

# Portfolio — 02-market-open 2026-05-20 (post-open, 13:41Z / 09:41 ET)

> **Phase note**: Today (2026-05-20) is the **final Live-Phase day**. Tomorrow's routines
> run under Learning-Month multi-sleeve rules; this portfolio file flips to per-sleeve
> tables at the first 5/21 routine. Until then, all 8 positions are tracked as a single
> Core-equivalent book under Variant C "AI-Capex Barbell".

## Intraday snapshot — Wed 5/20 (open print, 13:41Z)

| Metric                  |  Mon close (5/18) | Tue close (5/19) | Wed 01-pre-mkt (13:05Z) | Wed 02-open (13:41Z) |  Δ vs Tue close      |
|-------------------------|------------------:|-----------------:|------------------------:|---------------------:|---------------------:|
| Equity                  |       $100,686.35 |      $100,126.61 |             $100,383.12 |          $100,259.51 |  +$132.90 (+0.133%)  |
| SPY                     |           $738.65 |          $733.73 |                 $733.73 |              $735.54 |  +$1.81   (+0.246%)  |
| Cash %                  |            37.74% |           37.95% |                  37.85% |               37.90% |  -0.05 pp            |
| Position count          |                8  |               8  |                      8  |                   8  |       0              |

- **Day P&L vs Tue close: +$132.90 (+0.133%) vs SPY +0.246%** → **day-alpha -11.3 bp**.
  AI sleeve gave back overnight bounce at the open: AVGO $417.65 → $414.12 (-0.85% intraday)
  flipped UPL +0.82% → -0.03%; MSFT +2.71% → +2.02%. Defensive sleeve carried again: LLY
  +3.31% UPL on +1.37% intraday (fresh HWM $1030.90). V +1.40% UPL (steady). Core ETF VOO
  +0.04% UPL on +0.25% open.
- **2-day P&L vs Mon close: -0.424% vs SPY -0.422% → 2-day-alpha -0.2 bp** (flat across
  Tue+Wed-open arc — yesterday's +11.0 bp day-alpha is being given back today on the AI
  sleeve give-back; the book is operating exactly inside the strategy's design band).
- **YTD: Bull +0.260% vs SPX +7.959% → Alpha -7.700%.** vs Tue close alpha (-7.567%):
  **-13.2 bp widening** today. Within daily noise; no spec-action required.

## Open positions (broker mark @ 13:41Z)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Tue close | Trail Stop                                                                              |
|--------|----------:|----------:|----------:|-------------:|---------------:|---------:|--------:|-------:|-------------------:|-----------------------------------------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |  $675.98  |   $33,347.43 |        +$13.43 |  +0.040% |  33.26% | 50% (Core) | +0.245%            | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.25% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |  $413.14  |    $4,760.10 |        +$94.10 |  +2.017% |   4.75% |  7% | -0.776%            | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 5.74% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |  $388.97  |    $4,686.03 |        +$20.03 |  +0.429% |   4.67% |  7% | +0.305%            | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.75 / cushion 5.46% — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |  $601.32  |    $4,670.70 |         +$4.70 |  +0.101% |   4.66% |  7% | -0.187%            | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.36 / cushion 6.65% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |  $414.12  |    $4,664.69 |         -$1.31 |  -0.028% |   4.65% |  7% | +1.000% (vs Tue close) / **-0.85% give-back vs pre-mkt** | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.12 / **cushion 3.86% (tightest, re-tightened from 4.68% pre-mkt)** — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |  $329.60  |    $3,380.58 |        +$46.58 |  +1.397% |   3.37% |  5% | -0.094%            | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.65 / cushion 8.48% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |  $480.19  |    $3,305.59 |        -$28.41 |  -0.852% (worst UPL) |   3.30% |  5% | -0.221%            | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.42 / cushion 8.28% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 | $1,030.90 |    $3,444.39 |       +$110.39 |  +3.311% (best UPL) |   3.44% |  5% | **+1.366% (best day Δ)** | 10% trail / 3 sh GTC / **HWM $1,030.90 (new, auto-advanced)** / stop $927.81 (auto-trail from $920.96) / cushion 10.00% — 0.341 sh unprotected |

Total committed: $62,259.51 (62.10% of equity)
Cash retained: $38,000.00 (37.90%)
Open positions: 8 / 10 (NVDA deferred — earnings tonight PM; 9th slot reserved)
Leverage: 0.62× (cap 2×)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at start of session (01-pre-market).**
No fills today → no order-state changes. **LLY HWM auto-advanced** from $1023.29 (pre-mkt) to
$1030.90 (open print) → broker trail-stop auto-advances $920.96 → $927.81 (10% trail).
**Tightest cushion: AVGO 3.86%** (was 4.68% in pre-market, now 3.86% after intraday give-back;
still inside 10% trail design band). Second-tightest: GOOGL 5.46% (+24 bp vs pre-mkt). All
cushions inside the strategy's design band — **no stop hit, no imminent stop-out risk**.

Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,890 notional (~1.89% of equity). Unchanged.

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

**Zero trades at 02-market-open.** 11th consecutive no-action routine (Mon 5/18 four +
Tue 5/19 five + Wed 5/20 two so far). All 8 trailing stops intact GTC. LLY HWM auto-advanced
broker-side (no manual order action). AVGO cushion re-tightened on intraday give-back but
remains inside the 10% trail design band — monitoring through 03-midday and 04-pre-close.

## Recent Closed Positions (last 5)

(none)
