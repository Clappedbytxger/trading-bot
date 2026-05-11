---
name: research-stock
description: Research a single stock combining yfinance fundamentals (numbers, hallucination-free) and Gemini Search Grounding (news, qualitative). Use when you need a thesis check before trading a ticker.
---

# Skill: research-stock

Standard procedure for researching a single ticker. Two-source strategy:
- **Numbers from yfinance** — zero hallucination risk
- **News/qualitative from Gemini** — synthesized with Google Search Grounding

## When to use
- Before opening a new position
- When a position drops > 7% intraday (check for fundamental cause)
- During pre-market research on watchlist candidates
- During weekly review for "is thesis still valid"

## Procedure

### Step 1 — Pull the numbers (yfinance, free, accurate)

```python
from src.research.fundamentals import get_snapshot, get_earnings_date, is_in_earnings_window

snap = get_snapshot("MSFT")
earnings = get_earnings_date("MSFT")
in_window = is_in_earnings_window("MSFT")

# snap.price, snap.pe_ratio, snap.forward_pe, snap.operating_margin,
# snap.revenue_growth_yoy, snap.free_cashflow, snap.return_on_equity,
# snap.debt_to_equity, snap.beta, snap.fifty_two_week_low/high
```

### Step 2 — Pull the news + thesis (Gemini, free, synthesized)

```python
from src.research import research

PROMPT_TEMPLATE = """Research {ticker} ({company_name}) for long-term quality-growth investing.

Cover in concise bullets:

1. **Business model & moat** — what they sell, durable competitive advantages.
2. **Catalysts (next 12 months)** — what could move the stock.
3. **Key risks** — top 3 specific to this name.
4. **Valuation context** — current valuation rich, fair, or cheap vs 5-year average and peers.
5. **Last 30 days news** — material developments (no price commentary).

End with: ONE-SENTENCE THESIS or NO-THESIS verdict.
"""

result = research(PROMPT_TEMPLATE.format(ticker="MSFT", company_name="Microsoft"))
```

### Step 3 — (Optional) Cross-validate for high-stakes positions

If this would be a position >20% allocation, OR the Gemini answer feels uncertain:

```python
from src.research import deep_research

dr = deep_research(f"Should we open a long-term position in {ticker} right now?")
if dr.disagreement_detected:
    # Sources point in different directions — be more cautious. Read both answers.
    # Don't trade automatically. Flag to Robin in next WhatsApp summary.
    ...
```

## After research

Append to `memory/research_log.md`:
```markdown
## <ISO date> — <TICKER>
**Numbers (yfinance):** P/E <X>, fwd P/E <X>, op margin <X>%, rev growth YoY <X>%, FCF $<X>B
**Earnings:** next <date>, in 3d-window: <yes/no>
**Thesis (Gemini):** <one-sentence>
**Catalysts:** <bullet>
**Risks:** <bullet>
**Verdict:** buy / hold / pass
**Cross-validated (deep_research):** yes/no, disagreement: yes/no
**Citations:** [Gemini citations]
```

If verdict is **buy** AND it meets `strategy.md` entry criteria AND passes all
guardrails (including `is_in_earnings_window(ticker) == False`) → add to
`memory/daily/<today>.md` trade-idea draft.

## Anti-pattern
- DO NOT quote P/E, margins, or any number from the Gemini answer — always use yfinance for numbers.
- DO NOT use `deep_research()` for every ticker — it's reserved for high-stakes decisions. Default research is cheap and good enough for screening.
- DO NOT skip yfinance because Gemini already mentioned the numbers — Gemini can be wrong on figures.
