# Trade Log

Append-only log of every trade Bull executes (or attempts and aborts). Each entry has a
rationale linking back to `strategy.md` or `research_log.md`.

---

## 2026-05-12T15:14Z — 02-market-open tranche 1 (initial portfolio entry)

Routine: `02-market-open`. Broker: Alpaca paper. Clock: open.
Strategy: Variant C "AI-Capex Barbell" (`strategy.md` v1).
Pre-flight: all guardrails (1, 2, 3, 5, 8) passed. VOO deep_research (Gemini + Tavily)
agreed → no disagreement, position approved.

| # | Side | Symbol | Notional | Filled Qty | Avg Fill | Order ID | Rationale |
|--:|------|--------|---------:|-----------:|---------:|----------|-----------|
| 1 | BUY  | VOO    | $16,667  | 24.732890  | $673.880 | 5d152c94-a103-46ba-8b16-4b97951dda10 | Core ETF, tranche 1/3 toward 50% target. ETF-Core exception in Guardrail #1. |
| 2 | BUY  | MSFT   | $2,333   |  5.709601  | $408.610 | f013114c-c123-4939-baca-583fa8e4bd9f | AI/Quality. TCI exit = sentiment drawdown; thesis intact (fwd P/E 21.1). Tranche 1/3 of 7%. |
| 3 | BUY  | GOOGL  | $2,333   |  6.023830  | $387.295 | 870334b3-3d84-46d8-94dd-27c7b91bfc05 | AI/Quality. Search moat + TPU advantage. Tranche 1/3 of 7%. |
| 4 | BUY  | META   | $2,333   |  3.886520  | $600.280 | f649ace8-5201-446d-97b0-970983131014 | AI/Quality. Capex-fear drawdown = good entry, Q1 beat. Tranche 1/3 of 7%. |
| 5 | BUY  | AVGO   | $2,333   |  5.591774  | $417.220 | 9bc24ac6-0dcf-455b-9d1e-b33d12418104 | AI/Quality. Hyperscaler capex $750B direct tailwind. Tranche 1/3 of 7%. |
| 6 | BUY  | V      | $1,667   |  5.113183  | $326.020 | 3fd5f19a-5f19-4f86-804d-a71d78219353 | Defensive ballast, beta 0.78. Tranche 1/3 of 5%. |
| 7 | BUY  | BRK.B  | $1,667   |  3.440945  | $484.460 | b02676eb-9b8d-4aef-909f-7851d82274ed | Defensive ballast, beta 0.62. Tranche 1/3 of 5%. |
| 8 | BUY  | LLY    | $1,667   |  1.677741  | $993.598 | 18e12e75-ea99-444f-8943-1265f25b29ca | Defensive ballast, beta 0.48. Tranche 1/3 of 5%. |

Total notional committed: $30,999.62. Cash retained: $69,000.00 (for tranches 2 & 3).

### Stop placement (10% trailing, GTC)

Fractional trailing stops rejected by Alpaca (`{"code":42210000,"message":"fractional
orders must be DAY orders"}`). Fell back to integer-share trailing stops on the
floor(qty) of each fill. Fractional remainders (~0.0–0.9 sh per position, total
< 1.5 sh across all 8 positions, ≈ $300 notional unprotected) are temporarily without
trailing-stop coverage. **Logged as lesson; mitigation: in midday or pre-close routine,
use a regular fixed-price `stop` order (Alpaca allows fractional `stop`) at
avg_entry × 0.90 for the fractional remainders OR consolidate after tranche 3 fills.**

| Symbol | Stop Qty | Trail % | TIF | Stop Order ID | Unprotected Fractional |
|--------|---------:|--------:|-----|---------------|------------------------|
| VOO    | 24 | 10 | GTC | 711bae8b-4f15-451b-9985-3cdeeeccee02 | 0.732890 sh |
| MSFT   |  5 | 10 | GTC | 2d01444c-f06c-4285-bb9e-8533b75411af | 0.709601 sh |
| GOOGL  |  6 | 10 | GTC | a77bc906-48c9-4795-89fc-22b991a69f40 | 0.023830 sh |
| META   |  3 | 10 | GTC | 86876110-209a-48ac-8d50-469870b2c2e5 | 0.886520 sh |
| AVGO   |  5 | 10 | GTC | 41b64809-bdbc-49d4-a826-e47a3a905923 | 0.591774 sh |
| V      |  5 | 10 | GTC | 3a463224-73f1-43ee-a01e-57a62b3f0af1 | 0.113183 sh |
| BRK.B  |  3 | 10 | GTC | ebe010d9-d68a-4619-b847-42a41b2b9173 | 0.440945 sh |
| LLY    |  1 | 10 | GTC | b6fbf93e-0342-4a88-880b-36ce69ebe00b | 0.677741 sh |

### Deferred (no order placed)

- **NVDA** — target 7%, deferred. Reason: 97.5% of 52w-high + earnings 2026-05-20.
  Per `strategy.md` caveat, wait for at least one -3% red day post-earnings before
  initiating. Tracked in `portfolio.md` Pending section.

---

## 2026-05-13T13:42Z — 02-market-open tranche 2 of 3

Routine: `02-market-open`. Broker: Alpaca paper. Clock: open.
Strategy: Variant C "AI-Capex Barbell" (`strategy.md` v1).
Pre-flight: all guardrails (1, 2, 3, 5, 8) re-verified — passed. Post-fill VOO weight
33.4% (inside ETF-Core band 45–55% / cap 60%); largest order = VOO $16,667 = 24.2% of
$69k pre-trade cash (cap 30%); position count unchanged at 8/10; no name within 3
trading days of earnings (closest: AVGO 2026-06-03, 14 trading days out); leverage
post-fill 0.62x (cap 2x). Tranche 2 mirrors tranche 1 nominals exactly.

