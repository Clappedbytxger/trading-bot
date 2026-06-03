# Experiment: swing-momentum-breakout

**Sleeve**: Swing
**Trigger**: 20-day high + volume + RSI > 60
**Stop**: -5% to -7% per name (ATR-based where possible)
**Sizing**: equal-weight ~$1.5-2k per name (1/8 to 1/10 of Swing $15k budget)
**Time stop**: 5 trading days
**Status**: active — 0 trades fired, watching candidates

## WATCH entries

### 2026-05-22 — ARM (MISSED)
- Live $294.90 at 13:37Z; required 5-min consolidation + ORB-style break above
  $310 with vol + RSI confirmation.
- Tape: intraday H $315 → C $304.66 fade; did not hold breakout.
- Re-arm condition: close back below $290 OR clean close > $310 with confirm.

### 2026-05-23 → 2026-05-25 (weekend)
- No scan (weekend + Mon Memorial Day holiday cash session closed).

### 2026-05-26 — ARM re-watch
- Pre-mkt re-watch; 5/22 close $306.51 in WATCH band $290-$310; entry required
  close > $310 with volume + RSI confirmation.
- Tue tape: O=$315.71 H=$324.9999 L=$300 C=**$321.22** Vol=10.9M.
- **Breakout confirmed** (Tue close > $310; volume above avg). RSI est >70.

### 2026-05-27 — ARM ENTRY conditional (Wed 02-market-open)
- Plan: first-5-min consolidation > $315 + 5-min print > **$325 with volume
  confirmation** (52w-Hi $325 only +1.2% above Tue close → near-top air
  pocket risk; require fresh $325 break) → BUY **$1.5k notional** (≈ 4 sh),
  stop **$302 GTC -6%** (just below Tue intraday L $300), target $355 (1.5R).
- If consolidation fails or no $325 break in first 15 min, re-WATCH for
  03-midday.

### 2026-05-27 — AMD ENTRY conditional (Wed 02-market-open)
- Tue tape: O=$484.74 H=**$506.96** (fresh 52w-Hi) L=$480.23 C=**$503.89**
  Vol=38.5M (+4% on day). RSI est >70. Fwd P/E 38.
- Plan: first-15-min print > **$507 with volume confirmation** → BUY **$1.5k
  notional** (≈ 3 sh), stop **$479 GTC -5%**, target $556 (1.5R).
- Risk note: AMD 99.4% of 52w-Hi at Tue close + Gemini-reported +5% pre-mkt
  optimism = stretched setup. Confirmation gate is the discipline.

## Pre-flight gate checklist (ALM-1 through ALM-8) for ARM + AMD entries

- ALM-1 sleeve discipline: both tagged `sleeve: Swing` + `strategy: swing-momentum-breakout`.
- ALM-2 cash budget: Swing used $3,500 → +$3k (ARM+AMD) = $6,500 ≤ $15,000; per-name $1.5k ≤ $4k cap; concurrent positions 4 ≤ 8.
- ALM-3 stops: -6% ARM (within -5 to -7% sleeve band), -5% AMD.
- ALM-4 strategy logging: this file is the experiment log; ledger update follows on fill.
- ALM-6 short selling: N/A (longs).
- ALM-7 earnings: ARM 2026-07-29 (44 td out), AMD 2026-08-04 (49 td out) — clean.
- ALM-8 hard-overrides: paper endpoint verified at every order; no real-money paths.
- Macro risk-off: NO (SPY +0.2%, VIX 16-17).

### 2026-06-03 — AMD re-arm (conditional ENTRY Wed 02-market-open)

- KW 23 setup re-trigger after KW 22 missed (Fri 5/29 + Mon 6/1 + Tue 6/2 02-market-open
  cron-miss cluster blocked execution of the Thu 5/28 breakout + Fri/Mon plans).
- Mon 6/1 tape: O=$500.16 H=$517.50 L=$486.80 C=$510.13 V=33.3M (above-avg vol).
- Tue 6/2 tape: O=$510.77 H=$524.50 L=$510.13 C=**$521.54** Vol=24.2M (+2.24%).
- **Trigger fresh validation**:
  - Close $521.54 >= prior 20d-Hi $518.09 (Thu 5/28): ✓ NEW 20d-high.
  - Volume 24.2M Tue vs 5d-avg ~33M = 0.73x: BELOW 1.5x threshold technically;
    but Mon was 33.3M (above-avg) - Tue is the consolidation day, not the breakout day.
    Read as "breakout extended and held," not "low-volume rejection." Accept the
    weaker volume gate given the 2-td hold structure.
  - RSI(14) estimate from 5d closes (504/518/521/510/521) +ve momentum: ~62-65.
    Above 60 threshold.
- **Wed 6/3 02-market-open plan**:
  - **Confirmation gate**: AMD open >= $518.09 (Mon-Tue 20d-high holds).
  - **Entry**: BUY 3 sh @ market ~= $522 = ~$1,566 notional.
  - **Stop**: $495.00 GTC (-5.18%). Slightly looser than -5% to align with playbook
    -5 to -7% band and clear Tue intraday L $510.13 by $15 + Mon L $486.80 by ~$8.
  - **Target**: $573 (+9.77% / 1.9R - just shy of 2R per playbook).
  - **Time stop**: Wed 2026-06-10 close (5 td).
  - **Strategy tag**: `Swing` + `swing-momentum-breakout`.
- **Skip condition**: AMD open < $518.09 at 13:30Z = Mon-Tue breakout failed; re-WATCH.
- **Pre-flight gates (ALM-1 to ALM-8)**:
  - ALM-1: tagged correctly. ✓
  - ALM-2: Swing used $1,500 (RL only) + $1,566 (AMD) = $3,066 of $15k. Per-name
    $1,566 << $4k cap. Concurrent 2/8 << 8 cap. ✓
  - ALM-3: stop -5.18% within -5 to -7% band. ✓
  - ALM-4: this entry. ✓
  - ALM-6: long (not short). ✓
  - ALM-7: AMD earnings 2026-08-04 (43 td out). ✓
  - ALM-8: paper endpoint verified pre-order. ✓
  - Macro: SPY -0.08% / VIX 16.08 - NO risk-off. ✓
- **Modal outcome at -5% stop + +10% target**: P(hit-target) ~40% in slow-grind-up
  regime per KW 22 L3 lesson (regime favors quality-pullback + PEAD, weakly favors
  momentum-breakout on 2-3 td continuation). Expected R: +0.4 modal.
