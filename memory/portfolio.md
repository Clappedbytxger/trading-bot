---
last_updated: 2026-05-22T20:16:13Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 2 of 30 EOD)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 05-close-summary (0 trades; EOD reconcile, ledger refresh, German WhatsApp)
total_value_usd: 100906.04
cash_usd: 34500.00
long_market_value_usd: 66406.04
day_pnl_usd_vs_last_equity: +149.47
day_pnl_pct_vs_last_equity: +0.1483
day_pnl_usd_vs_5_21_eod: +144.32
day_pnl_pct_vs_5_21_eod: +0.1432
prior_5_21_eod_usd: 100761.72
spy_close_5_22_usd: 745.70
spy_close_5_21_usd: 742.72
spy_day_pct_5_22: +0.4012
day_alpha_bp_vs_spy: -25.8
lm_cum_pnl_usd_since_5_21_eod: +144.32
lm_cum_pnl_pct_since_5_21_eod: +0.1432
lm_cum_alpha_bp_vs_spy: -25.8
ytd_pnl_pct: 0.8950
benchmark_spx_ytd: 9.4636
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 745.70
alpha_vs_spx_ytd_pct: -8.5686
position_count_total: 10
position_count_core: 8
position_count_swing: 2
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.66
options_buying_power_usd: 67697.39
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
vix_close_5_22: 16.82
market_state: closed
next_open: 2026-05-26T13:30:00Z (Memorial Day Mon 5/25 = closed)
---

# Portfolio — 05-close-summary 2026-05-22 EOD (LM Day 2 of 30 closed)

> **Phase note**: 05-close-summary EOD reconcile after US cash session
> close 20:00Z. Clock verified `is_open=False`, next_open Tue 2026-05-26
> 13:30Z (Mon 5/25 = Memorial Day, market closed). 0 trades this routine.
> **Day-2 final: Bull +$144.32 / +0.143% vs 5/21 EOD; SPY +0.401%; Day-2
> alpha -25.8 bp** (slight further improvement from 04-pre-close's -32.8
> bp as Core ticked up modestly into the close while SPY held). LLY HWM
> walk-up #6 from 04-pre-close held — no walk-up #7 today (LLY mark
> retraced $1,070.34 → $1,065.50, 0.45% off the HWM but still within trail
> band). **AVGO cushion recovered** 3.43% → 3.78% on a mark uptick
> $412.27 → $413.75. **GOOGL cushion recovered** 3.93% → 4.08% on mark
> $382.79 → $383.40. **NVDA cushion compressed further** 3.05% → **2.81%**
> (mark $215.54 → $215.01, -$0.53 in the close; tightest since fill).
> All 10 stops verified live `OrderStatus.NEW` GTC post-close. Macro
> risk-off NOT active (SPY +0.40% / VIX 16.82). PDT count UNCHANGED at
> 2/5d. **LM Day 2 closing baseline: Bull equity $100,906.04, LM-cum
> P&L +$144.32 vs Day-1 close $100,761.72.**

