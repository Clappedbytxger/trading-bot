---
last_updated: 2026-06-10T12:09:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 21 of 30 -- Wed 6/10 01-pre-market; 10 LM days remaining incl today; CPI day)
phase_window: 2026-05-21 -> 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 01-pre-market (LM Day 21; 8th consecutive trading day with all-02/03/04/05-misses; 3rd consecutive on-time 01)
total_value_usd: 99870.82
cash_usd: 49845.72
long_market_value_usd: 50025.10
last_equity_eod_6_09_usd: 100191.77
prior_5_29_eod_usd: 102178.75
prior_6_05_eod_usd: 100099.09
lm_baseline_5_21_eod_usd: 100761.72
day_pnl_vs_6_09_eod_usd: -320.95
day_pnl_pct_vs_6_09_eod: -0.003204
week_to_date_pnl_vs_6_05_eod_usd: -228.27
week_to_date_pnl_pct_vs_6_05_eod: -0.002280
lm_cum_pnl_usd_since_5_21_eod: -890.90
lm_cum_pnl_pct_since_5_21_eod: -0.008842
spy_pre_mkt_6_10_usd: 737.05
spy_close_6_09_usd: 735.70
spy_close_6_05_usd: 737.55
spy_close_5_29_usd: 756.48
spy_wtd_pct_vs_6_05_close: -0.00251
spy_lm_pct_vs_5_21_baseline: -0.007711
ytd_pnl_pct: 0.0972
benchmark_spx_ytd: 8.1907
position_count_total: 10
position_count_core_active: 5
position_count_core_stub: 4
position_count_swing: 1
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.501
options_buying_power_usd: 74858.26
options_approved_level: 3
daytrade_count_5d: 0
pattern_day_trader: false
shorting_enabled: true
cash_reserve_min_usd: 3000
cash_available_for_non_core_sleeves_usd: 46846
sleeve_budget_swing_usd: 15000
sleeve_budget_daytrade_usd: 10000
sleeve_budget_crypto_usd: 5000
sleeve_budget_options_premium_usd: 5000
sleeve_used_swing_usd: 1500
sleeve_used_daytrade_usd: 0
sleeve_used_crypto_usd: 0
sleeve_used_options_usd: 0
polygon_api_key_set: true
polygon_options_chain_gated: true
polygon_options_chain_consecutive_blocks: 14
callmebot_outage_active: false
callmebot_streak_broken_6_10: true
callmebot_consecutive_503_days_broken_at: 5_consecutive_then_resolved_via_short_form
macro_risk_off_active: false
macro_regime: pre_cpi_hedging (Wed 6/10 12:30Z May CPI release event; VIX +17% to 22.16 on Tue close pre-CPI bid; futures +0.18% modest; oil +1.7% on geopol re-pricing; META cushion 0.76% book-record tightest -- knife-edge on the print)
vix_close_6_09: 22.16
market_state: pre_market_open (Wed 2026-06-10 12:09Z; 81 min to cash open at 13:30Z; CPI release 12:30Z = 21 min away pre-open)
next_open: 2026-06-10T13:30:00Z
cpi_release_today_z: 2026-06-10T12:30:00Z
orcl_earnings_today_pc: true
---

# Portfolio -- 01-pre-market 2026-06-10 (LM Day 21 -- KW 24 Wed; CPI day; META knife-edge)

> **Phase note**: Wed 2026-06-10 01-pre-market slot fired on-time at 12:06Z
> (3rd consecutive on-time 01 for KW 24). Mon 6/8 + Tue 6/9 02/03/04/05
> ALL MISSED -- 8 consecutive failed routines KW 24 (after 20 missed in
> KW 23). Cash $49,845.72 UNCHANGED since 5/22 confirms zero fills despite
> 4 stub liquidates + RL liquidate queued through 3-4 attempts each.
> **META cushion compressed to BOOK RECORD TIGHTEST 0.76%** (mark $583.13
> vs trail-stop $578.70) on Tue intraday drift -- the next-mechanical-stop
> candidate, with CPI release 12:30Z (21 min after this routine ends) as
> the direct trigger risk. **RL `swing-earnings-drift` recovered to
> +3.17% / +$47.54** -- PEAD fired late on td11-13 post-NFP-consumer-rotation;
> still queued to MARKET SELL Wed 02-market-open per ALM-3 time-stop
> discipline; **first Swing WIN in LM book history if it executes**.
> Polygon options-chain 14th consecutive 403; L4 default deadline slipped
> to Wed EOD. **CallMeBot 5-day outage BROKEN this routine** via single-shot
> short-form ≤500-char WhatsApp -- candidate L1-KW24 lesson encoded today.

