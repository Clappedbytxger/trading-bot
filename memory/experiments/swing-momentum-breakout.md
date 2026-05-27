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
