---
created: 2026-05-11
status: awaiting_robin_approval
phase: 1 (Alpaca paper, ~$100k budget)
research_window: TTM ending 2026-05-11
---

# Strategy Candidates — Initial Deep Research

## Macro Backdrop (TL;DR)

- **Fed:** target range 3.50–3.75% (effective 3.64%); held at April 2026 FOMC with 4 dissents. Powell out mid-May 2026, Warsh expected as new chair. Consensus = higher-for-longer. Next cuts priced for Dec 2026 / March 2027 (Goldman); BofA pushes cuts to H2 2027.
- **Inflation:** Core PCE 3.2% YoY (March 2026), still above 2% target. Energy is the main culprit. Goldman sees core PCE easing to ~2.5% by Dec 2026.
- **USD (DXY):** 97.89, down ~3.8% YoY. Range-bound to softer expected — mildly tailwind for US mega-caps with overseas revenue.
- **Equity backdrop:** S&P 500 +~30% TTM. AI capex remains *the* dominant theme — hyperscalers committing >$650B in 2026 capex, ~$500B AI-specific. Tech sector trades at ~11% discount to fair value (Morningstar). Earnings revisions strongest for AI infrastructure, industrials, utilities.
- **Top 3 risks (next 12mo):** (1) Sticky inflation + rate re-acceleration — likelihood 60–70%, severity high. (2) Recession — likelihood 30–49% (GS 30%, Moody's 49%), severity very high. (3) Geopolitical (Middle East, US–China) — likelihood 70–80%, severity high.

All quantitative data below comes from yfinance snapshots taken 2026-05-11. Qualitative claims come from Gemini-grounded research, cross-checked against Tavily for the macro and mega-cap analyses.

---

## Variant A — Pure Quality Growth (Conservative)

> "Don't try to beat the index by much. Just own it, plus a handful of compounders. Survive drawdowns."

- **Allocation:** 60% Core ETF + 40% Mega-Cap quality picks (5 names, 8% each)
- **Core (60%):** **VOO** (Vanguard S&P 500 ETF)
  - TER 0.03%, AUM ~$1.6T, distributing, deeply liquid. Cheapest broadly-liquid option for a US-domiciled paper account.
  - (Phase 2 EU live note: switch to **CSPX** UCITS — 0.07% TER, accumulating, avoids US estate tax exposure >$60k.)
- **Picks (40%, 8% each):**
  1. **MSFT** — Cloud (Azure) + Copilot/AI integration; fwd P/E 21.2, op margin 46%, ROE 34%, FCF $37B.
  2. **GOOGL** — Search moat intact, Cloud growing, Gemini + custom TPUs structural cost advantage; fwd P/E 27.2, op margin 36%, rev growth 22% YoY.
  3. **V** — Visa, global payments rail, beta 0.78, op margin 67%, ROE 60%. Defensive cash compounder.
  4. **BRK-B** — Berkshire, beta 0.62, $61B FCF, broad-economy ballast.
  5. **LLY** — Eli Lilly, GLP-1 leader, rev growth 56% YoY, beta 0.48; non-tech diversifier.
- **Entry criteria:** DCA over 3 trading weeks (split each entry into 3 tranches) to avoid timing risk. Never >30% cash deployed in one order (guardrail #5). No entries within 3 trading days of earnings (guardrail #8).
- **Exit criteria:**
  - Hard stop-loss at **-10%** per position (guardrail #3).
  - Thesis-broken exit: if a pick's TTM operating margin drops >300 bps or revenue growth turns negative for 2 consecutive quarters, trim or sell regardless of stop.
  - Quarterly review: trim any single name above 12% portfolio weight back to 8%.
- **Re-balancing cadence:** Quarterly (1st routine of Jan/Apr/Jul/Oct). VOO is the anchor — rebalance picks back toward target weights, never trim VOO unless above 65%.
- **Expected behavior vs SPX:** Roughly +1–3%/yr alpha potential in normal regimes from the quality tilt (V, BRK, LLY all dampen beta; MSFT/GOOGL tilt toward AI tailwind). In a sharp risk-off, drawdowns roughly equal to SPX (-10% stops cap idiosyncratic losses but VOO will follow market).
- **Pros:** Low concentration risk. Easy to operate. Robust to bot misjudgment — 60% just tracks the index. Aligns with "beat SPX over the long term" mission without requiring genius.
- **Cons:** Capped upside vs AI-thesis-played-perfectly scenario. Three of five picks (V/BRK/LLY) are explicitly defensive — if 2026 turns into a tech melt-up, this variant underperforms.

---

## Variant B — Quality Growth + Tactical Overlay (Moderate)

> "Own a quality core. Lean into the macro theme. Use sector ETFs for the tactical sleeve so we're not picking 10 individual semis."

- **Allocation:** 70% Quality Growth Core + 30% Tactical Sector Rotation
- **Core (70%):**
  - **VOO 35%** (anchor, same rationale as Variant A)
  - **Quality picks 35%, 7 names × 5%:** MSFT, GOOGL, META, AVGO, V, LLY, BRK-B
    - META: fwd P/E 16.7, op margin 41%, rev growth 33% YoY — cheapest mega-cap vs growth in the cohort.
    - AVGO: fwd P/E 23.7, op margin 45%, rev growth 30% — custom AI silicon + VMware recurring revenue.
    - (Others same as Variant A.)
- **Tactical (30%, sector ETFs):**
  - Current allocation (re-evaluated monthly): **SMH 12%** (semis — direct AI capex play), **XLI 10%** (industrials — data center construction, defense), **XLU 8%** (utilities — AI power demand).
  - Each tactical position has its own -10% stop. If a sector ETF drops out of top-3 sector outlook (per monthly research), rotate at month-end.
- **Entry criteria:** Same as Variant A. Tactical sleeve allowed to enter sector ETFs without DCA if a single buy is <30% of available cash.
- **Exit criteria:** -10% stop on every line. Sector ETFs reviewed monthly against the most recent `01-pre-market` macro research; rotate if the thesis weakens.
- **Re-balancing cadence:** Core quarterly. Tactical monthly. Total tactical sleeve never exceeds 35% (1 percentage-point band).
- **Expected behavior vs SPX:** Higher tracking error than A. Targets +3–6%/yr alpha in a continuation regime (AI capex thesis intact). Drawdowns can be deeper than SPX in a sharp tech sell-off because the tactical sleeve is concentrated.
- **Pros:** Direct exposure to the strongest fundamental themes (AI infra, industrials, utilities) without single-stock blow-up risk in the tactical sleeve. Monthly review forces Bull to re-engage with the macro.
- **Cons:** More moving parts → more chances to make a wrong rotation call. Sector ETFs have ~0.10% TER vs 0.03% on VOO — minor drag. Tactical sleeve concentration in semis/industrials means a soft-landing-without-AI scenario hurts disproportionately.

---

## Variant C — Bull-Custom: "AI-Capex Barbell" (My synthesis)

> "Macro says: higher-for-longer + AI capex still accelerating + meaningful recession tail-risk. Don't try to time it. Barbell quality-AI-cashflow on one side, low-beta cashflow compounders on the other, anchored by a low-cost index core."

- **Allocation:** 50% Core ETF + 35% AI/Quality Growth picks + 15% Defensive ballast
- **Core (50%):** **VOO** (same rationale; Phase 2 EU: switch to CSPX)
- **AI/Quality Growth picks (35%, 5 names × 7%):**
  1. **MSFT** (fwd P/E 21.2, FCF $37B, op margin 46%) — Azure + Copilot, the platform play.
  2. **GOOGL** (fwd P/E 27.2, op margin 36%, ROE 39%) — TPU cost advantage + Search moat; outperformed SPX by >100pp TTM on AI re-rating.
  3. **META** (fwd P/E 16.7, op margin 41%, rev growth 33%) — cheapest mega-cap relative to growth in this cohort; Reality Labs drag already discounted.
  4. **AVGO** (fwd P/E 23.7, op margin 45%, rev growth 30%) — custom AI accelerators for hyperscalers; VMware recurring revenue.
  5. **NVDA** (fwd P/E 19.6, op margin 65%, rev growth 73%, FCF $58B) — yes the trailing P/E looks high at 45, but **the forward P/E is just 19.6** because earnings have caught up. ROE 101%. If AI capex digestion comes, this is the first casualty — hence the 7% cap and hard stop.
- **Defensive ballast (15%, 3 names × 5%):**
  1. **V** (Visa, beta 0.78, op margin 67%, ROE 60%) — toll-booth on global commerce.
  2. **BRK-B** (beta 0.62, FCF $61B) — broad-economy hedge, ~28% cash on the balance sheet at this writing.
  3. **LLY** (beta 0.48, rev growth 56%) — non-correlated healthcare growth (GLP-1 still in expansion).
- **Entry criteria:**
  - DCA every position over 3 trading days (split each entry into 3 tranches).
  - No entry within 3 trading days before earnings (guardrail #8).
  - For NVDA specifically: do not initiate full 7% on a 52-week-high day. Wait for at least one -3% red day before completing tranches 2+3.
- **Exit criteria:**
  - Hard -10% stop on every position (guardrail #3).
  - Thesis-broken exit (any pick): op margin drops >300 bps, or 2 consecutive quarters of negative revenue growth, or hyperscaler capex guidance cut >15% (for NVDA/AVGO specifically).
  - Profit-take rule: any single name above 12% of portfolio gets trimmed back to 9% (locks in gains without exiting winners).
- **Re-balancing cadence:** Quarterly band check. Bands: VOO 45–55%, AI/Quality block 30–40% total, defensive 12–18%. If outside band, rebalance.
- **Expected behavior vs SPX:**
  - In a "soft landing + AI capex continues" regime → +4–7%/yr alpha (AI block does the heavy lifting).
  - In a "sticky inflation, no rate cuts, no recession" regime → roughly tracks SPX (defensive ballast neutralizes some upside, AI block keeps pace).
  - In a "recession + AI capex digestion" regime → drawdowns deeper than SPX from the AI sleeve, but V/BRK/LLY (avg beta ~0.63) dampen the bleed; -10% stops cap individual losses.
- **Pros:**
  - Directly aligned with the most evidence-backed macro theme (AI capex).
  - Defensive ballast is genuinely defensive (all three beta <0.8) rather than tech-with-a-defensive-label.
  - Reasonable fwd P/E on the AI block (median ~21) — not a YOLO on growth-at-any-price.
  - 10 positions total (8 + ETF + reserve cash slot) — comfortably under the 10-position guardrail #2 with headroom.
- **Cons:**
  - 35% concentrated in AI-linked mega-caps. A single-issue AI shock hurts all 5 names simultaneously, even though they're nominally diversified across software/silicon/platform.
  - LLY beta of 0.48 is great defensively but the name itself has GLP-1 competition risk (Novo, others) — not a true "uncorrelated" hedge.
  - More work than Variant A to monitor; requires Bull to actually keep an eye on hyperscaler capex guidance.

---

## Recommendation

**My recommendation: Variant C (Bull-Custom).**

One-sentence reasoning: The macro evidence is heavily skewed toward "AI capex is the dominant fundamental driver for the next 12 months, but recession tail-risk is non-trivial" — Variant C is the only one that directly captures both sides (concentrated AI exposure *and* genuine low-beta ballast), while Variant A under-exploits the strongest theme and Variant B introduces single-month rotation calls that the routine cadence is poorly suited to make well.

If you're uncomfortable with 35% concentrated in AI-linked names, **Variant A is the safer fallback** — it will get you ~80% of Variant C's expected return with materially less concentration risk. I would NOT recommend Variant B for Phase 1: monthly sector ETF rotations require timing skill that the routine schedule (one decision pass per day) can't reliably provide, and the tactical sleeve's volatility eats into the position-count guardrail.

---

## Citations

Macro & sector outlook:
- FOMC April 2026 statement and dot plot (federalreserve.gov, via Gemini grounding)
- Bank of America rate-path revision (Reuters via Gemini grounding)
- Goldman Sachs Top-of-Mind / GS Research outlook (gspublishing.com via Gemini)
- BLS / BEA core PCE release (March 2026, bea.gov via Gemini)
- Trading Economics DXY forecast (via Gemini)
- Morningstar US sector fair-value tables (via Gemini)
- Wellington Management 2026 outlook (via Gemini)
- Moody's, JPM, GS, EY-Parthenon recession probabilities (Gemini cross-referenced)

Quantitative fundamentals (all numerical values in this document):
- Yahoo Finance via yfinance snapshots taken 2026-05-11 (`src.research.fundamentals.get_snapshot`)

ETF tax/structure:
- Vanguard / iShares / SSGA fund factsheets (via Gemini)
- EU PRIIPs / US estate tax overview (via Gemini)

(Full citation URLs preserved in `/tmp/strategy_research/*.json` during the routine — not committed to memory to stay under token budget.)

---

## How to approve (Robin — manual step)

1. Pick a variant (A, B, or C, or propose a Variant D in `strategy_proposals.md`).
2. Overwrite `memory/strategy.md` with the chosen variant's content.
3. Update the frontmatter:
   ```
   ---
   version: 1
   approved: true
   created: 2026-05-11
   last_modified: <today>
   ---
   ```
4. Commit. The next scheduled routine (`01-pre-market` or `02-market-open`) will see `approved: true` and may begin placing trades within the hard guardrails in `CLAUDE.md`.

Until then, Bull stays in research-only mode. No trades.