## Sleeve summary (Wed 6/10 12:09Z; broker live marks 81 min pre-open)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs Tue pre-mkt | Notes |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------:|-------|
| Core       |  $62,000 (cost basis frozen) | $48,512.75 active + $344.55 in 4 stubs | 5 + 4 stubs | +$131.00 active + -$12.16 stubs net = **+$118.84** | +0.27% on active | -$420.46 active UPL Δ + -$0.83 stubs Δ = **-$421.29 net** | META cushion 0.76% book-record tightest; CPI 12:30Z trigger; 4 stubs 4th attempt queued |
| Swing      |  $15,000             | $1,500 (RL cost basis) | 1 (RL) + NVDA stub | **+$47.54** RL + -$1.52 stub = **+$46.02** | **+3.17%** RL (1st time green; td13 past time-stop) | **+$62.15 RL Δ** (Tue -$14.61 -> Wed +$47.54) | RL PEAD fired LATE on td11-13; liquidate Wed at 02 per ALM-3 time-stop modal regardless of P&L |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       --    |    $0            | Empty 15 LM days; PDT 0/5 full budget; AAPL ORB-short + energy ORB-long watch |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       --    |    $0            | Continued post-NFP-flush drift; no fresh trigger on any of 5 coins; effectively dormant remaining 10 LM days |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       --    |    $0            | Polygon chain BLOCKED 14 consecutive; **L4 DEFAULT SLIPPED 2x; firm deadline = Wed 05-close-summary OR next-routine-that-fires** |
| Cash reserve | ≥$3,000            |       --              |             --  |       --    |       --    |    --            | $3k earmarked of $49.85k cash |

Total deployable cash for non-Core sleeves: **$46,846** ($49,845.72 - $3,000 reserve).
Swing remaining budget after RL: **$13,500** (RL liquidate will return ~$1,547 to cash).

## Core sleeve (5 active + 4 stubs; frozen) -- Wed 6/10 12:09Z

| Symbol | Qty        | Avg Entry | Mark    | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|-----------:|----------:|--------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341  |  $675.703 | $671.41 |  $33,122.31  |  -$211.69  |  -0.64% |  33.16% | trail 10% / 49 sh GTC / HWM $699.15 / stop $629.235 / **cushion 6.28%** |
| LLY    |  3.341161  |  $997.857 | $1,137.01 |  $3,798.93 |  +$464.93  | +13.94% (best in book) |   3.80% | trail 10% / 3 sh GTC / **HWM $1,182.73 (book ATH; walked Mon)** / stop $1,064.457 / **cushion 6.38%** |
| META   |  7.767476  |  $600.710 | **$583.13** |   $4,529.44  |   -$136.56 |  -2.93% |   4.54% | trail 10% / 7 sh GTC / HWM $643.00 / stop $578.70 / **cushion 0.76% (BOOK RECORD TIGHTEST)** |
| V      | 10.256781  |  $325.053 | $323.49 |   $3,318.00  |   -$16.00  |  -0.48% |   3.32% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / **cushion 6.75%** |
| BRK.B  |  6.883950  |  $484.315 | $488.72 |   $3,364.32  |   +$30.32  |  +0.91% |   3.37% | trail 10% / 6 sh GTC / HWM $491.00 / stop $441.90 / **cushion 9.58%** |

**Tue intraday Core drift (broker mid-day mark moves; Tue 02/03/04/05 missed -- no Bull intervention)**:
- META: $585.25 Tue pre-mkt -> $583.13 Wed pre-mkt (-$0.40% drift; cushion 1.12% -> 0.76%)
- LLY: $1,149.79 -> $1,137.01 (-1.11%; no new HWM)
- V: $319.72 -> $323.49 (+1.18%)
- VOO: $679.77 -> $671.41 (-1.23%; SPY-tracking)
- BRK.B: $486.925 -> $488.72 (+0.37%)
- Net Core active UPL: +$551.46 Tue pre-mkt -> +$131.00 Wed pre-mkt = **-$420.46**

