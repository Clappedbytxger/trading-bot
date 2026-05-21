---
last_updated: 2026-05-21T20:30:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 1 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 05-close-summary (EOD HOLD — abort-entries posture continued; Day 1 closes with 0 trades on all sleeves)
total_value_usd: 100761.72
cash_usd: 38000.00
long_market_value_usd: 62761.72
day_pnl_usd_vs_thu_open: +151.23
day_pnl_pct_vs_thu_open: +0.1503
prior_close_5_20_usd: 100610.49
day_spy_pct_vs_thu_open: +0.2050
day_alpha_bp_vs_spy: -5.5
ytd_pnl_pct: 0.7617
benchmark_spx_ytd: 9.0240
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 742.77
spy_5_20_close: 741.25
alpha_vs_spx_ytd_pct: -8.2623
position_count_total: 8
position_count_core: 8
position_count_swing: 0
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.62
options_buying_power_usd: 69380.85
options_approved_level: 3
daytrade_count_5d: 0
pattern_day_trader: false
cash_reserve_min_usd: 3000
cash_available_for_non_core_usd: 35000
sleeve_budget_swing_usd: 15000
sleeve_budget_daytrade_usd: 10000
sleeve_budget_crypto_usd: 5000
sleeve_budget_options_premium_usd: 5000
sleeve_used_swing_usd: 0
sleeve_used_daytrade_usd: 0
sleeve_used_crypto_usd: 0
sleeve_used_options_usd: 0
polygon_api_key_set: false
macro_risk_off_active: false
vix_current: 16.72
market_state: closed
next_open: 2026-05-22T13:30:00Z
---

# Portfolio — 05-close-summary 2026-05-21 EOD (LM Day 1 of 30, 20:30Z / 16:30 ET)

> **Phase note**: 05-close-summary EOD snapshot. Market is CLOSED
> (`is_open=False`, next_open 2026-05-22 13:30Z). Day 1 of Learning Month
> closes with **0 trades on all sleeves** — the abort-entries posture
> from 02-market-open held all the way through 04-pre-close and is now
> locked in for Day 1. Day finished green: equity $100,761.72 vs 5/20
> close $100,610.49 → +$151.23 / +0.150%. SPY +0.205% → final day-alpha
> -5.5 bp (recovered from -8.8 bp at 04-pre-close as Core marks ticked
> up into the last 24 min). VIX 16.72 → no risk-off. 18th consecutive
> no-action routine extending the Live-Phase exit-week streak.

## Sleeve summary

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,761.72 (EOD mark) |             8  |  +$761.72   |   +1.229%   | Frozen — 8/8 stops live GTC; LLY HWM advanced 3x today; AVGO cushion recovered 3.43% → 3.90% |
| Swing      |  $15,000             |        $0             |             0  |       $0    |       —     | Empty (abort-entries Day 1)  |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     | Empty — Day 1 closes with PDT count 0 / 5d, never blocked |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     | Empty — `crypto-weekend-momentum` setup checked Fri 5/22 |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     | Empty — Options BP $69,380.85 / Level 3 ready |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     | $3k earmarked of $38k total  |

Total deployable cash for non-Core sleeves once trading resumes: **$35,000**.

## Core sleeve (8 positions, all inherited from Live-Phase exit)

| Symbol | Qty       | Avg Entry | EOD Mark   | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / cushion |
|--------|----------:|----------:|----------:|-------------:|-----------:|---------:|--------:|----------------------|
| VOO    | 49.332341 |  $675.703 |  $683.03  |   $33,695.47 |  +$361.47  |  +1.084% |  33.44% | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.20% |
| MSFT   | 11.521758 |  $404.973 |  $419.66  |    $4,835.22 |  +$169.22  |  +3.627% |   4.80% | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.20% |
| GOOGL  | 12.047273 |  $387.308 |  $387.66  |    $4,670.25 |   +$4.25   |  +0.091% |   4.64% | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 5.14% |
| META   |  7.767476 |  $600.710 |  $607.38  |    $4,717.81 |   +$51.81  |  +1.110% |   4.68% | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 7.58% |
| AVGO   | 11.264102 |  $414.236 |  $414.2595|    $4,666.26 |   +$0.26   |  +0.006% |   4.63% | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / cushion **3.90% (tightest, recovered)** |
| V      | 10.256781 |  $325.053 |  $331.12  |    $3,396.23 |   +$62.23  |  +1.866% |   3.37% | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.90% |
| BRK.B  |  6.883950 |  $484.315 |  $479.40  |    $3,300.17 |   -$33.83  |  -1.015% |   3.27% | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.13% |
| LLY    |  3.341161 |  $997.857 | $1,041.65 |    $3,480.32 |  +$146.32  |  +4.389% (best UPL) |   3.45% | 10% trail / 3 sh GTC / **HWM $1,047.295 ↑↑↑ (3rd today)** / stop $942.5655 / cushion 9.51% |

**Stop-cushion rotation since 04-pre-close (19:36Z):**
- **AVGO cushion recovered** 3.43% → **3.90%** (mark $412.265 → $414.2595, late-
  session bid added +$1.99 / +0.48% — flipped AVGO from -0.48% UPL to flat
  +0.006%). HWM unchanged at $442.36. AVGO ends Day 1 still the tightest
  cushion but well clear of the 3.00% log-flag threshold. The intraday
  tightening 5.25% → 3.69% → 3.43% → 3.90% mirrors the day's micro-rotation
  AVGO → AVGO → AVGO → modest recovery.
