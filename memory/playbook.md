# Playbook — Strategy Taxonomy

Active only during Learning Month (2026-05-21 → 2026-06-20). Each sub-strategy has
a slug, a sleeve, entry / exit / sizing rules, and a current status. Trade-log
entries during Learning Month MUST tag the `strategy:` slug from this file.

Bull may add/remove/refine sub-strategies autonomously — but every change must be
committed via PR and reflected in `memory/experiments/_ledger.md`.

---

## Format

```
### <slug>  (sleeve: <Sleeve>, status: <active|paused|killed>)
- **Thesis (1 line):** ...
- **Entry trigger:** specific quantitative/qualitative condition
- **Position size:** $X notional (or N contracts)
- **Stop:** -X%
- **Target:** +XR or +X%
- **Time stop:** N days/hours
- **Data needed:** yfinance / Polygon / Gemini
- **Notes:** open issues, edge cases
```

---

## Core (frozen — no new entries)

### `core-buy-and-hold` (sleeve: Core, status: active)
- **Thesis:** Live-Phase Variant-C benchmark. Hold the 8 existing names + VOO with -10% trail; no new orders during Learning Month.
- **Entry trigger:** None (frozen).
- **Position size:** As of 2026-05-20 inheritance.
- **Stop:** -10% trail (GTC, fractional handled via floor(qty) + uncovered slice).
- **Target:** Buy-and-hold, no profit-take during Learning Month.
- **Data needed:** yfinance for monitoring.

---

## Swing (2-5 day holds, long + short)

### `swing-momentum-breakout` (sleeve: Swing, status: active)
- **Thesis:** Stocks breaking 20-day high on above-avg volume + RSI > 60 tend to extend 3-7 days.
- **Entry trigger:** Close ≥ 20-day high AND volume ≥ 1.5x 20-day avg AND RSI(14) > 60. Polygon 1d aggregates.
- **Position size:** $1.5-2k notional.
- **Stop:** -5% from entry (or -1 ATR(14), whichever tighter).
- **Target:** +2R (10% from entry) OR close below 5-DMA, whichever first.
- **Time stop:** 5 trading days. Exit at market if neither stop nor target hit.
- **Data needed:** Polygon (aggregates + volume), yfinance (RSI).
- **Notes:** avoid earnings-week names (use Learning-Month-ALM-7 only if explicit earnings-strategy).

### `swing-mean-reversion` (sleeve: Swing, status: active)
- **Thesis:** Quality names (positive op margin, positive rev growth) that pull 2σ below 20-day MA on RSI < 30 tend to bounce.
- **Entry trigger:** Price ≤ MA20 - 2σ(20) AND RSI(14) < 30 AND ticker in S&P 500.
- **Position size:** $1.5-2k.
- **Stop:** -5% from entry.
- **Target:** Return to MA20 (~+5-7%).
- **Time stop:** 5 trading days.
- **Data needed:** Polygon (price/vol), yfinance (RSI + fundamentals filter).
- **Notes:** avoid biotech and small-caps — too binary.

### `swing-quality-pullback` (sleeve: Swing, status: active)
- **Thesis:** Quality compounders (ROE > 15%, op margin > 20%, rev growth > 10%) that pull back 5-10% from 52w-Hi without thesis-break offer favorable risk/reward.
- **Entry trigger:** Price 5-10% below 52w-Hi AND fundamentals filter met AND no negative earnings revision in 30 days.
- **Position size:** $1.5-2k.
- **Stop:** -5% from entry.
- **Target:** +7% or recovery to 52w-Hi.
- **Time stop:** 7 trading days.
- **Data needed:** yfinance (fundamentals + 52w-Hi).

### `swing-earnings-drift` (sleeve: Swing, status: active)
- **Thesis:** Post-earnings strong beats (rev + EPS beat + guide raise) trigger 1-2 week drift higher (post-earnings announcement drift, PEAD).
- **Entry trigger:** Day-after earnings: stock up ≥ 5% on print AND guidance raised AND analyst PT raises within 24h.
- **Position size:** $1.5-2k.
- **Stop:** -7% from entry (wider — earnings volatility).
- **Target:** +10% or 10 trading days.
- **Time stop:** 10 trading days.
- **Data needed:** Polygon (price reaction), Gemini (PT changes), yfinance (earnings dates).

### `swing-insider-buys` (sleeve: Swing, status: paused)
- **Thesis:** Cluster of insider Form-4 buys ($1M+ aggregate) on a sub-$10B name predicts 3-month outperformance.
- **Entry trigger:** Requires SEC Form-4 data feed. Polygon doesn't supply this directly.
- **Status:** PAUSED — pending evaluation of `https://openinsider.com` scrape or commercial feed.
- **Note:** revisit week 2 of Learning Month.

