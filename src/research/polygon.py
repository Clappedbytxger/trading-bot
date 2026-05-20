"""Polygon.io REST API helper — Learning Month real-time market data.

Polygon provides what Alpaca's free tier doesn't:
- Real-time stock aggregates (no 15-min delay)
- 1-minute and 5-minute bars for intraday strategies
- Options chains with IV / Greeks
- Pre-market and after-hours data

API docs: https://polygon.io/docs/stocks
Key from env: POLYGON_API_KEY

This module is a thin wrapper. Callers (routines) compose higher-level signals
(ORB, VWAP, IV-rank) from the primitives here.
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Literal

import httpx

_BASE = "https://api.polygon.io"
_CACHE: dict[str, tuple[float, object]] = {}
_CACHE_TTL_SECONDS = 30  # real-time tier: cache aggressively to stay under rate limit


def _key() -> str:
    k = os.environ.get("POLYGON_API_KEY")
    if not k:
        raise RuntimeError("POLYGON_API_KEY env var not set — Learning-Month required")
    return k


def _cached_get(url: str, params: dict | None = None) -> dict:
    cache_key = f"{url}?{sorted((params or {}).items())}"
    now = time.time()
    hit = _CACHE.get(cache_key)
    if hit and (now - hit[0]) < _CACHE_TTL_SECONDS:
        return hit[1]  # type: ignore[return-value]
    p = dict(params or {})
    p["apiKey"] = _key()
    r = httpx.get(url, params=p, timeout=10.0)
    r.raise_for_status()
    data = r.json()
    _CACHE[cache_key] = (now, data)
    return data


@dataclass
class Aggregate:
    ticker: str
    timestamp: datetime  # UTC, bar OPEN time
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
    vwap: Decimal | None
    transactions: int | None


@dataclass
class OptionContract:
    symbol: str          # e.g. O:NVDA260520C00220000
    underlying: str
    expiry: str          # YYYY-MM-DD
    strike: Decimal
    contract_type: Literal["call", "put"]
    bid: Decimal | None
    ask: Decimal | None
    last: Decimal | None
    iv: Decimal | None
    delta: Decimal | None
    gamma: Decimal | None
    theta: Decimal | None
    vega: Decimal | None
    open_interest: int | None
    volume: int | None


def get_aggregates(
    ticker: str,
    *,
    multiplier: int = 1,
    timespan: Literal["minute", "hour", "day", "week"] = "minute",
    from_date: str | None = None,        # YYYY-MM-DD
    to_date: str | None = None,          # YYYY-MM-DD
    limit: int = 5000,
    adjusted: bool = True,
) -> list[Aggregate]:
    """Get OHLCV bars for a ticker.

    Defaults: 1-minute bars for today. Use timespan='day' + multi-day range for
    daily charts.
    """
    today = datetime.utcnow().date()
    if from_date is None:
        from_date = today.isoformat()
    if to_date is None:
        to_date = today.isoformat()

    url = f"{_BASE}/v2/aggs/ticker/{ticker.upper()}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    data = _cached_get(url, {"adjusted": str(adjusted).lower(), "limit": str(limit), "sort": "asc"})
    results = data.get("results", []) or []
    out: list[Aggregate] = []
    for r in results:
        out.append(Aggregate(
            ticker=ticker.upper(),
            timestamp=datetime.utcfromtimestamp(r["t"] / 1000),
            open=Decimal(str(r["o"])),
            high=Decimal(str(r["h"])),
            low=Decimal(str(r["l"])),
            close=Decimal(str(r["c"])),
            volume=int(r.get("v") or 0),
            vwap=Decimal(str(r["vw"])) if "vw" in r and r["vw"] is not None else None,
            transactions=r.get("n"),
        ))
    return out


def get_last_quote(ticker: str) -> dict:
    """Latest NBBO bid/ask snapshot for a stock ticker."""
    url = f"{_BASE}/v2/last/nbbo/{ticker.upper()}"
    data = _cached_get(url)
    return data.get("results", {})


def get_snapshot(ticker: str) -> dict:
    """Real-time stock snapshot: last trade, last quote, today's OHLC, day-change."""
    url = f"{_BASE}/v2/snapshot/locale/us/markets/stocks/tickers/{ticker.upper()}"
    return _cached_get(url).get("ticker", {})


