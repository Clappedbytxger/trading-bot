"""Fundamentals module — yfinance-backed, zero-cost, hallucination-free.

Search APIs (Gemini, Tavily, Perplexity) can hallucinate numbers. For anything
quantitative, use this module. It pulls directly from Yahoo Finance.

Caveats:
    - yfinance is an unofficial Yahoo scraper. Occasionally a field returns None or
      stale data. Always handle that gracefully.
    - Rate-limit yourself: don't call >5 tickers/second. We use a 30-min in-memory
      cache per ticker to be polite.

Usage:
    from src.research.fundamentals import get_snapshot, get_earnings_date
    snap = get_snapshot("AAPL")
    print(snap.price, snap.pe_ratio, snap.market_cap)
"""
from __future__ import annotations

import datetime as dt
import time
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

_TTL_SECONDS = 30 * 60  # 30 minutes
_cache: dict[str, tuple[float, Any]] = {}


def _cached(key: str, builder):
    now = time.time()
    if key in _cache:
        ts, val = _cache[key]
        if now - ts < _TTL_SECONDS:
            return val
    val = builder()
    _cache[key] = (now, val)
    return val


def _d(value: Any) -> Decimal | None:
    if value is None:
        return None
    try:
        return Decimal(str(value))
    except (ValueError, ArithmeticError):
        return None


@dataclass
class FundamentalsSnapshot:
    ticker: str
    company_name: str | None
    sector: str | None
    industry: str | None
    price: Decimal | None
    market_cap: Decimal | None
    pe_ratio: Decimal | None  # trailing
    forward_pe: Decimal | None
    profit_margin: Decimal | None
    operating_margin: Decimal | None
    revenue_growth_yoy: Decimal | None
    eps_growth_yoy: Decimal | None
    debt_to_equity: Decimal | None
    free_cashflow: Decimal | None
    return_on_equity: Decimal | None
    return_on_assets: Decimal | None
    fifty_two_week_low: Decimal | None
    fifty_two_week_high: Decimal | None
    dividend_yield: Decimal | None
    beta: Decimal | None
    raw_info: dict[str, Any] = field(default_factory=dict, repr=False)


def get_snapshot(ticker: str) -> FundamentalsSnapshot:
    """Get the most-requested fundamentals in one call. Cached 30 min."""
    def _build() -> FundamentalsSnapshot:
        import yfinance as yf

        info = yf.Ticker(ticker).info or {}
        return FundamentalsSnapshot(
            ticker=ticker.upper(),
            company_name=info.get("longName") or info.get("shortName"),
            sector=info.get("sector"),
            industry=info.get("industry"),
            price=_d(info.get("currentPrice") or info.get("regularMarketPrice")),
            market_cap=_d(info.get("marketCap")),
            pe_ratio=_d(info.get("trailingPE")),
            forward_pe=_d(info.get("forwardPE")),
            profit_margin=_d(info.get("profitMargins")),
            operating_margin=_d(info.get("operatingMargins")),
            revenue_growth_yoy=_d(info.get("revenueGrowth")),
            eps_growth_yoy=_d(info.get("earningsGrowth")),
            debt_to_equity=_d(info.get("debtToEquity")),
            free_cashflow=_d(info.get("freeCashflow")),
            return_on_equity=_d(info.get("returnOnEquity")),
            return_on_assets=_d(info.get("returnOnAssets")),
            fifty_two_week_low=_d(info.get("fiftyTwoWeekLow")),
            fifty_two_week_high=_d(info.get("fiftyTwoWeekHigh")),
            dividend_yield=_d(info.get("dividendYield")),
            beta=_d(info.get("beta")),
            raw_info=info,
        )

    return _cached(f"snapshot::{ticker.upper()}", _build)


def get_earnings_date(ticker: str) -> dt.date | None:
    """Next scheduled earnings date for ticker. Returns None if unknown."""
    def _build() -> dt.date | None:
        import yfinance as yf

        try:
            cal = yf.Ticker(ticker).calendar
        except Exception:
            return None
        if not cal:
            return None
        # yfinance returns either dict-like or DataFrame depending on version
        earnings = None
        if isinstance(cal, dict):
            earnings = cal.get("Earnings Date")
        else:
            try:
                earnings = cal.loc["Earnings Date"].iloc[0]
            except Exception:
                earnings = None
        if earnings is None:
            return None
        if isinstance(earnings, list) and earnings:
            earnings = earnings[0]
        try:
            return dt.date.fromisoformat(str(earnings)[:10])
        except ValueError:
            return None

    return _cached(f"earnings::{ticker.upper()}", _build)


def is_in_earnings_window(ticker: str, *, trading_days: int = 3) -> bool:
    """True if ticker has earnings within next `trading_days` trading days.

    Used by guardrail: no new positions within 3 trading days of earnings.
    """
    earnings = get_earnings_date(ticker)
    if earnings is None:
        return False  # unknown — let other guardrails handle it
    delta = (earnings - dt.date.today()).days
    # Rough conversion: 3 trading days ~= 5 calendar days
    return 0 <= delta <= max(trading_days + 2, 5)


def get_price(ticker: str) -> Decimal | None:
    """Quick price lookup. Uses snapshot cache."""
    return get_snapshot(ticker).price


def get_recent_news(ticker: str, *, limit: int = 5) -> list[dict[str, str]]:
    """Recent news headlines for ticker. Use as a quick scan — Gemini for deep coverage."""
    import yfinance as yf

    try:
        items = yf.Ticker(ticker).news or []
    except Exception:
        return []

    result: list[dict[str, str]] = []
    for item in items[:limit]:
        content = item.get("content") or item
        result.append(
            {
                "title": content.get("title", ""),
                "publisher": content.get("provider", {}).get("displayName", "")
                if isinstance(content.get("provider"), dict)
                else content.get("publisher", ""),
                "link": (content.get("canonicalUrl", {}) or {}).get("url", "")
                if isinstance(content.get("canonicalUrl"), dict)
                else content.get("link", ""),
                "published": str(content.get("pubDate") or content.get("providerPublishTime", "")),
            }
        )
    return result


def _main_smoke_test() -> None:
    """Run: python -m src.research.fundamentals AAPL."""
    import sys

    from rich import print as rprint

    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    snap = get_snapshot(ticker)
    rprint("[bold]Snapshot:[/bold]", snap)
    rprint("[bold]Next earnings:[/bold]", get_earnings_date(ticker))
    rprint("[bold]In earnings window (3d):[/bold]", is_in_earnings_window(ticker))
    rprint("[bold]Recent news:[/bold]")
    for n in get_recent_news(ticker, limit=3):
        rprint(f"  - {n['title']} ({n['publisher']})")


if __name__ == "__main__":
    _main_smoke_test()
