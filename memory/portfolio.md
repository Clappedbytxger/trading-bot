---
last_updated: 2026-05-25T20:17:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 5 of 30 — Mon 5/25 Memorial Day holiday EOD WhatsApp slot; cash session CLOSED all day)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 05-close-summary (weekday holiday; market closed; 0 trades book-wide today; equity reconciliation; per-sleeve LM-cum attribution; WhatsApp DE evening brief sent; bull-personal piggyback follows)
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

# Portfolio — 05-close-summary 2026-05-25 (LM Day 5 EOD LOCKED, Memorial Day holiday)

> **Phase note**: Mon 2026-05-25 05-close-summary EOD WhatsApp slot.
> Memorial Day cash session was closed all day; `clock.is_open=False`
> confirmed at 20:17Z broker re-pull (next_open Tue 2026-05-26
> 13:30Z). Equity execution impossible book-wide; only Crypto sleeve
> (24/7) could have fired, and the 04-pre-close 19:37Z scan returned
> 0 signals. **0 trades book-wide on Mon 5/25.** Equity UNCHANGED
> across all 4 Mon intraday snapshots + Sun at **$100,901.97**
> (broker re-quote stream pushed zero new ticks Sun → 12:13Z → 16:39Z
> → 19:37Z → 20:17Z across all 10 positions). Day P&L vs Fri 5/22
> EOD: **-$4.07 / -0.0040%** (broker reconciliation noise; UPL-Δ
> attribution Core -$9.04, Swing +$5.85, others $0). Day alpha vs
> SPY: **0 bp** (no Mon tape; carryover -25.8 bp from 5/22 final).
> LM cumulative since 5/21 baseline: **+$140.25 / +0.1392% equity;
> -26.2 bp alpha vs SPY** (≈ -25.8 bp reported carryover, within
> reconciliation noise). Per-sleeve LM cum: **Core +$180.25 (best) /
> Swing -$39.13 (worst) / DT $0 / Crypto $0 / Options $0**. All 10
> GTC stops verified `OrderStatus.NEW` at 20:17Z. WhatsApp DE
> evening brief sent. Next equity touchpoint: **Tue 2026-05-26
> 01-pre-market at 13:00Z**.

## Sleeve summary (Mon 5/25 20:17Z 05-close-summary holiday EOD — identical to 19:37Z + 16:39Z + 12:13Z)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs 5/22 EOD | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|--------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,941.97 (Mon EOD)  |             8  |   +$941.97  |   +1.519%   | -$9.04        | Frozen — 8/8 stops live GTC; marks identical to Sun/12:13Z/16:39Z; AVGO 3.87% / GOOGL 3.97% still tightest 2 |
| Swing      |  $15,000             | $3,460.87 (Mon EOD)   |             2  |    -$39.13  |   -1.118%   | +$5.85        | NVDA -2.105% (cushion **2.96%**) / RL +0.199% (cushion 7.19%); both stops live GTC; marks identical to Sun/12:13Z/16:39Z |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — weekday holiday; force-flat=no-op; PDT count 0/5 (RESET on 5/23 broker rollover); sleeve untouched since Fri |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — Mon 19:37Z scan: 0/5 50/200 cross-up; 0/5 -10%/24h flush; weekend-momentum closed (no Fri fill); Friday-tighten N/A (Mon); **0 entries** |
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

**Notable Core changes since 03-midday 16:39Z (~3h ago)**:
- **All marks identical to 16:39Z snapshot** — broker's holiday quote
  stream produced ZERO new ticks across the entire Mon session
  (12:13Z → 16:39Z → 19:37Z). All 8 cushions unchanged.
- **LLY HWM unchanged at $1,070.3399** (no walk-up — holiday, no live
  trading). Stop $963.30591 intact.
- **All 8 trail orders verified `OrderStatus.NEW` GTC at 19:37Z**; no
  broker events all day.

