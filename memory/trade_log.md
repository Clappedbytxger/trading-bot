# Trade Log

Append-only log of every trade Bull executes (or attempts and aborts). Each entry has a
rationale linking back to `strategy.md` or `research_log.md`.

---

## 2026-05-12T15:14Z — 02-market-open tranche 1 (initial portfolio entry)

Routine: `02-market-open`. Broker: Alpaca paper. Clock: open.
Strategy: Variant C "AI-Capex Barbell" (`strategy.md` v1).
Pre-flight: all guardrails (1, 2, 3, 5, 8) passed. VOO deep_research (Gemini + Tavily)
agreed → no disagreement, position approved.

| # | Side | Symbol | Notional | Filled Qty | Avg Fill | Order ID | Rationale |
|--:|------|--------|---------:|-----------:|---------:|----------|-----------|
| 1 | BUY  | VOO    | $16,667  | 24.732890  | $673.880 | 5d152c94-a103-46ba-8b16-4b97951dda10 | Core ETF, tranche 1/3 toward 50% target. ETF-Core exception in Guardrail #1. |
| 2 | BUY  | MSFT   | $2,333   |  5.709601  | $408.610 | f013114c-c123-4939-baca-583fa8e4bd9f | AI/Quality. TCI exit = sentiment drawdown; thesis intact (fwd P/E 21.1). Tranche 1/3 of 7%. |
| 3 | BUY  | GOOGL  | $2,333   |  6.023830  | $387.295 | 870334b3-3d84-46d8-94dd-27c7b91bfc05 | AI/Quality. Search moat + TPU advantage. Tranche 1/3 of 7%. |
| 4 | BUY  | META   | $2,333   |  3.886520  | $600.280 | f649ace8-5201-446d-97b0-970983131014 | AI/Quality. Capex-fear drawdown = good entry, Q1 beat. Tranche 1/3 of 7%. |
| 5 | BUY  | AVGO   | $2,333   |  5.591774  | $417.220 | 9bc24ac6-0dcf-455b-9d1e-b33d12418104 | AI/Quality. Hyperscaler capex $750B direct tailwind. Tranche 1/3 of 7%. |
| 6 | BUY  | V      | $1,667   |  5.113183  | $326.020 | 3fd5f19a-5f19-4f86-804d-a71d78219353 | Defensive ballast, beta 0.78. Tranche 1/3 of 5%. |
| 7 | BUY  | BRK.B  | $1,667   |  3.440945  | $484.460 | b02676eb-9b8d-4aef-909f-7851d82274ed | Defensive ballast, beta 0.62. Tranche 1/3 of 5%. |
| 8 | BUY  | LLY    | $1,667   |  1.677741  | $993.598 | 18e12e75-ea99-444f-8943-1265f25b29ca | Defensive ballast, beta 0.48. Tranche 1/3 of 5%. |

Total notional committed: $30,999.62. Cash retained: $69,000.00 (for tranches 2 & 3).

### Stop placement (10% trailing, GTC)

Fractional trailing stops rejected by Alpaca (`{"code":42210000,"message":"fractional
orders must be DAY orders"}`). Fell back to integer-share trailing stops on the
floor(qty) of each fill. Fractional remainders (~0.0–0.9 sh per position, total
< 1.5 sh across all 8 positions, ≈ $300 notional unprotected) are temporarily without
trailing-stop coverage. **Logged as lesson; mitigation: in midday or pre-close routine,
use a regular fixed-price `stop` order (Alpaca allows fractional `stop`) at
avg_entry × 0.90 for the fractional remainders OR consolidate after tranche 3 fills.**

