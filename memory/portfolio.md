---
last_updated: 2026-05-22T13:38:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 2 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 02-market-open (2 Swing entries placed: NVDA + RL; Core untouched)
total_value_usd: 101208.22
cash_usd: 34500.00
long_market_value_usd: 66708.22
day_pnl_usd_vs_last_equity: +451.65
day_pnl_pct_vs_last_equity: +0.4483
day_pnl_usd_vs_5_21_eod: +446.50
day_pnl_pct_vs_5_21_eod: +0.4432
prior_5_21_eod_usd: 100761.72
spy_open_5_22_pct: +0.6000
day_alpha_bp_vs_spy: -15.2
ytd_pnl_pct: 1.2050
benchmark_spx_ytd: 9.6800
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 747.23
alpha_vs_spx_ytd_pct: -8.4750
position_count_total: 10
position_count_core: 8
position_count_swing: 2
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.66
options_buying_power_usd: 67854.10
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
macro_risk_off_active: false
vix_current_approx: 16
market_state: open
next_close: 2026-05-22T20:00:00Z
---

# Portfolio — 02-market-open 2026-05-22 (LM Day 2 of 30, 13:38Z / 09:38 ET)

> **Phase note**: 02-market-open executed cleanly. The 13:00Z 01-pre-market fired
> on schedule today (Step 1a back-fire NOT needed). Two Swing entries placed at
> open per yesterday's plan: NVDA $2k (`swing-quality-pullback`) + RL $1.5k
> (`swing-earnings-drift`). Both stops live GTC. Core untouched, all 8 trail
> stops verified. LLY trail HWM advanced ORGANICALLY at the open (no Bull
> action) from $1,047.295 → ~$1,063.67 → stop $957.303. **First non-zero
> sleeve count outside Core in LM window**: Swing 2/8. Day-alpha pre-open
> snap -15.2 bp (Bull +0.45% vs SPY +0.60%).

## Sleeve summary

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $63,218.04 (live mark)|             8  |  +$1,217.05 |   +1.963%   | Frozen — 8/8 stops live GTC; LLY HWM +1.55% organically vs 5/21 EOD |
| Swing      |  $15,000             | $3,500.00 (cost)      |             2  |    -$9.76   |   -0.279%   | NVDA + RL filled; both stops live GTC |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     | Empty — ORB watches active (5-min ORB resolves ~13:35Z+) |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     | Empty — no signal pre-open |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     | Empty — Polygon options chain still gated |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty       | Avg Entry | Mark       | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341 |  $675.703 |  $687.56   |   $33,918.94 |  +$584.94  |  +1.755% |  33.51% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.80% |
| MSFT   | 11.521758 |  $404.973 |  $423.50   |    $4,879.46 |  +$213.46  |  +4.575% |   4.82% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 8.04% |
| GOOGL  | 12.047273 |  $387.308 |  $387.08   |    $4,663.26 |   -$2.74   |  -0.059% |   4.61% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 5.00% |
| META   |  7.767476 |  $600.710 |  $614.31   |    $4,771.64 |  +$105.64  |  +2.264% |   4.71% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 8.62% |
| AVGO   | 11.264102 |  $414.236 |  $418.53   |    $4,714.36 |   +$48.36  |  +1.037% |   4.66% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / cushion 4.87% |
| V      | 10.256781 |  $325.053 |  $331.85   |    $3,403.71 |   +$69.71  |  +2.091% |   3.36% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 9.10% |
| BRK.B  |  6.883950 |  $484.315 |  $481.60   |    $3,315.31 |   -$18.69  |  -0.561% |   3.28% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.55% |
| LLY    |  3.341161 |  $997.857 | $1,062.91  |    $3,551.35 |  +$217.35  |  +6.519% (best UPL) |   3.51% | trail 10% / 3 sh GTC / **HWM ~$1,063.67 ↑ organic at open** / **stop $957.303** ↑ vs $942.5655 EOD 5/21 / cushion 9.94% |

**Notable Core changes since 5/21 EOD:**
- **LLY HWM advanced ORGANICALLY at the cash open** from $1,047.295 → ~$1,063.67
  (Alpaca trail recomputes server-side as price prints). **Stop bumped
  $942.5655 → $957.303 (+1.55%)** — biggest single-day organic trail-walk in
  LM so far. Confirms "frozen Core still produces protection drift on names
  printing HWMs" lesson; LLY now on its 4th consecutive HWM advance.
- **AVGO cushion tightened** 3.90% → **4.87%** (mark $414.26 → $418.53,
  +1.04% intraday rebound). Cushion improved despite no HWM change → AVGO
  is the only Core name still negative was reversed today.
- **GOOGL** now tightest cushion at 5.00% (mark $387.08, off slightly from
  5/21 EOD $387.66; flat-to-slightly-red on the day).
- **All 8 trail orders verified `OrderStatus.NEW` GTC** in post-fill order list.

**Cushion rank (live 13:38Z, tightest first):**
1. AVGO 4.87% (recovered)
2. GOOGL 5.00% (~unchanged)
3. MSFT 8.04%
4. BRK.B 8.55%
5. META 8.62%
6. V 9.10%
7. VOO 9.80%
8. LLY 9.94% (largest; benefited from organic HWM walk-up)

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken this
routine.** All stops remain GTC and intact.

Total Core committed: $63,218.04 (62.46% of equity)

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Mark    | Market Value | UPL$    | UPL%    | Stop  | Strategy slug             |
|--------|----------:|----------:|--------:|-------------:|--------:|--------:|------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 | $219.80 |    $1,998.53 | -$1.47  | -0.073% | $208.96 GTC (9 sh; 0.0925 sh uncovered slice) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 | $374.945|    $1,491.70 | -$8.30  | -0.553% | $350.64 GTC (3 sh; 0.978 sh uncovered slice; ~$367 unprotected — accepted per fractional handling)  | `swing-earnings-drift`   |

**NVDA thesis (`swing-quality-pullback`)**: Q1 FY27 rev $81.6B +85% YoY beat
$78.8B; non-GAAP EPS $1.87 beat $1.75-1.77; **Q2 guide $91B vs Street
$86-87B** (huge raise, ex-China). Hyperscaler rev $37.9B +115% YoY. Multiple
PT raises within 24h (HSBC $295→$325, MS $260→$285, Jefferies $275→$300,
Baird $300→$500, BofA $320→$350, GS $250→$285). Pullback -6.88% from 52w-Hi
$236.54. Day-1 -1.77% reaction = "priced-in," not thesis-break. Target:
+7% (~$235) OR 52w-Hi retest, whichever first. Time-stop 7 trading days.

**RL thesis (`swing-earnings-drift`)**: Day-1 +10.26% (5/21) on Q4 FY26 EPS
beat + strong full-price selling. Entered Day-2 post-print at $377.03 (5/22
open) above 95% trigger threshold $356.16. Target: +10% OR 10 trading days.
Stop -7% (wider per earnings volatility playbook).

**Other Swing candidates from plan — status:**
- **ARM (`swing-momentum-breakout`)**: WATCH; needs ORB-style 5-min consolidation
  > $290 + opening-range break confirmation. Pre-mkt $298.23, live ~$294.90
  at 13:37Z (fell from pre-mkt → modest fade). Re-evaluate at 03-midday.
- **AAPL (`swing-short-rejection`)**: WATCH; live $308.43 (vs 5/21 close
  $304.99 → +1.13%, made a new 52w-Hi at open). NO rejection candle YET.
  Re-evaluate end-of-day (need close < open AT 52w-Hi).
- **INTU**: SKIPPED (falling-knife AI-disruption narrative; thesis-risk filter).

## Daytrade / Scalp sleeve (intraday only — flat by 20:30Z, PDT count 2/5)

Empty (0 / 5). $10k budget intact. **PDT count 2 / 5d** — increased from 0 → 2
post-Swing-fills (Alpaca pre-counted NVDA + RL as eligible day-trades since
both have same-day open + active stop; PDT-watermark observation, not yet at
4-trade threshold). Budget for ORB scalps this session: realistically 1 ORB
to stay clear of PDT flip.

- **ORB WATCH list** (5-min ORB resolving ~13:35Z+): SPY, QQQ, NVDA, TSLA,
  AAPL, AMD. Execution deferred to 03-midday for any ORB break that fires
  AFTER 13:35Z (per routine spec). Max 1 ORB scalp this session.
- **VWAP-pullback WATCH**: defer to 03-midday (needs ≥30min above VWAP first).
- **gap-go WATCH**: TTWO, WDAY (RL already taken via Swing path — preferred).
  Re-check pre-mkt gap magnitudes for TTWO/WDAY at 03-midday.
- **scalp-tape**: defer to post-13:45Z. Max 1 round-trip.

## Crypto sleeve (24/7)

Empty (0 / 4). $5k budget intact. All 5 universe coins still 50<200 DMA
downtrend (no `crypto-trend-follow` cross-up). `crypto-weekend-momentum`
trigger checks at 05-close-summary Fri 21:00Z — BTC 7d -2.08% → would need
~+4% rally today. Re-check at 03-midday.

## Options sleeve (Level 3 enabled)

Empty (0 / 6 contracts). $5k premium budget intact. Options BP **$67,854.10**
/ Level 3 ✓. **`options-vertical-bull-call-spread` NVDA candidate not
executed** — Polygon options-chain endpoint returned None on IV/chain reads
this morning (`get_iv_rank` empty); Options-Starter add-on appears still
gated on Polygon tier. NVDA conviction routed through equity (`swing-quality-
pullback` $2k entry, executed above) as the fallback plan.
- SKIP `options-protective-put` (no FOMC/CPI today).
- SKIP `options-earnings-strangle` (no qualifying names; IV data gated).
- DEFER `options-long-call-momentum` (ARM extended, NVDA not a breakout).

## Today's trades

- **13:37:23Z** — BUY RL 3.978463 sh @ $377.03 (notional $1,500) market /
  filled. Stop sell 3 sh @ $350.64 GTC placed. Strategy: `swing-earnings-drift`.
  Order IDs: buy `3f64d479-d578-4bc4-b96a-86679bc97c63`, stop
  `9e45b1e8-cf59-408d-a702-9691f5dc3620`.
- **13:37:24Z** — BUY NVDA 9.092513 sh @ $219.961202 (notional $1,999.83 of
  $2,000) market / filled. Stop sell 9 sh @ $208.96 GTC placed. Strategy:
  `swing-quality-pullback`. Order IDs: buy
  `b9755836-53af-4198-8df3-5511e453af3e`, stop
  `ffb5e5a9-50fb-4e39-abef-849d72b8f323`.

**Organic broker events** (no Bull action, recorded for audit):
- **LLY trail HWM advanced ORGANICALLY at the open** from $1,047.295 →
  ~$1,063.67 (intraday print high used by Alpaca trail). **Stop bumped
  $942.5655 → $957.303 (+1.55%)** — single biggest day-on-day organic
  trail-walk so far this LM. LLY UPL now +6.519%.

## Pending (not yet opened)

- **ARM** — WATCH for 5-min consolidation > $290 + ORB-style break in
  13:30-14:00Z window. Sized $1.5k. Re-evaluate at 03-midday.
- **AAPL short** — WATCH for daily close < open AT 52w-Hi; check at 04-pre-close.
  Hard-to-borrow status TBD.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain. Equity entry
  taken instead; will not re-attempt today.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no closes in entire Live-Phase paper run + LM Day 1 + first
half-hour of LM Day 2)
