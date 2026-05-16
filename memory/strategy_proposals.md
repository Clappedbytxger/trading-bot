# Strategy Proposals

Append-only log of proposed `strategy.md` changes. Robin reviews these on GitHub and
either edits `strategy.md` directly or replies "approve" via WhatsApp. Bull may NOT
edit `strategy.md` autonomously — only this file.

Format:
```
## <ISO date> — Proposed change
**Current rule:** <quote from strategy.md>
**Proposed change:** <new wording>
**Evidence:** <bullets>
**Risk if wrong:** <1-2 sentences>
```

---

## 2026-05-16 — DCA tranche sizing must respect guardrail #5 mechanically

**Current rule** (`strategy.md` Variant C, Entry criteria, line 25):
> DCA every position over 3 trading days (split each entry into 3 tranches).

**Proposed change:**
> DCA every position over 3 trading days (split each entry into 3 tranches). **Each
> tranche must satisfy guardrail #5: the single largest order in any tranche may not
> exceed 30% of available cash at the time of execution.** For positions whose target
> nominal exceeds ~20% of starting equity (e.g. VOO at 50%), the executable tranche
> size is therefore `min(target_nominal_per_tranche, 0.30 × current_cash_at_open)`,
> and any residual rolls into an additional tranche on the next trading day.
> Pre-flight every tranche on `cash_at_open`, not just at strategy-design time.

**Evidence:**
- Lesson 2026-05-14 documented the mechanical violation: VOO tranche-3 sized at fixed
  $16,667 nominal would have been 43.9% of remaining $38k cash — blowing guardrail #5
  (cap 30%). T1 was 16.7% clean, T2 was 24.2% clean; only T3 broke because cash had
  drawn down faster than tranche size.
- The fix was applied ad-hoc in the moment (cap T3 at $11,400 = 30% × $38k, defer
  $5,267 residual), but the strategy spec doesn't formalize the rule — so the next
  large-nominal position (any new ETF designated as Core at 50%+) will hit the same
  trap unless the runner remembers the lesson.
- Operationally cleaner than the alternative (front-loaded DCA at e.g. 40/35/25)
  because it requires no per-position custom sizing logic — one formula, applied at
  pre-flight, robust to any starting cash position.

**Risk if wrong:**
- Auto-rolling residuals can stretch a "3-day DCA" into a 4-5-day execution under
  adverse cash conditions, slightly slowing initial position build. This is materially
  smaller than the risk of silently breaking a hard guardrail; the guardrail wins.
