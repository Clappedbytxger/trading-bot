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
