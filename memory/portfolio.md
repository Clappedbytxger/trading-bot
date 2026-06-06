---
last_updated: 2026-06-06T20:42:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 17 of 30 — Sat 6/6 06-weekly-review for KW 23; weekend snapshot)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates; 4 LM days remaining after today)
routine: 06-weekly-review (KW 23 Sat-slot; 5-day cron-miss cluster Mon-Fri 02/03/04/05 all missed; 3 Core trail-stops fired mechanically at broker layer)
total_value_usd: 100172.44
cash_usd: 49845.72
long_market_value_usd: 50326.72
week_pnl_usd_vs_5_29_eod: -2079.66
week_pnl_pct_vs_5_29_eod: -0.020353
prior_5_29_eod_usd: 102178.75
prior_6_05_eod_usd: 100099.09
spy_close_6_05_usd: 737.55
spy_close_5_29_usd: 756.48
spy_week_pct_kw23: -0.025024
week_alpha_bp_vs_spy: 46.71
lm_cum_pnl_usd_since_5_21_eod: -662.63
lm_cum_pnl_pct_since_5_21_eod: -0.006577
lm_cum_alpha_bp_vs_spy: 3.8
ytd_pnl_pct: 0.0990
benchmark_spx_ytd: 8.2603
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 737.55
alpha_vs_spx_ytd_pct: -8.1613
position_count_total: 10
position_count_core_active: 5
position_count_core_stub: 4
position_count_swing: 1
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.502
options_buying_power_usd: 75009.08
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
polygon_options_chain_consecutive_blocks: 12
callmebot_outage_active: true
callmebot_consecutive_503_days: 2_then_sat_attempt_pending
macro_risk_off_active: false
macro_regime: nfp_hawk_shock (Fri 6/5 NFP +172k vs +85k cons 102% beat; SPY -2.58% close; VIX +39.7% to 21.51; 10Y +6bp to 4.54%; DXY +0.49% to 99.895; futures repricing Fed-hike-by-Dec 48% → 65%)
vix_close_6_05: 21.51
market_state: closed (Fri 2026-06-05 20:00Z cash close; weekend; next_open Mon 2026-06-08T13:30Z)
next_open: 2026-06-08T13:30:00Z
---

# Portfolio — 06-weekly-review 2026-06-06 (LM Day 17 — KW 23 Sat-slot weekly review)

> **Phase note**: Sat 2026-06-06 06-weekly-review slot (KW 23). All Fri 02/03/04/05
> + all Mon-Fri 02/03/04/05 routines MISSED across KW 23 (20 missed routines this
> week; only 5 of 30 scheduled committed: Mon-Wed 01-pre-market on time + Thu+Fri
> 01-pre-market LATE FIRE). Despite the operational outage, **3 Core mechanical
> trail-stops fired at the broker layer** (GOOGL Tue $361.01 gap-fill / AVGO Thu
> $410.88 gap-fill / **MSFT Fri $419.40 CLEAN lock-in-gain — cleanest trail in
> book history**). Net realized -$193.94; Bull equity Fri 5/29 EOD $102,178.75
> → Fri 6/5 EOD **$100,099.09** = -$2,079.66 / -2.0353%. SPY -2.5024% (NFP-hawk
> Fri whoosh -2.58%) → **weekly alpha +46.71 bp POSITIVE — first since KW 20**;
> +97 bp swing from KW 22's -50 bp. **LM cum alpha now +3.8 bp** (swing +48.4 bp
> from KW 22 EOW -44.6 bp). YTD alpha gap -816 bp (improvement from -885 bp;
> +69 bp tightening). Bandit cull pre-condition PARTIALLY MET (`core-buy-and-hold`
> 3 closes but Core is benchmark sleeve, not bandit-eligible; rest below threshold)
> → **NO CULL again**. RL still open past time-stop (Fri 04-pre-close missed);
> queued for Mon 6/8 liquidate. Crypto ETH+AVAX mean-reversion triggers fired
> Fri but never executed (03-midday missed); Mon re-eval.

