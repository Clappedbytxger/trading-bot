"""Perplexity Sonar-Pro wrapper with local 4h JSON cache.

Why cached: routines fire 5x/day, often researching the same tickers. Cache key is
the prompt hash + model. TTL keeps results fresh enough for market-relevant info.

Why we don't use Claude's native web_search: token cost. Perplexity returns synthesized
answers (already grounded with citations) for far fewer tokens than dumping raw search
results into Opus's context.

Usage:
    from src.research.perplexity import research
    answer = research("Latest NVDA earnings reaction and forward guidance")
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path

import httpx


CACHE_DIR = Path(__file__).resolve().parents[2] / "memory" / ".perplexity_cache"
CACHE_TTL_SECONDS = 4 * 60 * 60  # 4 hours

API_URL = "https://api.perplexity.ai/chat/completions"
DEFAULT_MODEL = "sonar-pro"


@dataclass
class ResearchResult:
    answer: str
    citations: list[str]
    cached: bool
    model: str


def _cache_key(prompt: str, model: str) -> str:
    raw = f"{model}::{prompt}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:32]


def _read_cache(key: str) -> ResearchResult | None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{key}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if time.time() - data.get("timestamp", 0) > CACHE_TTL_SECONDS:
        return None
    return ResearchResult(
        answer=data["answer"],
        citations=data.get("citations", []),
        cached=True,
        model=data.get("model", DEFAULT_MODEL),
    )


def _write_cache(key: str, result: ResearchResult) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{key}.json"
    path.write_text(
        json.dumps(
            {
                "answer": result.answer,
                "citations": result.citations,
                "model": result.model,
                "timestamp": time.time(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def research(
    prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    system: str | None = None,
    use_cache: bool = True,
    timeout: float = 60.0,
) -> ResearchResult:
    """Query Perplexity Sonar-Pro for synthesized, citation-backed research.

    Args:
        prompt: The research question, e.g. "Latest macro outlook for US large-cap tech".
        model: sonar-pro (default), sonar, sonar-reasoning, sonar-deep-research.
        system: Optional system instruction (e.g. "Focus on fundamentals only").
        use_cache: Skip cache if False (e.g. when you NEED a live answer).

    Returns:
        ResearchResult with .answer (markdown) and .citations (URLs).
    """
    key = _cache_key(prompt + (system or ""), model)
    if use_cache:
        hit = _read_cache(key)
        if hit is not None:
            return hit

    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        raise RuntimeError("PERPLEXITY_API_KEY env var not set")

    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.2,
    }

    with httpx.Client(timeout=timeout) as client:
        response = client.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
        )
        response.raise_for_status()
        data = response.json()

    answer = data["choices"][0]["message"]["content"]
    citations = data.get("citations", [])

    result = ResearchResult(answer=answer, citations=citations, cached=False, model=model)
    _write_cache(key, result)
    return result


def _main_smoke_test() -> None:
    """Run: python -m src.research.perplexity "your question here"."""
    import sys

    from src.utils.env import load_local_env
    load_local_env()

    query = " ".join(sys.argv[1:]) or "Latest macro outlook for US large-cap tech, 2 sentences."
    print(f"Query: {query}\n")
    r = research(query)
    print(f"[cached={r.cached}] {r.answer}\n")
    print("Citations:")
    for c in r.citations:
        print(f"  - {c}")


if __name__ == "__main__":
    _main_smoke_test()