### `swing-short-rejection` (sleeve: Swing, status: active)
- **Thesis:** Overextended names (RSI > 75 on weekly, price > 30% above 200-DMA) printing a rejection candle at 52w-Hi tend to give back 5-10%.
- **Entry trigger:** Daily candle close < open AND high = 52w-Hi AND RSI(14, weekly) > 75. Short.
- **Position size:** $1.5-2k notional (short).
- **Stop:** Above the rejection-candle high + 1%.
- **Target:** -7% from entry OR break of 20-DMA support.
- **Time stop:** 5 trading days.
- **Data needed:** Polygon (daily aggregates), yfinance.
- **Notes:** Hard-to-borrow check via Alpaca before entry; some names not shortable.

### `swing-short-fundamental` (sleeve: Swing, status: active)
- **Thesis:** Companies with deteriorating op margins (>300bp YoY decline) + multiple expansion (fwd P/E +20% YoY) face de-rating.
- **Entry trigger:** Most recent quarter op margin down >300bp YoY AND current fwd P/E > 1y-ago fwd P/E + 20%. Short.
- **Position size:** $1.5-2k.
- **Stop:** -7% from entry.
- **Target:** -15% or fwd P/E back to 1y-ago level.
- **Time stop:** 15 trading days.
- **Data needed:** yfinance (margins, P/E history).

---

## Daytrade / Scalp (intraday only, flat by 04-pre-close)

### `daytrade-orb` (sleeve: Daytrade, status: active)
- **Thesis:** First 5-min range often defines the day's range. Break out + volume = continuation.
- **Entry trigger:** Break of 5-min opening range (high or low) on >150% of 5-min avg volume. Universe: SPY, QQQ, NVDA, TSLA, AAPL, AMD, META, MSFT.
- **Position size:** $3-4k notional.
- **Stop:** Opposite side of the 5-min ORB range.
- **Target:** 2x range width.
- **Time stop:** Force-flat by 20:30Z (04-pre-close).
- **Data needed:** Polygon 1-min aggregates (REAL-TIME — Alpaca free-tier 15-min-delayed kills this strategy).
- **Notes:** PDT-count this trade. Avoid first 5-min if SPY gap > 1% — wait for ORB to fully form.

### `daytrade-vwap-pullback` (sleeve: Daytrade, status: active)
- **Thesis:** In trending day, price pulls back to VWAP and bounces if trend is real.
- **Entry trigger:** 5-min close > VWAP for ≥30min AND pullback to VWAP ± 0.1% AND tape shows bid-stacking. Long. Inverse for short.
- **Position size:** $3-4k.
- **Stop:** 0.5-1% below VWAP entry.
- **Target:** Recent high of day (or 2x stop, whichever smaller).
- **Time stop:** Force-flat by 20:30Z.
- **Data needed:** Polygon 1m / 5m aggregates incl. VWAP.

### `daytrade-gap-fade` (sleeve: Daytrade, status: active)
- **Thesis:** Pre-market gaps without clean catalyst tend to fade in first 60min.
- **Entry trigger:** Pre-market gap > 3% AND no major news catalyst found via Gemini search AND stock is in S&P 1500.
- **Position size:** $3-4k. Direction: fade the gap.
- **Stop:** 50% of gap size.
- **Target:** Close half the gap.
- **Time stop:** 60 min after open.
- **Data needed:** Polygon (pre-market), Gemini (news scan).

### `daytrade-gap-go` (sleeve: Daytrade, status: active)
- **Thesis:** Earnings-beat or analyst-upgrade gaps with strong volume continue in the gap direction.
- **Entry trigger:** Pre-market gap > 3% AND clear catalyst (earnings, upgrade, M&A) AND open candle confirms direction (first 1m holds gap level).
- **Position size:** $3-4k. Direction: with the gap.
- **Stop:** Open price (gap-fill stop).
- **Target:** 2x gap size from open.
- **Time stop:** Force-flat by 20:30Z.

### `scalp-tape` (sleeve: Daytrade, status: active)
- **Thesis:** Pure tape-reading on highly-liquid ETFs catches 0.1-0.3% micro-moves.
- **Entry trigger:** 1-min momentum on SPY/QQQ — close > high of previous 3 candles AND volume > 2x avg. Long. Inverse for short.
- **Position size:** $4k (larger because tighter stop = lower $ risk).
- **Stop:** 0.15% from entry.
- **Target:** 0.3% (= 2R).
- **Time stop:** 15 min.
- **Data needed:** Polygon 1m aggregates real-time.
- **Notes:** PDT-cost is HIGH (each round-trip = 1 day-trade). Use sparingly while non-PDT, max 1 per day until 4-day-trade threshold flips PDT on.

### `daytrade-news-catalyst` (sleeve: Daytrade, status: active)
- **Thesis:** Major scheduled releases (FOMC, CPI, PPI, NFP) trigger 0.5-2% index moves within 10 min.
- **Entry trigger:** Release hits expected window; direction confirmed by first 1m candle on SPY post-release.
- **Position size:** $3-4k on SPY or QQQ.
- **Stop:** Opposite of post-release first candle high/low.
- **Target:** 2x stop.
- **Time stop:** 30 min post-release.
- **Data needed:** Gemini for release time + consensus; Polygon for execution.

