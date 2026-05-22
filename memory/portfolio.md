---
last_updated: 2026-05-22T16:42:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 2 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 03-midday (no trades; monitoring; LLY HWM organic advance #5)
total_value_usd: 100982.35
cash_usd: 34500.00
long_market_value_usd: 66482.35
day_pnl_usd_vs_last_equity: +225.78
day_pnl_pct_vs_last_equity: +0.2241
day_pnl_usd_vs_5_21_eod: +220.63
day_pnl_pct_vs_5_21_eod: +0.2190
prior_5_21_eod_usd: 100761.72
spy_open_5_22_pct: +0.5710
day_alpha_bp_vs_spy: -34.7
ytd_pnl_pct: 0.9824
benchmark_spx_ytd: 9.6322
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 746.96
alpha_vs_spx_ytd_pct: -8.6498
position_count_total: 10
position_count_core: 8
position_count_swing: 2
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.66
options_buying_power_usd: 67741.17
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
vix_current_approx: 16.59
market_state: open
next_close: 2026-05-22T20:00:00Z
---

# Portfolio — 03-midday 2026-05-22 (LM Day 2 of 30, 16:42Z / 12:42 ET)

> **Phase note**: 03-midday HOLD routine. 0 trades executed (NVDA + RL Swing
> positions both within drift band; no ARM trigger fired in the 13:30-14:00Z
> consolidation window; no clean Daytrade ORB/VWAP/scalp setup; no Crypto
> signal; Polygon options-chain still 403 Forbidden). **LLY HWM advanced
> ORGANICALLY 5th consecutive time** $1,063.67 → $1,069.11 since 02-market-open
> (stop $957.303 → $962.199, +0.51% additional walk-up). Equity drifted
> -$225.87 from 02-market-open peak on Core mark fade (MSFT, META, AVGO, GOOGL
> all eased into midday); Bull still **+$220.63 / +0.219% vs 5/21 EOD** but
> day-alpha widened to **-34.7 bp** as SPY held +0.571% while Core gave back
> some of the open-print pop. Swing sleeve UPL drifted -$9.76 → -$35.60 driven
> by NVDA -1.59% (cushion to stop 3.47% — still well above the playbook
> -5% trigger). RL UPL -0.26% (cushion 6.76%). All 10 stops verified live
> GTC. Macro risk-off NOT active (SPY +0.57% / VIX 16.59).

## Sleeve summary

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $63,018.43 (live mark)|             8  |  +$1,018.43 |   +1.642%   | Frozen — 8/8 stops live GTC; LLY HWM organic walk-up #5 (stop $962.199, +1.55% cumulative vs 5/21 EOD) |
| Swing      |  $15,000             | $3,500.00 (cost)      |             2  |    -$35.60  |   -1.017%   | NVDA -1.59% / RL -0.26% intraday; both stops live GTC; cushion ≥3.4% |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     | Empty — ORB window closed (13:30-14:00Z passed cleanly with no trigger); preserving PDT budget |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     | Empty — all 5 coins in 50<200 downtrend; no -10%/24h flush; weekend-momentum prep at 21:00Z |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     | Empty — Polygon options-chain still 403 Forbidden (re-tested 16:40Z) |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     | $3k earmarked of $34.5k cash |

Total deployable cash for non-Core sleeves: **$31,500** ($34.5k − $3k reserve).
Swing remaining budget after NVDA + RL: **$11,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty       | Avg Entry | Mark       | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|----------:|----------:|-----------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341 |  $675.703 |  $686.845  |   $33,883.67 |  +$549.67  |  +1.649% |  33.55% | trail 10% / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.71% |
| MSFT   | 11.521758 |  $404.973 |  $419.200  |    $4,829.92 |  +$163.92  |  +3.513% |   4.78% | trail 10% / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.10% |
| GOOGL  | 12.047273 |  $387.308 |  $385.540  |    $4,644.71 |   -$21.29  |  -0.456% |   4.60% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 4.61% |
| META   |  7.767476 |  $600.710 |  $607.670  |    $4,720.06 |   +$54.06  |  +1.159% |   4.67% | trail 10% / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 7.62% |
| AVGO   | 11.264102 |  $414.236 |  $413.801  |    $4,661.10 |    -$4.90  |  -0.105% |   4.62% | trail 10% / 11 sh GTC / HWM $442.36 / stop $398.124 / cushion 3.79% |
| V      | 10.256781 |  $325.053 |  $329.630  |    $3,380.94 |   +$46.94  |  +1.408% |   3.35% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.49% |
| BRK.B  |  6.883950 |  $484.315 |  $486.025  |    $3,345.77 |   +$11.77  |  +0.353% |   3.31% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 9.38% |
| LLY    |  3.341161 |  $997.857 | $1,063.183 |    $3,552.26 |  +$218.26  |  +6.547% (best UPL) |   3.52% | trail 10% / 3 sh GTC / **HWM ↑ organic #5 $1,069.11** / **stop $962.199** ↑ +0.51% vs 13:38Z / cushion 9.49% |

**Notable Core changes since 02-market-open (13:38Z):**
- **LLY HWM organic walk-up #5** $1,063.67 → $1,069.11 (+0.51%) with stop bumped
  $957.303 → $962.199. **Cumulative LLY stop walk vs 5/21 EOD $942.5655**: +$19.63
  / +2.08%. 5 consecutive HWM advances over 2 trading days; biggest single-name
  Core protection drift in the entire Live-Phase + LM record.
- **AVGO cushion compressed** 4.87% → **3.79%** as mark $418.53 → $413.80
  (-1.13% intraday). Still above the 3% routine-spec watch threshold but is now
  the tightest Core cushion. No action; AVGO earnings 6/3 = 8 trading days out
  (outside Live-Phase #8 exclusion zone but worth flagging into 04-pre-close
  in case of further compression).
- **GOOGL** drifted further negative -0.059% → **-0.456%** on mark $387.08 →
  $385.54. Still cushion 4.61% (2nd tightest), no action.
- **MSFT + META** gave back some of the open-print pop: MSFT +4.575% → +3.513%,
  META +2.264% → +1.159%. All within normal intraday drift.
- **V + BRK.B** mostly flat-to-slightly-negative vs 13:38Z.
- **All 8 trail orders verified `OrderStatus.NEW` GTC** in 16:40Z order list.

**Cushion rank (live 16:42Z, tightest first):**
1. AVGO 3.79% (tightest, compressed from 4.87%)
2. GOOGL 4.61% (compressed from 5.00%)
3. MSFT 7.10%
4. META 7.62%
5. V 8.49%
6. BRK.B 9.38%
7. LLY 9.49% (largest; benefited from organic HWM walk-up #5)
8. VOO 9.71%

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken this
routine.** All stops remain GTC and intact. AVGO cushion noted for 04-pre-close
re-check.

Total Core committed: $63,018.43 (62.41% of equity)

## Swing sleeve (2 / 8 positions, $11,500 budget remaining)

| Symbol | Qty       | Avg Entry | Mark    | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held | Time stop | Strategy slug             |
|--------|----------:|----------:|--------:|-------------:|--------:|--------:|------:|--------:|----------:|----------:|---------------------------|
| NVDA   |  9.092513 |  $219.961 | $216.475|    $1,968.30 | -$31.70 | -1.585% | $208.96 GTC | 3.47% | 1 | 2026-06-02 (7d) | `swing-quality-pullback` |
| RL     |  3.978463 |  $377.030 | $376.050|    $1,496.10 |  -$3.90 | -0.260% | $350.64 GTC | 6.76% | 1 | 2026-06-05 (10d) | `swing-earnings-drift`   |

**NVDA midday status (`swing-quality-pullback`)**: UPL drifted -0.073% → -1.585%
(-$30.23 intraday) on mark $219.80 → $216.475. Distance to stop $208.96 still
3.47% — well above the playbook's -5% trigger. Day 1 of 7-day time-stop. Target
$235 unchanged. **No action**; UPL within normal drift band (-2% / +3% per
routine spec) — would only flag at -5% drift or stop-cushion < 1%.

**RL midday status (`swing-earnings-drift`)**: UPL drifted -0.553% → -0.260%
(+$4.40 intraday recovery) on mark $374.945 → $376.05. Distance to stop $350.64
is 6.76% — comfortable. Day 1 of 10-day time-stop. Target $414.73 unchanged.
**No action**.

**Other Swing candidates from morning plan — midday status:**
- **ARM (`swing-momentum-breakout`)**: mark $307.64 (vs 13:37Z $294.90, +4.32%
  intraday). Did NOT consolidate above $290 in the 13:30-14:00Z window per the
  morning ORB-style trigger — instead grinded higher continuously. The trigger
  window has passed. ARM is now ~0.77% below the 01-pre-market "DO NOT chase
  above $310" line — chase risk has materially increased vs both pre-market
  and 02-market-open. **Decision: PASS** (missed trigger, do not chase). Will
  not re-arm today; revisit fresh in next 01-pre-market if ARM closes back
  below $290 (i.e. a clean retest of the breakout level).
- **AAPL (`swing-short-rejection`)**: mark $309.48 (vs 5/21 close $304.99,
  +1.47% intraday — fresh 52w-Hi extension). No rejection candle yet (today's
  bar is currently UP). Decision per playbook: defer to 04-pre-close for EOD
  candle confirmation. If 5/22 prints close < open at 52w-Hi → SHORT
  $1,500 (hard-to-borrow status TBD via Alpaca pre-order).
- **INTU**: still SKIP (falling-knife AI-disruption + restructuring narrative).

## Daytrade / Scalp sleeve (intraday only — flat by 20:30Z, PDT count 2/5)

Empty (0 / 5). $10k budget intact. **PDT count 2 / 5d** — UNCHANGED from
02-market-open (Alpaca watermark from NVDA + RL Swing fills with same-day GTC
stops, observation only). No drift to 3+ → ORB/scalp PDT budget is intact at
2 round-trips of headroom.

- **ORB WATCH list** (5-min ORB resolved ~13:35Z): no clean trigger fired in
  any of SPY/QQQ/NVDA/TSLA/AAPL/AMD that met playbook criteria (break of 5-min
  range on ≥150% avg vol + macro tape constructive). 13:30-14:00Z window has
  now closed; execution deferred per the routine spec. No `daytrade-orb` entry.
- **VWAP-pullback WATCH**: requires 5-min close > VWAP for ≥30 min before
  pullback signal can fire. By 16:42Z (3h 12min into session), criteria not
  cleanly met on any of the universe names without real-time Polygon 1-m
  aggregates pull (not refreshed since 02-market-open). No entry.
- **Gap-go status**: TTWO -3.48% (gap-down despite GTA VI reaffirm — Reuters
  flow tagged it as "buy-rumor sell-news"; the gap-fade thesis "no clean
  catalyst" doesn't apply since the catalyst IS the gap, so no gap-fade
  entry either). WDAY +5.45% has already played out — too late to chase.
  Decision: no gap-go / gap-fade entries.
- **scalp-tape**: SPY +0.57% / QQQ +0.70% — no clean 1-min momentum window
  emerged in the morning. PDT budget preserved. No entry.
- **daytrade-news-catalyst**: U-Mich + Waller speech passed at 14:00Z; no
  tier-1 surprise that warranted entry. No entry.

**Heads-up for 04-pre-close**: No forced exits pending (Daytrade sleeve empty
→ force-flat is a no-op today).

## Crypto sleeve (24/7)

Empty (0 / 4). $5k budget intact. Mid-session yfinance snapshot:

| Coin | Last | 24h | 7d | 50/200 DMA |
|------|-----:|----:|---:|------------|
| BTC-USD  | $76,835   | -0.91% | -2.08% | 50<200 ↓ |
| ETH-USD  | $2,118    | -0.61% | -4.10% | 50<200 ↓ |
| SOL-USD  | $86.72    | -0.50% | -1.93% | 50<200 ↓ |
| AVAX-USD | $9.41     | -0.33% | -0.18% | 50<200 ↓ |
| LINK-USD | $9.76     | +0.17% | -1.65% | 50<200 ↓ |

- **`crypto-trend-follow`**: 0 signals (all 5 still 50<200 downtrend; no
  cross-up imminent).
- **`crypto-mean-reversion`**: 0 (no -10%/24h flush; deepest is BTC -0.91%).
- **`crypto-weekend-momentum`** (Fri 21:00Z trigger): BTC 7d **-2.08%** —
  would need a +4%+ rally in next 4h to qualify for the weekly +2% threshold.
  Highly unlikely; final check at 05-close-summary 21:00Z.
- **Plan**: NO crypto entries at 03-midday. If 03-midday cron extends to Sat+Sun
  per the inbox Q1 C reminder, the next two routines fire 2026-05-23 17:30Z
  + 2026-05-24 17:30Z; with current 50<200 universe-wide downtrend, expected
  outcome both days is "scan + no signal."

## Options sleeve (Level 3 enabled)

Empty (0 / 6 contracts). $5k premium budget intact. Options BP **$67,741.17**
/ Level 3 ✓. **Polygon options-chain re-tested at 16:40Z → still 403 Forbidden**
on `/v3/snapshot/options/NVDA` endpoint (`get_iv_rank('NVDA')` returns None).
Options-Starter add-on still appears gated on the current Polygon tier.

- `options-vertical-bull-call-spread` NVDA candidate: BLOCKED (chain
  inaccessible). NVDA conviction already routed through equity sleeve at open.
- `options-protective-put`: no FOMC/CPI today. SKIP.
- `options-earnings-strangle`: no qualifying names in next 5d + IV-rank
  unavailable. SKIP.
- `options-long-call-momentum`: ARM extended (chase risk); NVDA pullback
  not a momentum breakout. DEFER.

**Decision: NO Options entries today**, per the 02-market-open fallback plan.

## Today's trades

(none at 03-midday — see 02-market-open section above for today's 2 Swing fills)

**Organic broker events** (no Bull action, recorded for audit):
- **LLY trail HWM advanced ORGANICALLY 5th consecutive time** $1,063.67 →
  $1,069.11 (+0.51%) since 02-market-open. **Stop bumped $957.303 → $962.199
  (+0.51%)**. Cumulative LLY trail walk over 2 LM days: $942.5655 → $962.199
  = **+$19.63 / +2.08%**. LLY UPL +6.547% (mark $1,063.18).

## Pending (not yet opened / re-evaluated)

- **ARM** — TRIGGER MISSED in 13:30-14:00Z window; price grinded to $307.64
  by 16:42Z without a clean ORB-style consolidation+break. No re-arm today;
  revisit in next 01-pre-market if ARM closes back below $290.
- **AAPL short** — WATCH for daily close < open AT 52w-Hi; defer to 04-pre-close
  (need EOD candle). Hard-to-borrow check via Alpaca required pre-order.
- **NVDA options bull-call-spread** — BLOCKED on Polygon chain (re-confirmed
  16:40Z). NVDA conviction taken via equity Swing entry at open. Drop for the
  day.
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no closes across Live-Phase paper run + LM Day 1 + LM Day 2 first half)
