---
last_updated: 2026-05-19T19:35:00Z
broker: alpaca
account_type: paper
total_value_usd: 100217.12
cash_usd: 38000.00
day_pnl_pct_vs_mon_close: -0.4660
day_spy_pct_vs_mon_close: -0.5890
day_alpha_bp_vs_spy: +12.3
ytd_pnl_pct: 0.2171
benchmark_spx_ytd: 7.7779
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 734.30
alpha_vs_spx: -7.5608
ytd_alpha_narrowing_vs_mon_close_bp: +16.9
position_count: 8
leverage_x: 0.62
---

# Portfolio — 04-pre-close 2026-05-19 (T-25min snapshot, 19:35Z / 15:35 ET)

## Pre-close snapshot vs Mon (5/18) close, Tue open, Tue midday

| Metric                  |  Mon close (20:15Z) | Tue open (13:33Z) | Tue midday (16:35Z) | Tue pre-close (19:35Z) |  Δ vs Mon close      |
|-------------------------|--------------------:|------------------:|--------------------:|-----------------------:|---------------------:|
| Equity                  |         $100,686.35 |       $100,365.22 |         $100,276.57 |            $100,217.12 |  -$469.23 (-0.466%)  |
| SPY                     |             $738.65 |           $734.30 |             $734.92 |                $734.30 |  -$4.35   (-0.589%)  |
| Cash %                  |              37.74% |            37.86% |              37.90% |                 37.92% |  +0.18 pp            |
| Position count          |                  8  |                8  |                  8  |                     8  |       0              |

- **Day P&L: -$469.23 (-0.466%) vs SPY -0.589%** → **day alpha +12.3 bp**, a net
  +2.5 bp recovery from midday's +9.8 bp as SPY rolled over (-0.084%) while Bull
  held tighter (-0.059%). Afternoon attribution flipped LLY further green (+0.95%
  midday-to-pre-close on the position UPL line), and BRK.B drifted red (-0.69%
  intraday post-midday) — but the net was Bull-positive vs SPY.
- **YTD: Bull +0.217% vs SPX +7.778% → Alpha -7.561%.** Vs Mon close alpha
  (-7.730%): **+16.9 bp narrowing** — the no-action discipline through a real
  weak-tape session continues to convert into measurable alpha-narrowing
  (+27.0 → +13.8 → +16.9 bp across open / midday / pre-close).

## Open positions (broker mark @ 19:35Z)

| Symbol | Qty       | Avg Entry | Pre-close Mark | Market Value | Unrealized P&L | UPL%     | Alloc % | Target | Day Δ vs Tue open | Trail Stop                                                |
|--------|----------:|----------:|---------------:|-------------:|---------------:|---------:|--------:|-------:|------------------:|-----------------------------------------------------------|
| VOO    | 49.332341 |  $675.703 |       $675.180 |   $33,308.21 |        -$25.79 |  -0.077% |  33.24% | 50% (Core) | -0.145%       | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 8.14% — 0.332 sh unprotected |
| MSFT   | 11.521758 |  $404.973 |       $417.945 |    $4,815.46 |       +$149.46 |  +3.203% (best UPL) |   4.81% |  7% | -2.353% (3rd-worst Δ) | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.82% — 0.522 sh unprotected |
| GOOGL  | 12.047273 |  $387.308 |       $389.120 |    $4,687.83 |        +$21.83 |  +0.468% |   4.68% |  7% | -2.411% (2nd-worst Δ) | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.75 / cushion 5.49% — 0.047 sh unprotected |
| META   |  7.767476 |  $600.710 |       $601.940 |    $4,675.56 |         +$9.56 |  +0.205% |   4.67% |  7% | -1.065%            | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.36 / cushion 6.74% — 0.767 sh unprotected |
| AVGO   | 11.264102 |  $414.236 |       $410.835 |    $4,627.69 |        -$38.31 |  -0.821% (worst UPL) |   4.62% |  7% | -0.884% (4th consecutive red day) | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.12 / **cushion 3.09% (tightest)** — 0.264 sh unprotected |
| V      | 10.256781 |  $325.053 |       $330.065 |    $3,385.40 |        +$51.40 |  +1.542% |   3.38% |  5% | -1.473%            | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.65 / cushion 8.61% — 0.257 sh unprotected |
| BRK.B  |  6.883950 |  $484.315 |       $482.500 |    $3,321.51 |        -$12.49 |  -0.375% |   3.31% |  5% | -1.238%            | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.42 / cushion 8.72% — 0.884 sh unprotected |
| LLY    |  3.341161 |  $997.857 |     $1,016.250 |    $3,395.46 |        +$61.46 |  +1.843% |   3.39% |  5% | **+2.733% (best day Δ)** | 10% trail / 3 sh GTC / HWM $1022.82 / stop $920.54 / cushion 9.42% — 0.341 sh unprotected |

Total committed: $62,217.12 (62.08% of equity)
Cash retained: $38,000.00 (37.92%)
Open positions: 8 / 10 (NVDA deferred — earnings 5/20 PM; 9th slot reserved)
Leverage: 0.62x (cap 2x)

**All 8 trailing stops verified `OrderStatus.NEW` GTC at 04-pre-close.** No HWM
auto-advanced this afternoon (no position made a new 52w-mark in the session).
**Tightest cushion: AVGO 3.09%** (was 3.69% at midday, -60 bp); 4th consecutive
down-day for AVGO, mark $410.835 vs HWM $442.36 → 7.13% off HWM, still inside
10% trail design band. Second-tightest: GOOGL 5.49% (+24 bp loosening vs midday
as it bounced slightly off the midday low). All cushions still inside the
strategy's 10% trail design band — no stop-out risk at current marks into the
final 25 minutes.

Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,880 notional (~1.88% of equity). Unchanged.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings **2026-05-20 (Wed) post-close** — T-0 day tomorrow.
  Guardrail-#8 earnings window open since 2026-05-15. Entry blocked. Re-evaluate
  post-print Thu 5/21 per strategy caveat (still needs ≥1 -3% red day before
  completing tranches 2+3; today's max intraday move was -1.13% on Mon close
  to midday print).
- **DCA tranche 3 of 3** — **DEFERRED PER ROBIN DECISION 2026-05-16: Option B**
  (processed in `memory/inbox.md`). Earliest re-evaluation window: Thu 2026-05-21
  in 01-pre-market (post-NVDA print + 3 trading days of Warsh-era tape).
  Most-likely actual execution: Mon 2026-05-25 or Tue 2026-05-26 if tape settles
  cleanly. T3 sizing per `strategy.md` v2 DCA rule: VOO capped at
  `min($16,667, 0.30 × cash_at_open)`, residual rolls forward to T4/T5.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **DEFERRED** to earliest Thu 2026-05-21 evaluation; most-likely
  execution Mon 2026-05-25 / Tue 2026-05-26.

## Today's trades

**Zero trades through 04-pre-close.** All four 5/19 routines (pre-market,
market-open, midday, pre-close) executed no orders — no spec triggers fired
across the full session. Worst position UPL into final 25min: AVGO -0.82%
(4th red day, tightest cushion 3.09%). Best: MSFT +3.20% (drawing down from
+5.69% pre-mkt open print as AI sleeve led the weak-tape leak). Bias = inaction
unless a spec trigger fires (lesson 2026-05-16). **8th consecutive no-action
routine.** Net day-alpha vs SPY remains +12.3 bp; net YTD-alpha-narrowing vs
Mon close remains +16.9 bp.

## Recent Closed Positions (last 5)

(none)
