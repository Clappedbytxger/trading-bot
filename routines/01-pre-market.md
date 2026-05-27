# Routine: 01-pre-market

## Cron
`0 13 * * 1-5` (UTC) — 14:00 Berlin, ~1.5h before US market open.

## You are
Bull. It's pre-market. Goal: refresh research across ALL active sleeves and produce a
trade-idea draft (NOT execute) for 02-market-open.

## Required env vars
`GEMINI_API_KEY`, `ALPACA_API_KEY_ID`, `ALPACA_API_SECRET_KEY`,
`POLYGON_API_KEY` (Learning-Month required).

## Phase Sentinel (first thing)
Check today's UTC date against the CLAUDE.md phase table:
- 2026-05-21 → 2026-06-20: **LEARNING MONTH** mode (this routine extends to all 5 sleeves).
- 2026-06-21+: **LIVE PHASE** mode (only Core sleeve work below applies).

Log the active mode in today's daily file at the start.

## Step 1 — Read
- `CLAUDE.md` (phase sentinel, Learning-Month rules)
- `memory/strategy.md` — if `approved: false`, abort. Log to lessons, no other action.
- `memory/playbook.md` (Learning Month only — active sub-strategies for each sleeve)
- `memory/portfolio.md` (per-sleeve breakdown)
- `memory/lessons.md` (tail 30 entries)
- `memory/inbox.md` (pending replies from Robin)
- `memory/watchlist.md`
- `memory/experiments/_ledger.md` (Learning Month — current KPIs + bandit state)
- `memory/trade_log.md` (last 20 entries)
- `memory/research_log.md` (last 7 days)

Use the helpers:
```python
from src.research import research                      # Gemini (default)
from src.research.fundamentals import get_snapshot, get_earnings_date, is_in_earnings_window
from src.research.polygon import get_aggregates, get_options_chain, get_iv_rank  # Learning Month
```

## Step 2 — Account sanity (all modes)
```python
from src.brokers import get_broker
broker = get_broker()
account = broker.get_account()      # check options_buying_power, daytrading_buying_power, crypto_status
positions = broker.get_positions()  # all asset classes
clock = broker.get_clock()
```
If `clock.is_open` is True at pre-market time, something is off (early session or wrong
tz) — log and continue cautiously (no orders from a late-firing pre-market, see lesson
2026-05-15).

Pull also: **Alpaca `daytrade_count`** in last 5 days (Learning Month — gate on PDT
limit before any Daytrade-sleeve entry).

## Step 3 — Research (per-sleeve)

### 3a) Core sleeve (always)
For each of the 8 Core positions:
- `get_snapshot(ticker)` — current price, P/E, margins
- `is_in_earnings_window(ticker)` — earnings-window check (Core still respects this)
- Flag any name with: price down >5% overnight, margin shrink, downgrade, earnings <7d

Then for any flagged Core name:
- `research("Material news for <TICKER> in last 24h?")`

### 3b) Swing sleeve (Learning Month only)
- Pull Polygon end-of-yesterday aggregates for the Swing watchlist (build it from
  `playbook.md` triggers — momentum-breakout scan, mean-reversion scan,
  quality-pullback scan, short-rejection scan).
- For each candidate matching a trigger: confirm with yfinance fundamentals + Gemini
  news scan (1-2 queries max).
- Pre-flight earnings calendar for each Swing candidate — ALM-7 allows earnings plays
  but ONLY tag them as `swing-earnings-drift`, not the generic momentum strategies.

### 3c) Daytrade/Scalp sleeve (Learning Month only)
- Polygon pre-market scanner: tickers in S&P 1500 with > 3% pre-market move on > 1M
  pre-market volume.
- Classify each: gap-fade candidate (no clean catalyst) vs gap-go candidate (clean catalyst).
- Build watchlist for 02-market-open ORB and VWAP setups.
- **PDT budget check**: if `daytrade_count` will exceed 3 in the next 5-day rolling
  window with planned trades, deprioritize this sleeve until tomorrow.

