# Experiments — Learning Month trade journal

One file per active sub-strategy from `memory/playbook.md`. Bull appends per-trade
notes here on every executed entry/exit during Learning Month (2026-05-21 → 2026-06-20).

## File naming convention
- `_ledger.md` — KPI roll-up (updated daily by 05-close-summary)
- `<strategy-slug>.md` — per-strategy trade journal (e.g. `swing-momentum-breakout.md`)
- `_final_report_2026-06-20.md` — generated on last day of Learning Month

## Per-trade entry format

```
## YYYY-MM-DD HH:MMZ — <ENTRY|EXIT|UPDATE> <TICKER> <BUY|SELL|SHORT|COVER>
- **Sleeve / Strategy:** <Sleeve> / <slug>
- **Trigger hit:** which exact condition from playbook.md fired
- **Position:** <qty> @ <price> = $<notional>; stop @ <price>; target @ <price>
- **Thesis (1-2 lines):** why this fits the strategy
- **Expected R-multiple:** target/risk ratio expected
- **Actual (on exit only):** realized P&L $, R-multiple, days held, delta vs expected
- **Lesson if any:** one-liner; only if a generalizable rule emerged
```

## Files are append-only

Never delete entries. The full per-strategy trade history is the input to the
weekly bandit cull and the final 2026-06-20 report.