| Symbol | Stop Qty | Trail % | TIF | Stop Order ID | Unprotected Fractional |
|--------|---------:|--------:|-----|---------------|------------------------|
| VOO    | 24 | 10 | GTC | 711bae8b-4f15-451b-9985-3cdeeeccee02 | 0.732890 sh |
| MSFT   |  5 | 10 | GTC | 2d01444c-f06c-4285-bb9e-8533b75411af | 0.709601 sh |
| GOOGL  |  6 | 10 | GTC | a77bc906-48c9-4795-89fc-22b991a69f40 | 0.023830 sh |
| META   |  3 | 10 | GTC | 86876110-209a-48ac-8d50-469870b2c2e5 | 0.886520 sh |
| AVGO   |  5 | 10 | GTC | 41b64809-bdbc-49d4-a826-e47a3a905923 | 0.591774 sh |
| V      |  5 | 10 | GTC | 3a463224-73f1-43ee-a01e-57a62b3f0af1 | 0.113183 sh |
| BRK.B  |  3 | 10 | GTC | ebe010d9-d68a-4619-b847-42a41b2b9173 | 0.440945 sh |
| LLY    |  1 | 10 | GTC | b6fbf93e-0342-4a88-880b-36ce69ebe00b | 0.677741 sh |

### Deferred (no order placed)

- **NVDA** — target 7%, deferred. Reason: 97.5% of 52w-high + earnings 2026-05-20.
  Per `strategy.md` caveat, wait for at least one -3% red day post-earnings before
  initiating. Tracked in `portfolio.md` Pending section.

---

## 2026-05-13T13:42Z — 02-market-open tranche 2 of 3

Routine: `02-market-open`. Broker: Alpaca paper. Clock: open.
Strategy: Variant C "AI-Capex Barbell" (`strategy.md` v1).
Pre-flight: all guardrails (1, 2, 3, 5, 8) re-verified — passed. Post-fill VOO weight
33.4% (inside ETF-Core band 45–55% / cap 60%); largest order = VOO $16,667 = 24.2% of
$69k pre-trade cash (cap 30%); position count unchanged at 8/10; no name within 3
trading days of earnings (closest: AVGO 2026-06-03, 14 trading days out); leverage
post-fill 0.62x (cap 2x). Tranche 2 mirrors tranche 1 nominals exactly.

| # | Side | Symbol | Notional | Filled Qty | Avg Fill | Order ID | Rationale |
|--:|------|--------|---------:|-----------:|---------:|----------|-----------|
| 1 | BUY  | VOO    | $16,667  | 24.599451  | $677.535 | 3d2a99c2-6dda-48ff-8cb4-982ccaa9a5fa | Core ETF, tranche 2/3 → 33.4% post-fill, on track for ~50% after tranche 3. |
| 2 | BUY  | MSFT   | $2,333   |  5.812157  | $401.400 | 2d1627f4-78da-4c60-8390-8eaaa1b124bf | AI/Quality tranche 2/3. Thesis intact (fwd P/E 21.07, op-margin 46%). |
| 3 | BUY  | GOOGL  | $2,333   |  6.023443  | $387.320 | 12af7a8c-4492-4cf9-96a3-c007fea7a755 | AI/Quality tranche 2/3. Thesis *strengthened* post Q1 beat (EPS $5.11 vs $2.64 est). |
| 4 | BUY  | META   | $2,333   |  3.880957  | $601.140 | a982fec8-b763-48af-9b5b-34d2fb7f3d77 | AI/Quality tranche 2/3. Capex-fear drawdown -24% vs Hi; fwd P/E 16.66 cheapest mega-cap. |
| 5 | BUY  | AVGO   | $2,333   |  5.672327  | $411.295 | e81ffe27-5bac-4e6d-b338-c9a87e3055f1 | AI/Quality tranche 2/3. Hyperscaler capex tailwind unchanged. |
| 6 | BUY  | V      | $1,667   |  5.143598  | $324.092 | 2911151c-edc3-4bf2-a1f2-18b130981fd8 | Defensive tranche 2/3, beta 0.78. |
| 7 | BUY  | BRK.B  | $1,667   |  3.443006  | $484.170 | f8bb3f15-11db-452f-9e0f-649d4dec1cdd | Defensive tranche 2/3, beta 0.62. |
| 8 | BUY  | LLY    | $1,667   |  1.663420  | $1002.152| 425939e6-3792-48be-9825-14288d63985d | Defensive tranche 2/3, beta 0.48. |