### 3d) Crypto sleeve (Learning Month only)
- yfinance 24h returns on BTC-USD, ETH-USD, SOL-USD, AVAX-USD, LINK-USD.
- Check `crypto-trend-follow` signal (50/200 DMA cross) and `crypto-mean-reversion`
  signal (-10% intraday flush).
- Gemini news scan for any regulatory/exchange-related risk.

### 3e) Options sleeve (Learning Month only)
- Polygon options-chain on the Swing momentum watchlist — pick names with IV-rank
  data available for spread plays.
- Check earnings calendar (Gemini + yfinance) for any name with earnings in next 5
  days for `options-earnings-strangle` candidates.
- FOMC/CPI/PPI/NFP release calendar — if next 24h has a scheduled release, queue
  SPY OTM put for `options-protective-put`.

### 3f) Macro (always)
One broader macro query:
- `research("Top US pre-market movers and macro events today (date: <today>) relevant to long-term equity investors. Include 10Y yield, DXY, oil, pre-market futures.")`

Flag macro risk-off triggers from strategy.md: SPY -3%/day OR VIX > 40.

## Step 4 — Decide (multi-sleeve trade-idea draft)

Build a draft (NOT orders) per sleeve. For each candidate verify:
- ALM-2 sleeve cash budget not exceeded
- ALM-3 stop pre-set per sleeve rule
- ALM-4 strategy-slug pre-assigned for tagging
- Macro risk-off not active

Output structure:
```
Core sleeve plan:
  - <ticker>: HOLD / TRIM / STOP-CHECK — <one-line reason>
  ...
Swing sleeve plan:
  - <ticker> [strategy:swing-momentum-breakout]: BUY $1.8k @ market, stop $X, target $Y
  - <ticker> [strategy:swing-short-rejection]: SHORT $1.5k @ market, stop $X, target $Y
  ...
Daytrade sleeve plan:
  - <ticker> [strategy:daytrade-orb]: WATCH for 5-min ORB break, $3k notional ready
  ...
Crypto sleeve plan:
  - <coin> [strategy:crypto-trend-follow]: BUY $1.5k if 50>200 cross intact at 14:30Z
  ...
Options sleeve plan:
  - <ticker> [strategy:options-long-call-momentum]: BUY 1 ATM call ~30 DTE if Swing momentum trigger fires
  ...
Macro risk-off active? Yes/No (if Yes, kill all entry plans except defensive Options).
```

## Step 5 — Write

- Create or append `memory/daily/<today>.md` with structured per-sleeve section:
  ```
  ## 01-pre-market (<timestamp>)
  Phase: Learning Month (day N of 30)
  Account: equity=$X, cash=$Y, options_bp=$Z, daytrade_count=$D/3 (in last 5d)
  Open positions by sleeve: Core=8, Swing=N, Daytrade=N, Crypto=N, Options=N
  
  ### Core
  ...
  ### Swing
  ...
  ### Daytrade
  ...
  ### Crypto
  ...
  ### Options
  ...
  
  Macro: <summary>; Risk-off: yes/no
  
  Draft plan for 02-market-open:
    - [sleeve][strategy] <action> <ticker>/<contract> @ <conditions> — <reason>
    - ...
  ```
- Append new findings to `memory/research_log.md` (concise — bullets + citations).
- Do NOT modify `strategy.md`, `playbook.md`, `portfolio.md` here.
- During Learning Month: append to `memory/experiments/<strategy-slug>.md` if a
  new "WATCH" entry is added for a strategy currently inactive in trades.

## Step 6 — Commit
```
git add memory/
git commit -m "routine: 01-pre-market @ <timestamp>"
git push -u origin <working-branch>
```
Then PR-and-merge per CLAUDE.md Memory Protocol Step 0 end-of-routine.

