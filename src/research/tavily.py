"""Tavily search module — used only for deep_research() cross-validation.

Why this is NOT the default:
    Tavily returns raw snippets. Synthesis is left to Opus, which costs more tokens
    than Gemini's grounded synthesis. So we use Tavily strategically:
    - As a SECOND opinion to Gemini for high-stakes decisions
    - When Gemini's answer is ambiguous and we want raw source snippets

Free tier: 1000 requests/month. We use < 50/month for cross-validation only.

API docs: https://docs.tavily.com/
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path

import httpx


CACHE_DIR = Path(__file__).resolve().parents[2] / "memory" / ".tavily_cache"
CACHE_TTL_SECONDS = 4 * 60 * 60  # 4 hours

API_URL = "https://api.tavily.com/search"


@dataclass
class TavilyResult:
    answer: str  # Tavily's synthesized answer (when include_answer=advanced)
    snippets: list[dict]  # list of {title, url, content, score}
    cached: bool


def _cache_key(query: str, topic: str, depth: str) -> str:
    raw = f"{topic}::{depth}::{query}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:32]


def _read_cache(key: str) -> TavilyResult | None:
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
    return TavilyResult(
        answer=data.get("answer", ""),
        snippets=data.get("snippets", []),
        cached=True,
    )


def _write_cache(key: str, result: TavilyResult) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{key}.json"
    path.write_text(
        json.dumps(
            {
                "answer": result.answer,
                "snippets": result.snippets,
                "timestamp": time.time(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def search(
    query: str,
    *,
    topic: str = "news",  # "news" | "general" | "finance" (if available)
    search_depth: str = "advanced",  # "basic" | "advanced"
    max_results: int = 5,
    days: int = 7,  # only for topic=news
    use_cache: bool = True,
    timeout: float = 60.0,
) -> TavilyResult:
    """Tavily search with sensible defaults for trading research.

    Returns synthesized answer + ranked snippets. Use sparingly — Gemini is the default.
    """
    key = _cache_key(query, topic, search_depth)
    if use_cache:
        hit = _read_cache(key)
        if hit is not None:
            return hit

    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        raise RuntimeError("TAVILY_API_KEY env var not set")

    payload = {
        "api_key": api_key,
        "query": query,
        "topic": topic,
        "search_depth": search_depth,
        "include_answer": "advanced",
        "max_results": max_results,
    }
    if topic == "news":
        payload["days"] = days

    with httpx.Client(timeout=timeout) as client:
        response = client.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()

    result = TavilyResult(
        answer=data.get("answer", "") or "",
        snippets=[
            {
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "content": r.get("content", ""),
                "score": r.get("score", 0),
            }
            for r in data.get("results", [])
        ],
        cached=False,
    )
    _write_cache(key, result)
    return result


def _main_smoke_test() -> None:
    """Run: python -m src.research.tavily "your question here"."""
    import sys

    from rich import print as rprint

    from src.utils.env import load_local_env
    load_local_env()

    query = " ".join(sys.argv[1:]) or "NVDA latest earnings reaction"
    print(f"Query: {query}\n")
    r = search(query)
    rprint(f"[cached={r.cached}]")
    rprint(f"[bold]Answer:[/bold] {r.answer}\n")
    rprint("[bold]Top snippets:[/bold]")
    for s in r.snippets[:3]:
        rprint(f"  • [{s['score']:.2f}] {s['title']}")
        rprint(f"    {s['url']}")


if __name__ == "__main__":
    _main_smoke_test()
