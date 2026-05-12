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

## 2026-05-12 — Missing pre-market plan blocks market-open execution
- **Pattern:** 02-market-open ran with no `memory/daily/<today>.md` from 01-pre-market.
- **Lesson:** Without an upstream draft plan, 02-market-open must only refresh state +
  stop-loss-check existing positions, never initiate new trades from scratch. The
  routine spec's "do NOT execute new trades" clause is the binding rule. Surface the
  scheduling gap to Robin in the WhatsApp summary so the cron / scheduler can be
  inspected.
- **Encoded as rule?** Already encoded in `routines/02-market-open.md` Step 1.

