---
last_updated: 2026-05-18T16:37:15Z
broker: alpaca
account_type: paper
total_value_usd: 100503.65
cash_usd: 38000.00
day_pnl_pct_vs_fri_yf_close: -0.2342
day_pnl_pct_vs_fri_broker_close: -0.0883
week_pnl_pct: 0.5037
week_spy_pct: -0.4406
ytd_pnl_pct: 0.5037
benchmark_spx_ytd: 8.0140
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 735.91
alpha_vs_spx: -7.5103
ytd_alpha_widening_today_open_bp: +35.1
position_count: 8
leverage_x: 0.62
---

# Portfolio — 03-midday 2026-05-18 (mid-session snapshot, 16:37Z)

## Today's intraday progression

| Metric                          | Fri close (yf-basis) | Mon post-open (13:37Z) | Mon mid-day (16:37Z) | Δ vs Fri close |
|---------------------------------|---------------------:|-----------------------:|---------------------:|---------------:|
| Equity                          |        $100,739.35  |        $100,562.42    |        $100,503.65  |    -$235.70 (-0.234%)   |
| SPY                             |             $739.17 |               $738.70 |              $735.91 |    -$3.26 (-0.441%) |
| Cash %                          |             37.72%  |              37.79%   |              37.81%  |    +0.09 pp       |
| Position count                  |                  8  |                   8   |                   8  |     0             |
| Tranches filled                 |                 16  |                  16   |                  16  |     0             |

- Day P&L (yf-basis): **-0.234%** vs SPY day **-0.441%** → Bull leads SPY by **+21 bp** intraday. Versus the post-open print where Bull lagged SPY by -11 bp, that's a **+32 bp swing in Bull's favor over the mid-session window** — defensive ballast + cash drag now showing the design intent on a weak-tape day.
- Alpha YTD: **-7.510%** vs SPX **+8.014%** (Bull YTD +0.504%) → **+35.1 bp tightening** from this morning's open print (-7.861%). Comes mostly from SPX rolling over -38 bp while Bull only gave back -6 bp net since open.
- Broker vs yfinance feed reconciliation: broker equity $100,503.65 vs Fri broker close $100,592.43 = -$88.78 (-0.088%) — broker basis essentially flat. The Fri IEX-lag gap continues to narrow as expected; no action.

## Open positions (broker live mark @ 16:37Z)

| Symbol | Qty | Avg Entry | Mark | Market Value | Unrealized P&L | UPL% | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|-----:|-------------:|---------------:|-----:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $676.505 | $33,373.58 |  +$39.58 | +0.12% | 33.21% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $419.950 |  $4,838.56 | +$172.56 | +3.70% (best)  |  4.81% |  7%            | 10% trail on 11 sh GTC, HWM $428.17, stop $385.35 — 0.522 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $417.350 |  $4,701.07 |  +$35.07 | +0.75% |  4.68% |  7%            | 10% trail on 11 sh GTC, HWM $442.36, stop $398.12 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $400.730 |  $4,827.70 | +$161.70 | +3.47% |  4.80% |  7%            | 10% trail on 12 sh GTC, **HWM $408.61** (auto-advanced from $403.70 at open), **stop $367.75** (from $363.33) — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $609.320 |  $4,732.88 |  +$66.88 | +1.43% |  4.71% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| LLY    |  3.341161 | $997.857 |  $988.04 |  $3,301.20 |  -$32.80 | -0.98% (worst) |  3.28% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| V      | 10.256781 | $325.053 | $330.665 |  $3,391.56 |  +$57.56 | +1.73% |  3.37% |  5%            | 10% trail on 10 sh GTC, **HWM $330.86** (auto-advanced from $328.99 at open), **stop $297.77** (from $296.09) — 0.257 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $484.765 |  $3,337.10 |   +$3.10 | +0.09% |  3.32% |  5%            | 10% trail on 6 sh GTC, HWM $488.30, stop $439.47 — 0.884 sh unprotected |

Total committed: $62,503.65 (62.19% of equity)
Cash retained: $38,000.00 (37.81%)
Open positions: 8 / 10 (NVDA deferred; 9th slot held in reserve)
Leverage: 0.62x (cap 2x)
All 8 trailing stops verified `status=new` GTC on Alpaca @ 16:37Z. HWMs auto-advanced on V (+$1.87) and GOOGL (+$4.91) intraday; all others unchanged. Cushion ≥7.5% on every name.
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,886 notional (~1.88% of equity). Mitigation deferred until after tranche 3 consolidates remainders to ≥1 whole share.

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

**Zero trades placed in 03-midday.** Mid-day spec-triggers (UPL ≤ -7%, UPL ≥ +15%, thesis-break) inspected on all 8 positions: none fired. Worst position LLY -0.98%, best MSFT +3.70% — both deep inside the no-action band. Trailing-stop HWMs auto-advanced on V (+$1.87) and GOOGL (+$4.91) — Alpaca-managed, no manual intervention required. See `memory/daily/2026-05-18.md` for full mid-day attribution.

## Recent Closed Positions (last 5)

(none)
