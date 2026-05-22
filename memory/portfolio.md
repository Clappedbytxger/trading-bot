---
last_updated: 2026-05-22T19:36:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 2 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 04-pre-close (no trades; Daytrade force-flat no-op; LLY HWM organic walk-up #6)
total_value_usd: 100880.46
cash_usd: 34500.00
long_market_value_usd: 66380.46
day_pnl_usd_vs_last_equity: +123.89
day_pnl_pct_vs_last_equity: +0.1230
day_pnl_usd_vs_5_21_eod: +118.74
day_pnl_pct_vs_5_21_eod: +0.1178
prior_5_21_eod_usd: 100761.72
spy_close_5_22_intraday_pct: +0.4458
day_alpha_bp_vs_spy: -32.8
ytd_pnl_pct: 0.8763
benchmark_spx_ytd: 9.5101
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 746.03
alpha_vs_spx_ytd_pct: -8.6338
position_count_total: 10
position_count_core: 8
position_count_swing: 2
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.66
options_buying_power_usd: 67690.23
options_approved_level: 3
daytrade_count_5d: 2
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
vix_current_approx: 16.73
market_state: open
next_close: 2026-05-22T20:00:00Z
time_to_close_min: 24
---

# Portfolio — 04-pre-close 2026-05-22 (LM Day 2 of 30, 19:36Z / 15:36 ET, 24 min to close)

> **Phase note**: 04-pre-close PRE-CLOSE routine. 0 trades executed
> (Daytrade sleeve empty → force-flat no-op; Swing NVDA + RL stops
> verified live GTC, no time-stop triggers, no tighten-to-breakeven
> applicable; Crypto Friday-tighten no-op (empty); Options 7-DTE/IV-
> crush no-op (empty); AAPL `swing-short-rejection` EOD candle check
> = NO trigger (today's candle is UP +1.00% with fresh $311.40 52w-Hi
> extension); ARM PASS-already at 03-midday). **LLY HWM advanced
> ORGANICALLY 6th consecutive time** $1,069.11 → $1,070.3399 (stop
> $962.199 → $963.30591, +0.115% additional walk-up). Equity drifted
> -$101.89 from 03-midday on continued Core mark fade (GOOGL the main
> negative contributor: -$2.75 mark intraday); Bull still **+$118.74 /
> +0.118% vs 5/21 EOD** but day-alpha **-32.8 bp** (slightly improved
> from -34.7 bp as SPY gave back some of the midday +0.57% to close-near
> +0.45%). Swing sleeve UPL drifted -$35.60 → **-$41.17**; NVDA cushion
> compressed 3.47% → **3.05% (tightest since fill)**; RL recovered
> slightly. All 10 stops verified live GTC. Macro risk-off NOT active
> (SPY +0.45% / VIX 16.73). **AVGO + GOOGL cushion both <4% now**
> (3.43% / 3.93%) — flagged for 05-close-summary WhatsApp Robin notice.

## Sleeve summary

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $63,178.49 (live mark)|             8  |  +$1,000.49 |   +1.605%   | Frozen — 8/8 stops live GTC; LLY HWM organic walk-up #6 (stop $963.30591, +2.20% cumulative vs 5/21 EOD); AVGO + GOOGL cushion both <4% |
| Swing      |  $15,000             | $3,500.00 (cost)      |             2  |    -$41.17  |   -1.176%   | NVDA -2.01% (cushion 3.05% — tightest since fill) / RL -0.07% (cushion 6.94%); both stops live GTC |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     | Empty — force-flat no-op; PDT count 2/5 unchanged; 2 round-trips of headroom |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     | Empty — Friday-tighten no-op (no -8% trails to tighten); `crypto-weekend-momentum` Fri-close trigger NOT met (BTC 7d -3.02% vs +2% threshold) |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     | Empty — Polygon options-chain still 403 Forbidden (deferred 4th re-test); 7-DTE no-op |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty       | Avg Entry | Mark       | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341 |  $675.703 |  $685.680  |   $33,826.20 |  +$492.20  |  +1.477% |  33.53% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.55% |
| MSFT   | 11.521758 |  $404.973 |  $418.320  |    $4,819.78 |  +$153.78  |  +3.296% |   4.78% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.91% |
| GOOGL  | 12.047273 |  $387.308 |  $382.790  |    $4,611.58 |   -$54.42  |  -1.166% |   4.57% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 3.93% (biggest tighten today: 4.61% → 3.93%)** |
| META   |  7.767476 |  $600.710 |  $609.465  |    $4,734.00 |   +$68.00  |  +1.457% |   4.69% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 7.89% |
| AVGO   | 11.264102 |  $414.236 |  $412.270  |    $4,643.85 |   -$22.15  |  -0.475% |   4.60% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.43% (tightest in book; compressed 3.79% → 3.43%)** |
| V      | 10.256781 |  $325.053 |  $329.285  |    $3,377.40 |   +$43.40  |  +1.302% |   3.35% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.39% |
| BRK.B  |  6.883950 |  $484.315 |  $485.675  |    $3,343.36 |    +$9.36  |  +0.281% |   3.31% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 9.32% |
| LLY    |  3.341161 |  $997.857 | $1,067.130 |    $3,565.45 |  +$231.45  |  +6.942% (best UPL) |   3.53% | trail 10% / 3 sh GTC / **HWM ↑ organic #6 $1,070.3399** / **stop $963.30591** ↑ +0.115% vs 16:42Z / cushion 9.73% |

**Notable Core changes since 03-midday (16:42Z):**
- **LLY HWM organic walk-up #6** $1,069.11 → $1,070.3399 (+0.115%) with
  stop bumped $962.199 → $963.30591 (+0.115%). **Cumulative LLY stop walk
  vs 5/21 EOD $942.5655**: +$20.74 / +2.20%. 6 consecutive HWM advances
  over 2 trading days; **biggest single-name Core protection drift in the
  entire Live-Phase + LM record**.
- **AVGO cushion compressed further** 3.79% → **3.43%** as mark $413.80 →
  $412.27 (-0.37% intraday). Still above the 3% routine-spec watch
  threshold but now tightest in book. AVGO earnings 2026-06-03 = **7
  trading days out** (5/26, 5/27, 5/28, 5/29, 6/1, 6/2, 6/3; 5/25 closed
  for Memorial Day). Still outside Live-Phase #8 3-day exclusion zone.
- **GOOGL cushion compressed sharply** 4.61% → **3.93%** as mark $385.54 →
  $382.79 (-0.71% intraday). **Biggest single-name cushion compress today**.
  Now 2nd-tightest in book. No thesis-break catalyst found; routine drift.
- MSFT/META/V/BRK.B: small drifts ±0.10-0.30%; no flags.
- VOO -0.17% drift mirrors broad-market late-afternoon fade.
- **All 8 trail orders verified `OrderStatus.NEW` GTC** in 19:35Z order list.

**Cushion rank (live 19:35Z, tightest first):**
1. AVGO **3.43%** (tightest, compressed further from 3.79%)
2. GOOGL **3.93%** (biggest tighten today: 4.61% → 3.93%)
3. MSFT 6.91%
4. META 7.89%
5. V 8.39%
6. BRK.B 9.32%
7. VOO 9.55%
8. LLY 9.73% (largest; benefited from organic HWM walk-up #6)

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken this
routine.** All stops remain GTC and intact. AVGO + GOOGL cushion compress
flagged for the 05-close-summary WhatsApp.

Total Core committed: $63,178.49 (62.63% of equity)

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Mark    | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held | Time stop | Strategy slug             |
|--------|----------:|----------:|--------:|-------------:|--------:|--------:|------:|--------:|----------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 | $215.540|    $1,959.80 | -$40.20 | -2.010% | $208.96 GTC | **3.05%** | 1 | 2026-06-02 (7d) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 | $376.785|    $1,499.03 |  -$0.97 | -0.065% | $350.64 GTC | 6.94% | 1 | 2026-06-05 (10d) | `swing-earnings-drift`   |

**NVDA pre-close status (`swing-quality-pullback`)**: UPL drifted -1.585%
→ -2.010% (-$8.49 intraday) on mark $216.475 → $215.5401. Distance to stop
$208.96 compressed to **3.05%** — tightest since fill but still above the
playbook -5% trigger. Day 1 of 7-day time-stop (today is fill day; first
time-stop check on 6/2 close). Target $235 unchanged. **No action**; UPL
within drift band, cushion above trigger. Tighten-to-breakeven rule does
not apply (negative UPL).

**RL pre-close status (`swing-earnings-drift`)**: UPL recovered slightly
into the close -0.260% → -0.065% (+$2.93 intraday) on mark $376.05 →
$376.785. Distance to stop $350.64 = 6.94% (slight improve from 6.76%).
Day 1 of 10-day time-stop. Target $414.73 unchanged. **No action**.

**AAPL midday-deferred check (`swing-short-rejection`)**:
- Today's daily candle (yfinance ≈24min before final close): O $306.06 / H
  **$311.40 (new 52w-Hi +2.10% above prior $304.99)** / L $305.85 / C $309.13.
- Daily print = **UP candle** (close +1.00% above open). NOT a rejection.
- **Decision: PASS — no AAPL short entry today**. Re-watch on Tue
  01-pre-market (Mon 5/25 = Memorial Day, market closed). Setup is more
  extended (RSI now likely ≥80) — eventual rejection, when it prints, gives
  a tighter stop and better R-multiple.

**ARM midday-deferred check (`swing-momentum-breakout`)**:
- Today: O $289.06 / H $315.00 / L $288.21 / C $304.66 (3.28% fade off high).
- Decision: re-screen on Tue 5/26. Re-arm BUY only if ARM closes back below
  $290 (clean retest); $290-$310 = WATCH; >$310 = no-chase per 01-pre-market.

## Daytrade / Scalp sleeve (intraday only — flat by 20:30Z, PDT count 2/5)

Empty (0 / 5). $10k budget intact. **PDT count 2 / 5d** — UNCHANGED from
02-market-open watermark. **Force-flat at 04-pre-close**: VERIFIED 0
positions. No-op. No roll-to-swing requests pending in `inbox.md`.

- No ORB/VWAP/scalp/gap-go/gap-fade/news-catalyst entries triggered today
  per 03-midday determination. No EOD adjustments needed.

## Crypto sleeve (24/7)

Empty (0 / 4). $5k budget intact. **Friday-tighten no-op** (no -8% trails
to tighten; sleeve empty). End-of-Friday yfinance snapshot:

| Coin | Last | 24h | 7d | 50/200 DMA |
|------|-----:|----:|---:|------------|
| BTC-USD  | $75,775  | -2.27% | -3.02% | 50<200 ↓ (gap widened -4.2% → -6.2%) |
| ETH-USD  | $2,068.91| -2.93% | -5.09% | 50<200 ↓ |
| SOL-USD  | $84.45   | -3.11% | -2.41% | 50<200 ↓ |
| AVAX-USD | $9.20    | -2.56% | -0.98% | 50<200 ↓ |
| LINK-USD | $9.42    | -3.25% | -3.04% | 50<200 ↓ |

- **`crypto-weekend-momentum` Friday-close trigger (final eval at
  05-close-summary 21:00Z)**: BTC 7d **-3.02%** vs +2% threshold — would
  need a +5.18% rally in next ~80 min to qualify. Effectively impossible.
  **NO weekend-momentum entry expected at 05-close-summary.**
- `crypto-mean-reversion`: 0 (no -10%/24h flush — deepest is LINK -3.25%).
  Universe bleeding more uniformly than at midday; weekend `03-midday`
  Sat+Sun routines should re-check if BTC/ETH gap down a further 5-7%.
- `crypto-trend-follow`: 0 signals (universe-wide 50<200 downtrend widening).
- **Plan**: NO crypto entries at 04-pre-close. Final Fri check at
  05-close-summary; weekend 03-midday Sat+Sun next (IF Robin extended cron
  per inbox Q1 C).

## Options sleeve (Level 3 enabled)

Empty (0 / 6 contracts). $5k premium budget intact. Options BP **$67,690.23**
/ Level 3 ✓. Polygon options-chain status unchanged (still 403 Forbidden
last test 16:40Z); 4th re-test deferred — NVDA conviction already routed
through Swing equity.

- 7 DTE rule: no positions, no-op.
- IV-crush check: no positions, no-op.
- Protective-put staleness: none open.

**Decision: NO Options actions today**, per the 03-midday determination.

## Today's trades

(none at 04-pre-close — see 02-market-open section for today's 2 Swing fills)

**Organic broker events** (no Bull action, recorded for audit):
- **LLY trail HWM advanced ORGANICALLY 6th consecutive time** $1,069.11 →
  $1,070.3399 (+0.115%) since 03-midday. **Stop bumped $962.199 →
  $963.30591 (+0.115%)**. Cumulative LLY trail walk over 2 LM days:
  $942.5655 → $963.30591 = **+$20.74 / +2.20%**. LLY UPL +6.942% (mark
  $1,067.13).

## Pending (not yet opened / re-evaluated)

- **AAPL** — short-rejection candle did NOT print today (UP candle +1.00%
  with fresh $311.40 52w-Hi extension). Re-watch on Tue 5/26 01-pre-market.
- **ARM** — re-arm `swing-momentum-breakout` only if ARM closes back below
  $290 (clean retest); above $290 + below $310 stays WATCH on Tue 5/26.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain (4th re-test
  deferred). NVDA conviction running via equity Swing entry.
- **Crypto weekend-momentum** — trigger NOT met (BTC 7d -3.02%); final eval
  at 05-close-summary 21:00Z but ≥98% probability NO entry.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no closes across Live-Phase paper run + LM Day 1 + LM Day 2 full)