---

## Crypto (24/7, long-only on Alpaca paper)

### `crypto-trend-follow` (sleeve: Crypto, status: active)
- **Thesis:** Crypto exhibits strong trends; 50/200 DMA cross has been profitable historically.
- **Entry trigger:** Daily 50-DMA crosses above 200-DMA on BTC/USD or ETH/USD.
- **Position size:** $1.5-2k per coin.
- **Stop:** -8% trail (GTC).
- **Target:** No fixed target; trail until 50-DMA crosses back below 200-DMA.
- **Data needed:** yfinance (`BTC-USD`, `ETH-USD` daily).

### `crypto-weekend-momentum` (sleeve: Crypto, status: active)
- **Thesis:** Retail tape on weekends amplifies trend. Friday-close longs that show momentum into Monday-open often extend.
- **Entry trigger:** Fri 21:00Z (05-close-summary): BTC/USD up >2% for the week AND no negative regulatory news.
- **Position size:** $1-1.5k.
- **Stop:** -5% (tighter for short hold).
- **Target:** Exit Mon 14:00Z (after 02-market-open) if green ≥ 2%; else hold to crypto-trend-follow logic.
- **Data needed:** yfinance + Gemini (news scan).

### `crypto-mean-reversion` (sleeve: Crypto, status: active)
- **Thesis:** Crypto -10% intraday flushes often bounce ≥5% within 24-48h on quality coins.
- **Entry trigger:** BTC/ETH/SOL down >10% in 24h AND no fundamental break (i.e., not an exchange collapse).
- **Position size:** $1.5-2k.
- **Stop:** -5% from entry.
- **Target:** +5% bounce.
- **Time stop:** 48 hours.
- **Data needed:** yfinance (24h returns), Gemini (news scan).

---

## Options (Level 3 enabled — long calls/puts + spreads + multi-leg)

### `options-long-call-momentum` (sleeve: Options, status: active)
- **Thesis:** Calls on momentum-breakout names amplify the underlying move.
- **Entry trigger:** Same as `swing-momentum-breakout`. Strike: ATM or 1-strike ITM. Expiry: ~30-45 DTE.
- **Position size:** ~$500 premium per contract; max 2 contracts.
- **Stop:** -50% of premium paid.
- **Target:** +100% premium or expire 7 DTE out (close to avoid theta cliff).
- **Time stop:** Close at 7 DTE regardless of P&L.
- **Data needed:** Polygon options-chain (Options-Starter add-on required).

### `options-protective-put` (sleeve: Options, status: active)
- **Thesis:** Buying SPY OTM puts before known catalysts (FOMC, CPI) hedges Core sleeve drawdown.
- **Entry trigger:** Day before scheduled FOMC announcement or CPI/PPI release.
- **Position size:** 1 SPY put per $30k Core equity, ~5% OTM, ~30 DTE.
- **Stop:** None — hedge runs through event.
- **Target:** Close morning after event (regardless of profit/loss). Net P&L is the cost of the hedge.
- **Data needed:** Gemini (event calendar), Polygon (chain).

### `options-vertical-bull-call-spread` (sleeve: Options, status: active)
- **Thesis:** Defined-risk directional bet with capped max-loss = net debit.
- **Entry trigger:** Same as swing-momentum-breakout OR swing-quality-pullback. Buy ATM call, sell ~10-delta OTM call. 30-45 DTE.
- **Position size:** Net debit ≤ $500 per spread; max 2 spreads.
- **Stop:** None — max loss = net debit.
- **Target:** +60% of max profit OR 7 DTE close.
- **Data needed:** Polygon options-chain.

### `options-earnings-strangle` (sleeve: Options, status: active)
- **Thesis:** Pre-earnings IV-rank > 70 names where realized move historically exceeds implied move offer long-vol edge.
- **Entry trigger:** Day-of-earnings close: IV rank > 70 AND avg historical 5-day post-earnings move > implied move from straddle premium.
- **Position size:** 1 strangle = 1 ATM call + 1 ATM put, max $800 total premium.
- **Stop:** None (defined max-loss = total premium).
- **Target:** Close winning leg morning-after at 80% of total strangle premium recouped. If both legs intact (low realized move), close 1 day post-earnings to avoid IV crush.
- **Data needed:** Polygon options-chain + IV calc; Gemini for earnings calendar.

### `options-cash-secured-put` (sleeve: Options, status: paused)
- **Thesis:** Sell ATM puts on quality names with cash backing; collect premium or get assigned at discount.
- **Status:** PAUSED — needs cash collateral commitment; revisit in week 2 of Learning Month after seeing how other Options strategies use the $5k premium budget.

---

## Status legend
- **active**: Bull may take trades on this strategy if triggers fire.
- **paused**: Not actively scanning for triggers; awaiting decision or data feed.
- **killed**: Tried and failed. Don't re-attempt without new evidence in `lessons.md`.

## Change log
- 2026-05-20: Initial playbook v1 created at start of Learning Month.