**No Tue HWM walks** (none of the trailing stops moved; trail bands held flat as marks drifted).

**Cushion rank (Wed 12:09Z, active Core only, tightest first)**:
1. **META 0.76% (BOOK RECORD TIGHTEST)** -- knife-edge pre-CPI 12:30Z
2. VOO 6.28%
3. LLY 6.38%
4. V 6.75%
5. BRK.B 9.58%

**Fractional stubs in book (4 -- queued for Wed 6/10 02-market-open 4th-attempt consolidated liquidate)**:

| Symbol | Qty | Avg | Mark | mv | UPL$ | UPL% | Liquidate attempt # | Strategy attribution finalizer |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| MSFT stub | 0.521758 | $401.40 | $398.42 | $207.88 | -$1.55 | -0.74% | 3rd attempt | Locks `core-buy-and-hold` MSFT final at ~+$167 realized incl. stub |
| NVDA stub | 0.092513 | $219.961 | $203.51 | $18.83 | -$1.52 | -7.48% | 10th attempt | Locks `swing-quality-pullback` final at ~-$100 realized + stub |
| GOOGL stub | 0.047273 | $387.320 | $360.35 | $17.03 | -$1.27 | -6.96% | 6th attempt | Locks `core-buy-and-hold` GOOGL final at ~-$317 realized incl. stub |
| AVGO stub | 0.264102 | $411.295 | $381.70 | $100.81 | -$7.82 | -7.20% | 5th attempt | Locks `core-buy-and-hold` AVGO final at ~-$45 realized incl. stub |
| Sub-total stubs | -- | -- | -- | **$344.55** | **-$12.16** | -- | -- | -- |

Strategy slug for 5 active + 3 Core-legacy stubs: `core-buy-and-hold`. **No new Core
entries authorized during LM** (Sleeve 1 frozen per strategy.md v3).

Total Core committed: $48,512.75 active + $344.55 stubs = **$48,857.30 (48.92% of equity)**.
KW 24 to-date Core UPL Δ -$405.27 + 0 realized (no fills) = net **-$405.27**.

**Core watch items for Wed 02-market-open**:
- **META cushion 0.76% (BOOK RECORD TIGHTEST)** -- next mechanical stop-candidate
  IF CPI 12:30Z prints hot. Mechanical stop will fire at $578.70 if mark touches
  it. Modal realized: ~-$154 ($578.70 - $600.71 = -$22.01 * 7 sh). No override
  authorized; accept fill if it triggers per ALM-1 + Core-frozen rules.
- **4 fractional stubs queued together for Wed 6/10 02-market-open consolidated
  liquidate (4th attempt)**. Combined mv ~$345.
- **VOO/LLY/V/BRK.B** all holding above 6.28% cushion -> routine HOLD.

## Swing sleeve (1 / 8 positions; RL recovered into profit at td13) -- Wed 6/10 12:09Z

| Symbol | Qty       | Avg Entry | Mark    | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held (cal / td) | Time stop | Strategy slug             |
|--------|----------:|----------:|--------:|-------------:|--------:|--------:|------:|--------:|--------------------:|----------:|---------------------------|
| RL     |  3.978463 |  $377.030 | **$388.98** |  $1,547.54   | **+$47.54** | **+3.17%** | $350.64 GTC | **9.86%** | 19 cal / 13 td | **PAST td10 time-stop by 3 td** -- Wed 6/10 4th-attempt liquidate queued | `swing-earnings-drift` |

**RL recovery analysis**: Tue mark $373.33 -> Wed pre-mkt $388.98 = +$15.65 /
+4.19% in 1 session. UPL flipped -$14.61 Tue -> +$47.54 Wed. PEAD-style
DRIFT finally fired on Tue post-NFP-consumer-rotation tape (Tue Day 11+12+13
held a slow grind higher into consumer-discretionary rotation as cool-wage
NFP-print absorbed the hawkish-Fed initial reaction).

