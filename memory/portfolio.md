---
last_updated: 2026-05-24T16:36:33Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 4 of 30 — Sunday weekend-crypto-cycle)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 03-midday (weekend-crypto-cycle; market closed; 0 trades; crypto scan only)
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
day_alpha_bp_vs_spy: 0.0 (weekend — no SPY tape; carryover -25.8 bp from 5/22 EOD)
lm_cum_pnl_usd_since_5_21_eod: +140.25
lm_cum_pnl_pct_since_5_21_eod: +0.1392
lm_cum_alpha_bp_vs_spy: -25.8 (carryover from 5/22 EOD; no weekend SPY tape)
ytd_pnl_pct: 0.8909
benchmark_spx_ytd: 9.4636
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 745.70 (Fri 5/22 close — no weekend tape)
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
market_state: closed (Sunday — weekend; Mon 5/25 Memorial Day closed)
next_open: 2026-05-26T13:30:00Z
---

# Portfolio — 03-midday 2026-05-24 (LM Day 4, Sunday weekend-crypto-cycle)

> **Phase note**: Sun 2026-05-24 03-midday weekend cycle. `clock.is_open
> = False` confirmed; equities don't trade. 0 trades book-wide. Equity
> unchanged from Sat snapshot at **$100,901.97** (broker re-quote stream
> identical to Sat for all 10 positions). **LM Day 4 routine #1 of 1**
> (only 03-midday fires on weekends per cron `30 17 * * 1-7`). Crypto
> sleeve **scanned** — all 5 universe names still 50<200 DOWN; BTC gap
> narrowed further -5.09% → -4.67% but no cross; no -10%/24h flush;
> weekend-momentum no-monitor (no Fri-close fill). **0 crypto entries.**
> Macro risk-off N/A (no weekend tape). **Notable broker change**:
> `daytrade_count` rolled back 2 → 0 on the 5/23 EOD snap — provisional
> pre-count from the 5/22 Swing-w/-GTC-stop fills has reversed. PDT
> budget for Tue 5/26 fully restored at 5/5. Mon 2026-05-25 = Memorial
> Day (US cash session closed). Next equity touchpoint: Tue 2026-05-26
> 01-pre-market at 13:00Z.

## Sleeve summary (Sun 5/24 16:36Z weekend snapshot)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs 5/22 EOD | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|--------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,941.97 (Sun mark) |             8  |   +$941.97  |   +1.519%   | -$9.04        | Frozen — 8/8 stops live GTC; marks identical to Sat (no fresh tape); AVGO 3.87% / GOOGL 3.97% still tightest 2 |
| Swing      |  $15,000             | $3,460.87 (Sun mark)  |             2  |    -$39.13  |   -1.118%   | +$5.85        | NVDA -2.105% (cushion **2.96%**) / RL +0.199% (cushion 7.19%); both stops live GTC; marks identical to Sat |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — weekend N/A; **PDT count RESET 2 → 0** on 5/23 broker rollover; sleeve untouched since Fri |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — Sun scan: 0/5 50/200 cross-up; 0/5 -10%/24h flush; weekend-momentum no-monitor (no Fri fill); **0 entries** |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     |    $0         | Empty — Polygon options-chain still gated; 4th re-test scheduled Tue 5/26 |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     |    —          | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty        | Avg Entry | Sun Mark   | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|-----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341  |  $675.703 |   $685.55  |  $33,819.79  |  +$485.79  |  +1.457% |  33.52% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.54% |
| MSFT   | 11.521758  |  $404.973 |   $418.57  |   $4,822.66  |  +$156.66  |  +3.358% |   4.78% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.96% |
| GOOGL  | 12.047273  |  $387.308 |   $382.97  |   $4,613.74  |   -$52.26  |  -1.120% |   4.57% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 3.97% (unchanged vs Sat — 2nd-tightest)** |
| META   |  7.767476  |  $600.710 |   $610.26  |   $4,740.18  |   +$74.18  |  +1.590% |   4.70% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 8.01% |
| AVGO   | 11.264102  |  $414.236 |   $414.14  |   $4,664.91  |    -$1.09  |  -0.023% |   4.62% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.87% (unchanged vs Sat — still tightest)** |
| V      | 10.256781  |  $325.053 |   $328.88  |   $3,373.25  |   +$39.25  |  +1.178% |   3.34% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.28% |
| BRK.B  |  6.883950  |  $484.315 |   $486.38  |   $3,348.22  |   +$14.22  |  +0.426% |   3.32% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 9.45% |
| LLY    |  3.341161  |  $997.857 | $1,065.00  |   $3,558.34  |  +$224.34  |  +6.729% (best UPL) |   3.53% | trail 10% / 3 sh GTC / HWM $1,070.3399 (held flat) / stop $963.30591 / cushion 9.55% |

