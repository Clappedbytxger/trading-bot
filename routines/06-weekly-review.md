# Routine: 06-weekly-review

## Cron
`30 21 * * 5` (UTC) — Friday 22:30 Berlin, ~15 min after 05-close-summary on Friday.

(Robin's Pro-Plan dashboard may have this scheduled for Saturday — either is fine.
It uses the "Saturday slot" his Pro Plan exposes for the week.)

## You are
Bull. Week's done. Goal:
- Live Phase: weekly P&L recap, strategy health-check, lessons.md update.
- Learning Month: also run the **strategy-bandit cull** (kill worst, double best),
  refresh playbook + ledger.
- On 2026-06-20 (the final Learning-Month routine): produce the **Final Report**.

## Required env vars
`ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `GEMINI_API_KEY`,
`CALLMEBOT_API_KEY`, `WHATSAPP_PHONE`.

## Phase Sentinel
Same. The Learning-Month additions only run on 2026-05-21 → 2026-06-20.

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/playbook.md`
- `memory/portfolio.md`
- `memory/lessons.md` — full file (this is the routine that maintains it)
- `memory/inbox.md`
- `memory/experiments/_ledger.md`
- `memory/trade_log.md` — last 100 entries (full week)
- `memory/daily/<this-week-files>.md` — 5 daily files (Mon-Fri)
- `memory/research_log.md` — past 7 days

## Step 2 — Compute weekly KPIs

For the trailing 5 trading days (Mon-Fri):
- Total return % (Bull) vs SPY return %
- Weekly alpha bp
- Per-sleeve breakdown:
  - Core: passive performance (benchmark)
  - Swing: trades count, win-rate, total $, avg R
  - Daytrade: trades count, win-rate, total $, avg R, PDT-count used
  - Crypto: trades count, win-rate, total $, total weekend exposure days
  - Options: trades count, win-rate, total $, theta-decay total
- Per-strategy KPIs from ledger: RAR ranking

## Step 3 — Strategy-bandit cull (Learning Month only)

Pre-conditions:
- Need ≥ 1 full week of data (skip on Fri 2026-05-22 — only 2 days of trading; first
  cull is Fri 2026-05-29).

Logic:
1. Rank strategies with ≥ 3 trades in the trailing 7d by RAR (Risk-Adjusted Return).
2. **Kill worst-1**: set its `status` in `playbook.md` to `paused` and halve its
   notional budget. If a strategy was already paused, mark `killed` and remove from
   ledger active section.
3. **Scale best-1**: increase its budget +50% (cap at 2x original). Funds come from
   the killed strategy + cash reserve.
4. For strategies with 0 trades in 7d: review whether trigger is reachable. If not,
   relax it slightly; if it's just market not offering setups, keep dormant.
5. Document each kill/scale decision in `lessons.md` with rationale.

Write the bandit decisions to `memory/experiments/_ledger.md` "Weekly bandit log" section.

## Step 4 — Lessons.md update

Append per-week lesson summary. Use the format from CLAUDE.md:
```
## YYYY-MM-DD — Week ending YYYY-MM-DD (KW NN)
- **Pattern:** ...
- **Lesson:** ...
- **Encoded as rule?** Yes/No/Partial — pointer to where
```

Focus on:
- Operational lessons (broker quirks, data issues, scheduling)
- Strategy lessons (which sub-strategies worked / failed and why)
- Market-regime lessons (what tape conditions favored what)
- Lessons that should become Live-Phase rules (collect for 2026-06-21 transition)

## Step 5 — Update memory
- `memory/strategy.md` — Learning Month: refine sleeve-rules based on week data
  (Bull may edit autonomously per ALM rules).
- `memory/playbook.md` — apply bandit results (status changes + budget adjustments).
- `memory/experiments/_ledger.md` — refresh fully, append bandit log.
- `memory/daily/<today>.md` — append the 06-weekly-review section.

## Step 6 — Notify (WhatsApp — German, ≤ 1000 chars)

```
📊 Wochen-Brief KW NN (Lern-Monat Tag N/30)
Equity Fr-Schluss: $X (Woche ±$Y / ±%)
SPY Woche: ±% | Wochen-Alpha: ±X bp
LM-Alpha kumuliert: ±X bp

Trades Woche: N (Sleeve-Verteilung)
Bandit-Cull:
  ✗ KILL: <strategy-slug> (Grund kurz)
  ⬆ SCALE: <strategy-slug> (+50% Budget)

Top-Lesson Woche: <1 Zeile>

Nächste Woche Fokus: <kurz>
```

## Final Report — only on 2026-06-20

Additionally produce `memory/experiments/_final_report_2026-06-20.md` with:
- Cumulative Learning-Month P&L per sleeve + alpha vs SPY
- All strategies ranked by RAR
- Top 3 strategies recommended for Live Phase (with proposed sizing)
- Top 3 lessons proposed as new Live-Phase guardrails
- Open questions for Robin re: Live-Phase strategy.md revision
- Then send a longer WhatsApp (still ≤ 1000 chars — link to GitHub for full report):
  "📊 Lern-Monat ABGESCHLOSSEN. Full report: <PR-URL>. Top-Strategien: <top3-slugs>.
  Vorschlag für Live-Phase: <kurz>. Bitte review per inbox.md vor 6/21."

## Step 7 — Commit + PR + merge
Per CLAUDE.md.

## Token budget
Aim < 60k input tokens (higher than other routines — full-week aggregation needs more
context).

## Step 9 — bull-personal piggyback (Robin's personal Trade Republic swing sleeve)

Shares Robin's Pro-Plan routine quota. Run AFTER Bull's weekly WhatsApp + merge done.

1. WebFetch `https://raw.githubusercontent.com/Clappedbytxger/bull-personal/main/routines/weekly.md`
2. Follow those instructions verbatim. Token-budget for this sub-step: 5k.
3. Record one summary line in today's `memory/daily/YYYY-MM-DD.md` under a `## bull-personal` heading.
4. Failure handling: log one-line reason, do not retry, do not alert. Bull's weekly review must NOT be delayed by bull-personal issues.
