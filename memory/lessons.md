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
- **Lesson:** Every routine starts with `git fetch && git merge origin/main --no-edit` into the working branch, and ends by **opening or refreshing a PR with auto-merge enabled** (NOT direct push to main, since main is branch-protected and direct pushes return HTTP 403). Any merge conflict in memory files = abort + notify, never auto-resolve.
- **Encoded as rule?** Yes (added to `CLAUDE.md` Memory Protocol Step 0; mirrored in `routines/01-pre-market.md` Step 0 + Step 6). PR-based flow uses GitHub MCP (`create_pull_request` + `enable_pr_auto_merge`).

## 2026-05-12 — Strategy mandates 50% VOO but guardrail #1 caps single position at 35%
- **Pattern:** First real pre-market draft: `strategy.md` (Variant C) specifies 50% VOO core, while `CLAUDE.md` Hard Guardrail #1 caps any single position at 35%. Conflict detected before any orders placed.
- **Lesson:** When `strategy.md` conflicts with a Hard Guardrail in `CLAUDE.md`, the Hard Guardrail wins (non-negotiable). The routine must cap to the guardrail, park the residual cash, flag to Robin, and request explicit resolution (revise guardrail vs. revise strategy vs. split core across multiple ETFs). Never silently exceed a guardrail; never silently skip the strategy.
- **Encoded as rule?** Yes — Robin chose to extend Guardrail #1 with an ETF-Core exception (broad-market index ETFs designated as Core may go up to 60%; individual stocks still 35%). Encoded in `CLAUDE.md` 2026-05-12.

## 2026-05-12 — Alpaca rejects fractional trailing-stop orders
- **Pattern:** Tranche 1 BUYs used `notional` (dollar amount) → Alpaca fills produce fractional share quantities (e.g. 24.7329 VOO, 5.7096 MSFT). Sending the full fractional `qty` as a trailing-stop order with `time_in_force=gtc` returns HTTP `{"code":42210000,"message":"fractional orders must be DAY orders"}`. Trailing stops require GTC to actually trail across days, and fractional orders force DAY — the two are mutually incompatible at Alpaca.
- **Lesson:** Either (a) submit BUYs by integer `qty` rather than `notional` so fills are whole-share, or (b) on fill, place the trailing stop on `floor(filled_qty)` shares (integer fallback) and cover the remaining fractional sliver with a regular fixed-price `stop` order at `avg_entry × 0.90` (Alpaca allows fractional `stop` orders as DAY, but for true protection across nights this needs to be re-issued each day, or consolidated once tranches sum to ≥1 whole share). Today we took option (b) integer-only; ~1.5 sh / ~$300 notional left temporarily uncovered. Mitigation: address in 03-midday or after tranche 3 when fractional remainders consolidate to whole shares.
- **Encoded as rule?** Partially — recorded here; needs codification in routines (likely a helper in `src/brokers/` that abstracts "place trailing stop on a fractional position"). Open question: prefer integer-qty BUYs (cleaner stops, slight cash drift from target weight) vs. notional BUYs (exact weight, fractional stop gymnastics).

## 2026-05-14 — Fixed-nominal DCA breaks guardrail #5 on the final tranche of a heavyweight position
- **Pattern:** Strategy designates VOO as 50%-of-equity Core ETF, executed via DCA over 3 days at fixed $16,667 nominal per tranche. By tranche-3, cash had drawn down from $100k (T1) → $69k (T2) → **$38k (T3)**. A $16,667 single order = $16,667 / $38k = **43.9% of cash**, blowing guardrail #5 (cap 30%). T1 was 16.7%, T2 was 24.2% — both clean — so the violation didn't surface until the final-tranche pre-flight check.
- **Lesson:** When DCA-ing a position whose nominal exceeds ~20% of starting equity, the final tranche(s) will mechanically violate guardrail #5 because cash shrinks faster than tranche size. Two viable encodings: (a) **front-load** the DCA so tranches are sized in *decreasing* nominals (e.g. 40/35/25) keeping each ≤30% of remaining cash; or (b) **dynamically cap each tranche** at `min(target_nominal, 0.30 × current_cash)` and roll the residual into an automatic tranche-3.5/tranche-4 across additional days. Pre-flight every tranche on `cash_at_open`, not just at strategy-design time.
- **Encoded as rule?** Informally — applied today by capping VOO T3 at $11,400 ($38k × 30%) and deferring $5,267 residual. Should be formalized in `strategy.md` (DCA schedule explicitly), or in a routine helper that takes a target nominal and current cash and returns the executable size + residual to defer. Open question for Robin: pref (a) front-loaded DCA spec, or (b) auto-rolling residual?

## 2026-05-15 — 01-pre-market firing post-open is non-authoritative; do not retroactively trigger trades
- **Pattern:** 01-pre-market cron slot 13:00Z fired late at 13:48Z today (18 min AFTER market open, AFTER 02-market-open had already executed at 13:30Z without a pre-market draft). 3rd consecutive business day the 13:00Z slot has failed or fired late.
- **Lesson:** A late-firing 01-pre-market never retroactively authorizes trades — by the time it runs, 02-market-open has already made its no-trade decision per spec. The correct response is to: (a) log the anomaly prominently in the daily file, (b) still complete the routine for audit/continuity (account sanity, quant pulse, macro pulse), (c) record a retroactive trade-idea draft so the next routines have context, (d) NEVER place orders from a late-firing pre-market. Tranche-3-style execution remains tied to *pre-market existing at open*, not *pre-market existing at all*.
- **Encoded as rule?** Partially — `CLAUDE.md` already says "clock.is_open=True at pre-market time → log and continue cautiously". This entry hardens the rule: continue **cautiously** explicitly means **no orders, draft is audit-only**. Should be reinforced in `routines/01-pre-market.md` Step 2 next time that file is touched. Open question for Robin: 3 consecutive misses suggests a runner-side schedule issue; needs investigation outside of Bull's scope.

## 2026-05-14 — `enable_pr_auto_merge` is not enough; routines must ACTIVELY merge
- **Pattern:** End-of-routine flow opened PR #10 and called `mcp__github__enable_pr_auto_merge`. The MCP returned "already in clean status (all checks passed). Auto-merge only applies when checks are pending — you can merge directly." → PR sat open, `main` never updated. Downstream routines would have cloned a stale `main` and read no trade plan, no portfolio update, nothing.
- **Lesson:** `enable_pr_auto_merge` only schedules a merge **when there are pending required checks** to wait on. On this repo `main` has no required checks today, so auto-merge silently no-ops. **The merge is the highest-priority step of the routine** — if it doesn't happen, every downstream routine reads stale state and no trades fire. End-of-routine flow must be: try `enable_pr_auto_merge` (handles the pending-checks case), and on "already clean" or any other error **fall through to `merge_pull_request` directly** (`mergeMethod: MERGE`). Always verify with `pull_request_read` that `merged: true` before ending. Conflicts/policy-blocks → log + flag Robin in German; never end a routine with an unmerged PR.
- **Encoded as rule?** Yes — `CLAUDE.md` Memory Protocol Step 0 (end-of-routine) rewritten today; all seven routine files (`00`–`06`) updated to point at the same flow. Old `git push origin main` snippet (which never worked under branch protection anyway) removed everywhere.
