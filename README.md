# Bull — 24/7 AI Trading Bot

Long-term investment bot powered by Claude Opus 4.7 routines. Targets beating the S&P 500
via fundamentals-driven quality-growth picks in US stocks + ETFs.

## Quick Start

See [`SETUP.md`](./SETUP.md) for the full manual onboarding (API keys, GitHub, Claude
Cloud Environment, Routines).

## Architecture

- **Scheduler:** Claude Code Remote Routines (Cloud, cron-based)
- **Brain:** Claude Opus 4.7 (`claude-opus-4-7`)
- **Research:**
  - Numbers → yfinance (free, hallucination-free)
  - Qualitative → Gemini 2.5 Flash with Google Search Grounding (free tier, 1500 req/day)
  - High-stakes cross-validation → Tavily (free tier, used for `deep_research()` only)
- **Broker:** Alpaca Paper (Phase 1) → Interactive Brokers (Phase 2 live, via VPS)
- **Notifications:** CallMeBot WhatsApp (German summaries)
- **Memory:** File-based, GitHub-persisted, auto-committed after each routine

## Routines (Mon–Fri, US Market Hours)

| Routine | DE-Time | WhatsApp |
|---|---|---|
| `01-pre-market` | 14:00 | — |
| `02-market-open` | 15:30 | YES |
| `03-midday` | 18:30 | — |
| `04-pre-close` | 21:30 | — |
| `05-close-summary` | 22:15 | YES |
| `06-weekly-review` | Fri 22:30 | YES |

Plus one-time `00-strategy-init` to research and propose the initial strategy.

## Hard Guardrails

Encoded in [`CLAUDE.md`](./CLAUDE.md) — max position size, stop-loss, no crypto/forex,
auto-commit memory changes. Read it before touching anything.

## Phase Plan

- **Phase 1 (weeks 1-3):** Alpaca Paper, validate strategy, iterate prompts.
- **Phase 2 (week 4+):** Migrate to IBKR Live on a Hetzner VPS with IB Gateway.

See [`plans/`](https://github.com/) for the full design plan.
