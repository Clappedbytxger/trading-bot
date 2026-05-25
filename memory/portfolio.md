---
last_updated: 2026-05-25T16:39:23Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 5 of 30 — Mon 5/25 Memorial Day holiday; cash session CLOSED; crypto-only execution scan)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 03-midday (weekday holiday; market closed; 0 trades; equity snapshot-only; crypto scan = 0 signals)
total_value_usd: 100901.97
cash_usd: 34500.00
long_market_value_usd: 66401.97
day_pnl_usd_vs_5_22_eod: -4.07
day_pnl_pct_vs_5_22_eod: -0.0040
day_pnl_usd_vs_5_21_eod: +140.25
day_pnl_pct_vs_5_21_eod: +0.1392
prior_5_22_eod_usd: 100906.04
prior_5_21_eod_usd: 100761.72
prior_5_23_eod_broker_snap_usd: 100861.21
spy_close_5_22_usd: 745.70
spy_close_5_21_usd: 742.72
spy_day_pct_5_22: +0.4012
day_alpha_bp_vs_spy: 0.0 (Memorial Day — no SPY tape; carryover -25.8 bp from 5/22 EOD)
lm_cum_pnl_usd_since_5_21_eod: +140.25
lm_cum_pnl_pct_since_5_21_eod: +0.1392
lm_cum_alpha_bp_vs_spy: -25.8 (carryover from 5/22 EOD; no Mon holiday SPY tape)
ytd_pnl_pct: 0.8909
benchmark_spx_ytd: 9.4636
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 745.70 (Fri 5/22 close — no Mon holiday tape)
alpha_vs_spx_ytd_pct: -8.5727
position_count_total: 10
position_count_core: 8
position_count_swing: 2
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.66
options_buying_power_usd: 67700.98
options_approved_level: 3
daytrade_count_5d: 0
pattern_day_trader: false
cash_reserve_min_usd: 3000
cash_available_for_non_core_sleeves_usd: 31500
sleeve_budget_swing_usd: 15000
sleeve_budget_daytrade_usd: 10000
sleeve_budget_crypto_usd: 5000
sleeve_budget_options_premium_usd: 5000
sleeve_used_swing_usd: 3500
sleeve_used_daytrade_usd: 0
sleeve_used_crypto_usd: 0
sleeve_used_options_usd: 0
polygon_api_key_set: true
polygon_options_chain_gated: true
macro_risk_off_active: false
vix_close_5_22: 16.82
market_state: closed (Mon 2026-05-25 Memorial Day; next_open Tue 2026-05-26T13:30Z)
next_open: 2026-05-26T13:30:00Z
---

# Portfolio — 03-midday 2026-05-25 (LM Day 5, Memorial Day holiday; cash session closed)

> **Phase note**: Mon 2026-05-25 03-midday on a Memorial Day cash-session-
> closed weekday. `clock.is_open=False` confirmed; equity execution
> impossible book-wide; only Crypto sleeve (24/7) ran a full scan. 0
> trades book-wide. Equity unchanged from Sun snapshot at **$100,901.97**
> (broker re-quote stream identical Sun → Mon 12:13Z → Mon 16:39Z for
> all 10 positions). Crypto scan = 0/5 50/200 cross-up, 0/5 -10%/24h
> flushes, weekend-momentum no-op (no Fri-close fill). **0 crypto
> entries.** Macro risk-off N/A (no Mon SPY/VIX tape; carryover NOT
> active). Next equity touchpoint: Tue 2026-05-26 01-pre-market at
> 13:00Z (post-holiday open).

