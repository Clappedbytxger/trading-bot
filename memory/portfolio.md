---
last_updated: 2026-05-20T19:39:15Z
broker: alpaca
account_type: paper
total_value_usd: 100626.38
cash_usd: 38000.00
day_pnl_pct_vs_tue_close: +0.4992
day_spy_pct_vs_tue_close: +1.0331
day_alpha_bp_vs_spy: -53.4
two_day_pnl_pct_vs_mon_close: -0.0596
two_day_spy_pct_vs_mon_close: +0.3529
two_day_alpha_bp_vs_spy: -41.3
ytd_pnl_pct: 0.6253
benchmark_spx_ytd: 8.8068
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 741.31
alpha_vs_spx: -8.1815
ytd_alpha_widening_vs_03midday_bp: -11.0
position_count: 8
leverage_x: 0.62
phase: live-phase-legacy
phase_flip_next: 2026-05-21T13:00:00Z (first Learning-Month routine — 01-pre-market)
---

# Portfolio — 04-pre-close 2026-05-20 (intraday, 19:39Z / 15:39 ET, ~21min to close)

> **Phase note**: This is the **last 04-pre-close under Live Phase**. Tomorrow's
> routines (starting 01-pre-market 13:00Z) run under Learning-Month multi-sleeve rules;
> this portfolio file flips to per-sleeve sub-tables (Core / Swing / Daytrade / Crypto
> / Options) at the first 5/21 routine. Until then, all 8 positions are tracked as a
> single Core-equivalent book under Variant C "AI-Capex Barbell".

## Intraday snapshot — Wed 5/20 (~6h into session, 19:39Z, ~21min to close, post-FOMC-minutes)

| Metric                  |  Mon close (5/18) | Tue close (5/19) | Wed 02-open (13:41Z) | Wed 03-midday (16:39Z) | Wed 04-pre-close (19:39Z) | Δ vs 03-midday  |
|-------------------------|------------------:|-----------------:|---------------------:|-----------------------:|--------------------------:|----------------:|
| Equity                  |       $100,686.35 |      $100,126.61 |          $100,259.51 |            $100,376.39 |               $100,626.38 |  +$249.99 (+0.249%) |
| SPY                     |           $738.65 |          $733.73 |              $735.54 |                $738.86 |                   $741.31 |  +$2.45  (+0.332%) |
| Cash %                  |            37.74% |           37.95% |               37.90% |                 37.86% |                    37.76% |  -0.10 pp |
| Position count          |                8  |               8  |                   8  |                     8  |                        8  |       0 |
| Daytrade count (5d)     |                —  |               —  |                   —  |                     —  |                        0  |       — |

- **Day P&L vs Tue close: +$499.77 (+0.499%) vs SPY +1.033%** → **day-alpha -53.4 bp**
  (widened from -44.8 bp at 03-midday; post-FOMC-minutes broad-market melt-up
  outpaced Bull's concentrated AI+defensive book by another -8.6 bp — Bull's book
  still gained +$249.99 from 03-midday in absolute terms; broad-tape just won).
  MSFT extended (+3.02% → +3.84%, **best UPL in book**). GOOGL **recovered** the
  cushion bleed (-0.76% → +0.22% UPL, cushion 4.32% → 5.26%). LLY recovered toward
  HWM (+0.82% → +1.62%). AVGO held (+1.02% → +0.95%) and **inherits the "tightest
  cushion" label at 4.80%** from GOOGL by 6 bp.
- **2-day P&L vs Mon close: -0.060% vs SPY +0.353% → 2-day-alpha -41.3 bp**
  (vs -33.6 bp at 03-midday → -7.7 bp continued widening; well inside daily noise).
- **YTD: Bull +0.625% vs SPX +8.807% → Alpha -8.182%.** vs 03-midday alpha -8.072%:
  **-11.0 bp continued widening**. Live-Phase exit-day pinned by broad-tape outperformance.

## Open positions (broker mark @ 19:39Z)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Tue close | Trail Stop                                                                              |
|--------|----------:|----------:|----------:|-------------:|---------------:|---------:|--------:|-------:|-------------------:|-----------------------------------------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |  $681.43  |   $33,616.54 |       +$282.54 |  +0.848% |  33.41% | 50% (Core) | +1.050%            | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.99% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |  $420.54  |    $4,845.36 |       +$179.36 |  +3.844% (best UPL) |   4.81% |  7% | +1.005%            | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.40% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |  $388.17  |    $4,676.39 |        +$10.39 |  +0.223% |   4.65% |  7% | +0.097% **(recovered from tightest)** | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 5.26% — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |  $603.53  |    $4,687.91 |        +$21.91 |  +0.469% |   4.66% |  7% | +0.182%            | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 6.99% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |  $418.185 |    $4,710.47 |        +$44.47 |  +0.953% |   4.68% |  7% | +0.989%            | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 4.80% (now tightest)** — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |  $330.72  |    $3,392.10 |        +$58.12 |  +1.743% |   3.37% |  5% | +0.245%            | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.79% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |  $480.78  |    $3,309.67 |        -$24.33 |  -0.730% (worst UPL) |   3.29% |  5% | -0.098%            | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.39% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 | $1,013.995|    $3,387.92 |        +$53.92 |  +1.617% |   3.37% |  5% | -0.323% **(recovery off intraday round-trip low $1006.07)** | 10% trail / 3 sh GTC / HWM $1,037.88 / stop $934.092 / cushion 7.88% — 0.341 sh unprotected |