## Sleeve summary (Sat 6/6 20:42Z, reflecting Fri 6/5 EOD broker state + Sat re-quote)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs 5/29 EOD | Notes |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|--------------:|-------|
| Core       |  $62,000 (cost basis frozen) | $48,512.75 active + $355.66 in 4 stubs | 5 + 4 stubs | +$510.75 active + ~+$0.93 stubs net = **+$511.68** | +1.06% on active | -$1,793.96 UPL Δ + -$193.94 realized = -$1,987.90 net | 3 KW23 closes (GOOGL Tue / AVGO Thu / MSFT Fri); MSFT stub NEW post-fill; cushion-watch shifts to META 2.45% tightest |
| Swing      |  $15,000             | $1,500 (RL cost basis) | 1 (RL) + NVDA stub | -$41.69 RL + -$1.37 stub = -$43.06 | -$30.06 (UPL Δ -$53.06 → -$43.06 +$10.55) | -$53.06 → -$43.06 Δ +$10.55 ; modal Mon liquidate ~-$40 final | RL past td10 time-stop (Fri 04/05 missed); liquidate Mon 6/8 |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty 12 LM days; PDT 0/5 full budget |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0         | 2 ETH+AVAX triggers fired Fri but 03-midday missed → 0 fills; Mon re-eval (24h window expired) |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     |    $0         | Polygon chain BLOCKED 11+ routines; **L4 ESCALATION 3rd weekly ping; Mon 6/8 EOD default = reallocate to Cash** |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     |    —          | $3k earmarked of $49.85k cash |

Total deployable cash for non-Core sleeves: **$46,846** ($49,845.72 − $3,000 reserve).
Swing remaining budget after RL: **$13,500**.

## Core sleeve (5 active + 4 stubs; frozen) — Sat 6/6 20:42Z

| Symbol | Qty        | Avg Entry | Mark    | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|-----------:|----------:|--------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341  |  $675.703 | $678.00 |  $33,447.33  |  +$113.33  |  +0.34% |  33.39% | trail 10% / 49 sh GTC / HWM $699.15 / stop $629.235 / **cushion 7.18%** (was 9.81% Fri 5/29 EOD; SPY -2.50% week drag) |
| LLY    |  3.341161  |  $997.857 | $1,131.42 |  $3,780.26 |  +$446.26  | +16.40% (best in book) |   3.77% | trail 10% / 3 sh GTC / HWM **$1,166.225 (NEW ATH Fri +1.49% organic walk)** / stop $1,049.6025 / **cushion 7.23%** (was 6.41% 5/29; healthcare-defensive bid Fri) |
| META   |  7.767476  |  $600.710 | $593.00 |   $4,606.11  |   -$59.89  |  -1.28% |   4.60% | trail 10% / 7 sh GTC / HWM $643.00 / stop $578.70 / **cushion 2.45% (TIGHTEST IN BOOK)** (was 8.50% Fri 5/29 EOD; -4.19% Fri NQ-tech NFP-hawk drag) |
| V      | 10.256781  |  $325.053 | $323.57 |   $3,318.79  |   -$15.21  |  -0.46% |   3.31% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / **cushion 6.78%** (was 7.57% 5/29; flat week) |
| BRK.B  |  6.883950  |  $484.315 | $488.13 |   $3,360.26  |   +$26.26  |  +0.79% |   3.35% | trail 10% / 6 sh GTC / HWM **$491.00 (NEW Fri +0.20% organic walk)** / stop $441.90 / **cushion 9.47%** (was 7.17% 5/29; defensive bid Fri) |

**Fri 6/5 Core HWM advances (2 organic — defensive rotation Fri)**:
- **LLY**: $1,149.10 → $1,166.225 (+1.49% — new book-record ATH); stop $1,034.19 → $1,049.6025
- **BRK.B**: $489.36 → $491.00 (+0.34%); stop $440.424 → $441.90

