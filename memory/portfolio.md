---
last_updated: 2026-05-15T13:55:00Z
broker: alpaca
account_type: paper
total_value_usd: 100804.03
cash_usd: 38000.00
day_pnl_pct: -0.3878
ytd_pnl_pct: 0.8040
benchmark_spx_ytd: 8.597
spy_ytd_reference_date: 2026-01-02
spy_ytd_reference_close: 681.31
spy_today_price: 739.88
alpha_vs_spx: -7.793
position_count: 8
---

# Portfolio — 02-market-open 2026-05-15 (intraday, 13:55Z re-fire snapshot)

**No trades today.** Same status as the 13:30Z run — DCA tranche 3 of 3 remains
**blocked** by missing on-time pre-market draft (2nd consecutive business day) and
pending Robin A/B/C reply. This snapshot is a light refresh after `02-market-open`
already ran cleanly at 13:30Z. Daily file has the full prior analysis under
`## 02-market-open`; the re-fire note is appended under `## 02-market-open (13:55Z re-fire)`.

Equity intraday at **$100,804.03** vs yesterday close $101,196.48 → **Day P&L
-$392.45 / -0.388%** (+10 bp recovery vs 13:30Z snapshot at -0.483%). SPY now
$739.88 → SPY day -1.11% (recovered ~9 bp from -1.20% at the open). **Bull beat SPY
by +72 bp on the day** (unchanged); alpha-vs-SPX unchanged at **-7.79%**. All 8
positions still green on UPL: worst BRK.B **+0.30%** (slightly off the 13:30Z
+0.40%), best GOOGL **+2.92%** (rotated up from META/MSFT as GOOGL bounced +1.10%
vs 13:30Z). Day-best mover into the 13:55Z mark: GOOGL **+1.10%** intraday;
day-worst: MSFT **-0.36%** intraday off its 13:30Z high. AVGO stabilised
(+0.05% intraday) after the -3.19% opening drop.

SPY now **$739.88** → SPY YTD **+8.597%** (vs 2026-01-02 ref $681.31). Bull YTD
**+0.804%** → **Alpha vs SPX -7.793%** (mechanically unchanged — both legs
ticked up ~10 bp together).

All 8 trailing stops verified GTC, status=new, no fills, no modifications. HWMs
ratcheted on 2 of 8 since 13:30Z snapshot: MSFT 417.35 → **418.26**, V 327.11 →
**328.37**. (BRK.B 487.14 → 487.1399 — within rounding, treated unchanged.) No
position within 7 percentage points of its -10% stop (closest is AVGO at 7.0% above
stop). No stop-tightening trigger fired (threshold +15% UPL; best GOOGL +2.92%).

## Open Positions

| Symbol | Qty | Avg Entry | Now | Market Value | Unrealized P&L | Day Δ | Alloc % | Target % | Trail-Stop |
|--------|----:|----------:|----:|-------------:|---------------:|------:|--------:|---------:|------------|
| VOO    | 49.332341 | $675.703 | $680.570 | $33,574.11 | +$240.11 (+0.72%) | -1.05% | 33.31% | 50% (Core ETF) | 10% trail on 49 sh GTC, HWM $689.10, stop $620.19 — 0.332 sh unprotected |
| MSFT   | 11.521758 | $404.973 | $415.950 |  $4,792.47 | +$126.47 (+2.71%) | +1.97% |  4.75% |  7%            | 10% trail on 11 sh GTC, HWM **$418.26** (↑) , stop $376.43 — 0.522 sh unprotected |
| AVGO   | 11.264102 | $414.236 | $426.005 |  $4,798.56 | +$132.56 (+2.84%) | -3.24% |  4.76% |  7%            | 10% trail on 11 sh GTC, HWM $442.36, stop $398.12 — 0.264 sh unprotected |
| GOOGL  | 12.047273 | $387.308 | $398.630 |  $4,802.40 | +$136.40 (+2.92%) | -0.49% |  4.76% |  7%            | 10% trail on 12 sh GTC, HWM $403.70, stop $363.33 — 0.047 sh unprotected |
| META   |  7.767476 | $600.710 | $612.280 |  $4,755.87 |  +$89.87 (+1.93%) | -0.78% |  4.72% |  7%            | 10% trail on 7 sh GTC, HWM $623.73, stop $561.36 — 0.767 sh unprotected |
| LLY    |  3.341161 | $997.857 |$1008.720 |  $3,370.30 |  +$36.30 (+1.09%) | +0.20% |  3.34% |  5%            | 10% trail on 3 sh GTC, HWM $1022.82, stop $920.54 — 0.341 sh unprotected |
| V      | 10.256781 | $325.053 | $328.215 |  $3,366.43 |  +$32.43 (+0.97%) | +1.77% |  3.34% |  5%            | 10% trail on 10 sh GTC, HWM **$328.37** (↑) , stop $295.53 — 0.257 sh unprotected |
| BRK.B  |  6.883950 | $484.315 | $485.750 |  $3,343.88 |   +$9.88 (+0.30%) | +0.19% |  3.32% |  5%            | 10% trail on 6 sh GTC, HWM $487.14, stop $438.43 — 0.884 sh unprotected |

Total committed: $62,804.03 (62.30% of equity)
Cash retained: $38,000.00 (37.70%)
Open positions: 8 / 10 (NVDA deferred; 9th slot held in reserve)
Leverage: 0.62x (cap 2x)
Day P&L: -$392.45 (-0.388%) — Bull beat SPY day -1.11% by **+72 bp** on cash drag
+ defensive-sleeve resilience (alpha unchanged vs 13:30Z snapshot).
Fractional uncovered: ~3.40 sh aggregate ≈ ~$1,890 notional (~1.88% of equity).
Mitigation still deferred until after tranche 3 consolidates remainders to ≥1 whole share.

## Pending (not yet opened)

- **NVDA** — target 7%. Earnings 2026-05-20 (Wed) post-close. Guardrail-#8 earnings
  window **opens today 2026-05-15**. Entry blocked. Re-evaluate post-print per
  strategy caveat (needs ≥1 -3% red day before completing tranches 2+3; still
  near 52w-Hi pre-print).
- **DCA tranche 3 of 3** — **STILL BLOCKED, now 2 days in a row.** Pattern: 5/13
  tranche 2 fired; 5/14 tranche 3 blocked (missing pre-market); 5/15 tranche 3
  blocked again (missing pre-market, no Robin reply on A/B/C). De-facto path is now
  the "(C) defer a full week into post-NVDA / post-Fed-transition window" from
  yesterday's 04-pre-close — but that needs to become an explicit Robin choice,
  not a runner-failure default.

## DCA progression

- Tranche 1 of 3: **executed 2026-05-12** (8 names, $30,999.62 notional).
- Tranche 2 of 3: **executed 2026-05-13** (8 names, $30,999.62 notional).
- Tranche 3 of 3: **NOT EXECUTED 2026-05-14** — blocked by missing pre-market draft.
- Tranche 3 of 3: **NOT EXECUTED 2026-05-15** — same root cause + Robin reply pending.
  Post-tranche-3 weights would land near: VOO ≈ 50%, AI/Quality ≈ 7% each,
  defensive ≈ 5% each (vs today's: VOO 33.29%, AI/Quality 4.71–4.78% each,
  defensive 3.32–3.35% each).

## Recent Closed Positions (last 5)

(none)
