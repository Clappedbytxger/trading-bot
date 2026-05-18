---
last_updated: 2026-05-18T19:40:32Z
broker: alpaca
account_type: paper
total_value_usd: 100611.93
cash_usd: 38000.00
day_pnl_pct_vs_fri_yf_close: -0.1265
day_pnl_pct_vs_fri_broker_close: +0.0194
week_pnl_pct: 0.6119
week_spy_pct: -0.2908
ytd_pnl_pct: 0.6119
benchmark_spx_ytd: 8.1770
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 737.02
alpha_vs_spx: -7.5651
ytd_alpha_widening_vs_midday_bp: -5.5
position_count: 8
leverage_x: 0.62
---

# Portfolio — 04-pre-close 2026-05-18 (pre-close snapshot, 19:40Z, ~20 min to close)

## Today's intraday progression

| Metric                          | Fri close (yf-basis) | Mon post-open (13:37Z) | Mon mid-day (16:37Z) | Mon pre-close (19:40Z) | Δ vs Fri close |
|---------------------------------|---------------------:|-----------------------:|---------------------:|-----------------------:|---------------:|
| Equity                          |        $100,739.35  |        $100,562.42    |        $100,503.65  |        $100,611.93    |    -$127.42 (-0.127%)   |
| SPY                             |             $739.17 |               $738.70 |              $735.91 |              $737.02  |    -$2.15 (-0.291%) |
| Cash %                          |             37.72%  |              37.79%   |              37.81%  |              37.77%   |    +0.05 pp       |
| Position count                  |                  8  |                   8   |                   8  |                   8   |     0             |
| Tranches filled                 |                 16  |                  16   |                  16  |                  16   |     0             |

- Day P&L (yf-basis): **-0.127%** vs SPY day **-0.291%** → Bull leads SPY by **+16.5 bp** intraday. Day-shape: -11 bp at open → +21 bp lead at midday → +16.5 bp lead pre-close — defensive ballast + AI-sleeve resilience both contributing.
- Alpha YTD: **-7.565%** vs SPX **+8.177%** (Bull YTD +0.612%) → **-5.5 bp widening** from midday print (-7.510%) but still **+29.6 bp tighter than this morning's open** (-7.861%).
- Broker basis vs Fri broker close ($100,592.43): **+$19.50 (+0.019%)** — broker basis green for the day; IEX-feed gap has fully closed.

## Open positions (broker live mark @ 19:40Z)

| Symbol | Qty | Avg Entry | Mark | Market Value | Unrealized P&L | UPL% | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|-----:|-------------:|---------------:|-----:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $677.440 | $33,419.70 |  +$85.70 | +0.26% | 33.22% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $423.215 |  $4,876.18 | +$210.18 | +4.51% (best)  |  4.85% |  7%            | 10% trail on 11 sh GTC, HWM $428.17, stop $385.35 — 0.522 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $418.920 |  $4,718.76 |  +$52.76 | +1.13% |  4.69% |  7%            | 10% trail on 11 sh GTC, HWM $442.36, stop $398.12 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $397.325 |  $4,786.68 | +$120.68 | +2.59% |  4.76% |  7%            | 10% trail on 12 sh GTC, HWM $408.61, stop $367.75 — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $611.390 |  $4,748.96 |  +$82.96 | +1.78% |  4.72% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| LLY    |  3.341161 | $997.857 | $983.300 |  $3,285.36 |  -$48.64 | -1.46% (worst) |  3.27% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| V      | 10.256781 | $325.053 | $332.500 |  $3,410.38 |  +$76.38 | +2.29% |  3.39% |  5%            | 10% trail on 10 sh GTC, **HWM $332.67** (auto-advanced from $330.86 mid-day), **stop $299.40** (from $297.77) — 0.257 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $488.950 |  $3,365.91 |  +$31.91 | +0.96% |  3.35% |  5%            | 10% trail on 6 sh GTC, **HWM $489.25** (auto-advanced from $488.30 mid-day), **stop $440.33** (from $439.47) — 0.884 sh unprotected |

Total committed: $62,611.93 (62.23% of equity)
Cash retained: $38,000.00 (37.77%)
Open positions: 8 / 10 (NVDA deferred; 9th slot held in reserve)
Leverage: 0.62x (cap 2x)
All 8 trailing stops verified `status=NEW` GTC on Alpaca @ 19:40Z. HWMs auto-advanced on V (+$1.81) and BRK.B (+$0.95) since midday; all other names unchanged. Cushion ≥7.0% on every name (LLY tightest ~6.6%).
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,888 notional (~1.88% of equity). Mitigation deferred until after tranche 3 consolidates remainders to ≥1 whole share.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings **2026-05-20 (Wed) post-close**. Guardrail-#8 earnings
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

**Zero trades placed today across 01-pre-market, 02-market-open, 03-midday, 04-pre-close.** All four routines honored the lesson-2026-05-16 "bias to inaction" rule. Spec triggers inspected throughout (UPL ≤ -7%, UPL ≥ +15%, thesis-break, day-end stop tighten): none fired. Trailing-stop HWMs auto-advanced today on V (+$1.81 net) and BRK.B (+$0.95) and GOOGL (+$4.91 at open) — Alpaca-managed; no manual intervention. See `memory/daily/2026-05-18.md` for full per-routine detail.

## Recent Closed Positions (last 5)

(none)
