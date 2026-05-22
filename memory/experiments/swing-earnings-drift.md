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

### Outcome (TBD — to be filled in post-exit)

- Exit date:
- Exit price / exit reason:
- Realized P&L $:
- Realized R-multiple:
- Days held:
- Delta vs expectation:
- Lesson:
