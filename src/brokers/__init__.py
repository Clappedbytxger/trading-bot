"""Broker adapter layer — swap implementations via ACTIVE_BROKER env var."""
import os

from .base import BrokerAdapter


def get_broker() -> BrokerAdapter:
    """Factory — returns the broker adapter selected by ACTIVE_BROKER env var.

    Defaults to alpaca (Phase 1 paper trading).
    """
    active = os.environ.get("ACTIVE_BROKER", "alpaca").lower()
    if active == "alpaca":
        from .alpaca import AlpacaAdapter
        return AlpacaAdapter()
    if active == "ibkr":
        from .ibkr import IbkrAdapter  # noqa: lazy import, ib-async optional
        return IbkrAdapter()
    raise ValueError(f"Unknown ACTIVE_BROKER: {active!r}")
