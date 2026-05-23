---
last_updated: 2026-05-23T16:36:23Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 3 of 30 — Saturday weekend-crypto-cycle)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 03-midday (weekend-crypto-cycle; market closed; 0 trades; crypto scan only)
total_value_usd: 100901.97
cash_usd: 34500.00
long_market_value_usd: 66401.96
day_pnl_usd_vs_5_22_eod: -4.07
day_pnl_pct_vs_5_22_eod: -0.0040
day_pnl_usd_vs_5_21_eod: +140.25
day_pnl_pct_vs_5_21_eod: +0.1392
prior_5_22_eod_usd: 100906.04
prior_5_21_eod_usd: 100761.72
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
options_buying_power_usd: 0 (weekend N/A; Fri 5/22 EOD was $67,697.39)
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
market_state: closed (Saturday — weekend; Mon 5/25 Memorial Day closed)
next_open: 2026-05-26T13:30:00Z
---

# Portfolio — 03-midday 2026-05-23 (LM Day 3, Saturday weekend-crypto-cycle)

> **Phase note**: Sat 2026-05-23 03-midday weekend cycle. `clock.is_open
> = False` confirmed; equities don't trade. 0 trades book-wide.
> Equity drifted **$100,906.04 → $100,901.97 (-$4.07)** on Alpaca's
> weekend quote-stream refresh noise (broker re-quotes from cached
> pricing service; equities have no live tape). **LM Day 3 routine #1
> of 1** (only 03-midday fires on weekends per cron `30 17 * * 1-7`).
> Crypto sleeve **scanned** — all 5 universe names still 50<200 DOWN;
> no -10%/24h flush; weekend-momentum monitor not needed (no Fri-close
> fill). **0 crypto entries.** Macro risk-off N/A (no weekend tape).
> Mon 2026-05-25 = Memorial Day (US cash session closed). Next equity
> touchpoint: Tue 2026-05-26 01-pre-market at 13:00Z.

## Sleeve summary (Sat 5/23 16:36Z weekend snapshot)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs 5/22 EOD | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|--------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,941.97 (Sat mark) |             8  |   +$941.97  |   +1.519%   | -$9.04        | Frozen — 8/8 stops live GTC; cushion drift ±12 bp on weekend mark noise; GOOGL now 2nd-tightest at 3.97% behind AVGO 3.87% |
| Swing      |  $15,000             | $3,460.87 (Sat mark)  |             2  |    -$39.13  |   -1.118%   | +$5.85        | NVDA -1.917% (cushion **2.96%** ↑ from 2.81%) / RL +0.199% (cushion 7.19% ↑ from 7.00%); both stops live GTC |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — weekend N/A; PDT count 2/5 UNCHANGED; sleeve untouched since Fri |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty — Sat scan: 0/5 50/200 cross-up; 0/5 -10%/24h flush; weekend-momentum no-monitor (no Fri fill); **0 entries** |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     |    $0         | Empty — Polygon options-chain still gated; 4th re-test deferred to Tue 5/26 |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     |    —          | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty        | Avg Entry | Sat Mark   | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|-----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341  |  $675.703 |   $685.55  |  $33,819.79  |  +$485.79  |  +1.458% |  33.52% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.54% |
| MSFT   | 11.521758  |  $404.973 |   $418.57  |   $4,822.66  |  +$156.66  |  +3.358% |   4.78% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 6.96% |
| GOOGL  | 12.047273  |  $387.308 |   $382.97  |   $4,613.74  |   -$52.26  |  -1.120% |   4.57% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 3.97% (compressed from 4.08%)** |
| META   |  7.767476  |  $600.710 |   $610.26  |   $4,740.18  |   +$74.18  |  +1.590% |   4.70% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 8.01% |
| AVGO   | 11.264102  |  $414.236 |   $414.14  |   $4,664.91  |    -$1.09  |  -0.023% |   4.62% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.87% (recovered from 3.78%, still tightest)** |
| V      | 10.256781  |  $325.053 |   $328.88  |   $3,373.25  |   +$39.25  |  +1.178% |   3.34% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.28% |
| BRK.B  |  6.883950  |  $484.315 |   $486.38  |   $3,348.22  |   +$14.22  |  +0.426% |   3.32% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 9.45% |
| LLY    |  3.341161  |  $997.857 | $1,065.00  |   $3,558.34  |  +$224.34  |  +6.728% (best UPL) |   3.53% | trail 10% / 3 sh GTC / HWM $1,070.3399 (held flat) / stop $963.30591 / cushion 9.55% |