Total notional committed: $30,999.62 (mirrors tranche 1 exactly). Pre-trade cash $69,000
→ post-trade cash $38,000. Equity ticked from $100,003.27 (pre-trade) to $100,056.93
(post-trade, intraday revaluation).

### Stop refresh (10% trailing, GTC) — cancel-and-replace at floor(new_qty)

Per lesson 2026-05-12 (Alpaca fractional-stop limitation), cancelled all 8 prior
trailing stops and re-issued at the new floor(total_qty). Fractional remainders
(aggregate ~3.40 sh ≈ $1,876 notional) remain temporarily without trailing coverage —
acceptable risk on a single-session basis; will consolidate after tranche 3 fills bring
several positions over the next integer share.

| Symbol | Total Qty Post | Stop Qty | Frac Unprotected | Trail % | TIF | New Stop Order ID | Cancelled Old Stop |
|--------|---------------:|---------:|-----------------:|--------:|-----|-------------------|--------------------|
| VOO    | 49.332341 | 49 | 0.332 sh | 10 | GTC | 1bcc50ac-99b8-4693-96ab-b6a2273dc75e | 711bae8b-4f15-451b-9985-3cdeeeccee02 |
| MSFT   | 11.521758 | 11 | 0.522 sh | 10 | GTC | d80cc207-d60a-40b8-a0ff-c62aa4b8866e | 2d01444c-f06c-4285-bb9e-8533b75411af |
| GOOGL  | 12.047273 | 12 | 0.047 sh | 10 | GTC | c73e0611-158e-4403-9839-c10e254e19b2 | a77bc906-48c9-4795-89fc-22b991a69f40 |
| META   |  7.767476 |  7 | 0.767 sh | 10 | GTC | c4e57975-bc6c-41ce-bd4e-1d2968931b16 | 86876110-209a-48ac-8d50-469870b2c2e5 |
| AVGO   | 11.264102 | 11 | 0.264 sh | 10 | GTC | 4fa0abdb-d78e-4627-86ba-f31838e883ae | 41b64809-bdbc-49d4-a826-e47a3a905923 |
| V      | 10.256781 | 10 | 0.257 sh | 10 | GTC | fc1ab752-bc74-4afd-9cc2-58a0722e4187 | 3a463224-73f1-43ee-a01e-57a62b3f0af1 |
| BRK.B  |  6.883950 |  6 | 0.884 sh | 10 | GTC | a8c09e00-b997-4ed9-b07f-fe47219d46ac | ebe010d9-d68a-4619-b847-42a41b2b9173 |
| LLY    |  3.341161 |  3 | 0.341 sh | 10 | GTC | 9a0a47bc-3033-4c43-904b-19d65106c063 | b6fbf93e-0342-4a88-880b-36ce69ebe00b |

Note: re-issued trail-stop loses the prior tranche-1-day HWM (max +1% built up), but
HWM reset is acceptable when re-anchored to the now-larger combined position.

### Deferred (no order placed)

- **NVDA** — target 7%, still deferred. Reason unchanged from 5/12 + 98.7% of 52w-Hi
  today (even closer than yesterday). Earnings 2026-05-20 → guardrail #8 window opens
  2026-05-15. Will re-evaluate after the print.

---

## 2026-05-16T20:50Z — DCA tranche 3 formally DEFERRED per Robin Option B (no order placed)

Routine: `06-weekly-review` follow-up (Robin chat reply). Broker: Alpaca paper. Clock: closed (weekend).
Strategy: Variant C "AI-Capex Barbell" (`strategy.md` v2 — DCA rule updated same day).

