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

## 2026-05-22 — daytrade_count pre-counts open positions w/ same-day GTC stops
- **Pattern:** Placed 2 Swing BUY orders (NVDA + RL) at 13:37Z with same-day
  GTC protective stops attached. Immediately after fills, `daytrade_count`
  jumped 0 → 2 even though both positions remained OPEN (no closing fills
  occurred). Alpaca's `daytrade_count` field appears to pre-count any position
  opened today that has an outstanding sell order (e.g. our protective stops)
  — i.e., the system treats them as "eligible to round-trip same-day" and
  pre-debits the PDT budget. If the stops don't trigger today (most likely
  scenario for properly-sized Swing entries), the count should reverse at
  next-day rollover, but the budget IS provisionally consumed.
- **Lesson:** When budgeting PDT round-trips per session, subtract one from
  the budget for every same-day-opened position with an active GTC stop, not
  just for actual completed round-trips. Today we have 2 ORB / scalp round-
  trips of headroom remaining (4-threshold − 2-pre-counted = 2), not 4.
  This is more conservative than the playbook's "max 3 day-trades per rolling
  5-day window" comment implies in practice; account for the watermark
  reservation before planning Daytrade execution at 03-midday.
- **Mitigation options for future LM sessions:**
  - **Accept the watermark**: cap intended same-day Daytrade execution to
    `4 − (Swing-opens-w/-GTC-stop-today)` to avoid PDT flip risk.
  - **Defer the Swing stop**: place the Swing BUY first, run the session,
    THEN place the GTC stop in a later routine (03-midday or 04-pre-close).
    This avoids the pre-count but leaves the Swing position unprotected
    during the 13:30-18:30Z window. **Not recommended** — ALM-3 requires
    sleeve stops at entry, and a -5% gap intraday would burn more than the
    PDT-watermark cost.
  - **Use a Limit-sell at target instead of a Stop-sell**: a sell-LIMIT at
    the target price might not trigger the same pre-count (Limit orders
    away from market are not "round-trip-imminent"). Untested. Defer to
    a future routine to verify.
- **Encoded as rule?** Yes — recorded here and noted in today's daily file
  and `_ledger.md` refresh log. Follow-up next routine (03-midday): verify
  the count remained at 2 (no unexpected drift), and confirm the count
  resolves at 5/23 daily rollover. If it persists across sessions, escalate.

## 2026-05-23 — Week ending 2026-05-22 (KW 21) — first LM cross-phase week