**Action queued for Wed 6/10 02-market-open**: MARKET SELL 3.978 sh DAY at
04 open (4th attempt). Modal final realized: **+$45 to +$55 / +0.43R to
+0.52R**. **FIRST SWING WIN IN LM BOOK HISTORY** if it executes. Stop
$350.64 GTC cancel post-fill. Strategy attribution: `swing-earnings-drift`
with `actual-vs-modal-comment: literature-Day-3-5 peak (+3.36% td2-3)
not captured; late-fire drift td11-13 captured via time-stop laxness;
on a 1-trade sample this is luck not skill; record as data point for
the LM Final Report 6/20`.

## Daytrade / Scalp sleeve (0 / 5; $10k budget intact)

Empty. PDT count 0/5 (full budget). 15 LM days with 0 entries. No fills
KW 24 because all Mon-Tue 02/03 routines MISSED. ORB / VWAP / scalp
triggers all reachable on data -- the absence is operational (cron-miss)
more than concept. Continue ACTIVE; re-evaluate Wed 6/10 if 02-market-open
fires reliably.

**Wed 6/10 ORB watch list**:
- AAPL post-WWDC ORB-short candidate
- AAPL gap-fade-short if >1.5% gap-down
- XLE/XOM ORB-long if energy continues firming
- SPY/QQQ post-CPI ORB only if clean directional bias

## Crypto sleeve (24/7, $5k budget intact)

Empty. All 5 universe coins -0.9% to -2.7% 24h on continued post-NFP-flush
drift; no 24h move has crossed -10% flush threshold. BTC 50/200 cross-up
gap WIDE post-Fri flush (ETA pushed past 6/20 LM end).

**Crypto sleeve realistically dormant for remaining 10 LM days** -- contributing
$0 to LM Final Report 6/20.

`crypto-weekend-momentum`: next eval Fri 6/12 21:00Z; BTC 7d -2.8% <<+2% threshold.

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. **Polygon options-chain
BLOCKED 14 consecutive routines** (5/26 1st through 6/10 14th).

**L4 ESCALATION default-trigger SLIPPED 2x**: Mon 6/8 EOD then Tue 6/9 EOD
both deadlines slipped because 05-close-summary missed both days. **Revised
firm deadline: Wed 6/10 05-close-summary (21:15Z) OR THE NEXT ROUTINE THAT
FIRES**, whichever comes first. Robin inbox.md Pending still EMPTY. Default
path (b) = reallocate $5k Options premium -> Cash reserve; mark Options
sleeve PAUSED in strategy.md v3.

**Missed Options opportunities Wed (forward)**:
- **CPI Wed 12:30Z `options-protective-put` 0-DTE setup**: chain inaccessibility
  = direct cost ~$30-100 on $300-500 premium IF CPI hot.
- **ORCL post-close `options-earnings-strangle`**: chain inaccessibility =
  direct cost ~$30-80.

Cumulative Options-sleeve opportunity-cost LM-to-date estimate: ~$350-1500
of would-be P&L depending on entry timing. Meaningful relative to $5k
premium budget; the L4 default reallocation is now overdue.

## Today's trades (Wed 6/10 -- 0 trades book-wide this routine)

(none yet; pre-market routine; market opens 13:30Z. 5 orders queued for
02-market-open if it fires: 4 stub liquidates + 1 RL liquidate.)

## Pending (queued for downstream routines)

- **5 orders queued Wed 6/10 02-market-open**: 4 stub liquidates (4th attempt)
  + 1 RL liquidate (4th attempt; **first Swing WIN candidate**).
- **META cushion-watch CRITICAL** (0.76% book-record tightest) -- mechanical
  stop possible Wed 13:30Z on CPI reaction.
- **CPI Wed 12:30Z** -- direct META trigger risk + macro pulse for all sleeves.
- **ORCL Q4 earnings Wed post-close** -- `swing-earnings-drift` Thu 6/11
  candidate IF beat + guide + PT raise within 24h.
- **AAPL `swing-short-rejection`** -- WWDC catalyst veto active until 6/13;
  re-evaluate 6/15.
