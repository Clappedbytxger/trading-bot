# Research Log

Synthesized findings from Gemini (default) and Tavily (deep_research only), plus
numerical snapshots from yfinance. One entry per significant research session. Older
entries (> 30 days) can be pruned by the weekly-review routine.

---

## 2026-05-26 — Pre-market (LM Day 6 of 30, Tue, first session post-Memorial Day)

**Macro (Gemini, 12:21Z):**
- **10Y yield 4.49%** (-12bp vs Fri 5/22 4.61%); bond rally on Middle-East
  de-escalation talks (US-Iran deal optimism). Pre-Tue dovish drift continues.
- **DXY 99.03** (-0.21% / -35bp vs 5/22 99.38). Risk-on currency tape.
- **Brent $97.9** (+1.8%), **WTI $91.33** (-5.18%). Diverging crude on
  Strait-of-Hormuz reopening expectation.
- **Pre-market futures GREEN**: S&P +0.68%, Nasdaq +0.7%, Dow +0.59%.
  Pre-open SPY gap implied < 1% → ORB rule guard satisfied.
- **VIX 16.85** (vs 5/22 16.82; futures +1.29% pre-open). No risk-off.
- **PCE + Q1-GDP-2nd-estimate** confirmed Thu 5/28 13:30Z — only material
  scheduled release in next 5td. No FOMC/CPI/PPI/NFP.

**NVDA post-earnings update (Gemini):**
- **BofA PT $350 (from $320)** 5/22 post-print; **UBS PT $280** (from $275)
  5/21; KeyBanc/MS/DA Davidson/Truist/Jefferies/JPM/Benchmark/Rosenblatt/
  Needham/MS all maintained ratings or raised PTs 5/21-22.
- **Vera CPU launch** announced 5/26: "up to 1.5× faster than alternatives",
  $200B agentic-AI-CPU TAM (includes China per Jensen 5/25), $20B CPU
  revenue projected current FY.
- Q1 FY27 print 5/20: revenue **$81.6B** (vs $78-80B consensus / whispers),
  +85% YoY; DC **$75.2B** / +92% YoY; **$80B fresh buyback authorization**;
  dividend +25% to $0.25 quarterly. Hyperscale rev +115% to $37.9B.
- Counter-take: **Michael Burry 5/26 cautions** "temporary AI demand" +
  hyperscaler debt-funded capex concentration. Logged as bear input; no
  thesis-break trigger.
- **Bull stance**: `swing-quality-pullback` thesis intact and strengthened.
  Position NVDA $2k @ $219.96 from 5/22 → pre-mkt cushion 4.235% (vs 2.96%
  Mon EOD). Tighten-to-breakeven trigger ≥ +5% UPL = ≈ $230.96 mark.

**RL post-earnings update (Gemini):**
- FY26 revenue **> $8B** (+15% YoY); 6.5M new DTC customers.
- Post-print PT raises 5/22: **UBS $511** (from $480), **Barclays $439**
  (from $430), **Wells $415** (from $400). All OW.
- "Next Great Chapter: Drive" strategy showing positive results.
- **Bull stance**: `swing-earnings-drift` PEAD thesis reinforced. Position
  RL $1.5k @ $377.03 from 5/22 → pre-mkt cushion ~7.7% (UPL +1.31%).
  Tighten-to-breakeven trigger ≥ +5% UPL ≈ $395.88 mark.

**AVGO into 6/3 earnings (Gemini):**
- **Citi top-semi pick 2026** (Atif Malik $500 PT from $475, 5/12 ahead of
  print). AI rev +106% YoY to $8.4B (Q1 FY26).
- Partnerships 5/19-22: LSEG 5y VMware Cloud Foundation 9; $125M
  semiconductor hub at UCLA w/ Meta, Applied, GlobalFoundries, Synopsys;
  joins Applied EPIC platform for advanced chip packaging.
- No pre-announcement / Apple-chip news in last 24h.
- **Bull stance**: AVGO Core position FROZEN (Live-Phase #8 PAUSED but
  Core sleeve is in LM-freeze regardless). No Core-add. Earnings-strangle
  candidate via Options sleeve BLOCKED on Polygon chain (5th re-test
  pending Wed 5/27).

**Other tickers checked:**
- AAPL: no specific 24h catalyst. 5/22 daily was UP candle ($306.12 →
  $308.82) with fresh 52w-Hi $311.40 → no `swing-short-rejection` trigger.
  WATCH today.
