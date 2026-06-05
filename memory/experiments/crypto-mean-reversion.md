# Experiment Log — `crypto-mean-reversion`

Sleeve: Crypto. Status: active. Playbook reference: `memory/playbook.md`.

**Thesis (one line):** Crypto -10% intraday flushes often bounce ≥5% within 24-48h on
quality coins; long-only via Alpaca-native crypto trading.

---

## 2026-06-05 — Triggers FIRED (ETH + AVAX); queued for 03-midday execution

- **Routine**: 01-pre-market 15:39Z LATE FIRE.
- **Late-fire constraint**: Per lesson 2026-05-15, 01 firing post-open is research+draft
  only. Crypto entries cannot be authorized from this routine. **Queue for 03-midday
  at 17:30Z** (crypto trades 24/7; 03-midday will fire normally).

### Trigger scan (Fri 6/5 ~15:39Z yfinance close-vs-prev-close)

| Coin | 24h % | 7d % | Trigger fired? |
|------|------:|-----:|----------------|
| BTC-USD | -5.70% | -18.00% | NO (approaching but >-10%) |
| **ETH-USD** | **-10.87%** | -21.61% | **✓ TRIGGER (-10.87% < -10%)** |
| SOL-USD | -6.87% | -21.89% | NO |
| **AVAX-USD** | **-10.38%** | -21.85% | **✓ TRIGGER (-10.38% < -10%)** |
| LINK-USD | -9.11% | -19.34% | NO (close to trigger) |

### Catalyst classification (NOT a fundamental break)

- **Macro driver**: NFP May +172k vs +85k cons (hawkish surprise) → 10Y +6bp → DXY +0.49%
  → systemic risk-off across crypto cohort. Futures repricing 65% Fed-hike-by-Dec (up
  from 48%).
- **Not an exchange collapse**: no Coinbase / Binance / FTX-style trigger event; no
  protocol exploit; no stablecoin de-peg. Per playbook spec: passes the "no fundamental
  break" filter.
- **Crypto-flow correlation**: all 5 universe names down -5% to -11% in 24h; correlated
  selling = flow, not idiosyncratic news.

### Queued entry plan for 03-midday 17:30Z

#### ETH-USD `crypto-mean-reversion`

- **Entry**: BUY $1,500 notional @ market.
- **Expected quantity at $1,577.18 mark**: 0.95108 ETH (approximate; market fill TBD).
- **Stop**: -5% from entry (-5% trail GTC).
- **Target**: +5% bounce from entry (target ~$1,656).
- **Time stop**: 48 hours from fill = Sun 6/7 ~17:30Z.
- **Expected R**: 1R (target +5% / stop -5%).
- **Risk**: $75 (5% of $1,500); within $5k Crypto sleeve cap; well within $2k/coin cap.
- **Sleeve attribution**: Crypto sleeve $1,500 of $5,000 budget.

#### AVAX-USD `crypto-mean-reversion`

- **Entry**: BUY $1,500 notional @ market.
- **Expected quantity at $6.89 mark**: ~217.7 AVAX.
- **Stop**: -5% from entry (-5% trail GTC).
- **Target**: +5% bounce from entry (target ~$7.23).
- **Time stop**: 48 hours from fill = Sun 6/7 ~17:30Z.
- **Expected R**: 1R (target +5% / stop -5%).
- **Risk**: $75 (5% of $1,500); within $5k Crypto sleeve cap; well within $2k/coin cap.
- **Sleeve attribution**: Crypto sleeve $1,500 of $5,000 budget.

### Combined Crypto sleeve commitment after fills

- **Used**: $3,000 (60% of $5k budget).
- **Open positions**: 2 / 4 (cap).
- **Remaining cash budget**: $2,000.
- **ALM-2 cap check**: ✓ $2k/coin not exceeded (sized $1.5k each).
- **ALM-3 stop check**: ✓ -5% trail per playbook (tighter than the default -8% trend-follow).
- **ALM-4 strategy tag**: ✓ `crypto-mean-reversion` pre-assigned.

### Risk-off override interaction

- Macro risk-off override threshold: SPY -3% OR VIX > 40. Fri intraday: SPY -1.37%,
  VIX 16.63. **NOT triggered**. Crypto entries are NOT blocked by macro-defensive mode.
- If SPY-decline extends to -3% intraday by 04-pre-close: strategy.md says "Crypto:
  tighten trail to -5%" — already at -5% per mean-reversion spec, so no further action
  needed.

### Outcome (TBD — to be filled in post-exit per entry)

- ETH-USD: Exit date / price / R / P&L / lesson:
- AVAX-USD: Exit date / price / R / P&L / lesson:
