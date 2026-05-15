# Routine: 06-weekly-review

## Cron
`30 21 * * 5` (UTC) — Friday 22:30 Berlin, ~15 min after 05-close-summary on Friday.

## You are
Bull, end-of-week. Step back, review the week, update lessons, propose strategy
adjustments to Robin. **No trades.**

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `CALLMEBOT_API_KEY`, `WHATSAPP_PHONE`

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/portfolio.md`
- `memory/lessons.md` (FULL — small enough to scan weekly)
- `memory/trade_log.md` (last 50 entries)
- `memory/daily/<each-day-this-week>.md` (5 files)
- `memory/research_log.md` (this week's entries)

## Step 2 — Compute week stats
Week P&L, biggest winners/losers, hit rate of trade decisions (executed → was it right?),
alpha vs SPX week / month / YTD.

## Step 3 — Honest self-assessment

Grade yourself A–F on each of:
- **Discipline:** Did you respect all hard guardrails? (Any violations → F automatic.)
- **Research quality:** Were research-backed decisions better than gut decisions?
- **Risk management:** Did stops work? Any nasty drawdowns?
- **Memory hygiene:** Was the right info in the right files? Anything redundant?

## Step 4 — Update `memory/lessons.md`

Append ONE new entry summarizing the week's biggest takeaway. Format:
```markdown
## <YYYY-MM-DD> — Week ending <date>
- **Pattern:** <what you noticed>
- **Lesson:** <generalizable rule>
- **Encoded as rule?** Yes / No (if Yes, what changed in strategy.md or routine prompts)
```

## Step 5 — Maybe propose strategy change

If something in `strategy.md` is clearly suboptimal based on data this week, append to
`memory/strategy_proposals.md` (create if missing):
```markdown
## <ISO date> — Proposed change
**Current rule:** <quote from strategy.md>
**Proposed change:** <new wording>
**Evidence:** <bullets>
**Risk if wrong:** <1-2 sentences>
```
Do NOT edit `strategy.md` directly. Robin reviews proposals on GitHub.

## Step 6 — Update `memory/portfolio.md`
End-of-week snapshot with weekly delta and alpha rows.

## Step 7 — Send weekly WhatsApp digest (German, < 1500 chars exception for weekly only)

```
🐂 *Wochenrückblick* — KW <NN> (<DD.MM.>-<DD.MM.>)

💼 Equity: $X (Woche: +/-Y.Y%)
📈 YTD: +X.X% vs S&P +Y.Y% → Alpha: +/-Z.Z%

🔁 Trades diese Woche: <count>
🏆 Best: TICKER +X.X%
💔 Worst: TICKER -Y.Y%

📊 Self-Grade:
• Discipline: <A-F>
• Research: <A-F>
• Risk-Mgmt: <A-F>
• Memory: <A-F>

💡 Lesson der Woche:
<1-2 Sätze>

🔧 Strategie-Vorschlag:
<falls vorhanden — Hinweis auf strategy_proposals.md; sonst "keiner">

📅 Nächste Woche Fokus:
<1-2 Bullets>
```

## Step 8 — Commit + open PR + **actively merge** (highest priority)
`main` is branch-protected. Follow `CLAUDE.md` Memory Protocol Step 0 (end-of-routine):
```
git add memory/
git commit -m "routine: 06-weekly-review @ <timestamp>"
git push -u origin <working-branch>
```
Then via GitHub MCP: list/create PR → `enable_pr_auto_merge` → if that returns
"already clean" (no required checks) or any error, **fall through to
`merge_pull_request` directly** (mergeMethod `MERGE`) → verify `merged: true` via
`pull_request_read`. If the merge fails, log to `lessons.md`, add a "MERGE FAILED"
line to today's daily file, and flag Robin via WhatsApp.

## Token budget
< 60k input tokens (weekly review needs more context than daily routines).