Decision: **Robin chose Option B** via Claude Code chat session 2026-05-16T20:45Z.
Robin sent a WhatsApp "B" reply earlier (5/15 or 5/16) which never reached Bull —
CallMeBot is outbound-only. See `memory/inbox.md` Processed entry + lesson
2026-05-16 on WhatsApp asymmetry.

**Action**: T3 deferred ~1 week into post-NVDA + post-Warsh window.
- Earliest re-evaluation: Thu 2026-05-21 in 01-pre-market (post NVDA-print 5/20).
- Likely actual execution: Mon 5/25 or Tue 5/26, conditional on:
  - NVDA block strategy caveat (≥1 -3% red day on AI sleeve before completing T2+T3 on the AI names);
  - No fresh thesis-break events on any of the 8 held names;
  - Macro tape settling post-Warsh first remarks (Mon 5/18).
- T3 sizing on execution day per `strategy.md` v2: VOO capped at
  `min($16,667, 0.30 × cash_at_open)`, residual rolls forward to T4 (and T5 if needed).

No orders placed. No stops modified. No positions touched.

### Why this matters as a trade-log entry

A deferred-but-decided execution is a real trading decision (not a non-event).
Logging here:
- Anchors the decision to a timestamp + a rationale traceable to Robin's reply.
- Closes the rolling "Robin A/B pending" open-question that's been carried in
  every daily file since 2026-05-13.
- Lets the next 01-pre-market read this entry and skip re-asking the question.


---

## 2026-05-20T13:41Z — 02-market-open (no orders placed) — final Live-Phase 02

Routine: `02-market-open`. Broker: Alpaca paper (`paper-api.alpaca.markets` ✓).
Phase: **LIVE PHASE (legacy)** — last 02 under Variant C; flips to Learning-Month
multi-sleeve at the 5/21 01-pre-market.

Plan loaded from `memory/daily/2026-05-20.md` 01-pre-market section: **HOLD all 8,
no trades, NVDA blocked (Earnings T-0 PM), T3 deferred** (now implicitly 6/21+ per v3).

### Decisions
- **All 8 Core positions HOLD.** No new entries, no trims, no stop adjustments
  beyond LLY's broker-side trail auto-advance.
- **NVDA: blocked** by guardrail #8 (earnings tonight). Re-eval Thu 5/21 (first
  Learning-Month routine) under Swing-sleeve framework.
- **T3 DCA: deferred** per Robin Option B 5/16; now further deferred to 6/21+ by
  Learning-Month Core-freeze rule.

### State changes recorded
- **LLY HWM auto-advance**: $1023.29 → $1030.90 (new intraday high at open print);
  broker-side 10% trail auto-advances stop floor $920.96 → $927.81. No manual order
  action (Alpaca trailing-stop tracks HWM server-side).
- **AVGO cushion re-tightening**: pre-mkt 4.68% → 13:41Z 3.86% on intraday give-back
  from $417.65 → $414.12. Still inside 10% trail design band; tightest in book again.
  No spec-trigger fired (give-back < -1% intraday); monitoring continues.

### Account & alpha
- Equity $100,259.51 (vs Tue close +$132.90 / +0.133%; vs Mon close -$426.84 / -0.424%).
- Day-alpha vs SPY (Tue close → 13:41Z): Bull +0.133% vs SPY +0.246% → **-11.3 bp**.
- 2-day-alpha vs SPY (Mon close → 13:41Z): Bull -0.424% vs SPY -0.422% → **-0.2 bp**
  (flat across full Tue+Wed-open arc).
- YTD: Bull +0.260% vs SPX +7.959% → Alpha -7.700% (-13.2 bp widening vs Tue close).

### Why this matters as a trade-log entry

This is the **11th consecutive no-action routine** since 5/18. Logging here:
- Closes the loop on the 02-market-open routine deliberately, rather than
  silently skipping (per lesson 2026-05-16: no-action days are intentional, not lazy).
- Records LLY HWM advance + AVGO cushion tightening as the only state changes
  that occurred without a manual order.
