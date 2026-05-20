---
version: 3
approved: true
created: 2026-05-11
last_modified: 2026-05-20
learning_month_window: 2026-05-21 → 2026-06-20
---

## Active Strategy — "Learning Month" Multi-Sleeve (v3)

> "Before risking real money, run 4 weeks of parallel experiments across timeframes,
> asset classes, and directionality. Each sleeve is its own micro-lab with its own
> entry/exit/sizing rules. Goal: produce a playbook of what works for the €300
> live-money phase, not maximize this month's paper P&L."

**Window**: 2026-05-21 → 2026-06-20 (30 days). On 2026-06-21 this file auto-archives
to `memory/strategy_learning_month_2026-05.md` and Live-Phase Variant C (Section 2)
reactivates.

### Sleeve allocations

| Sleeve | Cash budget | Max positions | Position size cap | Stops | Direction |
|---|---:|---:|---:|---|---|
| **Core** (frozen) | $62k (existing 8 names + VOO) | 8 (fixed) | unchanged | -10% trail | long-only |
| **Swing** | $15k | 8 | $4k notional | -5 to -7% / ATR | long + short |
| **Daytrade/Scalp** | $10k | 5 (intraday only) | $4k notional | -0.5 to -1.5% | long + short |
| **Crypto** | $5k | 4 | $2k notional | -8% trail (GTC) | long-only |
| **Options** | $5k premium | 6 contracts | $1k premium / pos | -50% premium (long) or spread-width (defined-risk) | long calls/puts/spreads |
| **Cash reserve** | ≥$3k | — | — | — | — |
| **Total** | $100k | up to 31 | — | — | — |

### Sleeve 1 — Core (frozen during Learning Month)

**Contents**: VOO, MSFT, GOOGL, META, AVGO, V, BRK.B, LLY (8 names) — current
holdings as of 2026-05-20. Trailing -10% stops remain active.

**Rules**:
- No new entries, no trims, no rebalances during Learning Month UNLESS:
  - A trailing stop triggers (then take the fill, log it, no re-entry on this sleeve).
  - A thesis-break event fires per the Variant-C exit criteria (Section 2).
  - Tranche-3 DCA decision is suspended for Learning Month — re-evaluate 6/21 onward.
- NVDA: hold as a Learning-Month "candidate" — entry via Swing sleeve allowed post-earnings if a clear momentum or mean-reversion setup forms.
- Day-over-day P&L on Core is the **Live-Phase benchmark** the other sleeves are
  measured against.

**Strategy slug for tagging**: `core-buy-and-hold`.

### Sleeve 2 — Swing-Experiment

**Mandate**: 2-5 trading day holds. Diversified strategy archetypes; cycle through
them to find what works.

**Sub-strategies (defined in `memory/playbook.md`)**:
- `swing-momentum-breakout` — 20-day high + volume + RSI > 60
- `swing-mean-reversion` — 2σ below 20-day MA + RSI < 30 on quality names
- `swing-quality-pullback` — top-50-quality screen + 5-10% pullback from 52w-Hi
- `swing-earnings-drift` — post-earnings strong-beat with positive guide; enter day-after
- `swing-insider-buys` — Form 4 cluster-buys (Polygon data) on small/mid-caps
- `swing-short-rejection` — 52w-Hi rejection candle on overextended names (short)
- `swing-short-fundamental` — deteriorating margins + multiple compression (short)

**Entry**: At market-open or on confirmed signal during 02/03/04 routines. Max 2 new
entries per routine to throttle exploration.

**Exit**: -5 to -7% stop / 1.5-2R target / time-stop 5 trading days. ATR-based stop
preferred when ATR available.

**Sizing**: equal-weight ~$1.5-2k per name (= 1/8 to 1/10 of sleeve budget).

### Sleeve 3 — Daytrade/Scalp

**Mandate**: Intraday only. Flat by 04-pre-close (20:30Z = 16:30 ET). NO overnight.

**Sub-strategies (in `memory/playbook.md`)**:
- `daytrade-orb` — Opening Range Breakout, 5-min ORB on highly liquid names (SPY, QQQ, NVDA, TSLA, AAPL, AMD)
- `daytrade-vwap-pullback` — Long pullback to VWAP in established uptrend; short the inverse
- `daytrade-gap-fade` — Fade open gap on overextended pre-market movers (no clear catalyst)
- `daytrade-gap-go` — Ride gap on positive catalyst (earnings beat, analyst upgrade)
- `scalp-tape` — Pure tape-reading 1m chart on /ES, /NQ proxy ETFs (SPY, QQQ) — micro-scalp 0.1-0.3% moves
- `daytrade-news-catalyst` — React to FOMC minutes, CPI prints, surprise earnings within 10min of release

