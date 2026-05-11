"""Gemini research module — Google Search Grounding for synthesized answers.

Why this is the default (instead of Perplexity):
    Gemini 2.5 Flash has a generous free tier (1500 requests/day) and includes Search
    Grounding — Google's own search engine returns synthesized, citation-backed answers
    similar to Perplexity Sonar-Pro, at $0 cost.

API docs: https://ai.google.dev/gemini-api/docs/grounding

Usage:
    from src.research.gemini import research
    result = research("Latest macro outlook US large-cap tech")
    print(result.answer)
    print(result.citations)
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path


CACHE_DIR = Path(__file__).resolve().parents[2] / "memory" / ".gemini_cache"
CACHE_TTL_SECONDS = 4 * 60 * 60  # 4 hours

DEFAULT_MODEL = "gemini-2.5-flash"


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


def _extract_citations(grounding_metadata) -> list[str]:
    """Pull citation URLs out of Gemini's grounding metadata response."""
    citations: list[str] = []
    if grounding_metadata is None:
        return citations
    chunks = getattr(grounding_metadata, "grounding_chunks", None) or []
    for chunk in chunks:
        web = getattr(chunk, "web", None)
        if web is not None:
            url = getattr(web, "uri", None)
            if url:
                citations.append(url)
    return citations


def research(
    prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    system: str | None = None,
    use_cache: bool = True,
    temperature: float = 0.2,
) -> ResearchResult:
    """Query Gemini with Search Grounding for synthesized, citation-backed research.

    Args:
        prompt: Research question.
        model: gemini-2.5-flash (default, free-tier) or gemini-2.5-pro (paid).
        system: Optional system instruction.
        use_cache: Skip cache if False.
        temperature: 0.2 = focused, 0.7 = more exploratory.

    Returns:
        ResearchResult with .answer (markdown text) and .citations (URLs).
    """
    key = _cache_key(prompt + (system or ""), model)
    if use_cache:
        hit = _read_cache(key)
        if hit is not None:
            return hit

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY env var not set")

    # Lazy import — keeps module importable without google-genai installed for offline tests.
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    config = types.GenerateContentConfig(
        temperature=temperature,
        tools=[types.Tool(google_search=types.GoogleSearch())],
        system_instruction=system,
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=config,
    )

    answer = response.text or ""
    grounding = None
    if response.candidates:
        grounding = getattr(response.candidates[0], "grounding_metadata", None)
    citations = _extract_citations(grounding)

    result = ResearchResult(answer=answer, citations=citations, cached=False, model=model)
    _write_cache(key, result)
    return result


def _main_smoke_test() -> None:
    """Run: python -m src.research.gemini "your question here"."""
    import sys

    from src.utils.env import load_local_env
    load_local_env()

    query = " ".join(sys.argv[1:]) or "Latest macro outlook for US large-cap tech, 2 sentences."
    print(f"Query: {query}\n")
    r = research(query)
    print(f"[cached={r.cached}] [model={r.model}]\n")
    print(r.answer)
    print("\nCitations:")
    for c in r.citations:
        print(f"  - {c}")


if __name__ == "__main__":
    _main_smoke_test()
