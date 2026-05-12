# Lessons

Append-only log of generalizable rules Bull has learned. Bull reads this BEFORE every
trading decision. Keep entries tight — pattern, lesson, encoded?

## Format

```
## <YYYY-MM-DD> — <short title>
- **Pattern:** <what was observed>
- **Lesson:** <generalizable rule>
- **Encoded as rule?** Yes (added to strategy.md) / No (still informal)
```

---

(no lessons yet — week 1 will populate this)

## 2026-05-12 — Routine aborted: strategy not approved
- **Pattern:** 01-pre-market routine triggered while `memory/strategy.md` still has `version: 0` and `approved: false`.
- **Lesson:** Trading-related routines must short-circuit at Step 1 when strategy is unapproved. No research, no broker calls, no orders — only log the abort. Robin must run `00-strategy-init` and manually approve `strategy.md` before any cron routine can do real work.
- **Encoded as rule?** Yes (already in `CLAUDE.md` Strategy Lifecycle and routine Step 1).

## 2026-05-12 — Git workflow: sync with main before AND after every routine
- **Pattern:** Cloud routines clone fresh; Robin may edit memory files (e.g. approve `strategy.md`) on `main` between routines. Without an explicit sync, the working branch falls behind and the routine acts on stale state (this morning: working branch still saw `approved: false` after Robin had already merged the approval to `main`).
- **Lesson:** Every routine starts with `git fetch && git merge origin/main --no-edit` into the working branch, and ends by merging the working branch back into `main` and pushing. Any merge conflict in memory files = abort + notify, never auto-resolve.
- **Encoded as rule?** Yes (added to `CLAUDE.md` Memory Protocol Step 0; mirrored in `routines/01-pre-market.md` Step 0 + Step 6).

## 2026-05-12 — Strategy mandates 50% VOO but guardrail #1 caps single position at 35%
- **Pattern:** First real pre-market draft: `strategy.md` (Variant C) specifies 50% VOO core, while `CLAUDE.md` Hard Guardrail #1 caps any single position at 35%. Conflict detected before any orders placed.
- **Lesson:** When `strategy.md` conflicts with a Hard Guardrail in `CLAUDE.md`, the Hard Guardrail wins (non-negotiable). The routine must cap to the guardrail, park the residual cash, flag to Robin, and request explicit resolution (revise guardrail vs. revise strategy vs. split core across multiple ETFs). Never silently exceed a guardrail; never silently skip the strategy.
- **Encoded as rule?** Yes — Robin chose to extend Guardrail #1 with an ETF-Core exception (broad-market index ETFs designated as Core may go up to 60%; individual stocks still 35%). Encoded in `CLAUDE.md` 2026-05-12.