Total committed: $62,626.38 (62.24% of equity)
Cash retained: $38,000.00 (37.76%)
Open positions: 8 / 10 (NVDA 9th slot reserved — earnings tonight PM ~20:00Z+)
Leverage: 0.62× (cap 2×)
Daytrade count (rolling 5d): 0 / 3 (PDT flag: False)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at 19:39Z (re-pulled live from broker).**
No fills today → no order-state changes. HWMs unchanged from 03-midday for all 8 names
(LLY's auto-advance $1037.88 from 03-midday window stands; no new intraday HWM since).
**Tightest cushion now AVGO 4.80%** (was 2nd at 03-midday; GOOGL recovered +94 bp to
5.26% and is no longer tightest). Both >3% spec-threshold; **no log-flag, no WhatsApp
escalation**. Second-tightest: GOOGL 5.26%.

Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,895 notional (~1.88% of equity). Unchanged.

## Pending (not yet opened)

- **NVDA** — target 7% (Core view) / Swing entry via `swing-earnings-drift` (Learning-Month view).
  **Earnings 2026-05-20 (Wed) post-close — TONIGHT ~20:00Z+, T-0 day**.
  Guardrail-#8 earnings window remains open since 2026-05-15. Entry blocked through 2026-05-23
  in Live-Phase terms — but Live-Phase ends 5/21. **Per `strategy.md` v3, NVDA candidacy
  moves to the Swing sleeve framework starting tomorrow's 01-pre-market** (not a Core add;
  sized ~$1.5-2k via `swing-earnings-drift` if strong-beat + positive-guide + gap holds
  opening 30-min range).
- **DCA tranche 3 of 3** — **DEFERRED PER ROBIN DECISION 2026-05-16: Option B**.
  Per `strategy.md` v3, **Tranche-3 DCA is suspended for Learning Month**. Effective
  implication: **T3 is now deferred to 6/21+** unless Robin overrides via `inbox.md`.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **DEFERRED** to 2026-06-21+ (Learning-Month freeze).

## Today's trades

**Zero trades at 04-pre-close.** 13th consecutive no-action routine. All 8 trailing
stops intact GTC. No HWM advances since 03-midday. AVGO inherits "tightest cushion"
label at 4.80% (GOOGL recovered +94 bp to 5.26%). Macro risk-off triggers clean
(SPY +1.03%, VIX 17.43, 10Y 4.572%). FOMC minutes (18:00Z drop) read as
neutral-to-mildly-dovish; no position changes required. **NVDA print tonight is
post-close, post-04-pre-close, post-05-close-summary first read** — partial coverage
expected in tonight's WhatsApp.

## Phase-transition state (final Live-Phase 04-pre-close)

- **8-day Live-Phase run summary** (2026-05-12 first tranche → 2026-05-20 pre-close):
  - Equity start (post-T1 5/12 close): ~$99,975.92 → 5/20 04-pre-close: $100,626.38
    → **+$650.46 / +0.651%** total Live-Phase P&L.
  - SPY 5/12 close ~$680.79 → 5/20 19:39Z $741.31 → **+8.89%** SPY same-window.
  - Live-Phase alpha vs SPY: **-8.24%** (essentially the entire YTD-alpha deficit
    accumulated in the 8-day Live-Phase paper run; ~70% of that came from being
    62%-deployed vs 100%-passive-SPY benchmark during a +8.89% SPY tape).
  - **Zero stop-outs, zero thesis-breaks, zero guardrail violations across 16 fills
    over T1+T2.** All operational issues caught and either fixed or surfaced to
    Robin (3× 01-pre-market cron misses, Alpaca fractional-stop rejections, DCA
    vs guardrail-#5 mechanics, WhatsApp question-shorthand, inbox.md
    introduction).
  - **13 consecutive no-action routines** across the Live-Phase exit week (Mon
    5/18 four + Tue 5/19 five + Wed 5/20 four). Action discipline carried the
    book cleanly into the Learning-Month boundary.
- **Tomorrow at 13:00Z (01-pre-market)**, this file structure flips to per-sleeve
  sub-tables:
  - Sleeve 1 — Core (8 names + reserved 9th NVDA-via-Swing slot moved out): $62,626 committed.
  - Sleeve 2 — Swing: $15k budget, 0 open.
  - Sleeve 3 — Daytrade/Scalp: $10k budget, 0 open.
  - Sleeve 4 — Crypto: $5k budget, 0 open.
  - Sleeve 5 — Options: $5k premium budget, 0 open.
  - Cash reserve: ≥$3k untouched.

## Recent Closed Positions (last 5)

(none)