- ARM: no specific 24h catalyst. 5/22 daily $290.07 open / $315.00 H /
  $306.51 C → wide 8.6% range; close in $290-$310 WATCH band per Mon spec
  ("re-arm only if ARM closes back below $290; above $290 + below $310
  stays WATCH"). No `swing-momentum-breakout` trigger (close < $310). WATCH.

**Polygon operational status (recurring blocker):**
- **`get_market_movers` (snapshot/locale/us/markets/stocks/gainers|losers)**:
  **403 Forbidden** (tier gate; same as LM Days 1-5).
- **Stock snapshot (snapshot/locale/us/markets/stocks/tickers/NVDA)**:
  **403 Forbidden** (tier gate).
- **Options chain (v3/snapshot/options/NVDA)**: **403 Forbidden** (5th
  re-test; tier gate persists).
- Daily aggregates (v2/aggs/ticker/{sym}/range/...): **works** but rate-
  limited at ~5 calls/min on free tier (got NVDA/AAPL/ARM/SPY cleanly,
  429'd on QQQ/AVGO/RL).
- **Operational impact**: Daytrade gap-scan + Options-strangle / protective-
  put strategies require chain/snapshot access; remain effectively gated
  pending Polygon-tier upgrade.

**Crypto universe (yfinance, 12:20Z):**
- BTC-USD $77,000.88 (24h -0.36%, 7d +0.33%); 50DMA $77,100 / 200DMA $80,274;
  gap **-3.95%** (+0.36pp convergence overnight vs Mon 19:37Z -4.31%
  stall).
- ETH $2,116.40, gap -10.65% (+0.24pp); SOL $85.05, gap -18.60% (+0.38pp);
  AVAX $9.37, gap -15.22% (+0.39pp); LINK $9.56, gap -12.24% (+0.39pp).
- 5/5 50<200; 0 cross-up. 0/5 24h flush > -10% (largest 24h: BTC -0.36%,
  wrong direction). `crypto-weekend-momentum` closed (Fri trigger NOT met).
- **0 crypto entries.**

**Bull's account snapshot (Alpaca paper, 12:20Z)**:
- Equity $101,242.86 (+$381.65 vs Mon close on overnight re-quote).
- Cash $34,500.00, Long MV $66,742.86, Options BP $67,871.43 / L3.
- DT count 0/5d; PDT False; Crypto ACTIVE; multiplier 2x.
- All 10 GTC stops `OrderStatus.NEW`.
- Notable pre-mkt: VOO +0.69%, LLY +1.06% (new HWM imminent), NVDA-Swing
  +1.33% (cushion to 4.235%), RL-Swing +1.11% (UPL flips to +1.31%).
  V -0.24% only red Core name pre-mkt.

**No thesis-break events. NVDA + RL Swing positions both materially
healthier pre-mkt vs Mon EOD. Macro tape supportive. Risk-off: NO. Bias
remains "no action unless spec-trigger fires" — likely outcome at 02-
market-open is HOLD across the book with potential AAPL short-rejection
watch + ARM momentum re-arm contingent on intraday tape.**

**Cited sources:** Gemini Search-Grounding (10Y/DXY/oil, futures, VIX,
PCE+GDP calendar, NVDA post-print PT changes + Vera CPU, RL FY26 + PT
raises, AVGO Citi PT + partnerships, Burry counter-take). yfinance for
fundamentals + crypto daily. Polygon for NVDA/AAPL/ARM/SPY daily
aggregates. Alpaca for broker account + pre-mkt position marks. See
`memory/daily/2026-05-26.md` for portfolio + draft plan.

---

## 2026-05-25 — Pre-market (LM Day 5 of 30, Mon US Memorial Day, cash CLOSED)

**Macro (Gemini, post-weekend pre-flight for Tue 5/26 reopen):**
- S&P 500 futures (ES) +0.35-0.92% on holiday-shortened tape; Nasdaq 100
  futures +0.42-1.36%. Equity-positive overnight.
- 10Y Treasury yield 4.51% (eased from 4.56% Fri 5/22). Dovish drift.
- DXY ~99.0 (-0.27%); USD softness on risk-on sentiment.
- WTI crude $90.65 (-4.7%) on US-Iran peace-agreement optimism;
  disinflationary impulse.
- Risk sentiment improved on geopolitical hopes.
- VIX 16.65 (vs Fri 16.70); no -3% SPY signal; SPY +0.39% Fri close
  (week +0.88%).
- Scheduled releases next 5 td: **Thu 2026-05-28 13:30Z = April PCE +
  Q1 GDP 2nd estimate** (only major release in the window; next CPI 6/10,
  PPI 6/11, FOMC minutes 7/8). May U Mich consumer sentiment revised
  LOWER to record low Fri 5/22.
- Earnings this week (none in Bull's book): CRM, SNOW, MRVL, DELL, HP.

**Per-position weekend news scan (Gemini):**
- **NVDA**: zero new material weekend news beyond the 5/20 print recap
  (already captured). Analyst median PT $275 (range $180-$400); Baird
  $500 (high). Vera CPU shipments to OpenAI/Anthropic/SpaceXAI/Oracle
  confirmed. CEO Huang "parabolic AI demand" at Dell World 5/19. NVDA at
  TD Cowen Tech Conf 5/28 + BofA Global Tech 6/4 — both upside catalyst
  candidates within the swing-hold window.
- **RL**: weekend analyst re-rating flow on the 5/21 print: JPM/Barclays/
  UBS/DB maintained BUY 5/23; UBS PT $511 raised 5/22, Needham $400→$405.
  FY27 guide mid-single-digit rev growth. Strong reinforcement of the
  Day-3 PEAD thesis on the open RL position.
- **AVGO**: Citi PT $475→$500 (5/12 catch-up), UBS $475→$490 (5/19),
  Goldman bullish on AI-infra. AVGO earnings 2026-06-03 = 6 td out from
  Tue 5/26 (outside the 3-td earnings exclusion window for new entries,
  but Core is frozen anyway during LM).
- **MSFT, GOOGL, META, V, BRK.B, LLY, VOO**: no material weekend news
  flagged.

**Crypto (yfinance, Mon 12:11Z 24h close):**
- BTC $77,247.33 +0.35% 24h, +0.38% 7d, 50/200 gap **-4.31%** (narrowed
  from -4.67% Sun; weekend convergence continues at ~0.36 pp/day pace).
- ETH $2,111.57 +0.65% / -0.80% / -10.89% gap.
- SOL $85.72 +0.55% / +0.50% / -18.98% gap.
- AVAX $9.37 +1.77% / +1.47% / -15.61% gap.
- LINK $9.52 +1.01% / -0.72% / **-12.63%** gap; 50-DMA $9.51 vs 200-DMA
  $9.50 — on the cusp but not a clean cross (within noise).
- `crypto-trend-follow` decision: **HOLD scan** — BTC convergence
  continues but no cross-up yet; LINK in noise-cusp watch. Next scan at
  Tue 03-midday.

**Plays this enables (Tue 5/26 draft only — no execution today, market
closed)**:
- Tue 02-market-open: full Account state re-pull + 10 GTC stop verification.
- Polygon options-chain **4th re-test** at Tue 01-pre-market.
- If chain unblocks AND PCE+GDP confirmed Thu 5/28 13:30Z: **2 SPY OTM
  protective puts** (~5% OTM, ~30 DTE, $1k total premium) per
  `options-protective-put` playbook spec (1 put per $30k Core equity).
- Swing screens: re-scan momentum-breakout / mean-reversion / quality-
  pullback / short-rejection / short-fundamental; AAPL re-watch; ARM
  re-arm if <$290.
- Daytrade: PDT budget full 5/5; post-holiday lighter-vol → tighten ORB
  filter to 1.7x avg-vol.
- Crypto: LINK 50/200 cusp watch + BTC continued convergence monitor.

---

## 2026-05-22 — Pre-market (LM Day 2 of 30, Fri KW 21 day 5)

**Macro (Gemini):**
- 10Y Treasury yield 4.56% (-1bp); DXY 99.36 (+0.10%, 6-week high consolidating).
- Oil: WTI $98.08 +1.8%, Brent $104.96 +2.3% on US-Iran tension / Strait of
  Hormuz supply-disruption concerns.
- Pre-market futures: ES +0.17% at 7,479; NQ +0.14% at 29,490; RTY +0.07%.
  Light calendar; primary scheduled releases: U-Mich final sentiment +
  inflation expectations (10 ET = 14Z), BLS State Employment April (10 ET).
- Fed: Waller lecture Frankfurt 10 ET; **Warsh sworn in as Fed Chair 11 ET**
  (~15Z) — watch for unexpected commentary post-ceremony.
- Notable overnight earnings/movers: NVDA flat AH (priced-in blow-out), TTWO +
  (GTA VI launch reaffirmed), WDAY + (Q1 beat + guide raise), RL +10.26% Thu
  (Q4 beat / strong full-price selling), WMT mixed (EPS beat / weak guide),
  Ross beat. **No FOMC/CPI/PPI/NFP today** → no tier-1 macro-catalyst day.

**NVDA Q1 FY27 post-earnings recap (Gemini):**
- Revenue $81.6B (+85% YoY, +20% QoQ) vs consensus $78.8-79.1B. Non-GAAP EPS
  $1.87 vs Street $1.75-1.77. GAAP EPS $2.39.
- **Q2 guidance $91B ±2% vs Street $86-87B** (huge raise; ex-China Data Center).
- Data Center rev $75.2B +92% YoY. Hyperscale specifically $37.9B +115% YoY.
  Now ~50/50 split hyperscalers vs ACIE (AI Clouds/Industrial/Enterprise/
  Sovereign), broadening customer base.
- Analyst PT raises within 24h: HSBC $295→$325, MS $260→$285, Jefferies
  $275→$300, Baird $300→$500, BofA $320→$350, GS $250→$285.
- Day-1 reaction (Thu 5/21): close $219.51, -1.77% on the session ("priced in"
  reaction, not thesis break). Intraday high $227.40, low $217.93 (vol 202M).
- Risks Wall Street flags: (1) valuation elevated, (2) China exclusion in Q2
  guide, (3) supply commitments balance up to $119B (memory cost edge could
  fade post-FY27).
- **Plays it enables (per playbook)**: `swing-quality-pullback` (top-pick), and
  `options-vertical-bull-call-spread` aligned with the same thesis.

**INTU thesis-risk scan (Gemini):**
- -20% Thu drop driven by (1) 17% workforce cut announcement (~3,000 layoffs,
  $300-340M restructuring charges), (2) lowered FY26 TurboTax revenue
  projections citing AI-driven competition, (3) preliminary FY27 guidance
  (revG 11-12%, non-GAAP EPS growth $3.56-3.62 — provided, not cut against
  prior outlook), (4) multiple analyst PT cuts overnight.
- Decision: `swing-mean-reversion` quant signal fires (z20 -2σ, RSI <25) but
  the qualitative "AI-disruption + restructuring" thesis-risk overlay
  disqualifies the playbook's "quality name that pulls back" precondition.
  **SKIPPED for today's plan.** Re-evaluate once INTU reclaims 5-DMA OR
  analyst PT actions stabilize.

**ARM catalyst scan (Gemini):**
- +16% Thu rally to $298.23 on (1) Bernstein upgrade to Outperform $300 PT
  citing AI data-center demand, (2) read-through from NVDA Q1 print —
  Vera CPU "$20B forecast" with material Arm royalty exposure, (3) prior Q4
  FY26 earnings beat (5/6/2026) provided underlying positive sentiment.
- Decision: `swing-momentum-breakout` quant signal fires but the +30% 5d
  context calls for confirmation entry not chase. WATCH for 13:30-14:00Z
  consolidation above $290 + 5-min ORB-break before entry. Reject any
  $310+ gap-up open.

**Polygon connectivity (Day 2 first-use, LM):**
- POLYGON_API_KEY confirmed SET (was unset on Day 1). Stock daily aggregates
  (NVDA, SPY, QQQ, TLT) returned successfully; pulled 5-day bars 5/15-5/21.
- Rate-limit: free-tier 5/min — hit a 429 burst when querying 11 tickers in
  one tight loop; spaced subsequent calls. Implication: pre-market scanners
  must batch via the snapshot endpoint, not per-ticker aggregates.
- VIX endpoint returned 0 bars (Polygon doesn't supply on this tier).
- BTC-USD/ETH-USD/SOL-USD/AVAX-USD/LINK-USD returned 429 in the same burst;
  fell back to yfinance for daily-resolution crypto returns + DMA calc.
- `get_iv_rank` returned None for NVDA / ARM / RL → options-chain endpoint
  appears NOT enabled on the current Polygon tier (Options-Starter add-on
  required per playbook). **DATA GAP** for `options-earnings-strangle`,
  `options-long-call-momentum`, `options-vertical-bull-call-spread` until
  resolved. NVDA conviction routes through equity sleeve as the
  primary play; options spread is on WATCH not BUY.

**Crypto state (yfinance):**
- BTC $77,422 / 7d -2.08% (vs trigger +2% for `crypto-weekend-momentum`)
- ETH $2,132 / 7d -4.10% — weakest momentum in universe
- SOL $87.48 / 7d -1.93%; AVAX $9.52 / 7d -0.18%; LINK $9.90 / 7d -1.65%
- All 5 names 50-DMA < 200-DMA → `crypto-trend-follow` no cross-up signal.
  No -10% intraday flushes → `crypto-mean-reversion` no signal.
- Re-check 03-midday + 05-close-summary 21Z for weekend-momentum BTC weekly +2%.

**Cited sources:** Gemini Search-Grounding (Investing.com / TIKR / MarketBeat
/ Seeking Alpha for INTU; Motley Fool / Seeking Alpha / KoalaGains for ARM;
multi-source consensus for NVDA Q1 FY27; standard macro sources for
10Y/DXY/oil/futures and U-Mich/State Employment/Fed schedule). yfinance for
quant + earnings dates. Polygon for stock daily aggregates. Alpaca broker
for pre-mkt position marks + account sanity. See `memory/daily/2026-05-22.md`
for portfolio detail + per-sleeve plan draft.

---

## 2026-05-12 — Initial pre-market research, all 9 strategy positions

**Macro (Gemini):**
- US April CPI: +3.8% YoY (vs 3.7% est). Gas-price driven, Strait-of-Hormuz / Iran tensions.
- Rate-cut odds 2026: ~60% probability of no cuts.
- Hyperscaler 2026 capex revised up to ~$750B (+67% YoY). Direct tailwind for NVDA/AVGO; double-edged for MSFT/META/GOOGL (capital intensity concern).
- Kevin Warsh Fed-Chair confirmation vote this week.

**MSFT (Gemini):** Drawdown −26% from 52w-Hi is sentiment-driven:
- TCI Fund Management nearly liquidated ~$8B stake (May 8) citing AI-disruption thesis against Office/Azure.
- DBS Bank cut PT on May 8.
- UK £2.8B cloud-licensing suit (April), ongoing CMA/FTC antitrust on cloud + AI.
- Fundamentals: fwd P/E 21.1 matches strategy spec; revG 18.3%; opM 46.3% — unchanged. **Strategy thesis intact, valuation now more attractive.**

**META (Gemini):** Drawdown −24% from 52w-Hi:
- Q1 2026 beat EPS + revenue, but raised AI capex guidance → capex-fear (echo of 2022).
- Lawsuits: Santa Clara scam-ad suit, Italy publisher copyright loss, federal copyright-AI training suit. Known regulatory headwinds.
- Fundamentals: fwd P/E 16.6; revG 33.1%; opM 40.6% — cheapest mega-cap relative to growth. **Strategy thesis intact, valuation more attractive.**

**NVDA (Gemini):** Earnings 2026-05-20 (Q1 FY27):
- Consensus: EPS $1.77, Rev $78.89B. Guidance ~$78B ±2% (73–80% YoY growth). Citi PT implies $80B.
- Jensen projected ≥$1T Blackwell + Vera Rubin orders through 2027.
- Risks: hyperscaler custom-silicon competition, China export-control exclusions, AI-capex digestion risk.
- Currently at 97.5% of 52w-Hi → strategy caveat triggers ("don't initiate full 7% on 52w-Hi day"). **WAIT.**

**Quant snapshots (yfinance):** See `memory/daily/2026-05-12.md` for full table.

**Cited sources:** Gemini Search-Grounding citations attached to each query (Yahoo Finance, Reuters, Bloomberg, Investor.com aggregations). Numbers cross-verified against yfinance for fwd P/E.

---

## 2026-05-13 — Pre-market: macro + NVDA preview + GOOGL sanity check

**Macro (Gemini):**
- **April PPI prints today 13:30Z / 08:30 ET.** Consensus: headline +0.5%, core +0.4%. Hot print would compound yesterday's hot CPI (+3.8% YoY) and amplify "no-2026-cuts" repricing.
- **Kevin Warsh full-chamber Senate confirmation vote today.** Powell's term ends 2026-05-15; Warsh expected sworn in same day. First remarks Mon 5/18 will set the rate-cut tape.
- Yesterday SPX -0.1%, Nasdaq -0.7%. Energy still the inflation driver (gasoline +28.4% YoY).
- Pre-market mixed: penny-stock movers dominate; mega-caps quiet.

**NVDA (Gemini):** Earnings Q1 FY27 confirmed 2026-05-20 (Wed) post-close.
- Citi forecast $80B revenue vs market consensus $78.6B; B300 line strength cited.
- Jensen Huang on Trump's China delegation this week — H200 export decision potentially imminent (bull if approved, bear if export tightening).
- New Illinois biometric privacy lawsuit (typical legal-flow noise, not a thesis hit).
- Board adds Suzanne Nora Johnson (5/8); strategic partnerships with IREN (5/7) and Corning (5/6) on AI infra/US manufacturing.
- StockInvest.us moved Strong-Buy → Buy (5/12) on technical weakness only — irrelevant to long-term thesis.
- Insider net selling $38.5M / 90d (zero exec sells); pattern matches post-vest cadence, not a signal.
- At **98.7% of 52w-Hi today** (vs 97.5% yesterday). Strategy caveat reinforced — **WAIT.**

**GOOGL (Gemini):** Yesterday's -0.40% close was pure noise; thesis strengthened, not weakened.
- Q1 2026 print blew the doors off: EPS **$5.11 vs $2.64 est**, revenue $109.9B vs $107.0B est.
- Cloud +63% YoY; Cloud RPO doubled sequentially to **$467.6B**; backlog nearly doubled.
- Quarterly dividend lifted $0.21 → $0.22.
- Google-backed Isomorphic Labs raised $2.1B (AI drug discovery).
- Alphabet preparing first-ever JPY bond issuance to fund AI infra.
- One Seeking Alpha "take some profit" piece (5/12) on stretched valuation — minority view, not a thesis-break.
- Quant: fwd P/E 26.78, op margin 36.1%, revG 21.8%, ROE ~39% — unchanged from yesterday.

**Quant deltas (yfinance) vs 5/12 pre-market:**
- NVDA $218.13 → $220.78 (+1.2%); Δhi -2.5% → -1.3% (deeper into 52w-high zone).
- AVGO $422.07 → $419.30 (-0.7%); GOOGL $385.94 → $387.35 (+0.4%); META $602.18 → $603.00 (+0.1%).
- MSFT $408.71 → $407.77 (-0.2%); V $324.95 → $326.42 (+0.5%); BRK-B $483.17 → $484.96 (+0.4%); LLY $983.70 → $989.87 (+0.6%); VOO $675.20 → $678.67 (+0.5%).
- No fundamentals shift (fwd P/E, op margin, revG, beta all within 1 decimal of 5/12). Thesis remains intact across the board.

**Cited sources:** Gemini Search-Grounding citations (Yahoo Finance, Reuters, Bloomberg, MarketWatch, Seeking Alpha, StockInvest.us). yfinance for quant.

---

## 2026-05-14 — Pre-market: hot PPI, Fed transition, NVDA-Culper short report

**Macro (Gemini):**
- **April PPI HOT**: headline +6.0% YoY, core +5.2% YoY — largest gain in 3+ years, beat expectations. Energy + transportation/warehousing (+12% YoY) the drivers. 10Y yield ~4.5%, 2Y to 4.0%. Boston Fed (Collins) hawkish; "no rush to cut."
- **Fed transition**: Powell's term ends **2026-05-15**; **Warsh sworn in 2026-05-16**. Warsh: hawkish but pro-"AI-fueled disinflation." Barclays since-1930 study: S&P avg drawdowns −5% / −12% / −16% at 1m / 3m / 6m post-new-chair. Market already paring rate-cut bets.
- **Today's 08:30 ET data**: Retail Sales (+0.5% nominal / +0.7% core est) + Weekly Jobless Claims (208k est). Import/Export Prices, Business Inventories (+0.3% est) at 10:00 ET.
- **Geopolitics**: Trump-Xi summit in Beijing today (Taiwan + trade); Brent ~$106/bbl on Strait-of-Hormuz disruption.

**NVDA (Gemini, earnings 5/20 post-close):**
- Consensus: rev $78.5–78.98B, EPS $1.75–1.78; data center ~$73.1B; GM ~75%. Prediction markets ~90% beat probability. Analysts: "perfection priced in."
- **Jensen Huang in China with Trump** today — potential H200 export decision catalyst (bull if eased / bear if tightened).
- **Analyst PT upgrades**: BofA $300 → $320 (2030 AI DC TAM raised to $1.7T); Susquehanna $250 → $275 (GB300 demand); RBC Outperform $250 reiterated.
- **Culper Research SHORT report** (NEW): alleges >20% of FY26 compute revenue still routed to China via illicit GPU diversion through SEA intermediaries, contra Nvidia's "effectively zero post-April-2025-restrictions" statements. Substance unverifiable pre-earnings; expected to add print-day volatility but unlikely thesis-breaking if specifics thin.
- Green Century ESG push for scope-3 emissions disclosure ahead of 2026 vote.
- At **99.1% of 52w-Hi** today (vs 98.7% on 5/13 / 97.5% on 5/12). Strategy caveat strongly binding; earnings window opens 5/15. **STILL WAIT.**

**Quant deltas (yfinance) vs 5/13 pre-market:**
- GOOGL $387.35 → **$402.62 (+3.9%)**; Δhi -3.6% → **-0.3%** (now at 99.7% of 52w-Hi). Q1-beat re-rating into day 3.
- META $603.00 → $616.63 (+2.3%); Δhi -24.3% → -22.6%.
- LLY $989.87 → $1015.75 (+2.6%); Δhi -12.7% → -10.4%.
- NVDA $220.78 → $225.83 (+2.3%); Δhi -1.3% → **-0.9%** (deeper into 52w-high zone).
- VOO $678.67 → $682.41 (+0.6%); SPY 737.10 → 742.31 (+0.7%).
- AVGO $419.30 → $416.79 (-0.6%); MSFT $407.77 → $405.21 (-0.6%); BRK-B $484.96 → $485.52 (+0.1%).
- V $326.42 → **$320.31 (-1.9%)**; the lone red name, on rising-rates rotation.
- No fundamentals shift (fwd P/E, op margin, revG, beta all within 1 decimal of 5/13). Thesis intact across the board.

**Cited sources:** Gemini Search-Grounding citations (Yahoo Finance, Reuters, Bloomberg, MarketWatch, Seeking Alpha, BLS PPI release, Culper Research disclosure). yfinance for quant.

---

## 2026-05-15 — Pre-market (LATE / post-open backfill at 13:48Z): Powell→Warsh, U-Mich record low

**Macro (Gemini, 1 grounded query):**
- **Powell's last day as Fed Chair.** Warsh sworn in Sat 2026-05-16; first FOMC chaired Jun 16-17. Powell stays on as governor (precedent-breaking).
- **U-Michigan May preliminary sentiment 48.2 — record low** (below ~52 prior). Yr-ahead inflation exp 4.5% (cool from 4.7%, still elevated). Hard-data prints today are net mixed:
  - Retail Sales +0.5% MoM (in line, consumer resilient).
  - Initial jobless claims **211k** (vs 208k est) — slight loosening at the margin.
- **10Y yield 4.57%** (+8 bp from yesterday's 4.49%); DXY 99.20 (5-week high); Brent $100-104/bbl, Iran-war premium unchanged.
- **Pre-market futures** Dow -0.67% / SPX -1.09% / NDX -1.58% → realized SPY -1.20% on the open. Tech/semis the worst sleeve.

**Quant deltas (yfinance) vs 5/14 pre-market:**
- VOO $682.41 → $679.72 (-0.39%); MSFT $405.21 → $414.45 (+2.28%); GOOGL $402.62 → $397.10 (-1.37%); META $616.63 → $611.29 (-0.87%); AVGO $416.79 → $427.13 (+2.48% on the day but -3.19% intraday off post-open peak); V $320.31 → $327.07 (+2.11%); BRK-B $485.52 → $485.16 (-0.07%); LLY $1015.75 → $1010.90 (-0.48%); NVDA $225.83 → $226.74 (+0.40%, dHi -0.9% → -4.14% because 52w-Hi printed at $236.54 in the meantime).
- **Fundamentals unchanged within 1 decimal across all 9** vs 5/14: fwd P/E, op margin, revG, beta all in line.
- **No earnings window on any held position** until AVGO 2026-06-03; tranche 3 clean of guardrail #8 whenever it unblocks.
- **NVDA in earnings window** (5/15 → 5/20); WAIT confirmed.

**Strategic read:**
- Soft data (U-Mich record-low sentiment) is the cleanest new input — bearish for cyclicals, neutral-to-positive for defensive quality. Validates Bull's defensive-ballast outperformance today (MSFT/V/LLY/BRK.B all green vs SPY -1.20%).
- Tape narrative: "Powell-last-day uncertainty + sticky inflation + softening consumer mood = higher-for-longer yields = AI sleeve pressure". Bull's 37.5% cash + 0.62-beta defensive sleeve continues to compress relative drawdown — alpha tightened +83 bp today.
- No thesis-break events on any of the 8 holdings; no entry triggers fired for new names.

**Cited sources:** Gemini Search-Grounding (U-Mich, BLS Retail Sales / Jobless Claims, Treasury yields, DXY). yfinance for quant. See `memory/daily/2026-05-15.md` for portfolio detail.

---

## 2026-05-18 — Pre-market (KW 21 start, Warsh-era Day 1)

**Macro (Gemini):**
- **Warsh Day 1 as Fed Chair.** Sworn in Sat 5/16 (Powell's term ended Fri 5/15). No public schedule for 5/18 announced; first FOMC he chairs is **June 16-17**. Senate confirmation 54-45 (most divisive in Fed history). Telegraphed stance: tighter inflation discipline, streamlined Fed communication, narrower mandate focus. Strategists model near-term policy continuity with Powell.
- **Powell-stays-as-governor dynamic** is a new wild card — two governors with different inflation tolerances could create FOMC-dot-plot dispersion through June.
- Gemini grounding did **not** return spot pre-market futures / 10Y / DXY / oil for 5/18 (flagged as too recent). Broker-side check punted to 02-market-open.

**NVDA pre-earnings preview (Gemini, earnings Wed 5/20 post-close):**
- Consensus: revenue ~$78B (Citi $80B, UBS models $81B), EPS ~$1.77 (range $1.69-1.99), data-center ~$73B, non-GAAP GM 74.5% (guidance 75% ±50 bp).
- **PT moves since 5/14**: BofA $320 (from $300), UBS $275 (from $245), Susquehanna $275 (from $250), RBC Outperform $250 reiterated, KeyBanc $300 (from $275). Net hawkish flow.
- **SK Hynix Q1 HBM sales to NVDA: +62.6% YoY** (KRW 7.78T) — bullish demand signal.
- **Jensen Huang on China**: called full export ban "completely ridiculous"; warned of accelerating China's independent tech ecosystem. Trump-Xi summit (ended 5/15) did **not** address semis; China reportedly rejecting H200 imports to favor domestic chip development. Consensus and management guidance exclude China DC revenue — any inclusion = material surprise.
- Hyperscaler aggregate capex raised to **$725B**; cloud-wide $830B in 2026 (~75% AI-specific). Direct read-through for AVGO + NVDA; capital-intensity question still for MSFT/META/GOOGL but mitigated by Q1 prints.
- NVDA market cap surpassed $5.7T on 5/16.
- **Bull stance**: WAIT. Earnings window blocking entry; strategy caveat (≥1 -3% red day on AI sleeve before completing tranches) remains in force post-print. Re-evaluate Thu 5/21 01-pre-market.

**Quant pulse (yfinance, prior-session close):**
- All 9 strategy names: fundamentals within 1 decimal of 5/15 read. **No thesis-break flags.**
- NVDA at 95.26% of 52w-Hi (vs 99.1% on 5/14 — pulled back from the high but still elevated).
- GOOGL at 98.29% of 52w-Hi; MSFT 75.96% (deep DD still); META 77.14% (capex-fear DD still).
- All in-window earnings flags: **only NVDA**. AVGO 2026-06-03 (12 td out, clean).
- SPY 98.62% of 52w-Hi at $739.17.

**No thesis-break events on any of the 8 holdings; no entry triggers fired for new names. NVDA wait + T3 defer both still binding.**

**Cited sources:** Gemini Search-Grounding (Warsh confirmation + bio, NVDA consensus, analyst PTs, Jensen comments, SK Hynix sales, hyperscaler capex). yfinance for quant. See `memory/daily/2026-05-18.md` for portfolio detail.

---

## 2026-05-19 — Pre-market (KW 21 Day 2, NVDA earnings T-1)

**Macro (Gemini):**
- **10Y yield 4.61%** (up ~4 bp from 5/15's 4.57%, 12 bp from 5/14). DXY 99.23 — 5-week high holds. Brent ~$110, WTI ~$103 — both off -1.5% overnight on Trump calling off planned Iran strike.
- **Pre-market futures red**: S&P -0.23 to -0.40%, Nasdaq leading lower on tech sell-off, Dow -0.15 to -0.7%. Chip names (NVDA -1%, MU, STX, WDC) all under pressure into NVDA print.
- **FOMC minutes** from Warsh-pre-handover meeting expected this week; market-implied Fed rate-hike-in-2026 probabilities have ticked up. Some sell-side warning 10Y could test 5.5% on hawkish minutes.
- **BRK exited UNH stake** — material headline for BRK.B (positive-to-neutral, derisking from a stressed name). BRK.B itself +1.18% on Mon, no thesis impact.

**NVDA pre-earnings preview (Gemini, earnings Wed 5/20 post-close):**
- Q1 FY27 consensus: rev **$78-79.2B** (whispers $80B+, NVDA's own guide $78B ±2%), EPS **$1.77-1.78**, data center **~$73B** (>90% of total sales). Blackwell ramp + hyperscaler demand the focus.
- **Q2 FY27 guidance is the bigger catalyst than the Q1 print** — consensus $85-87B, whispers $90B. >$87B confirms acceleration; <$85B = deceleration flag.
- **5/18 PT raises**: DA Davidson **$300 (from $250)**, Morgan Stanley **$285 (from $260)**, KeyBanc **$300 (from $275)**, Wedbush reiterates $300. Net hawkish flow; B of A $320 / Susquehanna $275 / UBS $275 still standing from earlier.
- **Options market pricing 8-10% post-earnings move.** Stock has fallen after 4 of last 5 prints — high bar.
- **Bull stance unchanged: WAIT.** Earnings-window guardrail #8 blocking entry; strategy caveat ≥1 -3% red day NOT yet triggered (pre-mkt -1%). Re-evaluate Thu 5/21 01-pre-market post-print.

**Quant pulse (yfinance, prior-session close):**
- All 9 strategy names: fundamentals (fwd P/E, op margin, beta) within 1 decimal of 5/18. **No thesis-break flags.**
- Day-over-day notable moves: **AVGO -1.05%** (2nd consecutive red day; cushion tightest in book at ~5.2%, still inside design band), **NVDA -1.33%** (pullback into print, %52w-Hi 95.26% → 93.99%), **LLY -1.67%** (lone defensive red name, cushion ~7%, beta 0.48 role intact). Best: V +2.11%, BRK-B +1.18%, MSFT +0.38%.
- Earnings-window check: **only NVDA** (5/20). AVGO 2026-06-03 now 11 td out (still clean of guardrail #8).
- T3 DCA: deferred per Robin Option B; next re-evaluation Thu 2026-05-21.

**No thesis-break events on any of the 8 holdings; no entry triggers fired for new names. NVDA WAIT + T3 defer both still binding. Bias = inaction.**

**Cited sources:** Gemini Search-Grounding (10Y/DXY/oil levels, pre-market futures, NVDA consensus, 5/18 PT actions, BRK-UNH exit headline). yfinance for quant. See `memory/daily/2026-05-19.md` for portfolio detail.

---

## 2026-05-20 — Pre-market (KW 21 Day 3, NVDA earnings T-0 PM; **LAST LIVE-PHASE DAY**)

**Phase note:** Today is the final Live-Phase routine (Core-only). Tomorrow 5/21 the date sentinel flips Bull to Learning-Month mode (all 5 sleeves active, sleeve-specific ALM rules).

**Macro (Gemini):**
- **10Y yield 4.64%** (-3 bp intraday from 4.67%, +3 bp vs Mon 4.61%). 16-month high of 4.687% still in the rear-view. Elevated borrowing-cost concern persists.
- **DXY 99.38** — six-week highs; USD strength reflects inflation & rate-hike repricing.
- **Brent $110.15** (-1%), **WTI $103.30** (-1.1%). Strait of Hormuz disruption ongoing; Citi bullish PT $150.
- **Pre-mkt futures GREEN**: S&P +0.15%, Nasdaq +0.4%. NVDA +1.3% pre-mkt into print. Potential snap of 3-day losing streak.
- **FOMC minutes today 18:00Z** — last Powell-era meeting (Apr 28-29), four dissents (most since 1992). Warsh formally starts as Chair Fri 5/22. Vice Chair Barr speaks today.
- **Geo:** US-Iran conflict / Strait of Hormuz / Xi-Putin in Beijing today. Tail-risk maintained, no new catalyst.
- **Macro risk-off triggers (SPY -3%/day OR VIX > 40): NEITHER fired.** Pre-mkt tape green.

**NVDA print (tonight post-close):**
- Q1 FY27 consensus rev ~$78B (whispers $79-80B+), EPS $1.77, DC ~$73B. >$80B revenue clears whisper bar.
- **Q2 FY27 guidance is the bigger catalyst:** consensus $85-87B, whispers $90B. >$87B = clean acceleration; <$85B = deceleration flag.
- **Options-implied move 8-10%.** NVDA shares +1.3% pre-mkt; -4.67% cumulative over last 5 sessions vs 5/15 close $231.42 → $220.61 (no single -3% day — max single-session was -1.33% on 5/19).
- Standing PT raises (5/18): DA Davidson $300, Morgan Stanley $285, KeyBanc $300, Wedbush $300 reiterate, BofA $320 standing. Net hawkish flow.
- **Bull stance: WAIT.** Entry blocked by guardrail #8 today; minimum re-entry window opens 2026-05-23 (3 td post-print). Per `strategy.md` v3 flip on 5/21, NVDA re-evaluation moves to Swing-sleeve framework (not Core-add) — first eval on Thu 5/21 01-pre-market under Learning-Month rules.

**Quant pulse (yfinance, pre-open):**
- All 9 strategy names: fundamentals (fwd P/E, op margin, beta) within 1 decimal of 5/19. **No thesis-break flags.**
- Overnight tape: **AVGO recovered +1.86%** (broker mark $410.02 → $417.65), breaking 4-day red streak; cushion 2.90% → 4.68%. **LLY +0.62%** new HWM $1023.29; trail stop auto-advanced $920.54 → $920.96 (+10.00% fresh cushion). All other names within ±0.6% of Tue close.
- Earnings-window check: **only NVDA** (today PM). AVGO 2026-06-03 now 10 td out (still clean of guardrail #8). All other held names > 6 weeks out.
- T3 DCA: deferred per Robin Option B (5/16); per `strategy.md` v3 frozen-Core rule effective 5/21, T3 is implicitly suspended until 6/21+ unless Robin overrides.

**No thesis-break events on any of the 8 holdings; no entry triggers fired for new names. NVDA WAIT + T3 defer both still binding. Bias = inaction. 10th consecutive no-action routine.**

**Cited sources:** Gemini Search-Grounding (10Y/DXY/oil levels, pre-mkt futures, NVDA Q1+Q2 consensus & whispers, options-implied move, FOMC-minutes context, geo-risk). yfinance for quant + earnings calendar. Alpaca broker for pre-mkt position marks. See `memory/daily/2026-05-20.md` for portfolio detail.

---

## 2026-05-27 — Pre-market (LM Day 7 of 30, Wed)

**Macro (Gemini, 1 grounded query):**
- **10Y yield 4.46-4.47%** (-2 bp vs Tue 4.49%; 2-week low).
- **DXY 99.08-99.11** (~-0.06 to -0.1% intraday).
- **Brent ~$94-97 (-0.5 to -3%); WTI ~$90-93 (-0.9 to -4%)** — US-Iran peace-
  talks optimism dismantling energy.
- **Pre-mkt futures GREEN**: S&P +0.1 to +0.28%, Nasdaq flat to +0.45%,
  Dow +0.2 to +0.43%. VIX 16-17 (fading toward 16).
- **PCE+GDP Thu 5/28 12:30Z** confirmed (Fed-preferred inflation + Q1 GDP
  2nd estimate; Q1 advance was 2.0% annualized). No FOMC/CPI/PPI/NFP next 5d.
- **AVGO earnings Wed 6/3 post-close**: consensus rev $22.08B, EPS $2.40
  (AI-semi tailwind).
- **AAPL**: BofA PT $330 → $380, citing AI roadmap; WWDC June 8-12. Record
  intraday $311.82 fresh 52w-Hi Tue, but closed -1.10% lower → mechanical
  rejection candle (close < open at 52w-Hi).

**Quant pulse (Polygon prev-day aggregates + yfinance fundamentals + Alpaca live mark):**
- SPY 750.59 (+0.65% Tue), QQQ 730.28 (tech-led rally).
- Core 8: VOO HWM walked +0.35% to $691.51 (stop $622.36); LLY HWM walked
  +1.08% to $1,081.94 (stop $973.75). 6 other Core trails unchanged; AVGO
  intraday H $435.31 < prior HWM $442.36 → no walk despite +3.23% UPL.
  All 10 GTC stops verified `OrderStatus.NEW`.
- Tightest Core cushion **flipped from AVGO 3.87% (Mon) → GOOGL 4.85% (Wed)**
  as AVGO ripped +$13.46 Tue.
- Swing NVDA: Tue O=216.54 / H=218.18 / L=212.00 / C=214.86 on **187M shares**
  (3× normal); intraday low cushion 1.45% but closed at 2.94%. Time-stop 6/2
  (4 td).
- Swing RL: Tue O=385 / H=392.10 / L=381.04 / C=381.78 on 0.95M shares; UPL
  flipped from +0.20% (Mon) to +2.02% (Wed live $384.65).
- **ARM new candidate** (`swing-momentum-breakout`): Tue close **$321.22**
  cleared $310 watch band; vol 10.9M elevated. 52w-Hi $325 only +1.2% above.
- **AMD new candidate** (`swing-momentum-breakout`): Tue close **$503.89**,
  fresh 52w-Hi $506.96 intraday on 38.5M vol (+4% on day). Fwd P/E 38 rich.
- **AAPL** (`swing-short-rejection`): mechanical trigger valid (52w-Hi +
  close-below-open), but BofA $380 PT raise + WWDC catalyst vetoes via
  ALM-6 short-thesis-required filter. **SKIP**.

**Polygon ops** (LM Day 7):
- Gainers/losers scanner: **403 Forbidden** (6th re-test consistently gated).
- Daily aggregates: 200 OK on first 5 calls then 429; sufficient for next-day
  watchlist.
- Options snapshot: **403 Forbidden** (5th re-test, NVDA Jun chain). Reference-
  contracts endpoint: 200 OK but no IV/Greeks/quotes (insufficient).

**Crypto scan (yfinance 220d, computed 50/200 DMA)**:
- BTC -3.73% gap (Tue -3.95% → +0.22 pp; convergence resumed); ETH -10.58%;
  SOL -18.38%; AVAX -15.00%; LINK -12.01%. 0/5 cross-up; 0/5 -10% flush.
  At Wed pace (~+0.22 pp/d), BTC ~17 td to neutral cross.

**Strategic read**:
- Tape today is "peace-trade risk-on": oil -3-4%, 10Y -2 bp, futures +0.2%,
  VIX <17. Supportive for tech / AI sleeve; reduced hedge urgency into PCE Thu.
- AVGO Tue ripped pre-earnings froth ($435 intraday H); 4 td to print. Core
  frozen → no action. Strangle blocked by Polygon chain.
- NVDA two-way coin-flip into Wed: 187M-share distribution day or capitulation
  bottom. Cushion 2.94% from stop; close-decision window 6/2.
- ARM + AMD momentum-breakout candidates queued for 02 with confirmation
  triggers ($325 ARM / $507 AMD). Both Swing $1.5k notional / -5 to -6% stops.
- AAPL short-rejection veto'd by BofA PT $380 + WWDC narrative — re-watch
  if 2nd consecutive 52w-Hi rejection prints + PT flow reverses.

**No thesis-break events on any 8 Core holdings; 2 Swing legs HOLD per
tighten-rules; 2 new Swing-momentum candidates conditional on 02 confirmation;
short-rejection vetoed; crypto + options sleeves dormant.**

**Cited sources:** Gemini Search-Grounding (macro levels, pre-mkt futures, oil,
PCE/GDP timing, AAPL BofA PT raise, AVGO earnings consensus). Polygon prev-day
aggregates (15 names; gainers/losers + options snapshots gated 403). yfinance
for fundamentals + crypto 220d history. Alpaca broker (paper endpoint verified)
for account + positions + open-stop status. See `memory/daily/2026-05-27.md`
for full per-sleeve detail.
