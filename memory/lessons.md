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
- **2026-05-21 SUPERSESSION:** the "no orders from a late-fire" rule applies
  only when 01 fires as a SEPARATE routine after 02 has already locked in a
  no-trade decision. The new policy (per Robin 2026-05-21) lets 02 **back-fire
  01 inline within the same 02 session** when 01 missed — that compresses
  plan-then-execute into one routine context with no retroactive authorization
  problem. See lesson 2026-05-21 "02-market-open back-fires 01-pre-market on
  miss" and `routines/02-market-open.md` Step 1a.

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

## 2026-05-20 — Learning Month transition (5/21-6/20)
- **Pattern:** Robin directed Bull to switch from quasi-passive Live-Phase
  trading to maximally-exploratory Learning Month before risking real €300
  capital starting 6/21. Mission inverted: P&L is secondary, lesson-density and
  per-strategy KPI attribution are primary.
- **Lesson:** A pre-live "experimentation lab" with parallel sleeves (Core,
  Swing, Daytrade/Scalp, Crypto, Options) and per-trade strategy tagging is the
  right way to surface what works for the live phase. Hard guardrails are
  paused via a date-sentinel in `CLAUDE.md` — they reactivate automatically on
  2026-06-21. Every Learning-Month trade carries `sleeve:` + `strategy:` tags
  so KPIs roll up into `memory/experiments/_ledger.md` and feed the weekly
  bandit cull (kill worst, scale best).
