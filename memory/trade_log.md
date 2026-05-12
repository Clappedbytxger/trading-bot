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
