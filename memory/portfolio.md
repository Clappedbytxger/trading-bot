---
last_updated: 2026-05-19T16:35:00Z
broker: alpaca
account_type: paper
total_value_usd: 100276.57
cash_usd: 38000.00
day_pnl_pct_vs_mon_close: -0.4073
day_spy_pct_vs_mon_close: -0.5050
day_alpha_bp_vs_spy: +9.8
ytd_pnl_pct: 0.2766
benchmark_spx_ytd: 7.8688
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 734.92
alpha_vs_spx: -7.5922
ytd_alpha_narrowing_vs_mon_close_bp: +13.8
position_count: 8
leverage_x: 0.62
---

# Portfolio — 03-midday 2026-05-19 (midday snapshot, 16:35Z / 12:35 ET)

## Midday snapshot vs Mon (5/18) close and vs Tue open

| Metric                  |  Mon close (20:15Z) | Tue open (13:33Z) | Tue midday (16:35Z) |  Δ vs Mon close      |
|-------------------------|--------------------:|------------------:|--------------------:|---------------------:|
| Equity                  |         $100,686.35 |       $100,365.22 |         $100,276.57 |  -$409.78 (-0.407%)  |
| SPY                     |             $738.65 |           $734.30 |             $734.92 |  -$3.73   (-0.505%)  |
| Cash %                  |              37.74% |            37.86% |              37.90% |  +0.16 pp            |
| Position count          |                  8  |                8  |                  8  |       0              |

- **Day P&L: -$409.78 (-0.407%) vs SPY -0.505%** → **day alpha +9.8 bp** (narrowed from
  +27.0 bp at open as SPY ticked back up +0.084% while the book leaked -0.09%, mostly
  on MSFT -2.15% and GOOGL -1.20% mid-session). Defensive sleeve doing real work today:
  LLY +2.92% intraday recovery (was -1.28% UPL at open, now +1.60% UPL), BRK.B +0.17%,
  V -0.12%. AI/Quality sleeve is the day's drag.
- **YTD: Bull +0.277% vs SPX +7.869% → Alpha -7.592%.** Vs Mon close alpha (-7.730%):
  **+13.8 bp narrowing** still (down from +31.7 bp at open). Still net positive
  weak-tape behaviour, just lighter than the open print.

## Open positions (broker mark @ 16:35Z)

| Symbol | Qty       | Avg Entry | Midday Mark | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Mon close | Trail Stop                                                |
|--------|----------:|----------:|------------:|-------------:|---------------:|---------:|--------:|-------:|-------------------:|-----------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |    $675.670 |   $33,332.38 |         -$1.62 |  -0.005% |  33.24% | 50% (Core) | -0.440%        | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.21% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |    $417.690 |    $4,812.52 |       +$146.52 |  +3.140% |   4.80% |  7% | -2.150% (worst day Δ) | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.77% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |    $388.120 |    $4,675.79 |         +$9.79 |  +0.210% |   4.66% |  7% | -1.201%            | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.75 / cushion 5.25% — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |    $602.105 |    $4,676.84 |        +$10.84 |  +0.232% |   4.66% |  7% | -0.775%            | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.36 / cushion 6.77% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |    $413.360 |    $4,656.13 |         -$9.87 |  -0.212% |   4.64% |  7% | -1.586% (3rd red day) | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.12 / **cushion 3.69% (tightest)** — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |    $330.620 |    $3,391.10 |        +$57.10 |  +1.713% |   3.38% |  5% | -0.118%            | 10% trail / 10 sh GTC / **HWM $335.17** (auto-advanced from $334.59) / **stop $301.65** / cushion 8.76% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |    $485.820 |    $3,344.36 |        +$10.36 |  +0.311% |   3.34% |  5% | +0.169%            | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.42 / cushion 9.35% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 |   $1013.855 |    $3,387.45 |        +$53.45 |  +1.603% (best Δ today) |   3.38% |  5% | +2.919% (best day Δ) | 10% trail / 3 sh GTC / HWM $1022.82 / stop $920.54 / cushion 9.21% — 0.341 sh unprotected |

Total committed: $62,276.57 (62.10% of equity)
Cash retained: $38,000.00 (37.90%)
Open positions: 8 / 10 (NVDA deferred — earnings 5/20 PM; 9th slot reserved)
Leverage: 0.62x (cap 2x)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at 03-midday.** V's HWM auto-advanced
intraday from $334.59 → $335.17 (stop $301.13 → $301.65). All other HWMs unchanged (no
position made a new 52w-mark intraday). **Tightest cushion: AVGO 3.69%** (was 4.02% at
open, -33 bp; third consecutive down-day for AVGO, mark $413.36 vs HWM $442.36 → 6.55%
off HWM, still well inside 10% trail). Second-tightest: GOOGL 5.25% (was 6.39%, -114 bp).
Joint third: MSFT and META at 6.77% (MSFT had the biggest tightening, -200 bp from open
on its -2.15% intraday drop). All cushions still inside the strategy's 10% trail design
band — no stop-out risk at current marks.

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

**Zero trades through 03-midday.** 02-market-open executed no orders per pre-market
plan; 03-midday Step-3 spec checks also clean (no UPL ≤ -7%, no UPL ≥ +15%, no
thesis-break, no -3% NVDA red day, no inbox reply, no T3 unlock). Worst UPL: AVGO
-0.21%. Best UPL: MSFT +3.14% (down from +5.40% at open but still nowhere near the
+15% trail-tighten threshold). Bias = inaction unless a spec trigger fires
(lesson 2026-05-16). **7th consecutive no-action routine.**

## Recent Closed Positions (last 5)

(none)