**Fri 6/5 Core mechanical CLOSES (3 — KW 23 mechanical-stop cluster; CLOSED ROW)**:
- **GOOGL Tue 6/2 13:33:50Z**: 12 sh @ $361.01 (gap-fill -$6.74 / -1.83% vs $367.749 trigger); realized **-$315.72** / -0.68R trail-spec; $80B AI-share-issuance dilution Mon catalyst
- **AVGO Thu 6/4 13:36:31Z**: 11 sh @ $410.882727 (gap-fill -$34.62 / -7.77% vs $445.50 trigger); realized **-$36.92** / -0.08R trail-spec; post-earnings beat-and-raise-rejected -13.58% gap-down catalyst
- **MSFT Fri 6/5 16:08:05Z**: 11 sh @ $419.40 (CLEAN slip -$0.288 / -0.07% vs $419.688 trigger); realized **+$158.70** / +0.36R trail-spec; **first WIN in LM Core trail sequence; cleanest trail-stop fill in book history**

**Cushion rank (Sat 20:42Z, active Core only, tightest first)**:
1. **META 2.45%** (new tightest in book; NQ-tech NFP-hawk drawdown; next mechanical stop-candidate if NFP-hawk extends)
2. V 6.78%
3. VOO 7.18%
4. LLY 7.23%
5. BRK.B 9.47%

(MSFT no longer in active Core after Fri 11-sh stop fill; stub of 0.5218 sh remains
pending Mon 6/8 02-market-open liquidate join the 3-stub queue.)

**Fractional stubs in book (4 — queued for Mon 6/8 consolidated liquidate)**:

| Symbol | Qty | Avg | Mark | mv | UPL$ | UPL% | Liquidate attempt # | Strategy attribution finalizer |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| MSFT stub | 0.521758 | $401.40 (broker-recalc) | $416.67 | $217.40 | +$7.97 | +3.80% | 1st (NEW) | Locks `core-buy-and-hold` MSFT final at ~+$167 realized incl. stub |
| NVDA stub | 0.092513 | $219.961 | $205.10 | $18.97 | -$1.37 | -6.76% | 9th | Locks `swing-quality-pullback` final at ~-$100 realized + stub |
| GOOGL stub | 0.047273 | $387.320 | $368.53 | $17.42 | -$0.89 | -4.85% | 5th | Locks `core-buy-and-hold` GOOGL final at ~-$317 realized incl. stub |
| AVGO stub | 0.264102 | $411.295 | $385.73 | $101.87 | -$6.75 | -6.22% | 4th | Locks `core-buy-and-hold` AVGO final at ~-$44 realized incl. stub |
| Sub-total stubs | — | — | — | **$355.66** | **-$1.04** | — | — | — |

Strategy slug for 5 active + 3 Core-legacy stubs: `core-buy-and-hold`. **No new Core
entries authorized during LM** (Sleeve 1 frozen per strategy.md v3).

Total Core committed: $48,512.75 active + $355.66 stubs = **$48,868.41 (48.78% of equity)**.
KW 23 Core UPL Δ -$1,793.96 vs 5/29 EOD + realized -$193.94 = net -$1,987.90.

**Core watch items for Mon 6/8 01-pre-market**:
- **META cushion 2.45% (new tightest in book)** — next mechanical stop-candidate if NQ-tech selloff extends Mon. -4.19% Fri NFP-hawk hit; no fresh thesis-break. Monitor; accept fill if it triggers per ALM-1 + organic-broker pattern.
- **4 fractional stubs queued together for Mon 6/8 02-market-open consolidated liquidate**.
- **VOO/LLY/V/BRK.B** all holding above 6.78% cushion → routine HOLD.

## Swing sleeve (1 / 8 positions, $13,500 budget remaining) — Sat 6/6 20:42Z

