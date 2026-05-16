---
last_updated: 2026-05-16T20:35:00Z
broker: alpaca
account_type: paper
total_value_usd: 100739.35
cash_usd: 38000.00
day_pnl_pct: -0.4924
week_pnl_pct: 0.7394
week_spy_pct: 0.1355
week_alpha_vs_spy_bp: 60.4
ytd_pnl_pct: 0.7394
benchmark_spx_ytd: 8.493
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 739.17
alpha_vs_spx: -7.754
ytd_alpha_tightening_this_week_pp: 0.502
position_count: 8
---

# Portfolio — 06-weekly-review 2026-05-16 (end-of-week KW 20 snapshot)

## Weekly delta and alpha (week of 2026-05-11 → 2026-05-15)

| Metric                          | Mon AM open (5/12) | Fri close (5/15) | Δ week        |
|---------------------------------|-------------------:|-----------------:|--------------:|
| Equity                          |        $100,000.00 |      $100,739.35 |    +$739.35   |
| Bull cumulative return          |              0.00% |          +0.74%  |    +74 bp     |
| SPY (entry 5/12 close $738.17)  |                  — |        $739.17   |    +0.135%    |
| **Week alpha vs SPY**           |                  — |              —   |   **+60 bp**  |
| SPX YTD                         |              +8.35% |        +8.49%   |    +14 bp     |
| YTD alpha vs SPX                |             -8.26% |         -7.75%  |   **+51 bp**  |
| Cash %                          |             100.0% |          37.7%  |    -62.3 pp   |
| Open positions                  |                  0 |               8 |       +8      |
| Tranches filled                 |                  0 |              16 |     +16 (T1+T2) |

Daily alpha tightening trajectory (cumulative YTD alpha vs SPX):
- 5/12 close (T1 fill day): **-8.26%**
- 5/13 close (T2 fill day): -8.13%  (+13 bp tightening)
- 5/14 close (no-trade):    -8.62%  (-49 bp widening on SPY +0.52% day)
- 5/15 close (no-trade):    **-7.75%** (+87 bp tightening on SPY -1.20% day)
- Net week: **+51 bp YTD-alpha tightening**

# Portfolio — 05-close-summary 2026-05-15 (final post-close snapshot)

**No trades today** (4th routine of the day with zero broker activity).
Daily file under `## 05-close-summary` has the full day attribution.

Final equity at close (yfinance official close prices for all 8 holdings + cash):
**$100,739.35** vs yesterday close $101,237.77 → **Day P&L -$498.42 / -0.4924%**.
SPY closed at **$739.17** → **SPY day -1.2029%**. Bull beat SPY by **+71 bp** on
the day — cleanest day-alpha tightening of the week, driven by MSFT's +3.05%
close (against a tape with AVGO -3.32% and the AI sleeve broadly red) plus the
37.7% cash sleeve absorbing ~45 bp of the macro drag and V/LLY/BRK.B
(defensive ballast) collectively hugging flat against the down-tape.

Alpha vs SPX at close: **-7.754%** — tightened **7 bp** from the 04-pre-close
-7.828% read at 19:32Z, continuing the day's "defensive-on-weak-tape" pattern
into the print. Cumulative week alpha trajectory: Thu close -8.62% → Fri AM
open -7.79% → Fri midday -7.84% → Fri pre-close -7.83% → **Fri close -7.75%**
= +0.87 pp YTD-alpha tightening for the week on a SPY -1.20% Friday closer.

Note on broker feed: Alpaca live API at 21:10Z showed equity $100,592.43 due
to IEX quote lag (broker prices ~30-60 bp stale vs official close on most
names). Reconstructed equity from yfinance close prices for the canonical
EOD record above. ~$147 reconciliation gap will close to zero by Mon AM when
Alpaca's overnight mark-to-market catches up. No action needed.

## Open Positions (close-of-session marks)

| Symbol | Qty | Avg Entry | Close | Market Value | Unrealized P&L | Day Δ | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|------:|-------------:|---------------:|------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $679.440 | $33,514.27 | +$180.30 (+0.55%) | -1.21% | 33.27% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $421.920 |  $4,862.07 | +$195.27 (+4.19%) | **+3.05%** (best day) |  4.83% |  7%            | 10% trail on 11 sh GTC, HWM **$428.17** (↑) , stop **$385.35** (↑) — 0.522 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $425.190 |  $4,789.65 | +$123.36 (+2.65%) | **-3.32%** (worst day) |  4.75% |  7%            | 10% trail on 11 sh GTC, HWM $442.36, stop $398.12 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $396.780 |  $4,780.32 | +$114.10 (+2.45%) | -1.07% |  4.75% |  7%            | 10% trail on 12 sh GTC, HWM $403.70, stop $363.33 — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $614.230 |  $4,771.27 | +$105.07 (+2.25%) | -0.68% |  4.74% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| LLY    |  3.341161 | $997.857 |$1004.920 |  $3,357.65 |  +$23.59 (+0.71%) | -0.18% |  3.33% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| V      | 10.256781 | $325.053 | $325.750 |  $3,341.16 |   +$7.16 (+0.21%) | **+1.00%** |  3.32% |  5%            | 10% trail on 10 sh GTC, HWM $328.99, stop $296.09 — 0.257 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $482.700 |  $3,322.96 |  -$11.12 (-0.33%) | -0.28% |  3.30% |  5%            | 10% trail on 6 sh GTC, HWM $488.30, stop $439.47 — 0.884 sh unprotected |

Total committed: $62,739.35 (62.28% of equity)
Cash retained: $38,000.00 (37.72%)
Open positions: 8 / 10 (NVDA deferred; 9th slot held in reserve)
Leverage: 0.62x (cap 2x)
Day P&L: -$498.42 (-0.492%) — Bull beat SPY day -1.203% by **+71 bp** on cash
drag + MSFT outperformance + V positive on the day. Alpha vs SPX **tightened**
into the close (-7.83% pre-close → -7.75% close) as the AI sleeve red-but-not-
bleeding traded down less than SPY's mega-cap-weighted basket.
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,890 notional (~1.88% of equity).
Mitigation still deferred until after tranche 3 consolidates remainders to ≥1 whole share.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings 2026-05-20 (Wed) post-close. Guardrail-#8 earnings
  window **open since 2026-05-15**. Entry blocked. Re-evaluate post-print Thu 5/21
  per strategy caveat (still needs ≥1 -3% red day before completing tranches 2+3).
- **DCA tranche 3 of 3** — **STILL BLOCKED, now 3rd business day in a row** (5/14,
  5/15 missed; 5/18 Monday morning depends on Robin's reply). Robin's A/B reply
  (post-14:05Z WhatsApp full re-explanation) still pending as of 21:15Z. No memory
  edit on `main` since 14:48Z PR #17 merge. Path of least intervention remains
  **(B) defer ~1 week into post-NVDA + post-Warsh window** — the de-facto default
  if Robin's reply is not received by Mon 13:00Z 01-pre-market.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **NOT EXECUTED 2026-05-14** — blocked by missing pre-market draft.
- Tranche 3 of 3: **NOT EXECUTED 2026-05-15** — same root cause + Robin A/B reply pending.

## Recent Closed Positions (last 5)

(none)
