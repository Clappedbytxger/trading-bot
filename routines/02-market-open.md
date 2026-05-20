# Routine: 02-market-open

## Cron
`30 14 * * 1-5` (UTC) — 15:30 Berlin = 09:30 ET, market just opened.

## You are
Bull. Market just opened. Goal: execute the planned trade-set from this morning's
01-pre-market across all active sleeves, then send a German WhatsApp brief.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`,
`CALLMEBOT_API_KEY`, `WHATSAPP_PHONE`, `POLYGON_API_KEY` (Learning-Month).

## Phase Sentinel
Same as 01-pre-market. Log the active mode in today's daily file.

## Step 1 — Read
- `CLAUDE.md`
- `memory/strategy.md`
- `memory/playbook.md` (Learning Month)
- `memory/portfolio.md`
- `memory/inbox.md` — process any Robin reply that hit between routines
- `memory/daily/<today>.md` — pick up the 01-pre-market trade-idea draft
- `memory/lessons.md` (tail 30)
- `memory/experiments/_ledger.md` (Learning Month)
- `memory/trade_log.md` (last 20)

If today's daily file is missing OR has no 01-pre-market section, **abort entries**:
that means 01 failed to fire and you have no validated plan. Take account snapshot,
log the gap, and send a German WhatsApp flagging "kein pre-market plan verfügbar —
keine neuen entries heute."

## Step 2 — Verify market state
```python
broker = get_broker()
clock = broker.get_clock()
account = broker.get_account()
positions = broker.get_positions()
```
- If `clock.is_open == False` at 14:30Z + 5min grace, log and abort (early-close day or scheduling glitch).
- Refresh per-sleeve position counts and cash budgets vs `playbook.md` caps.

## Step 3 — Execute trade plan (per-sleeve)

For each planned action from 01-pre-market, before placing the order, re-verify
**guardrails active in current phase**:
- Live Phase: original #1-#10.
- Learning Month: ALM-1 through ALM-8 (sleeve discipline, sleeve cash budgets,
  sleeve stops, sleeve logging, hard-overrides).

Order sequence (lowest-risk first to leave buying power for higher-risk):

1. **Core sleeve** (unchanged in Learning Month) — execute any STOP-CHECK adjustments
   or thesis-break exits decided in 01.
2. **Crypto sleeve** — 24/7 market, place planned crypto entries first while equity
   spread is still tight at open.
3. **Swing sleeve** — place planned swing entries (long + short) at market or limit
   per playbook. Set ATR-or-pct stops as bracket orders.
4. **Options sleeve** — place planned options orders. Use multi-leg orders for
   spreads; single-leg for outright calls/puts. NEVER cross the spread on illiquid
   contracts (bid-ask > 10% of mid → use a limit order at mid).
5. **Daytrade sleeve** — set up ORB watches; do NOT place market orders until the
   ORB level breaks within the first 30min. ORB execution happens in 03-midday for
   any setup that triggers AFTER this routine ends.

For each fill, immediately:
- Place sleeve-specific stop order (bracket on Alpaca where supported, separate stop
  order otherwise).
- Append `memory/trade_log.md` entry with mandatory `sleeve:` and `strategy:` tags.
- Append per-strategy file `memory/experiments/<strategy-slug>.md` ENTRY block.

## Step 4 — Update portfolio.md
Rewrite `memory/portfolio.md` with per-sleeve tables:
```
## Core
| Symbol | Qty | Avg Entry | Mark | MV | UPL | Stop |
...
## Swing
...
## Daytrade (intraday only — flat by 20:30Z)
...
## Crypto
...
## Options
...
```

Plus the top frontmatter with totals: equity, cash by sleeve, leverage, options_BP,
daytrade_count, day_pnl by sleeve.

## Step 5 — Update experiments ledger
For each new fill, increment the strategy's trade-count in
`memory/experiments/_ledger.md`. Closed trades update win-rate, avg-R, RAR.

## Step 6 — Notify (WhatsApp — German, ≤1000 chars)

Structure (always in German):
```
🌅 Morgen-Brief Lern-Monat (Tag N/30)
Equity: $X (Δ vs gestern: ±$Y / ±%)
Sleeves: Core $A | Swing $B | DT $C | Crypto $D | Opt $E

Trades heute (Open):
✓ [Sleeve] BUY/SHORT TICKER @ $X — Stop $Y / Target $Z
...

Macro: <kurz>
Risiko-Flags: <wenn vorhanden>

Top Experiment heute: <slug> (<1-Zeiler>)
Plan für 03-midday: <kurz>
```

If a pending question for Robin exists, spell it out fully per lesson 2026-05-15
(name decision, options, consequences, instruction "Bitte per memory/inbox.md auf
GitHub zurückschreiben — WhatsApp ist nur outbound").

## Step 7 — Commit + PR + merge
Per CLAUDE.md Memory Protocol Step 0 end-of-routine.

## Notes & edge cases
- **Macro risk-off triggers (SPY -3% / VIX > 40)**: kill all entries except defensive
  Options (`options-protective-put`). Log the trigger.
- **Re-fire of this routine within same session**: snapshot-refresh only per lesson
  2026-05-15. Do NOT re-place orders, do NOT re-send WhatsApp unless material delta.
- **Hard-borrow short error from Alpaca**: log and skip that short candidate; the
  strategy remains active for other names.
- **Options multi-leg order rejection**: try single-leg fallback; if still fails,
  log and abandon for the day.

## Token budget
Aim < 50k input tokens. Daily file should already have 01-pre-market section with the
plan — DO NOT re-research, just execute.
