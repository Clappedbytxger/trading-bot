"""Selective memory reader — keeps Opus context lean (token budget < 30k).

Usage from a routine:
    from src.memory.reader import load_core_context
    ctx = load_core_context()
    # ctx is a dict: {"strategy": "...", "portfolio": "...", "lessons": "...",
    #                 "recent_trades": "...", "recent_research": "..."}
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

MEMORY_DIR = Path(__file__).resolve().parents[2] / "memory"

# Token budgets per file (approx chars; 1 token ~= 4 chars on English text)
MAX_CHARS_STRATEGY = 8_000
MAX_CHARS_PORTFOLIO = 4_000
MAX_CHARS_LESSONS = 12_000
MAX_CHARS_TRADE_LOG_TAIL = 8_000  # last N chars only
MAX_CHARS_RESEARCH_TAIL = 12_000  # last 7d, capped


def _read(path: Path, max_chars: int | None = None, tail: bool = False) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if max_chars is None or len(text) <= max_chars:
        return text
    return text[-max_chars:] if tail else text[:max_chars]


def load_core_context() -> dict[str, str]:
    """Load the standard files every routine needs.

    Returns dict with keys: strategy, portfolio, lessons, recent_trades, recent_research,
    watchlist, daily_today, daily_yesterday.
    Missing files return empty strings — caller decides how to react.
    """
    today = dt.date.today().isoformat()
    yesterday = (dt.date.today() - dt.timedelta(days=1)).isoformat()

    return {
        "strategy": _read(MEMORY_DIR / "strategy.md", MAX_CHARS_STRATEGY),
        "portfolio": _read(MEMORY_DIR / "portfolio.md", MAX_CHARS_PORTFOLIO),
        "lessons": _read(MEMORY_DIR / "lessons.md", MAX_CHARS_LESSONS, tail=True),
        "recent_trades": _read(
            MEMORY_DIR / "trade_log.md", MAX_CHARS_TRADE_LOG_TAIL, tail=True
        ),
        "recent_research": _read(
            MEMORY_DIR / "research_log.md", MAX_CHARS_RESEARCH_TAIL, tail=True
        ),
        "watchlist": _read(MEMORY_DIR / "watchlist.md"),
        "daily_today": _read(MEMORY_DIR / "daily" / f"{today}.md"),
        "daily_yesterday": _read(MEMORY_DIR / "daily" / f"{yesterday}.md"),
    }


def is_strategy_locked() -> bool:
    """True if memory/strategy.md does not exist or its frontmatter says locked.

    Until Robin approves a strategy, no trades may be placed.
    """
    path = MEMORY_DIR / "strategy.md"
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8")
    if "version: 0" in text or "approved: false" in text:
        return True
    return False