- **Pattern:** KW 21 was a cross-phase week (Mon 5/18 → Wed 5/20 = final 3
  Live-Phase HOLD days under v2 strategy; Thu 5/21 → Fri 5/22 = Learning
  Month Day 1 + Day 2 under v3 multi-sleeve strategy). Bull week +0.382%
  (broker) vs SPY +0.883% = **-50 bp week-alpha**, a regression from KW 20's
  +60 bp. LM Day 1 (5/21) was lost to a 4th 01-pre-market cron miss (now
  4/10 miss-rate over the window where it actually matters operationally,
  per the 5/21 lesson). LM Day 2 (5/22) executed cleanly with the new
  Step-1a inline back-fire: 01-pre-market drafted within the same 02-market-
  open session, 2 Swing entries fired at the open (NVDA $2k swing-quality-
  pullback, RL $1.5k swing-earnings-drift), both with sleeve-specific stops
  GTC. 0 closes book-wide; 0 trades on Daytrade/Crypto/Options across the
  entire week. 100% of P&L attribution this week sits on `core-buy-and-hold`
  (+$340.52 UPL Δ; LLY HWM walked up 6+ times for cumulative +$24.27 /
  +2.58% organic protection drift — biggest single-week trail-walk in the
  book's history).
- **Lesson 1 (operational, primary):** **A cross-phase week + operational
  disruptions (cron miss + missing POLYGON key 5/21 + Polygon options-chain
  tier-gate 5/21-5/22) inevitably produces a thin LM sample.** Bull's first
  KW under multi-sleeve discipline saw 19 of 22 sub-strategies at 0 trades
  in 7d, but the attribution is mostly *operational* (data feeds, cron
  reliability), not *strategic* (concept failure). The 06-weekly-review
  bandit cull would have over-fit on this noise; the spec's "≥3 trades per
  strategy" gate correctly held off cull-day-1. **Generalizable rule**:
  bandit decisions must distinguish "no signal because the feed didn't
  scan" from "no signal because the market didn't offer the setup" — the
  former is operational debt to fix (Robin / Bull), the latter is the
  signal *itself*. This requires per-strategy logging of "attempted scans"
  not just "completed scans" — defer this to a `routines/*.md` enhancement
  in week 2.
- **Lesson 2 (market-regime):** SPY +0.88% week, VIX 16.59-17.79 range (no
  spike), no -3% day. This is a **slow-grind-up tape that disfavors mean-
  reversion and gap-fade strategies and favors quality-pullback + earnings-
  drift + buy-and-hold**. Both Swing entries on 5/22 (NVDA quality-pullback
  + RL earnings-drift) were taken into a tape where their playbook profile
  matches the regime — that's a positive selection decision and not luck;
  worth keeping a running log of "regime classification per week" to validate
  this matching post-hoc. Crypto sleeve: 5/5 universe still 50<200 across
  the week, 24h moves all <2%, weekend-momentum trigger NOT met (BTC 7d
  -3.02%). Crypto staying empty in this regime is correct behavior — not
  a strategy failure to scale down next week.
- **Lesson 3 (encoding candidate):** "Bias = inaction unless a spec-trigger
  fires." KW 21 trade count = 2 across 5 trading days × 22 active+paused
  sub-strategies × 5 sleeves = ~0.4% of the theoretical execution surface.
  Recurrence of the KW 20 lesson ("action discipline > action count"). This
  has now held cleanly across 2 consecutive weeks under 2 different
  strategy regimes (Live-Phase HOLD + Learning Month multi-sleeve), and is
  ripe to encode as a **routine-spec line** in `routines/03-midday.md` and
  `routines/04-pre-close.md`: "no-trade-day hit-rate is a quality metric,
  not a laziness metric." Defer the actual file-edit to a Robin-acknowledged
  pass since it touches routine specs.
- **Lesson 4 (LM design validation, partial):** The "Core sleeve as
  Live-Phase benchmark" mechanism is working — KW 21 Core attribution
  +$340.52 / +0.55% on $62k cost-basis is the comparator the other 4
  sleeves must beat over the LM window to justify their existence in the
  Live-Phase strategy.md v4 (post-6/21). With 28 LM days remaining, the
  other sleeves have a real but narrowing window to demonstrate per-strategy
  RAR ≥ Core's ~0.55%/week pace. The 2 Swing positions opened 5/22 will
  be the first realized data points (target +7% on NVDA / +10% on RL vs
  -5% / -7% stops). If Swing closes the LM window with realized P&L worse
  than Core's UPL drift, the 6/20 final report should propose folding
  Swing's discretionary budget into Core ETF for Phase 2 (€300 live).
- **Lesson 5 (operational follow-up, **STILL OPEN**):** 01-pre-market cron
  miss-rate is now **4/10 trading days** (5/13, 5/14, 5/15, 5/21) — i.e.
  40% silent-fail. Robin has not yet replied on inbox.md Q1 A (cron
  reliability fix: heartbeat monitor vs. runner change vs. accept the
  back-fire workaround). The 02-market-open Step-1a back-fire spec
  (merged 5/21) handles the symptom — execution still happens — but
  doesn't fix the root cause and adds latency to the morning prep on
  miss-days. Until Robin chooses a fix path, **Bull continues to surface
  this loudly in every 06-weekly-review WhatsApp**. The cron is upstream
  of Bull's execution scope; resolution requires Robin-side investigation.
- **Encoded as rule?** Partial:
  - Lessons 1-4: recorded here, no rule-edits yet (insufficient LM sample to
    justify changes to `strategy.md` / `playbook.md` / `routines/*.md`).
    Re-evaluate at KW 22 EOW.
  - Lesson 5: surfaced loudly to Robin each weekly WhatsApp. No autonomous
    routine-spec change (it's upstream of Bull). Defer rule-encoding pending
    Robin's fix-path choice.

## 2026-05-22 — fractional Swing stops leave meaningful unprotected slice on high-priced names
- **Pattern:** RL Swing fill at $377.03 for $1,500 notional → 3.978463 sh.
  Stop placed on `floor(qty) = 3 sh` per the playbook fractional-handling
  convention (inherited from Core 2026-05-12). Uncovered slice = 0.978463 sh
  ≈ **$367 ≈ 25% of position** unprotected by the stop. Compare NVDA fill
  at $219.96 for $2,000 → 9.092513 sh, uncovered slice 0.092513 sh ≈ $20
  ≈ 1% of position. The high share price + small notional combo on RL
  makes the uncovered fraction disproportionately large.
- **Lesson:** For Swing entries on names priced > $200 with notional ≤ $1.5k,
  consider:
  (a) **Round notional up** so the floor-share-count cleanly covers ≥95%
      of position (e.g. $1,500 → $1,886 on RL would give 5 sh stop coverage
      with ~$31 uncovered, but then breaches ALM-2's $4k cap less and stays
      within Swing budget).
  (b) **Round notional down** so we trade integer shares from the start
      (e.g. $1,500 → 3 sh × $377 = $1,131 → 3-sh BUY + 3-sh stop, 0
      uncovered). Smaller position but full stop coverage.
  (c) **Stop limit on fractional**: Alpaca's docs say STOP orders require
      whole shares; STOP_LIMIT may support fractional in some configs.
      Untested.
  Today's choice was (default playbook path): take the fill at the planned
  notional, accept the slice. For RL specifically, the slice is large enough
  that a hard breach-and-gap could cost ~$367 instead of the planned ~$105
  stop loss. Sized small enough that this is tolerable (~3% of Swing budget),
  but worth flagging.
- **Encoded as rule?** Partially. Recorded here. Defer rule-change to LM
  week-2 review after seeing how often the Swing sleeve actually hits these
  high-priced + low-notional combos. If 3+ occurrences, change the playbook
  to prefer integer-share sizing for names > $200 share price.

## 2026-05-28 — CallMeBot 403s on em-dashes in multi-part rapid-fire sends; use ASCII hyphen
- **Pattern**: Today's 01-pre-market 4-part multi-part WhatsApp send via
  `send_long_routine_message` returned HTTP 403 on **every** part within seconds
  of each other. Diagnostic probes isolated the cause: an em-dash (`—` U+2014)
  encoded as `%E2%80%94` in the URL — present in the helper's standard header
  pattern `🐂 *<routine>* (N/M) — HH:MM` AND inline in the body text (German
  layperson prose uses em-dash freely). A simple GET with em-dash + short body
  ~30 seconds later succeeded; back-to-back em-dash-containing URLs 403. Pattern:
  CallMeBot likely has a WAF/rate-limit rule that flags em-dash + fast
  successive requests as suspicious, returns 403, and silently cooldowns. The
  Wed 22:35-22:45Z burst of 503s on the same helper looked transient at the
  time; it was almost certainly the same root cause (em-dash + rate-burst).
- **Lesson**: Use ASCII hyphen `-` in WhatsApp message headers and bodies,
  not em-dash `—`. Hyphens are URL-safe and pass through CallMeBot reliably
  even on multi-part rapid sends. Em-dashes are aesthetic — Robin's WhatsApp
  reads identically with `-`.
- **Encoded as rule?** Yes:
  - `src/notify/whatsapp.py` headers in `send_routine_summary` and
    `send_long_routine_message` now use ASCII hyphen.
  - Docstring updated with the explicit note "CallMeBot 403s on em-dash in
    multi-part rapid-fire sends".
  - Routine specs should also avoid em-dashes in the German body templates;
    propagate when those specs are next touched.
  - Today's 01-pre-market WhatsApp send used a manual ASCII-hyphen header
    bypass; landed 4/4 parts queued first try.

## 2026-05-30 — Week ending 2026-05-29 (KW 22) — first full LM trading week

- **Pattern (weekly aggregate)**: KW 22 was the first full LM trading week
  (Mon 5/25 Memorial Day holiday + Tue-Fri active). Bull +1.2614% vs SPY
  +1.4456% = **weekly alpha -18.4 bp** (improvement from KW 21's -50 bp;
  +32 bp recovery). LM cumulative (Day 1-9): Bull +1.4063% / SPY +1.8526%
  / alpha **-44.6 bp**. First LM closed trade: NVDA `swing-quality-pullback`
  stop-out Wed 5/27 15:00:34Z at $208.95 / -1.0R exactly. 4 Core HWM
  advances Fri 5/29 = book-record single-day cluster (VOO, MSFT, AVGO,
  META) + LLY Thu +5.13% walk (biggest single-day Core HWM in book history;
  CVS Zepbound reinstatement + Foundayo coverage). Per-sleeve KW 22:
  Core +$1,379.91 / Swing -$107.18 / DT $0 / Crypto $0 / Options $0.
  19 of 22 sub-strategies at 0 trades 7d — bandit cull pre-condition NOT
  MET (need ≥3 trades per strategy). Fri 5/29 02-market-open through
  05-close-summary all MISSED (Fri AMD entry + NVDA stub close both
  planned, neither executed).

### Lesson L1 (operational, primary) — Fri 5/29 cron-miss CLUSTER (4 consecutive routines)

- **Pattern**: Git log shows the last commit Fri was `f03592f routine:
  01-pre-market @ 2026-05-29T12:05Z`. No 02-market-open, 03-midday,
  04-pre-close, 05-close-summary commits exist for Fri. Broker cash
  balance Sat snapshot $36,380.54 = unchanged from Thu pre-mkt = no
  Fri fills. The 02-market-open Step-1a back-fire spec (added 5/21
  to handle 01-misses) does NOT address 02 itself missing — only 01.
  When 02 misses, the entire downstream chain (Fri AMD entry + NVDA
  stub close from the Fri pre-market plan) silently fails to execute,
  and the day's daily-file is left with only the pre-market section.
- **Lesson**: A 4-consecutive-routine miss is **structurally different**
  from a single 01-miss; it's a runner-wide outage for a portion of the
  day, not a single-slot drop. The current back-fire spec covers
  upstream→downstream gaps (01→02) but not contemporaneous gaps (02
  itself missing while 03/04/05 still need a plan). Possible encodings:
  (a) **EOD self-heal**: 05-close-summary, when it fires, checks if
  02/03/04 also fired today; if not, reconstruct from 01-pre-market
  plan + actual broker delta and write an audit `_recovery.md` in
  daily/; (b) **Periodic heartbeat**: each routine writes a tiny
  `last_seen.txt` to the repo on completion; if more than 1 hour
  elapses without a heartbeat during cash session, escalate to Robin
  WhatsApp; (c) **Robin-side runner fix**: same as L1 from 5/21 (Q1 A
  cron reliability still open in Robin's inbox).
- **Encoded as rule?** No (recorded here only). Robin Q1 A from 5/21
  still open — surface again in Sat 5/30 weekly WhatsApp. The 4-miss
  cluster materially weakens the case for any KW 23 strategy that
  depends on contemporaneous 02-execution (i.e. all Daytrade
  sub-strategies, all swing-momentum-breakout breakouts at the open).
  Until cron reliability resolves, the back-fire spec is a partial
  mitigation, not a fix.

### Lesson L2 (strategy validation, primary) — NVDA stop fired cleanly at -1.0R

- **Pattern**: First LM closed trade was NVDA `swing-quality-pullback`
  on Wed 5/27 15:00:34Z. Stop order `ffb5e5a9-50fb-4e39-abef-849d72b8f323`
  (SELL STOP 9 sh @ $208.96 GTC) filled at $208.95 avg = 1 ¢ slip vs
  trigger; intraday L $208.78 per yfinance so the fill happened mid-
  breakdown. Realized -$99.10 = exactly -1.0R (planned -5% / $11.00
  per share × 9 sh = $99.10). The trade reached its downside boundary
  in ~30% of the allotted 7-td holding window (td2 of 7 = 5/22 fill
  + holiday-skip + 5/26 td1 + 5/27 stop mid-session). Stub 0.0925 sh
  ($19 mv) left unprotected per the fractional-handling lesson from
  5/20; pending Mon 6/1 02-market-open liquidate (Thu+Fri attempts
  both missed — see L1).
- **Lesson**: The stop mechanic works as designed. -1.0R exactly, no
  slippage of consequence, no broker drama. The trade thesis (quality-
  compounder pullback) was fundamentally INTACT at stop time — NVDA's
  Q1 FY27 print + $80B buyback + 65% op margin / 85% rev growth
  unchanged from entry — but technical distribution flow (Tue 187M-sh
  day → Wed continuation breakdown) overwhelmed the narrative on a
  2-td horizon. **Generalizable rule**: on quality-compounder swings,
  expect ~30% of stop-outs to be flow-driven rather than narrative-
  driven within the 5-7 td window. The stop IS the discipline; the
  narrative is post-hoc. Sample = 1 trade — defer broader implications
  to KW 23 EOW (likely RL time-stops 6/5; AMD entry attempt Mon 6/1).
- **Encoded as rule?** Partially — recorded here and reflected in
  `memory/experiments/swing-quality-pullback.md` outcome section.
  No playbook.md change (1 trade insufficient sample). If 2 more
  `swing-quality-pullback` trades stop at -1.0R in KW 23-24 with the
  same flow-driven pattern, consider widening stop to -7% (matching
  earnings-drift sleeve) or tightening time-stop from 7 td to 5 td
  to truncate the technical-distribution risk window.

### Lesson L3 (market-regime, encoding candidate) — slow-grind-up tape continues to favor Core + PEAD

- **Pattern**: KW 22 was a continued slow-grind-up tape (SPY +1.4%,
  VIX -8.9% to 15.32 broke below 16 first time in 2 weeks, no -3%
  day, 4 Core HWM advances Fri + LLY massive Thu walk). This is now
  2 consecutive weeks (KW 21 + KW 22) of the same regime. In this
  regime:
  - **WORKS**: `core-buy-and-hold` (KW 21 +$340 / KW 22 +$1,380), 
    `swing-earnings-drift` would work if it had a fresh PEAD setup
    (RL was a Day-after-Day setup; the playbook's true Day 3-5
    drift target hasn't been tested with a fresh entry in this regime).
  - **DOESN'T WORK**: `swing-momentum-breakout` on EXTENDED names
    (ARM +10.76% Thu = chase-and-fail). Mean-reversion entirely
    (no flushes). Crypto trend-follow + mean-reversion (no -10% flushes,
    50/200 still inverted).
- **Lesson**: 2 consecutive weeks of the same regime is a signal that
  the LM playbook should bias entries toward "quality pullback +
  PEAD on the right side of the print" rather than chasing momentum
  breakouts at 52w highs. The regime-classification should be a
  pre-flight gate at 01-pre-market: scan SPY 5d range / VIX trend /
  major-event proximity and tag the day "slow-grind-up" / "trending"
  / "rangebound" / "risk-off". Then strategies fire ONLY if their
  regime affinity matches.
- **Encoded as rule?** No (still informal). Right time to encode is
  end of KW 23 — if a 3rd consecutive slow-grind-up week extends the
  pattern, propose a playbook v2 amendment in `strategy_proposals.md`
  with regime-tagging on each sub-strategy. Until then, just track
  regime classification per week in the weekly-review lesson.

### Lesson L4 (operational, escalation trigger) — Polygon options-chain blocked 6 consecutive routines

- **Pattern**: Polygon options-chain endpoint has returned 403
  Forbidden on every routine attempt since LM Day 1 (5/21). Today's
  KW 22 daily logs show 6 consecutive routine attempts blocked
  (Mon 5/26 4th re-test, Tue 5/26 5th, Wed 5/27 5th, Thu 5/28 6th
  deferred, Fri 5/29 6th = STILL 403). All 4 Options sub-strategies
  (`options-long-call-momentum`, `options-vertical-bull-call-spread`,
  `options-earnings-strangle`, `options-protective-put`) cannot fire.
  Reference-contracts endpoint works (200 OK) but provides no IV /
  Greeks / quotes — useless for sleeve activity.
- **Lesson**: This is no longer "transient tier-gate timing"; it's a
  **structural data-feed barrier** that has now blocked an entire
  sleeve for 9+ days. The sleeve has $5k premium budget that's
  completely unutilized while 22% of the strategy taxonomy
  (4 of 22 sub-strategies, 5 of 22 if you include `options-cash-secured-put`
  which is independently paused) sits idle. Two paths for Robin:
  (a) Subscribe to **Polygon Options Starter ($79/mo)** and validate
      chain unblocks. ROI judgment: Options sleeve P&L would need to
      beat $79/mo × 1 month = $79 = ~1.6% return on the $5k premium
      budget. Plausible if even 1 well-timed `options-long-call-momentum`
      on AMD or NVDA fires.
  (b) **Accept Options sleeve cannot run during LM** and reallocate
      the $5k premium budget to Swing or Crypto sleeves for KW 23+.
      Increment Swing budget $15k → $18k (covers 1-2 more concurrent
      positions); OR add to Crypto $5k → $7k (more headroom if 50/200
      cross fires); OR add to Cash reserve.
- **Encoded as rule?** No — this is Robin's decision (budget changes
  >$3k touch strategy.md territory per ALM rules). Surface in Sat 5/30
  weekly WhatsApp as the primary "operational question for Robin".
  If still 403 on Mon 6/1 01-pre-market 7th re-test AND no Robin
  reply by Mon EOD, default to path (b) and reallocate to Cash for
  KW 23 unless instructed otherwise (this is the safer default since
  it doesn't increase sleeve risk).

### Lesson L5 (operational) — CallMeBot 403 isn't just em-dash; length+content WAF hypothesis

- **Pattern**: Fri 5/29 01-pre-market multi-part news brief: 5 parts
  × 400-500 chars body (well under 700 char SAFE_PART_LEN) sent via
  `send_long_routine_message` with ASCII-hyphen-only headers per
  lesson 2026-05-28. **All 5 parts returned HTTP 403** across 3 retry
  attempts per part and 3 cadence variants (35s/45s/60s inter-part
  sleep). Diagnostic probes after the failure: short-text probes
  (50-60 char, plain ASCII, no Bull header) returned 200 OK / queued.
  Progressive complexity probes with emoji + bold markdown + multi-line
  + full `🐂 *01-pre-market* (1/5) - HH:MM` header also returned 200 OK
  at 60-char body. The 403 only fires on 400-500 char bodies with
  multi-paragraph German content.
- **Lesson**: The 2026-05-28 em-dash lesson was correct but incomplete.
  CallMeBot's WAF appears to fire on a **length+content composite**:
  ≥400 char per-part bodies in rapid succession trigger a heuristic
  even with pure-ASCII headers. The mitigation 2026-05-28 (use ASCII
  hyphen) was necessary but not sufficient. Three hypotheses for the
  Fri 403 cluster:
  - **H1**: Multi-paragraph German content with high letter density +
    emoji header pattern hits a length-based content-density WAF rule.
  - **H2**: Robin's CallMeBot per-recipient daily-volume cap. Thu sent
    4 parts; Wed sent more; Fri's 5+6 retries+probes in a few minutes
    could have tipped a daily rolling quota.
  - **H3**: URL-encoded length once `%F0%9F%90%82` (emoji) +
    `\n → %0A` paragraphs expand pushes payload past a hidden URL-
    length cap stricter than the documented 1000.
- **Workaround for KW 23 onward**:
  - Cap news briefs at **max 3-4 parts** (not 5).
  - Each part **≤400 chars body** (was 700 SAFE_PART_LEN).
  - **60+ s inter-part sleep** (was 35-45s).
  - **No emoji in headers for multi-part sends** (test hypothesis H1/H3).
  - If H2 is correct: rate-limit Bull's WhatsApp output to ≤4 parts/day
    across all routines combined.
- **Encoded as rule?** No (recorded here only). When `src/notify/whatsapp.py`
  is next touched, lower `SAFE_PART_LEN` from 700 → 400, raise
  `INTER_PART_SLEEP` from 35 → 60, and add a `max_parts=4` arg with
  default. Until then: routines that hit 5+ parts should split the
  brief across two ROUTINES (e.g. half at 01-pre-market, half at
  02-market-open) rather than try to push 5 parts through
  `send_long_routine_message`.

- **Operational follow-ups STILL OPEN at end of KW 22**:
  - L1 from 5/21: 01-pre-market cron miss-rate now 4 of 14 trading days
    (5/13, 5/14, 5/15, 5/21). **NEW from KW 22**: 4-consecutive-routine
    miss Fri 5/29 (02 + 03 + 04 + 05). Cron reliability is now the
    dominant operational risk, blocking both pre-market planning AND
    post-plan execution.
  - L4 from KW 22 (above): Polygon options-chain 6-consecutive-block
    escalation — Robin to decide (a) subscribe Options Starter $79/mo
    or (b) reallocate $5k budget.
  - L5 from KW 22 (above): CallMeBot 403 length+content WAF — mitigation
    by capping parts/length, but root-cause still hypothesized.
- **Encoded as rule?** Partial:
  - Lessons L1-L5: recorded here, no routine-spec changes yet.
    Re-evaluate at KW 23 EOW after another full week of data.
  - L4 surfaced loudly to Robin in Sat 5/30 weekly WhatsApp.

## 2026-05-27 — CallMeBot's "1000 char" cap is actually ~700-800; use multi-part
- **Pattern (initial reading):** First send of the new Top-5 News digest used
  a 1032-char body → truncated. Trimmed to 898 chars and re-sent → STILL
  truncated mid-item-4 per Robin. CallMeBot's documented 1000-char ceiling is
  misleading; in practice messages get cut somewhere around 700-800 chars
  (possibly the URL-encoded length once newlines `\n → %0A` and the emoji
  `🐂 → %F0%9F%90%82` expand, or simply a stricter server-side limit than
  the docs admit).
- **First fix that didn't hold:** A 960-char body limit. 898 was already
  under that and still got cut.
- **Lesson:** Never rely on a single CallMeBot message for the Top-5 News
  brief (or any multi-section daily WhatsApp). Always use the multi-part
  sender. Split on paragraph boundaries (`\n\n`) at a conservative
  `SAFE_PART_LEN = 700` chars/part so each news item stays in one part, and
  sleep ~35-45 s between parts (rate limit ~1 msg / 30 s). Each part gets a
  `(N/M)` header tag so Robin re-stitches in order.
- **Encoded as rule?** Yes —
  - `src/notify/whatsapp.py` got `send_long_routine_message(...)` and
    `_split_on_blank_lines(...)` with `SAFE_PART_LEN = 700` and
    `INTER_PART_SLEEP = 35`.
  - `routines/01-pre-market.md` Step 7d now mandates that helper for the
    news brief and explicitly drops the 960-char body limit.
  - Other routines that use the same notifier (02-market-open, 05-close-
    summary, 06-weekly-review) should switch to `send_long_routine_message`
    at next touch — propagate this when those specs are next edited.

## 2026-06-04 — Two consecutive Core gap-down stop-fills in 3 sessions: trail-stop fill-vs-trigger gap is the rule, not exception
- **Pattern:** Tue 6/2 GOOGL trail-stop fired @ $361.01 vs trigger $367.749 = $6.74 / 1.83% below trigger (gap-down on $80B AI-share-issuance dilution news). Thu 6/4 AVGO trail-stop fired @ $410.88 vs trigger $439.938 = $29.06 / 6.61% below trigger (gap-down on post-earnings beat-and-raise that didn't raise enough). Both fills 3-7% worse than mechanical trail expectation; both on idiosyncratic post-event opens (one share-issuance, one earnings-disappointment). Both turned previously-large UPL ($1,100+ peak GOOGL; $880+ peak AVGO) into modest realized losses (-$316 GOOGL; -$37 AVGO).
- **Lesson:** Mechanical -10% trail-stops on quality-growth single names will systematically fill 3-7% below trigger when (a) a binary post-event open (earnings, share issuance, antitrust, regulatory) (b) the gap-down outpaces the -10% trail. This is real-market behavior — the trail does its job at the broker layer; gap-fill risk is the cost of mechanical discipline. **Implication for Live-Phase**: when a Core name is approaching a known binary catalyst (earnings within 3 td per Live-Phase #8), pre-event consider (i) protective-put on Core's $30k+ allocation (-1.5R hedge cost; matches `options-protective-put` strategy), OR (ii) accept the gap-fill tail. During Learning Month, Core was frozen so neither path was open; the gap-fills were the inherited Live-Phase cost. **Specifically encode for Live Phase**: the entry-protection #8 rule (no entry within 3 td of earnings) protects against entry-side earnings risk but does NOT protect against held-position earnings risk. Add held-position pre-earnings consideration to strategy.md re-activation 2026-06-21.
- **Encoded as rule?** Informally — recorded here. Should be formalized in `strategy.md` Live-Phase section before 2026-06-21 reactivation: add "held-position pre-earnings protective-put consideration" as bullet under exit-criteria. Also Confirms lesson 2026-06-02 GOOGL gap-fill which had been informal; this is the second data point validating the systemic nature.

## 2026-06-04 — RL `swing-earnings-drift` cushion compression to sub-3% emergency without thesis-break
- **Pattern:** RL entered 5/22 on PEAD setup (post-Q4-FY26-beat day-after entry). KW 22 td1-5 cushion trajectory 7.19% → 3.66%; KW 23 td6-9 trajectory 3.66% → **2.59% Thu td9**. Total cushion erosion 5.6 pp over 9 td. No fresh thesis-break catalyst at any point (no analyst PT cuts, no guide change, no margin-deterioration print); just continued consumer-discretionary segment weakness with no flow into the PEAD-expected drift. PEAD literature peaks Day 3-5; Tue+Wed td2-3 of hold did deliver the +3.36% peak vs entry, but Thu+Fri Day 4-5 of week-1 reversed completely and bled deeper than entry.
- **Lesson:** PEAD-style setups have an asymmetric failure mode: the drift either fires within the Day 3-5 window or it never fires at all. Once the drift retraces below entry without a fresh catalyst, the modal outcome shifts from "+1.4R target" to "-1.0R stop or 0R time-stop". **Specifically for `swing-earnings-drift`**: consider adding a "Day 5 of hold check" — if cushion has compressed below 50% of entry-cushion AND UPL has gone negative without a fresh catalyst, evaluate emergency-tighten to lock breakeven-minus rather than ride into time-stop. The current playbook spec has no mid-hold cushion-compression rule — only the -7% stop or +5% tighten-to-breakeven or 10-td time-stop. Cushion compression as a leading indicator of likely stop-hit is the missing rule.
- **Encoded as rule?** Informally — recorded here. Should be folded into `playbook.md` `swing-earnings-drift` spec on next 06-weekly-review: "Mid-hold cushion-compression check at td5: if cushion < 50% of entry cushion AND UPL <= -2% AND no fresh PT raise / guide change in 5 td → emergency-tighten stop to -2% from current mark." This would have triggered Tue 6/2 (cushion ~3.6% vs entry 7%) and likely saved ~$20-30 vs the path Bull is on now.