## Sleeve summary (EOD)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Day Δ$    | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|----------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,951.01 (live mark)|             8  |   +$951.01  |   +1.534%   | +$189.29  | Frozen — 8/8 stops live GTC; LLY HWM #6 held (no walk-up #7 today); AVGO + GOOGL cushion recovered to 3.78% / 4.08% |
| Swing      |  $15,000             | $3,455.02 (live mark) |             2  |    -$44.98  |   -1.285%   | -$44.98   | NVDA -2.25% (cushion **2.81% — tightest since fill**) / RL +0.003% (cushion 7.00%); both stops live GTC |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0     | Empty all day; PDT count 2/5 UNCHANGED from 02-market-open watermark; 2 round-trips of headroom into next session |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0     | Empty — `crypto-weekend-momentum` Fri-close trigger NOT met (BTC 7d -3.02% << +2% threshold; final EOD check confirmed no entry); all 5 in 50<200 downtrend |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     |    $0     | Empty — Polygon options-chain still 403 Forbidden (4th re-test deferred); NVDA conviction routed via equity sleeve |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     |    —      | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty       | Avg Entry | Mark       | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341 |  $675.703 |  $685.750  |   $33,829.65 |  +$495.65  |  +1.487% |  33.53% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.56% |
| MSFT   | 11.521758 |  $404.973 |  $419.020  |    $4,827.85 |  +$161.85  |  +3.469% |   4.78% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.06% |
| GOOGL  | 12.047273 |  $387.308 |  $383.400  |    $4,618.92 |   -$47.08  |  -1.009% |   4.58% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 4.08% (recovered 3.93% → 4.08% into the close)** |
| META   |  7.767476 |  $600.710 |  $609.480  |    $4,734.12 |   +$68.12  |  +1.460% |   4.69% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 7.90% |
| AVGO   | 11.264102 |  $414.236 |  $413.750  |    $4,660.52 |    -$5.48  |  -0.117% |   4.62% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.78% (recovered 3.43% → 3.78% into the close)** |
| V      | 10.256781 |  $325.053 |  $329.000  |    $3,374.48 |   +$40.48  |  +1.214% |   3.34% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.31% |
| BRK.B  |  6.883950 |  $484.315 |  $485.980  |    $3,345.46 |   +$11.46  |  +0.344% |   3.32% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 9.37% |
| LLY    |  3.341161 |  $997.857 |  $1,065.50 |    $3,560.01 |  +$226.01  |  +6.779% (best UPL) |   3.53% | trail 10% / 3 sh GTC / **HWM $1,070.3399 held (no walk-up #7 today)** / stop $963.30591 / cushion 9.59% |

**Notable Core changes since 04-pre-close (19:36Z):**
- **LLY HWM held flat at $1,070.3399** — no organic walk-up #7 today. Mark
  retraced from $1,067.13 → $1,065.50 (-0.15% into the close). 6 organic
  walk-ups over LM Day 1+2 (cumulative +$20.74 / +2.20% on stop), but the
  Day 2 close did not extend HWM. Trail stop $963.30591 unchanged.
- **AVGO mark recovered** $412.27 → $413.75 (+0.36% into the close);
  cushion 3.43% → **3.78%** (improvement, no longer tightest in book).
  AVGO still the 3rd-tightest Core cushion. AVGO earnings 2026-06-03 = 7
  trading days out (5/26, 5/27, 5/28, 5/29, 6/1, 6/2, 6/3 — Mon 5/25 closed
  for Memorial Day); still outside Live-Phase #8 3-day exclusion zone.
- **GOOGL mark recovered** $382.79 → $383.40 (+0.16% into the close);
  cushion 3.93% → **4.08%** (recovered). Still 2nd-tightest in book.
- **MSFT mark up** $418.32 → $419.02 (+0.17%); cushion 6.91% → 7.06%.
- **V mark down** $329.285 → $329.00 (-0.09%); cushion 8.39% → 8.31%.
- **META mark up** $609.465 → $609.48 (+0.002%); cushion ~7.89% → 7.90%.
- **BRK.B mark up** $485.675 → $485.98 (+0.06%); cushion 9.32% → 9.37%.
- **VOO mark up** $685.68 → $685.75 (+0.01%); cushion 9.55% → 9.56%.
- **All 8 trail orders verified `OrderStatus.NEW` GTC** in 20:16Z order
  list (post-close).

**Cushion rank (live 20:16Z EOD, tightest first):**
1. AVGO **3.78%** (recovered from 3.43% at 04-pre-close)
2. GOOGL **4.08%** (recovered from 3.93%)
3. MSFT 7.06% (up from 6.91%)
4. META 7.90%
5. V 8.31%
6. BRK.B 9.37%
7. VOO 9.56%
8. LLY 9.59% (slight compress from 9.73% as mark eased off the HWM)

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken.**
All stops remain GTC and intact post-close.

Total Core committed: $62,951.01 (62.39% of equity). Core UPL day Δ
**+$189.29** ($761.72 → $951.01); the only Core name not green vs entry
post-close: AVGO -0.117% and GOOGL -1.009%.

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Mark    | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held | Time stop | Strategy slug             |
|--------|----------:|----------:|--------:|-------------:|--------:|--------:|------:|--------:|----------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 | $215.01 |    $1,954.98 | -$45.02 | -2.251% | $208.96 GTC | **2.81%** | 1 | 2026-06-02 (7d) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 | $377.04 |    $1,500.04 |  +$0.04 | +0.003% | $350.64 GTC | 7.00% | 1 | 2026-06-05 (10d) | `swing-earnings-drift`   |

**NVDA EOD status (`swing-quality-pullback`)**: UPL compressed further
-2.010% → -2.251% (-$4.82 into the close) on mark $215.54 → $215.01.
**Cushion 3.05% → 2.81% (tightest since fill, by a wide margin)**. Still
above the playbook -5% stop trigger; first time-stop check on 6/2 close.
**Watch on Tue 5/26 open: if cushion compresses to <2% (mark ≈ $213.22),
tighten posture** — consider half-out at market to lock the remaining
1-1.5% cushion against a gap-down through the stop. Day-2 alpha
attribution: NVDA contributed -$45.02 (biggest negative single-name
contributor). No tighten-to-breakeven (rule requires +5%+ UPL). NO action.

**RL EOD status (`swing-earnings-drift`)**: UPL improved slightly into the
close -0.065% → +0.003% (+$1.01 intraday last 24 min). Mark $376.785 →
$377.04 (back to entry $377.03 within $0.01). Cushion 6.94% → **7.00%**.
First time-stop check on 6/5 close. Day-2 alpha attribution: RL +$0.04
(net-neutral). PEAD thesis intact — Day-2 typically a digestion day before
Day 3-5 drift. NO action.

**AAPL final EOD candle confirm (`swing-short-rejection`)**:
- Daily candle: O $306.06 / H $311.40 (new 52w-Hi) / L $305.85 / C $309.13.
- Daily print = **UP candle +1.00%** (close > open). NOT a rejection.
- Decision: **PASS — no AAPL short today**. Re-watch on Tue 5/26
  01-pre-market (Mon 5/25 = Memorial Day, market closed).

**ARM final EOD (`swing-momentum-breakout`)**:
- Daily candle: O $289.06 / H $315.00 / L $288.21 / C $304.66 (3.28% fade
  off the high; still above 20-day Hi $298.23 from 01-pre-market screen).
- Decision: **re-screen on Tue 5/26**. Re-arm BUY only if ARM closes back
  below $290 (clean retest); $290-$310 = WATCH; >$310 = no-chase.

## Daytrade / Scalp sleeve (intraday only — flat by 20:30Z, PDT count 2/5)

Empty (0 / 5). $10k budget intact. **PDT count 2/5d UNCHANGED from
02-market-open watermark** (no Bull-side intraday round-trip occurred
today). 2 round-trips of headroom before 4-trip PDT flip into next session.

- No ORB/VWAP/scalp/gap-go/gap-fade/news-catalyst entries triggered today
  per 03-midday + 04-pre-close determinations. EOD: still 0 fills, 0 close.

## Crypto sleeve (24/7, $5k budget intact)

Empty (0 / 4). **`crypto-weekend-momentum` final Fri-close trigger check**:

| Coin | EOD 5/22 (yf) | 24h | 7d ref to 5/15 | 50/200 DMA |
|------|--------------:|----:|---------------:|------------|
| BTC-USD  | $75,887.59 | -2.13% | -3.02% (effectively unchanged from 04-pre-close -3.02%) | 50<200 ↓ (gap -6.2%) |
| ETH-USD  | $2,071.63  | -2.81% | -5.09% | 50<200 ↓ |
| SOL-USD  | $84.86     | -2.64% | -2.41% | 50<200 ↓ |
| AVAX-USD | $9.23      | -2.24% | -0.98% | 50<200 ↓ |
| LINK-USD | $9.50      | -2.47% | -3.04% | 50<200 ↓ |

- **`crypto-weekend-momentum` Friday-close decision = NO ENTRY** (BTC 7d
  -3.02% vs +2% threshold; trigger NOT met). Confirms 04-pre-close call.
- `crypto-mean-reversion`: 0 (no -10%/24h flush; deepest is ETH -2.81%).
  Universe-wide -2 to -3% bleed continued through the close — flagged for
  weekend `03-midday` Sat+Sun routines (IF Robin extended cron per inbox
  Q1 C). If BTC/ETH gap down a further 5-7% over the weekend, the
  `crypto-mean-reversion` trigger may fire on Sat/Sun.
- `crypto-trend-follow`: 0 signals (universe-wide 50<200 downtrend; BTC
  50DMA gap widened -6.2%; no imminent cross-up).
- **NO crypto entries at 05-close-summary.**

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. Options BP **$67,697.39**
/ Level 3 ✓. Polygon options-chain still 403 Forbidden last test (16:40Z);
4th re-test deferred. NVDA conviction already running via Swing equity.

- 7 DTE rule: no positions, no-op.
- IV-crush check: no positions, no-op.
- Protective-put staleness: none open.

**Decision: NO Options actions today.**

## Today's trades (EOD reconcile)

(none at 05-close-summary — see 02-market-open section for today's 2 Swing fills:
NVDA $2k notional `swing-quality-pullback` and RL $1.5k notional
`swing-earnings-drift`.)

**Organic broker events (this routine, no Bull action)**:
- LLY trail HWM held at $1,070.3399 (no walk-up #7 today; mark closed at
  $1,065.50, -0.45% off the HWM). Stop $963.30591 unchanged.

## Pending (not yet opened / re-evaluated)

- **AAPL** — short-rejection EOD candle confirmed UP (+1.00% at $309.13
  with fresh $311.40 52w-Hi). Re-watch on Tue 5/26 01-pre-market.
- **ARM** — re-arm `swing-momentum-breakout` only if ARM closes back below
  $290 (clean retest); above $290 + below $310 stays WATCH on Tue 5/26.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain (4th re-test
  deferred). NVDA conviction running via equity Swing entry.
- **Crypto weekend-momentum** — confirmed NO ENTRY at EOD (BTC 7d -3.02%).
- **Crypto mean-reversion** — pre-trigger watch over the long weekend (5/23
  Sat + 5/24 Sun + 5/25 Memorial Day closed). If BTC/ETH gap down a
  further 5-7% on no fundamental break, trigger could fire on weekend
  `03-midday` (if cron extension applied).
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze.

## Recent Closed Positions (last 5)

(none — no closes across Live-Phase paper run + LM Day 1 + LM Day 2)

## LM Day 2 closing baseline

- Bull equity: **$100,906.04** (+$144.32 / +0.143% vs Day-1 close $100,761.72).
- SPY: $745.70 (+0.401% DoD); VIX 16.82.
- Day-2 alpha: **-25.8 bp** (Bull +0.143% vs SPY +0.401%).
- LM cumulative (since 5/21 EOD baseline): **+$144.32 / +0.143%** equity;
  **-25.8 bp** alpha vs SPY.
- Per-sleeve LM cumulative: Core +$189.29 / Swing -$44.98 / DT $0 /
  Crypto $0 / Options $0.
- Top experiment LM Day 2: `core-buy-and-hold` +$189.29.
- Bottom experiment LM Day 2: `swing-quality-pullback` -$45.02 (NVDA only).
- Trades today: 2 entries (NVDA, RL), 0 closes. Win/Loss: 0/0 (both open).
- PDT count (5d): 2 (unchanged from 02-market-open watermark).
