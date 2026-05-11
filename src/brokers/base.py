"""Abstract broker interface.

All concrete brokers (Alpaca for Phase 1, IBKR for Phase 2) implement these methods.
Keep the surface area small — only what the routines actually need.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from typing import Literal


OrderSide = Literal["buy", "sell"]
OrderType = Literal["market", "limit", "stop", "stop_limit", "trailing_stop"]
TimeInForce = Literal["day", "gtc"]


@dataclass
class Account:
    cash: Decimal
    equity: Decimal
    buying_power: Decimal
    currency: str = "USD"


@dataclass
class Position:
    symbol: str
    qty: Decimal
    avg_entry_price: Decimal
    current_price: Decimal
    market_value: Decimal
    unrealized_pl: Decimal
    unrealized_pl_pct: Decimal


@dataclass
class Order:
    """Submission spec. Set qty OR notional, not both."""
    symbol: str
    side: OrderSide
    qty: Decimal | None = None
    notional: Decimal | None = None
    order_type: OrderType = "market"
    limit_price: Decimal | None = None
    stop_price: Decimal | None = None
    trail_percent: Decimal | None = None
    time_in_force: TimeInForce = "day"
    client_order_id: str | None = None


@dataclass
class OrderResult:
    broker_order_id: str
    status: str
    submitted_at: str
    filled_qty: Decimal | None = None
    filled_avg_price: Decimal | None = None


@dataclass
class Clock:
    is_open: bool
    next_open: str  # ISO timestamp
    next_close: str  # ISO timestamp


class BrokerAdapter(ABC):
    """Minimum surface area shared by all broker backends."""

    name: str

    @abstractmethod
    def get_account(self) -> Account: ...

    @abstractmethod
    def get_positions(self) -> list[Position]: ...

    @abstractmethod
    def get_clock(self) -> Clock: ...

    @abstractmethod
    def place_order(self, order: Order) -> OrderResult: ...

    @abstractmethod
    def cancel_order(self, broker_order_id: str) -> None: ...

    @abstractmethod
    def get_last_price(self, symbol: str) -> Decimal: ...
