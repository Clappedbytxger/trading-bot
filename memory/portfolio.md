---
last_updated: 2026-05-20T21:15:00Z
broker: alpaca
account_type: paper
total_value_usd: 100610.49
cash_usd: 38000.00
long_market_value_usd: 62610.49
day_pnl_pct_vs_tue_close: +0.4834
day_spy_pct_vs_tue_close: +1.0263
day_alpha_bp_vs_spy: -54.3
two_day_pnl_pct_vs_mon_close: -0.0753
two_day_spy_pct_vs_mon_close: +0.3529
two_day_alpha_bp_vs_spy: -42.8
ytd_pnl_pct: 0.6105
benchmark_spx_ytd: 8.7983
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 741.26
alpha_vs_spx: -8.1878
ytd_alpha_widening_vs_04preclose_bp: -0.6
livephase_total_pnl_pct: 0.6347
livephase_alpha_vs_spy_pct: -8.244
position_count: 8
leverage_x: 0.62
options_buying_power_usd: 69305.24
options_approved_level: 3
daytrade_count_5d: 0
pattern_day_trader: false
phase: live-phase-legacy (FINAL EOD)
phase_flip_next: 2026-05-21T13:00:00Z (first Learning-Month routine — 01-pre-market)
---

# Portfolio — 05-close-summary 2026-05-20 (EOD, 21:15Z / 17:15 ET, post-close)

> **Phase note**: This is the **final EOD snapshot under Live Phase**. Tomorrow's
> 13:00Z 01-pre-market is the first Learning-Month routine; this portfolio file
> flips to per-sleeve sub-tables (Core / Swing / Daytrade / Crypto / Options) at
> that point. Today's EOD is presented in the legacy single-book "AI-Capex Barbell"
> form, with the Learning-Month sleeve assignment foreshadowed (all 8 names move
> into the **frozen Core sleeve** tomorrow per `strategy.md` v3).

## EOD snapshot — Wed 5/20 (21:15Z / 17:15 ET, market closed since 20:00Z)

| Metric                  |  Mon close (5/18) | Tue close (5/19) | Wed 02-open (13:41Z) | Wed 03-midday (16:39Z) | Wed 04-pre-close (19:39Z) | Wed 05-close (21:15Z) | Δ vs 04-pre-close |
|-------------------------|------------------:|-----------------:|---------------------:|-----------------------:|--------------------------:|----------------------:|------------------:|
| Equity                  |       $100,686.35 |      $100,126.61 |          $100,259.51 |            $100,376.39 |               $100,626.38 |          $100,610.49 |  -$15.89 (-0.016%) |
| SPY                     |           $738.65 |          $733.73 |              $735.54 |                $738.86 |                   $741.31 |              $741.26 |  -$0.05  (-0.007%) |
| VIX                     |             17.82 |            18.06 |                17.79 |                  17.43 |                     17.43 |                17.36 |  -0.07 |
| 10Y yield               |            4.623% |          4.667%  |               4.59%  |                 4.59%  |                    4.572% |               4.572% |  flat |
| Cash %                  |            37.74% |           37.95% |               37.90% |                 37.86% |                    37.76% |               37.77% |  +0.01 pp |
| Position count          |                8  |               8  |                   8  |                     8  |                        8  |                   8  |       0 |
| Daytrade count (5d)     |                —  |               —  |                   —  |                     —  |                        0  |                   0  |       — |

- **Day P&L vs Tue close: +$483.88 (+0.483%) vs SPY +1.026%** → **day-alpha -54.3 bp**
  (vs -53.4 bp at 04-pre-close → -0.9 bp final-15-min slip; broad-tape and Bull's
  book both essentially closed flat from 04-pre-close — micro-slippage on AVGO
  ($418.185 → $417.75) and LLY ($1013.99 → $1015.07) roughly offset, net book
  finished -$15.89 / -1.6 bp into the bell vs SPY -$0.05 / -0.7 bp). Best UPL of
  the day: **MSFT +3.76%**. Worst UPL: **BRK.B -0.71%**.
- **2-day P&L vs Mon close: -0.075% vs SPY +0.353% → 2-day-alpha -42.8 bp**
  (vs -41.3 bp at 04-pre-close → -1.5 bp final tick; well inside daily noise).
- **YTD: Bull +0.610% vs SPY +8.798% → Alpha -8.19%** (vs 04-pre-close alpha
  -8.18% → -0.6 bp marginal widening into the bell; effectively the same).

## Open positions (broker mark @ 21:15Z EOD)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Tue close | Trail Stop                                                                              |
|--------|----------:|----------:|----------:|-------------:|---------------:|---------:|--------:|-------:|-------------------:|-----------------------------------------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |  $680.94  |   $33,592.36 |       +$258.36 |  +0.775% |  33.39% | 50% (Core) | +1.020%            | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.92% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |  $420.20  |    $4,841.44 |       +$175.44 |  +3.760% (best UPL) |   4.81% |  7% | +0.923%            | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.32% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |  $389.00  |    $4,686.39 |        +$20.39 |  +0.437% |   4.66% |  7% | +0.311%            | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 5.46% — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |  $604.60  |    $4,696.22 |        +$30.22 |  +0.648% |   4.67% |  7% | +0.359%            | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 7.15% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |  $417.75  |    $4,705.58 |        +$39.58 |  +0.848% |   4.68% |  7% | +0.884%            | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 4.70% (tightest, -10 bp from 04)** — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |  $330.153 |    $3,386.31 |        +$52.31 |  +1.569% |   3.37% |  5% | +0.073%            | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.63% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |  $480.90  |    $3,310.49 |        -$23.51 |  -0.705% (worst UPL) |   3.29% |  5% | -0.073%            | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.42% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 | $1,015.07 |    $3,391.52 |        +$57.52 |  +1.725% |   3.38% |  5% | -0.180% (recovery continues off $1006.07 intraday low) | 10% trail / 3 sh GTC / HWM $1,037.88 / stop $934.092 / cushion 7.98% — 0.341 sh unprotected |