| Symbol | Qty       | Avg Entry | Mark    | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held (cal / td) | Time stop | Strategy slug             |
|--------|----------:|----------:|--------:|-------------:|--------:|--------:|------:|--------:|--------------------:|----------:|---------------------------|
| RL     |  3.978463 |  $377.030 | $366.55 |  $1,458.31   | -$41.69 | -2.78% | $350.64 GTC | **4.54%** | 15 cal / 10+ td | **PAST 6/5 td10 time-stop** — Mon 6/8 liquidate queued | `swing-earnings-drift` |

**RL `swing-earnings-drift` PAST TIME-STOP** — Fri 6/5 = td10 was scheduled exit
window. Fri 04-pre-close (20:30Z) + 05-close-summary (21:15Z) both MISSED so the
position was not exited at close. Stop $350.64 GTC `OrderStatus.NEW` did NOT
trigger intraday (Fri close mark $366.55 = cushion 4.54% > stop threshold).

**Action queued for Mon 6/8 01-pre-market / 02-market-open**: MARKET SELL fractional
3.978 sh DAY. Modal final attribution -$30 to -$50 / -2 to -3.5% / -0.30R to -0.48R
clean. Acceptable per the playbook's "time-stop = neutral-bad exit" modal.

**PEAD thesis post-mortem (final)**: Original entry thesis was Q4 FY26 beat → 1-2
week drift higher. RL delivered a Tue+Wed +3.36% peak (PEAD Day 3-4 in-window), then
Thu-Fri-Mon-Tue-Wed-Thu deterioration with no fresh catalyst, then Fri NFP-cool-wages
recovery to ~-2.5% bleed. Net: PEAD fired then reversed = literature-consistent
failed-PEAD outcome. **Strategy-spec learning carryover** (deferred encoding to KW 24
EOW after realized exit confirms data point): consider adding "mid-hold
cushion-compression check at td5" rule from lesson 2026-06-04. 1 trade not enough
sample; need ≥2 more.

## Daytrade / Scalp sleeve (0 / 5; $10k budget intact)

Empty. PDT count 0/5 (full budget). 12 LM days with 0 entries. **No fills KW 23
because all Mon-Fri 02/03 routines MISSED.** ORB / VWAP / scalp triggers all
reachable on data — the absence is operational (cron-miss) more than concept.
Continue ACTIVE; re-evaluate Mon 6/8 if 02-market-open fires reliably.

## Crypto sleeve (24/7, $5k budget intact)

Empty. **2 `crypto-mean-reversion` TRIGGERS FIRED Fri 6/5 (ETH -10.87%/24h AND AVAX
-10.38%/24h crossed -10% flush threshold)** but the queued 03-midday execution
MISSED so 0 fills.

**Sat 6/6 weekend re-evaluation**: Both flushes have now extended past 48h. The
24h-flush trigger window has CLOSED. Mon 6/8 01-pre-market needs fresh signal
evaluation:
- If ETH/AVAX recovered ≥5% over weekend → opportunity-cost realized; trigger window expired.
- If ETH/AVAX extended further down → may re-fire on a fresh 24h window basis.
- BTC 50/200 cross-up gap likely WIDENED on the Fri flush; no `crypto-trend-follow` signal.

`crypto-weekend-momentum`: Fri 5/29-style trigger was Fri 6/5 21:00Z 05-close-summary
slot which MISSED — but trigger logically would NOT have fired anyway (BTC 7d
-18%, vastly below +2% threshold). Re-arm Fri 6/12 21:00Z.

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. **Polygon options-chain BLOCKED
for 11+ consecutive routines** (5/26 4th through 6/6 12th).

**L4 ESCALATION re-fires Sat 6/6 WhatsApp (3rd weekly ping)**. Two paths for Robin:
(a) Polygon Options Starter $79/mo subscription; (b) reallocate $5k premium → Cash
reserve. **Default if no reply by Mon 6/8 EOD = path (b)** (Bull will execute the
reallocation in Mon 6/8 01-pre-market memory-edit + log in `_ledger.md`).