- **AMD `swing-momentum-breakout`** -- closed-as-missed; re-arm only on fresh signal.
- **Crypto trend-follow (BTC)** -- 50/200 gap WIDE post-Fri flush; ETA past 6/20.
- **Polygon Form-4 access** -- `swing-insider-buys` remains PAUSED.
- **L4 Options reallocation default** -- Wed 05-close-summary or next-routine-fires;
  hard deadline NOW.
- **Telegram-bot / GitHub-Issues alternative notify channel** -- still owed
  on Robin's runner-fix queue (separate from L1 cron-miss). Wed routine's
  WhatsApp success shows the WAF can be worked around in the short term,
  but the underlying single-channel-outbound-only architecture remains
  fragile.

## Recent Closed Positions (last 5 LM)

1. **MSFT** (`core-buy-and-hold`) -- closed Fri 2026-06-05 16:08:05Z @ $419.40 avg,
   11 sh; realized **+$158.70 / +0.36R trail-spec**. **First WIN; cleanest trail-stop
   fill in book history; 0.07% slip vs trigger.**
2. **AVGO** (`core-buy-and-hold`) -- closed Thu 2026-06-04 13:36:31Z @ $410.882727
   avg, 11 sh; realized -$36.92 / -0.08R trail-spec. Gap-fill -7.77% on post-earnings
   beat-and-raise-rejected.
3. **GOOGL** (`core-buy-and-hold`) -- closed Tue 2026-06-02 13:33:50Z @ $361.01 avg,
   12 sh; realized -$315.72 / -0.68R trail-spec. Gap-fill -1.83% on $80B AI-share-
   issuance dilution.
4. **NVDA** (`swing-quality-pullback`) -- closed Wed 2026-05-27 15:00:34Z @ $208.95
   avg, 9 sh; realized -$99.10 / -1.0R exactly.

(4 LM closes to date; potential 5th close TODAY = RL `swing-earnings-drift`
4th-attempt liquidate at 02-market-open; modal +$45-55 = **first Swing WIN**.)

## KW 24 running tally -- Wed pre-mkt 12:09Z

- Bull equity: **$100,099.09 Fri 6/5 close -> $100,188.09 Mon close -> $100,191.77 Tue close -> $99,870.82 Wed pre-mkt** (KW 24 WTD -$228.27 / -0.228% vs 6/5 close; LM-cum -$890.90 / -0.884% vs 5/21 baseline).
- SPY: $737.55 Fri 6/5 close -> $739.22 Mon -> $735.70 Tue -> $737.05 Wed pre-mkt (KW 24 WTD -0.07% / -0.25% vs 6/5 close incl pre-mkt drift).
- **KW 24 WTD alpha (provisional, 2.5 sessions): ~+2 bp slight positive** (Bull -0.23% vs SPY -0.25%); meaningful read awaits Wed cash session post-CPI.
- **LM cum alpha (since 5/21 EOD baseline): essentially flat -- Bull -0.884% vs SPY -0.771% = -11 bp slight negative**.
- Per-sleeve KW 24 to-date attribution: Core -$405.27 (UPL Δ) / Swing +$62.15 (RL recovery) / DT $0 / Crypto $0 / Options $0.
- Top sub-strategy KW 24 to-date: **`swing-earnings-drift` RL +$62.15 UPL Δ** (PEAD late-fire on Tue consumer-rotation).
- Bottom sub-strategy KW 24 to-date: **`core-buy-and-hold` aggregate -$405.27 UPL Δ** (META compression + VOO/LLY drift).
- LM trade count: 4 closed + 0 KW 24 closes (RL pending Wed liquidate = potential 5th LM close + 1st Swing WIN).
- PDT count (5d): **0** (full budget); Options BP $74,858.26 / L3 ✓.
- **CallMeBot 5-day outage BROKEN Wed 12:09Z via single-shot short-form** (lesson L1-KW24 candidate; not yet encoded).
- **Next routine**: Wed 2026-06-10 02-market-open at 13:30Z (LM Day 21, 10 LM days remaining; 5-order execute batch + 0-2 Daytrade ORB-short entries + WhatsApp short-form attempt #2 to test 2-part-vs-1-part WAF rule).