**Entry**: 02/03 routines for ORB and VWAP; news-catalyst any routine where a tagged
event hits.

**Exit**: -0.5 to -1.5% stop. Targets: 1R for scalps, 2-3R for ORB/VWAP. **All
positions MUST be flat by 04-pre-close.** Robin-override required to roll an
intraday position to Swing.

**PDT constraint**: max 3 day-trades per rolling 5-day window until PDT flag auto-
activates on Alpaca (4th day-trade triggers it). Track day-trade count carefully.

### Sleeve 4 — Crypto

**Mandate**: 24/7 crypto exposure via Alpaca-native crypto trading. Long-only
(Alpaca paper doesn't support crypto shorting).

**Universe**: BTC/USD, ETH/USD, SOL/USD, AVAX/USD, LINK/USD (the top-5 by liquidity
on Alpaca).

**Sub-strategies**:
- `crypto-trend-follow` — Long when 50-DMA > 200-DMA on daily; exit on cross-down or -8% trail
- `crypto-weekend-momentum` — Long Friday-close, exit Monday-open if green ≥2% (capitalize on retail weekend tape)
- `crypto-mean-reversion` — Long after -10% intraday flush + ETH dominance check

**Entry**: 03-midday and 05-close-summary on weekdays; 03-midday on weekends (Sat
+ Sun).

**Exit**: -8% trail (GTC). Profit-take: scale 1/3 at +10%, 1/3 at +25%, let rest ride.

### Sleeve 5 — Options

**Mandate**: experimentation with derivatives mechanics. Alpaca Options Level 3
enabled (long calls/puts + verticals + multi-leg).

**Sub-strategies**:
- `options-long-call-momentum` — Long ATM-to-ITM calls on tickers showing momentum signal (often same names as swing-momentum-breakout)
- `options-protective-put` — Hedge Core sleeve by buying SPY OTM puts before known macro events (FOMC, CPI)
- `options-vertical-bull-call-spread` — Defined-risk directional bet; ~30-45 DTE, ~10-delta short leg
- `options-earnings-strangle` — Long ATM call + ATM put pre-earnings on names with high IV-rank, exit morning-after on either leg ≥ 80% of total premium
- `options-cash-secured-put` — Sell ATM put on quality names; collect premium or get assigned at discount (Level 3 enables this on paper)

**Entry**: 01-pre-market and 02-market-open for earnings/event-driven; intraday on
catalyst triggers.

**Exit**: -50% of debit-premium stop on long single-leg. Spreads: max loss = spread
width (built-in). Time stops: 7 DTE forced close to avoid theta cliff and gamma
risk on Friday expirations.

### Macro / risk-off override

If SPY drops -3% in a single day OR VIX spikes >40, ALL sleeves except Core go to
defensive mode immediately:
- Swing: close all longs, hold cash; consider selective shorts only.
- Daytrade: flat for the rest of the day, no new entries.
- Crypto: tighten trail to -5%.
- Options: close any naked long calls; let protective puts run.

This rule is enforced by 03-midday and 04-pre-close — they check the macro condition
explicitly.

### Strategy-bandit weekly cull (06-weekly-review)

Every Friday, rank sub-strategies by **(realized P&L) / (max risk taken)** over the
trailing 7 days. Min sample = 3 trades.
- Bottom-1 strategy → budget halved next week.
- Top-1 strategy → budget +50% next week (rebalanced from bottom-1 and from cash reserve).
- Strategies with 0 trades in 7 days: review whether the trigger was unreachable
  (then loosen) or whether market simply didn't offer setups (then keep dormant).

---

## Reference — Live-Phase Strategy (reactivates 2026-06-21)

### Variant C — Bull-Custom: "AI-Capex Barbell" (locked, awaits Live phase)

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
  - DCA every position over 3 trading days (split each entry into 3 tranches). **Each tranche must satisfy guardrail #5: the single largest order in any tranche may not exceed 30% of available cash at the time of execution.** For positions whose target nominal exceeds ~20% of starting equity (e.g. VOO at 50%), the executable tranche size is therefore `min(target_nominal_per_tranche, 0.30 × current_cash_at_open)`, and any residual rolls into an additional tranche on the next trading day. Pre-flight every tranche on `cash_at_open`, not just at strategy-design time. (Added v2 2026-05-16 per strategy_proposals.md.)
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