Missed Options opportunities KW 23 (high-confidence retrospective):
- **NFP-hawk Fri SPY -2.58% protective-put**: estimated +50-80 bp on 30-DTE 5%-OTM SPY
  put bought Thu pre-NFP. Premium ~$300-500; would-be P&L +$30-60 = +10-15% return.
- **AVGO post-earnings strangle (Wed pre-print)**: AVGO -13.58% Thu vs implied move
  ~6% = textbook long-vol setup. Premium ~$800; would-be P&L +$500-1000.
- **NVDA bull-call-spread (Mon pre-flush)**: NVDA bled -3% week; protective spread
  would have produced positive convexity.

Cumulative Options-sleeve opportunity-cost KW 23 estimate: **~$300-1200 of would-be
P&L** depending on entry timing precision. This is meaningful relative to the $5k
premium budget. Robin's reply to the L4 escalation matters.

## Today's trades (Sat 6/6 — weekend; 0 trades book-wide this routine)

(none; weekend; market closed. Last broker fill was MSFT trail-stop Fri 6/5
16:08:05Z @ $419.40 +$158.70 realized. Logged in trade_log.md this routine in arrears.)

## Organic broker events KW 23

- **Tue 6/2 13:33:50Z**: GOOGL trail-stop FILLED 12 sh @ $361.01 (gap-fill -1.83%
  vs $367.749 trigger). Realized -$315.72. 1st LM Core close. Catalyst: continued
  Mon $80B AI-share-issuance dilution; GOOGL -3.86% Tue close.
- **Thu 6/4 13:36:31Z**: AVGO trail-stop FILLED 11 sh @ $410.882727 (gap-fill
  -7.77% vs $445.50 trigger). Realized -$36.92. 2nd LM Core close. Catalyst:
  post-earnings beat-and-raise-rejected -13.58% Thu gap-down ($100B 2027 AI target
  not raised; software shortfall).
- **Fri 6/5 16:08:05Z**: MSFT trail-stop FILLED 11 sh @ $419.40 (CLEAN slip
  -0.07% vs $419.688 trigger). Realized **+$158.70**. **3rd LM Core close +
  first WIN; cleanest trail-stop fill in book history**. Catalyst: NFP-hawk Fri
  systemic NQ-tech selloff (-2.13% MSFT intraday at fill time).
- **Fri 6/5 organic Core trail HWMs (2 walks Fri)**:
  - LLY: $1,149.10 → $1,166.225 (+1.49% organic, healthcare-defensive bid; new ATH)
  - BRK.B: $489.36 → $491.00 (+0.34% organic, defensive bid)

## Pending (not yet opened / re-evaluated)

- **4 fractional stubs CONSOLIDATED LIQUIDATE** — Mon 6/8 02-market-open: MSFT 1st +
  NVDA 9th + GOOGL 5th + AVGO 4th. Combined ~$355 in book; queue 4 MARKET SELL
  fractional DAY orders together.
- **RL `swing-earnings-drift` PAST TIME-STOP** — Mon 6/8 02-market-open MARKET SELL
  3.978 sh DAY; modal -$30 to -$50 realized.
- **Crypto ETH+AVAX `crypto-mean-reversion` re-evaluate** — Mon 6/8 01-pre-market:
  check 24h flush window; if expired, log opportunity-cost; if fresh signal, queue
  for 02 / 03 execution.
- **META cushion-watch 2.45%** — next mechanical Core stop-candidate if NQ-tech
  selloff extends Mon.
- **Polygon options-chain 12th re-test** — Mon 6/8 01-pre-market. If still 403 AND
  no Robin reply by Mon EOD, EXECUTE default path (b): reallocate $5k premium →
  Cash reserve.
- **L4 ESCALATION (3rd weekly ping) sent in Sat 6/6 WhatsApp** — Robin to reply
  via inbox.md by Mon EOD.
