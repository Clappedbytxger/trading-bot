# Experiments Ledger — Learning Month KPIs

Updated by `05-close-summary` daily and `06-weekly-review` weekly. The week-end
strategy-bandit (kill worst, double best) consumes this table.

Window: 2026-05-21 → 2026-06-20.

## How KPIs are computed
- **Trades**: count of closed trades attributable to this strategy.
- **Win-rate**: closed trades with P&L > 0 / closed trades.
- **Avg R**: mean of (P&L / initial-risk) across closed trades. Positive = net gain on R basis.
- **Max DD**: largest peak-to-trough equity drawdown attributable to this strategy.
- **Net P&L**: cumulative $ realized + unrealized.
- **Alpha vs SPY**: strategy daily-return mean - SPY daily-return mean over same window.
- **Cost basis**: budget allocated by sleeve.
- **Risk-adj return (RAR)**: Net P&L / |Max DD|. Used for weekly bandit ranking.

## Ledger

| Strategy slug | Sleeve | Status | Trades | Win-rate | Avg R | Net P&L | Max DD | RAR | Alpha vs SPY | Last update |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| core-buy-and-hold          | Core      | active | **2 closed (GOOGL Tue 6/2 stop -$315.72 / -1.36R-cushion-anchor; AVGO Thu 6/4 stop -$36.92 / -0.08R-trail-anchor)** + 6 active + 3 stubs pending liquidate | — | — | +UPL Thu intraday for 6 active ~$1,905; realized -$352.64 cum (GOOGL -$315.72 + AVGO -$36.92) | -$315.72 (GOOGL gap-fill peak); -$917 from Wed UPL on AVGO give-back if anchored to last-day cushion | — | LM cum tracking deferred to 05-close-summary | 2026-06-04 01-pre-market |
| swing-momentum-breakout    | Swing     | active | 0 (AMD trigger DROPPED-AS-MISSED Thu 6/4 after 4 consecutive cron-miss entry days Fri 5/29 + Mon 6/1 + Tue 6/2 + Wed 6/3; Thu trigger weakened with intraday breach $499.87 of $510 spec; ARM SKIP -5.96% Thu purge; AAPL no rejection WWDC ahead) | — | — | $0.00 (opportunity-cost ~$60 missed Wed open) | $0 | — | — | 2026-06-04 01-pre-market |
| swing-mean-reversion       | Swing     | active | 0 (1 SKIP = INTU thesis-risk; no fresh triggers KW 22 — slow-grind-up tape disfavors mean-reversion) | — | — | $0.00 | $0 | — | — | 2026-05-30 06-weekly-review |
| swing-quality-pullback     | Swing     | active | **1 CLOSED (NVDA stop-out Wed 5/27 @ $208.95; -$99.10 / -1.0R exactly) + stub 0.0925 sh pending Mon 6/1 liquidate** | 0 / 1 | -1.0R | -$99.10 realized + -$0.82 stub UPL = ~-$99.92 final | -$99.10 | -1.0 | — | 2026-05-30 06-weekly-review |
| swing-earnings-drift       | Swing     | active | **1 open (RL); td10 TIME-STOP at Fri 6/5 close; cushion RECOVERED to 4.82% Fri intraday (HOLD into close per Option C)** | — | — | -$37.76 UPL (Fri 6/5 ~15:39Z intraday; UPL -2.52%); +$31.11 recovery from Thu on NFP-consumer-discretionary positive | $0 (no closes; close pending 04-pre-close 20:30Z) | — | — | 2026-06-05 01-pre-market |
| swing-insider-buys         | Swing     | paused | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-short-rejection      | Swing     | active | 0 (AAPL WATCH 5/26/27/28/29; no rejection candle in any session — closed >open each day) | — | — | $0.00 | $0 | — | — | 2026-05-30 06-weekly-review |
| swing-short-fundamental    | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-orb               | Daytrade  | active | 0 (POLYGON set since 5/22 AM; ORB rule in-play Tue-Fri at gap <1%; no clean breakouts in first 5-min) | — | — | $0.00 | $0 | — | — | 2026-05-30 06-weekly-review |
| daytrade-vwap-pullback     | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-gap-fade          | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-gap-go            | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| scalp-tape                 | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-news-catalyst     | Daytrade  | active | 0 (PCE+GDP Thu 5/28 was the KW 22 candidate event but Thu 02-market-open / news-react window not utilized; PCE came in-line / SPY +0.55% to ATH so the catalyst pattern fired benignly) | — | — | $0.00 | $0 | — | — | 2026-05-30 06-weekly-review |
| crypto-trend-follow        | Crypto    | active | 0 (BTC 50/200 gap converging -4.31% Mon → -3.26% Fri at +0.23 pp/day; ETA cross 6/15-6/17 at current pace; no entries triggered KW 22) | — | — | $0.00 | $0 | — | — | 2026-05-30 06-weekly-review |
| crypto-weekend-momentum    | Crypto    | active | 0 (Fri 5/29 trigger NOT met: BTC 7d -2.88% << +2%; closed; re-arm next Fri 6/5 21:00Z) | — | — | $0.00 | $0 | — | — | 2026-05-30 06-weekly-review |
| crypto-mean-reversion      | Crypto    | active | **0 fills; 2 TRIGGERS FIRED Fri 6/5 (ETH -10.87% AND AVAX -10.38% / 24h); queued for 03-midday 17:30Z execution at $1.5k each = $3k total / 60% of $5k sleeve** | — | — | $0.00 (pending fills) | $0 | — | — | 2026-06-05 01-pre-market |
| options-long-call-momentum | Options   | active | 0 (Polygon chain BLOCKED 11 consecutive routines incl Fri 6/5; NVDA conviction routed via Swing equity stopped Wed 5/27 -1R) | — | — | $0.00 | $0 | — | — | 2026-06-05 01-pre-market |
| options-protective-put     | Options   | active | 0 (Polygon chain BLOCKED 11x; **Fri 6/5 NFP-hawk SPY -1.37% would have been textbook protective-put profit ~30-50 bp; chain inaccessibility = direct cost**) | — | — | $0.00 | $0 | — | — | 2026-06-05 01-pre-market |
| options-vertical-bull-call-spread | Options | active | 0 (Polygon chain BLOCKED 11x) | — | — | $0.00 | $0 | — | — | 2026-06-05 01-pre-market |
| options-earnings-strangle  | Options   | active | 0 (AVGO 6/3 missed long-vol opportunity Thu 6/4 -13.58% gap; Polygon chain BLOCKED 11x; IV-rank stub returns None) | — | — | $0.00 | $0 | — | — | 2026-06-05 01-pre-market |
| options-cash-secured-put   | Options   | paused | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |

## Sleeve roll-ups

| Sleeve | Cash Budget | Used | Open positions | Cumulative P&L | Cumulative Alpha vs SPY |
|---|---:|---:|---:|---:|---:|
| Core     | $62,000 | $64,331.93 (Fri 5/29 EOD; +$2,330.92 UPL) | 8 | +$2,330.92 / +3.76% (10-day Live-Phase + LM Day 1-9 Fri EOD; LLY +10.74% / MSFT +11.18% / AVGO +7.85% / META +5.29% / VOO +2.93% lead) | LM-window: Bull +1.41% vs SPY +1.85% → **-44.6 bp** |
| Swing    | $15,000 | $1,500 (RL cost basis; NVDA closed Wed) | 2 (RL active + NVDA stub pending liquidate) | -$99.10 realized + -$0.82 stub + -$52.24 RL = **-$152.16 net** (UPL incl. realized) | — |
| Daytrade | $10,000 | $0      | 0 | $0 | — (PDT 0/5d full budget; 0 entries across 9 LM days) |
| Crypto   | $5,000  | $0      | 0 | $0 | — (BTC convergence -3.26% Fri; ~14 td to neutral at +0.23 pp/day pace) |
| Options  | $5,000  | $0      | 0 | $0 | — (Polygon chain BLOCKED 6 consecutive routines; **ESCALATION needed**) |
| Cash reserve | $3,000 | — (of $36,381 cash total, ≥$3k reserved per ALM-2) | — | — | — |

