---
name: send-whatsapp
description: Format and send a German WhatsApp summary to Robin via CallMeBot. Use in routines 02-market-open, 05-close-summary, 06-weekly-review (or for urgent alerts).
---

# Skill: send-whatsapp

Robin reads these on his phone. Make them scannable in 5 seconds.

## Rules

- **German.** Robin's native language.
- **< 1000 characters** (CallMeBot has a soft limit; WhatsApp render quality degrades over ~1500 chars).
- **No emojis except the structured ones in the template** — they aid scanning, not decoration.
- **Numbers must be exact.** No rounding to "ungefähr". USD with $, percentages with %.
- **Never include API keys, order IDs, or anything sensitive.**
- **WhatsApp-Markdown only:** `*bold*`, `_italic_`, `~strikethrough~`, `` `monospace` ``. No standard markdown headers (#) — they render as literal text.

## Template — Market Open (02)

```
🐂 Market Open — <Mo/Di/Mi/Do/Fr> <DD.MM.>

💼 Portfolio: $<X> (Cash $<Y>)
📊 YTD: +<X.X>% (S&P: +<Y.Y>%) → Alpha: +<Z.Z>%

🔁 Trades heute:
• <BUY/SELL> <qty> <TICKER> @ ~$<price> (<alloc>%)
(oder: "Keine Trades heute — alle Positionen im Plan.")

⚠️ Flags: <kurz, nur wenn relevant>

📅 Plan: <1 Satz>
```

## Template — Close Summary (05)

```
🐂 Tagesschluss — <Mo/Di/Mi/Do/Fr> <DD.MM.>

💼 Equity: $<X> (Tag: +/-<Y.Y>%)
📈 YTD: +<X.X>% (S&P: +<Y.Y>%) → Alpha: +/-<Z.Z>%

🔁 Trades: <count>
🏆 Best: <TICKER> +<X.X>%
💔 Worst: <TICKER> -<Y.Y>%

💡 <Lesson nur wenn neu gespeichert>

📅 Morgen: <1 Satz>
```

## Template — Weekly Review (06)

```
🐂 *Wochenrückblick* KW <NN>

💼 Equity: $<X> (Woche: +/-<Y.Y>%)
📈 YTD: +<X.X>% vs S&P +<Y.Y>% → Alpha: +/-<Z.Z>%

🔁 Trades: <count>
🏆 Best: <TICKER> +<X.X>%
💔 Worst: <TICKER> -<Y.Y>%

📊 Self-Grade: D=<A-F>, R=<A-F>, Risk=<A-F>, Mem=<A-F>

💡 Lesson: <1-2 Sätze>

🔧 Strategie-Vorschlag: <ja, siehe Repo / nein>

📅 Nächste Woche: <1 Bullet>
```

## Code

```python
from src.notify.whatsapp import send_routine_summary

body_de = "..."  # one of the templates above, filled in
send_routine_summary("Market Open", body_de)
```

## Urgent alert (any routine can send)

If something urgent happens (guardrail violated, broker error, big drawdown), send
ad-hoc:
```python
from src.notify.whatsapp import send_whatsapp

send_whatsapp(
    "🚨 Bull-Alert: <TICKER> -<X>% intraday auf negative Nachrichten. "
    "Position teilweise geschlossen ({qty} @ ${price}). Details: memory/daily/{today}.md"
)
```