- **AAPL `swing-short-rejection`** — WWDC 6/8-12 catalyst veto active until 6/13.
- **AMD `swing-momentum-breakout`** — closed-as-missed per Thu 6/4; re-arm only on
  fresh signal (no chase).
- **Crypto trend-follow (BTC)** — 50/200 gap likely WIDENED on NFP-hawk flush; monitor.
- **Polygon Form-4 access** — `swing-insider-buys` remains PAUSED.

## Recent Closed Positions (last 5 LM)

1. **MSFT** (`core-buy-and-hold`) — closed Fri 2026-06-05 16:08:05Z @ $419.40 avg,
   11 sh; realized **+$158.70 / +0.36R trail-spec**. **First WIN; cleanest trail-stop
   fill in book history; 0.07% slip vs trigger.**
2. **AVGO** (`core-buy-and-hold`) — closed Thu 2026-06-04 13:36:31Z @ $410.882727
   avg, 11 sh; realized -$36.92 / -0.08R trail-spec. Gap-fill -7.77% on post-earnings
   beat-and-raise-rejected. Stub 0.264 sh pending Mon liquidate.
3. **GOOGL** (`core-buy-and-hold`) — closed Tue 2026-06-02 13:33:50Z @ $361.01 avg,
   12 sh; realized -$315.72 / -0.68R trail-spec. Gap-fill -1.83% on $80B AI-share-
   issuance dilution. Stub 0.047 sh pending Mon liquidate.
4. **NVDA** (`swing-quality-pullback`) — closed Wed 2026-05-27 15:00:34Z @ $208.95
   avg, 9 sh; realized -$99.10 / -1.0R exactly. Stub 0.0925 sh pending Mon liquidate.

(4 LM closes to date; Live-Phase paper run had 0 closes.)

## KW 23 EOW running tally — LOCKED at Sat 20:42Z

- Bull equity: **$100,099.09 Fri 6/5 close → $100,172.44 Sat re-quote** (-$2,079.66 / -2.0353% KW 23 vs 5/29 EOD; -$662.63 / -0.6577% LM-cum vs 5/21 EOD baseline).
- SPY KW 23: $756.48 → $737.55 = -2.5024%; SPY LM-cum: $742.72 → $737.55 = -0.696%.
- **KW 23 weekly alpha: +46.71 bp POSITIVE (first since KW 20 +60 bp; +97 bp swing from KW 22 -50 bp)**.
- **LM cum alpha: +3.8 bp (essentially flat-positive; swing +48.4 bp from KW 22 EOW -44.6 bp)**.
- Per-sleeve KW 23 attribution: **Core -$1,987.90 (realized -$193.94 + UPL Δ -$1,793.96) / Swing -$11.20 / DT $0 / Crypto $0 (opp-cost ~$50-150 ETH+AVAX missed) / Options $0 (opp-cost ~$300-1200 NFP-protective-put + AVGO strangle missed)**.
- Top sub-strategy KW 23: **`core-buy-and-hold` MSFT leg only +$158.70 realized clean lock** (only positive single-leg attribution).
- Bottom sub-strategy KW 23: **`core-buy-and-hold` aggregate net -$1,987.90** — single largest single-strategy weekly loss in book history.
- LM trade count: 4 closed (NVDA 5/27 + GOOGL 6/2 + AVGO 6/4 + MSFT 6/5) + 1 open past time-stop (RL).
- Bandit cull this week: **NO CULL** (Core 3 closes but not bandit-eligible; rest below threshold).
- PDT count (5d): **0** (full budget); Options BP $75,009.08 / L3 ✓.
- **Next routine**: Mon 2026-06-08 01-pre-market at 13:00Z (LM Day 19 of 30; 4 LM days remaining; consolidated 4-stub liquidate + RL liquidate + META cushion-watch + Polygon options-chain 12th re-test + L4 default-trigger Mon EOD if no Robin reply + crypto ETH+AVAX trigger re-eval).
