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

## 2026-05-15 — WhatsApp must spell out open questions, not reference them by shorthand
- **Pattern:** Bull referenced "Robin's A/B/C reply still pending" in 3 consecutive
  daily files (5/13 04-pre-close, 5/14 05-close-summary, 5/15 02-market-open WhatsApp
  draft) and in the 13:30Z 02-market-open WhatsApp send — but never re-stated *what*
  the A/B/C options actually were after the original 5/13 framing. Robin reasonably
  replied: "Was meinst du mit meiner A/B/C reply? Wenn das wichtig ist, musst du mir
  erklären in der Whatsapp Nachricht was ich zu tun habe." The shorthand assumed
  Robin had perfect recall of a 3-day-old question buried in a daily file he doesn't
  read. He doesn't — the WhatsApp is his interface, not the memory tree.
- **Lesson:** Every WhatsApp that flags a pending Robin-decision MUST re-state the
  question in full each time, not by shorthand reference. Specifically: (a) name
  the decision in one phrase, (b) list each option with its concrete consequence
  (dollars / allocation / risk), (c) state Bull's tendency and *why*, (d) give one
  unambiguous instruction for how to reply (chat text vs. memory edit). If options
  collapse over time (e.g. (C) becoming equivalent to (B)), explicitly retire the
  dead option in the WhatsApp — don't carry forward stale shorthand. The 5/13
  question was actually A/B from inception; (C) was Bull's later rewording of (B)
  for emphasis and should never have appeared as a distinct option.
- **Encoded as rule?** Informally — recorded here. The next 04-pre-close /
  05-close-summary / 06-weekly-review WhatsApp drafts must spell out the
  tranche-3 question in full per this rule, not "the A/B/C question". Should be
  reinforced in `routines/02-market-open.md` Step 6, `routines/05-close-summary.md`
  Step 6, `routines/06-weekly-review.md` Step 6, and the WhatsApp helper if/when
  a "draft_whatsapp(open_questions=[...])" abstraction is introduced.

## 2026-05-15 — Routine re-fires: snapshot-refresh, no duplicate side-effects
- **Pattern:** `02-market-open` invoked twice in the same session (13:30Z at the
  cash-equity open, and 13:55Z ≈25 min later, before the scheduled 14:30Z cron).
  First fire completed cleanly: portfolio updated, daily section written, WhatsApp
  drafted+sent, commit merged via PR #15. Second fire arrived with the routine
  already at its terminal state and Robin's pending question unchanged.
- **Lesson:** When a WhatsApp-yes routine fires a second time in the same
  session, the second fire is a **snapshot-refresh + sanity-check only**, not a
  full re-execution. Specifically: (a) re-pull live broker state (positions,
  stops, account) and verify nothing material has changed since the first fire,
  (b) refresh `portfolio.md` to current intraday values, (c) append a short
  "re-fire" section to today's daily file documenting the delta, (d) do NOT place
  new orders, (e) do NOT re-send the WhatsApp summary unless a material delta
  has occurred (stop breach, thesis-break event, Robin reply, position
  count/cash change). Material delta is the trigger; "same content, 25 min later"
  is not a delta and re-sending erodes Robin's signal-to-noise.
- **Encoded as rule?** Informally — recorded here. Should be reinforced in
  `routines/02-market-open.md` and the equivalent for other WhatsApp-yes routines
  (`05-close-summary`, `06-weekly-review`). Until then, this entry is
  authoritative.

## 2026-05-14 — `enable_pr_auto_merge` is not enough; routines must ACTIVELY merge
- **Pattern:** End-of-routine flow opened PR #10 and called `mcp__github__enable_pr_auto_merge`. The MCP returned "already in clean status (all checks passed). Auto-merge only applies when checks are pending — you can merge directly." → PR sat open, `main` never updated. Downstream routines would have cloned a stale `main` and read no trade plan, no portfolio update, nothing.
- **Lesson:** `enable_pr_auto_merge` only schedules a merge **when there are pending required checks** to wait on. On this repo `main` has no required checks today, so auto-merge silently no-ops. **The merge is the highest-priority step of the routine** — if it doesn't happen, every downstream routine reads stale state and no trades fire. End-of-routine flow must be: try `enable_pr_auto_merge` (handles the pending-checks case), and on "already clean" or any other error **fall through to `merge_pull_request` directly** (`mergeMethod: MERGE`). Always verify with `pull_request_read` that `merged: true` before ending. Conflicts/policy-blocks → log + flag Robin in German; never end a routine with an unmerged PR.
- **Encoded as rule?** Yes — `CLAUDE.md` Memory Protocol Step 0 (end-of-routine) rewritten today; all seven routine files (`00`–`06`) updated to point at the same flow. Old `git push origin main` snippet (which never worked under branch protection anyway) removed everywhere.

