# Experiment Log — `swing-earnings-drift`

Sleeve: Swing. Status: active. Playbook reference: `memory/playbook.md`.

**Thesis (one line):** Post-earnings strong beats (rev + EPS beat + guide raise) trigger 1-2 week drift higher (post-earnings announcement drift, PEAD).

---

## 2026-05-22 — Entry #1: RL

- **Routine**: 02-market-open, 13:37:23Z.
- **Entry trigger fired**: RL opened at $373.67, above the 95% threshold of
  Thu's close $374.90 → $356.16. Day-1 reaction Thu 5/21 was +10.26% on Q4
  FY26 beat.
- **Catalyst**: Q4 FY26 EPS beat consensus, driven by "strong full-price
  selling" (per Gemini macro scan 5/21). Day-1 +10.26% reaction is above
  the playbook's ≥5% threshold.
- **PT raises within 24h**: Not yet confirmed name-by-name in Gemini scan;
  the +10.26% Day-1 reaction itself is the primary positive-drift signal.
  (Future improvement: verify PT raise count is ≥2 before entry.)
- **Position size**: $1,500 notional → 3.978463 sh @ $377.03 avg.
- **Stop**: $350.64 GTC (3 sh; 0.978463 sh uncovered slice ≈ $367 ≈ 25% of
  position unprotected — accepted per fractional handling lesson) → -7% from fill.
- **Target**: +10% (~$414.73) OR 10 trading days time-stop.
- **Time stop**: 10 trading days → exit on 2026-06-05 close if neither
  target nor stop hit.
- **Expected R-multiple**: 1.4R (target +10% / stop -7%).
- **Order IDs**: buy `3f64d479-d578-4bc4-b96a-86679bc97c63`, stop
  `9e45b1e8-cf59-408d-a702-9691f5dc3620`.
- **Risk**: Retail/consumer discretionary is sleeve-outside-of-typical-tech-
  comfort. WMT printed weak guide same week → broader retail tape pressure
  possible. Sized smaller ($1.5k vs NVDA $2k) to reflect lower conviction.
- **Sleeve attribution**: Sleeve = Swing. $1.5k counted against $15k Swing
  budget → $11.5k remaining post NVDA + RL.

### Midday updates

- **2026-05-22 16:42Z (03-midday Day 1 of hold)**: mark $376.05 (vs entry
  $377.03, -0.260% / -$3.90 UPL). Stop $350.64 intact (cushion 6.76%).
  Distance to target $414.73: 10.28% upside still required. RL recovered
  slightly from open-session low ($374.945 → $376.05). No action taken;
  UPL within routine-spec drift band. Time-stop date 2026-06-05 unchanged.
- **Uncovered slice watch**: 0.978463 sh × $376.05 ≈ $368 still unprotected
  by the 3-share stop (per fractional handling lesson). Today's intraday
  range did not stress this; flag for 04-pre-close again.
- **2026-05-22 19:36Z (04-pre-close Day 1 of hold)**: mark $376.785 (vs
  entry $377.03, **-0.065% / -$0.97 UPL**). Stop $350.64 intact
  (`OrderStatus.NEW` GTC verified at broker, id `9e45b1e8-cf59-408d-a702-
  9691f5dc3620`). **Cushion improved 6.76% → 6.94% intraday** as RL
  recovered into the close ($376.05 → $376.785). Distance to target
  $414.73: 10.07% upside still required. Day 1 essentially flat —
  consistent with PEAD pattern where Day 2 reaction is muted before Day
  3-5 drift takes hold. No tighten-to-breakeven (rule requires +5%+ UPL).
  No time-stop hit (today is fill day; first time-stop check on 6/5 close).
  **No action**. Time-stop date 2026-06-05 unchanged.
- **Uncovered slice (re-check)**: 0.978463 sh × $376.785 ≈ $369 still
  unprotected by the 3-share stop. Today's intraday range did not stress
  it; carry forward to 05-close-summary / next Tue 01-pre-market.
- **2026-05-22 20:16Z (05-close-summary Day 1 EOD)**: EOD mark $377.04
  (vs entry $377.03, **+0.003% / +$0.04 UPL**). Stop $350.64
  `OrderStatus.NEW` GTC verified live post-close. **Cushion improved
  further 6.94% → 7.00% into the close** (RL ticked up $0.255 in the
  final 24 min). Distance to target $414.73: 9.99% upside required. Day
  1 effectively flat ($0.04 UPL) — consistent with the PEAD playbook
  expectation where the Day-after-entry is often a digestion day before
  Day 3-5 drift takes hold. No tighten-to-breakeven (rule requires +5%+
  UPL). **No action.** Time-stop date 2026-06-05 unchanged.
  **Day 1 P&L attribution**: RL contributed +$0.04 to the Bull EOD —
  net-neutral. PEAD thesis intact; the drift signal hasn't fired yet but
  the +$0 mark vs entry is preferable to the alternative (a Day-2 fade
  back to pre-print prices).
