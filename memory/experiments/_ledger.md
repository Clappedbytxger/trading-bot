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
| core-buy-and-hold          | Core      | active | 16 fills (T1+T2, no closes) | — | — | +$951.01 (UPL) | $0 (no closes) | — | -8.57% (Live-Phase carryover + LM Day 2 EOD) | 2026-05-22 05-close-summary |
| swing-momentum-breakout    | Swing     | active | 0 (ARM WATCH → MISSED 13:30-14:00Z; intraday H $315 → C $304.66 fade; re-arm on close <$290) | — | — | $0.00 | $0 | — | — | 2026-05-22 05-close-summary |
| swing-mean-reversion       | Swing     | active | 0 (1 SKIP = INTU thesis-risk) | — | — | $0.00 | $0 | — | — | 2026-05-22 02-market-open |
| swing-quality-pullback     | Swing     | active | **1 open (NVDA)** | — | — | -$45.02 (UPL) | $0 (no closes) | — | — | 2026-05-22 05-close-summary |
| swing-earnings-drift       | Swing     | active | **1 open (RL)** | — | — | +$0.04 (UPL) | $0 (no closes) | — | — | 2026-05-22 05-close-summary |
| swing-insider-buys         | Swing     | paused | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| swing-short-rejection      | Swing     | active | 0 (1 WATCH = AAPL — EOD final candle UP +1.00% close $309.13 with fresh $311.40 52w-Hi extension; PASS today, re-watch Tue 5/26) | — | — | $0.00 | $0 | — | — | 2026-05-22 05-close-summary |
| swing-short-fundamental    | Swing     | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-orb               | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-vwap-pullback     | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-gap-fade          | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-gap-go            | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| scalp-tape                 | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| daytrade-news-catalyst     | Daytrade  | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| crypto-trend-follow        | Crypto    | active | 0 (1 scan, no signal) | — | — | $0.00 | $0 | — | — | 2026-05-21 05-close-summary |
| crypto-weekend-momentum    | Crypto    | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| crypto-mean-reversion      | Crypto    | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-long-call-momentum | Options   | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-protective-put     | Options   | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-vertical-bull-call-spread | Options | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-earnings-strangle  | Options   | active | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |
| options-cash-secured-put   | Options   | paused | 0 | — | — | $0.00 | $0 | — | — | 2026-05-20 |

## Sleeve roll-ups

| Sleeve | Cash Budget | Used | Open positions | Cumulative P&L | Cumulative Alpha vs SPY |
|---|---:|---:|---:|---:|---:|
| Core     | $62,000 | $62,951.01 (live mark, +$951.01 UPL) | 8 | +$951.01 / +1.534% (10-day Live-Phase + LM Day 1-2 EOD) | -8.57% Live-Phase + LM Day 2 EOD |
| Swing    | $15,000 | $3,500 cost (NVDA $2k + RL $1.5k) | 2 | -$44.98 UPL (NVDA -2.25% cushion 2.81%, RL +0.003% cushion 7.00%) | — (Day 1 of hold; no realized P&L yet) |
| Daytrade | $10,000 | $0      | 0 | $0 | — |
| Crypto   | $5,000  | $0      | 0 | $0 | — |
| Options  | $5,000  | $0      | 0 | $0 | — |
| Cash reserve | $3,000 | — (of $34,500 cash total, ≥$3k reserved per ALM-2) | — | — | — |

## Weekly bandit log (06-weekly-review writes here)

(none yet — first bandit review will fire Fri 2026-05-29 in 06-weekly-review)

## Daily refresh log

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