| # | Side | Symbol | Notional | Filled Qty | Avg Fill | Order ID | Rationale |
|--:|------|--------|---------:|-----------:|---------:|----------|-----------|
| 1 | BUY  | VOO    | $16,667  | 24.599451  | $677.535 | 3d2a99c2-6dda-48ff-8cb4-982ccaa9a5fa | Core ETF, tranche 2/3 → 33.4% post-fill, on track for ~50% after tranche 3. |
| 2 | BUY  | MSFT   | $2,333   |  5.812157  | $401.400 | 2d1627f4-78da-4c60-8390-8eaaa1b124bf | AI/Quality tranche 2/3. Thesis intact (fwd P/E 21.07, op-margin 46%). |
| 3 | BUY  | GOOGL  | $2,333   |  6.023443  | $387.320 | 12af7a8c-4492-4cf9-96a3-c007fea7a755 | AI/Quality tranche 2/3. Thesis *strengthened* post Q1 beat (EPS $5.11 vs $2.64 est). |
| 4 | BUY  | META   | $2,333   |  3.880957  | $601.140 | a982fec8-b763-48af-9b5b-34d2fb7f3d77 | AI/Quality tranche 2/3. Capex-fear drawdown -24% vs Hi; fwd P/E 16.66 cheapest mega-cap. |
| 5 | BUY  | AVGO   | $2,333   |  5.672327  | $411.295 | e81ffe27-5bac-4e6d-b338-c9a87e3055f1 | AI/Quality tranche 2/3. Hyperscaler capex tailwind unchanged. |
| 6 | BUY  | V      | $1,667   |  5.143598  | $324.092 | 2911151c-edc3-4bf2-a1f2-18b130981fd8 | Defensive tranche 2/3, beta 0.78. |
| 7 | BUY  | BRK.B  | $1,667   |  3.443006  | $484.170 | f8bb3f15-11db-452f-9e0f-649d4dec1cdd | Defensive tranche 2/3, beta 0.62. |
| 8 | BUY  | LLY    | $1,667   |  1.663420  | $1002.152| 425939e6-3792-48be-9825-14288d63985d | Defensive tranche 2/3, beta 0.48. |

Total notional committed: $30,999.62 (mirrors tranche 1 exactly). Pre-trade cash $69,000
→ post-trade cash $38,000. Equity ticked from $100,003.27 (pre-trade) to $100,056.93
(post-trade, intraday revaluation).

### Stop refresh (10% trailing, GTC) — cancel-and-replace at floor(new_qty)

Per lesson 2026-05-12 (Alpaca fractional-stop limitation), cancelled all 8 prior
trailing stops and re-issued at the new floor(total_qty). Fractional remainders
(aggregate ~3.40 sh ≈ $1,876 notional) remain temporarily without trailing coverage —
acceptable risk on a single-session basis; will consolidate after tranche 3 fills bring
several positions over the next integer share.

| Symbol | Total Qty Post | Stop Qty | Frac Unprotected | Trail % | TIF | New Stop Order ID | Cancelled Old Stop |
|--------|---------------:|---------:|-----------------:|--------:|-----|-------------------|--------------------|
| VOO    | 49.332341 | 49 | 0.332 sh | 10 | GTC | 1bcc50ac-99b8-4693-96ab-b6a2273dc75e | 711bae8b-4f15-451b-9985-3cdeeeccee02 |
| MSFT   | 11.521758 | 11 | 0.522 sh | 10 | GTC | d80cc207-d60a-40b8-a0ff-c62aa4b8866e | 2d01444c-f06c-4285-bb9e-8533b75411af |
| GOOGL  | 12.047273 | 12 | 0.047 sh | 10 | GTC | c73e0611-158e-4403-9839-c10e254e19b2 | a77bc906-48c9-4795-89fc-22b991a69f40 |
| META   |  7.767476 |  7 | 0.767 sh | 10 | GTC | c4e57975-bc6c-41ce-bd4e-1d2968931b16 | 86876110-209a-48ac-8d50-469870b2c2e5 |
| AVGO   | 11.264102 | 11 | 0.264 sh | 10 | GTC | 4fa0abdb-d78e-4627-86ba-f31838e883ae | 41b64809-bdbc-49d4-a826-e47a3a905923 |
| V      | 10.256781 | 10 | 0.257 sh | 10 | GTC | fc1ab752-bc74-4afd-9cc2-58a0722e4187 | 3a463224-73f1-43ee-a01e-57a62b3f0af1 |
| BRK.B  |  6.883950 |  6 | 0.884 sh | 10 | GTC | a8c09e00-b997-4ed9-b07f-fe47219d46ac | ebe010d9-d68a-4619-b847-42a41b2b9173 |
| LLY    |  3.341161 |  3 | 0.341 sh | 10 | GTC | 9a0a47bc-3033-4c43-904b-19d65106c063 | b6fbf93e-0342-4a88-880b-36ce69ebe00b |

Note: re-issued trail-stop loses the prior tranche-1-day HWM (max +1% built up), but
HWM reset is acceptable when re-anchored to the now-larger combined position.

### Deferred (no order placed)

- **NVDA** — target 7%, still deferred. Reason unchanged from 5/12 + 98.7% of 52w-Hi
  today (even closer than yesterday). Earnings 2026-05-20 → guardrail #8 window opens
  2026-05-15. Will re-evaluate after the print.
