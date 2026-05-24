# Experiment Log — `swing-quality-pullback`

Sleeve: Swing. Status: active. Playbook reference: `memory/playbook.md`.

**Thesis (one line):** Quality compounders (ROE > 15%, op margin > 20%, rev growth > 10%) that pull back 5-10% from 52w-Hi without thesis-break offer favorable risk/reward.

---

## 2026-05-22 — Entry #1: NVDA

- **Routine**: 02-market-open, 13:37:24Z.
- **Entry trigger fired**: NVDA $219.92 at the open, within ±2% of yesterday's
  $219.51 reference. Pullback -6.88% from 52w-Hi $236.54.
- **Fundamentals filter check**: ROE 114.3% > 15% ✓ / op margin 65.6% > 20% ✓ /
  rev growth 85.2% > 10% ✓ / no negative earnings revisions (post-print PT
  raises are all UP: HSBC, MS, Jefferies, Baird, BofA, GS).
- **Catalyst**: Q1 FY27 rev $81.6B +85% YoY beat $78.8B consensus; non-GAAP EPS
  $1.87 beat $1.75-1.77; **Q2 guide $91B vs Street $86-87B** (huge raise,
  ex-China). Hyperscaler rev $37.9B +115% YoY. Day-1 reaction -1.77% on 5/21
  read as "priced-in," not thesis-break.
- **Position size**: $2,000 notional → 9.092513 sh @ $219.9612 avg.
- **Stop**: $208.96 GTC (9 sh; 0.092513 sh uncovered slice ≈ $20) → -5% from fill.
- **Target**: +7% (~$235.36) OR retest of 52w-Hi $236.54, whichever first.
- **Time stop**: 7 trading days → exit on 2026-06-02 close if neither target
  nor stop hit.
- **Expected R-multiple**: 1.4R (target +7% / stop -5%).
- **Order IDs**: buy `b9755836-53af-4198-8df3-5511e453af3e`, stop
  `ffb5e5a9-50fb-4e39-abef-849d72b8f323`.
- **Risk**: Big-cap AI capex digestion overhang (sector risk); single-name
  concentration if a sentiment air-pocket hits the AI block (NVDA/AVGO/MSFT all
  correlated). Mitigated by -5% hard stop.

### Midday updates

- **2026-05-22 16:42Z (03-midday Day 1 of hold)**: mark $216.475 (vs entry
  $219.9612, -1.585% / -$31.70 UPL). Stop $208.96 intact (cushion 3.47% —
  well above the playbook -5% trigger). Distance to target $235.36: 8.71%
  upside still required. No action taken; UPL within the routine-spec
  drift band (-2% / +3%). Time-stop date 2026-06-02 unchanged.
- **2026-05-22 19:36Z (04-pre-close Day 1 of hold)**: mark $215.5401 (vs
  entry $219.9612, **-2.010% / -$40.20 UPL**). Stop $208.96 intact
  (`OrderStatus.NEW` GTC verified at broker, id `ffb5e5a9-50fb-4e39-abef-
  849d72b8f323`). **Cushion compressed 3.47% → 3.05% intraday** (tightest
  since fill) but still above the playbook -5% trigger. Distance to target
  $235.36: 9.20% upside still required. No tighten-to-breakeven (rule
  requires +5%+ UPL — NVDA is at -2.01%). No time-stop hit (today is fill
  day; first time-stop check on 6/2 close). **No action**; UPL drift -1.5%
  below entry over Day 1 is within the playbook expected variance for a
  $1.5-2k 7-day swing. Time-stop date 2026-06-02 unchanged. Flagged for
  re-check on Tue 5/26 open (Mon 5/25 = Memorial Day closed) for any
  further cushion compress to <2% which would warrant a tighter management
  posture.
- **2026-05-22 20:16Z (05-close-summary Day 1 EOD)**: EOD mark $215.01
  (vs entry $219.9612, **-2.251% / -$45.02 UPL**). Stop $208.96
  `OrderStatus.NEW` GTC verified live post-close. **Cushion compressed
  further 3.05% → 2.81% into the close** (mark slipped another $0.53 from
  04-pre-close mark $215.54). Tightest cushion since fill, by a wide
  margin. Distance to target $235.36: 9.46% upside required. NVDA -2.25%
  Day 1 still within the -5% stop and matches the historical "Day 1 fade
  after a +85% YoY earnings print is priced-in" pattern; no thesis-break
  catalyst surfaced (no fresh AI-capex digestion headlines on the wires
  post-close per Gemini macro scan-skip). No tighten-to-breakeven (rule
  requires +5%+ UPL). **No action.** Time-stop date 2026-06-02 unchanged.
  **Day 1 P&L attribution**: NVDA contributed -$45.02 to the Bull EOD,
  the single biggest negative contributor outside the Core mark drift.
  **Watch on Tue 5/26 open**: if cushion compresses to <2% (mark
  ≈ $213.22), tighten posture — consider half-out at market to lock the
  remaining 1-1.5% cushion against a gap-down through the stop. Note:
  Mon 5/25 = Memorial Day, US market closed; weekend headlines could
  meaningfully reprice NVDA at Tue's open.

- **2026-05-24 16:36Z (03-midday Day 1+weekend hold, Sun)**: weekend
  mark $215.33, identical to Sat 5/23 snapshot (broker's weekend quote
  stream produced no fresh tick Sat → Sun on NVDA). UPL **-2.105%
  / -$42.11**, cushion **2.96%** — both unchanged from Sat. Stop $208.96
  `OrderStatus.NEW` GTC verified live. No action. Time-stop date
  2026-06-02 unchanged (Mon 5/25 = Memorial Day, US market closed → first
  live tick on this position arrives Tue 5/26 13:30Z open). **Tue 5/26
  open watch reaffirmed**: if cushion compresses to <2% (mark ≈ $213.22),
  tighten posture — consider half-out at market to lock the remaining
  1-1.5% cushion against a gap-down through the stop. Long-weekend
  AI-capex headline risk possible but no specific catalyst on the
  calendar.

### Outcome (TBD — to be filled in post-exit)

- Exit date:
- Exit price / exit reason:
- Realized P&L $:
- Realized R-multiple:
- Days held:
- Delta vs expectation:
- Lesson:
