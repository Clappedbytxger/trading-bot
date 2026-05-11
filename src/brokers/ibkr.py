"""IBKR adapter — Phase 2 (live trading via IB Gateway on VPS).

Not implemented yet. Build in week 4 once Alpaca-Paper strategy is validated.
Connection model: IB Gateway runs on a Hetzner VPS in headless mode (controlled by IBC
for auto-relogin). This adapter connects via ib-async over the VPS host:port.

Required env vars when activated:
    IBKR_GATEWAY_HOST, IBKR_GATEWAY_PORT, IBKR_CLIENT_ID, IBKR_ACCOUNT_ID

Implementation outline (TODO):
    from ib_async import IB, Stock, MarketOrder, LimitOrder, StopOrder
    self._ib = IB()
    self._ib.connect(host, port, clientId=client_id)
    # implement get_account, get_positions, place_order, etc. mirroring base.py
"""
from __future__ import annotations

from decimal import Decimal

from .base import Account, BrokerAdapter, Clock, Order, OrderResult, Position


class IbkrAdapter(BrokerAdapter):
    name = "ibkr"

    def __init__(self) -> None:
        raise NotImplementedError(
            "IBKR adapter is Phase 2 work. Build after Alpaca-Paper validation. "
            "See plans/ich-kreire-dich-als-eventual-spring.md for the migration plan."
        )

    def get_account(self) -> Account: ...
    def get_positions(self) -> list[Position]: ...
    def get_clock(self) -> Clock: ...
    def place_order(self, order: Order) -> OrderResult: ...
    def cancel_order(self, broker_order_id: str) -> None: ...
    def get_last_price(self, symbol: str) -> Decimal: ...