## Weekly bandit log (06-weekly-review writes here)

### 2026-05-30 (Sat-slot 06-weekly-review for KW 22) — **NO CULL** (pre-condition not met)

- **Window**: Mon 5/25 → Fri 5/29 (4 trading days; Mon Memorial Day holiday).
- **Pre-condition check**: Routine spec requires ≥3 trades per strategy in the
  trailing 7d. **NOT MET** — strategy trade counts:
  - `swing-quality-pullback`: 1 closed (NVDA stop Wed) — below threshold
  - `swing-earnings-drift`: 0 closed, 1 open (RL) — below threshold
  - `core-buy-and-hold`: 0 fills (Core frozen) — below threshold + not bandit-eligible
  - All other 19 sub-strategies: 0 trades — below threshold
- **Decision**: Skip kill / scale / budget re-allocation again. Sleeve budgets
  remain at initialized values (Core $62k, Swing $15k, Daytrade $10k, Crypto $5k,
  Options $5k, Cash $3k reserve). Status of all 22 sub-strategies UNCHANGED
  from playbook v1 initialization.
- **Why we cannot soft-cull anyway** (despite KW 22 being labeled "first eligible bandit cull"):
  - The 1-trade `swing-quality-pullback` close is a clean -1.0R fill, not a
    strategy failure — the stop fired exactly as designed. A 1-trade sample
    doesn't distinguish "bad strategy" from "bad single trade".
  - Sleeve activation is the gating constraint, not strategy concept: Options
    blocked 6 consecutive routines on Polygon chain; Daytrade had no clean
    ORB setups; Crypto market not offering -10% flushes or 50/200 cross-ups.
  - The right action this week is to **fix activation barriers** (Polygon
    options-chain escalation, encoded in WhatsApp), not to cull strategies.
- **Next eligible bandit cull**: Fri 2026-06-05 / Sat 2026-06-06 (KW 23 EOW).
  By then RL will have time-stopped on 6/5; AMD/ARM re-attempts may have fired;
  AVGO earnings 6/3 will provide options-strangle data IF chain unblocks.

### Weekly KPI roll-up — KW 22 (week ending Fri 2026-05-29, broker-basis)