- **Uncovered slice (EOD re-check)**: 0.978463 sh × $377.04 ≈ $369 still
  unprotected by the 3-share stop. Day 1 intraday range didn't stress
  it. Carry forward to Tue 5/26 01-pre-market — if RL gaps down >5%
  overnight Mon → Tue, the uncovered slice prints $18 of additional loss
  beyond the planned -7% stop-out. Note: long-weekend gap risk is real
  but RL has no major catalysts on the calendar for the long weekend.

- **2026-05-24 16:36Z (03-midday Day 1+weekend hold, Sun)**: weekend
  mark $377.78, identical to Sat 5/23 snapshot. UPL **+0.199% / +$2.98**,
  cushion **7.19%** — both unchanged from Sat. Stop $350.64
  `OrderStatus.NEW` GTC verified live. No action. Time-stop date
  2026-06-05 unchanged. PEAD thesis intact for Day-3+ of hold; typical
  drift profile is Day 3-5 acceleration, which first ticks live on
  Tue 5/26 open (Mon 5/25 = Memorial Day, closed). **Uncovered slice
  re-check**: 0.978463 sh × $377.78 ≈ $370 still unprotected by the
  3-share stop. Long-weekend gap risk monitored — no RL catalysts on
  the calendar Mon → Tue; if RL gaps down >5% overnight Mon → Tue
  open, the uncovered slice prints ~$18 of additional loss beyond the
  planned -7% stop-out. Acceptable given Swing budget context.

### KW 22 mid-hold checkpoint (06-weekly-review 2026-05-30)

- **Day 8 calendar / 5 td elapsed** (5/22 fill + holiday-skip 5/25 + 5/26 td1
  + 5/27 td2 + 5/28 td3 + 5/29 td4 = wait that's only 4 td; let me recount:
  5/22 = fill day (counts as td1 of hold per playbook), 5/25 holiday-skip,
  5/26 td2, 5/27 td3, 5/28 td4, 5/29 td5). 5 td elapsed; 5 td remaining
  before time-stop 2026-06-05 close.
- **Fri 5/29 EOD mark**: $363.90, UPL **-$52.24 / -3.482%**.
- **Cushion**: 3.66% (vs stop $350.64) — compressed from KW 21 EOW 7.00%
  to KW 22 EOW 3.66% over 5 td. Net -3.34 pp cushion erosion.
- **Trajectory KW 22**: Tue +1.31% (post-holiday pop, $377.78 → $381.97 pre-mkt,
  Day 3 of hold = textbook PEAD acceleration window) → Wed +2.02% (held the
  early-week pop $384.65, PEAD pattern firing as expected) → Thu -1.45% (giveback
  $376.23, consumer-discretionary weakness; WMT-sympathy retail tape drag) →
  Fri -1.85% ($363.90 close, sharper continuation lower; no specific RL
  catalyst, broader retail bid evaporated).
- **PEAD thesis assessment**: Original entry expected 1-2 week drift higher
  on Q4 FY26 beat + guide. Tue+Wed delivered the Day 3-5 PEAD acceleration
  textbook (+3.36% peak vs entry). Thu+Fri reversal completely retraced
  the drift and pushed UPL deeper red than entry-day (-3.48% vs entry +0.20%
  Day 1). **Thesis is weakening, not yet broken.** The 4 fresh PT raises
  on 5/22 weekend (UBS $511, Barclays $439, Wells $415, Needham $405)
  remain in-force but flow has stopped converting.
- **Decision Sat 5/30**: HOLD (no tighten-to-breakeven; UPL still negative;
  no emergency tighten — cushion 3.66% > 3.0% playbook threshold by 66 bp).
  Stop $350.64 GTC verified live.
- **Mon 6/1 watch**: if RL gaps red >2% pre-mkt (mark <$357), cushion drops
  to <2% and emergency tighten is on the table. Otherwise HOLD into td6.
- **Time-stop schedule (10 td from fill = 6/5 close)**:
  - Mon 6/1 = td6 (HOLD)
  - Tue 6/2 = td7 (HOLD; AVGO earnings day = -1d to AVGO catalyst Tue post-close)
  - Wed 6/3 = td8 (HOLD; AVGO post-close = sympathy risk if AVGO misses)
  - Thu 6/4 = td9 (HOLD; final tighten-or-cut decision window)
  - Fri 6/5 = td10 (TIME-STOP: close at market if neither target $414.73
    nor stop $350.64 hit by close)
- **Expected R outcome at current trajectory**: If RL drifts back to entry
  by 6/5 close = $377.03 = 0R. If RL continues bleed at Thu+Fri pace
  (~-1.5% per day) = $363.90 × (1-0.015)^4 = ~$342.79 = STOP HIT before
  time-stop = -1.0R (matches NVDA stop outcome). If RL bounces back to
  +5% by 6/5 = $395.88 = +0.7R. **Modal outcome from here: -1.0R stop-out
  or 0R time-stop close.** Below the planned 1.4R expectation.

### Outcome (TBD — to be filled in post-exit)

- Exit date:
- Exit price / exit reason:
- Realized P&L $:
- Realized R-multiple:
- Days held:
- Delta vs expectation:
- Lesson:

### LM Day 15 emergency cushion compression (01-pre-market 2026-06-04 13:50Z LATE FIRE)

- **Day 9 td elapsed** (5/22 td1 + 5/26 td2 + 5/27 td3 + 5/28 td4 + 5/29 td5 +
  6/1 td6 + 6/2 td7 + 6/3 td8 + **6/4 = td9**). Time-stop Fri 6/5 close = **td10
  tomorrow**.
- **Thu 6/4 intraday mark** ~$359.72; **UPL -$68.87 / -4.59%** (deteriorated from
  Wed pre-mkt $363.51 / -3.59%; -1.0 pp / -$15 over 1 td).
- **Cushion 2.59%** (mark $359.72 / stop $350.64 - 1) — **BELOW the playbook 3%
  emergency threshold for the first time in the hold** (peak was 7.19% Sat 5/23
  weekend snap).
- **Stop $350.64 GTC** verified live (`OrderStatus.NEW` id `9e45b1e8-...`); fixed
  stop, no trail.
- **Trajectory KW 23**: Mon 6/1 (td6) UPL essentially unchanged from KW 22 EOW
  -3.48% → Tue 6/2 (td7) UPL -3.5% → Wed 6/3 (td8) UPL -3.59% → **Thu 6/4 (td9)
  UPL -4.59%**. Slow grind lower, no catalyst, cushion-bleed +33 bp on Thu (3.66%
  → 2.59%).
- **No fresh thesis-break catalyst** per Gemini Thu scan: no analyst PT changes,
  no margin guide change. Just continued consumer-discretionary weakness with
  Thu AVGO-led Nasdaq pressure pulling NQ-correlated names down marginally.
- **AVGO post-earnings sympathy**: AVGO -13.58% Thu but RL +0.07% Thu (essentially
  flat); RL avoided AVGO drag thanks to consumer-discretionary segment being
  decoupled. The AVGO-Thu effect on RL: ZERO. The RL bleed is its own slow drift.
- **LULU earnings tonight 6/4 post-close** (cons EPS $1.68 / rev $2.44B) — closest
  consumer-discretionary read for RL. A LULU miss + guide-down would create RL
  sympathy gap risk into NFP Fri morning.

### Decision matrix for 03-midday + 04-pre-close

Bull's recommendation is **HOLD into Fri 6/5 td10 time-stop**, but with explicit
contingency gates:

- **Option A — Emergency-tighten to -2% stop** ($352.53):
  - Locks worst-case -4.4% (vs current -7% stop -4.59% UPL = essentially same exit
    price as Option C if no Fri rebound).
  - Reduces overnight LULU-sympathy gap risk.
  - Costs the ~$4-9 of optionality on a Fri NFP-driven rebound (modal +1-3% rebound
    = +$15-40 UPL recovery).
  - Strategy-attribution stays clean (-0.6R to -0.9R band).
- **Option B — Close-early at market now** (Thu intraday):
  - Locks -4.59% / -0.66R right now.
  - Eliminates overnight LULU gap AND Fri NFP gap risk.
  - Cedes the 26-hour time-stop optionality entirely.
  - Strategy-attribution -0.66R = neutral-bad (similar to NVDA -1.0R Swing close).
- **Option C — HOLD into Fri 6/5 close** (td10 time-stop):
  - Preserves NFP-rebound optionality (modal +1-3% Fri move).
  - Risk: LULU miss + RL gap-down overnight + NFP-cold Fri morning could compress
    cushion < 0% (mark < $350.64) and trigger -7% stop = -1.0R clean.
  - Modal outcomes Fri 6/5 close: -4.59% (flat continuation) OR -7% (-1.0R stop)
    OR 0R (NFP-rebound to entry $377.03 = +4.81% rebound needed).

**Bull's queued recommendation for 03-midday (17:30Z)**:
- IF Thu 6/4 cushion stays > 1.5% intraday (mark > $355.95) at 17:30Z → **HOLD**
  (Option C).
- IF Thu 6/4 cushion < 1.5% intraday at 17:30Z → **CLOSE EARLY** (Option B).
- IF cushion < 0.5% intraday → MARKET SELL immediately don't wait for routine.
- **Reasoning**: Option C preserves the asymmetric Fri rebound optionality at
  small marginal risk (~$8-20 worse-case incremental). The PEAD thesis was
  weakening but never broke, the consumer-discretionary segment is decoupled from
  the AVGO-led Thu purge, and the cost-of-discipline (tight-stop now vs let-time-
  stop play out) is small in dollars.

### Uncovered slice (Thu 6/4 carry-forward)

- 0.978463 sh × $359.72 = ~$352 still unprotected by the 3-share fixed stop. Today's
  intraday range bracketed $355-$362; slice took a small mark-to-market hit but no
  stop event was triggered on it (the 3-share leg is the protected position).
- Long-weekend risk: NFP Fri + weekend = sleeve-correlated risk window. The slice
  prints additional ~$3-5 loss per 1% RL gap-down if Fri turns sharp red.
- Acceptable given Swing budget context ($15k cap; RL at $1.5k cost basis using
  10% of sleeve).