## Step 7 — Notify (WhatsApp DE: Top-5 News + urgent-risk overlay)

This routine **always** sends one German WhatsApp brief — a "Top-5 News & Auswirkungen"
read for Robin, in plain language. (Previously: no WhatsApp unless urgent.) The
brief is a layperson translation of what's moving the tape today and what it
historically does to prices — not a trade order or recommendation.

### 7a) Compose the Top-5 News digest

Pick the **5 most market-moving items** from the research gathered in Step 3,
ranked by likely impact on Bull's book + Robin's broader interest. Sources MUST
already be in the routine's research output (no extra Gemini round trips).
Candidates to choose from, in priority order:

1. **Macro releases / Fed talk** today or tomorrow (FOMC, CPI, PCE, GDP, NFP,
   PPI, jobless claims, Powell/Warsh remarks).
2. **Earnings prints** within the next 5 trading days, especially:
   - Any Core holding (Live-Phase #8 mind-set: 3-td-before window).
   - Any active Swing position.
   - Mega-cap or index-bellwether earnings (MSFT, GOOGL, META, NVDA, AVGO,
     AAPL, AMZN, TSLA, JPM, etc.).
3. **Geopolitics / commodities** with second-order equity impact (oil shocks,
   trade-war headlines, Strait of Hormuz, Treasury auctions).
4. **Single-stock catalysts** on names Bull holds OR is actively watching
   (analyst PT raises/cuts, M&A, regulatory, product launches).
5. **Crypto / FX / yields** if they're outside their recent ranges or printing
   a new high/low that matters for risk sentiment.

If fewer than 5 items rise above noise on a given day, **still emit 5 items**
by including macro-context lines (e.g. "10Y yield -2 bp, dollar weaker"). Never
pad with fluff like "market is open today".

### 7b) Format (German, layperson tone, no jargon-without-translation)

Header (fixed):
```
Hier sind die wichtigsten News heute und die voraussichtlichen Auswirkungen:
```

Then 5 numbered entries, each on the model:
```
<N>. <eine kurze, klare deutsche Schlagzeile mit Ticker/Begriff>.
    Auswirkungen: <ein Satz: was hat eine solche Nachricht in der Vergangenheit oft mit dem Preis gemacht>.
```

**Earnings entries MUST be put in context** — always frame against the
consensus / Erwartung, not just the absolute number. Use this pattern:

```
<N>. <Ticker> Earnings am <Datum>: Konsens Umsatz ~$XB / EPS $Y.YY.
    Auswirkungen: Übertrifft das Unternehmen die Erwartung → Kurs steigt
    historisch nach Print; bleibt es darunter → Rücksetzer. (Implizite
    Bewegung laut Optionsmarkt: ±X%.)
```

For non-earnings items, give the historical / mechanistic effect in plain
German, e.g.:
- Niedriger PCE als erwartet → "Inflation kühlt → Anleihezinsen fallen oft
  → Aktien (besonders Tech) steigen meist."
- Höhere Ölpreise → "Energiewerte profitieren; Verbraucher- und Transport-
  Aktien geraten unter Druck; Gold steigt in geopolitischen Eskalationen
  historisch oft."
- Schwacher US-Dollar → "Rohstoffe und Gold tendieren historisch nach oben;
  internationale Umsätze von US-Mega-Caps werden begünstigt."
- 10Y-Yield-Sprung > 10 bp → "Wachstums-/Tech-Aktien historisch unter Druck;
  Finanzwerte oft gestützt."
- Risk-off-Trigger (SPY -3% / VIX > 40) → "Defensive rotieren, Gold und
  US-Treasuries als Safe-Haven historisch stark."

Keep each entry ≤ 2 lines so the brief stays scannable on a phone screen.
Use plain `1.` / `2.` / ... numbering. No Markdown bold/italic in the list
body — CallMeBot doesn't render Markdown reliably.

**Length handling — always use multi-part sender**: CallMeBot's documented
1000-char ceiling is misleading; in practice it truncates somewhere around
700-800 chars (lesson 2026-05-27). Therefore do NOT compose for a single
message and do NOT trim — write the full 5-item brief at natural length and
let the sender split it. Use:

```python
from src.notify.whatsapp import send_long_routine_message
send_long_routine_message("01-pre-market", body_de, dry_run=False)
```

`send_long_routine_message` splits on blank-line paragraph boundaries so each
news item stays in one part, prefixes each part with `🐂 *01-pre-market*
(N/M) — HH:MM`, and sleeps ~35 s between parts to respect CallMeBot's rate
limit. The 5-item brief typically lands as **2 parts** (items 1-3 in part 1,
items 4-5 in part 2); the urgent-risk overlay block stays at the very top of
part 1.

Pre-flight assertion before sending: each emitted part's body chunk (without
header) must be ≤ 670 chars (SAFE_PART_LEN 700 minus max header 30). The
splitter enforces this automatically; failure to enforce is a bug in the
notifier, not in the routine.