## Sleeve summary (Mon 5/25 16:39Z holiday snapshot — identical to 12:13Z)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs 5/22 EOD | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|--------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,941.97 (Mon mark) |             8  |   +$941.97  |   +1.519%   | -$9.04        | Frozen — 8/8 stops live GTC; marks identical to Sun/12:13Z; AVGO 3.87% / GOOGL 3.97% still tightest 2 |
| Swing      |  $15,000             | $3,460.87 (Mon mark)  |             2  |    -$39.13  |   -1.118%   | +$5.85        | NVDA -2.105% (cushion **2.96%**) / RL +0.199% (cushion 7.19%); both stops live GTC; marks identical to Sun/12:13Z |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — weekday holiday N/A; PDT count 0/5 (RESET on 5/23 broker rollover); sleeve untouched since Fri |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — Mon 16:39Z scan: 0/5 50/200 cross-up; 0/5 -10%/24h flush; weekend-momentum no-monitor (no Fri fill); **0 entries** |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     |    $0         | Empty — Polygon options-chain still gated; 4th re-test scheduled Tue 5/26 |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     |    —          | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty        | Avg Entry | Mon Mark   | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|-----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341  |  $675.703 |   $685.55  |  $33,819.79  |  +$485.79  |  +1.457% |  33.52% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.54% |
| MSFT   | 11.521758  |  $404.973 |   $418.57  |   $4,822.66  |  +$156.66  |  +3.358% |   4.78% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.96% |
| GOOGL  | 12.047273  |  $387.308 |   $382.97  |   $4,613.74  |   -$52.26  |  -1.120% |   4.57% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 3.97% (unchanged — 2nd-tightest)** |
| META   |  7.767476  |  $600.710 |   $610.26  |   $4,740.18  |   +$74.18  |  +1.590% |   4.70% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 8.01% |
| AVGO   | 11.264102  |  $414.236 |   $414.14  |   $4,664.91  |    -$1.09  |  -0.023% |   4.62% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.87% (unchanged — still tightest)** |
| V      | 10.256781  |  $325.053 |   $328.88  |   $3,373.25  |   +$39.25  |  +1.178% |   3.34% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.28% |
| BRK.B  |  6.883950  |  $484.315 |   $486.38  |   $3,348.22  |   +$14.22  |  +0.426% |   3.32% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 9.45% |
| LLY    |  3.341161  |  $997.857 | $1,065.00  |   $3,558.34  |  +$224.34  |  +6.729% (best UPL) |   3.53% | trail 10% / 3 sh GTC / HWM $1,070.3399 (held flat) / stop $963.30591 / cushion 9.55% |

**Notable Core changes since 01-pre-market 12:13Z (~4.5h ago)**:
- **All marks identical to 12:13Z snapshot** — broker's holiday quote stream
  produced no fresh ticks for any Core name. All 8 cushions unchanged.
- **LLY HWM unchanged at $1,070.3399** (no walk-up — holiday, no live
  trading). Stop $963.30591 intact.
- **All 8 trail orders verified `OrderStatus.NEW` GTC**; no broker events.

**Cushion rank (Mon 16:39Z, tightest first — identical to 12:13Z)**:
1. AVGO **3.87%** (still tightest)
2. GOOGL **3.97%** (2nd-tightest)
3. MSFT 6.96%
4. META 8.01%
5. V 8.28%
6. BRK.B 9.45%
7. VOO 9.54%
8. LLY 9.55%

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken.**