**Notable Core changes since Sat 5/23 16:36Z (~24h ago)**:
- **All marks identical to Sat snapshot** — broker's weekend quote stream
  produced no fresh ticks on Sunday across any Core name. All 8 cushions
  unchanged.
- **LLY HWM unchanged at $1,070.3399** (no walk-up — weekend, no live
  trading). Stop $963.30591 intact.
- **All 8 trail orders verified `OrderStatus.NEW` GTC**; no broker
  events to log.

**Cushion rank (Sun 16:36Z, tightest first — identical to Sat)**:
1. AVGO **3.87%** (still tightest)
2. GOOGL **3.97%** (2nd-tightest)
3. MSFT 6.96%
4. META 8.01%
5. V 8.28%
6. BRK.B 9.45%
7. VOO 9.54%
8. LLY 9.55%

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken.**

Total Core committed: $62,941.97 (62.38% of equity). Sunday Core UPL Δ
**$0.00** vs Sat (no fresh quotes).

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Sun Mark | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held | Time stop | Strategy slug             |
|--------|----------:|----------:|---------:|-------------:|--------:|--------:|------:|--------:|----------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 |  $215.33 |   $1,957.89  | -$42.11 | -2.105% | $208.96 GTC | **2.96%** | 1 td | 2026-06-02 (7 td out) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 |  $377.78 |   $1,502.98  |  +$2.98 | +0.199% | $350.64 GTC | 7.19% | 1 td | 2026-06-05 (10 td out) | `swing-earnings-drift`   |

**NVDA Sun status (`swing-quality-pullback`)**: Sun mark $215.33,
identical to Sat. UPL -2.105% (broker re-pricing the UPL% slightly
on Sun snap from -1.917% reported Sat; both reference the same
$215.33 mark — broker's internal `unrealized_plpc` field is a tad
sensitive to the avg-entry rounding). Cushion **2.96%** unchanged.
Day-3 thesis intact (-5% pullback from 52w-Hi quality compounder;
fundamentals unchanged). NO action this routine. **Tue 5/26 open
watch**: if cushion compresses to <2% (mark ≈ $213.22), tighten
posture per Day-1 experiment-log Watch note.

**RL Sun status (`swing-earnings-drift`)**: Sun mark $377.78,
identical to Sat. UPL **+0.199%** / +$2.98. Cushion 7.19%. First
time-stop check on 6/5 close. PEAD thesis intact for Day-3+ of
hold. NO action this routine.

## Daytrade / Scalp sleeve (intraday only — weekend N/A)

Empty (0 / 5). $10k budget intact. **PDT count RESET 0 / 5d**
(reverted from Sat's 2 on the 5/23 broker EOD snap — provisional
pre-count from 5/22 Swing-w/-GTC-stop entries has reversed since
no actual round-trips occurred). Weekend, no entries possible.
**No action this routine.** Heads-up for Tue 5/26: ORB setups may
re-trigger; up to 2 new Daytrade entries permitted per 03-midday
spec.

## Crypto sleeve (24/7, $5k budget intact) — SCANNED

Empty (0 / 4). Sun 16:36Z scan of universe:

| Coin     | Last (5/24) | 24h     | 7d      | 50DMA       | 200DMA      | State        | 50/200 gap | Δ vs Sat 5/23 50/200 gap |
|----------|------------:|--------:|--------:|------------:|------------:|--------------|-----------:|--------------------------|
| BTC-USD  |  $76,387.29 |  -0.37% |  -1.35% |  $76,759.64 |  $80,522.82 | 50<200 DOWN  |     -4.67% | narrowed -5.09% → -4.67% |
| ETH-USD  |   $2,094.73 |  -1.00% |  -1.55% |   $2,263.96 |   $2,546.79 | 50<200 DOWN  |    -11.11% | narrowed -11.40% → -11.11% |
| SOL-USD  |      $85.24 |  -0.49% |  +0.08% |      $86.43 |     $107.12 | 50<200 DOWN  |    -19.31% | narrowed -19.71% → -19.31% |
| AVAX-USD |       $9.21 |  -1.86% |  +0.33% |       $9.39 |      $11.17 | 50<200 DOWN  |    -15.92% | narrowed -16.28% → -15.92% |
| LINK-USD |       $9.42 |  -1.42% |  -1.37% |       $9.49 |      $10.91 | 50<200 DOWN  |    -12.97% | narrowed -13.37% → -12.97% |