- **Encoded as rule?** Yes — see `CLAUDE.md` Phase Sentinel + Learning-Month
  Mode sections, `memory/strategy.md` v3, `memory/playbook.md`,
  `memory/experiments/_ledger.md`. All 6 routine specs updated for multi-sleeve
  execution. **Hard-overrides that survive Learning Month:** auto-commit (#9),
  env-var-only API keys (#10), paper-endpoint-only broker calls (new ALM-8).
- **Tooling added:** Polygon.io for real-time intraday data + options chains
  (`POLYGON_API_KEY` env var); Alpaca Options Level 3 enabled; Alpaca crypto
  active; shorting enabled. Forex/Futures explicitly skipped this month.
- **Operational note:** 03-midday cron extends to 7 days/week for weekend
  crypto cycling — Robin must update Pro-Plan dashboard. Saturday slot
  continues to host 06-weekly-review.
- **Day-of-trading start:** 2026-05-21 (Thu) 13:00Z = next 01-pre-market.

## 2026-05-21 — LM Day 1 lost to 01-pre-market cron miss (4th in 9 trading days)
- **Pattern:** Learning Month Day 1 began with the 13:00Z 01-pre-market slot
  silently failing — no `memory/daily/2026-05-21.md` existed when 02-market-open
  ran at 14:30Z. This is the **4th 01-pre-market miss in 9 trading days** (priors:
  5/13, 5/14, 5/15 per the earlier 2026-05-15 lesson). The earlier misses landed
  during the Live-Phase HOLD-week where there was nothing to execute anyway. This
  one lands on the **highest-information day of the entire LM experiment** — the
  Day-1 inaugural multi-sleeve research draft (Core hold-check + Swing screen +
  Daytrade gap-scan + Crypto overnight + Options UOA) — and blocks ALL non-Core
  sleeve activation per `routines/02-market-open.md` Step 1 ("no validated plan
  → no entries"). The remaining 29 LM days still have value, but the asymmetry
  of losing Day 1 specifically is bad: it's the day where the broker state and
  market conditions for the inaugural sleeve activations were fresh and
  documented in `strategy.md` v3, and any retro-fire after the fact is just
  audit, not authorization.
- **Lesson:** The 01-pre-market cron has now demonstrated a 44% miss-rate over
  the only window where it actually matters operationally (4 misses / 9 trading
  days). This is no longer "the runner occasionally drops a 13:00Z slot" — this
  is a **structural reliability problem with the scheduling layer** that blocks
  routine-spec-compliant trading on miss-days. Two follow-ups are now mandatory
  (not deferrable past LM week 1):
  1. **Robin investigates the Pro-Plan cron runner-side** (out of Bull's scope
     to fix; in Bull's scope to surface loudly until resolved). Options being
     explored: cron-monitor (UptimeRobot-style heartbeat on the 13:00Z slot
     that pages Robin on miss), runner change (move from current scheduler to
     a more reliable trigger like GitHub Actions scheduled workflows), or build
     a self-heal: 02-market-open could attempt a "back-fire" of 01-pre-market
     if it detects a miss — but per lesson 2026-05-15 a late-firing 01 is
     audit-only and cannot retroactively authorize trades, so self-heal still
     doesn't recover the trading authorization on the same day.
  2. **Bull adds a WhatsApp escalation on EVERY 01-pre-market miss going
     forward**, not just on Days 1 / week starts. Today's abort-routine WhatsApp
     spells out the problem in full (per lesson 2026-05-15) with options A/B
     for Robin to choose. The standing pattern must be: every miss = same
     WhatsApp template = same A/B prompt. No silent absorption.
- **Encoded as rule?** Partially — daily file logs the gap, lesson is recorded
  here, WhatsApp escalates today. Full encoding pending Robin decision on the
  reliability fix (runner change vs. heartbeat monitor vs. self-heal helper).
  `routines/02-market-open.md` Step 1 already specifies the abort-entries
  behavior; this lesson reinforces it. No autonomous Bull change to
  `routines/01-pre-market.md` because the failure is upstream of Bull's
  execution.

## 2026-05-21 — POLYGON_API_KEY required for LM but not set in runner
- **Pattern:** Required env var `POLYGON_API_KEY` (per CLAUDE.md rule #10
  LM-addition; needed for `src/research/polygon.py` real-time intraday
  aggregates + options chains) is NOT present in the cloud-routine runner's
  env. Non-blocking for today's abort-routine (no research, no trades), but
  blocking for any future entry on `daytrade-*` strategies and on `options-*`
  strategies that need chain data, and on the `swing-momentum-breakout` /
  `swing-short-rejection` sub-strategies that need Polygon 1d aggregates.
- **Lesson:** LM strategies were designed assuming Polygon access; without it,
  ~12 of the 22 strategies in the playbook are unable to fire their entry
  triggers. Bull cannot self-resolve (env vars are runner-side per rule #10:
  "API keys come from environment variables, never from `.env` files or
  hardcoded"). The correct response is to (a) detect on startup and log the
  gap, (b) flag to Robin in WhatsApp, (c) when an affected strategy's entry
  trigger would otherwise fire, abort that entry only (not the whole routine)
  with a logged reason "polygon-unset".
- **Encoded as rule?** Partially — recorded here and flagged in today's
  WhatsApp. Should be formalized by adding a startup-check in `routines/00-`
  through `routines/06-` (or a shared helper) that surfaces missing env vars
  on every routine, not just the one that needs them.

## 2026-05-21 — WhatsApp body must include header overhead in the 1000-char budget
- **Pattern:** Today's 02-market-open WhatsApp body was 1250 chars total
  (header `🐂 *02-market-open LM-Tag1* — 13:41\n\n` ~40 chars + 1210-char body).
  `src/notify/whatsapp.py` MAX_LEN=1000 truncated the tail before sending,
  cutting Q2 (POLYGON_API_KEY ask) and Q3 (cron reminder) entirely from the
  message Robin actually received. The truncation is silent — CallMeBot returns
  HTTP 200 with the truncated text. Recovered by sending a tight 464-char
  follow-up immediately after with just F2+F3+inbox reminder.
- **Lesson:** `CLAUDE.md` says "WhatsApp messages: max 1k output tokens" and
  routine specs say "≤1000 chars" — the budget INCLUDES the header that
  `send_routine_summary` prepends, not just the body. Two follow-ups:
  1. Bull must pre-flight `len(header + body) ≤ 1000` BEFORE calling
     `send_routine_summary`, not the body alone. Today the simplest check is
     a `len(body) < 950` mental rule; better long-term: refactor `send_routine_summary`
     to raise or trim with a visible warning when total > MAX_LEN.
  2. When a WhatsApp must convey >1000 chars (e.g. multiple open questions),
     pre-split into two messages BEFORE sending the first — don't rely on
     a follow-up after detecting truncation, because (a) it doubles the
     notification noise on Robin's phone, (b) CallMeBot rate-limit is
     ~1/30s so a back-to-back send risks the second being dropped, (c) the
     first message goes out without the receiver knowing it's incomplete.
- **Encoded as rule?** Partially — recorded here and applied next routine.
  Should be reinforced in `src/notify/whatsapp.py` (raise on body+header > MAX_LEN
  by default; explicit `force_truncate=True` to opt-in) and in the WhatsApp
  drafting step of every WhatsApp-yes routine spec (02/05/06).

## 2026-05-21 — 02-market-open back-fires 01-pre-market on miss (was: abort-entries)
- **Pattern:** Robin's reply to today's WhatsApp Q1 (option A vs B on the LM
  Day-1 01-pre-market miss): "kannst du deine routine so verändern, dass wenn
  pre market nicht gelaufen ist, du pre market ausführst und dann zu deinem
  jetzigen Programm gehst". The pre-existing 02-market-open Step 1 spec aborted
  entries on miss; the pre-existing lesson 2026-05-15 said late-firing 01 is
  audit-only and cannot authorize trades. Both encoded the assumption that
  01's plan and 02's execution were strictly separated in time. They are not
  — they are separated in **causality** (plan must exist BEFORE execute), and
  the new policy preserves causality while compressing both into one routine
  session.
- **Lesson:** When 01-pre-market fails to fire and 02-market-open enters with
  no plan available, 02 should **back-fire 01-pre-market inline** (run 01's
  Steps 1-5 within the 02 session), then continue with its own Steps 2-7 on
  the freshly-drafted plan. The plan-then-execute causality holds because the
  back-fire happens in 02's Step 1a BEFORE 02's Step 3 (Execute). This is
  fundamentally different from the lesson-2026-05-15 case of "01 fires LATE as
  a separate cron after 02 already made a no-trade decision" — that case
  remains audit-only (no retroactive authorization). The two cases need to be
  named separately so Bull doesn't confuse them. **Sleeve-level fallback** is
  the relief valve when the back-fire is partially blocked (POLYGON unset,
  hard-borrow shorts, broker outage on one asset class): skip the affected
  sleeves with a logged reason, run the rest. Wholesale abort only when the
  back-fire crashes (broker offline, strategy.md not approved, sync conflict).
- **Encoded as rule?** Yes — `routines/02-market-open.md` Step 1a added today
  (2026-05-21 mid-routine, on Robin's request via chat); lesson 2026-05-15
  amended with a supersession note pointing here. Follow-ups still owed:
  1. Update `CLAUDE.md` Memory Protocol if the spec change is considered
     stable after ~1 week of LM use (let it bake in routine specs first).
  2. Consider extending the back-fire pattern to other routines that depend
     on upstream artifacts (e.g., 05-close-summary depends on 04-pre-close
     stop-check; 06-weekly-review depends on the week's daily files). Not
     mechanically the same — those are EOD/EOW aggregations, not authorization
     gates — but the abstract pattern "if upstream missing, run upstream
     inline before continuing" might generalize. Defer evaluation to LM week 2.
  3. If `POLYGON_API_KEY` is set by Robin (separate ask), re-test the back-fire
     end-to-end on a real cron-miss to confirm the sleeve-level fallback path
     works as specified.