Total Core committed: $62,941.97 (62.38% of equity). Mon Core UPL Δ
**$0.00** vs 12:13Z and vs Sun (no fresh quotes; market closed).

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Mon Mark | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held (calendar / td) | Time stop | Strategy slug             |
|--------|----------:|----------:|---------:|-------------:|--------:|--------:|------:|--------:|--------------------------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 |  $215.33 |   $1,957.89  | -$42.11 | -2.105% | $208.96 GTC | **2.96%** | 3 cal / 1 td (holiday doesn't count) | 2026-06-02 (7 td out) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 |  $377.78 |   $1,502.98  |  +$2.98 | +0.199% | $350.64 GTC | 7.19% | 3 cal / 1 td | 2026-06-05 (10 td out) | `swing-earnings-drift`   |

**NVDA Mon status (`swing-quality-pullback`)**: Mon mark $215.33,
identical to 12:13Z and Sun. UPL -2.105% / -$42.11. Cushion **2.96%**
unchanged. Day-3 calendar of hold (5/22 fill → 5/23 Sat → 5/24 Sun →
5/25 Mon); only **1 trading-day elapsed** for time-stop accounting
(5/22 fill day; 5/25 holiday doesn't count). Thesis intact: -6.88%
pullback from 52w-Hi $236.54; quality compounder fundamentals
unchanged; weekend analyst median PT $275 reinforces upside.
NO action this routine. **Tue 5/26 open watch**: if cushion compresses
<2% (mark ≈ $213.22), tighten posture per Day-1 experiment-log Watch note.

**RL Mon status (`swing-earnings-drift`)**: Mon mark $377.78, identical
to 12:13Z and Sun. UPL **+0.199%** / +$2.98. Cushion 7.19%. Day-3
calendar of hold; only **1 trading-day elapsed**. PEAD thesis intact
(UBS PT $511 / Needham $405 weekend re-iterations). First time-stop
check on 6/5 close. NO action this routine.

## Daytrade / Scalp sleeve (intraday only — weekday holiday N/A)

Empty (0 / 5). $10k budget intact. **PDT count 0 / 5d** (RESET on 5/23
broker rollover from provisional 2). Memorial Day cash session closed
— no entries possible. **No action this routine.** Heads-up for Tue
5/26: ORB / VWAP / gap-scan watches re-arm at 02-market-open; up to 2
new Daytrade entries permitted per 03-midday spec; PDT budget full 5/5.

## Crypto sleeve (24/7, $5k budget intact) — SCANNED

Empty (0 / 4). Mon 16:39Z scan of universe:

| Coin     | Last (Mon)  | 24h     | 7d      | 50DMA       | 200DMA      | State        | 50/200 gap | Δ vs 12:11Z |
|----------|------------:|--------:|--------:|------------:|------------:|--------------|-----------:|--------------|
| BTC-USD  |  $77,558.11 |  +0.75% |  +0.78% |  $76,943.04 |  $80,407.07 | 50<200 DOWN  |     -4.31% | UNCHANGED -4.31% (stalled) |
| ETH-USD  |   $2,127.29 |  +1.40% |  -0.06% |   $2,264.39 |   $2,540.89 | 50<200 DOWN  |    -10.88% | -10.89% → -10.88% |
| SOL-USD  |      $86.06 |  +0.95% |  +0.89% |      $86.52 |     $106.77 | 50<200 DOWN  |    -18.97% | -18.98% → -18.97% |
| AVAX-USD |       $9.44 |  +2.53% |  +2.23% |       $9.40 |      $11.14 | 50<200 DOWN  |    -15.60% | -15.61% → -15.60% |
| LINK-USD |       $9.599|  +1.80% |  +0.06% |       $9.509|      $10.88 | 50<200 DOWN  |    -12.62% | -12.63% → -12.62% |

- **`crypto-trend-follow`**: 0/5 50/200 cross-up. BTC convergence
  **stalled at -4.31%** between 12:11Z scan and 16:39Z scan
  (the daily candle for Mon UTC has only added ~0.4% to BTC price
  with the 50-DMA already incorporating Sun's tape — the next pp/day
  convergence step requires Tue's full session). At the underlying
  ~0.4 pp/day prior pace, BTC cross-up could still fire within 5-9 td.
  **Correction note**: the 12:13Z 01-pre-market section claimed LINK
  50-DMA was above 200-DMA-trail by $0.01 ($9.51 vs $9.50); fresh
  authoritative scan shows LINK 200-DMA is **$10.88** — well above
  the 50-DMA $9.509. LINK is NOT on the cusp; gap -12.62% from
  cross-up. BTC remains the only meaningful convergence candidate.
  **0 entries.**
- **`crypto-mean-reversion`**: 0/5 24h flush <-10%; largest 24h move
  is AVAX **+2.53%** (positive direction, opposite of trigger).
  **0 entries.**
- **`crypto-weekend-momentum`**: Fri 5/22 21:00Z trigger NOT met
  (BTC 7d -3.02% << +2%) → no Fri-close fill → no Mon-open exit
  monitor needed. **No-op.** Validation: BTC 7d Mon = +0.78%
  (positive but late; Fri 5/22 read correctly excluded entry).

**Decision: NO Crypto entries this routine.** Sleeve remains 0 / 4
positions; budget $5,000 intact. Continue convergence monitoring at
every 03-midday + 05-close-summary.

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. Polygon options-
chain 4th re-test scheduled for Tue 5/26 01-pre-market (today is no-op;
options market closed for Memorial Day; 403 was a tier-gate issue, not
a market-hours issue). NVDA conviction continues to route via Swing
equity.

- 7 DTE rule: no positions, no-op.
- IV-crush check: no positions, no-op.
- Protective-put staleness: none open.

**Decision: NO Options actions this routine.**

## Today's trades (Mon Memorial Day holiday)

(none — 0 trades book-wide on Mon 2026-05-25; equity market closed for
Memorial Day; crypto scan returned 0 entry signals.)

## Organic broker events (this routine, no Bull action)

- None. All 10 GTC stops verified `OrderStatus.NEW`. All marks identical
  to 12:13Z 01-pre-market snap (and to Sun 5/24 weekend snap). LLY HWM
  held flat $1,070.3399. daytrade_count remained 0; PDT False.

## Pending (not yet opened / re-evaluated)

- **AAPL** — `swing-short-rejection` re-watch on Tue 5/26 01-pre-market.
- **ARM** — `swing-momentum-breakout` re-arm only if ARM closes back
  below $290; above $290 + below $310 stays WATCH on Tue 5/26.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain (4th
  re-test scheduled for Tue 5/26 01-pre-market). NVDA conviction
  running via equity Swing.
- **Crypto weekend-momentum** — confirmed NO ENTRY at Fri 5/22 EOD;
  monitor closed Sun. Re-arm next Fri 5/29 21:00Z (05-close-summary).
- **Crypto trend-follow (BTC)** — gap stalled at -4.31% on Mon; needs
  Tue full session to resume convergence. Monitor on every 03-midday.
- **SPY protective-put** for Thu 5/28 PCE+GDP — decision deferred to
  Tue 5/26 / Wed 5/27 02-market-open contingent on Polygon chain unblock.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+
  per strategy.md v3 LM freeze.
- **AVGO earnings 2026-06-03**: 5 td out from Tue 5/26 cash open. Core
  hold posture intact; LM-paused Live-Phase #8 means no automatic
  exclusion zone for Core (and Core is frozen anyway).

## Recent Closed Positions (last 5)

(none — no closes across Live-Phase paper run + LM Day 1-5)

## LM Day 5 (Mon holiday) running tally

- Bull equity: **$100,901.97** (UNCHANGED vs Sun snap; -$4.07 / -0.004%
  vs 5/22 EOD; +$140.25 / +0.139% vs 5/21 EOD baseline). Broker
  last_equity snap $100,861.21 represents the 5/23 EOD broker mark;
  today's equity +$40.76 vs that watermark on overnight re-quote noise.
- SPY: $745.70 (Fri 5/22 close, no Mon holiday tape); VIX 16.82.
- Day-5 alpha (carryover only): **-25.8 bp** vs SPY (no Mon SPY tape;
  identical to 5/22 EOD final alpha and 5/23-5/24 carryover).
- LM cumulative (since 5/21 EOD baseline): **+$140.25 / +0.139%**
  equity; **-25.8 bp** alpha vs SPY (carryover).
- Per-sleeve LM cumulative: Core +$180.25 / Swing -$39.13 / DT $0 /
  Crypto $0 / Options $0.
- Top experiment LM Day 1-5: `core-buy-and-hold` +$180.25.
- Bottom experiment LM Day 1-5: `swing-quality-pullback` -$42.11
  (NVDA only).
- Trades today: 0 entries, 0 closes. Win/Loss: 0/0.
- PDT count (5d): **0** (RESET held since 5/23 broker rollover).