- **LLY trail HWM advanced AGAIN** $1,046.415 → **$1,047.295** (+$0.88).
  Stop bumped $941.7735 → **$942.5655** (+$0.79). **3rd organic LLY trail-
  advance of the day** — biggest single name driving cushion progression
  on Day 1. LLY closes at +4.389% UPL (the day's best Core name); the
  stop has crept up ~$3.52 today total (from $939.044 at open to $942.5655
  EOD).
- **GOOGL cushion tightened** 5.32% → **5.14%** (mark $388.43 → $387.66,
  -0.20% into close). Now 2nd-tightest after AVGO; HWM unchanged at $408.61.
  Worth watching if GOOGL ticks lower at 5/22 open.
- **All other 5 stops (VOO/MSFT/META/V/BRK.B)**: HWMs unchanged. Cushions
  rotated modestly with EOD marks:
  - VOO 9.17% → 9.20% (+3 bp)
  - MSFT 7.02% → 7.20% (+18 bp)
  - META 7.54% → 7.58% (+4 bp)
  - BRK.B 8.20% → 8.13% (-7 bp; BRK.B faded into close to -1.02% UPL)
  - V 8.89% → 8.90% (+1 bp)
- **All 8 trail orders verified `OrderStatus.NEW` GTC** via live broker
  open-orders query post-close.

**Cushion rank (EOD, tightest first):**
1. AVGO 3.90% (no flag; recovered intraday)
2. GOOGL 5.14% (slight tighten end of day)
3. MSFT 7.20%
4. META 7.58%
5. BRK.B 8.13%
6. V 8.90%
7. VOO 9.20%
8. LLY 9.51%

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken
this routine.** All stops remain GTC and intact across the EOD print.

Total Core committed: $62,761.72 (62.29% of equity)
Cash retained: $38,000.00 (37.71%)

## Swing sleeve
Empty (0 / 8). $15k budget intact. Abort-entries continued from 02/03/04;
no plan = no entries per ALM-1. Day 1 ends with **zero Swing trades** —
first real chance is tomorrow's 02-market-open (assuming 01-pre-market
back-fires on schedule, or the new Step 1a inline back-fire kicks in if
it doesn't). Sub-strategies remain at 0 trades / 0 setups identified.

## Daytrade / Scalp sleeve (intraday only)
Empty (0 / 5). $10k budget intact. Daytrade count (rolling 5d) **0**
across the entire Day 1 → PDT-watermark vacuously safe. ORB/VWAP/scalp/gap
strategies remain dormant — POLYGON_API_KEY still **NOT SET**, will block
all Polygon-dependent sub-strategies (`daytrade-orb`, `daytrade-vwap-pullback`,
`scalp-tape`) even if 01-pre-market fires tomorrow.

## Crypto sleeve (24/7)
Empty (0 / 4). $5k budget intact. 1 scan logged Day 1 (03-midday: all
5 universe names in 50<200 downtrend, 0 entries). **Friday 5/22 setup**:
`crypto-weekend-momentum` entry trigger checks BTC weekly +2% at Fri
21:00Z 05-close-summary. As of Day 1 close BTC 5d -1.40% → would need
~3.4% rally Friday alone to qualify. Watch but not currently set up.

## Options sleeve (Level 3 enabled)
Empty (0 / 6 contracts). $5k premium budget intact. Options BP **$69,380.85**
/ Level 3 ✓ (broker confirms). No Greeks check / no 7-DTE close / no
IV-crush exit needed (zero contracts). POLYGON_API_KEY still NOT SET →
blocks any Options entry that requires chain reads.

## Today's trades

**Zero trades — full LM Day 1 closes with 0 fills across all 5 sleeves.**
18th consecutive no-action routine extending the Live-Phase exit-week
streak (now 9 trading days + LM Day 1 = ~10 trading days no-trade since
the last real fill).

**Organic broker events** (not Bull actions, recorded for audit):
- **LLY trail HWM bumped 3rd time of the day**: $1,046.415 → $1,047.295
  in the last 24 min. Stop: $941.7735 → $942.5655. Cumulative Day-1
  organic trail advance: $939.044 (open) → $942.5655 (EOD), i.e. +$3.52
  / +0.37%. This is a meaningful data point — even a frozen Core sleeve
  generates positive trail-stop "protection drift" on names that print
  intraday HWMs.
- **AVGO mark recovered** $412.265 → $414.2595 (+0.48% into close);
  UPL flipped -0.48% → +0.006%. Cushion 3.43% → 3.90%. HWM unchanged.

## Pending (not yet opened)

- **NVDA Swing entry candidate** (`swing-earnings-drift`): now Day-2 post-
  print (Wed 5/20 post-close earnings). 01-pre-market 2026-05-22 13:00Z
  should pull NVDA Day-1 reaction (5/21 EOD close), PT revisions (Gemini
  news scan), and guidance details. Day-2 entry under `swing-earnings-drift`
  playbook is permitted if Day-1 reaction was ≥+5% AND PT raises within
  24h. Will be evaluated tomorrow's 01-pre-market.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no closes in entire Live-Phase paper run + LM Day 1)
