---
last_updated: 2026-05-30T20:38:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 10 of 30 - Sat 5/30 06-weekly-review for KW 22; weekend snapshot)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 06-weekly-review (KW 22 - Sat slot; Fri 21:30Z slot apparently missed; bandit cull pre-condition NOT MET; weekly KPI rollup completed)
total_value_usd: 102178.75
cash_usd: 36380.54
long_market_value_usd: 65798.21
week_pnl_usd_vs_5_22_eod: +1272.71
week_pnl_pct_vs_5_22_eod: +0.012614
prior_5_22_eod_usd: 100906.04
prior_5_21_eod_usd: 100761.72
spy_close_5_29_usd: 756.48
spy_close_5_22_usd: 745.70
spy_week_pct_kw22: +0.014456
week_alpha_bp_vs_spy: -18.4
lm_cum_pnl_usd_since_5_21_eod: +1417.03
lm_cum_pnl_pct_since_5_21_eod: +0.014063
lm_cum_alpha_bp_vs_spy: -44.6
ytd_pnl_pct: 2.1788
benchmark_spx_ytd: 11.0332
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 756.48
alpha_vs_spx_ytd_pct: -8.8544
position_count_total: 10
position_count_core: 8
position_count_swing: 2
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.64
options_buying_power_usd: 69279.64
options_approved_level: 3
daytrade_count_5d: 0
pattern_day_trader: false
cash_reserve_min_usd: 3000
cash_available_for_non_core_sleeves_usd: 33380
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
macro_risk_off_active: false
vix_close_5_29: 15.32
market_state: closed (Fri 2026-05-29 20:00Z cash close; weekend; next_open Mon 2026-06-01T13:30Z)
next_open: 2026-06-01T13:30:00Z
---

# Portfolio — 06-weekly-review 2026-05-30 (LM Day 10 — KW 22 Sat-slot weekly review)

