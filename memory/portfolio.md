---
last_updated: 2026-05-18T13:37:00Z
broker: alpaca
account_type: paper
total_value_usd: 100562.42
cash_usd: 38000.00
day_pnl_pct_vs_fri_yf_close: -0.1756
day_pnl_pct_vs_fri_broker_close: -0.0298
week_pnl_pct: 0.5624
week_spy_pct: -0.0636
ytd_pnl_pct: 0.5624
benchmark_spx_ytd: 8.4235
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 738.70
alpha_vs_spx: -7.8611
ytd_alpha_widening_today_open_bp: -10.7
position_count: 8
leverage_x: 0.62
---

# Portfolio — 02-market-open 2026-05-18 (post-open snapshot, 13:37Z)

## Today's open delta

| Metric                          | Fri close (yf-basis) | Mon pre-open (13:00Z) | Mon post-open (13:37Z) | Δ vs Fri close |
|---------------------------------|---------------------:|----------------------:|-----------------------:|---------------:|
| Equity                          |        $100,739.35  |        $100,522.33   |        $100,562.42    |    -$176.93 (-0.176%)   |
| SPY                             |             $739.17 |               $738.70 (intraday) |               $738.70 |    -$0.47 (-0.064%) |
| Cash %                          |             37.72%  |              37.80%  |              37.79%   |    +0.07 pp       |
| Position count                  |                  8  |                   8  |                   8   |     0             |
| Tranches filled                 |                 16  |                  16  |                  16   |     0             |

- Day P&L (yf-basis): **-0.176%** vs SPY day **-0.064%** → Bull lags SPY by **~11 bp** on the AM open as AI-sleeve gives back part of Fri's late-session rally. Defensives flat (V +0.03%, BRK.B -0.29%), Core ETF VOO tracking SPY within feed noise.
- Alpha YTD: **-7.861%** vs SPX **+8.424%** (Bull YTD +0.562%) → **-10.7 bp widening** from Fri close -7.754%. Routine noise, not a regime change.
- Broker vs yfinance feed reconciliation: broker shows -$30 vs Fri broker close $100,592.43 (essentially flat). The ~$147 IEX-lag gap from Fri close has narrowed to ~$30 — converging as expected per Fri lesson; no action.

## Open positions (broker live mark @ 13:37Z)

| Symbol | Qty | Avg Entry | Mark | Market Value | Unrealized P&L | Day Δ | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|-----:|-------------:|---------------:|------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $679.135 | $33,503.32 | +$169.32 (+0.51%) | -0.045% | 33.32% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $417.870 |  $4,814.60 | +$148.60 (+3.19%) | -0.961% |  4.79% |  7%            | 10% trail on 11 sh GTC, HWM $428.17, stop $385.35 — 0.522 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $420.075 |  $4,731.77 |  +$65.77 (+1.41%) | -1.209% |  4.71% |  7%            | 10% trail on 11 sh GTC, HWM $442.36, stop $398.12 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $401.590 |  $4,838.06 | +$172.06 (+3.69%) | **+1.208%** (best) |  4.81% |  7%            | 10% trail on 12 sh GTC, HWM $403.70, stop $363.33 — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $606.255 |  $4,709.07 |  +$43.07 (+0.92%) | -1.304% |  4.68% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| LLY    |  3.341161 | $997.857 |  $990.76 |  $3,310.29 |  -$23.71 (-0.71%) | -1.411% (worst) |  3.29% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| V      | 10.256781 | $325.053 | $325.840 |  $3,342.07 |   +$8.07 (+0.24%) | +0.028% |  3.32% |  5%            | 10% trail on 10 sh GTC, HWM $328.99, stop $296.09 — 0.257 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $481.300 |  $3,313.25 |  -$20.75 (-0.62%) | -0.292% |  3.29% |  5%            | 10% trail on 6 sh GTC, HWM $488.30, stop $439.47 — 0.884 sh unprotected |

Total committed: $62,562.42 (62.21% of equity)
Cash retained: $38,000.00 (37.79%)
Open positions: 8 / 10 (NVDA deferred; 9th slot held in reserve)
Leverage: 0.62x (cap 2x)
All 8 trailing stops verified `status=new` GTC on Alpaca @ 13:37Z. HWMs unchanged from Fri close — no fresh intraday highs in first ~7 min. Cushion ≥6.8% on every name.
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,890 notional (~1.88% of equity). Mitigation deferred until after tranche 3 consolidates remainders to ≥1 whole share.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings 2026-05-20 (Wed) post-close. Guardrail-#8 earnings
  window **open since 2026-05-15**. Entry blocked. Re-evaluate post-print Thu 5/21
  per strategy caveat (still needs ≥1 -3% red day before completing tranches 2+3).
- **DCA tranche 3 of 3** — **DEFERRED PER ROBIN DECISION 2026-05-16: Option B**
  (Processed in `memory/inbox.md`). Earliest re-evaluation window: Thu 2026-05-21
  in 01-pre-market (post NVDA-print + 3 trading days of Warsh-era tape). Most likely
  actual execution: Mon 2026-05-25 or Tue 2026-05-26 if tape settles cleanly. T3
  sizing per `strategy.md` v2 DCA rule: VOO capped at `min($16,667, 0.30 × cash_at_open)`,
  residual rolls forward to T4/T5.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **DEFERRED** to earliest Thu 2026-05-21 evaluation; most-likely-execution Mon 2026-05-25 / Tue 2026-05-26.

## Today's trades

**Zero trades placed in 02-market-open.** Plan from 01-pre-market executed cleanly: all 8 holds = HOLD, NVDA = WAIT, T3 = DEFER. No watchlist trigger fired. No stop maintenance required (HWMs unchanged, no breaches). See `memory/daily/2026-05-18.md` for full attribution.

## Recent Closed Positions (last 5)

(none)