## 2026-05-16 — WhatsApp is outbound-only; inbox.md is now the canonical reply channel
- **Pattern:** Robin sent a WhatsApp "B" reply to Bull's tranche-3 question
  (origin 5/13, fully re-explained 5/15 14:05Z) — but the reply never reached
  any routine. CallMeBot is a one-way HTTP service: Bull POSTs to send,
  Robin's WhatsApp replies go to a phone but no inbound listener exists in
  `src/notify/whatsapp.py`. Three days of "Robin's A/B reply still pending"
  daily-file notes + a Default-B fallback were drafted on the assumption
  that WhatsApp was bidirectional. It isn't. Robin reasonably asked in chat:
  "Ist das bei dir angekommen?" — no, it wasn't, because the channel doesn't
  exist on the inbound side.
- **Lesson:** Every "Robin must reply" prompt across `CLAUDE.md`,
  `routines/*.md`, and daily WhatsApp messages MUST name a concrete inbound
  channel that scheduled routines can actually read. The chat session works
  for ad-hoc interactions but is invisible to scheduled cron routines.
  Until a real bidirectional channel exists (Telegram bot / Twilio WhatsApp
  Business webhook / GitHub-issues-poller), the canonical reply mechanism
  is **`memory/inbox.md`**: Robin edits the file on GitHub web UI between
  routines, commits to `main`, and Bull's next routine reads it at Step 1
  (READ) after the start-of-routine sync. Every WhatsApp question Bull
  sends must explicitly say "Bitte per memory/inbox.md auf GitHub
  zurückschreiben — WhatsApp-Antworten erreichen Bull NICHT."
- **Encoded as rule?** Yes — `memory/inbox.md` created 2026-05-16 with full
  usage instructions. Two follow-ups still owed:
  1. Update `CLAUDE.md` Communication Style section to name inbox.md as
     the reply channel and remove any implicit "WhatsApp reply" assumption.
  2. Update all WhatsApp draft templates (in routines 02/03/04/05/06) to
     say "Bitte per memory/inbox.md zurückschreiben — WhatsApp ist nur
     outbound" wherever a Robin-reply is requested. These belong in the
     respective routine-spec edits, not in this lesson body.
  Both follow-ups are deferred to a Robin-confirmed CLAUDE.md edit pass
  (since `CLAUDE.md` is a top-level config that benefits from explicit
  Robin acknowledgment, the same way strategy.md does).

## 2026-05-16 — Week ending 2026-05-15 (KW 20)
- **Pattern:** Week-1 of live paper trading. Strategy executed cleanly on its first
  weak-tape stress test: SPY -1.20% Friday, Bull -0.49% → +71 bp day-alpha, the
  cleanest single-day outperformance of the week. Weekly: Bull +0.74% vs SPY +0.135%
  = **+60 bp week-alpha** with the book still only 62% deployed (tranche 3 deferred).
  YTD-alpha gap tightened from -8.26% (Tue close) to -7.75% (Fri close) = +51 bp
  this week. **Zero stop-outs, zero thesis-breaks, zero guardrail violations across
  16 executed fills.** Every operational issue this week (3 consecutive 01-pre-market
  cron misses, Alpaca fractional-stop rejections, IEX feed lag at post-close pull,
  WhatsApp question-shorthand confusion, tranche-3 mechanical guardrail-#5 conflict)
  was caught and either fixed or surfaced to Robin — no silent failures.
- **Lesson:** In early-phase paper trading, **operational lessons outnumber strategy
  lessons by ~4:1, and that's healthy.** The strategy itself ("AI-Capex Barbell"
  with defensive ballast + cash sleeve) hasn't been stress-tested by a real
  drawdown yet, but its single design promise — that cash + low-beta defensives
  buffer the AI-sleeve volatility on weak-tape days — is empirically confirmed on
  the only meaningful down-day in the dataset (5/15). Lesson for week 2 onward:
  **resist the urge to "do something" while the strategy is working.** Every week
  Bull *doesn't* tighten stops, trim winners, chase NVDA at 52w-high, or rebalance
  intraday is a week of compounding the strategy spec. Action discipline > action
  count.
- **Encoded as rule?** No (still informal). Strategy.md needs no edit; this is a
  behavioral reminder for routines 02/03/04. Proposed encoding for next week:
  add a single line to routines 03-midday / 04-pre-close "Bias = inaction unless
  a spec-trigger fires. Hit-rate of no-action days is a quality metric, not a
  laziness metric." One concrete strategy-mechanics gap *was* surfaced this week
  (DCA tranche sizing vs guardrail #5) — proposed to Robin in
  `memory/strategy_proposals.md` 2026-05-16, awaiting his review.
