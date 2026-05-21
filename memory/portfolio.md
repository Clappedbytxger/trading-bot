---
last_updated: 2026-05-21T19:36:00Z
broker: alpaca
account_type: paper
broker_endpoint: paper-api.alpaca.markets
phase: learning-month (Day 1 of 30)
phase_window: 2026-05-21 → 2026-06-20
phase_flip_next: 2026-06-21T00:00:00Z (Live-Phase Variant C reactivates)
routine: 04-pre-close (HOLD — abort-entries posture continued; daytrade sleeve empty so force-flat is no-op)
total_value_usd: 100729.41
cash_usd: 38000.00
long_market_value_usd: 62729.41
day_pnl_usd_vs_wed_close: +118.92
day_pnl_pct_vs_wed_close: +0.1182
day_spy_pct_vs_wed_close: +0.2064
day_alpha_bp_vs_spy: -8.8
ytd_pnl_pct: 0.7294
benchmark_spx_ytd: 9.0240
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_current_price: 742.78
alpha_vs_spx: -8.2946
position_count_total: 8
position_count_core: 8
position_count_swing: 0
position_count_daytrade: 0
position_count_crypto: 0
position_count_options: 0
leverage_x: 0.62
options_buying_power_usd: 69364.70
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
vix_current: 16.89
mins_to_close_at_snapshot: 24.3
---

# Portfolio — 04-pre-close 2026-05-21 (LM Day 1 of 30, 19:36Z / 15:36 ET)

> **Phase note**: 04-pre-close snapshot under Learning-Month rules, 24 min
> before market close. Abort-entries posture from 02-market-open is continued
> (no 01-pre-market back-fire today). Daytrade sleeve is empty so the
> force-flat step is a no-op; all other non-Core sleeves also empty.
> Core stops re-verified live (8/8 GTC). LLY HWM advanced again intraday
> ($1,043.382 → $1,046.415). AVGO cushion tightened further (3.69% → 3.43%)
> but remains above the 3% spec-threshold. Today is Thursday → no Friday
> crypto-tighten action. Macro: SPY +0.21% / VIX 16.89 → no risk-off.

## Sleeve summary

| Sleeve     | Cash budget          | Used                  | Open positions | Sleeve UPL$ | Sleeve UPL% | Notes                       |
|------------|---------------------:|----------------------:|---------------:|------------:|------------:|-----------------------------|
| Core       |  $62,000 (cost basis)| $62,729.41 (mark)     |             8  |  +$729.41   |   +1.176%   | Frozen — 8/8 stops live, AVGO cushion 3.43% (new tightest, still ≥ 3% threshold) |
| Swing      |  $15,000             |        $0             |             0  |       $0    |       —     | Empty (abort-entries Day 1)  |
| Daytrade   |  $10,000             |        $0             |             0  |       $0    |       —     | Empty — force-flat step no-op; POLYGON_API_KEY unset would block ORB/VWAP/scalp anyway |
| Crypto     |   $5,000             |        $0             |             0  |       $0    |       —     | Empty — Thursday so Fri-tighten not applicable; no open positions to manage |
| Options    |   $5,000 (premium)   |        $0             |             0  |       $0    |       —     | Empty — no Greeks check / 7-DTE close needed |
| Cash reserve | ≥$3,000            |       —               |             —  |       —     |       —     | $3k earmarked of $38k total  |

Total deployable cash for non-Core sleeves once trading resumes: **$35,000**.

## Core sleeve (8 positions, all inherited from Live-Phase exit)

| Symbol | Qty       | Avg Entry | Mark      | Market Value | UPL$       | UPL%     | Alloc % | Trail Stop / cushion |
|--------|----------:|----------:|----------:|-------------:|-----------:|---------:|--------:|----------------------|
| VOO    | 49.332341 |  $675.703 |  $682.84  |   $33,686.10 |  +$352.10  |  +1.056% |  33.45% | 10% trail / 49 sh GTC / HWM $689.10 / stop $620.19 / cushion 9.17% |
| MSFT   | 11.521758 |  $404.973 |  $418.85  |    $4,825.89 |  +$159.89  |  +3.427% |   4.79% | 10% trail / 11 sh GTC / HWM $432.70 / stop $389.43 / cushion 7.02% |
| GOOGL  | 12.047273 |  $387.308 |  $388.43  |    $4,679.52 |   +$13.52  |  +0.290% |   4.65% | 10% trail / 12 sh GTC / HWM $408.61 / stop $367.749 / cushion 5.32% |
| META   |  7.767476 |  $600.710 |  $607.16  |    $4,716.10 |   +$50.10  |  +1.074% |   4.68% | 10% trail / 7 sh GTC / HWM $623.73 / stop $561.357 / cushion 7.54% |
| AVGO   | 11.264102 |  $414.236 |  $412.265 |    $4,643.79 |   -$22.21  |  -0.476% |   4.61% | 10% trail / 11 sh GTC / HWM $442.36 / stop $398.124 / **cushion 3.43% (tightest)** |
| V      | 10.256781 |  $325.053 |  $331.06  |    $3,395.61 |   +$61.61  |  +1.848% |   3.37% | 10% trail / 10 sh GTC / HWM $335.17 / stop $301.653 / cushion 8.89% |
| BRK.B  |  6.883950 |  $484.315 |  $479.775 |    $3,302.75 |   -$31.25  |  -0.937% |   3.28% | 10% trail / 6 sh GTC / HWM $489.36 / stop $440.424 / cushion 8.20% |
| LLY    |  3.341161 |  $997.857 | $1,041.45 |    $3,479.65 |  +$145.65  |  +4.369% (best UPL) |   3.46% | 10% trail / 3 sh GTC / **HWM $1,046.415 ↑↑** / stop $941.7735 ↑↑ / cushion 9.57% |