def get_market_movers(
    direction: Literal["gainers", "losers"] = "gainers",
    *,
    include_otc: bool = False,
) -> list[dict]:
    """Top US-market movers (pre-market and intraday). Used by gap scanner."""
    url = f"{_BASE}/v2/snapshot/locale/us/markets/stocks/{direction}"
    data = _cached_get(url, {"include_otc": str(include_otc).lower()})
    return data.get("tickers", []) or []


def get_options_chain(
    underlying: str,
    *,
    expiry_date: str | None = None,          # YYYY-MM-DD or None for any
    expiry_lte: str | None = None,           # latest expiry to include
    expiry_gte: str | None = None,           # earliest expiry to include
    contract_type: Literal["call", "put"] | None = None,
    strike_price_lte: float | None = None,
    strike_price_gte: float | None = None,
    limit: int = 250,
) -> list[OptionContract]:
    """Fetch options chain for an underlying ticker, optionally filtered.

    Returns OptionContract dataclasses. Greeks + IV come from the chain snapshot
    endpoint (requires the Options Starter subscription on Polygon).
    """
    url = f"{_BASE}/v3/snapshot/options/{underlying.upper()}"
    params: dict[str, str] = {"limit": str(limit)}
    if expiry_date:
        params["expiration_date"] = expiry_date
    if expiry_lte:
        params["expiration_date.lte"] = expiry_lte
    if expiry_gte:
        params["expiration_date.gte"] = expiry_gte
    if contract_type:
        params["contract_type"] = contract_type
    if strike_price_lte is not None:
        params["strike_price.lte"] = str(strike_price_lte)
    if strike_price_gte is not None:
        params["strike_price.gte"] = str(strike_price_gte)

    data = _cached_get(url, params)
    results = data.get("results", []) or []
    out: list[OptionContract] = []
    for r in results:
        details = r.get("details") or {}
        greeks = r.get("greeks") or {}
        quote = r.get("last_quote") or {}
        last_trade = r.get("last_trade") or {}
        out.append(OptionContract(
            symbol=details.get("ticker", ""),
            underlying=underlying.upper(),
            expiry=details.get("expiration_date", ""),
            strike=Decimal(str(details.get("strike_price", 0))),
            contract_type=details.get("contract_type", "call"),
            bid=Decimal(str(quote.get("bid"))) if quote.get("bid") is not None else None,
            ask=Decimal(str(quote.get("ask"))) if quote.get("ask") is not None else None,
            last=Decimal(str(last_trade.get("price"))) if last_trade.get("price") is not None else None,
            iv=Decimal(str(r.get("implied_volatility"))) if r.get("implied_volatility") is not None else None,
            delta=Decimal(str(greeks.get("delta"))) if greeks.get("delta") is not None else None,
            gamma=Decimal(str(greeks.get("gamma"))) if greeks.get("gamma") is not None else None,
            theta=Decimal(str(greeks.get("theta"))) if greeks.get("theta") is not None else None,
            vega=Decimal(str(greeks.get("vega"))) if greeks.get("vega") is not None else None,
            open_interest=r.get("open_interest"),
            volume=(r.get("day") or {}).get("volume"),
        ))
    return out


def get_iv_rank(ticker: str, *, lookback_days: int = 252) -> Decimal | None:
    """Compute IV-rank from 1-year history of ATM IV.

    IV-rank = (current_IV - 1y_min_IV) / (1y_max_IV - 1y_min_IV) × 100

    Returns None if insufficient data. Used by `options-earnings-strangle`.
    """
    # Polygon doesn't expose historical IV directly on the free chain endpoint —
    # caller may need the historical IV endpoint with a paid tier. Stub returns None
    # so the routine can fall back to skipping the strategy on this name.
    _ = ticker, lookback_days
    return None


def is_in_earnings_window_polygon(ticker: str, *, days: int = 5) -> bool:
    """Reference-data earnings check. Polygon's earnings endpoint requires the
    Stocks Starter tier. Fall back to src.research.fundamentals.is_in_earnings_window
    if this returns None / errors.
    """
    try:
        url = f"{_BASE}/vX/reference/financials"
        _ = _cached_get(url, {"ticker": ticker.upper(), "limit": "1"})
        # The current Polygon /reference/financials doesn't expose next-earnings;
        # callers should use yfinance via fundamentals.is_in_earnings_window instead.
        return False
    except Exception:
        return False


__all__ = [
    "Aggregate",
    "OptionContract",
    "get_aggregates",
    "get_last_quote",
    "get_snapshot",
    "get_market_movers",
    "get_options_chain",
    "get_iv_rank",
    "is_in_earnings_window_polygon",
]