- **`crypto-trend-follow`**: 0/5 50/200 cross-up. **BTC gap narrowed
  further -5.09% → -4.67% — leading the weekend convergence**; at
  current pace (≈ -0.4 pp/day) BTC could see a 50/200 cross-up within
  the next 6-10 trading days (rough extrapolation). The other 4 also
  narrowed but their gaps are 2-4x wider — they remain dormant. **0 entries.**
- **`crypto-mean-reversion`**: 0/5 24h flush <-10%; largest is AVAX
  -1.86%. **0 entries.**
- **`crypto-weekend-momentum`**: Fri 5/22 21:00Z trigger NOT met
  (BTC 7d -3.02% << +2%) → no position opened → no Sun monitor
  needed. **No-op.** (BTC 7d Sun = -1.35%, closer to neutral but
  still negative — validates the no-entry decision retrospectively.)

**Decision: NO Crypto entries this routine.** Sleeve remains 0 / 4
positions; budget $5,000 intact.

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. Polygon options-chain
4th re-test scheduled for Tue 5/26 01-pre-market (weekend re-test is
no-op; options market closed; 403 was a tier-gate, not a market-hours
issue). NVDA conviction already running via Swing equity.

- 7 DTE rule: no positions, no-op.
- IV-crush check: no positions, no-op.
- Protective-put staleness: none open.

**Decision: NO Options actions this routine.**

## Today's trades (Sun weekend-crypto-cycle)

(none — 0 trades book-wide on Sun 2026-05-24; crypto scan returned 0
entry signals; equities can't trade weekends.)

## Organic broker events (this routine, no Bull action)

- **`daytrade_count` ROLLED 2 → 0** on the 5/23 broker EOD snap (between
  Sat 16:36Z snapshot and Sun 16:36Z snapshot). Confirms the
  provisional pre-count from the 5/22 Swing-w/-GTC-stop fills has
  reversed since no actual round-trip occurred within the standard
  PDT day-trade detection window. PDT budget for Tue 5/26 = full
  5/5 again (5-day rolling).
- All marks otherwise identical to Sat — broker's weekend quote stream
  did not push any fresh ticks Sat → Sun. LLY HWM held flat at
  $1,070.3399. All 10 stops remain `OrderStatus.NEW` GTC.

## Pending (not yet opened / re-evaluated)

- **AAPL** — `swing-short-rejection` re-watch on Tue 5/26 01-pre-market.
- **ARM** — `swing-momentum-breakout` re-arm only if ARM closes back
  below $290; above $290 + below $310 stays WATCH on Tue 5/26.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain (4th
  re-test scheduled for Tue 5/26 01-pre-market). NVDA conviction
  running via equity Swing.
- **Crypto weekend-momentum** — confirmed NO ENTRY at Fri 5/22 EOD;
  monitor closed on Sun.
- **Crypto trend-follow (BTC)** — gap continues to narrow weekend-over-
  weekend (-6.2% Fri → -5.09% Sat → -4.67% Sun). Cross-up could fire
  within the next 6-10 trading days at current pace. Monitor on every
  03-midday routine until either trigger fires or pace reverses.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+
  per strategy.md v3 LM freeze.
- **AVGO earnings 2026-06-03**: 5 td out from Tue 5/26 cash open. Core
  hold posture intact; LM-paused Live-Phase #8 means no automatic
  exclusion zone for Core (and Core is frozen anyway).

## Recent Closed Positions (last 5)

(none — no closes across Live-Phase paper run + LM Day 1-4)

## LM Day 4 (Sunday) running tally

- Bull equity: **$100,901.97** (-$4.07 / -0.004% vs 5/22 EOD; +$140.25 /
  +0.139% vs 5/21 EOD baseline $100,761.72). Broker last_equity snap
  $100,861.21 represents the 5/23 EOD broker mark, so today's equity
  has ticked +$40.76 vs that watermark on overnight re-quote noise.
- SPY: $745.70 (Fri 5/22 close, no weekend tape); VIX 16.82.
- Day-4 alpha (carryover only): **-25.8 bp** vs SPY (no weekend SPY
  tape; identical to 5/22 EOD final alpha and 5/23 weekend carryover).
- LM cumulative (since 5/21 EOD baseline): **+$140.25 / +0.139%**
  equity; **-25.8 bp** alpha vs SPY (carryover).
- Per-sleeve LM cumulative: Core +$180.25 / Swing -$39.13 / DT $0 /
  Crypto $0 / Options $0.
- Top experiment LM Day 1-4: `core-buy-and-hold` +$180.25.
- Bottom experiment LM Day 1-4: `swing-quality-pullback` -$42.11 (NVDA
  only).
- Trades today: 0 entries, 0 closes. Win/Loss: 0/0.
- PDT count (5d): **0** (RESET from 2 on 5/23 broker rollover).
