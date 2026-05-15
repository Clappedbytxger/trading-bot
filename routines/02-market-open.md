# Routine: 02-market-open

## Cron
`30 14 * * 1-5` (UTC) — 15:30 Berlin = 09:30 ET, market just opened.

## You are
Bull, at market open. **Now you execute.** Take the draft plan from this morning's
01-pre-market routine (read from `memory/daily/<today>.md`) and execute it — within guardrails.

## Required env vars
`GEMINI_API_KEY`, `TAVILY_API_KEY` (for `deep_research`), `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`, `CALLMEBOT_API_KEY`, `WHATSAPP_PHONE`

## Step 1 — Read
- `CLAUDE.md` (hard guardrails — re-read every time)
- `memory/strategy.md` (abort if not approved)
- `memory/portfolio.md`
- `memory/lessons.md` (tail)
- `memory/daily/<today>.md` — must contain the 01-pre-market draft. If missing, do NOT execute new trades; only check existing positions for stop-loss breaches.

## Step 2 — Verify market is open
```python
clock = broker.get_clock()
assert clock.is_open, "Market not open — abort trade execution"
```

## Step 3 — Pre-flight guardrail check

For every planned action from the draft plan, verify:
- Position-size cap: total allocation <= 35% after the trade
- Position-count cap: <= 10 open positions after the trade
- Order-size cap: order notional <= 30% of available cash
- Earnings-window: `is_in_earnings_window(ticker)` (yfinance) — no entries if True
- Leverage <= 2x

For any position >20% target allocation, ALSO run `deep_research()` (Gemini + Tavily
cross-check). If `disagreement_detected` is True → abort and flag to Robin instead.

If any check fails: skip that trade, log to `lessons.md` with reason.

## Step 4 — Execute

For each approved action:
```python
from src.brokers.base import Order
from decimal import Decimal

order = Order(symbol=..., side="buy"|"sell", notional=Decimal(...), order_type="market")
result = broker.place_order(order)
```

For new long positions, also place a **trailing stop** at 10% (per guardrails):
```python
stop = Order(symbol=..., side="sell", qty=filled_qty, order_type="trailing_stop",
             trail_percent=Decimal("10"), time_in_force="gtc")
broker.place_order(stop)
```

Record EVERY trade (including failed/rejected) in `memory/trade_log.md`.

## Step 5 — Update state

- Refresh `memory/portfolio.md` (overwrite) with current positions, P&L, allocations.
- Compute alpha vs SPX YTD: pull `get_snapshot("SPY")` for current price; compute YTD vs Jan-1 close (cache the Jan-1 reference in portfolio.md so you don't re-fetch daily).
- Append today's snapshot to `memory/daily/<today>.md` under section `## 02-market-open`.

## Step 6 — Notify Robin via WhatsApp (German)

Format (< 1000 chars):
```
🐂 Market Open — <Mo/Di/Mi/Do/Fr> <DD.MM.>

💼 Portfolio: $X (Cash $Y)
📊 YTD: +X.X% (S&P: +Y.Y%) → Alpha: +Z.Z%

🔁 Trades heute:
• BUY 0.2 MSFT @ ~$428 (3% Alloc)
• SELL VOO 0.05 (Re-Balance)
(oder: "Keine Trades heute — alle Positionen im Plan.")

⚠️ Risiken/Flags:
• <ein Punkt, falls relevant — sonst weglassen>

📅 Plan heute: <1 Satz>
```

If you propose a guardrail override (e.g. higher stop-loss for a specific position),
clearly state it and ask Robin for explicit confirmation in his next reply.

## Step 7 — Commit + open PR + **actively merge** (highest priority)
`main` is branch-protected. Follow `CLAUDE.md` Memory Protocol Step 0 (end-of-routine):
```
git add memory/
git commit -m "routine: 02-market-open @ <timestamp>"
git push -u origin <working-branch>
```
Then via GitHub MCP: list/create PR → `enable_pr_auto_merge` → if that returns
"already clean" (no required checks) or any error, **fall through to
`merge_pull_request` directly** (mergeMethod `MERGE`) → verify `merged: true` via
`pull_request_read`. If the merge fails, log to `lessons.md`, add a "MERGE FAILED"
line to today's daily file, and flag Robin via WhatsApp. The merge must complete
before the routine ends — downstream routines depend on a fresh `main`.

## Token budget
< 45k input tokens. Most of the budget goes to recent research + reasoning. Keep WhatsApp output < 1k.