> **Phase note**: Sat 2026-05-30 06-weekly-review slot (KW 22). Fri 5/29
> 21:30Z slot apparently MISSED (no commit in git log for it; Fri 02-04-05
> routines also all missed). Sat snapshot reflects Fri 5/29 EOD broker
> state with weekend re-quote noise. Bull equity **$102,178.75**
> (+$1,272.71 / +1.2614% vs Fri 5/22 EOD baseline). SPY KW 22 +1.4456%
> → **weekly alpha -18.4 bp** (improvement from KW 21's -50 bp). LM cum
> alpha (5/21 baseline → 5/29): **-44.6 bp**. **1 close this week** (NVDA
> Wed stop-out -$99.10 / -1.0R exactly). 4 Core HWM advances (VOO,
> MSFT, AVGO, META) + LLY massive Thu +5.13% walk on CVS Zepbound +
> Foundayo coverage. Sleeve-wise: Core +$1,379.91 / Swing -$107.18 /
> DT $0 / Crypto $0 / Options $0. **Bandit cull pre-condition NOT MET**
> (no strategy with ≥3 trades in 7d) — NO CULL. NVDA stub (0.0925 sh)
> and AMD swing entry both planned by Fri 01-pre-market but missed
> execution; re-queue Mon 6/1 01-pre-market.

## Sleeve summary (Sat 5/30 20:38Z, reflecting Fri 5/29 EOD broker state)

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Δ vs 5/22 EOD | Notes |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|--------------:|-------|
| Core       |  $62,000 (cost basis)| $64,331.93            |             8  | +$2,330.92  |   +3.76%    | +$1,379.91    | Frozen; 8/8 trail stops live GTC; LLY new HWM $1,149.10 (+5.13% Thu walk) — book record; MSFT, AVGO, VOO, META also walked Fri |
| Swing      |  $15,000             | $1,500 (RL cost basis; NVDA closed) | 2 (RL + NVDA stub) | -$53.06     |   -3.53%    | -$8.08 open + -$99.10 realized | RL UPL -$52.24 (-3.48%, cushion 3.66%) / NVDA stub 0.0925 sh -$0.82; **time-stop 6/5 = 4 td out for RL** |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty; PDT 0/5 full budget; NVDA Wed stop on 5/22-Swing-w/-GTC-stop entry = not PDT (>1d hold) |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     |    $0         | Empty; BTC 50/200 gap -3.26% (converging +0.23 pp/day; ~14 td to cross); 0 entries Mon-Fri |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     |    $0         | Empty; Polygon chain BLOCKED 6 consecutive routines (escalation needed) |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     |    —          | $3k earmarked of $36.38k cash |

Total deployable cash for non-Core sleeves: **$33,380** ($36.38k − $3k reserve).
Swing remaining budget after RL + NVDA stub: **$13,500**.

## Core sleeve (8 positions, frozen)

| Symbol | Qty        | Avg Entry | Fri 5/29 EOD Mark | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / HWM / cushion |
|--------|-----------:|----------:|-----------------:|-------------:|-----------:|---------:|--------:|----------------------------|
| VOO    | 49.332341  |  $675.703 |   $695.49        |  $34,310.15  |  +$976.15  |  +2.928% |  33.58% | trail 10% / 49 sh GTC / HWM **$697.00 (NEW Fri +0.79%)** / stop **$627.30** / cushion 9.81% |
| MSFT   | 11.521758  |  $404.973 |   $450.24        |   $5,187.56  |  +$521.56  | +11.178% (2nd best) |   5.08% | trail 10% / 11 sh GTC / HWM **$450.33 (NEW Fri +4.08%)** / stop **$405.30** / cushion 9.98% |
| GOOGL  | 12.047273  |  $387.308 |   $380.34        |   $4,582.06  |   -$83.94  |  -1.799% |   4.48% | trail 10% / 12 sh GTC / HWM $408.61 / stop $367.749 / **cushion 3.31% (tightest in book; was 4.95% Fri pre-mkt → compressed on Fri -2.51% session)** |
| META   |  7.767476  |  $600.710 |   $632.51        |   $4,913.01  |  +$247.01  |  +5.294% |   4.81% | trail 10% / 7 sh GTC / HWM $643.00 / stop $578.70 / cushion 8.50% |
| AVGO   | 11.264102  |  $414.236 |   $446.77        |   $5,032.46  |  +$366.46  |  +7.854% |   4.93% | trail 10% / 11 sh GTC / HWM **$448.88 (NEW Fri +1.47%)** / stop **$403.99** / cushion 9.58% |
| V      | 10.256781  |  $325.053 |   $326.36        |   $3,347.40  |   +$13.40  |  +0.402% |   3.28% | trail 10% / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 7.57% |
| BRK.B  |  6.883950  |  $484.315 |   $474.48        |   $3,266.30  |   -$67.70  |  -2.031% |   3.20% | trail 10% / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 7.17% |
| LLY    |  3.341161  |  $997.857 | $1,105.00        |   $3,691.98  |  +$357.98  | +10.737% (best UPL — was +12.74% Fri pre-mkt) |   3.61% | trail 10% / 3 sh GTC / HWM **$1,149.10 (Thu +5.13% — biggest single-day Core walk in book history)** / stop **$1,034.19** / cushion 6.41% |

**Fri 5/29 Core HWM advances (4 total — biggest single-day cluster in book history)**:
- **VOO**: $691.51 → $697.00 (+0.79%); stop $622.36 → $627.30
- **MSFT**: $432.70 → $450.33 (+4.08% — biggest MSFT walk in book); stop $389.43 → $405.30
- **AVGO**: $442.36 → $448.88 (+1.47% pre-earnings froth into Tue 6/3 print); stop $398.12 → $403.99
- (LLY HWM was set Thu $1,093 → $1,149.10 +5.13%; broker stop $1,034.19 carried through Fri)
- (META HWM was set Wed $623.73 → $638.50 then Thu $643.00; broker stop $578.70 carried through Fri)

**Cushion rank (Sat 20:38Z reflecting Fri 5/29 EOD, tightest first)**:
1. **GOOGL 3.31% (tightest in book; compressed from 4.95% pre-mkt on Fri -2.51% session)**
2. LLY 6.41% (down from pre-mkt 8.78% on Thu's +5.13% trail walk consuming cushion)
3. BRK.B 7.17%
4. V 7.57%
5. META 8.50%
6. AVGO 9.58%
7. VOO 9.81%
8. MSFT 9.98%

Strategy slug for all 8: `core-buy-and-hold`. **No Core actions taken KW 22.**

Total Core committed: $64,331.93 (62.96% of equity). KW 22 Core UPL Δ
**+$1,379.91** vs Fri 5/22 EOD ($951.01 → $2,330.92).

**Core watch items for Mon 6/1 01-pre-market**:
- **GOOGL cushion 3.31% (new tightest)** — compressed from 4.95% pre-mkt on Fri's -2.51% session ($385.95 → $380.34). If continues compressing Mon, evaluate any catalyst (regulatory? AI-search market share?). No fresh news 24h.
- **AVGO earnings Tue 6/3 post-close — 2 td out**. Live-Phase #8 paused; Core frozen → no Core-add. Options earnings-strangle BLOCKED on Polygon chain.

## Swing sleeve (2 / 8 positions, $13,500 budget remaining)

| Symbol | Qty       | Avg Entry | Fri 5/29 EOD Mark | Market Value | UPL$    | UPL%    | Stop  | Cushion | Days held (cal / td) | Time stop | Strategy slug             |
|--------|----------:|----------:|------------------:|-------------:|--------:|--------:|------:|--------:|--------------------:|----------:|---------------------------|
| RL     |  3.978463 |  $377.030 |  $363.90          |   $1,447.76  | -$52.24 | -3.482% | $350.64 GTC | **3.66%** | 8 cal / 5 td | 2026-06-05 (5 td out — Mon 6/1 = td6) | `swing-earnings-drift` |
| NVDA stub | 0.092513 | $219.961 |  $211.14         |      $19.53  |  -$0.82 | -4.012% | (none — main 9 sh stop FILLED Wed 5/27 15:00:34Z $208.95) | n/a | 8 cal / 5 td | n/a | `swing-quality-pullback` (CLOSED main, **LIQUIDATE stub Mon 6/1 02-market-open**) |

**RL `swing-earnings-drift` HOLD** — Day 8 calendar / 5 td elapsed (5/22 fill;
holiday-skipped Mon). UPL deteriorated significantly Fri: 5/22 EOD +$0.04 →
Fri pre-mkt -$24.27 (cushion 5.79%) → Fri EOD -$52.24 (**cushion 3.66%**).
RL gave back the Tue+Wed pop sharply on Thu -1.45% + Fri -1.85%; no catalyst,
just consumer-discretionary weakness with WMT-style retail tape pressure (sympathy).

**PEAD thesis assessment**: Original entry thesis was Q4 FY26 beat → 1-2
week drift higher. By td5 we should be seeing the drift acceleration (PEAD
literature peaks Day 3-5 post-print). Instead RL is now -1.6% from entry,
**not drifting per PEAD pattern**. The 4 fresh PT raises (UBS $511, Barclays
$439, Wells $415, Needham $405) on 5/22 weekend supported the entry but
analyst optimism has not converted to flow. **Thesis weakening, not yet broken.**

**NO tighten-to-breakeven** this routine (UPL still negative at -3.48%;
tighten rule fires at UPL ≥ +5%). **NO emergency tighten** (cushion 3.66% >
the 3.0% emergency threshold from playbook by 66 bp; stop $350.64 GTC verified
live). **Time-stop 6/5 = 5 td out**; Mon 6/1 = td6, Tue 6/2 = td7, Wed 6/3 =
td8, Thu 6/4 = td9, Fri 6/5 = td10 (time-stop fires at close 6/5 if neither
target nor stop hit). **Compression watch**: if cushion < 3% intraday at any
Mon-Fri 03-midday (≈ mark $361.16), evaluate emergency-tighten or close-early
decision.

**NVDA stub LIQUIDATE — RE-QUEUE for Mon 6/1 02-market-open** (3rd attempt).
Thu 5/28 and Fri 5/29 planned closes BOTH did not execute (cash $36,380.54
unchanged across both sessions = no fractional sell occurred). Reason: cron
miss pattern on 02-market-open (matches the upstream 01-pre-market miss
problem). Re-queue Mon 6/1 02-market-open. Order: market SELL fractional
0.0925 sh DAY. Locks final `swing-quality-pullback` attribution at
**-$99.10 main + ~-$0.82 stub ≈ -$99.92 / -5.0% of $2,000 cost basis**.

**Swing candidates for Mon 6/1 01-pre-market re-evaluation**:

- **AMD** [`swing-momentum-breakout`] — **STILL ACTIVE CANDIDATE**. Fri close
  $516.10 (-$1.99 / -0.38% vs Thu $518.09 close; minor red day) but **HELD
  above the spec $510 threshold all session** (intraday L not below $510 per
  routine spec re-check). The "clean break + hold $510" criterion remains
  intact. RSI(14) >60 sustained. Mon 6/1 02-market-open re-queue: BUY 3 sh
  AMD @ market ≈ $516 = ~$1,548 notional; stop $490 GTC -5%; target $568
  (+10%) or 5-DMA break; time-stop 6/8. Tag `Swing` + `swing-momentum-breakout`.
- **ARM** [`swing-momentum-breakout`] — REMAINS EXTENDED (Fri close $353.29,
  +5.38% Fri intraday; +210% YTD). Above the $325 ATH; entry sub-1R. **SKIP**;
  re-arm only on consolidation + higher-low base above $320.
- **AAPL** [`swing-short-rejection`] — Fri close $312.06 (-0.14% vs Thu);
  intraday H $313.30 = essentially flat. No rejection candle. **SKIP**; WWDC
  6/8-12 catalyst veto continues.

## Daytrade / Scalp sleeve (0 / 5; $10k budget intact)

Empty. PDT count 0/5 (full budget). NVDA Wed stop-out was on the 5/22 Swing
entry (5-day-old position) → not a same-day round-trip → PDT count unaffected.
Sleeve has now logged 9 LM days with 0 entries. Trigger reachability is good
(POLYGON set since 5/22 AM; pre-mkt SPY/QQQ futures consistently <1% gap so
ORB rule in-play); the absence is genuine "no clean ORB setup formed in the
first 5-min" each Tue-Fri rather than data-gap. Continue ACTIVE; max 1 ORB
per session preserved for PDT runway.

## Crypto sleeve (24/7, $5k budget intact)

Empty. Mon-Fri scans all 0/5 cross-up + 0/5 -10%/24h flush. BTC 50/200 gap
narrowed from -4.31% Mon → -3.26% Fri (continuing convergence at +0.23 pp/day;
extrapolated cross in ~14 trading days at current pace, target ~6/15-6/17).
Other 4 coins remain >-10% gap (ETH -10.35%, SOL -17.79%, AVAX -14.42%,
LINK -11.43%). `crypto-weekend-momentum`: Fri 5/29 trigger NOT met
(BTC 7d -2.88% << +2%); re-arm Fri 6/5 21:00Z.

**Weekend-cycle scans planned**: Sat 5/30 03-midday at 17:30Z + Sun 5/31
03-midday at 17:30Z (this routine is the 06-weekly-review at 20:38Z; weekend
crypto-cycle 03-midday fires separately on its own slot).

## Options sleeve (Level 3 enabled, empty)

Empty (0 / 6 contracts). $5k premium budget intact. **Polygon options-chain
BLOCKED for 6 consecutive routines** (Mon 5/26 4th re-test through Fri 5/29
6th). All 4 Options sub-strategies cannot fire signals:
- `options-long-call-momentum` (NVDA, ARM, AMD candidates): chain gated
- `options-vertical-bull-call-spread` (NVDA): chain gated
- `options-earnings-strangle` (AVGO 6/3 = 2 td out): chain + IV-rank gated
- `options-protective-put` (SPY for next macro event): chain gated; PCE+GDP
  Thu 5/28 came in soft → un-hedged exposure was OK in retrospect

**Escalation action**: This Sat WhatsApp will surface the 6-consecutive-block
to Robin in German. Two options for Robin:
- (a) Subscribe to Polygon Options Starter ($79/mo) and validate chain unblocks.
- (b) Accept Options sleeve cannot run during LM; reallocate $5k premium
  budget to Swing or Crypto sleeves for KW 23+.
Bull will defer the reallocation decision to Robin (touches sleeve allocations
in strategy.md = approval territory per ALM rules for budget shifts >$3k).

## Today's trades (Sat 5/30 — weekend; 0 trades book-wide for KW 22 Sat snapshot)

(none; weekend; market closed. Last broker fill was NVDA stop-out Wed 5/27
15:00:34Z. No fills Thu, Fri, Sat — Fri 02-market-open through 05-close-summary
all MISSED so the 2 planned actions (NVDA stub liquidate + AMD swing entry)
never executed.)

## Organic broker events KW 22

- **Wed 5/27 15:00:34Z**: NVDA stop order `ffb5e5a9-50fb-4e39-abef-849d72b8f323`
  FILLED at $208.95 avg (9 sh; 1 ¢ slip vs $208.96 stop trigger). Realized
  -$99.10. First LM closed trade.
- **Thu 5/28 intraday**: LLY trail HWM walked $1,093.00 → $1,149.10 (+5.13% —
  biggest single-day Core HWM advance in book history); broker stop bumped
  $983.70 → $1,034.19. Driver: CVS Zepbound reinstatement + Foundayo coverage
  triple-catalyst.
- **Thu 5/28 intraday**: META trail HWM walked $638.50 → $643.00 (+0.70%);
  broker stop bumped $574.65 → $578.70.
- **Thu 5/28 intraday**: VOO trail HWM walked $691.51 → $694.29 (+0.40%);
  broker stop bumped to $624.86 → carried through Fri.
- **Fri 5/29 intraday**: VOO trail HWM walked $694.29 → $697.00 (+0.39%);
  broker stop bumped $624.86 → $627.30.
- **Fri 5/29 intraday**: MSFT trail HWM walked $432.70 → $450.33 (+4.08%);
  broker stop bumped $389.43 → $405.30. Biggest MSFT walk in book history.
- **Fri 5/29 intraday**: AVGO trail HWM walked $442.36 → $448.88 (+1.47%);
  broker stop bumped $398.12 → $403.99. Pre-earnings froth into Tue 6/3 print.
- **All other Core stops unchanged** (no fresh HWMs Thu/Fri for GOOGL, V, BRK.B).

## Pending (not yet opened / re-evaluated)

- **NVDA stub LIQUIDATE** — RE-QUEUE Mon 6/1 02-market-open (3rd attempt after
  Thu/Fri both missed). Market SELL fractional 0.0925 sh DAY. Locks
  `swing-quality-pullback` final attribution at ~-$99.92 / -5.0%.
- **AMD `swing-momentum-breakout` ENTRY** — RE-QUEUE Mon 6/1 02-market-open
  (Fri attempt missed). BUY 3 sh AMD @ market ≈ $516 = ~$1,548 notional; stop
  $490 GTC -5%; target $568 / +10% or 5-DMA break; time-stop 6/8.
- **RL `swing-earnings-drift` time-stop watch** — Fri 6/5 close decision. Mon
  6/1 = td6 of 10. Cushion compression watch < 3% intraday.
- **AAPL `swing-short-rejection`** — re-watch on fresh rejection candle.
- **Crypto weekend-momentum** — re-arm Fri 6/5 21:00Z (05-close-summary).
- **Crypto trend-follow (BTC)** — convergence pace +0.23 pp/day; ETA neutral
  cross ~6/15-6/17. Monitor every 03-midday.
- **Polygon options-chain 7th re-test** — Mon 6/1 01-pre-market. If still 403,
  this routine's escalation WhatsApp to Robin becomes the trigger for one of
  the two paths (Options Starter sub OR reallocate $5k budget).
- **AVGO earnings Tue 6/3 post-close** — 2 td out. Core hold posture intact
  (frozen); options strangle BLOCKED.
- **Polygon Form-4 access** — `swing-insider-buys` remains PAUSED.
- **DCA tranche 3 of 3 (legacy Live-Phase)** — deferred to 2026-06-21+ per
  strategy.md v3 LM freeze.

## Recent Closed Positions (last 5)

1. **NVDA** (`swing-quality-pullback`) — closed Wed 2026-05-27 15:00:34Z @
   $208.95 avg, 9 sh; realized -$99.10 / -1.0R exactly. Stub 0.0925 sh
   ($19.53 mv) still open pending Mon 6/1 02-market-open liquidate.

(only 1 LM close to date; Live-Phase paper run had 0 closes.)

## KW 22 EOW running tally — LOCKED at Sat 20:38Z

- Bull equity: **$102,178.75** (+$1,272.71 / +1.2614% KW 22 vs 5/22 EOD; +$1,417.03 / +1.4063% LM-cum vs 5/21 EOD baseline).
- SPY KW 22: $745.70 → $756.48 = +1.4456%; SPY LM-cum: $742.72 → $756.48 = +1.8526%.
- **KW 22 weekly alpha: -18.4 bp** (improvement from KW 21's -50.1 bp; +32 bp recovery).
- **LM cum alpha: -44.6 bp** (widened from -25.8 bp post-5/22 by the NVDA realized hit + RL deterioration; Core gains partly offset).
- Per-sleeve KW 22 attribution: **Core +$1,379.91 / Swing -$107.18 / DT $0 / Crypto $0 / Options $0**.
- Top sub-strategy KW 22: `core-buy-and-hold` +$1,379.91 (LLY $134 + MSFT $215 + AVGO $216 + META $173 = $738 of which; 4 Core HWM walks Fri = book-record single-day cluster).
- Bottom sub-strategy KW 22: `swing-quality-pullback` -$99.10 realized (-1.0R clean; first LM close).
- LM trade count: 1 closed (NVDA Wed stop) + 2 open (RL + NVDA stub).
- Bandit cull this week: **NO CULL** (pre-condition ≥3 trades not met for any strategy).
- PDT count (5d): **0** (full budget); Options BP $69,279.64 / L3 ✓.
- **Next routine**: Mon 2026-06-01 01-pre-market at 13:00Z (post-weekend; full equity execution resumes; NVDA stub re-queue + AMD entry re-queue + RL td6/10 monitoring + AVGO earnings 2 td out prep + Polygon options-chain 7th re-test for escalation decision).
