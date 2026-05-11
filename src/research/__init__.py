"""Research facade.

Use these two functions from routines and skills — they pick the right backend
based on the use case.

    from src.research import research, deep_research

    # Default: Gemini with Search Grounding (free, fast, synthesized)
    answer = research("Latest macro outlook for US large-cap tech")
    print(answer.answer)

    # High-stakes only: Gemini + Tavily cross-validation
    consensus = deep_research(
        "Should we open a position in NVDA at current valuation?",
        flag_disagreement=True,
    )
    if consensus.disagreement_detected:
        # Opus should be MORE cautious — sources disagree
        ...

For quantitative data (price, P/E, earnings date) use src.research.fundamentals — never
ask a search API for numbers.
"""
from __future__ import annotations

from dataclasses import dataclass

from .gemini import ResearchResult, research as _gemini_research


@dataclass
class DeepResearchResult:
    gemini_answer: str
    gemini_citations: list[str]
    tavily_answer: str
    tavily_snippets: list[dict]
    disagreement_detected: bool
    disagreement_reason: str  # short explanation when disagreement_detected


def research(prompt: str, *, system: str | None = None, use_cache: bool = True) -> ResearchResult:
    """Default research entry-point. Uses Gemini with Search Grounding."""
    return _gemini_research(prompt, system=system, use_cache=use_cache)


def deep_research(
    prompt: str,
    *,
    system: str | None = None,
    use_cache: bool = True,
    flag_disagreement: bool = True,
) -> DeepResearchResult:
    """Cross-validate research across Gemini + Tavily. Use for high-stakes decisions only.

    Returns both answers. If `flag_disagreement` is True, runs a simple heuristic to
    detect when the two sources point in opposite directions — caller (Opus) can then
    be more cautious.

    Cost: 1 Gemini call (free) + 1 Tavily call (free tier, ~50/month budget).
    """
    from .tavily import search as _tavily_search

    g = _gemini_research(prompt, system=system, use_cache=use_cache)
    t = _tavily_search(prompt, use_cache=use_cache)

    disagreement, reason = _detect_disagreement(g.answer, t.answer) if flag_disagreement else (False, "")

    return DeepResearchResult(
        gemini_answer=g.answer,
        gemini_citations=g.citations,
        tavily_answer=t.answer,
        tavily_snippets=t.snippets,
        disagreement_detected=disagreement,
        disagreement_reason=reason,
    )


# Simple heuristics — Opus will do the real semantic comparison when it reads both.
# This just surfaces obvious cases.
_BULLISH_TOKENS = {"buy", "bullish", "strong buy", "outperform", "upgrade", "beat"}
_BEARISH_TOKENS = {"sell", "bearish", "downgrade", "miss", "underperform", "warn"}


def _detect_disagreement(a: str, b: str) -> tuple[bool, str]:
    if not a or not b:
        return False, ""
    al = a.lower()
    bl = b.lower()

    a_bull = any(tok in al for tok in _BULLISH_TOKENS)
    a_bear = any(tok in al for tok in _BEARISH_TOKENS)
    b_bull = any(tok in bl for tok in _BULLISH_TOKENS)
    b_bear = any(tok in bl for tok in _BEARISH_TOKENS)

    if (a_bull and b_bear and not b_bull) or (a_bear and b_bull and not b_bear):
        return True, "Opposite directional language detected between sources"
    return False, ""


__all__ = [
    "research",
    "deep_research",
    "ResearchResult",
    "DeepResearchResult",
]
