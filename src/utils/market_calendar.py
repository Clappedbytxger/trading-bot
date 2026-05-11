"""NYSE market calendar helpers.

Uses pandas-market-calendars under the hood. Most routines just need "is today a
trading day?" and "minutes to open/close".
"""
from __future__ import annotations

import datetime as dt
from zoneinfo import ZoneInfo

import pandas_market_calendars as mcal

NYSE = mcal.get_calendar("NYSE")
ET = ZoneInfo("America/New_York")


def is_trading_day(date: dt.date | None = None) -> bool:
    date = date or dt.date.today()
    schedule = NYSE.schedule(start_date=date, end_date=date)
    return not schedule.empty


def next_trading_day(after: dt.date | None = None) -> dt.date:
    after = after or dt.date.today()
    schedule = NYSE.schedule(
        start_date=after + dt.timedelta(days=1),
        end_date=after + dt.timedelta(days=10),
    )
    return schedule.index[0].date()


def minutes_to_open() -> int | None:
    """Minutes until NYSE opens today. None if market is open or no session today."""
    now = dt.datetime.now(tz=ET)
    today = now.date()
    schedule = NYSE.schedule(start_date=today, end_date=today)
    if schedule.empty:
        return None
    open_at = schedule.iloc[0]["market_open"].to_pydatetime().astimezone(ET)
    if now >= open_at:
        return None
    return int((open_at - now).total_seconds() // 60)


def minutes_to_close() -> int | None:
    """Minutes until NYSE closes today. None if market is closed."""
    now = dt.datetime.now(tz=ET)
    today = now.date()
    schedule = NYSE.schedule(start_date=today, end_date=today)
    if schedule.empty:
        return None
    close_at = schedule.iloc[0]["market_close"].to_pydatetime().astimezone(ET)
    open_at = schedule.iloc[0]["market_open"].to_pydatetime().astimezone(ET)
    if now < open_at or now >= close_at:
        return None
    return int((close_at - now).total_seconds() // 60)