Total committed: $62,610.49 (62.23% of equity)
Cash retained: $38,000.00 (37.77%)
Open positions: 8 / 10 (NVDA 9th slot reserved — earnings print ~20:20Z+ tonight; detail-read tomorrow 01-pre-market)
Leverage: 0.62× (cap 2×)
Daytrade count (rolling 5d): 0 / 3 (PDT flag: False)
Options BP / level: $69,305.24 / Level 3 ✓ (operational pre-check for tomorrow's Options sleeve activation)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at 21:15Z (re-pulled live from broker post-close).**
No fills today → no order-state changes since 04-pre-close. HWMs unchanged from 03-midday for
all 8 names (LLY's intraday $1037.88 HWM stands; no new intraday HWM advances on the final 21min).
**Tightest cushion AVGO 4.70%** (tightened 10 bp from 04-pre-close's 4.80% on the small
$418.185 → $417.75 final-15-min print). All cushions >3% spec-threshold; **no log-flag, no
WhatsApp escalation**. Second-tightest: GOOGL 5.46% (re-loosened +20 bp on the final tick).

Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,894 notional (~1.88% of equity). Unchanged from 04.

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

**Zero trades at 05-close-summary.** 14th consecutive no-action routine (Mon 5/18
four + Tue 5/19 five + Wed 5/20 five = entire Live-Phase exit week, end-to-end
action-free). All 8 trailing stops intact GTC at the bell. No HWM advances since
03-midday (LLY's $1037.88 holds). AVGO holds "tightest cushion" label at 4.70%
(slight -10 bp tighten from 04-pre-close on a benign final-tick AVGO print).
Macro all-clear at the close (SPY +1.03%, VIX 17.36, 10Y 4.572%). FOMC-minutes
neutral-dovish read holds; no position changes required.

**NVDA print landed ~20:20Z+** (after-hours window). Initial 16:15 ET AH print
read $223.46 — essentially flat on the close ($223.47 regular-hours close). The
print itself and the conference-call guidance (which is the bigger catalyst per
01-pre-market read on consensus $85-87B / whisper $90B Q2 guide) play out
post-this-routine. **Per spec, detailed NVDA-print read happens at tomorrow
13:00Z 01-pre-market — Learning-Month's first routine.**

## Phase-transition state (FINAL Live-Phase 05-close-summary)

- **9-day Live-Phase run summary** (2026-05-12 first tranche → 2026-05-20 close):
  - Equity start (post-T1 5/12 close): ~$99,975.92 → 5/20 close: **$100,610.49**
    → **+$634.57 / +0.635%** total Live-Phase P&L.
  - SPY 5/12 close ~$680.79 → 5/20 close $741.26 → **+8.88%** SPY same-window.
  - Live-Phase alpha vs SPY: **-8.24%** (essentially the entire YTD-alpha deficit
    accumulated in the 9-day Live-Phase paper run; ~70% from being 62%-deployed
    vs 100%-passive-SPY benchmark during a strong-tape +8.88% SPY window).
  - **Zero stop-outs, zero thesis-breaks, zero guardrail violations across 16 fills
    over T1+T2.** All operational issues caught and either fixed or surfaced to
    Robin (3× 01-pre-market cron misses, Alpaca fractional-stop rejections, DCA
    vs guardrail-#5 mechanics, WhatsApp question-shorthand, inbox.md introduction,
    `enable_pr_auto_merge` no-op trap on clean-status PRs).
  - **14 consecutive no-action routines** across the Live-Phase exit week (Mon
    5/18 four + Tue 5/19 five + Wed 5/20 five). Action discipline carried the
    book end-to-end into the Learning-Month boundary with the 8-position Core
    book intact, $38k cash dry, all trails GTC, all guardrails clean.
  - Best UPL: MSFT +3.76% (entry $404.97 → $420.20). Worst UPL: BRK.B -0.71%
    (entry $484.31 → $480.90, contained by 8.42% cushion).
- **Tomorrow at 13:00Z (01-pre-market)**, this file flips to per-sleeve sub-tables:
  - Sleeve 1 — Core (8 names, frozen): $62,610 committed (was $62,626 at 04).
  - Sleeve 2 — Swing: $15k budget, 0 open. **NVDA candidacy evaluated here via
    `swing-earnings-drift` per post-print read.**
  - Sleeve 3 — Daytrade/Scalp: $10k budget, 0 open.
  - Sleeve 4 — Crypto: $5k budget, 0 open. Universe BTC/ETH/SOL/AVAX/LINK.
  - Sleeve 5 — Options: $5k premium budget, 0 open. Level 3 enabled, $69.3k options BP ✓.
  - Cash reserve: ≥$3k untouched out of $38k total cash.
- **Hard-overrides surviving the phase flip**: #9 auto-commit, #10 env-var API
  keys, new ALM-8 paper-endpoint-only broker calls. All others (#1-#8) PAUSED
  through 2026-06-20 inclusive; reactivate automatically 2026-06-21.

## Recent Closed Positions (last 5)

(none — no positions closed in the entire Live-Phase paper run)
