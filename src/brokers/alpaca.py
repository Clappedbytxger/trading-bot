"""Alpaca adapter — used for Phase 1 paper trading.

Reads credentials from env vars: ALPACA_API_KEY_ID, ALPACA_API_SECRET_KEY, ALPACA_BASE_URL.
Default base URL targets the paper endpoint.
"""
from __future__ import annotations

import os
from decimal import Decimal

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide as AlpacaSide
from alpaca.trading.enums import TimeInForce as AlpacaTif
from alpaca.trading.requests import (
    LimitOrderRequest,
    MarketOrderRequest,
    StopLimitOrderRequest,
    StopOrderRequest,
    TrailingStopOrderRequest,
)

from .base import (
    Account,
    BrokerAdapter,
    Clock,
    Order,
    OrderResult,
    Position,
)


def _d(value: float | str | None) -> Decimal:
    """Coerce Alpaca's mix of float/str into Decimal safely."""
    if value is None:
        return Decimal("0")
    return Decimal(str(value))


class AlpacaAdapter(BrokerAdapter):
    name = "alpaca"

    def __init__(self) -> None:
        key = os.environ["ALPACA_API_KEY_ID"]
        secret = os.environ["ALPACA_API_SECRET_KEY"]
        base_url = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
        paper = "paper" in base_url
        self._trading = TradingClient(key, secret, paper=paper, url_override=base_url)
        self._data = StockHistoricalDataClient(key, secret)

    def get_account(self) -> Account:
        a = self._trading.get_account()
        return Account(
            cash=_d(a.cash),
            equity=_d(a.equity),
            buying_power=_d(a.buying_power),
            currency=a.currency or "USD",
        )

    def get_positions(self) -> list[Position]:
        positions = self._trading.get_all_positions()
        result: list[Position] = []
        for p in positions:
            result.append(
                Position(
                    symbol=p.symbol,
                    qty=_d(p.qty),
                    avg_entry_price=_d(p.avg_entry_price),
                    current_price=_d(p.current_price),
                    market_value=_d(p.market_value),
                    unrealized_pl=_d(p.unrealized_pl),
                    unrealized_pl_pct=_d(p.unrealized_plpc) * Decimal("100"),
                )
            )
        return result

    def get_clock(self) -> Clock:
        c = self._trading.get_clock()
        return Clock(
            is_open=bool(c.is_open),
            next_open=c.next_open.isoformat() if c.next_open else "",
            next_close=c.next_close.isoformat() if c.next_close else "",
        )

    def get_last_price(self, symbol: str) -> Decimal:
        req = StockLatestTradeRequest(symbol_or_symbols=symbol)
        trades = self._data.get_stock_latest_trade(req)
        return _d(trades[symbol].price)

    def place_order(self, order: Order) -> OrderResult:
        if order.qty is None and order.notional is None:
            raise ValueError("Order needs either qty or notional")
        if order.qty is not None and order.notional is not None:
            raise ValueError("Order can't have both qty and notional")

        side = AlpacaSide.BUY if order.side == "buy" else AlpacaSide.SELL
        tif = AlpacaTif.DAY if order.time_in_force == "day" else AlpacaTif.GTC

        common = {
            "symbol": order.symbol,
            "side": side,
            "time_in_force": tif,
            "client_order_id": order.client_order_id,
        }
        if order.qty is not None:
            common["qty"] = float(order.qty)
        else:
            common["notional"] = float(order.notional)

        if order.order_type == "market":
            req = MarketOrderRequest(**common)
        elif order.order_type == "limit":
            if order.limit_price is None:
                raise ValueError("limit order requires limit_price")
            req = LimitOrderRequest(limit_price=float(order.limit_price), **common)
        elif order.order_type == "stop":
            if order.stop_price is None:
                raise ValueError("stop order requires stop_price")
            req = StopOrderRequest(stop_price=float(order.stop_price), **common)
        elif order.order_type == "stop_limit":
            if order.stop_price is None or order.limit_price is None:
                raise ValueError("stop_limit requires both stop_price and limit_price")
            req = StopLimitOrderRequest(
                stop_price=float(order.stop_price),
                limit_price=float(order.limit_price),
                **common,
            )
        elif order.order_type == "trailing_stop":
            if order.trail_percent is None:
                raise ValueError("trailing_stop requires trail_percent")
            req = TrailingStopOrderRequest(
                trail_percent=float(order.trail_percent), **common
            )
        else:
            raise ValueError(f"Unsupported order type: {order.order_type}")

        submitted = self._trading.submit_order(req)
        return OrderResult(
            broker_order_id=str(submitted.id),
            status=str(submitted.status),
            submitted_at=submitted.submitted_at.isoformat() if submitted.submitted_at else "",
            filled_qty=_d(submitted.filled_qty) if submitted.filled_qty else None,
            filled_avg_price=_d(submitted.filled_avg_price) if submitted.filled_avg_price else None,
        )

    def cancel_order(self, broker_order_id: str) -> None:
        self._trading.cancel_order_by_id(broker_order_id)


def _main_smoke_test() -> None:
    """Run: python -m src.brokers.alpaca — prints account + positions."""
    from rich import print as rprint

    from src.utils.env import load_local_env
    load_local_env()

    adapter = AlpacaAdapter()
    rprint("[bold]Account:[/bold]", adapter.get_account())
    rprint("[bold]Clock:[/bold]", adapter.get_clock())
    rprint("[bold]Positions:[/bold]", adapter.get_positions())


if __name__ == "__main__":
    _main_smoke_test()
