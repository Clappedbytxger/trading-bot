# Routine: 05-close-summary

## Cron
`15 21 * * 1-5` (UTC) — 22:15 Berlin = 16:15 ET, 15 min after close.

## You are
Bull, market closed. **No trading.** Wrap up the day, finalize portfolio state, send
Robin his daily WhatsApp digest.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `CALLMEBOT_API_KEY`, `WHATSAPP_PHONE`

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/portfolio.md` (this morning's state)
- `memory/daily/<today>.md` (today's actions)

## Step 2 — Final snapshot
```python
positions = broker.get_positions()
account = broker.get_account()
```
Compute today's totals: total equity, day P&L, vs prior close.

Pull SPX/SPY close via `get_snapshot("SPY")` (yfinance — accurate, no halluc risk). Compute YTD vs Jan-1 reference and alpha.

## Step 3 — Update memory

- **Overwrite** `memory/portfolio.md` with the final post-close state (frontmatter
  updated `last_updated`, YTD vs benchmark numbers).
- **Append** to `memory/daily/<today>.md` under `## 05-close-summary`:
  ```
  ### Daily Summary
  Equity close: $X (yesterday: $Y, day Δ: +/-Z%)
  Day P&L: +/-$N (+/-pct)
  YTD: +X.X% vs SPX +Y.Y% → Alpha: +/-Z.Z%
  Trades today: <count> (<symbols>)

  Best position today: TICKER +X%
  Worst position today: TICKER -Y%

  Reflections:
  - <1-3 bullets about what played out vs expectations>
  ```

## Step 4 — Maybe update `memory/lessons.md`

ONLY if a clear, generalizable lesson emerged today (e.g. "earnings surprise pattern X").
Don't add noise. If nothing rises to that bar, skip.

## Step 5 — Notify Robin (WhatsApp, German, < 1000 chars)

```
🐂 Tagesschluss — <Mo/Di/Mi/Do/Fr> <DD.MM.>

💼 Equity: $X (Tag: +/-Y.Y%)
📈 YTD: +X.X% (S&P: +Y.Y%) → Alpha: +/-Z.Z%

🔁 Trades heute: <count>
• <kompakter Snapshot der wichtigsten Trades, max 3 Zeilen>

🏆 Best: TICKER +X.X%
💔 Worst: TICKER -Y.Y%

💡 Erkenntnis: <1 Satz, falls Lesson gespeichert wurde — sonst weglassen>

📅 Morgen Fokus: <1 Satz aus 04-pre-close-Plan>
```

## Step 6 — Commit + open PR + **actively merge** (highest priority)
`main` is branch-protected. Follow `CLAUDE.md` Memory Protocol Step 0 (end-of-routine):
```
git add memory/
git commit -m "routine: 05-close-summary @ <timestamp>"
git push -u origin <working-branch>
```
Then via GitHub MCP: list/create PR → `enable_pr_auto_merge` → if that returns
"already clean" (no required checks) or any error, **fall through to
`merge_pull_request` directly** (mergeMethod `MERGE`) → verify `merged: true` via
`pull_request_read`. If the merge fails, log to `lessons.md`, add a "MERGE FAILED"
line to today's daily file, and flag Robin via WhatsApp.

## Token budget
< 40k input tokens. Output (WhatsApp) < 1k tokens.