**Cushion rank (Mon 19:37Z EOD, tightest first — identical to 16:39Z + 12:13Z)**:
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
**$0.00** vs 16:39Z, 12:13Z, and Sun (no fresh quotes; market closed
all day).

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Mon EOD  | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held (calendar / td) | Time stop | Strategy slug             |
|--------|----------:|----------:|---------:|-------------:|--------:|--------:|------:|--------:|--------------------------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 |  $215.33 |   $1,957.89  | -$42.11 | -2.105% | $208.96 GTC | **2.96%** | 3 cal / 1 td (holiday doesn't count) | 2026-06-02 (7 td out) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 |  $377.78 |   $1,502.98  |  +$2.98 | +0.199% | $350.64 GTC | 7.19% | 3 cal / 1 td | 2026-06-05 (10 td out) | `swing-earnings-drift`   |

**NVDA Mon EOD status (`swing-quality-pullback`)**: Mon EOD mark
$215.33, identical to 16:39Z, 12:13Z, and Sun. UPL -2.105% / -$42.11.
Cushion **2.96%** unchanged. Day-3 calendar of hold (5/22 fill →
5/23 Sat → 5/24 Sun → 5/25 Mon); only **1 trading-day elapsed** for
time-stop accounting (5/22 fill day; 5/25 holiday doesn't count).
Thesis intact: -6.88% pullback from 52w-Hi $236.54; quality
compounder fundamentals unchanged; weekend analyst median PT $275
reinforces upside. No tighten-to-breakeven (UPL still negative;
tighten only fires at UPL ≥+5%). No time-stop hit. Stop $208.96 GTC
verified `OrderStatus.NEW` at 19:37Z. **NO action this routine.**
**Tue 5/26 open watch**: if cushion compresses <2% (mark ≈ $213.22),
tighten posture per Day-1 experiment-log Watch note.

**RL Mon EOD status (`swing-earnings-drift`)**: Mon EOD mark $377.78,
identical to 16:39Z, 12:13Z, and Sun. UPL **+0.199%** / +$2.98.
Cushion 7.19%. Day-3 calendar of hold; only **1 trading-day elapsed**.
PEAD thesis intact (UBS PT $511 / Needham $405 weekend re-iterations).
No tighten-to-breakeven (UPL <+5%; tighten check mark $395.88).
First time-stop check on 6/5 close. Stop $350.64 GTC verified
`OrderStatus.NEW` at 19:37Z. **NO action this routine.**

## Daytrade / Scalp sleeve (intraday only — weekday holiday; FORCE-FLAT = no-op)

Empty (0 / 5). $10k budget intact. **PDT count 0 / 5d** (RESET on 5/23
broker rollover from provisional 2). Memorial Day cash session closed
— no entries possible all day. **Force-flat step (3c) is a NO-OP**
because the sleeve had 0 positions going into 04-pre-close. No inbox
roll-to-swing override pending. Verified open positions count = 0 after
Step 3c. Heads-up for Tue 5/26: ORB / VWAP / gap-scan watches re-arm
at 02-market-open; up to 2 new Daytrade entries permitted per 03-midday
spec; PDT budget full 5/5.

## Crypto sleeve (24/7, $5k budget intact) — SCANNED

Empty (0 / 4). Mon 19:37Z scan of universe:

| Coin     | Last (Mon EOD) | 24h    | 7d     | 50DMA       | 200DMA      | State        | 50/200 gap | Δ vs 16:39Z |
|----------|---------------:|-------:|-------:|------------:|------------:|--------------|-----------:|--------------|
| BTC-USD  |  $77,339.03    | +0.46% | +0.50% |  $76,938.66 |  $80,405.97 | 50<200 DOWN  | **-4.31%** | UNCHANGED -4.31% (3rd consecutive scan stalled) |
| ETH-USD  |   $2,118.33    | +0.97% | -0.48% |   $2,264.21 |   $2,540.84 | 50<200 DOWN  |    -10.89% | -10.88% → -10.89% (1bp wider) |
| SOL-USD  |      $85.59    | +0.40% | +0.34% |      $86.51 |     $106.77 | 50<200 DOWN  |    -18.98% | -18.97% → -18.98% (1bp wider) |
| AVAX-USD |       $9.37    | +1.77% | +1.47% |       $9.40 |      $11.14 | 50<200 DOWN  |    -15.61% | -15.60% → -15.61% (1bp wider) |
| LINK-USD |       $9.529   | +1.06% | -0.67% |       $9.508|      $10.88 | 50<200 DOWN  |    -12.63% | -12.62% → -12.63% (1bp wider) |

- **`crypto-trend-follow`**: 0/5 50/200 cross-up. BTC convergence
  **remains stalled at -4.31%** — third consecutive intraday scan
  (12:11Z → 16:39Z → 19:37Z) at the same gap. Mon's daily candle has
  been a sideways grind in the $77k handle (price slipped $77,558 →
  $77,339 between 16:39Z and 19:37Z, -0.28% intraday, but the 50-DMA
  + 200-DMA rounding absorbed it). The 5-9 td extrapolation now
  extends to 6-10 td (Mon contributed ~0 net pp). **0 entries.**
- **`crypto-mean-reversion`**: 0/5 24h flush <-10%; largest 24h move
  is AVAX **+1.77%** (positive direction, opposite of trigger).
  **0 entries.**
- **`crypto-weekend-momentum`**: Fri 5/22 21:00Z trigger NOT met
  (BTC 7d -3.02% << +2%) → no Fri-close fill → no Mon-open exit
  monitor needed. **Closed; re-arm next Fri 5/29 21:00Z.**
- **Friday-tighten (-8% → -6%)**: spec rule applies on **Friday only**.
  Today is Monday — **N/A**. Sleeve has 0 open positions anyway.

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

## Today's trades (Mon Memorial Day holiday — EOD locked)

(none — 0 trades book-wide on Mon 2026-05-25; equity market closed
for Memorial Day all day; crypto scan returned 0 entry signals at
12:11Z + 16:39Z + 19:37Z.)

## Organic broker events (Mon 5/25, no Bull action)

- None all day. All 10 GTC stops verified `OrderStatus.NEW` at 19:37Z.
  All marks identical to 16:39Z, 12:13Z, and Sun 5/24 weekend snap.
  LLY HWM held flat $1,070.3399 (no live trading → no walk-up).
  `daytrade_count` remained 0; `pattern_day_trader` False.

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

## LM Day 5 (Mon holiday) EOD running tally — LOCKED at 19:37Z

- Bull equity: **$100,901.97** (UNCHANGED vs Sun snap, vs 12:13Z, vs
  16:39Z; -$4.07 / -0.004% vs 5/22 EOD; +$140.25 / +0.139% vs 5/21
  EOD baseline). Broker `last_equity` $100,861.21 = 5/23 EOD watermark;
  today's equity +$40.76 vs that on overnight re-quote noise.
- SPY: $745.70 (Fri 5/22 close — no Mon holiday tape); VIX 16.82.
- Day-5 alpha (carryover only): **-25.8 bp** vs SPY (no Mon SPY tape;
  identical to 5/22 EOD final alpha and 5/23-5/24 carryover).
- LM cumulative (since 5/21 EOD baseline): **+$140.25 / +0.139%**
  equity; **-25.8 bp** alpha vs SPY (carryover).
- Per-sleeve LM cumulative: Core +$180.25 / Swing -$39.13 / DT $0 /
  Crypto $0 / Options $0.
- Top experiment LM Day 1-5: `core-buy-and-hold` +$180.25 UPL Δ.
- Bottom experiment LM Day 1-5: `swing-quality-pullback` -$42.11 UPL
  (NVDA only).
- Trades today: **0 entries, 0 closes**. Win/Loss: 0/0.
- PDT count (5d): **0** (RESET held since 5/23 broker rollover).
- Day 5 closing baseline locked: cumulative LM-window P&L $0 realized
  + Core UPL $941.97 + Swing UPL -$39.13 = $902.84 UPL total / LM cum
  alpha -25.8 bp / LM cum trade count 2 (both still open).
- **Next routine**: 05-close-summary at 21:15Z Mon (per cron — likely
  also snapshot-only on holiday; will collapse to EOD-snap WhatsApp
  brief if it fires). Then **Tue 2026-05-26 01-pre-market at 13:00Z**
  for the post-holiday open.
