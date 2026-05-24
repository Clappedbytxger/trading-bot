# Routine: 05-close-summary

## Cron
`15 21 * * 1-5` (UTC) — 22:15 Berlin = 16:15 ET, 15 min after close.

## You are
Bull. Day is done. Goal: finalize per-sleeve P&L, update experiment ledger, write
lessons, send German WhatsApp evening brief.

## Required env vars
`ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `GEMINI_API_KEY`,
`CALLMEBOT_API_KEY`, `WHATSAPP_PHONE`.

## Phase Sentinel
Same. Learning Month adds per-sleeve attribution + ledger refresh.

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/playbook.md`
- `memory/portfolio.md`
- `memory/lessons.md` (tail 30)
- `memory/inbox.md`
- `memory/daily/<today>.md`
- `memory/experiments/_ledger.md`
- `memory/trade_log.md` (last 30 — covers today's trades fully)
- `memory/research_log.md` (today only)

## Step 2 — Final account snapshot
```python
broker = get_broker()
account = broker.get_account()
positions = broker.get_positions()
```
Verify `clock.is_open == False`. Pull final equity, cash, options_BP, daytrade_count.
Pull SPY close for benchmark.

## Step 3 — Compute per-sleeve P&L

For each sleeve, compute:
- Day P&L $ (realized + unrealized delta vs yesterday's close)
- Day P&L % (vs sleeve cost-basis)
- Cumulative P&L $ since Learning-Month start
- Cumulative alpha vs SPY since Learning-Month start
- Open positions count

SPY benchmark: `spy_today_close - spy_yesterday_close` for the day; cumulative from
2026-05-20.

## Step 4 — Update experiment ledger

For each strategy with ≥ 1 trade today:
- Increment trade-count for closes.
- Recompute win-rate, avg R, max DD, RAR.
- Update `last_update` date.

Recompute sleeve roll-ups (used cash, cumulative P&L).

If any strategy has crossed a milestone (10th trade, first +5R, first -5R aggregate
loss), flag it in `lessons.md`.

## Step 5 — Update memory
- `memory/portfolio.md` — final EOD snapshot per-sleeve.
- `memory/trade_log.md` — any remaining today's trades (should be empty after
  03+04 already logged them; this is a backstop).
- `memory/experiments/_ledger.md` — refreshed KPIs.
- Per-strategy `memory/experiments/<slug>.md` — close-of-day update if there's a
  delta vs intraday.
- `memory/daily/<today>.md` — final section:
  ```
  ## 05-close-summary (<timestamp>)
  Final equity: $X (day Δ: ±$Y / ±%)
  SPY close: $Z (day Δ: ±%)
  Day alpha: ±X bp
  
  Per-sleeve P&L (today):
    - Core: ±$X (±%)
    - Swing: ±$X (±%)
    - Daytrade: ±$X (±%)
    - Crypto: ±$X (±%)
    - Options: ±$X (±%)
  
  Cumulative since LM start (2026-05-21):
    - Total alpha vs SPY: ±X bp
    - Best sleeve: <name> +$Y
    - Worst sleeve: <name> ±$Z
  
  Top experiment today: <slug> (<one-liner>)
  Bottom experiment today: <slug> (<one-liner>)
  
  Lessons appended today: <count> (refs)
  ```
- `memory/lessons.md` — append ONLY if a genuinely new generalizable rule emerged.

## Step 6 — Notify (WhatsApp — German, ≤ 1000 chars)

Structure:
```
🌙 Abend-Brief Lern-Monat (Tag N/30)
Equity: $X (Tag ±$Y / ±%)
SPY: ±% | Day-Alpha: ±X bp

Sleeve-Bilanz heute:
✓ Core ±$X | Swing ±$X | DT ±$X | Crypto ±$X | Opt ±$X

Trades heute: N (W:K L:M)
Top: [strategy-slug] +$X
Flop: [strategy-slug] -$X

LM-Alpha kumuliert: ±X bp
Lessons heute: <ja/nein, kurz>
Morgen: <kurz, 1 Zeile>

[Offene Frage an Robin falls vorhanden — vollständig spelled out per lesson 2026-05-15]
```

Per CLAUDE.md WhatsApp rules: max 1000 chars, German, no fluff. If an open question
for Robin exists, spell it out (decision name + options + consequences + reply-channel
instruction).

## Step 7 — Commit + PR + merge
Per CLAUDE.md. **This is one of the highest-priority merges of the day** — tomorrow's
01-pre-market depends on this state being on main.

## Token budget
Aim < 45k input tokens.

## Step 8 — bull-personal piggyback (Robin's personal Trade Republic swing sleeve)

Shares Robin's Pro-Plan routine quota. Run AFTER Bull's WhatsApp has been sent and the
merge is verified — bull-personal must never delay Bull's own close-summary.

1. WebFetch `https://raw.githubusercontent.com/Clappedbytxger/bull-personal/main/routines/eod.md`
2. Follow those instructions verbatim. Token-budget for this sub-step: 5k.
3. Record one summary line in today's `memory/daily/YYYY-MM-DD.md` under a `## bull-personal` heading.
4. If the piggyback fails, log a one-line reason in the daily file and exit. Bull's routine is already done — bull-personal failures must NOT trigger any retry or alert beyond the daily-file log.