**Stop-cushion rotation since 16:38Z snapshot:**
- **AVGO** went from 3.69% → **3.43%** (mark $413.36 → $412.265, -0.26% leg
  of an already weak day). Still above the 3% spec-threshold → no log-flag,
  but it has now tightened twice today (5.25% → 3.69% → 3.43%); is the
  Core name to watch first thing at 5/22 01-pre-market.
- **LLY** HWM advanced again $1,043.382 → **$1,046.415** intraday (LLY at
  $1,041.45 / +4.37% UPL — extends its top-UPL position). Stop bumped
  $939.044 → **$941.7735** (+$2.73). 2nd organic trail-advance of the day
  under LM rules.
- All other 6 stops (VOO/MSFT/GOOGL/META/V/BRK.B): HWMs unchanged from
  03-midday → stop prices unchanged. Cushions widened modestly as the
  late-day SPY rally pulled marks up:
  - VOO 8.71% → 9.17% (+46 bp)
  - MSFT 6.65% → 7.02% (+37 bp)
  - META 6.63% → 7.54% (+91 bp)
  - BRK.B 8.08% → 8.20% (+12 bp; BRK.B recovered to -0.94% UPL from -1.07%)
  - GOOGL 5.36% → 5.32% (-4 bp; basically flat — GOOGL traded sideways)
  - V 8.89% → 8.89% (unchanged)
- All 8 trail orders re-verified `OrderStatus.NEW` GTC via live broker
  open-orders query.

**Tightest cushion: AVGO 3.43%** (was AVGO 3.69% at 16:38Z; was GOOGL 4.49%
at 14:30Z). AVGO is the only Core position with a negative UPL today (-0.48%)
and has tightened steadily through the session. Spec-threshold for log/flag
is < 3.00%; we're at 3.43%, ~43 bp of buffer. No flag/WhatsApp triggered
this routine, but AVGO is the top candidate for thesis-check at 5/22
01-pre-market if it gaps down at open.

Strategy slug for all 8: `core-buy-and-hold`. No Core actions taken this
routine.

Total Core committed: $62,729.41 (62.27% of equity)
Cash retained: $38,000.00 (37.73%)

## Swing sleeve
Empty (0 / 8). $15k budget intact. Abort-entries continued from 02-open per
LM-Day-1 plan; no 01-pre-market screen, no Swing positions to verify-stop on
or time-stop out. Earnings-window check N/A. No tighten-to-breakeven action
(no positions ≥ +5% UPL in the sleeve — sleeve is empty).

## Daytrade / Scalp sleeve (intraday only — **FORCE FLAT** at 04-pre-close)
Empty (0 / 5). $10k budget intact. **Force-flat step is a no-op** — zero
open intraday positions at 19:36Z. No roll-to-swing requests in `inbox.md`.
Day-trade count (rolling 5d): **0** / PDT: **False**. ORB/VWAP/scalp/gap
strategies remain dormant — POLYGON_API_KEY still unset.

## Crypto sleeve (24/7)
Empty (0 / 4). $5k budget intact. **No Friday-tighten action** — today is
Thursday (KW 21 day 4). The -8% → -6% trail-tighten + `crypto-weekend-momentum`
Friday-close entry both apply tomorrow (2026-05-22 04-pre-close / 05-close-
summary). No scan re-run this routine (03-midday established the baseline:
all 5 universe names 50<200 DMA downtrend; nothing changed in the 3 hours
between scans — re-running would burn tokens for the same answer).

## Options sleeve (Level 3 enabled)
Empty (0 / 6 contracts). $5k premium budget intact. Options BP $69,365 /
Level 3 ✓. **No Greeks check needed** (zero open contracts → no theta/delta
to track). **No 7-DTE close needed** (no contracts to expire). **No IV-crush
post-earnings exit needed** (no earnings strangles held). **No stale
protective-put cleanup needed** (no hedges open).

## Today's trades

**Zero trades — 04-pre-close HOLD** (abort-entries posture continued from
02-open / 03-midday per the LM-Day-1 fallback plan; Daytrade force-flat is
a no-op on an empty sleeve). 17th consecutive no-action routine extending
the Live-Phase exit-week streak.

Organic broker events (not Bull actions, but recorded for audit):
- **LLY trail HWM bumped** $1,043.382 → $1,046.415 (intraday high reached
  ~15:00Z); stop $939.044 → $941.7735. 2nd LLY HWM advance of the day.
- **AVGO mark drifted further** $413.36 → $412.265 (-0.26%); HWM unchanged.

## Pending (not yet opened)

- **NVDA Swing entry candidate** (`swing-earnings-drift`): blocked — needs
  01-pre-market for post-print Day-1 reaction tape. Re-evaluate next valid
  01-pre-market (5/22 13:00Z).
- **DCA tranche 3 of 3 (legacy Live-Phase)**: deferred to 2026-06-21+ per
  strategy.md v3 LM freeze. No change.

## Recent Closed Positions (last 5)

(none — no closes in entire Live-Phase paper run + LM Day 1)