- Bull week: $100,906.04 (Fri 5/22 EOD) → $102,178.75 (Fri 5/29 EOD) = **+$1,272.71 / +1.2614%**
- SPY week: $745.70 (5/22 EOD) → $756.48 (5/29 EOD) = **+1.4456%**
- **Weekly alpha: -18.4 bp** (improvement from KW 21's -50.1 bp; +32 bp recovery)
- LM cumulative (since 5/21 EOD baseline): **+$1,417.03 / +1.4063% equity / -44.6 bp alpha vs SPY**
- YTD: Bull +2.179% vs SPY +11.033% → **YTD alpha -885 bp** (improvement from -857 bp; +28 bp YTD-gap tightening)
- Max equity intra-week: $102,219.92 (broker last_equity Fri 5/29 close)
- Min equity intra-week: $100,901.97 (Tue 5/26 pre-open; carryover Mon holiday)
- Peak-to-trough drawdown intra-week: -0.0% (monotonic up after holiday)
- VIX range: 15.32 → 17.01; EOD 5/29 = **15.32** (broke below 16 first time in 2 weeks; firm risk-on)
- Total trades book-wide: 1 close (NVDA Wed stop-out)
- PDT day-trade count Fri EOD: 0/5 (Wed stop on Swing-w/-GTC-stop entry from 5/22 = not a same-day round-trip; Thu 5/23 broker rollover holds)

### Per-sleeve P&L attribution (KW 22)

| Sleeve     | Days active | Trades | Realized $ | Open UPL Δ (Fri 5/29 vs Fri 5/22) | Net P&L attribution |
|------------|------------:|-------:|-----------:|----------------------------------:|--------------------:|
| Core       | 4 (Tue-Fri; Mon holiday)  | 0      |  $0        | +$1,379.91 (UPL $951.01 → $2,330.92) | **+$1,379.91** |
| Swing      | 4         | 1 close | -$99.10   | -$8.08 (open UPL -$44.98 → -$53.06)  | **-$107.18**  |
| Daytrade   | 4         | 0      |  $0        | $0                                  | $0           |
| Crypto     | 4         | 0      |  $0        | $0                                  | $0           |
| Options    | 4         | 0      |  $0        | $0                                  | $0           |
| **Total**  | —         | 1      | -$99.10    | **+$1,371.83**                      | **+$1,272.71** (match: broker Δ $1,272.71; reconciliation noise $0.02) |

**Best sub-strategy KW 22**: `core-buy-and-hold` (+$1,379.91 UPL Δ — sole positive contributor; 4 Core HWM advances Fri = book-record single-day cluster: VOO $691.51→$697 / MSFT $432.70→$450.33 / AVGO $442.36→$448.88 / META $623.73→$643. LLY Thu walk $1,093→$1,149.10 = book-record single-day +5.13%).

**Worst sub-strategy KW 22**: `swing-quality-pullback` (-$99.10 realized + -$0.82 stub UPL ≈ -$99.92 final). First LM closed trade; stop fired cleanly at -5% / -1.0R exactly; no slippage of consequence. Stub liquidate re-queued Mon 6/1.

**Strategies with 0 trades in 7d**: 19 of 22 (Crypto + Daytrade + Options
sleeves entirely + 5 of 8 Swing sub-strategies). Per routine spec, "review
whether trigger is reachable":
- POLYGON-dependent Swing (5 strategies, all set since 5/22 AM): triggers
  REACHABLE — confirmed (Wed AMD touched $510; Wed ARM exceeded $310; Thu/Fri
  AMD breakout). Tape is offering setups; **02-market-open cron miss on Fri
  5/29 prevented the Fri AMD entry from firing**. Keep ACTIVE.
- Polygon-options-chain-dependent (4 Options strategies): triggers STILL not
  reachable — 6 consecutive 403. **ESCALATION trigger fires Sat 5/30 WhatsApp**
  (sub Options Starter OR reallocate $5k budget; Robin to decide via inbox.md).
- Crypto trend-follow + mean-reversion: triggers reachable; market not
  offering setups (50<200 across all 5 coins; 24h flushes all <2%). Keep
  dormant — this is tape, not concept.
- Crypto weekend-momentum: trigger reachable; Fri 5/29 BTC 7d -2.88% << +2%
  → NOT fired. Re-arm Fri 6/5 21:00Z.
- `swing-mean-reversion`, `swing-short-rejection`, `swing-short-fundamental`:
  triggers reachable; slow-grind-up tape disfavors mean-reversion + shorts.
  Keep dormant.
- `swing-insider-buys`: still PAUSED (Polygon Form-4 not in base tier).
- `options-cash-secured-put`: still PAUSED.

### 2026-05-23 (Sat-slot 06-weekly-review for KW 21) — **NO CULL** (pre-condition not met)

- **Window**: Mon 5/18 → Sat 5/23 (5 trading days; 3 Live-Phase HOLD + 2 LM Day 1-2 + Sat weekend).
- **Pre-condition check**: Routine spec requires ≥1 full week of LM data and
  ≥3 trades per strategy in the trailing 7d. **NOT MET** — only 2 LM trading
  days have occurred (5/21 + 5/22); no strategy has ≥3 trades; `swing-quality-
  pullback` and `swing-earnings-drift` each have 1 open trade with $0 realized P&L.
- **Decision**: Skip kill / scale / budget re-allocation. Sleeves remain at
  initialized budgets (Core $62k, Swing $15k, Daytrade $10k, Crypto $5k,
  Options $5k, Cash $3k reserve). Status of all 22 sub-strategies unchanged
  from playbook v1 initialization (5/20).
- **First eligible bandit cull**: Fri 2026-05-29 21:30Z OR Sat 2026-05-30 (KW
  22 EOW) — first full LM week with realistic per-strategy KPI sample.
- **Reference for next week's bandit**: "Top by RAR" candidates are the
  Swing strategies that have already touched the tape (`swing-quality-
  pullback`, `swing-earnings-drift`); they will have either closed exits or
  open UPL with meaningful sample by 5/29. "Bottom by RAR" candidates are
  the Daytrade strategies that haven't generated a single signal in
  ~10 trading days under POLYGON_unset → POLYGON_set transition — but
  attribution there is operational (data gap) more than strategy (concept gap),
  and the bandit should account for that.

### Weekly KPI roll-up — KW 21 (week ending Fri 2026-05-22, broker-basis)

- Bull week: $100,522.33 (5/15 broker EOD) → $100,906.04 (5/22 broker EOD) = **+$383.71 / +0.382%**
- SPY week: $739.17 (5/15 EOD) → $745.70 (5/22 EOD) = **+0.883%**
- **Weekly alpha: -50.1 bp** (regression from KW 20's +60 bp)
- LM-window cumulative (since 5/21 EOD baseline): **+$144.32 / +0.143% equity / -25.8 bp alpha vs SPY**
- YTD: Bull +0.891% vs SPY +9.464% → **YTD alpha -857 bp**
- Max equity intra-week: $101,208.22 (5/22 13:38Z post-fill watermark)
- Min equity intra-week: $100,126.61 (5/19 EOD)
- Peak-to-trough drawdown intra-week: -1.07% (5/19), recovered fully by 5/20 close
- VIX range: 16.59 → 17.79; EOD 5/22 = 16.82 (no risk-off across the week)
- Total trades book-wide: 2 (both Swing entries on 5/22; 0 closes)
- PDT day-trade count Fri EOD: 2/5 (Alpaca pre-counted from Swing-w/-GTC-stop entries; no actual round-trips)

### Per-sleeve P&L attribution (KW 21)

| Sleeve     | Days active | Trades | Realized $ | Open UPL Δ (Fri-EOD vs prior Fri) | Net P&L attribution |
|------------|------------:|-------:|-----------:|----------------------------------:|--------------------:|
| Core       | 5          | 0      |  $0        | +$340.52 (UPL $610.49 → $951.01)   | **+$340.52** |
| Swing      | 1 (Fri)    | 2      |  $0        | -$44.98 (NVDA -$45.02 + RL +$0.04)  | **-$44.98**  |
| Daytrade   | 5          | 0      |  $0        | $0                                  | $0           |
| Crypto     | 5          | 0      |  $0        | $0                                  | $0           |
| Options    | 5          | 0      |  $0        | $0                                  | $0           |
| **Total**  | —          | 2      |  $0        | **+$295.54**                        | **+$295.54** |

**Best sub-strategy KW 21**: `core-buy-and-hold` (+$340.52 UPL Δ — only sleeve
with positive net attribution; LLY HWM walked +2.58% cumulative across the
week, biggest organic protection drift in book history).

**Worst sub-strategy KW 21**: `swing-quality-pullback` (NVDA -$45.02 UPL EOD;
Day 1 of 7-td hold; thesis intact, cushion 2.81% Fri → 2.96% Sat).

**Strategies with 0 trades in 7d**: 19 of 22 (Crypto + Daytrade + Options
sleeves entirely + 6 of 8 Swing sub-strategies). Per routine spec, "review
whether trigger is reachable":
- POLYGON-dependent (10 strategies, now resolved 5/22 AM): triggers are
  reachable from KW 22 onward.
- Polygon-options-chain-dependent (4 Options strategies): triggers
  STILL not reachable until tier-gate resolves. Status quo through KW 22.
- Crypto trend-follow + mean-reversion: triggers reachable, market simply
  didn't offer setups (50<200 across the entire 5-coin universe; 24h drops
  all <2%). Keep dormant — this is tape, not concept.
- Crypto weekend-momentum: trigger reachable, didn't fire (BTC 7d -3.02%).
  Keep dormant.
- `swing-mean-reversion`, `swing-short-rejection`, `swing-momentum-breakout`,
  `swing-short-fundamental`: triggers reachable, market didn't offer clean
  setups or the qualitative filter (INTU thesis-risk) overrode. Keep dormant.
- `swing-insider-buys`: still paused (Polygon Form-4 not in base tier).
- `options-cash-secured-put`: still paused.

## Daily refresh log

- **2026-05-30 20:38Z (06-weekly-review, KW 22 Sat-slot)** — **NO BANDIT CULL**
  (pre-condition: ≥3 trades per strategy not met for any strategy in trailing 7d).
  Weekly KPI roll-up appended above. Weekly alpha **-18.4 bp** (improvement
  from KW 21's -50 bp; +32 bp recovery). LM-window cumulative since 5/21 EOD
  baseline: **+$1,417.03 / +1.4063% / -44.6 bp alpha**. Top sub-strategy KW 22:
  `core-buy-and-hold` +$1,379.91 UPL Δ (LLY +5.13% Thu walk + MSFT/AVGO/VOO/
  META 4 Core HWM advances Fri = book-record single-day cluster). Bottom:
  `swing-quality-pullback` -$99.10 realized (-1.0R clean; NVDA stop-out Wed
  5/27; stub close re-queued Mon 6/1 02-market-open after Thu/Fri both
  missed). 5 lessons appended to `memory/lessons.md` as week-ending KW 22
  entry (L1 Fri cron-miss cluster, L2 NVDA stop validates -5% mechanic, L3
  slow-grind-up regime favors quality + PEAD, L4 Polygon options-chain 6
  consecutive blocks = escalation needed, L5 CallMeBot 403 length+content
  WAF hypothesis). No strategy.md / playbook.md edits this routine (1 closed
  trade insufficient for strategy-level cull or refinement; defer to KW 23
  EOW). Next eligible bandit cull = Fri 6/5 / Sat 6/6 (KW 23 EOW). WhatsApp
  sent German weekly brief at end of routine; **also surfaces Polygon
  options-chain escalation question** to Robin via inbox.md path. Inbox.md
  Pending: empty.

- **2026-05-29 12:05Z (01-pre-market, LM Day 9 — Fri post-PCE risk-on tape)** —
  **NORMAL pre-market routine** (broker reachable; account pulled; clock
  is_open=False 85 min to cash open; futures green; VIX 15.80; no risk-off).
  KPI deltas vs Thu 5/28 12:05Z snap: `core-buy-and-hold` UPL **$+1,481.91 →
  $+2,084.08 (+$602.17 on Thu's broad rally)** — LLY ATH walk +$116.94 (+5.13%
  trail walk from $1093 HWM to $1149.10 = biggest single-day organic trail
  walk in book history), MSFT +$188.16 (+3.47%), AVGO +$200.61 (+1.12%
  continuation pre-6/3 earnings), META +$5.78 (flat close but new intraday
  ATH $643 / stop walked +0.70%), VOO walked HWM $691.51 → $694.29 (+0.40%).
  `swing-quality-pullback` realized -$99.10 (NVDA stop Wed) + stub UPL -$0.46
  (Thu 02-open close DID NOT FIRE — re-queue Fri); `swing-earnings-drift`
  UPL **+$2.98 → -$24.27 (-$27.25 on Thu RL -1.45% giveback)** cushion
  compressed 7.19% → 5.79%. Bull equity **$100,901.97 → $101,960.92 (+$1,058.95
  / +1.05%)** over the 5/26-5/28 stretch since Mon holiday EOD lock; vs 5/21 EOD
  baseline +$1,199.20 / +1.19%. SPY: Fri pre-mkt $754.60 close Thu vs $745.70
  5/22 EOD = +1.19% over the same stretch → **LM cum alpha drift roughly neutral
  ~-41 bp** (refined intraday). VIX 15.80 (-5.7% Thu; risk-on confirmed).
  Daytrade count (5d): **0** (still RESET; full PDT budget). Options BP
  $69,170.73 / L3 ✓. **Polygon options-chain 6th re-test FAILED 12:08Z** —
  all 4 Options sub-strategies remain BLOCKED. **AMD swing-momentum-breakout
  CANDIDATE** for Fri 02-open entry (Thu +4.55% clean break + hold $510 = $518.09
  close; new 52w-Hi $527.20 intraday; sizing 3 sh @ ~$520 = ~$1,560 stop $494
  GTC target $572). **ARM SKIP** (Thu +10.76% extended ATH $349.42; sub-1R now).
  **AAPL SKIP** (no rejection candle Thu; WWDC 6/8-12 ahead). **NVDA stub close
  re-queue Fri 02-open** (Thu plan failed to execute; cash unchanged confirms).
  RL HOLD; tighten-to-breakeven only at UPL ≥+5%. Crypto 0/5 cross-up; BTC
  -3.26% gap (+0.24 pp/day Thu pace). Inbox.md Pending: empty. WhatsApp
  Top-5 News DE multi-part scheduled for 12:??Z send via
  `send_long_routine_message` (ASCII hyphen workaround per lesson 2026-05-28
  baked into helper). Macro risk-off NOT active. **First eligible bandit
  cull** still scheduled Fri 5/29 21:30Z (today; 06-weekly-review).

- **2026-05-20 EOD (05-close-summary)** — Final Live-Phase EOD pre-LM-start. 0 trades
  across all 22 seeded strategies (Core in HOLD; Swing/Daytrade/Crypto/Options not
  yet active). Per-strategy KPIs unchanged from initialization; `core-buy-and-hold`
  row updated with carryover Live-Phase mark (+$610.31 UPL on $62,610.49 cost-basis,
  -8.24% alpha vs SPY over the 9-day Live-Phase paper run 5/12 → 5/20). All sleeve
  budgets ready for LM Day 1 activation tomorrow 13:00Z.

- **2026-05-21 14:30Z (02-market-open, LM Day 1)** — **ABORT-ENTRIES routine** because
  the 13:00Z 01-pre-market did not fire (4th miss in 9 trading days). 0 trades on any
  sleeve. Only KPI delta: `core-buy-and-hold` UPL drifts $610.31 → $468.18 (-$142.13
  intraday) on broker mid-morning marks. BRK.B leading the drawdown -1.59% UPL, MSFT
  leading gains +4.33%. SPY -0.430% intraday → Core day-alpha so far +28.9 bp (Core
  -0.141% intraday vs SPY -0.430%, alpha from individual-name dispersion). Swing /
  Daytrade / Crypto / Options sleeves remain at 0 trades — no plan = no entries per
  ALM-1. Robin notified via WhatsApp + inbox.md options A/B for unblocking Day 1.

- **2026-05-21 16:38Z (03-midday, LM Day 1)** — **HOLD routine** (abort-entries posture
  continued; no 01-pre-market back-fire). 0 trades on any sleeve. KPI deltas:
  `core-buy-and-hold` UPL drifts $468.18 → $504.44 (+$36.26 intraday recovery). Sleeve
  leadership flipped: LLY +4.027% UPL takes lead from MSFT +3.014% (MSFT gave back the
  morning spike; LLY HWM bumped to $1,043.38 with stop bumped to $939.04 organically).
  BRK.B recovered to -1.071% UPL (from -1.59%). AVGO is the new tightest cushion at
  3.69% (from 5.25% morning). SPY -0.329% intraday → Core day-alpha **+22.4 bp**
  (compressed from +28.9 bp). `crypto-trend-follow` scanned all 5 universe names: all
  in 50<200 downtrend → 0 entries triggered. VIX 17.24 (no risk-off). No new
  inbox.md replies from Robin yet.

- **2026-05-21 19:36Z (04-pre-close, LM Day 1)** — **HOLD routine** (Daytrade sleeve
  empty → force-flat is a no-op; abort-entries posture continued). 0 trades on any
  sleeve. KPI deltas: `core-buy-and-hold` UPL drifts $504.44 → **$729.41** (+$224.97
  on a late-session SPY rally; Bull equity flips green vs 5/20 close, +$118.92 /
  +0.118%). LLY HWM advanced **again** $1,043.38 → $1,046.415 (stop bumped $939.04
  → $941.77) — 2nd organic trail-advance of the day, extending LLY's lead to +4.369%
  UPL. AVGO continued to tighten: cushion 3.69% → **3.43%** (mark $413.36 → $412.265),
  still above 3% threshold but the only Core name negative on the day (-0.476% UPL).
  SPY +0.206% intraday into late-day rally → Core day-alpha **-8.8 bp** (compressed
  from +22.4 bp at 03-midday; SPY out-ran the Core dispersion late). VIX 16.89
  (no risk-off). Daytrade count (5d): 0 / PDT: False. No new inbox.md replies from
  Robin yet. No crypto re-scan (no new signal expected within 3h window).

- **2026-05-21 20:30Z (05-close-summary, LM Day 1 EOD)** — **EOD HOLD routine** (market
  closed; 0 trades book-wide for Day 1). KPI deltas: `core-buy-and-hold` UPL drifts
  $729.41 → **$761.72** (+$32.31 on late-day Core tick-up; AVGO recovered $412.265
  → $414.2595 cushion 3.43% → 3.90% UPL -$22.21 → +$0.26; LLY HWM advanced
  **3rd time of the day** $1,046.415 → $1,047.295, stop bumped $941.77 → $942.5655).
  Bull equity $100,761.72 / **+$151.23 vs 5/20 close +0.150%**. SPY EOD $742.77 /
  +0.205% → **final Day-1 alpha -5.5 bp** (recovered from -8.8 bp at 04-pre-close
  as Core ticked up while SPY finished flat from 19:36Z). VIX EOD 16.72 (no risk-off).
  Daytrade count (5d): 0 / PDT: False post Day-1. Options BP $69,380.85 / L3 ✓.
  Sleeve P&L attribution Day 1: **Core +$151.23 only**; Swing/DT/Crypto/Options
  all $0 (empty all day). Top sub-strategy (by elimination): `core-buy-and-hold`
  (only sleeve with attribution). Bottom (by elimination): 4 POLYGON-dependent
  sub-strategies (`daytrade-orb`, `daytrade-vwap-pullback`, `scalp-tape`,
  `options-long-call-momentum`) which couldn't scan a single signal due to
  POLYGON_API_KEY unset. 18 consecutive no-action routines. Inbox.md still empty
  on Q1 A/B/C — re-broadcast via WhatsApp this routine. **Day 1 closing baseline
  locked: cumulative LM-window P&L $0 net + Core carryover UPL +$151.23.**

- **2026-05-22 13:38Z (02-market-open, LM Day 2)** — **FIRST NON-CORE LM FILLS**.
  2 Swing entries placed at the open: NVDA $2k notional (`swing-quality-pullback`)
  + RL $1.5k notional (`swing-earnings-drift`). Both filled within 1.4 seconds:
  NVDA 9.092513 sh @ $219.9612, RL 3.978463 sh @ $377.03. Sleeve-specific stops
  live GTC: NVDA $208.96 (-5%), RL $350.64 (-7%). Swing sleeve used $3,500 of
  $15k → $11,500 remaining; 2/8 positions. `core-buy-and-hold` UPL drifted
  $761.72 → $1,217.05 (+$455.33) on broad Core green print at the open, biggest
  contributor LLY (+$70+) which advanced HWM ORGANICALLY $1,047.295 → ~$1,063.67
  (stop $942.5655 → $957.303, +1.55%). AVGO recovered 3.90% → 4.87% cushion.
  Day-trade count: 0 → 2 (Alpaca pre-counts open positions w/ same-day GTC stops
  as eligible day-trades — observation only, threshold is 4). Daytrade sleeve
  empty; ORB watches set for SPY/QQQ/NVDA/TSLA/AAPL/AMD but execution deferred
  to 03-midday per routine spec. Crypto + Options remain empty. NVDA options
  bull-call-spread BLOCKED on Polygon options-chain gate; NVDA conviction routed
  through equity sleeve as fallback. Day-alpha snap 13:38Z: Bull +0.448% vs
  SPY +0.60% → -15.2 bp.

- **2026-05-22 19:36Z (04-pre-close, LM Day 2)** — **HOLD / FORCE-FLAT NO-OP**
  routine (0 trades; Daytrade sleeve empty → force-flat is a no-op; Swing
  stops verified live GTC; Crypto Friday-tighten no-op (sleeve empty);
  Options 7-DTE/IV-crush no-op (sleeve empty); AAPL `swing-short-rejection`
  EOD candle = NO trigger today (UP candle +1.00% with fresh $311.40 52w-Hi
  extension)). Equity drifted $100,982.35 → **$100,880.46** (-$101.89 /
  -0.101% on continued Core mark fade, GOOGL main negative contributor
  -$2.75 mark intraday). `core-buy-and-hold` UPL drifted $1,018.43 →
  **$1,000.49** (-$17.94). LLY HWM organic walk-up **#6** $1,069.11 →
  $1,070.3399 (stop $962.199 → $963.30591, +0.115% additional bump;
  cumulative LLY trail walk over 2 LM days: $942.5655 → $963.30591 =
  +2.20%, biggest-ever organic protection drift in Live-Phase + LM record).
  AVGO cushion compressed further 3.79% → **3.43% (tightest in book)**;
  GOOGL cushion compressed 4.61% → **3.93% (biggest single-day tighten)**.
  Swing sleeve drift: NVDA UPL -1.585% → -2.010% (cushion 3.47% → **3.05%**
  — tightest since fill but still above playbook -5% trigger), RL UPL
  -0.260% → -0.065% (cushion 6.76% → 6.94%, slight improve). No Swing
  exits; no tighten-to-breakeven (both UPL negative). ARM `swing-momentum-
  breakout`: intraday H $315 → C $304.66 (-3.28% off high) — re-arm only
  on close <$290 per 01-pre-market. Crypto sleeve: all 5 50<200 downtrend
  widened (BTC gap -4.2% → -6.2%); 24h moves -2.27% to -3.25% (more
  uniformly bleeding); `crypto-weekend-momentum` Fri-close trigger NOT
  met (BTC 7d **-3.02%** vs +2% threshold). Options: Polygon options-chain
  4th re-test deferred. Day-alpha snap 19:36Z: Bull +0.118% vs SPY +0.446%
  → **-32.8 bp** (slightly improved from -34.7 bp at 03-midday as SPY gave
  back some midday gains while Bull held). Macro risk-off NOT active
  (SPY +0.45% / VIX 16.73 / no -3% or >40 threshold). No WhatsApp this
  routine (per spec — only on urgent risk).

- **2026-05-22 20:16Z (05-close-summary, LM Day 2 EOD)** — **EOD HOLD routine**
  (market closed; 0 trades; EOD reconcile only). KPI deltas: `core-buy-and-hold`
  UPL drifts $1,000.49 → **$951.01** (-$49.48; LLY mark eased $1,067.13 →
  $1,065.50, no HWM walk-up #7 today; AVGO + GOOGL marks recovered modestly
  → cushions improved 3.43% → **3.78%** and 3.93% → **4.08%**; MSFT mark up
  $418.32 → $419.02; rest of Core ±$0.30 mark drifts). `swing-quality-pullback`
  UPL $-40.20 → **-$45.02** (NVDA mark $215.54 → $215.01, -$0.53 in the close;
  **cushion compressed 3.05% → 2.81% — tightest since fill**, but still above
  -5% playbook trigger). `swing-earnings-drift` UPL $-0.97 → **+$0.04** (RL
  mark $376.785 → $377.04, recovered $0.255 in the close; cushion 6.94% →
  7.00%). Bull equity $100,880.46 → **$100,906.04** (+$25.58 / +0.025% intraday
  drift from 04-pre-close; vs Day-1 baseline $100,761.72 +$144.32 / +0.143%).
  SPY EOD $745.70 (+0.401% DoD vs 5/21 EOD $742.72) → **Day-2 final alpha
  -25.8 bp** (improved from -32.8 bp at 04-pre-close as Core ticked up modestly
  while SPY held). VIX EOD 16.82 (no risk-off). Daytrade count (5d): 2 / PDT:
  False (UNCHANGED from 02-market-open watermark). Options BP $67,697.39 /
  L3 ✓. Sleeve P&L attribution Day 2: **Core +$189.29** (UPL drift $761.72
  → $951.01 over the full Day 2 trading session), **Swing -$44.98** (NVDA
  -$45.02 + RL +$0.04, both opened today at 02-market-open), DT/Crypto/Options
  all $0 (empty all day). **Top sub-strategy Day 2**: `core-buy-and-hold`
  +$189.29 (only sleeve with positive attribution). **Bottom Day 2**:
  `swing-quality-pullback` -$45.02 (NVDA only). `swing-earnings-drift` +$0.04
  (net-neutral; PEAD thesis intact for Day 3+). `crypto-weekend-momentum`
  final Fri-close trigger NOT MET (BTC 7d -3.02% << +2% threshold) → confirmed
  NO entry at EOD. `crypto-mean-reversion` pre-trigger watch over long weekend
  (5/23-5/25; Mon 5/25 = Memorial Day closed). Options sleeve `options-vertical-
  bull-call-spread` (NVDA) still BLOCKED on Polygon chain (4th re-test deferred).
  Inbox.md Pending: empty (Robin Q1 A/B/C still partially open — A resolved
  by no-recurrence, B resolved POLYGON set / chain still gated, C cron extension
  TBD for Sat 5/23). Robin notified via WhatsApp at 21:00Z (LM Day 2 evening
  brief in German, ≤1000 chars per CLAUDE.md spec). **LM Day 2 closing baseline
  locked: Bull equity $100,906.04 / cumulative LM-window P&L $0 realized +
  Core UPL $951.01 + Swing UPL -$44.98; LM cum alpha -25.8 bp; LM cum trade
  count 2 (both open).** Next routine: Tue 5/26 01-pre-market 13:00Z (Mon 5/25
  Memorial Day = closed cash session, weekday cron may fire and log `is_open=False`
  skip; Sat+Sun 03-midday extension awaits Robin inbox Q1 C confirmation).

- **2026-05-22 16:42Z (03-midday, LM Day 2)** — **HOLD routine** (0 trades).
  Equity drifted $101,208.22 → **$100,982.35** (-$225.87 / -0.223%) on Core
  mark fade into midday (MSFT +4.575% → +3.513%, META +2.264% → +1.159%,
  AVGO +1.037% → -0.105% cushion 4.87% → **3.79% tightest in book**, GOOGL
  -0.059% → -0.456% cushion 4.61%, V mild giveback). `core-buy-and-hold`
  UPL$ $1,217.05 → **$1,018.43** (-$198.62). Only Core gainers vs 13:38Z:
  BRK.B (small) and LLY (HWM organic walk-up #5 $1,063.67 → $1,069.11
  → stop $957.303 → $962.199, +0.51% additional bump; cumulative LLY
  trail walk over 2 LM days: $942.5655 → $962.199 = +2.08%, biggest-ever
  organic protection drift in Live-Phase + LM record). Swing sleeve drift:
  NVDA UPL -0.073% → -1.585% (cushion to stop 3.47% — above the playbook
  -5% trigger), RL UPL -0.553% → -0.260% (cushion 6.76%). No Swing exits.
  ARM `swing-momentum-breakout` WATCH: trigger window 13:30-14:00Z closed
  without a clean ORB-style consolidation+break; price grinded to $307.64
  (+4.32% intraday from 13:37Z $294.90, now 0.77% below the "DO NOT chase
  above $310" line). Decision: **PASS** — missed trigger, do not chase
  → will re-arm only if ARM closes back below $290. AAPL `swing-short-
  rejection`: defer to 04-pre-close EOD candle. Daytrade sleeve: ORB
  window closed, no clean signal — 0 entries; PDT count UNCHANGED at 2/5.
  Crypto sleeve: all 5 still 50<200 downtrend, deepest 24h move BTC
  -0.91%, no signal. Options: Polygon options-chain re-tested at 16:40Z
  → **still 403 Forbidden** (`get_iv_rank('NVDA')` returns None); 0 entries.
  Day-alpha snap 16:42Z: Bull +0.219% vs SPY +0.571% → **-34.7 bp**
  (widened from -15.2 bp at 13:38Z; Core mark-fade outpaced SPY drift).
  Macro risk-off NOT active (SPY +0.57% / VIX 16.59 / no -3% or >40
  threshold). No WhatsApp this routine (per spec — only on urgent risk).

- **2026-05-23 20:47Z (06-weekly-review, Sat-slot for KW 21)** — **NO BANDIT CULL**
  (pre-condition: ≥3 trades per strategy not met; only 2 LM trading days have
  occurred). Weekly KPI roll-up appended above. Weekly alpha -50.1 bp (regression
  from KW 20's +60 bp). LM-window cumulative since 5/21 EOD baseline: +$144.32 /
  +0.143% / -25.8 bp alpha. Top sub-strategy KW 21: `core-buy-and-hold` +$340.52
  UPL Δ (LLY HWM walked +2.58% cumulative). Bottom: `swing-quality-pullback`
  -$45.02 EOD (NVDA Day 1 of 7-td hold; thesis intact). 19/22 sub-strategies
  at 0 trades 7d — attribution mostly POLYGON-unset (resolved 5/22 AM) +
  Polygon-options-chain-gated (still open) + tape-not-offering-setups (Crypto/
  some Swing). 5 lessons appended to `memory/lessons.md` as week-ending KW 21
  entry. No strategy.md / playbook.md edits this routine (insufficient signal
  from 2 LM days). First eligible bandit cull = Fri 5/29 / Sat 5/30 (KW 22 EOW).
  No WhatsApp send-failure: German weekly brief sent at end of routine, ≤1000
  chars including header. Inbox.md Pending = empty.

- **2026-05-24 16:36Z (03-midday, LM Day 4 — Sunday weekend-crypto-cycle)** —
  **WEEKEND HOLD routine** (0 trades; equities don't trade weekends; crypto
  sleeve scanned, no entry signals). KPI deltas vs Sat 5/23 16:36Z snapshot:
  ALL marks identical (broker's weekend quote stream produced no fresh ticks
  Sat → Sun across any of the 10 positions). `core-buy-and-hold` UPL =
  **$941.97** (unchanged), `swing-quality-pullback` UPL = **-$42.11**
  (unchanged), `swing-earnings-drift` UPL = **+$2.98** (unchanged). Bull
  equity **$100,901.97** (unchanged vs Sat; -$4.07 / -0.004% vs 5/22 EOD;
  +$140.25 / +0.139% vs 5/21 EOD baseline). SPY: no weekend tape, carryover
  Fri close $745.70; VIX 16.82 carryover. **LM Day 4 alpha (carryover from
  5/22 EOD): -25.8 bp**. **Notable broker change**: `daytrade_count` ROLLED
  **2 → 0** on the 5/23 broker EOD snap (between Sat 16:36Z and Sun 16:36Z).
  Confirms the provisional pre-count from the 5/22 Swing-w/-GTC-stop fills
  has reversed since no round-trip occurred. PDT budget for Tue 5/26 = full
  5/5 again. Options BP $67,700.98 / Level 3. Sleeve P&L attribution Day 4:
  Core $0 / Swing $0 / DT $0 / Crypto $0 / Options $0 (all identical to Sat;
  no fresh attribution on weekend snap). **Top sub-strategy Day 4 (Sun)**:
  n/a — no fresh attribution. **Bottom Day 4 (Sun)**: n/a — same reason.
  **Crypto scan**: BTC -0.37%/24h, -1.35%/7d, 50/200 gap narrowed further
  **-5.09% → -4.67%** (leading the convergence; cross-up could fire within
  6-10 trading days at current pace). ETH -1.00%/24h. SOL -0.49%/24h. AVAX
  -1.86%/24h. LINK -1.42%/24h. **0 crypto entries**: 0/5 50/200 cross-up
  signals, 0/5 -10%/24h flush triggers, weekend-momentum no-monitor (no
  Fri-close fill; closed). Macro risk-off N/A (no weekend tape; carryover
  NOT active). Inbox.md Pending: empty. **LM Day 4 (Sun) running tally
  locked: Bull equity $100,901.97 / cumulative LM-window P&L $0 realized +
  Core UPL $941.97 + Swing UPL -$39.13 = $902.84 UPL total / LM cum alpha
  -25.8 bp / LM cum trade count 2 (both open).** Next routine: Tue
  2026-05-26 01-pre-market at 13:00Z (Mon 5/25 Memorial Day cash session
  closed; weekend ends).

- **2026-05-23 16:36Z (03-midday, LM Day 3 — Saturday weekend-crypto-cycle)** —
  **WEEKEND HOLD routine** (0 trades; equities don't trade weekends; crypto
  sleeve scanned, no entry signals). KPI deltas vs Fri 5/22 EOD: `core-buy-
  and-hold` UPL drifts $951.01 → **$941.97** (-$9.04 on weekend quote-refresh
  noise; GOOGL cushion compressed 4.08% → 3.97% **new 2nd-tightest**, AVGO
  cushion recovered 3.78% → 3.87% **still tightest**, other Core marks
  ±$0.50 of Fri close). `swing-quality-pullback` UPL $-45.02 → **-$42.11**
  (NVDA mark $215.01 → $215.33 +$0.32 on weekend quote-noise; cushion
  recovered 2.81% → **2.96%**). `swing-earnings-drift` UPL $+0.04 →
  **+$2.98** (RL mark $377.04 → $377.78 +$0.74; cushion 7.00% → **7.19%**).
  Bull equity $100,906.04 → **$100,901.97** (-$4.07 / -0.004% on weekend
  refresh noise; vs 5/21 EOD baseline +$140.25 / +0.139%). SPY: no
  weekend tape, carryover Fri close $745.70 (+0.401% DoD); VIX 16.82
  carryover. **LM Day 3 alpha (carryover from 5/22 EOD): -25.8 bp**.
  Daytrade count (5d): 2 / PDT: False (UNCHANGED). Options BP: weekend
  N/A. Sleeve P&L attribution Day 3: Core -$9.04 (mark refresh), Swing
  +$5.85 (mark refresh: NVDA +$2.91, RL +$0.74; mark $377.78 hits ~+0.20%
  vs entry on weekend quote), DT/Crypto/Options all $0. **Top sub-strategy
  Day 3 (Sat)**: `swing-earnings-drift` +$2.94 mark refresh on RL (only
  positive equity-attribution this routine; `core-buy-and-hold` net
  negative -$9.04 on noise). **Bottom Day 3 (Sat)**: `core-buy-and-hold`
  -$9.04 mark refresh. **Crypto scan**: BTC -0.12%/24h, -3.50%/7d, 50/200
  gap narrowed -6.2% → -5.09% but no cross. ETH -0.32%/24h. SOL -0.34%/24h.
  AVAX -0.07%/24h. LINK -1.16%/24h. **0 crypto entries**: 0/5 50/200
  cross-up signals, 0/5 -10%/24h flush triggers, weekend-momentum no-
  monitor (no Fri-close fill). Macro risk-off N/A (no weekend tape;
  carryover NOT active). Inbox.md Pending: empty. **LM Day 3 (Sat)
  running tally locked: Bull equity $100,901.97 / cumulative LM-window
  P&L $0 realized + Core UPL $941.97 + Swing UPL -$39.13 = $902.84 UPL
  total / LM cum alpha -25.8 bp / LM cum trade count 2 (both open).**
  Next routine: Sun 2026-05-24 03-midday at 17:30Z (weekend crypto-cycle
  Day 2 of 2; Mon 5/25 Memorial Day cash session closed; Tue 5/26
  01-pre-market at 13:00Z is next equity touchpoint).

- **2026-05-25 19:37Z (04-pre-close, LM Day 5 EOD — Memorial Day weekday holiday)** —
  **HOLIDAY EOD HOLD routine** (0 trades; cash session closed all day;
  equity sleeves snapshot-only; Daytrade force-flat = no-op on empty
  sleeve; Friday-tighten N/A on Monday; crypto sleeve full scan, 0
  entries). Note: routine fired at 19:37Z = ~53 min EARLY vs the
  20:30Z cron slot; per spec "time-to-close > 60min → log + proceed
  cautiously" — cash market is fully closed today so the early-fire
  is moot for execution. **All marks IDENTICAL across the 4 Mon
  intraday snapshots** (12:13Z → 16:39Z → 19:37Z + Sun) — broker pushed
  zero new ticks all day. KPI deltas vs 16:39Z: `core-buy-and-hold`
  UPL **+$941.97** UNCHANGED, `swing-quality-pullback` UPL **-$42.11**
  UNCHANGED, `swing-earnings-drift` UPL **+$2.98** UNCHANGED. Bull
  equity **$100,901.97** UNCHANGED. SPY: no Mon tape, carryover Fri
  close $745.70; VIX 16.82 carryover. **LM Day 5 EOD alpha (carryover
  from 5/22 EOD): -25.8 bp** (identical to 5/22-5/24 carryover).
  Daytrade count (5d): **0** (RESET held). Options BP $67,700.98 /
  L3 ✓. **Sleeve P&L attribution Day 5 EOD**: Core $0 / Swing $0 / DT
  $0 / Crypto $0 / Options $0 (no fresh attribution — broker pushed
  zero new ticks all day). **Top / Bottom sub-strategy Day 5 EOD**:
  n/a (no fresh attribution). **Crypto scan @ 19:37Z**: BTC +0.46%/24h,
  gap **-4.31% UNCHANGED for the 3rd consecutive Mon intraday scan**
  (12:11Z → 16:39Z → 19:37Z all at -4.31%; price slipped $77,558 →
  $77,339 but DMAs absorbed it). ETH +0.97%/24h. SOL +0.40%/24h. AVAX
  +1.77%/24h (largest, positive direction). LINK +1.06%/24h. **0
  crypto entries**: 0/5 50/200 cross-up, 0/5 -10%/24h flush, weekend-
  momentum closed. Macro risk-off N/A (no Mon SPY/VIX tape; carryover
  NOT active). **Daytrade force-flat (Step 3c)**: sleeve was 0/5 going
  in; force-flat is a NO-OP; verified `daytrade_count=0` and 0 open
  Daytrade positions after step. **Swing stops verified live GTC**:
  NVDA $208.96 + RL $350.64 both `OrderStatus.NEW`. **Crypto Friday-
  tighten**: N/A (Mon, not Fri; sleeve empty anyway). **Options Greeks
  / 7-DTE / IV-crush**: N/A (sleeve empty; Polygon chain still gated).
  Inbox.md Pending: empty. **LM Day 5 (Mon holiday) EOD running tally
  LOCKED: Bull equity $100,901.97 / cumulative LM-window P&L $0
  realized + Core UPL $941.97 + Swing UPL -$39.13 = $902.84 UPL total
  / LM cum alpha -25.8 bp / LM cum trade count 2 (both still open).**
  No WhatsApp (per spec — 04-pre-close is WhatsApp-NO unless urgent).
  Next routine: 05-close-summary at 21:15Z (also holiday — likely
  snapshot-only EOD WhatsApp). Then Tue 2026-05-26 01-pre-market at
  13:00Z (post-holiday open; AAPL re-watch, ARM re-arm, Polygon
  options-chain 4th re-test, SPY protective-put pre-flight for Thu
  5/28 PCE+GDP, NVDA Day-2 cushion check).

- **2026-05-25 16:39Z (03-midday, LM Day 5 — Memorial Day weekday holiday)** —
  **HOLIDAY HOLD routine** (0 trades; cash session closed; equity sleeves
  snapshot-only; crypto sleeve full scan, 0 entries). KPI deltas vs Mon
  01-pre-market 12:13Z snap: **ALL marks identical** for the 10 equity
  positions (broker pushing zero fresh ticks on the holiday). `core-buy-
  and-hold` UPL = **+$941.97** (UNCHANGED), `swing-quality-pullback` UPL =
  **-$42.11** (UNCHANGED), `swing-earnings-drift` UPL = **+$2.98**
  (UNCHANGED). Bull equity **$100,901.97** (UNCHANGED vs Sun + vs 12:13Z;
  -$4.07 vs 5/22 EOD; +$140.25 / +0.139% vs 5/21 EOD baseline). SPY: no
  Mon holiday tape, carryover Fri close $745.70; VIX 16.82 carryover.
  **LM Day 5 alpha (carryover from 5/22 EOD): -25.8 bp** (identical to
  5/22-5/24 carryover). Daytrade count (5d): **0** (RESET held from 5/23
  broker rollover). Options BP $67,700.98 / L3 ✓. Sleeve P&L attribution
  Day 5: Core $0 / Swing $0 / DT $0 / Crypto $0 / Options $0 (no fresh
  attribution on holiday snap). **Top / Bottom sub-strategy Day 5**: n/a
  (no fresh attribution). **Crypto scan @ 16:39Z**: BTC +0.75%/24h
  (+0.78%/7d, gap **-4.31%** UNCHANGED from 12:11Z — convergence stalled
  intraday; full Tue session needed to resume). ETH +1.40%/24h. SOL
  +0.95%/24h. AVAX **+2.53%/24h** (largest move, positive direction).
  LINK +1.80%/24h. **0 crypto entries**: 0/5 50/200 cross-up, 0/5
  -10%/24h flush, weekend-momentum no-monitor (no Fri-close fill).
  Macro risk-off N/A (no Mon SPY/VIX tape; carryover NOT active; pre-
  market futures + 10Y dovish drift from 12:13Z scan still in effect).
  **Correction note**: 12:13Z report claimed LINK 50-DMA was above
  200-DMA-trail by $0.01; fresh authoritative scan shows LINK 200-DMA
  $10.88 (well above 50-DMA $9.509). LINK is NOT on the cusp; BTC
  remains the leading convergence candidate. Inbox.md Pending: empty.
  **LM Day 5 (Mon holiday) running tally locked: Bull equity
  $100,901.97 / cumulative LM-window P&L $0 realized + Core UPL $941.97
  + Swing UPL -$39.13 = $902.84 UPL total / LM cum alpha -25.8 bp / LM
  cum trade count 2 (both open).** Next routine: Tue 2026-05-26
  01-pre-market at 13:00Z (post-holiday open; full equity execution
  resumes; AAPL `swing-short-rejection` re-watch, ARM `swing-momentum-
  breakout` re-arm watch, Polygon options-chain 4th re-test, SPY
  protective-put pre-flight for Thu 5/28 PCE+GDP).

- **2026-05-25 20:17Z (05-close-summary, LM Day 5 EOD LOCKED — Memorial Day weekday holiday)** —
  **HOLIDAY EOD WhatsApp HOLD routine** (0 trades book-wide; cash session
  closed all day; equity sleeves snapshot-only; crypto scan no-op since
  04-pre-close 19:37Z already cleared 0 signals at the final intraday
  pass). Routine fired at 20:17Z = ~58 min EARLY vs the 21:15Z cron slot;
  treated as the formal EOD reconcile since cash market is fully closed
  for the day. KPI deltas vs 04-pre-close 19:37Z: **NONE** — `core-buy-
  and-hold` UPL **+$941.97** UNCHANGED, `swing-quality-pullback` UPL
  **-$42.11** UNCHANGED (NVDA mark $215.33 / cushion 2.96%), `swing-
  earnings-drift` UPL **+$2.98** UNCHANGED (RL mark $377.78 / cushion
  7.19%). Bull equity **$100,901.97** UNCHANGED across all 5 Mon snaps
  (12:13Z, 16:39Z, 19:37Z, 20:17Z + Sun). **Day P&L vs Fri 5/22 EOD**:
  -$4.07 / -0.0040% (broker reconciliation noise; per-sleeve UPL-Δ
  attribution: Core -$9.04, Swing +$5.85, DT/Crypto/Options $0).
  **Day alpha vs SPY: 0 bp** (no Mon tape; SPY held at Fri close
  $745.70). **LM cumulative since 5/21 baseline**: +$140.25 / +0.1392%
  equity, -26.2 bp alpha vs SPY (≈ -25.8 bp reported carryover within
  reconciliation noise). **Per-sleeve LM cumulative attribution**: Core
  +$180.25 (best) / Swing -$39.13 (worst) / DT $0 / Crypto $0 / Options
  $0. **Top LM experiment**: `core-buy-and-hold` +$180.25 (LLY HWM
  walked 6 organic times across LM Day 1-2 — biggest book-history
  protection drift). **Bottom LM experiment**: `swing-quality-pullback`
  -$42.11 (NVDA only; thesis intact per weekend analyst median PT
  $275). Daytrade count (5d): **0** (RESET held). Options BP $67,700.98
  / L3 ✓. **No strategy milestones triggered today** (no 10th-trade, no
  first +5R, no first -5R aggregate loss). All 10 GTC stops verified
  `OrderStatus.NEW` at 20:17Z. WhatsApp DE evening brief sent ≤1000
  chars to `+4915153136372` via CallMeBot. **No `lessons.md` append**
  (no new generalizable rule emerged on holiday-no-trade EOD). Inbox.md
  Pending: empty. Next routine: **Tue 2026-05-26 01-pre-market at
  13:00Z** (post-holiday open; Polygon options-chain 4th re-test, AAPL
  `swing-short-rejection` re-watch, ARM `swing-momentum-breakout`
  re-arm watch, NVDA Day-2-of-7-td cushion watch, RL Day-2-of-10-td
  watch, SPY protective-put pre-flight for Thu 5/28 PCE+GDP).

- **2026-06-04 13:50Z (01-pre-market LATE FIRE, LM Day 15 — Thu post-AVGO/CRWD earnings)** —
  **AVGO Core trail-stop FIRED Thu 6/4 13:36:31Z @ $410.882727** on post-earnings
  gap-down (-13.58% Thu net; -7.85% gap-fill from $439.938 trigger). 2nd LM Core
  close (after GOOGL Tue 6/2). Realized -$36.92 on 11 sh / -0.79% of $4,665.94
  cost basis; gave back $880 of Wed UPL. AVGO earnings post-mortem: rev $22.2B
  slight miss / EPS $2.44 beat / AI semi $10.8B beat / Q3 guide $29.4B raised
  → BUT long-term $100B 2027 AI target NOT raised (Wall St wanted higher);
  software shortfall. "Beat-and-raise rejected because raise wasn't enough."
  `core-buy-and-hold` row updated. **RL `swing-earnings-drift` cushion COMPRESSED
  to 2.59% Thu (mark $359.72 / stop $350.64; UPL -4.59%) = sub-3% emergency
  threshold for first time in hold**; td9 of 10, time-stop Fri 6/5 close.
  Bull's recommendation queued for 03-midday: HOLD-into-td10 if cushion > 1.5%;
  CLOSE-EARLY if cushion < 1.5%; emergency stop-tighten as middle option.
  **AMD `swing-momentum-breakout` DROPPED-AS-MISSED** after 4 consecutive cron-miss
  entry-day pattern (Fri 5/29 + Mon-Tue-Wed 02-market-open all missed); Thu Wed
  trigger weakened (Thu C=$525.07 < Wed C=$542.52 new 20d-Hi; intraday L $499.87
  breached $510 spec threshold). Opportunity-cost ~$60 missed Wed open paper UPL.
  3 fractional stubs queued together for next live routine (NVDA 6th attempt +
  GOOGL 2nd attempt + AVGO NEW). MSFT cushion **2.65% = book-record tightest**;
  next mechanical stop-candidate. Equity $101,381.67 (-$615.78 vs Wed pre-mkt;
  +$619.95 vs 5/21 LM baseline). SPY +0.18% Thu intraday; VIX 15.71 (-2.18%);
  Macro risk-off NOT active. Polygon options-chain 10th block (AVGO strangle was
  textbook missed long-vol setup). Inbox.md Pending: empty. WhatsApp Dringend
  multi-part sent: AVGO stop + MSFT cushion + RL emergency + L4 escalation.

- **2026-06-05 15:39Z (01-pre-market LATE FIRE, LM Day 16 — Fri NFP-hawk + crypto-flush)** —
  **LATE FIRE research+draft only**, no orders authorized (per lesson 2026-05-15). Routine
  fired ~2h09m after cash open. **NFP May +172k vs +85k cons (102% beat) drove hawkish
  re-pricing**: SPY -1.37% / NQ -2.53% / VIX 16.63 (+8%) / 10Y +6 bp to 4.54% / DXY +0.49% /
  futures repricing 65% Fed-hike-by-Dec (was 48%). **MSFT cushion compressed to book-record
  tightest 0.46%** (stop $419.688 vs mark $421.625) on NQ-tech selloff — next mechanical
  stop-candidate, NO thesis-break catalyst (just rate-pressure). LLY HWM walked to NEW ATH
  $1166.225 (+1.49% organic) on healthcare-defensive rotation. BRK.B HWM walked $490.035
  (+0.14%). RL `swing-earnings-drift` cushion RECOVERED to 4.82% Fri intraday (was 2.59%
  Thu); mark $367.54 +2.18% from Thu on NFP-consumer-discretionary positive (cool wages
  3.4% AHE benefits retail tape). **HOLD into td10 close** per Thu Option C recommendation.
  **2 crypto-mean-reversion triggers FIRED**: ETH -10.87%/24h AND AVAX -10.38%/24h crossed
  -10% flush threshold. Catalyst = NFP-hawk-driven systemic risk-off (not exchange
  collapse → passes "no fundamental break" filter). **Queued for 03-midday 17:30Z**:
  ETH $1.5k + AVAX $1.5k = $3k total / 60% of $5k Crypto sleeve. First non-Core LM sleeve
  activation since 5/22 Swing. **Polygon options-chain 11th consecutive 403** — L4
  ESCALATION re-fires; NFP `options-protective-put` was textbook missed opportunity
  Fri. Default-if-no-Robin-reply Mon 6/8 = reallocate $5k → Cash reserve. **Thu 6/4
  WhatsApp send FAILED (503)** — Robin did NOT see yesterday's brief; Fri brief
  re-includes Thu key items. **3 fractional stubs** (NVDA 7th, GOOGL 3rd, AVGO 2nd)
  queued together for 03-midday. Equity $100,880.55 (-$501.12 vs Thu pre-mkt; +$118.83
  vs 5/21 LM baseline). Inbox.md Pending: empty. WhatsApp Top-5 News DE + Dringend
  overlay multi-part scheduled.