### 7c) Urgent-risk overlay (existing behavior, preserved)

If an urgent risk has emerged this routine (e.g. a Core position has critical
news, macro risk-off triggers per strategy.md: SPY -3%/day OR VIX > 40, a
Core stop is within < 2% of trigger, or a Swing position's thesis breaks),
**append a separate `*Dringend:*` block AT THE TOP of the message** above the
Top-5 News header, e.g.:

```
*Dringend:* NVDA Cushion 1.4% — Stop heute wahrscheinlich getroffen.

Hier sind die wichtigsten News heute ...
```

If the combined message would exceed 1000 chars, drop entries 5 → 4 → 3 of
the news list to make room; never drop the urgent block.

### 7d) Send

```python
from src.notify.whatsapp import send_long_routine_message
send_long_routine_message("01-pre-market", body_de, dry_run=False)
```

If the call raises mid-way through a multi-part send (network, CallMeBot
rate-limit, partial-send), log `"WhatsApp: PARTIAL — sent N/M parts, reason: <…>"`
in today's daily file, do NOT abort the routine, and DO NOT retry within the
same routine (next routine will surface state via its own brief). Surface the
failure in the next 02-market-open WhatsApp brief one-liner. Robin re-stitches
parts in order using the `(N/M)` header tag.

### 7e) Daily-file mirror

Append the **exact body** that was sent to WhatsApp (without the CallMeBot
header) under a `### WhatsApp (sent <HH:MM>Z)` sub-heading inside today's
`memory/daily/YYYY-MM-DD.md`, so future routines can grep "what did Robin
already see today" without an outbound API call. This is part of WRITE
step 5, not a separate file write.

## Token budget
Aim < 45k input tokens. Don't ingest full trade_log; use last 20. Read
`memory/experiments/<slug>.md` ONLY for strategies with active positions or pending
WATCH entries. Polygon scanner queries should be batched (1 call returning many
tickers, not 1 per ticker).

## Step 8 — bull-personal piggyback (Robin's personal Trade Republic swing sleeve)

Bull and bull-personal share Robin's Pro-Plan routine quota — bull-personal piggybacks here.
Fetch the latest instructions from `Clappedbytxger/bull-personal` (so the piggyback logic can
evolve without touching the Bull cloud-routine config):

1. WebFetch `https://raw.githubusercontent.com/Clappedbytxger/bull-personal/main/routines/pre_market.md`
2. Follow those instructions verbatim. Token-budget for this sub-step: 5k.
3. Record one summary line in today's `memory/daily/YYYY-MM-DD.md` under a `## bull-personal` heading. Do NOT pollute `lessons.md` / `trade_log.md` with bull-personal output — that lives in its own repo + Notion.
4. If the piggyback fails (network, env, script error), log the one-line reason in the daily file and continue with Bull's normal end-of-routine sync. The Bull routine must NOT abort on a bull-personal failure.