- Marks the last Live-Phase 02-market-open. Tomorrow this entry-log section flips to
  per-sleeve tagged entries with mandatory `sleeve:` + `strategy:` fields per ALM-1.

---

## 2026-05-20T16:39Z — 03-midday (no orders placed) — final Live-Phase 03

Routine: `03-midday`. Broker: Alpaca paper (`paper-api.alpaca.markets` ✓).
Phase: **LIVE PHASE (legacy)** — last 03 under Variant C; flips to Learning-Month
multi-sleeve at the 5/21 03-midday (which also extends to weekends per v3 cron).

Plan loaded from `memory/daily/2026-05-20.md` 02-market-open section: **HOLD all 8,
no trades, NVDA blocked (Earnings T-0 PM), T3 deferred** (now implicitly 6/21+ per v3).

### Decisions
- **All 8 Core positions HOLD.** No new entries, no trims, no stop adjustments
  beyond LLY's broker-side trail auto-advance on a new intraday HWM.
- **NVDA: blocked** by guardrail #8 (earnings tonight 20:00Z+). Re-eval Thu 5/21
  (first Learning-Month routine) under Swing-sleeve framework.
- **T3 DCA: deferred** per Robin Option B 5/16; now further deferred to 6/21+ by
  Learning-Month Core-freeze rule.

### State changes recorded (broker-side only, no manual orders)
- **LLY HWM auto-advance**: $1030.90 → $1037.88 (+$6.98) on a fresh intraday high
  that printed between 13:41Z and 16:39Z. Broker 10% trail-stop auto-advances stop
  floor $927.81 → $934.092. Mark pulled back to $1006.07 by 16:39Z = -3.06% off the
  new HWM (round-trip move). No manual action — Alpaca tracks HWM server-side.
- **AVGO cushion-bleed broken**: 02-open 3.86% (tightest in book) → 16:39Z 4.86%
  (+100 bp) on intraday recovery $414.12 → $418.46. UPL flipped -0.03% → +1.02%.
  Bounce that started overnight (+1.86%) followed through after the open give-back.
- **GOOGL cushion slip**: 02-open 5.46% → 16:39Z 4.32% (-114 bp). Now tightest in
  book. Mark $388.97 → $384.35 = -1.19% intraday. UPL +0.43% → -0.76%. Still >3%
  spec-threshold; no log-flag required. Tape-driven, not name-specific (no Gemini
  scan triggered — no fresh catalyst).

### Account & alpha (16:39Z vs 02-open 13:41Z)
- Equity $100,376.39 (intraday +$116.88 / +0.117% vs 02-open).
- vs Tue close: +$249.78 / +0.249%. SPY +0.698% → **day-alpha -44.8 bp** (widened
  from -11.3 bp at 02-open as mid-session breadth rally outpaced Bull's concentrated
  AI+defensive book).
- vs Mon close: -0.308% vs SPY +0.028% → 2-day-alpha **-33.6 bp** (re-opened from
  -0.2 bp at 02-open by LLY round-trip + GOOGL slip).
- YTD: Bull +0.376% vs SPX +8.448% → Alpha -8.072% (-37.2 bp widening vs 02-open).

### Why this matters as a trade-log entry

This is the **12th consecutive no-action routine** since 5/18. Logging here:
- Records broker-side state changes (LLY HWM advance, AVGO cushion-bleed broken,
  GOOGL new tightest cushion) for audit continuity — none of these were manual
  orders, but they're material to the next routine's HOLD/CUT decision-making.
- Closes the loop on the 03-midday routine deliberately, rather than silently
  skipping (per lesson 2026-05-16: no-action days are intentional, not lazy).
- Marks the **last Live-Phase 03-midday**. Tomorrow this entry-log section flips
  to per-sleeve tagged entries with mandatory `sleeve:` + `strategy:` fields per
  ALM-1, and includes Crypto sleeve actions on weekends.