**Notable Core changes since 5/22 EOD (20:16Z, ~44h ago)**:
- **All marks within ±$0.50 of Fri close**, all moves attributable to
  weekend quote-stream refresh noise (no live equity tape; broker uses
  cached pricing service).
- **GOOGL** mark eased $383.40 → $382.97 (-$0.43); cushion compressed
  4.08% → **3.97%** (now 2nd-tightest in book).
- **AVGO** mark up $413.75 → $414.14 (+$0.39); cushion recovered 3.78%
  → **3.87%** (still tightest in book but direction = improving).
- **MSFT** down $419.02 → $418.57; **VOO** down $685.75 → $685.55;
  **LLY** down $1,065.50 → $1,065.00; **V** down $329.00 → $328.88;
  **META** up $609.48 → $610.26; **BRK.B** up $485.98 → $486.38.
- **LLY HWM unchanged at $1,070.3399** — no walk-up (weekend, no live
  trading). Stop $963.30591 intact.
- **All 8 trail orders still GTC**; no broker events to log.

**Cushion rank (Sat 16:36Z weekend snapshot, tightest first)**:
1. AVGO **3.87%** (recovered from 3.78%; still tightest)
2. GOOGL **3.97%** (compressed from 4.08%; new 2nd-tightest)
3. MSFT 6.96% (down from 7.06%)
4. META 8.01% (up from 7.90%)
5. V 8.28% (down from 8.31%)
6. BRK.B 9.45% (up from 9.37%)
7. VOO 9.54% (down from 9.56%)
8. LLY 9.55% (down from 9.59%)

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken.**

Total Core committed: $62,941.97 (62.38% of equity). Weekend Core UPL
delta **-$9.04** ($951.01 → $941.97).

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Sat Mark | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held | Time stop | Strategy slug             |
|--------|----------:|----------:|---------:|-------------:|--------:|--------:|------:|--------:|----------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 |  $215.33 |   $1,957.89  | -$42.11 | -1.917% | $208.96 GTC | **2.96%** | 1 td | 2026-06-02 (7 td out) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 |  $377.78 |   $1,502.98  |  +$2.98 | +0.199% | $350.64 GTC | 7.19% | 1 td | 2026-06-05 (10 td out) | `swing-earnings-drift`   |

**NVDA Sat status (`swing-quality-pullback`)**: Weekend mark $215.33
(+$0.32 vs Fri $215.01). UPL recovered -2.251% → -1.917% (+$2.91 on
quote-noise; nothing live traded). Cushion 2.81% → **2.96%** —
modest recovery on the weekend quote, still well above -5% playbook
trigger. **Watch on Tue 5/26 open: if cushion compresses to <2% (mark
≈ $213.22), tighten posture** — consider half-out at market to lock the
remaining 1-1.5% cushion against a gap-down through the stop. Day-3
thesis intact (-5% pullback from 52w-Hi quality compounder; fundamentals
unchanged). NO action this routine.

**RL Sat status (`swing-earnings-drift`)**: Weekend mark $377.78 (+$0.74
vs Fri $377.04). UPL improved +0.003% → **+0.199%** (+$0.74 on
quote-noise). Cushion 7.00% → **7.19%**. First time-stop check on 6/5
close. PEAD thesis intact for Day-3+ of hold; typical post-earnings
drift profile is Day 3-5 acceleration. NO action this routine.

## Daytrade / Scalp sleeve (intraday only — weekend N/A, PDT count 2/5)

Empty (0 / 5). $10k budget intact. PDT count **2 / 5d UNCHANGED**.
Weekend, no entries possible. **No action this routine.**

## Crypto sleeve (24/7, $5k budget intact) — SCANNED

Empty (0 / 4). Sat 16:36Z scan of universe:

| Coin     | Last (5/23) | 24h     | 7d      | 50DMA       | 200DMA      | State        | 50/200 gap | Δ vs Fri 50/200 gap     |
|----------|------------:|--------:|--------:|------------:|------------:|--------------|-----------:|--------------------------|
| BTC-USD  |  $75,400.66 |  -0.12% |  -3.50% |  $76,552.25 |  $80,653.97 | 50<200 DOWN  |     -5.09% | narrowed -6.2% → -5.09%  |
| ETH-USD  |   $2,058.00 |  -0.32% |  -5.59% |   $2,262.21 |   $2,553.16 | 50<200 DOWN  |    -11.40% | wider (Fri not measured) |
| SOL-USD  |      $84.02 |  -0.34% |  -2.91% |      $86.31 |     $107.50 | 50<200 DOWN  |    -19.71% | wider                    |
| AVAX-USD |       $9.14 |  -0.07% |  -1.62% |       $9.38 |      $11.21 | 50<200 DOWN  |    -16.28% | wider                    |
| LINK-USD |       $9.31 |  -1.16% |  -4.26% |       $9.47 |      $10.93 | 50<200 DOWN  |    -13.37% | wider                    |

- **`crypto-trend-follow`**: 0/5 50/200 cross-up; BTC gap narrowed
  -6.2% → -5.09% (slow improvement, but not crossed). ETH/SOL/AVAX/LINK
  gaps remain wider, no imminent cross. **0 entries.**
- **`crypto-mean-reversion`**: 0/5 24h flush <-10% (largest is LINK
  -1.16%). **0 entries.**
- **`crypto-weekend-momentum`**: Fri 5/22 21:00Z Friday-close trigger
  NOT met (BTC 7d -3.02% << +2%) → no position opened → no monitor
  needed today. **No-op.**

**Decision: NO Crypto entries this routine.** Sleeve remains 0 / 4
positions; budget $5,000 intact.

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. Polygon options-chain
4th re-test deferred to Tue 5/26 01-pre-market (no benefit re-testing on
weekend — options market closed; 403 was a tier-gate, not a market-hours
issue, but a clean Tue re-test consolidates the audit trail). NVDA
conviction already running via Swing equity.

- 7 DTE rule: no positions, no-op.
- IV-crush check: no positions, no-op.
- Protective-put staleness: none open.

**Decision: NO Options actions this routine.**

## Today's trades (Sat weekend-crypto-cycle)

(none — 0 trades book-wide on Sat 2026-05-23; crypto scan returned 0
entry signals; equities can't trade weekends.)

## Organic broker events (this routine, no Bull action)

None. Weekend, no live trading. LLY HWM held flat at $1,070.3399. All
8 Core trail stops + 2 Swing stops remain `OrderStatus.NEW` GTC.

## Pending (not yet opened / re-evaluated)

- **AAPL** — `swing-short-rejection` re-watch on Tue 5/26 01-pre-market.
- **ARM** — `swing-momentum-breakout` re-arm only if ARM closes back
  below $290; above $290 + below $310 stays WATCH on Tue 5/26.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain (4th
  re-test on Tue 5/26 01-pre-market). NVDA conviction running via
  equity Swing.
- **Crypto weekend-momentum** — confirmed NO ENTRY at Fri 5/22 EOD;
  no monitor needed this weekend.
- **Crypto mean-reversion** — pre-trigger watch through Sun 5/24
  03-midday. If BTC/ETH gap down a further 5-7% on no fundamental
  break, trigger could fire on Sun 03-midday.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+
  per strategy.md v3 LM freeze.
- **AVGO earnings 2026-06-03**: 5 td out from Tue 5/26 cash open. Core
  hold posture intact; LM-paused Live-Phase #8 means no automatic
  exclusion zone for Core (and Core is frozen anyway).

## Recent Closed Positions (last 5)

(none — no closes across Live-Phase paper run + LM Day 1-3)

## LM Day 3 (Saturday) running tally

- Bull equity: **$100,901.97** (-$4.07 / -0.004% vs Day-2 EOD $100,906.04
  on weekend mark refresh noise; +$140.25 / +0.139% vs 5/21 EOD baseline
  $100,761.72).
- SPY: $745.70 (Fri 5/22 close, no weekend tape); VIX 16.82.
- Day-3 alpha (carryover only): **-25.8 bp** vs SPY (no weekend SPY
  tape; identical to 5/22 EOD final alpha).
- LM cumulative (since 5/21 EOD baseline): **+$140.25 / +0.139%**
  equity; **-25.8 bp** alpha vs SPY (carryover).
- Per-sleeve LM cumulative: Core +$180.25 / Swing -$39.13 / DT $0 /
  Crypto $0 / Options $0.
- Top experiment LM Day 1-3: `core-buy-and-hold` +$180.25.
- Bottom experiment LM Day 1-3: `swing-quality-pullback` -$42.11 (NVDA
  only).
- Trades today: 0 entries, 0 closes. Win/Loss: 0/0.
- PDT count (5d): 2 (unchanged from 5/22 02-market-open watermark).
