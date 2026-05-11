---
name: place-trade
description: Place a trade with mandatory pre-flight guardrail checks. Always use this skill instead of calling the broker directly.
---

# Skill: place-trade

Standardized trade-execution procedure. Pre-flight guardrails, place, immediately set
trailing stop on new longs, record everything.

## Pre-flight checklist (ALL must pass)

```python
from decimal import Decimal
from src.brokers import get_broker

broker = get_broker()
account = broker.get_account()
positions = broker.get_positions()
clock = broker.get_clock()

# 1. Market must be open
assert clock.is_open, "Market closed — abort"

# 2. Position-count cap (only when opening a new position)
new_symbols = {p.symbol for p in positions}
if is_opening_new and ticker not in new_symbols:
    assert len(new_symbols) < 10, "10-position cap reached"

# 3. Order-size cap: <= 30% of cash
order_notional = Decimal(notional_usd)
assert order_notional <= account.cash * Decimal("0.30"), "Order exceeds 30% of cash"

# 4. Post-trade allocation: <= 35% of equity per position
projected_value = (existing_pos.market_value if existing_pos else Decimal(0)) + order_notional
assert projected_value <= account.equity * Decimal("0.35"), "Allocation exceeds 35% cap"

# 5. Leverage <= 2x (only relevant on margin accounts)
assert account.buying_power <= account.equity * Decimal("2"), "Leverage exceeds 2x"

# 6. Earnings window check — use yfinance, not search
from src.research.fundamentals import is_in_earnings_window
if is_opening_new and is_in_earnings_window(ticker):
    raise GuardrailViolation(f"{ticker} has earnings within 3 trading days — abort entry")
```

## Place order

```python
from src.brokers.base import Order

order = Order(
    symbol=ticker,
    side="buy",
    notional=order_notional,
    order_type="market",
    time_in_force="day",
    client_order_id=f"bull-{ticker}-{int(time.time())}",
)
result = broker.place_order(order)
```

## Immediately attach trailing stop (new long positions only)

After fill confirms (or assume filled for market orders), place trailing stop:
```python
stop = Order(
    symbol=ticker,
    side="sell",
    qty=filled_qty,
    order_type="trailing_stop",
    trail_percent=Decimal("10"),
    time_in_force="gtc",
)
broker.place_order(stop)
```

## Record everything

Append to `memory/trade_log.md`:
```markdown
## <ISO datetime> — <BUY/SELL> <TICKER>
- **Quantity:** <qty> (notional ~$<notional>)
- **Type:** market / limit @ $X
- **Fill:** $<avg_price> @ <fill_time>
- **Broker order ID:** <id>
- **Rationale:** <1-2 sentences linking to strategy.md or research>
- **Stop:** trailing 10% @ GTC (order id: <id>) — only for new longs
- **Allocation post-trade:** <pct>%
- **Cash remaining:** $<cash>
```

## On failure (guardrail or broker error)

DO NOT silently skip. Append to `memory/lessons.md`:
```markdown
## <date> — Aborted trade <TICKER>
- Attempted: <BUY/SELL> <qty> @ <type>
- Failure: <guardrail violated OR broker error message>
- Lesson: <what to do differently — e.g. "check earnings calendar earlier in pre-market routine">
```
